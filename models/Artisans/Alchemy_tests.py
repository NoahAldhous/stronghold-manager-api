CREATE_ALCHEMY_TESTS_TABLE = (
    """CREATE TABLE IF NOT EXISTS alchemy_tests (
        id SERIAL PRIMARY KEY,
        organ TEXT NOT NULL,
        magic_item TEXT NOT NULL,
        crafted_by TEXT NOT NULL,
        medicine_dc_base INT NOT NULL,
        medicine_dc_bonus TEXT NOT NULL,
        artisan_id INT,
        FOREIGN KEY(artisan_id) REFERENCES artisan_shops(id) ON DELETE CASCADE    
    );"""
)

POPULATE_ALCHEMY_TESTS_TABLE = (
    """INSERT INTO alchemy_tests (
        organ,
        magic_item,
        crafted_by,
        medicine_dc_base,
        medicine_dc_bonus,
        artisan_id
    ) SELECT 
        tests.organ,
        tests.item,
        tests.crafted,
        tests.dc_base,
        tests.dc_bonus,
        shops.id
    FROM (
        VALUES
            (
                'eyes',
                'potion of invisibility to monsters',
                'alchemist',
                15,
                '0'
            ),
            (
                'blood',
                'arrows of monsters slaying',
                'blacksmith',
                10,
                'CR'
            ),
            (
                'blood',
                'sword of monster slaying',
                'blacksmith',
                10,
                'CR'
            ),
            (
                'brains',
                'potion of monster control',
                'alchemist',
                12,
                'CR'
            ),
            (
                'heart',
                'scroll of protection from monsters',
                'scribe',
                12,
                '0'
            )
    ) AS tests(organ, item, crafted, dc_base, dc_bonus)
        JOIN artisan_shops as shops
            ON tests.crafted = shops.artisan_name
    """
)