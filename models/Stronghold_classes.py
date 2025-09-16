CREATE_STRONGHOLD_CLASSES_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_classes (id SERIAL PRIMARY KEY, class_name TEXT UNIQUE, class_stronghold_name TEXT UNIQUE, class_stronghold_description TEXT);"
)

POPULATE_STRONGHOLD_CLASSES_TABLE = (
    """ INSERT INTO TABLE stronghold_classes (
        class_name, 
        class_stronghold_name, 
        class_stronghold_description
    ) SELECT
        classes.name,
        classes.stronghold,
        classes.description
    FROM (
        VALUES
            (
                'barbarian',
                'camp',
                'The barbarian''s camp promises good food and drink as well as contests of strength and bravery.'
            ),
            (
                'bard',
                'theatre',
                'The bard''s theatre promises drama and entertainment! Poetry and song. But also rumour and intrigue!'
            ),
            (
                'cleric',
                'church',
                'The cleric''s church is a bastion of faith for believers and adherents to their deity''s laws, and a symbol of resistance against those forces that oppose the cleric''s god.'    
            ),
            (
                'druid',
                'grove',
                'The druid''s grove is a symbol of nature''s beauty and power.'
            ),
            (
                'fighter',
                'fortress',
                'The fighter''s fortress is a bastion against intruders, and it rewards those who practice their martial training.'    
            ),
            (
                'monk',
                'monastery',
                'The monk''s monastery is a monument to contemplation and self-reliance.'
            ),
            (
                'paladin',
                'chapel',
                'The paladin''s chapel broadcasts the power of good and law across the countryside.'
            ),
            (
                'ranger',
                'lodge',
                'The ranger''s lodge is a place of good hunting and security.'
            ),
            (
                'rogue',
                'tavern',
                'The rogue''s tavern is a hotbed of intrigue and information.'
            ),
            (
                'sorcerer',
                'sanctum',
                'The sorcerer''s sanctum houses a collection of curiousities and antiquities.'
            ),
            (
                'warlock',
                'fane',
                'The warlock''s fane is a locus of power commited to a being of alien intelligence.'
            ),
            (
                'wizard',
                'library',
                'The wizard''s library is a bastion of knowledge and research best hidden from the mundane world.'
            )
    ) AS classes(name, stronghold, description);
    """
)

GET_ALL_STRONGHOLD_CLASSES=(
    "SELECT * FROM stronghold_classes;"
)

GET_STRONGHOLD_CLASS_BY_ID=(
    "SELECT * FROM stronghold_classes WHERE id = %s;"
)

GET_STRONGHOLD_CLASS_BY_CLASS_NAME=(
    "SELECT * FROM stronghold_classes WHERE class_name = %s;"
)

CLEAR_STRONGHOLD_CLASSES_TABLE=(
    "DELETE FROM stronghold_classes;"
)