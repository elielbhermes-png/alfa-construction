-- 0002_add_audit_logs_seed.sql
-- Seed audit logs (none needed, kept for structure)
INSERT INTO audit_logs (action, details, created_at) VALUES ('init', '{}', NOW());
