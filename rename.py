
import glob
import os


folder = "res"
files = sorted(glob.glob(f"{folder}/*.mp3"))
files.remove(f"{folder}/titlepage.mp3")

index = 0
for file in files:
    index += 1
    newname = folder + f"/{index:03}.mp3"
    print(f"{file} to {newname}...")
    os.system(f"mv {file} {newname}")
