CREATE_CLASS_DEMESNE_EFFECTS_TABLE = (
    "CREATE TABLE IF NOT EXISTS class_demesne_effects (id SERIAL PRIMARY KEY, stronghold_class_id INT, effect_description TEXT UNIQUE, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id) ON DELETE CASCADE);"
)

POPULATE_CLASS_DEMESNE_EFFECTS_TABLE = (
    """INSERT INTO class_demesne_effects (
        stronghold_class_id,
        effect_description    
    ) SELECT 
        classes.id,
        effects.description
    FROM (
        VALUES
            (
                'barbarian',
                'Ale within the barbarian''s demesne is particularly refreshing, bringing good cheer with no hangovers the next day no matter how much is consumed.'
            ),
            (
                'barbarian',
                'Wildlife within the barbarian''s demesne grows especially large and fierce, migrating as the camp moves.'
            ),
            (
                'barbarian',
                'Poisons brought into the barbarian''s demesne within the hour. No such cowardly ''civilised'' forms of death are permitted.'
            ),
            (
                'bard',
                'Whenever wind blows through the trees in the bard''s demesne, music plays. Hooves on roads beat out a complex rhythm.'
            ),
            (
                'bard',
                'Folks who live for a week in the bard''s demesne find themselves ending conversations with rhyming couplets.'
            ),
            (
                'bard',
                'Thunder can be counted on to roll whenever someone in the bard''s demesne says something dramatic. Ravens obediently alight on nearby branches when it is dramatically expected of them.'
            ),
            (
                'cleric',
                'Folks who live in the cleric''s demesne are immune to disease.'
            ),
            (
                'cleric',
                'The cleric can hear the prayers of those living in their demesne who are in concordance with the cleric''s deity.'
            ),
            (
                'cleric',
                'While the cleric is hale, the weather in their demesne is fair. If the cleric is wounded or suffering, the weather turns foul. For this effect to happen, the cleric merely has to be on the same plane as their demesne.'
            ),
            (
                'druid',
                'Local birds and mammals in the druid''s demesne can speak Common and Elven. They enjoy talking to new people but will try to find and warn the druid if suspicious strangers enter the demesne.'
            ),
            (
                'druid',
                'Nuts, fruits and vegetables grown naturally (i.e, not farmed or cultivated) in the druid''s demesne grant those who eat them the effect of goodberry. If taken outside the demesne, they lose this effect.'
            ),
            (
                'druid',
                'No roads or trails in the druid''s demesne last more than a day. However, allies and the units of allies can pass through the demesne as though there were roads.'
            ),
            (
                'fighter',
                'Fortifications in the fighter''s demesne grant units defending them an extra +2 morale bonus.'
            ),
            (
                'fighter',
                'Menhirs appear in the fighter''s demesne, following anyone hostile to those who call this province home, imposing themselves between intruders and locals.'
            ),
            (
                'fighter',
                'Archers who train in the fighter''s demesne find their arrows go farther and strike more accurately.'
            ),
            (
                'fighter',
                'Edged weapons in the fighter''s demesne are keener and do not dull.'
            ),
            (
                'monk',
                'Creatures age more slowly within the confines of the monk''s demesne.'
            ),
            (
                'monk',
                'The temperature in the monk''s demesne is always temperate, all year round, all day long.'
            ),
            (
                'monk',
                'Violence of any kind in the demesne has a 15% chance of summoning a Source of Earth, who immediately uses Back to Earth to end the violence. The monk can reverse these effects.'
            ),
            (
                'paladin',
                'Clear blue skies and warm sun dominate year-round. Rain falls only at night, and thunderstorms avoid the area.'
            ),
            (
                'paladin',
                'Evil creatures in daylight have disadvantage on attack rolls, saving throws, and ability checks.'
            ),
            (
                'paladin',
                'The paladin is instantly aware of the presence and location in their demesne of any chaotic or evil creature with more than 7 hit dice. The range of this awareness is a number of hexes equal to the level of the paladin''s stronghold.'
            ),
            (
                'ranger',
                'Stags, harts and other game are always plentiful in the ranger''s demesne, but they are larger and fiercer than normal.'
            ),
            (
                'ranger',
                'Enemies of the ranger and the locals must make DC 15 Wisdom (Survival) checks to navigate the ranger''s demesne. On a failure, they are attacked by 2d6 winter wolves.'
            ),
            (
                'ranger',
                'Allies treat the ranger''s demesne as favoured terrain when moving their units. Enemy units treat it as difficult terrain.'
            ),
            (
                'rogue',
                'One ally per level of the rogue''s stronghold can hide in the rogue''s demesne, and no mundane or magical means will reveal their location.'
            ),
            (
                'rogue',
                'Creatures trespassing in the rogue''s demesne have the overwhelming sensation they are being spied upon.'
            ),
            (
                'rogue',
                'When a creature hostile to the rogue and aware of their existence finishes a long rest within the rogue''s demesne, roll a d20. On a roll of 10 or less, the creature triggers a hidden trap, taking 3d8 piercing damage.'
            ),
            (
                'sorcerer',
                'Curses, blessings, and oaths pronounced within the sorcerer''s demesne have a 15% chance of causing the speaker to roll on the Wild Magic table.'
            ),
            (
                'sorcerer',
                'Folks who live in the sorcerer''s demesne for a season learn one random sorcerer cantrip. They lose the ability to cast it if they ever leave.'
            ),
            (
                'sorcerer',
                'Raindrops in the sorcerer''s demesne cast dazzling prismatic reflections during the day.'
            ),
            (
                'warlock',
                'The sun appears as a baleful orbs in the sky over the warlock''s demesne.'
            ),
            (
                'warlock',
                'In the warlock''s demesne, constellations in the night sky are strange, and stars occasionally fall from the sky.'
            ),
            (
                'warlock',
                'The warlock is immediately aware of enemies in their demesne.'
            ),
            (
                'warlock',
                'Once per month, the warlock can summon an earthquake, as per the spell, targeting any enemies in their demesne.'
            ),
            (
                'wizard',
                'The library of the wizard''s stronghold has a copy of every nonmagical book anyone brings into the wizard''s demesne.'
            ),
            (
                'wizard',
                'By concentrating for 10 minutes, the wizard can scry on any person or location in their demesne as per the scrying spell. The wizard can do this while anywhere, including another plane.'
            ),
            (
                'wizard',
                'Once per day, the wizard can control the weather in their demesne. The wizard doesn''t have to be in their demesne to do this. The effect is otherwise the same as the control weather spell.'
            )
    ) AS effects(class, description)
        JOIN stronghold_classes AS classes
            ON classes.class_name = effects.class
    """
)

GET_ALL_CLASS_DEMESNE_EFFECTS = (
    "SELECT * FROM class_demesne_effects;"
)

GET_CLASS_DEMESNE_EFFECTS_BY_CLASS_ID = (
    "SELECT * FROM class_demesne_effects WHERE class_id = %s;"
)

CLEAR_CLASS_DEMESNE_EFFECTS_TABLE = (
    "DELETE FROM class_demesne_effects;"
)