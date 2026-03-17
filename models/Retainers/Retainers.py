CREATE_RETAINERS_TABLE = (
    """CREATE TABLE IF NOT EXISTS retainers (
        id SERIAL PRIMARY KEY,
        class_id INT NOT NULL REFERENCES classes(id) ON DELETE CASCADE,
        retainer_name TEXT UNIQUE NOT NULL,
        armour_id INT NOT NULL REFERENCES retainer_armour_classes(id)
        );"""
)

POPULATE_RETAINERS_TABLE = (
    """INSERT INTO retainers (
        class_id,
        retainer_name,
        armour_id    
    ) SELECT 
        classes.id,
        retainers.name,
        armour.id
    FROM (
        VALUES
            (
                'barbarian',
                'reaver',
                'medium'
            ),
            (
                'barbarian',
                'spirit warden',
                'medium'
            ),
            (
                'bard',
                'loremaster',
                'light'
            ),
            (
                'bard',
                'troubadour-warrior',
                'light'
            ),
            (
                'cleric',
                'curate',
                'medium'
            ),
            (
                'cleric',
                'exorcist',
                'medium'
            ),
            (
                'cleric',
                'healer',
                'heavy'
            ),
            (
                'cleric',
                'shadow priest',
                'medium'
            ),
            (
                'cleric',
                'stormspeaker',
                'heavy'
            ),
            (
                'cleric',
                'warden',
                'medium'
            ),
            (
                'cleric',
                'battle priest',
                'heavy'
            ),
            (
                'druid',
                'mystic',
                'medium'
            ),
            (
                'druid',
                'skinwalker',
                'medium'
            ),
            (
                'fighter',
                'knight-sorcerer',
                'heavy'
            ),
            (
                'fighter',
                'swordmaster',
                'heavy'
            ),
            (
                'fighter',
                'warlord',
                'heavy'
            ),
            (
                'monk',
                'acolyte of the way',
                'medium'
            ),
            (
                'monk',
                'acolyte of darkness',
                'medium'
            ),
            (
                'monk',
                'elemental acolyte',
                'medium'
            ),
            (
                'paladin',
                'cavalier',
                'heavy'
            ),
            (
                'paladin',
                'justicar',
                'heavy'
            ),
            (
                'paladin',
                'knight of the green order',
                'heavy'
            ),
            (
                'ranger',
                'beast lord',
                'medium'
            ),
            (
                'ranger',
                'tracker',
                'medium'
            ),
            (
                'rogue',
                'executioner',
                'light'
            ),
            (
                'rogue',
                'guild adept',
                'light'
            ),
            (
                'rogue',
                'cutpurse',
                'light'
            ),
            (
                'sorcerer',
                'thaumaturgist',
                'light'
            ),
            (
                'sorcerer',
                'chaos mage',
                'light'
            ),
            (
                'warlock',
                'alienist',
                'light'
            ),
            (
                'warlock',
                'diabolist',
                'light'
            ),
            (
                'warlock',
                'exarch',
                'light'
            ),
            (
                'wizard',
                'conjurer',
                'light'
            ),
            (
                'wizard',
                'enchanter',
                'light'
            ),
            (
                'wizard',
                'evoker',
                'light'
            ),
            (
                'wizard',
                'illusionist',
                'light'
            ),
            (
                'wizard',
                'necromancer',
                'light'
            ),
            (
                'wizard',
                'seer',
                'light'
            ),
            (
                'wizard',
                'shaper',
                'light'
            ),
            (
                'wizard',
                'theurgist',
                'light'
            )   
    ) AS retainers(class, name, armour)
        JOIN retainer_armour_classes AS armour
            ON retainer.armour = armour.armour_type
        JOIN classes
            ON retainer.class = classes.class_name
    ;"""
)