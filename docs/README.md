# ALFA CONSTRUCTION — GitHub Repository

**Repository:** alfa-construction-website
**Stack:** React + TypeScript + Vite + Tailwind + Supabase + Netlify

## Repository Structure

```
alfa-construction-website/
├── client/                     # Frontend (React + TS + Vite + Tailwind)
│   ├── public/
│   ├── src/
│   │   ├── app/                # Router + App shell
│   │   ├── components/         # UI components and layout
│   │   ├── pages/              # Public pages + admin pages
│   │   ├── lib/                # Types, validation, supabase clients
│   │   ├── contexts/           # Supabase + I18n context
│   │   └── styles/             # Design system (global.css)
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── tailwind.config.js
├── server/                     # Supabase Edge Functions (Netlify)
│   ├── contact-function.ts
│   └── quotation-function.ts
├── supabase/                   # Supabase database migrations
│   └── migrations/
│       ├── 0000_init.sql
│       ├── 0001_add_site_settings.sql
│       └── 0002_add_audit_logs_seed.sql
├── docs/                       # Documentation
│   ├── README.md
│   ├── deployment-guide.md
│   └── security.md
├── .github/workflows/          # CI/CD
│   └── ci.yml
├── netlify.toml                # Netlify configuration
├── .env.example                # Environment variables template
├── .gitignore
├── package.json
├── tailwind.config.js
├── postcss.config.js
└── vite.config.ts
```

## Prerequisites

- Node.js >= 18
- npm >= 9
- A GitHub account
- A Supabase project (free tier works)
- A Netlify account (for deployment)

## Local Installation

```bash
git clone https://github.com/<your-user>/alfa-construction-website.git
cd alfa-construction-website
npm install
cp .env.example .env
# Edit .env with your Supabase URL and anon key
```

## Development Commands

```bash
npm run dev        # Start Vite dev server on port 3000
npm run build      # TypeScript check + production build
npm run preview    # Preview production build
npm run test       # Run unit tests
npm run supabase:reset # Start local Supabase
npm run supabase:migrate # Push migrations to local Supabase
```

## Deployment (Netlify)

1. Push this repository to GitHub.
2. In Netlify, click **Add new site** → **Import an existing project**.
3. Connect your GitHub repo.
4. Set:
   - **Build command:** `npm run build`
   - **Publish directory:** `client/dist`
5. Add environment variables from `.env.example`.
6. Deploy.

## Supabase Project Setup

1. Create a project at https://supabase.com/dashboard.
2. Run the migrations in `supabase/migrations/` via the Supabase dashboard
   (Database → Migrations → New migration).
3. Configure the following Storage buckets:
   - `project-images` (public, for published project images)
   - `private-documents` (private, for quotation documents)
4. Set Row Level Security policies (see `supabase/migrations/0000_init.sql`).

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `VITE_SUPABASE_URL` | Yes | Your Supabase project URL |
| `VITE_SUPABASE_ANON_KEY` | Yes | Supabase anon key (client-side safe) |
| `SMTP_HOST` | No | Transactional email provider host |
| `NETLIFY_SITE_ID` | No | Netlify site ID for webhooks |

See `.env.example` for the full template.

## Testing

```bash
npm run test           # Unit tests (Vitest)
npm run test:e2e       # End-to-end tests (Playwright)
```

## Admin Dashboard

1. Visit `/admin/login`.
2. Create your first administrator account via the Supabase dashboard
   (Auth → Users → New user).
3. Set a secure password and complete sign-in.
4. Navigate to **Settings** and configure your company details.

## Security

- The Supabase service-role key is NEVER exposed to the browser.
- All database operations go through `supabase-js` client (anon key).
- Server-side operations use Netlify Edge Functions.
- Row Level Security policies protect all tables.
- File uploads are validated on the server side.

## License

MIT
