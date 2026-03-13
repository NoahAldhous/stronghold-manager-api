CREATE_RETAINER_CLASS_ABILITY_RELATIONS_TABLE = (
    """CREATE TABLE IF NOT EXISTS retainer_class_ability_relations (
        id SERIAL PRIMARY KEY,
        class_id INT NOT NULL REFERENCES classes(id) ON DELETE CASCADE,
        ability_id INT NOT NULL REFERENCES abilities(id) ON DELETE CASCADE
        );"""
)

POPULATE_RETAINER_CLASS_ABILITY_RELATIONS_TABLE = (
    """INSERT INTO retainer_class_ability_relations (
            class_id,
            ability_id
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
                    'bard',
                    'charisma'
                ),
                (
                    'cleric',
                    'wisdom'
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
                    'monk',
                    'dexterity'
                ),
                (
                    'monk',
                    'wisdom'
                ),
                (
                    'paladin',
                    'strength'
                ),
                (
                    'paladin',
                    'charisma'
                ),
                (
                    'ranger',
                    'dexterity'
                ),
                (
                    'ranger',
                    'wisdom'
                ),
                (
                    'rogue',
                    'dexterity'
                ),
                (
                    'sorcerer',
                    'dexterity'
                ),
                (
                    'warlock',
                    'charisma'
                ),
                (
                    'wizard',
                    'intelligence'
                )
        ) AS relations(class, ability)
            JOIN abilities 
                ON relations.ability = abilities.ability_name
            JOIN classes
                ON relations.class = classes.class_name
        );
        """
)