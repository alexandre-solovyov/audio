
from mutagen.easyid3 import EasyID3
import glob
import sys
import xml.etree.ElementTree as et


tree = et.parse("content.opf")
root = tree.getroot()
meta = root.find("{http://www.idpf.org/2007/opf}metadata")
title = meta.find("{http://purl.org/dc/elements/1.1/}title").text
author = meta.find("{http://purl.org/dc/elements/1.1/}creator").text.split()[-1]

print(f"Found title={title} and author={author}")


album = f"{author} -- {title}"
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
