import os, re

for root, dirs, files in os.walk('client/src'):
    for f in files:
        if f.endswith('.tsx') or f.endswith('.ts'):
            path = os.path.join(root, f)
            with open(path) as fh:
                c = fh.read()
            # Replace backslashes in import paths with forward slashes
            c = re.sub(r"from\s+'(@/[^']*)'$", lambda m: "from '" + m.group(1).replace('\\', '/') + "'", c, flags=re.MULTILINE)
            with open(path, 'w') as fh:
                fh.write(c)
print('All fixed')
