import os, re

files = [
    'client/src/pages/admin/LoginPage.tsx',
    'client/src/pages/admin/AdminLayout.tsx',
    'client/src/pages/admin/Dashboard.tsx',
    'client/src/pages/admin/ProjectsAdmin.tsx',
    'client/src/pages/admin/ServicesAdmin.tsx',
    'client/src/pages/admin/MediaAdmin.tsx',
    'client/src/pages/admin/MessagesAdmin.tsx',
    'client/src/pages/admin/QuotesAdmin.tsx',
    'client/src/pages/admin/SettingsPage.tsx',
    'client/src/contexts/I18nContext.tsx',
    'client/src/contexts/SupabaseProvider.tsx',
    'client/src/app/App.tsx',
]

for path in files:
    with open(path, 'r') as f:
        content = f.read()
    
    # Fix import lines: "import x from '@/path'" -> "import x from '@/path'"
    # Fix: "import x from '@/../components/ui/button'"
    def fix_import(m):
        parts = m.group(0).split("'")
        if len(parts) >= 3:
            mod = parts[1]
            # Convert @/../ -> @/
            mod = mod.replace('@/../', '@/')
            # Remove trailing '' at end
            mod = mod.rstrip('\'')
            # Fix: "from '@/../components/ui/button'"
            # parts[0] is "import { Button } from ", parts[2] is "',"
            return "'" + parts[0] + "'" + "@" + mod + "'" + parts[2]
        return m.group(0)
    
    # Match: import { X } from '@/../components/ui/button'
    pattern = re.compile(r"import\s+{[^}]+}\s+from\s+'(@/\.\./[^']*)''")
    new_content = pattern.sub(fix_import, content)
    
    if new_content != content:
        with open(path, 'w') as f:
            f.write(new_content)
        print('Fixed:', path)
