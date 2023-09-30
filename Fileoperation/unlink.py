from pathlib import Path

cd = Path.cwd()
newfilepath = cd/'Fileoperation\\read_write2.txt'
newfilepath.unlink()