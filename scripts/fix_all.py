import os, re

files = [
    'client/src/pages/admin/AdminLayout.tsx',
    'client/src/pages/admin/Dashboard.tsx',
    'client/src/pages/admin/LoginPage.tsx',
    'client/src/pages/admin/MediaAdmin.tsx',
    'client/src/pages/admin/MessagesAdmin.tsx',
    'client/src/pages/admin/ProjectsAdmin.tsx',
    'client/src/pages/admin/ServicesAdmin.tsx',
    'client/src/pages/admin/QuotesAdmin.tsx',
    'client/src/pages/admin/SettingsPage.tsx',
    'client/src/contexts/I18nContext.tsx',
    'client/src/contexts/SupabaseProvider.tsx',
]

for path in files:
    with open(path, 'r') as f:
        content = f.read()
    
    # Fix: replace "import import { X } from '@\\path'" with "import { X } from '@/path'"
    content = re.sub(r'import\s+import\s+\{([^}]+)\}\s+from\s+\'@\\([^\']+)\'', r"import {\1} from '@/\2'", content)
    
    with open(path, 'w') as f:
        f.write(content)
    print('Fixed:', path)
