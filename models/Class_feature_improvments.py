CREATE_CLASS_FEATURE_RESTRICTIONS_TABLE = (
    "CREATE TABLE IF NOT EXISTS class_feature_restrictions(id SERIAL PRIMARY KEY, restriction_name TEXT UNIQUE, restriction_description TEXT UNIQUE);"
)

POPULATE_CLASS_FEATURE_RESTRICTIONS_TABLE = (
    """ INSERT INTO class_feature_restrictions(
        restriction_name,
        restriction_description
        ) SELECT
            restrictions.name,
            restrictions.descripton
        FROM (
            VALUES
                (
                    'quantity',
                    'You can do this a number of times equal to your stronghold level, after which you must take an extended rest to refresh this ability.'
                ),
                (
                    'spell slot',
                    'You may use this extra spell slot a number of times equal to your stronghold level, after which you must take an extended rest to refresh this ability.'
                ),
                (
                    'sorcery points',
                    'These bonus points only refresh when you take an extended rest.'
                ),
                (
                    'damage rolls',
                    'You can do this to a number of damage rolls equal to your stronghold level, after which you must take an extended rest to refresh this ability.'
                ),
                (
                    'attacks',
                    'You can do this for a number of attacks equal to your stronghold level, after which you must take an extended rest to refresh this ability.'
                ),
                (
                    'action surges',
                    'You can do this for a number of surges equal to your stronghold level, after which you must take an extended rest to refresh this ability.'
                ),
                (
                    'inspiration dice',
                    'This applies to a number of inspiration dice equal to your stronghold level, after which you must take an extended rest to refresh this ability.'
                )
        ) AS restrictions(name, description);
    """
)

CREATE_CLASS_FEATURE_IMPROVEMENTS_TABLE = (
    "CREATE TABLE IF NOT EXISTS class_feature_improvements(id SERIAL PRIMARY KEY, stronghold_class_id INT, improvement_name TEXT UNIQUE, improvement_description TEXT, improvement_restriction_id INT, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id) ON DELETE CASCADE, FOREIGN KEY(improvement_restriction_id) REFERENCES class_feature_restrictions(id) ON DELETE CASCADE);"
)

POPULATE_CLASS_FEATURE_IMPROVEMENTS_TABLE = (
    """INSERT INTO class_feature_improvements (
        stronghold_class_id,
        improvement_name,
        improvement_description,
        improvement_restriction_id
    ) SELECT 
        classes.id,
        improvements.name,
        improvements.description,
        restrictions.id
    FROM (
        VALUES 
            (
                'barbarian',
                'chieftan''s rage',
                'Whenever you reduce an enemy to 0 hit points, you can choose to make an additional weapon attack or move up to your speed.',
                'quantity',
            ),
            (
                'bard',
                'encouraging inspiration',
                'While an ally has unspent bardic inspiration dice, their proficiency bonus increases by 1.',
                'inspiration dice',
            ),
            (
                'cleric',
                'manifest divinity',
                'When you use your Channel Divinity class feature, all allies within 30 feet regain 3d8 hit points.',
                'quantity',
            ),
            (
                'druid',
                'savage shape',
                'When you assume your Wild Shape, you may assume the form of any monstrosity, fey or dragon, including those wit a flying or swimming speed. You may use this ability to transform into a creature with a Challenge Rating up to half your level, rounded up. All other Wild Shape restrictions and benefits apply (including using all of the form''s actions and abilities except legendary actions).',
                'quantity',
            ),
            (
                'fighter',
                'fighting surge',
                'Whenever you attack by using your Action Surge, you automatically score a critical hit on successful attack rolls.',
                'action surges',
            ),
            (
                'monk',
                'focused ki',
                'Whenever you are attack while you have unspent ki, you can ignore all of the attack''s effects except its damage.',
                'quantity',
            ),
            (
                'paladin',
                'righteous smite',
                'Your Divine Smite burns through enemy resistance. Enemies normally resistant to either radiant damage or your weapon damage lose it. Enemies immune to either type of damage are now resistant to it, and enemies without resistance to either radiant or your weapon damage become vulnerable.',
                'attacks',
            ),
            (
                'ranger',
                'chosen enemy',
                'Your favoured enemy has vulnerability to your attacks.',
                'damage rolls',
            ),
            (
                'rogue',
                'vanishing strike',
                'After you hit with a Sneak Attack, you may become invisible. Anything you are wearing or carrying is invisible as long as it is on your person. This effect lasts until the end of your next turn or until you attack or cast a spell.',
                'quantity',
            ),
            (
                'sorcerer',
                'sourcer of magic',
                'You gain bonus sorcery points equal in number to your stronghold level.',
                'sorcery points',
            ),
            (
                'warlock',
                'master invoker',
                'You gain an extra spell slot.',
                'spell slot',
            ),
            (
                'wizard',
                'spellmaster',
                'You can maintain two spells with concentration at once.',
                'quantity',
            ),
    ) AS improvements(class, name, description, restriction)
        JOIN stronghold_classes AS classes
            ON classes.class_name = improvements.class
        JOIN class_feature_restrictions AS restrictions
            ON restrictions.restriction_name = improvements.restriction;
    """
)

GET_ALL_CLASS_FEATURE_IMPROVEMENTS = (
    """SELECT
        classes.class_name AS class,
        improvements.improvement_name AS name,
        improvements.improvement_description AS description,
        restrictions.restriction_description AS restriction
        FROM class_feature_improvements AS improvements
        LEFT JOIN stronghold_classes AS classes
            ON classes.id = improvements.stronghold_class_id
        LEFT JOIN class_feature_restrictions AS restrictions
            ON restrictions.id = improvements.improvement_restriction_id;
    """
)

GET_CLASS_FEATURE_IMPROVEMENT_BY_CLASS_ID = (
    """SELECT
        classes.class_name AS class,
        improvements.improvement_name AS name,
        improvements.improvement_description AS description,
        restrictions.restriction_description AS restriction
        FROM class_feature_improvements AS improvements
        LEFT JOIN stronghold_classes AS classes
            ON classes.id = improvements.stronghold_class_id
        LEFT JOIN class_feature_restrictions AS restrictions
            ON restrictions.id = improvements.improvement_restriction_id
        WHERE improvements.stronghold_class_id = %s;
    """
)

CLEAR_CLASS_FEATURE_RESTRICTIONS_TABLE = (
    "DELETE FROM class_feature_restrictions;"
)

CLEAR_CLASS_FEATURE_IMPROVEMENTS_TABLE = (
    "DELETE FROM class_feature_improvements;"
)