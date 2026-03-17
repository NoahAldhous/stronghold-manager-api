CREATE_SIGNATURE_ABILITY_RANGES_TABLE = (
    """CREATE TABLE IF NOT EXISTS signature_ability_ranges (
        id SERIAL PRIMARY KEY,
        range_type TEXT NOT NULL,
        reach INT,
        short_range INT,
        long_range INT
    )"""
)

POPULATE_SIGNATURE_ABILITY_RANGES_TABLE = (
    """INSERT INTO ability_ranges (
        range_type,
        reach,
        short_range,
        long_range   
    ) SELECT
        ranges.type,
        ranges.reach,
        ranges.short,
        ranges.long
    FROM (
        VALUES
            (
                'melee',
                5,
                0,
                0
            ),
            (
                'hybrid',
                5,
                20,
                60
            ),
            (
                'ranged',
                0,
                150,
                600
            ),
            (
                'spell 10',
                0,
                10,
                0
            ),
            (
                'spell 60',
                0,
                60,
                0
            ),
            (
                'spell 120',
                0,
                120,
                0
            )
    ) AS ranges(type, reach, short, long);
    """
)