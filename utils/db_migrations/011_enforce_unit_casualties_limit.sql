CREATE OR REPLACE FUNCTION check_casualties_not_greater_than_size()
RETURNS TRIGGER AS $$
DECLARE
    max_size INT;
BEGIN
    SELECT unit_size INTO max_size FROM unit_size_levels WHERE id = NEW.size_id;

    IF max_size IS NULL THEN
        RAISE EXCEPTION 'Invalid size_id: %', NEW.size_id;
    END IF;

    IF NEW.casualties > max_size THEN
        RAISE EXCEPTION 'Casualties (%) cannot exceed unit size (%)', NEW.casualties, max_size;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS enforce_casualties_size_limit ON units;

CREATE TRIGGER enforce_casualties_size_limit
BEFORE INSERT OR UPDATE ON units
FOR EACH ROW
EXECUTE FUNCTION check_casualties_not_greater_than_size();