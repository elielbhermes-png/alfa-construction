import os

# Fix App.tsx - add location variable before AppShell
path = 'client/src/app/App.tsx'
with open(path, 'rb') as f:
    content = f.read()
old = b'function AppShell() {\n  const isAdminRoute'
new = b'function AppShell() {\n  const location = useLocation();\n  const isAdminRoute'
if old in content:
    content = content.replace(old, new, 1)
    with open(path, 'wb') as f:
        f.write(content)
    print('App.tsx fixed')

# Fix Dashboard.tsx
path = 'client/src/pages/admin/Dashboard.tsx'
with open(path, 'r') as f:
    c = f.read()
c = c.replace('const { supabase, initialized } = useSupabase();', 'const { supabase, initialized } = useSupabase();')
c = c.replace('supabase.from', 'supabase!.from')
with open(path, 'w') as f:
    f.write(c)
print('Dashboard fixed')

# Fix AdminLayout
path = 'client/src/pages/admin/AdminLayout.tsx'
with open(path, 'r') as f:
    c = f.read()
c = c.replace('supabase!.auth', 'supabase!.auth')
with open(path, 'w') as f:
    f.write(c)
print('AdminLayout fixed')
