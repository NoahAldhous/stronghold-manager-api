CREATE_CLASSES_TABLE = (
    """CREATE TABLE IF NOT EXISTS classes (
        id SERIAL PRIMARY KEY,
        class_name TEXT UNIQUE NOT NULL
    );
    """
)

POPULATE_CLASSES_TABLE = (
    """INSERT INTO classes (
        class_name    
    ) SELECT
        class.name
    FROM (
        VALUES
            (
                'barbarian'
            ),
            (
                'bard'
            ),
            (
                'cleric'
            ),
            (
                'druid'
            ),
            (
                'fighter'
            ),
            (
                'monk'
            ),
            (
                'ranger'
            ),
            (
                'rogue'
            ),
            (
                'paladin'
            ),
            (
                'sorcerer'
            ),
            (
                'warlock'
            ),
            (
                'wizard'
            )
    ) AS class(name);
    """
)