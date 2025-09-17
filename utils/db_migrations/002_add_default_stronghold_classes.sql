UPDATE strongholds
SET stronghold_class_id = (
    SELECT id FROM stronghold_classes WHERE class_name = 'fighter'
);

ALTER TABLE strongholds
ALTER COLUMN stronghold_class_id SET NOT NULL;