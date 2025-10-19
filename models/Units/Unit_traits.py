CREATE_UNIT_TRAITS_TABLE = (
    """CREATE TABLE IF NOT EXISTS unit_traits (
        id SERIAL PRIMARY KEY,
        trait_name TEXT UNIQUE NOT NULL,
        trait_description TEXT UNIQUE NOT NULL,
        cost INT
    );"""
)

POPULATE_UNIT_TRAITS_TABLE = (
    """INSERT INTO unit_traits (
        trait_name,
        trait_description,
        cost    
    ) SELECT 
        traits.name,
        traits.description,
        traits.cost
    FROM (
        VALUES 
            (
                'amphibious',
                'This unit does not suffer terrain penalties from fighting in water or on land.',
                50
            ),
            (
                'bred for war',
                'This unit cannot be diminished, and cannot have disadvantage on Morale checks.',
                100
            ),
            (
                'brutal',
                'This unit inflicts 2 casualties on a successful Power check.',
                200
            ),
            (
                'courageous',
                'Once per battle, this unit can choose to succeed on a Morale check it just failed.',
                50
            ),
            (
                'eternal',
                'This unit cannot be horrified, and it always succeeds on Morale checks to attack undead and fiends',
                50
            ),
            (
                'frenzy',
                'If this unit dimishes an enemy unit, it immediately makes a free attack against that unit.',
                50
            ),
            (
                'horrify',
                'If this unit inflicts a casualty on an enemy unit, that unit must make a DC15 Morale check. Failure exhausts the unit.',
                200
            ),
            (
                'martial',
                'If this unit succeeds on a Power check and its size is greater than the defending unt, it inflicts 2 casualties.',
                100
            ),
            (
                'mindless',
                'This unit cannot fail Morale checks.',
                100
            ),
            (
                'regenerate',
                'When this unit refreshes, increment its casualty die. This trait ceases to function if the unit suffers a casualty from battle magic.',
                200
            ),
            (
                'ravenous',
                'While any enemy unit is diminished, this unit can spend a round feeding on the corpses to increment their casualty die.',
                50
            ),
            (
                'hurl rocks',
                'If this unit succeeds on an Attack check, it inflicts 2 casualties. Against fortifications, it inflicts 1d6 casualties.',
                250
            ),
            (
                'savage',
                'This unit has advantage on their first Attack check it makes each battle.',
                50
            ),
            (
                'stalwart',
                'Enemy battle magic has disadvantage on power checks against this unit.',
                50
            ),
            (
                'twisting roots',
                'As an action, this unit can sap the walls of a fortification. Siege units have advantage on Power checks against sapped fortifications.',
                200
            ),
            (
                'undead',
                'Green and regular troops must pass a Morale check to attack this unit. Each enemy unit need only do this once.',
                50
            ),
            (
                'charge',
                'Cannot use while engaged. A Charge is an attack with advantage on the Attack check. It inflicts 2 casualties on a successful Power check. The charging unit is then engaged with the defending unit and must make a DC13 Morale check to disengage.',
                0
            ),
            (
                'always diminished',
                'This unit is always diminished.',
                0
            )
    ) AS traits(name, description, cost);
    """
)