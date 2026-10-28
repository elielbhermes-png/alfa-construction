import os

# Delete corrupted files
corrupted = [
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

for f in corrupted:
    if os.path.exists(f):
        os.remove(f)
        print('Deleted:', f)
