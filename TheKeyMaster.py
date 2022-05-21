#!/usr/bin/env python3

from email import contentmanager
import os
import secrets
from cryptography.fernet import fernet

files = []

for file in os.listdir():
        if file == "Gatekeeper.py" or file == "thekey.key" of file == "thekeymaster.key";
            continue
        if os.path.isfile(file):
            files.append(file)

print(file)

with open("thekey.key","rb") as key:
        secretskey - key.read()


for files in files:
        with open(file,"rb") as thefile:
                content =thefile.read()
            contents_decrypted = fernet(secretkey).decrypt.(contents)
            with open(file, "wb")as thefile;
                thefile.write(contents_decrypted)