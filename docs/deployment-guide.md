# ALFA CONSTRUCTION — Deployment Guide

## Overview

This guide covers the complete deployment of the ALFA Construction website
to Netlify with Supabase backend.

## Prerequisites

- Node.js >= 18
- npm >= 9
- GitHub account
- Supabase project (free tier works)
- Netlify account

## Step 1: Create the GitHub Repository

1. Go to https://github.com/new
2. Repository name: `alfa-construction-website`
3. Visibility: **Public** (or private, if you plan to keep it private)
4. Initialize with README (optional)
5. Click **Create repository**

## Step 2: Push the Code

```bash
cd /c/Users/elielb/alfa-constructions-template
git init
git add .
git commit -m "Initial ALFA Construction website"
git branch -M main
# Add remote and push
git remote add origin https://github.com/<your-user>/alfa-construction-website.git
git push -u origin main
```

## Step 3: Configure Supabase

1. Go to https://supabase.com/dashboard and create a new project.
2. Wait for the project to be ready.
3. Go to **Database** → **Migrations** → **New migration**.
4. Upload `supabase/migrations/0000_init.sql`.
5. Repeat for `0001_add_site_settings.sql` and `0002_add_audit_logs_seed.sql`.
6. Go to **Storage** → **New bucket**:
   - Name: `project-images`, Public: Yes, File size limits: 10MB
   - Name: `private-documents`, Public: No, for quotation documents
7. Go to **Auth** → **Providers**:
   - Enable **Email** provider (for password reset, if needed).
8. Go to **Settings** → **API**:
   - Note your **Project URL** and **anon public** key.

## Step 4: Configure Netlify

1. Go to https://app.netlify.com/ and click **Add new site** → **Import an existing project**.
2. Connect your GitHub account.
3. Select the `alfa-construction-website` repository.
4. Configure the build settings:
   - **Build command:** `npm run build`
   - **Publish directory:** `client/dist`
5. Add environment variables:
   - `VITE_SUPABASE_URL` — your Supabase project URL
   - `VITE_SUPABASE_ANON_KEY` — your supabase anon key
   - (Optional) `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, `SMTP_FROM`
6. Click **Deploy site**.

## Step 5: Configure Domain (Optional)

1. Go to **Site settings** → **Domain management**.
2. Add the custom domain: `www.alfa-constructions.Netlify.com`.
3. Netlify will provide DNS records. Add them to your domain registrar.
4. Verify the domain (Netlify will detect it automatically).
5. Set the custom domain as the site's "Primary" domain.
6. Optionally set up a redirect from `alfa-constructions.com` to the Netlify domain.

## Step 6: Verify Deployment

1. Open the Netlify URL.
2. Test:
   - Homepage loads
   - Navigation works
   - Contact forms work
   - Project pages load
   - Admin login at `/admin/login`
3. Check the browser console for errors.
4. Verify no sensitive data is exposed.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Build fails | Check `npm run build` locally. Ensure all env vars are set. |
| Admin can't sign in | Create an admin user in Supabase Auth dashboard. |
| Forms don't submit | Verify `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY`. |
| Images not loading | Check storage bucket policies and public access. |
| 404 on all routes | Ensure SPA fallback is configured in Netlify. |
