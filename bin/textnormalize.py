#!/usr/bin/env python3

import sys

fileinfo = []
for f in sys.argv[1:]:
    linelength = 0
    with open(f) as buffer:
        lines = buffer.readlines()
    shortf = f.replace(".txt", "").replace("text/", "").upper()
    newf = "build/text/" + shortf
    fileinfo.append(shortf + "=Type(04),AuxType(0000),VersionCreate(70),MinVersion(BE),Access(C3)")
    with open(newf, 'w') as buffer:
        for l in lines:
            l = l[:-1]
            if not l:
                linelength = 0
            if l and linelength:
                l = l + ' '*(linelength-len(l))
            buffer.write(l + "\n")
            if l.startswith("[info]"):
                linelength = 20
            elif l.startswith("[description]"):
                linelength = 77
with open("build/text/_FileInformation.txt", "w") as infobuff:
    infobuff.write("\r\n".join(fileinfo))