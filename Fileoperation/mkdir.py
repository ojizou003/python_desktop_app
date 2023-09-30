from pathlib import Path

cd = Path.cwd()
newfolderpath = cd/'Fileoperation\新しいフォルダ'
Path(newfolderpath).mkdir()
