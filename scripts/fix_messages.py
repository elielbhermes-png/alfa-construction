content = open('client/src/pages/admin/MessagesAdmin.tsx', 'r').read()

# Find the broken line and fix it
broken = """    const note = notes[id] ? notes[id] + '''
' + form.note : form.note;"""

fixed = """    const note = notes[id] ? notes[id] + '\\n' + form.note : form.note;"""

if broken in content:
    content = content.replace(broken, fixed)
    open('client/src/pages/admin/MessagesAdmin.tsx', 'w').write(content)
    print("Fixed")
else:
    print("Not found, searching...")
    # Find what's actually there
    idx = content.find('const note = notes')
    print(repr(content[idx:idx+150]))
