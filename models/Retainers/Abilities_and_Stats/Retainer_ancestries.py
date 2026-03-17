CREATE_RETAINER_ANCESTRIES_TABLE = (
    """CREATE TABLE IF NOT EXISTS retainer_ancestries(
        id SERIAL PRIMARY KEY,
        ancestry_name TEXT NOT NULL,
        ancestry_size TEXT NOT NULL,
        ancestry_speed INT NOT NULL,
        ancestry_darkvision_distance INT NOT NULL 
    );
    """
)

POPULATE_RETAINER_ANCESTRIES_TABLE =(
    """INSERT INTO retainer_ancestries (
        ancestry_name,
        ancestry_size,
        ancestry_speed,
        ancestry_darkvision_distance
    ) SELECT
        ancestries.name,
        ancestries.size,
        ancestries.speed,
        ancestries.darkvision
    FROM (
        VALUES
            (
                'dwarf',
                'medium',
                25,
                60
            ),
            (
                'elf',
                'medium',
                30,
                60
            ),
            (
                'halfling',
                'small',
                25,
                0
            ),
            (
                'human',
                'medium',
                30,
                0
            ),
            (
                'dragonborn',
                'medium',
                30,
                0
            ),
            (
                'gnome',
                'small',
                25,
                60
            ),
            (
                'half-elf',
                'medium',
                30,
                60
            ),
            (
                'half-orc',
                'medium',
                30,
                60
            ),
            (
                'tiefling',
                'medium',
                30,
                60
            )
    );
    """
)