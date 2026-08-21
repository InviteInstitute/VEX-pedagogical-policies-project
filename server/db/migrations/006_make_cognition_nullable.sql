BEGIN;

ALTER TABLE current_state.state_snapshots ALTER COLUMN cognition DROP NOT NULL;

COMMIT;
