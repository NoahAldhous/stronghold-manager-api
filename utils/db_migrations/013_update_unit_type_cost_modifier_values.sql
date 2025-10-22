UPDATE unit_types
SET cost_modifier = CASE 
    WHEN type_name = 'flying' THEN 2
    WHEN type_name = 'archers' THEN 1.75
    WHEN type_name = 'cavalry' THEN 1.5
    WHEN type_name = 'levies' THEN 0.75
    WHEN type_name = 'infantry' THEN 1
    WHEN type_name = 'siege engine' THEN 1.5
    ELSE 1
END;