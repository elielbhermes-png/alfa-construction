# ALFA CONSTRUCTION — Security Guide

## Overview

This document describes the security architecture and configuration of the
ALFA Construction website. It covers authentication, database security,
file storage, form security, and secrets management.

## Authentication

- Supabase Authentication is used for all user management.
- The admin dashboard is protected by Supabase Auth.
- Session tokens are handled client-side via `supabase-js` with
  `autoRefreshToken: true` and `persistSession: true`.
- The admin route guard (`AdminLayout`) checks for an active session.
- The first administrator must be created through the Supabase dashboard
  (Auth → Users → New user). No default passwords are set.

## Row Level Security (RLS)

All tables use Row Level Security. Policies defined in `supabase/migrations/0000_init.sql`:

- **Public visitors** can read published projects and published services only.
- **Public visitors** cannot read profiles, contact messages, quotation requests,
  site settings, or audit logs.
- **Authenticated users** can insert contact messages and quotation requests.
- **Admin users** can manage projects, services, media, messages, quotes, and settings.
- **Editors** can manage published content but not user roles.

## Secrets Management

- The Supabase service-role key is NEVER exposed to the browser.
- The Supabase anon key is safe for client-side use (with correct RLS).
- Email provider credentials, if any, are stored in Netlify environment variables.
- Local development uses `.env` (gitignored). Commit only `.env.example`.

## Input Validation

- All form inputs are validated with Zod schemas (`client/src/lib/validation.ts`).
- Server-side validation uses the same schemas.
- File uploads are validated by Supabase Storage policies (file type, size).

## File Storage

- `project-images` storage bucket: public, for published project images.
  - Upload/update/delete restricted to authenticated admins.
- `private-documents` storage bucket: private, for quotation documents.
  - Accessed via short-lived signed URLs after authorization.

## Auditability

- `audit_logs` table tracks administrative actions (publication, deletion,
  settings changes).
- Access to audit logs is restricted to admin users.

## Privacy and Data Retention

- Contact messages and quotation requests are retained for 90 days by default.
- Admin users can delete records manually.
- Personal data is collected only as needed (name, email, phone, etc.).

## Deployment Security Checklist

- [ ] No secrets in the repository
- [ ] Env vars set in Netlify
- [ ] RLS policies applied
- [ ] Storage buckets configured
- [ ] CSP headers set
- [ ] HTTPS enforced

## Remaining Risks

- No security solution is perfect. Regular security reviews are recommended.
- This document is informational; the application is not guaranteed to be
  completely secure against all attack vectors.
