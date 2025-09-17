ALTER TABLE strongholds
ADD COLUMN stronghold_class_id INT;

ALTER TABLE strongholds
ADD CONSTRAINT fk_strongholds_class
FOREIGN KEY (stronghold_class_id) REFERENCES stronghold_classes(id);