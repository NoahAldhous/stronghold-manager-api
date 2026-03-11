ALTER TABLE stronghold_artisans
ADD CONSTRAINT unique_stronghold_artisan
UNIQUE (stronghold_id, artisan_id)