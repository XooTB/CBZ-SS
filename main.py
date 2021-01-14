import os
from zipfile import ZipFile

# lis1 = [f for f in os.listdir("./TempManga")]

# for f in lis1:
#     fil = f'TempManga/{f}'
#     pre, ext = os.path.splitext(fil)
#     os.rename(fil, pre + '.cbz')

lis2 = [f for f in os.listdir("./TempManga")]

for f in lis2:
    fil_dir = f"TempManga/{f}"
    with ZipFile(fil_dir, 'r') as zip:
        a = zip.namelist()
        print(f'Extracting: {f}')
        for i in range(30):
            zip.extract(a[i], f'C:/Users/XooT/Pictures/{f}')
