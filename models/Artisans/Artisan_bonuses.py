CREATE_ARTISAN_BONUSES_TABLE = (
    """CREATE TABLE IF NOT EXISTS artisan_bonuses (
        id SERIAL PRIMARY KEY,
        artisan_id INT NOT NULL,
        bonus_name TEXT NOT NULL,
        numerical_bonus INT,
        bonus_multiplier TEXT,
        bonus_description TEXT NOT NULL,
        requires_extended_rest BOOLEAN,
        FOREIGN KEY(artisan_id) REFERENCES artisan_shops(id) ON DELETE CASCADE
    );"""
)

POPULATE_ARTISAN_BONUSES_TABLE = (
    """INSERT INTO artisan_bonuses (
        artisan_id,
        bonus_name,
        numerical_bonus,
        bonus_multiplier,
        bonus_description,
        requires_extended_rest
    ) SELECT
        shops.id,
        bonuses.name,
        bonuses.number,
        bonuses.multiplier,
        bonuses.description,
        bonuses.rest
    FROM (
        VALUES
            (
                'alchemist',
                'alchemy',
                10,
                'shop_level',
                'The laboratory allows your alchemist to craft potions 10%% cheaper and faster than normal per level of the laboratory.',
                false
            ),
            (
                'blacksmith',
                'crafting',
                10,
                'shop_level',
                'The smithy allows your blacksmith to craft magic arms and armor 10%% cheaper and faster than normal per level of the smithy. What items your smith can forge depends on which organs you bring!',
                false
            ),
            (
                'captain',
                'unit_experience',
                1,
                'shop_level',
                'Your barracks can upgrade a number of units equal to its level. It begins at 1st level (one unit affected) and can be upgraded to 5th level (5 units affected). The units affected are chosen at the start of a battle and cannot be changed until the next battle.',
                false
            ),
            (
                'carpenter',
                'siege_unit_cost',
                10,
                'shop_level',
                'Carpenters lower the cost to build and upkeep siege engines by 10%% per level of their shop',
                false
            ),
            (
                'carpenter',
                'stronghold_upgrade_time',
                10,
                'shop_level',
                'Carpenters let you improve your stronghold 10%% faster per level of their shop.',
                false
            ),
            (
                'farmer',
                'revenue',
                100,
                'quantity',
                'The stronghold produces 100 gp per season per farmer on your land.',
                false
            ),
            (
                'mason',
                'free_repairs',
                250,
                'shop_level',
                'Your mason will make free repairs worth 250 gp per quarry level per week.',
                false
            ),
            (
                'mason',
                'stronghold_upgrade_cost',
                10,
                'shop_level',
                'Masons decrease the cost required to improve your stronghold by 10%% per quarry level. This time decrease can be combined with the carpenter''s benefit.',
                false
            ),
            (
                'miner',
                'revenue',
                '500',
                'none',
                'A mine produces 500 gp per season.',
                false
            ),
            (
                'miner',
                'unit_equipment',
                1,
                'shop_level',
                'In addition, a mine improves the equipment of some number of your units by one level—a light unit becomes medium, medium becomes heavy, etc. This bonus can be applied to one unit per mine level, as it includes the time and cost of maintaining their improved equipment.',
                false
            ),
            (
                'sage',
                'sage_background',
                0,
                'none',
                'Your sage grants you access to the Sage background ability. If your sage doesn''t know the answer to your question, they know where the answer can be found.',
                false
            ),
            (
                'sage',
                'combat_advantage',
                1,
                'shop_level',
                'You can use the chosen advantage on a number of attacks equal to the level of your sage''s library, after which you must take an extended rest to recharge this ability.',
                true
            ),
            (
                'sage',
                'nearest_codex',
                0,
                'none',
                'Your sage also knows the location of the nearest codex. It may be hidden in a ruin within a few miles of your stronghold, or it may be a hundred miles away in the library of the king''s archmage. But your sage knows its whereabouts.',
                false
            ),
            (
                'scribe',
                'scroll_crafting',
                10,
                'shop_level',
                'If a spellcaster of appropriate level is present for at least an hour, a scribe can craft a magic scroll in a fraction of the time it would take a wizard or sorcerer to do it alone. The time and cost are both reduced by 10%% per level of the tannery.',
                false
            ),
            (
                'spy',
                'spy_difficulty',
                1,
                'shop_level',
                'Your spy increases the DC for agents spying on you by 3 plus 1 per level of your spy''s network.',
                false
            ),
            (
                'spy',
                'follower_chart',
                1,
                'shop_level',
                'Each time you roll on your followers chart, the spy lets you increase or decrease your roll by up to 3 plus 1 per level of your network.',
                false
            ),
            (
                'tailor',
                'charisma_check',
                1,
                'shop_level',
                'With a tailor in your retinue, you can, as a reaction, replace the result of any Charisma check with a 12 (before adding bonuses). This can be done a number of times equal to your tailor’s shop level, after which you must take an extended rest to refresh this ability.',
                true
            )
    ) AS bonuses(artisan, name, number, multiplier, description, rest)
        JOIN artisan_shops AS shops
            ON bonuses.artisan = shops.artisan_name;    
    """
)