CREATE_ARTISAN_SHOPS_TABLE = (
   """CREATE TABLE IF NOT EXISTS artisan_shops (
        id SERIAL PRIMARY KEY,
        artisan_name TEXT UNIQUE NOT NULL,
        shop_name TEXT UNIQUE NOT NULL,
        shop_description TEXT UNIQUE NOT NULL,
        upgradeable BOOLEAN
       )"""
)

POPULATE_ARTISAN_SHOPS_TABLE = (
    """INSERT INTO artisan_shops (
        artisan_name,
        shop_name,
        shop_description,
        upgradeable    
    ) SELECT 
        shops.artisan,
        shops.name,
        shops.description,
        shops.upgradeable
    FROM (
        VALUES
            (
                'alchemist',
                'laboratory',
                'The laboratory allows your alchemist to craft potions 10% cheaper and faster than normal per level of the laboratory. The alchemist is not a wizard or sorcerer but understands the principles of magic well enough to duplicate their effects. The kinds of potions your alchemist can make depend on the monster organs you bring them!'
            ),
            (
                'blacksmith',
                'smithy',
                'Your blacksmith can forge magic arms and armour. Like with the alchemist, this requires the blacksmith to have some knowledge of the nature of magic, but they don''t need to be a wizard, thanks to the incredibly potent arcane power held within a creature''s blood. The smithy allows your blacksmith to craft magic arms and armour 10% cheaper and faster than normal per level of the smithy. What items your smith can forge depends on which organs you bring!'
            ),
            (
                'captain',
                'barracks',
                'The first thing your captain does is supervise construction of a barracks. Your barracks temporarily upgrades the experience level of some number of units by one—green units become regular, regular units become seasoned, etc. Your barracks can upgrade a number of units equal to its level. It begins at 1st level (one unit affected) and can be upgraded to 5th level (5 units affected). The units affected are chosen at the start of a battle and cannot be changed until the next battle.'
            ),
            (
                'carpenter',
                'shop',
                'Carpenters lower the cost to build and upkeep siege engines by 10% per level of their shop, and they let you improve your stronghold 10% faster per level of the shop.'
            ),
            (
                'farmer',
                'market',
                'Farmers represent a substantive technological improvement over hunting and gathering. A farm with crops and domesticated animals can produce many times the food required to sustain the farmer''s family. The excess is traded via carters who regularly pass through and buy and sell at the local market. Taxing this commerce provides income for the lord of the stronghold. The stronghold produces 100 gp per season per farmer on your land. Farmers also enjoy having a place to drink ale, talk, and relax after a hard day''s work before they return home to their families. This place is called a tavern, and thus is a small town born.'
            ),
            (
                'mason',
                'quarry',
                'If you attract a mason, there must be a quarry somewhere nearby. This is the equivalent of the artisan''s shop. The quarry starts at 1st level, and the lord can improve it like any other shop. Having a mason on staff means you pay nothing to repair your stronghold after a siege. Your mason will make free repairs worth 250 gp per quarry level per week. A 3rd-level quarry therefore makes free repairs worth 750 gp per week (250 x 3 per week). Masons decrease the cost required to improve your stronghold by 10% per quarry level. This time decrease can be combined with the carpenter''s benefit.'
            ),
            (
                'miner',
                'mine',
                'The ore extracted from your mine is valuable, and you can sell what you don''t use in improving your stronghold and the weapons and armor of your units. A mine produces 500 gp per season. In addition, a mine improves the equipment of some number of your units by one level—a light unit becomes medium, medium becomes heavy, etc. This bonus can be applied to one unit per mine level, as it includes the time and cost of maintaining their improved equipment.'
            ),
            (
                'sage',
                'library',
                'Give your sage a week to search the library and cross-reference the various scrolls, tomes, and codices within, and they can give you secret knowledge of the enemies you plan to fight. Obviously, you''ll need to tell your sage what foes you''ll soon go up against. If you know exactly the kind of monster you''re about to fight, and your sage has the time to do the research, you gain one of the following advantages in combat against that type of creature: • You have advantage on your next attack roll against such a creature. • You negate one resistance on your next attack roll against such a creature. • Such a creature has disadvantage on its next saving throw against your spells or abilities. You can use the chosen advantage on a number of attacks equal to the level of your sage''s library, after which you must take an extended rest to recharge this ability. Your sage also knows the location of the nearest codex. It may be hidden in a ruin within a few miles of your stronghold, or it may be a hundred miles away in the library of the king''s archmage. But your sage knows its whereabouts.'
            ),
            (
                'scribe',
                'tannery',
                'Magical scrolls require rare and unique chemicals to make inks as well as special tanning techniques to cure the vellum in a tannery. All parchment is made from cured animal hide, but vellum is especially durable, resistant to both flame and water, and well suited to holding the unique inks used in a magical scroll without running or fading over time. A scribe would never consider inking onto paper. A paper scroll wouldn''t survive long in the conditions the typical adventuring lord is used to. If a spellcaster of appropriate level is present for at least an hour, a scribe can craft a magic scroll in a fraction of the time it would take a wizard or sorcerer to do it alone. The time and cost are both reduced by 10% per level of the tannery.'
            ),
            (
                'spy',
                'network',
                'Your spy makes it much harder for your enemies and even your allies to know what you''re up to. Your spy increases the DC for agents spying on you by 3 plus 1 per level of your spy''s network. In addition, your spy knows which nearby folk might be interested in signing on to your service. Each time you roll on your followers chart, the spy lets you increase or decrease your roll by up to 3 plus 1 per level of your network. By this method you gain some measure of control over whom you recruit.'
            ),
            (
                'tailor',
                'shop',
                'With a tailor in your retinue, you can, as a reaction, replace the result of any Charisma check with a 12 (before adding bonuses). This can be done a number of times equal to your tailor''s shop level, after which you must take an extended rest to refresh this ability.'
            )
    ) AS shops(artisan, name, description, upgradeable);
    """
)