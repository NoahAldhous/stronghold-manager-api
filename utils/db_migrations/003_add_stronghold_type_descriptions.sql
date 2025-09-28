ALTER TABLE stronghold_types
ADD COLUMN stronghold_type_description TEXT;

UPDATE stronghold_types
SET stronghold_type_description = CASE
    WHEN type_name = 'keep' THEN 'raise armies and improve your fighting ability.'
    WHEN type_name = 'tower' THEN 'research new spells.'
    WHEN type_name = 'temple' THEN 'summon extraplanar allies to aid you in battle.'
    WHEN type_name = 'establishment' THEN 'collect secrets and generate cash.'
    WHEN type_name = 'castle' THEN 'create a combination of the other four strongholds.'
    ELSE 'unknown stronghold type'
END;

ALTER TABLE stronghold_types
ALTER COLUMN stronghold_type_description SET NOT NULL;

ALTER TABLE stronghold_types
ADD CONSTRAINT unique_stronghold_type_description UNIQUE (stronghold_type_description);