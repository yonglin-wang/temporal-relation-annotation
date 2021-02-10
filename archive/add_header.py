import os

path = 'Jonne'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.xml' in file:
            files.append(os.path.join(r, file))

for file in files:
    with open(file, "r+") as f:
        old = f.read()  # read everything in the file
        if old[-1] == "\n":
            old = old[:-1]
        f.seek(0)  # rewind
        f.write(old)  # write the new line before
