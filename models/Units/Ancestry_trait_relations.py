CREATE_ANCESTRY_TRAIT_RELATIONS_TABLE = (
    """CREATE TABLE IF NOT EXISTS ancestry_trait_relations (
        id SERIAL PRIMARY KEY,
        ancestry_id INT,
        trait_id INT,
        FOREIGN KEY(ancestry_id) REFERENCES unit_ancestries(id) ON DELETE CASCADE,
        FOREIGN KEY(trait_id) REFERENCES unit_traits(id) ON DELETE CASCADE 
    );"""
)

POPULATE_ANCESTRY_TRAIT_RELATIONS_TABLE = (
    """INSERT INTO ancestry_trait_relations (
        ancestry_id,
        trait_id    
    ) SELECT
        ancestries.id,
        traits.id
    FROM (
        VALUES
            (
                'bugbear',
                'martial'
            ),
            (
                'dragonborn',
                'courageous'
            ),
            (
                'dwarf',
                'stalwart'
            ),
            (
                'elf',
                'eternal'
            ),
            (
                'elf (winged)',
                'eternal'
            ),
            (
                'ghoul',
                'undead'
            ),
            (
                'ghoul',
                'horrify'
            ),
            (
                'ghoul',
                'ravenous'
            ),
            (
                'gnoll',
                'frenzy'
            ),
            (
                'hobgoblin',
                'bred for war'
            ),
            (
                'hobgoblin',
                'martial'
            ),
            (
                'human',
                'courageous'
            ),
            (
                'lizardfolk',
                'amphibious'
            ),
            (
                'ogre',
                'brutal'
            ),
            (
                'orc',
                'savage'
            ),
            (
                'skeleton',
                'undead'
            ),
            (
                'skeleton',
                'mindless'
            ),
            (
                'treant',
                'siege engine'
            ),
            (
                'treant',
                'twisting roots'
            ),
            (
                'treant',
                'hurl rocks'
            ),
            (
                'troll',
                'regenerate'
            ),
            (
                'zombie',
                'undead'
            ),
            (
                'zombie',
                'mindless'
            )
    ) AS relations(ancestry, trait)
        JOIN unit_ancestries AS ancestries
            ON relations.ancestry = ancestries.ancestry_name
        JOIN unit_traits AS traits
            ON relations.trait = traits.trait_name;
    """
)