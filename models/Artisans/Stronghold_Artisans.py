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