CREATE_STRONGHOLD_ARTISANS_TABLE = (
    """CREATE TABLE IF NOT EXISTS stronghold_artisans (
        id SERIAL PRIMARY KEY,
        stronghold_id INT,
        alchemist INT CHECK (alchemist BETWEEN 0 AND 5),
        blacksmith INT CHECK (blacksmith BETWEEN 0 AND 5),
        captain INT CHECK (captain BETWEEN 0 AND 5),
        carpenter INT CHECK (carpenter BETWEEN 0 AND 5),
        farmer INT CHECK (farmer BETWEEN 0 AND 5),
        mason INT CHECK (mason BETWEEN 0 AND 5),
        miner INT CHECK (miner BETWEEN 0 AND 5),
        sage INT CHECK (sage BETWEEN 0 AND 5),
        scribe INT CHECK (scribe BETWEEN 0 AND 5),
        spy INT CHECK (spy BETWEEN 0 AND 5), 
        tailor INT CHECK (tailor BETWEEN 0 AND 5)  
    );"""
)

INSERT_INITIAL_STRONGHOLD_ARTISANS = (
    """INSERT INTO stronghold_artisans (
        stronghold_id,
        alchemist,
        blacksmith,
        captain,
        carpenter,
        farmer,
        mason,
        miner,
        sage,
        scribe,
        spy,
        tailor    
    ) VALUES (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,    
        %s,
        %s,
        %s,
        %s,
        %s,
        %s    
    ) RETURNING stronghold_id;"""
)

# This should be updated to create a proper JSON object taking from the other artisan tables, with associated costs, shop names and benefits. 
GET_STRONGHOLD_ARTISANS_BY_STRONGHOLD_ID = (
    """SELECT * FROM stronghold_artisans WHERE stronghold_id = %s;"""
)

