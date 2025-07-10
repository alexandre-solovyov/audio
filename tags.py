
from mutagen.easyid3 import EasyID3
import glob
import sys


album = f"{sys.argv[1]} -- {sys.argv[2]}"
artist = u"AI"
folder = "res"
files = sorted(glob.glob(f"{folder}/*.mp3"))

try:
    files.remove(f"{folder}/titlepage.mp3")
except:
    pass

for file in files:
    print(file)
    audio = EasyID3(file)
    audio['title'] = file.replace(f"{folder}/", "").replace(".mp3", "")
    audio['artist'] = artist
    audio['album'] = album
    audio.save()
