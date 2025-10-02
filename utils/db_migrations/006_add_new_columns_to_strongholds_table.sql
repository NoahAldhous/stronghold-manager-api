ALTER TABLE strongholds
    ADD COLUMN class_feature_improvement_uses INTEGER NOT NULL DEFAULT 0,
    ADD COLUMN casualties INTEGER NOT NULL DEFAULT 0;

UPDATE strongholds
SET class_feature_improvement_uses = stronghold_level;

UPDATE strongholds s
SET casualties = 0
FROM stronghold_size_levels ssl
WHERE ssl.stronghold_level = s.stronghold_level
    AND ssl.stronghold_type_id = s.stronghold_type_id;

ALTER TABLE strongholds
    ADD CONSTRAINT check_class_feature_improvement_uses_range
        CHECK (class_feature_improvement_uses >= 0 AND class_feature_improvement_uses <= stronghold_level);

CREATE OR REPLACE FUNCTION enforce_casualties_limit()
RETURNS TRIGGER AS $$
DECLARE
    max_size INT;
BEGIN   
    SELECT ssl.size INTO max_size
    FROM stronghold_size_levels ssl
    WHERE ssl.stronghold_level = NEW.stronghold_level
        AND ssl.stronghold_type_id = NEW.stronghold_type_id;

    IF NEW.casualties < 0 OR NEW.casualties > max_size THEN
        RAISE EXCEPTION 'Invalid casualties value % for stronghold (max %)', NEW.casualties, max_size;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_enforce_casualties
BEFORE INSERT OR UPDATE ON strongholds
FOR EACH ROW EXECUTE FUNCTION enforce_casualties_limit();