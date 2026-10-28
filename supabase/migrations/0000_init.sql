-- 0000_init.sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id),
  email VARCHAR(255) NOT NULL,
  display_name VARCHAR(255),
  role TEXT NOT NULL DEFAULT 'editor',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE projects (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  slug VARCHAR(255) NOT NULL,
  short_description TEXT,
  description TEXT,
  location VARCHAR(255),
  category_id VARCHAR(50),
  cover_image_path VARCHAR(500),
  status VARCHAR(20) NOT NULL DEFAULT 'draft',
  start_date DATE,
  completion_date DATE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  created_by UUID REFERENCES auth.users(id)
);

CREATE TABLE services (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  slug VARCHAR(255) NOT NULL,
  short_description TEXT,
  description TEXT,
  image_path VARCHAR(500),
  display_order INTEGER DEFAULT 0,
  status VARCHAR(20) NOT NULL DEFAULT 'draft',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE site_settings (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  key VARCHAR(255) NOT NULL UNIQUE,
  value JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE contact_messages (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  company VARCHAR(255),
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(30),
  subject VARCHAR(255) NOT NULL,
  message TEXT NOT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'new',
  notes TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE quotation_requests (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  company VARCHAR(255),
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(30) NOT NULL,
  service_id VARCHAR(50),
  project_location VARCHAR(255) NOT NULL,
  project_description TEXT NOT NULL,
  estimated_budget VARCHAR(50),
  desired_start_date VARCHAR(50),
  status VARCHAR(20) NOT NULL DEFAULT 'new',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE audit_logs (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES auth.users(id),
  action VARCHAR(100) NOT NULL,
  entity_type VARCHAR(100),
  entity_id UUID,
  details JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE media (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  storage_path VARCHAR(500) NOT NULL,
  caption VARCHAR(500),
  alt_text VARCHAR(500),
  project_id UUID REFERENCES projects(id),
  is_public BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_projects_category ON projects(category_id);
CREATE INDEX idx_projects_slug ON projects(slug);
CREATE INDEX idx_services_status ON services(status);
CREATE INDEX idx_contact_messages_status ON contact_messages(status);
CREATE INDEX idx_quotation_requests_status ON quotation_requests(status);

CREATE OR REPLACE FUNCTION update_updated_at() RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER projects_updated_at BEFORE UPDATE ON projects FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER services_updated_at BEFORE UPDATE ON services FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER contact_messages_updated_at BEFORE UPDATE ON contact_messages FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER quotation_requests_updated_at BEFORE UPDATE ON quotation_requests FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER media_updated_at BEFORE UPDATE ON media FOR EACH ROW EXECUTE FUNCTION update_updated_at();

-- RLS policies
ALTER TABLE projects ENABLE ROW LEVEL SECURITY;
ALTER TABLE services ENABLE ROW LEVEL SECURITY;
ALTER TABLE contact_messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE quotation_requests ENABLE ROW LEVEL SECURITY;
ALTER TABLE media ENABLE ROW LEVEL SECURITY;
ALTER TABLE site_settings ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;

-- Public: published projects
CREATE POLICY "Public can read published projects" ON projects FOR SELECT USING (status = 'published');

-- Public: published services
CREATE POLICY "Public can read published services" ON services FOR SELECT USING (status = 'published');

-- Public: contact messages are private
CREATE POLICY "Public cannot read contact messages" ON contact_messages FOR SELECT USING (false);

-- Public: quotation requests are private
CREATE POLICY "Public cannot read quotation requests" ON quotation_requests FOR SELECT USING (false);

-- Public: media is private
CREATE POLICY "Public cannot read media" ON media FOR SELECT USING (false);

-- Public: site settings are private
CREATE POLICY "Public cannot read site settings" ON site_settings FOR SELECT USING (false);

-- Public: audit logs are private
CREATE POLICY "Public cannot read audit logs" ON audit_logs FOR SELECT USING (false);

-- Profiles: public visitors can read their own profile
CREATE POLICY "Public can read own profile" ON profiles FOR SELECT USING (auth.uid() = id);

-- Authenticated users can insert contact messages
CREATE POLICY "Authenticated users can insert contact messages" ON contact_messages FOR INSERT WITH CHECK (auth.uid() IS NOT NULL);

-- Authenticated users can insert quotation requests
CREATE POLICY "Authenticated users can insert quotation requests" ON quotation_requests FOR INSERT WITH CHECK (auth.uid() IS NOT NULL);

-- Authenticated users can update their own contact messages
CREATE POLICY "Authenticated users can update own message" ON contact_messages FOR UPDATE USING (auth.uid() = current_setting('request.jwt.claim.sub')::uuid);

-- Only admins can manage projects
CREATE POLICY "Admins can manage projects" ON projects FOR ALL USING (
  EXISTS (SELECT 1 FROM profiles WHERE profiles.id = auth.uid() AND profiles.role IN ('admin', 'editor'))
);

-- Only admins can manage services
CREATE POLICY "Admins can manage services" ON services FOR ALL USING (
  EXISTS (SELECT 1 FROM profiles WHERE profiles.id = auth.uid() AND profiles.role IN ('admin', 'editor'))
);

-- Only admins can manage media
CREATE POLICY "Admins can manage media" ON media FOR ALL USING (
  EXISTS (SELECT 1 FROM profiles WHERE profiles.id = auth.uid() AND profiles.role IN ('admin', 'editor'))
);

-- Only admins can manage messages
CREATE POLICY "Admins can manage messages" ON contact_messages FOR ALL USING (
  EXISTS (SELECT 1 FROM profiles WHERE profiles.id = auth.uid() AND profiles.role IN ('admin', 'editor'))
);

-- Only admins can manage quotes
CREATE POLICY "Admins can manage quotes" ON quotation_requests FOR ALL USING (
  EXISTS (SELECT 1 FROM profiles WHERE profiles.id = auth.uid() AND profiles.role IN ('admin', 'editor'))
);

-- Only admins can manage site settings
CREATE POLICY "Admins can manage site settings" ON site_settings FOR ALL USING (
  EXISTS (SELECT 1 FROM profiles WHERE profiles.id = auth.uid() AND profiles.role = 'admin')
);

-- Only admins can manage audit logs
CREATE POLICY "Admins can manage audit logs" ON audit_logs FOR ALL USING (
  EXISTS (SELECT 1 FROM profiles WHERE profiles.id = auth.uid() AND profiles.role = 'admin')
);

-- Only admins can read profiles
CREATE POLICY "Admins can read profiles" ON profiles FOR ALL USING (
  EXISTS (SELECT 1 FROM profiles WHERE profiles.id = auth.uid() AND profiles.role = 'admin')
);
