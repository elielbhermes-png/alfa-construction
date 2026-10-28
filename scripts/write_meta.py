import os

os.makedirs('client/src/contexts', exist_ok=True)
os.makedirs('client/src/lib', exist_ok=True)
os.makedirs('supabase/migrations', exist_ok=True)
os.makedirs('server', exist_ok=True)
os.makedirs('.github/workflows', exist_ok=True)

supabase_provider = """import { createClient, SupabaseClient } from '@supabase/supabase-js';
import { createContext, useContext, type ReactNode, useState } from 'react';

export type SupabaseContextValue = {
  supabase: SupabaseClient | null;
  initialized: boolean;
  loading: boolean;
};

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

export const SupabaseContext = createContext<SupabaseContextValue>({
  supabase: null, initialized: false, loading: true,
});

export function SupabaseProvider({ children }: { children: ReactNode }) {
  const [supabase, setSupabase] = useState<SupabaseClient | null>(null);
  const [initialized, setInitialized] = useState(false);
  const [loading, setLoading] = useState(true);

  if (!supabaseUrl || !supabaseAnonKey) {
    setLoading(false);
    return <SupabaseContext.Provider value={{ supabase, initialized, loading }}>{children}</SupabaseContext.Provider>;
  }

  const supabaseClient = createClient(supabaseUrl, supabaseAnonKey, {
    auth: { autoRefreshToken: true, persistSession: true, detectSessionInUrl: true },
  });
  setSupabase(supabaseClient);
  setInitialized(true);
  setLoading(false);

  return <SupabaseContext.Provider value={{ supabase, initialized, loading }}>{children}</SupabaseContext.Provider>;
}

export function useSupabase(): SupabaseContextValue {
  const ctx = useContext(SupabaseContext);
  if (!ctx) throw new Error('useSupabase must be used within SupabaseProvider');
  return ctx;
}

export async function getSupabaseClient(): Promise<SupabaseClient | null> {
  if (!supabaseUrl || !supabaseAnonKey) return null;
  return createClient(supabaseUrl, supabaseAnonKey, {
    auth: { autoRefreshToken: true, persistSession: true, detectSessionInUrl: true },
  });
}
"""

database_types = """export interface Project {
  id: string; title: string; slug: string; short_description: string; description: string;
  location: string | null; category_id: string | null; cover_image_path: string | null;
  status: string; start_date: string | null; completion_date: string | null;
  created_at: string; updated_at: string;
}
export interface ProjectImage { id: string; project_id: string; storage_path: string; caption: string; alt_text: string; display_order: number; created_at: string; }
export interface Service {
  id: string; title: string; slug: string; short_description: string; description: string;
  image_path: string | null; display_order: number; status: string; created_at: string; updated_at: string;
}
export interface ContactMessage {
  id: string; name: string; company: string | null; email: string; phone: string | null;
  subject: string; message: string; status: string; created_at: string; updated_at: string;
}
export interface QuotationRequest {
  id: string; name: string; company: string | null; email: string; phone: string | null;
  service_id: string | null; project_location: string; project_description: string;
  estimated_budget: string | null; desired_start_date: string | null;
  status: string; created_at: string; updated_at: string;
}
export interface Media { id: string; storage_path: string; caption: string; alt_text: string; project_id: string | null; is_public: boolean; created_at: string; updated_at: string; }
export interface SiteSettings { key: string; value: string; created_at: string; updated_at: string; }
"""
supabase_admin = """import { createClient } from '@supabase/supabase-js';

const supabaseUrl = process.env.VITE_SUPABASE_URL;
const serviceKey = process.env.SUPABASE_SERVICE_KEY;

export const supabaseAdmin = createClient(supabaseUrl!, serviceKey!, {
  auth: { autoRefreshToken: false, persistSession: false },
});
"""

netlify = """[build]
  command = "npm run build"
  publish = "client/dist"

[functions]
  directory = "server"

[[redirects]]
  from = "/*.js"
  to = "/_redirects/:splat"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Cache-Control = "no-cache, no-store, must-revalidate"
    Pragma = "no-cache"
    Expires = "0"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
"""

env_example = """# Supabase
VITE_SUPABASE_URL = "[REDACTED]"
VITE_SUPABASE_ANON_KEY = "[REDACTED]"

# Email provider (optional)
# EMAIL_API_KEY = "[REDACTED]"
# EMAIL_FROM = "no-reply@alfa-constructions.com"

# Netlify
NETLIFY_SITE_ID = "[REDACTED]"

# SendGrid (optional)
# SENDGRID_API_KEY = "[REDACTED]"
# SENDGRID_FROM_EMAIL = "no-reply@alfa-constructions.com"
"""

migrations = """-- 0000_init.sql
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
"""
migrations2 = """-- 0001_add_site_settings.sql
-- Seed default site settings
INSERT INTO site_settings (key, value, created_at, updated_at) VALUES
('site_settings', '{"site_name":"ALFA CONSTRUCTION","logo":"","contact_email":"ali-safa@alfa-constructions.com","phone":"+242 06 822 22 20","address":"Avenue Docteur Cardorelle, Songolo, Congo","website":"www.alfa-constructions.Netlify.com","about":"ALFA Construction est un groupe de construction de reference en Republique du Congo.","footer":"","hours":"Lun - Ven : 08h00 - 18h00"}', NOW(), NOW())
ON CONFLICT (key) DO UPDATE SET value = EXCLUDED.value, updated_at = NOW();
"""

migrations3 = """-- 0002_add_audit_logs_seed.sql
-- Seed audit logs (none needed, kept for structure)
INSERT INTO audit_logs (action, details, created_at) VALUES ('init', '{}', NOW());
"""

supabase_client = """import { createClient, SupabaseClient } from '@supabase/supabase-js';
import { createContext, useContext, type ReactNode, useState } from 'react';

export type SupabaseContextValue = {
  supabase: SupabaseClient | null;
  initialized: boolean;
  loading: boolean;
};

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

export const SupabaseContext = createContext<SupabaseContextValue>({ supabase: null, initialized: false, loading: true });

export function SupabaseProvider({ children }: { children: ReactNode }) {
  const [supabase, setSupabase] = useState<SupabaseClient | null>(null);
  const [initialized, setInitialized] = useState(false);
  const [loading, setLoading] = useState(true);

  if (!supabaseUrl || !supabaseAnonKey) {
    setLoading(false);
    return <SupabaseContext.Provider value={{ supabase, initialized, loading }}>{children}</SupabaseContext.Provider>;
  }

  const supabaseClient = createClient(supabaseUrl, supabaseAnonKey, {
    auth: { autoRefreshToken: true, persistSession: true, detectSessionInUrl: true },
  });
  setSupabase(supabaseClient);
  setInitialized(true);
  setLoading(false);

  return <SupabaseContext.Provider value={{ supabase, initialized, loading }}>{children}</SupabaseContext.Provider>;
}

export function useSupabase(): SupabaseContextValue {
  const ctx = useContext(SupabaseContext);
  if (!ctx) throw new Error('useSupabase must be used within SupabaseProvider');
  return ctx;
}

export async function getSupabaseClient(): Promise<SupabaseClient | null> {
  if (!supabaseUrl || !supabaseAnonKey) return null;
  return createClient(supabaseUrl, supabaseAnonKey, { auth: { autoRefreshToken: true, persistSession: true, detectSessionInUrl: true } });
}
"""

server_index = """import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { type ServeHandlerInfo } from "https://deno.land/std@0.168.0/http/server.ts";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

async function validateSupabase(env: Record<string, string | undefined>) {
  const url = env.VITE_SUPABASE_URL;
  const anonKey = env.VITE_SUPABASE_ANON_KEY;
  if (!url || !anonKey) return null;
  const { createClient } = await import("@supabase/supabase-js");
  return createClient(url, anonKey);
}

const handler: ServeHandlerInfo = (req) => {
  if (req.method === "OPTIONS") return new Response(null, { headers: corsHeaders });

  try {
    const supabase = await validateSupabase(Deno.env.toObject());
    if (!supabase) {
      return new Response(JSON.stringify({ error: "Unsupported" }), { status: 400, headers: { "Content-Type": "application/json" } });
    }

    const body = await req.json();
    const { name, company, email, phone, subject, message, privacy } = body;

    if (req.url.includes("/contact")) {
      if (!name || !email || !subject || !message || !privacy) {
        return new Response(JSON.stringify({ error: "Missing or invalid fields" }), { status: 400, headers: { "Content-Type": "application/json" } });
      }
      const { error } = await supabase.from("contact_messages").insert({
        name, company: company || null, email, phone: phone || null, subject, message, status: "new"
      });
      if (error) return new Response(JSON.stringify({ error: error.message }), { status: 500, headers: { "Content-Type": "application/json" } });
      return new Response(JSON.stringify({ success: true }), { headers: { "Content-Type": "application/json" } });
    }

    if (req.url.includes("/quotation")) {
      const { service, projectLocation, projectDescription, estimatedBudget, desiredStartDate } = body;
      if (!name || !email || !phone || !service || !projectLocation || !projectDescription) {
        return new Response(JSON.stringify({ error: "Missing or invalid fields" }), { status: 400, headers: { "Content-Type": "application/json" } });
      }
      const { error } = await supabase.from("quotation_requests").insert({
        name, company: company || null, email, phone, service_id: service, project_location: projectLocation,
        project_description: projectDescription, estimated_budget: estimatedBudget || null, desired_start_date: desiredStartDate || null, status: "new"
      });
      if (error) return new Response(JSON.stringify({ error: error.message }), { status: 500, headers: { "Content-Type": "application/json" } });
      return new Response(JSON.stringify({ success: true }), { headers: { "Content-Type": "application/json" } });
    }

    return new Response(JSON.stringify({ error: "Not found" }), { status: 404, headers: { "Content-Type": "application/json" } });
  } catch (e) {
    return new Response(JSON.stringify({ error: e.message }), { status: 500, headers: { "Content-Type": "application/json" } });
  }
};

serve(handler, { port: 4000, onListen: ({ port }) => console.log(`API on port ${port}`) });
"""

ci_yaml = """name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm install
      - run: npm run build
      - run: npm audit --audit-level=high
"""

with open('client/src/contexts/SupabaseProvider.tsx', 'w') as f:
    f.write(supabase_provider)
with open('client/src/lib/database.types.ts', 'w') as f:
    f.write(database_types)
with open('client/src/lib/supabaseAdmin.ts', 'w') as f:
    f.write(supabase_admin)
with open('netlify.toml', 'w') as f:
    f.write(netlify)
with open('.env.example', 'w') as f:
    f.write(env_example)
with open('supabase/migrations/0000_init.sql', 'w') as f:
    f.write(migrations)
with open('supabase/migrations/0001_add_site_settings.sql', 'w') as f:
    f.write(migrations2)
with open('supabase/migrations/0002_add_audit_logs_seed.sql', 'w') as f:
    f.write(migrations3)
with open('server/index.ts', 'w') as f:
    f.write(server_index)
with open('.github/workflows/ci.yml', 'w') as f:
    f.write(ci_yaml)

print("Meta files written")
