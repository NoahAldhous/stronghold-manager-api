CREATE_TREASURY_CURRENCY_TABLE = (
    """CREATE TABLE IF NOT EXISTS treasury_currency
    (
        id SERIAL PRIMARY KEY,
        stronghold_id INT,
        platinum INT,
        gold INT,
        silver INT,
        electrum INT,
        copper INT,
        FOREIGN KEY(stronghold id) REFERENCES strongholds(id)
    );"""
)

CREATE_TREASURY_ITEMS_TABLE = (
    """CREATE TABLE IF NOT EXISTS treasury_items
    (
        id SERIAL PRIMARY KEY,
        stronghold_id INT,
        currency_id INT,
        name TEXT,
        description TEXT,
        value INT
    )
    """
)

GET_ALL_TREASURY_CURRENCY = (
    "SELECT * FROM treasury_currency;"
)

UPDATE_TREASURY_CURRENCY = (
    """UPDATE treasury_currency 
        SET platinum = %s,
        SET gold = %s,
        SET silver = %s,
        SET electrum = %s,
        SET copper = %s
        WHERE stronghold_id = %s;"""
)

INSERT_TREASURY_CURRENCY = (
    """INSERT INTO treasury_currency (
        stronghold_id,
        platinum,
        gold,
        silver,
        electrum,
        copper
    ) VALUES (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    ) RETURNING stronghold_id;"""
)

INSERT_TREASURY_ITEM = (
    """INSERT INTO treasury_items (
        stronghold_id,
        currency_id,
        name,
        description,
        value
    ) VALUES(
        %s, %s, %s, %s, %s    
    )"""
)