CREATE_RETAINER_CLASS_SAVES_RELATIONS_TABLE = (
    """CREATE TABLE IF NOT EXISTS retainer_class_saves_relations (
        id SERIAL PRIMARY KEY,
        class_id INT NOT NULL REFERENCES classes(id) ON DELETE CASCADE,
        save_id INT NOT NULL REFERENCES abilities(id) ON DELETE CASCADE
    );"""
)

POPULATE_RETAINER_CLASS_SAVES_RELATIONS_TABLE = (
    """INSERT INTO retainer_class_saves_relations (
        class_id,
        save_id
    ) SELECT
        classes.id,
        abilities.id
    FROM (
        VALUES
            (
                'barbarian',
                'strength'
            ),
            (
                'barbarian'.
                'constitution'
            ),
            (
                'bard',
                'dexterity'
            ),
            (
                'bard',
                'charisma'
            ),
            (
                'cleric',
                'wisdom'
            ),
            (
                'druid',
                'intelligence'
            ),
            (
                'druid',
                'wisdom'
            ),
            (
                'fighter',
                'strength'
            ),
            (
                'fighter',
                'constitution'
            ),
            (
                'monk',
                'strength'
            ),
            (
                'monk',
                'dexterity'
            ),
            (
                'paladin',
                'strength'
            ),
            (
                'paladin',
                'wisdom'
            ),
            (
                'paladin',
                'charisma'
            ),
            (
                'ranger',
                'strength'
            ),
            (
                'ranger',
                'dexterity'
            ),
            (
                'rogue',
                'dexterity'
            ),
            (
                'rogue',
                'intelligence'
            ),
            (
                'sorcerer',
                'constitution'
            ),
            (
                'sorcerer',
                'charisma'
            ),
            (
                'warlock',
                'wisdom'
            ),
            (
                'warlock',
                'charisma'
            ),
            (
                'wizard',
                'intelligence'
            ),
            (
                'wizard',
                'wisdom'
            )
    ) AS relations(class, ability)
        JOIN abilities 
            ON abilities.ability_name = relations.ability
        JOIN classes 
            ON classes.class_name = relations.class;
    """
)