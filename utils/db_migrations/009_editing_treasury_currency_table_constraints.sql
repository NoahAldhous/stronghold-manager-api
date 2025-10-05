ALTER TABLE treasury_currency
DROP CONSTRAINT IF EXISTS treasury_currency_stronghold_id_fkey;

ALTER TABLE treasury_currency
ADD CONSTRAINT fk_treasury_currency_stronghold_id
FOREIGN KEY (stronghold_id)
REFERENCES strongholds(id)
ON DELETE CASCADE,
ADD CONSTRAINT unique_treasury_per_stronghold
UNIQUE (stronghold_id);