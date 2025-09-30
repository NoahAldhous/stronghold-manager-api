UPDATE stronghold_type_features
SET feature_description = CASE
    WHEN feature_name = 'raising units' THEN 'Reduce the cost and upkeep of units by 10% per level. Gain 2 units per level of stronghold upon construction.'
    WHEN feature_name = 'training' THEN 'Gain a bonus based on one of your armour or weapon proficiencies.'
    WHEN feature_name = 'concordance' THEN 'Petition your deity or patron for aid, and receive blessings, powerful allies, or a bonk on the head for bothering them.'
    WHEN feature_name = 'spell research' THEN 'Create enhanced versions of your existing spells, and name them after yourself.'
    WHEN feature_name = 'rumors' THEN 'Gather intel about monsters you might be fighting, a dungeon''s secret doors, traps, and puzzles, or the location of powerful magic items.'
    WHEN feature_name = 'favours' THEN 'Pay another stronghold to gain one of their benefits temporarily.'
    WHEN feature_name = 'revenue' THEN 'Your stronghold makes money. You gain 1,000gp per stronghold level per season.'
    ELSE 'unknown stronghold feature'
END;