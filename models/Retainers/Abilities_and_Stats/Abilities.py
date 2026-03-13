CREATE_RETAINER_ABILITIES_TABLE = (
    """CREATE TABLE IF NOT EXISTS abilities (
        id SERIAL PRIMARY KEY,
        ability_name TEXT UNIQUE NOT NULL,
        abbreviation TEXT UNIQUE NOT NULL
        );"""
)

POPULATE_RETAINER_ABILITES_TABLE = (
    """INSERT INTO abilities (
        ability_name,
        abbreviation
    ) SELECT
        abilities.ability
        abilities.abbreviation
    FROM (
        VALUES
            (
                'strength',
                'str'
            ),
            (
                'dexterity',
                'dex'
            ),
            (
                'constitution',
                'con'
            ),
            (
                'intelligence',
                'int'
            ),
            (
                'wisdom'
                'wis'
            ),
            (
                'charisma'
                'cha'
            )
    ) AS abilities(ability, abbreviation);
    """
)