#!/usr/bin/env python3
"""Fix the chr(10) / newline issue in MessagesAdmin.tsx"""
import os

path = os.path.join('client', 'src', 'pages', 'admin', 'MessagesAdmin.tsx')
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find and fix the problematic lines
new_lines = []
for i, line in enumerate(lines):
    # Line 39 (0-indexed) has the corrupted string
    if i == 39:
        # Replace the corrupted content
        new_lines.append("    const note = notes[id] ? notes[id] + '\\n' + form.note : form.note;\n")
    else:
        new_lines.append(line)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done - checking result")
with open(path, 'r', encoding='utf-8') as f:
    print(f.read()[350:550])
