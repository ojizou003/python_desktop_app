from pathlib import Path

cd = Path.cwd()
print(cd)
# filepath = Path(f'{cd}\Fileoperation\Practice.py')
filepath = cd/'Fileoperation\sample.txt'
print(filepath)
with filepath.open(encoding='utf-8') as f:
  print(f.read())
contents = '\n追記'
with filepath.open(mode='a',encoding='utf-8') as f:
  f.write(contents)
  