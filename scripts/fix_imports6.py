import os, re

files = [
    'client/src/contexts/I18nContext.tsx',
    'client/src/contexts/SupabaseProvider.tsx',
    'client/src/pages/admin/AdminLayout.tsx',
    'client/src/pages/admin/Dashboard.tsx',
    'client/src/pages/admin/LoginPage.tsx',
    'client/src/pages/admin/MediaAdmin.tsx',
    'client/src/pages/admin/MessagesAdmin.tsx',
    'client/src/pages/admin/ProjectsAdmin.tsx',
    'client/src/pages/admin/ServicesAdmin.tsx',
    'client/src/pages/admin/QuotesAdmin.tsx',
    'client/src/pages/admin/SettingsPage.tsx',
]

for path in files:
    with open(path, 'r') as f:
        content = f.read()
    
    def fix_import(m):
        full = m.group(0)
        parts = full.split('@')
        module = parts[1].lstrip('/')
        return "import " + parts[0] + "from '@/" + module + "'"
    
    content = re.sub(r'import\s+{[^}]+}\s+@/\S+', fix_import, content)
    content = re.sub(r'import\s+(\w+)\s+@/(\.\./)+lib/(\S+)', r"import \1 from '@/lib/\3'", content)
    
    with open(path, 'w') as f:
        f.write(content)
    print('Fixed:', path)
