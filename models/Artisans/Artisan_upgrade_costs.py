CREATE_ARTISAN_UPGRADE_COSTS_TABLE = (
    "CREATE TABLE IF NOT EXISTS artisan_upgrade_costs_table (id SERIAL PRIMARY KEY, artisan_level INT UNIQUE NOT NULL, cost INT UNIQUE NOT NULL);"
)

POPULATE_ARTISAN_UPGRADE_COSTS_TABLE = (
    """INSERT INTO artisan_upgrade_costs_table (
        artisan_level,
        cost
    ) SELECT
        costs.level,
        costs.cost
    FROM (
        VALUES
            (
                1,
                0
            ),
            (
                2,
                1000
            ),
            (
                3,
                1500
            ),
            (
                4,
                2000
            ),
            (
                5,
                2500
            )
    ) AS costs(level, cost);
    """
)