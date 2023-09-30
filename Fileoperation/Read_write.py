from pathlib import Path

cd = Path.cwd()
filepath = cd/'Fileoperation\\read_write.txt'
contents = filepath.read_text(encoding='utf-8')
print(contents)
newfilepath = cd/'Fileoperation\\read_write2.txt'
newcontents = '\n新しい書き込み'
newfilepath.write_text(newcontents,encoding='utf-8')