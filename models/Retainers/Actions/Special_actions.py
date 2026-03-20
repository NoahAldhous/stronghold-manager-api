CREATE_SPECIAL_ACTIONS_TABLE = (
    """CREATE TABLE IF NOT EXISTS special_actions (
        id SERIAL PRIMARY KEY,
        action_name TEXT NOT NULL,
        action_description TEXT NOT NULL,
        action_level INT CHECK (action_level BETWEEN 0 AND 7) 
    )"""
)

POPULATE_SPECIAL_ACTIONS_TABLE = (
    """INSERT INTO special_actions (
        action_name,
        action_description,
        action_level
    ) SELECT 
        actions.name,
        actions.description,
        actions.level
    FROM (
        VALUES
            (
                'orison',
                'as an action, choose an ally a healer can see within 30 feet. On its next attack roll or saving throw, roll a d4 and add the result to the ally''s result.',
                0
            )
    ) AS actions(name, description, level);
        """
)