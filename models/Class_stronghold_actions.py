CREATE_CLASS_STRONGHOLD_ACTIONS_TABLE = (
    "CREATE TABLE IF NOT EXISTS class_stronghold_actions (id SERIAL PRIMARY KEY, stronghold_class_id INT, action_name TEXT UNIQUE, action_description TEXT, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id) ON DELETE CASCADE);"
)

POPULATE_CLASS_STRONGHOLD_ACTIONS_TABLE = (
    """INSERT INTO class_stronghold_actions (
        stronghold_class_id, 
        action_name,
        action_description
    ) SELECT 
        classes.id,
        actions.name,
        actions.description
    FROM (
        VALUES
            (
                'barbarian',
                'they should be afraid',
                'You issue forth a might ''Yawp!'' that causes all enemies within 60 feet to become frightened until initiative count 20 on the next round.'
            ),
            (
                'barbarian',
                'feel my fury!',
                'You rage, and your allies gain the benefits of your rage as long as those allies aren''t wearing heavy armour.'
            ),
            (
                'barbarian',
                'herald the storm',
                'You cast chain lightning with a DC equal to 8 plus your proficiency modifier, plus your Constitution modifier. You may do this even while raging, and this does not end your rage.'
            ),
            (
                'bard',
                'harmonise',
                'Until initiative count 20 on the next round, all inspiration dice produce their maximum result when rolled, followed by the sound of a two-note chord: one root note and another a fifth higher than the root.'
            ),
            (
                'bard',
                'accompaniment',
                'A three-piece band arrives singing your praises. Until initiative count 20 on the next turn, enemies make saving throws against your magic by rolling three d20s and using the worst of the three. The band has exceptionally good rhythm and world-class lute fingering, and the singer has an unusually high voice.'
            ),
            (
                'bard',
                'encore',
                'You regain all inspiration dice.'
            ),
            (
                'cleric',
                'a plague upon you',
                'All enemies within 30 feet of you must succeed on a Constitution saving throw of suffer the effects of the contagion spell.'
            ),
            (
                'cleric',
                'no rest for the wicked',
                'Shafts of golden light stab down from the sky, penetrating walls and ceilings. The beams target all undead, demons and devils within 60 feet of you, even those hidden or invisible. Targets must succeed on a Wisdom saving throw or be annihilated.'
            ),
            (
                'cleric',
                'lift up the weary',
                'You and all allies in the stronghold recover all Hit Dice and gain 30 temporary hit points.'
            ),
            (
                'druid',
                'sea of thorns',
                'Grasping vines rise from the ground for 1 minute. Every enemy within 60 feet must make a Dexterity saving throw or be restrained for the duration, taking 3d8 piercing damage at the start of each of their turns from stabbing thorns. At the end of its turn, an affected enemy can make another saving throw to escape.'
            ),
            (
                'druid',
                'into the wild green yonder',
                'You cast banishment on an enemy, sending them to Arcadia on a failed save.'
            ),
            (
                'druid',
                'homegrown henchmen',
                'You summon 1d4 + 1 shambling mounds who fight gor you for 1 minute.'
            ),
            (
                'fighter',
                'close the gap',
                'Until initiative count 20 on the next round, any enemy who tries to cast a spell in your demesne experiences searing pain. The enemy can choose another action, but if it chooses to cast the spell, it must make a DC 16 Constitution saving throw. On a failed save, it takes 1d6 force damage per level of the spell, and the spell has no effect and is wasted.'
            ),
            (
                'fighter',
                'just like we practiced',
                'Until the end of your next turn, you and all your allies'' weapon attacks hit automatically. Roll anyway, though- you might score a crit!'
            ),
            (
                'fighter',
                'it''s not over ''til it''s over',
                'You and your allies are restored to full hit points.'
            ),
            (
                'monk',
                'perfect form',
                'Until initiative count 20 on the next round, your skin becomes diamond. For the duration, you are immune to all but psychic damage.'
            ),
            (
                'monk',
                'crashing waves against the cliff',
                'You make eight unarmed attacks against an adjacent enemy.'
            ),
            (
                'monk',
                'refocus',
                'You regain all ki, as though you had finished a short or long rest.'
            ),
            (
                'paladin',
                'chains of judgement',
                'Each chaotic or evil creature (your choice) within 120 feet must succeed on a Constitution saving throw or be bound by gold (anti-evil) or silver (anti-chaos) chains, grappling it until it makes a Strength or Dexterity check as an action against your spell DC.'
            ),
            (
                'paladin',
                'bind to the earth',
                'Flying creatures within 120 feet must succeed on a Constitution check against your spell save DC or immediately land. They cannot take off again for 10 minutes.'
            ),
            (
                'paladin',
                'armour of the gods',
                'Choose an ally within sight to gain an AC bonus equal to your Charisma bonus, as their armour becomes gold, for 10 minutes. Each ally can be affected by this ability only once per day.'
            ),
            (
                'ranger',
                'know thy foe',
                'Small targets appear on the vulnerable spots of nearby enemies. Until initiative count 20 on the next round, all enemies within 60 feet have vulnerability to your attacks.'
            ),
            (
                'ranger',
                'can''t hit what you can''t see',
                'You summon a fog cloud in a 60-foot radius that lasts for 1 minute. You and your allies can see through this fog as though it were merely a hazy mist that did not obscure vision.'
            ),
            (
                'ranger',
                'bleed them out',
                'Until initiative count 20 on the next turn, all of your successful attacks also cause the target to bleed. A bleeding creature take 3d8 slashing damage at the start of each of its following turns, and can make a DC 18 Constitution save at the end of each of it turns to end the bleeding.'
            ),
            (
                'rogue',
                'marked for death',
                'All enemies within 60 feet are marked for death. For the next minute, if you hit a marked enemy, you can remove its mark to deal an extra 6d6 slashing damage.'
            ),
            (
                'rogue',
                'that trick won''t work on me',
                'Enemies within 60 feet are revealed, losing stealth and invisibility.'
            ),
            (
                'rogue',
                'let the gods decide',
                'You gain a Coin of Fate. Each time you are hit in combat, you may flip the coin. Heads, the attack misses instead. Tails, the attack hits as normal and you lose the coin.'
            ),
            (
                'sorcerer',
                'full burst',
                'You cast three spells from your list of known spells, using spells slots as normal.'
            ),
            (
                'sorcerer',
                'escalation',
                'For the next minute, all of your spells are heightened, as per the heightened Metamagic effect. You cannot use sorcery points to heighten an already heightened spell.'
            ),
            (
                'sorcerer',
                'phoenix soul',
                'You are wreathed by a fire shield. Enemies who strike the shield take 4d8 damage instead of 2d8.'
            ),
            (
                'warlock',
                'renew the pact',
                'You recover all spell slots as though you completed a short rest.'
            ),
            (
                'warlock',
                'why choose?',
                'You fire an eldritch blast at each enemy you can see within 60 feet.'
            ),
            (
                'warlock',
                'call in that favour',
                'You summon a type-VI servitor.'
            ),
            (
                'wizard',
                'practice fundamentals',
                'You cast a spell from your list of prepared spells. This does not use a spell slot.'
            ),
            (
                'wizard',
                'stop and let me think',
                'You cast flesh to stone on all enemies within 60 feet. This does not use a spell slot.'
            ),
            (
                'wizard',
                'time to pay attention',
                'You recover all spent spell slots as though you had finished a long rest.'
            )
    ) AS actions(class, name, description)
        JOIN stronghold_classes AS classes
            ON classes.class_name = actions.class;
    """
)

GET_ALL_CLASS_STRONGHOLD_ACTIONS = (
    "SELECT * FROM class_stronghold_actions;"
)

GET_STRONGHOLD_ACTIONS_BY_CLASS_ID = (
    "SELECT * FROM class_stronghold_actions WHERE stronghold_class_id = %s;"
)

CLEAR_STRONGHOLD_ACTIONS_TABLE = (
    "DELETE FROM class_stronghold_actions;"
)