CREATE_RETAINER_ARMOUR_CLASSES_TABLE = (
   """CREATE TABLE IF NOT EXISTS retainer_armour_classes (
       id SERIAL PRIMARY KEY,
       armour_type TEXT NOT NULL,
       armour_class INT NOT NULL
    );"""
)

POPULATE_RETAINER_ARMOUR_CLASSES_TABLE = (
    """INSERT INTO retainer_armour_classes (
        armour_type,
        armour_class
    ) SELECT 
        armour.type,
        armour.cost
    FROM (
        VALUES
            (
                'light',
                12
            ),
            (
                'medium',
                15
            ),
            (
                'heavy',
                18
            )
    ) AS armour(type, cost);
    """
)