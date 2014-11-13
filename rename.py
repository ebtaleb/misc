import os
import string
import glob

avi = glob.glob("*.avi")
idx = glob.glob("*.idx")
srt = glob.glob("*.srt")
sub = glob.glob("*.sub")

avi.sort()
idx.sort()
srt.sort()
sub.sort()

for filename in srt:
    os.rename(filename, avi[0][:-4]+".srt")
    avi.pop(0)

for filename in idx:
    os.rename(filename, avi[0][:-4]+".idx")
    avi.pop(0)

for filename in sub:
    os.rename(filename, avi2[0][:-4]+".sub")
    avi2.pop(0)

