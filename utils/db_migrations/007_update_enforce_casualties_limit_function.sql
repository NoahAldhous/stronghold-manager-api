CREATE OR REPLACE FUNCTION enforce_casualties_limit()
RETURNS TRIGGER AS $$
DECLARE
    max_size INT;
BEGIN   
    SELECT ssl.stronghold_size INTO max_size
    FROM stronghold_size_levels ssl
    WHERE ssl.stronghold_level = NEW.stronghold_level
        AND ssl.stronghold_type_id = NEW.stronghold_type_id;

    IF NEW.casualties < 0 OR NEW.casualties > max_size THEN
        RAISE EXCEPTION 'Invalid casualties value % for stronghold (max %)', NEW.casualties, max_size;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;