CREATE_STRONGHOLD_RETAINERS_TABLE = (
    """CREATE TABLE IF NOT EXISTS stronghold_retainers (
        id SERIAL PRIMARY KEY,
        individual_name TEXT NOT NULL,
        stronghold_id INT NOT NULL REFERENCES strongholds(id) ON DELETE CASCADE,
        retainer_id INT NOT NULL REFERENCES retainers(id) ON DELETE CASCADE,
        ancestry_id INT NOT NULL REFERENCES retainer_ancestries(id) ON DELETE CASCADE,
        retainer_level INT NOT NULL CHECK (retainer_level BETWEEN 1 AND 20),
        health_levels_lost INT NOT NULL CHECK (health_levels_lost BETWEEN 0 AND retainer_level)
        )"""
)

ADD_STRONGHOLD_RETAINER = (
    """INSERT INTO stronghold_retainers (
        individual_name,
        stronghold_id,
        retainer_id,
        ancestry_id,
        retainer_level,
        health_levels_lost
    ) VALUES (
        %s,
        %s,
        (
            SELECT id
                FROM retainers
                WHERE retainer_name = %s
        ),
        (
            SELECT id
                FROM retainer_ancestries
                WHERE ancestry_name = %s
        ),
        %s,
        %s
    ) RETURNING id;
    """
)