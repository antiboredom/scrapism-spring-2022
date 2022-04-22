import glob
import sys
import os

folder = sys.argv[1]
exts = ["*.gif", "*.jpg", "*.png"]
exts += [e.upper() for e in exts]

top = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Images</title>
    <style>
        img {
            object-fit: contain;
            display: inline-block;
            width: 33%;
            height: 300px;
        }
    </style>
  </head>

  <body>
    <section>
"""


bottom = """
    </section>
  </body>
</html>
"""


print(top)

for ext in exts:
    path = os.path.join(folder, ext)
    for f in glob.glob(path):
        print(f'''<img src="{f}">''')

print(bottom)
