import requests 
import os

version = open('version').read()
newest = requests.get('https://raw.githubusercontent.com/Abominate34/Test_repo/main/version.txt').text.split('\n')[0]


if version == newest:
	print("Current version is newest")

else:
	print('old_version')
	f=open(r'main.py',"wb") 
	ufr = requests.get("https://raw.githubusercontent.com/Abominate34/Test_repo/main/test.py") 
	f.write(ufr.content)
	f.close()
	f=open(r'version',"wb").write(newest).close()
