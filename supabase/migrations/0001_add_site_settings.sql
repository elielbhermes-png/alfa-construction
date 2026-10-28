-- 0001_add_site_settings.sql
-- Seed default site settings
INSERT INTO site_settings (key, value, created_at, updated_at) VALUES
('site_settings', '{"site_name":"ALFA CONSTRUCTION","logo":"","contact_email":"ali-safa@alfa-constructions.com","phone":"+242 06 822 22 20","address":"Avenue Docteur Cardorelle, Songolo, Congo","website":"www.alfa-constructions.Netlify.com","about":"ALFA Construction est un groupe de construction de reference en Republique du Congo.","footer":"","hours":"Lun - Ven : 08h00 - 18h00"}', NOW(), NOW())
ON CONFLICT (key) DO UPDATE SET value = EXCLUDED.value, updated_at = NOW();
