CREATE TABLE IF NOT EXISTS treasury_currency
    (
        id SERIAL PRIMARY KEY,
        stronghold_id INT,
        platinum INT,
        gold INT,
        silver INT,
        electrum INT,
        copper INT,
        FOREIGN KEY(stronghold_id) REFERENCES strongholds(id)
    );