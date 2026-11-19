PRAGMA foreign_keys = ON;
CREATE TRIGGER IF NOT EXISTS trg_tasks_updated_at
AFTER UPDATE ON tasks
FOR EACH ROW
WHEN NEW.updated_at = OLD.updated_at
BEGIN
UPDATE tasks
SET updated_at = CURRENT_TIMESTAMP
WHERE id = OLD.id;
END;