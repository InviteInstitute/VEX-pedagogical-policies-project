BEGIN;

ALTER TABLE chat.messages
    ADD COLUMN IF NOT EXISTS stage INTEGER;

ALTER TABLE current_state.state_snapshots
    ADD COLUMN IF NOT EXISTS stage INTEGER;

COMMIT;
