CREATE_STRONGHOLD_ARTISANS_TABLE = (
    """CREATE TABLE IF NOT EXISTS stronghold_artisans (
        id SERIAL PRIMARY KEY,
        stronghold_id INT NOT NULL REFERENCES strongholds(id) ON DELETE CASCADE,
        artisan_id INT NOT NULL REFERENCES artisan_shops(id) ON DELETE CASCADE,
        shop_level INT CHECK (shop_level BETWEEN 1 AND 5)
    )"""
)

INSERT_STRONGHOLD_ARTISAN = (
    """INSERT INTO stronghold_artisans (
        stronghold_id,
        artisan_id,
        shop_level
        ) VALUES (
            %s,
            (
                SELECT id
                    FROM artisan_shops
                    WHERE artisan_name = %s
            ),
            %s
        )
        RETURNING id;
        """
)

UPDATE_STRONGHOLD_ARTISAN = (
    """UPDATE stronghold_artisans s
        SET s.level = %s
        FROM artisan_shops a
        WHERE s.artisan_id = a.id
        AND s.stronghold_id = %s
        AND a.artisan_name = %s
        RETURNING s.*;
    """
)

GET_STRONGHOLD_ARTISANS_BY_STRONGHOLD_ID = (
    """SELECT * FROM stronghold_artisans WHERE stronghold_id = %s;"""
)

# Delete table
DELETE_STRONGHOLD_ARTISANS_TABLE = (
    """DROP TABLE IF EXISTS stronghold_artisans;"""
)