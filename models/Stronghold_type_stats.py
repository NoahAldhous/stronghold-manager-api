GET_ALL_STRONGHOLD_STATS = ("""
WITH stats AS (
    SELECT
    st.type_name,
    scl.stronghold_level,
    ssl.stronghold_size,
    stl.toughness,
    scl.fortification_morale_bonus,
    SUM(scl.cost_to_build) OVER (
        PARTITION BY scl.stronghold_type_id
        ORDER BY scl.stronghold_level
    ) AS cost_to_build_total,
    SUM(scl.time_to_build) OVER (
        PARTITION BY scl.stronghold_type_id
        ORDER BY scl.stronghold_level
    ) AS time_to_build_total,
    LEAD(scl.cost_to_build) OVER (
        PARTITION BY scl.stronghold_type_id
        ORDER BY scl.stronghold_level
    ) AS cost_to_upgrade,
    LEAD(scl.time_to_build) OVER (
        PARTITION BY scl.stronghold_type_id
        ORDER BY scl.stronghold_level
    ) AS time_to_upgrade
    FROM stronghold_construction_levels scl
    JOIN stronghold_size_levels ssl
        ON scl.stronghold_type_id = ssl.stronghold_type_id
        AND scl.stronghold_level = ssl.stronghold_level
    JOIN stronghold_toughness_levels stl
        ON scl.stronghold_type_id = stl.stronghold_type_id
        AND scl.stronghold_level = stl.stronghold_level
    JOIN stronghold_types st
        ON scl.stronghold_type_id = st.id
)
SELECT jsonb_object_agg(type_name, type_stats) AS stats
FROM (
    SELECT
        type_name,
        jsonb_object_agg(
            'level' || stronghold_level,
            jsonb_build_object(
                'size', stronghold_size,
                'toughness', toughness,
                'fortificationBonus',fortification_morale_bonus,
                'timeToBuild', time_to_build_total,
                'costToBuild', cost_to_build_total,
                'costToUpgrade', COALESCE(cost_to_upgrade, 0),
                'timeToUpgrade', COALESCE(time_to_upgrade, 0)
            )
        ) AS type_stats
        FROM stats
        GROUP BY type_name
) t;
;""")