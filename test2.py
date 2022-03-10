import requests 
import os
import sys
import subprocess
#ver1



def checkupdates():
	print('Проверка обновлений...')

	version_link = 'https://raw.githubusercontent.com/Abominate34/Test_repo/main/version'
	code_link = "https://raw.githubusercontent.com/Abominate34/Test_repo/main/test2.py"
	file_to_restart = "test.py"

	version = open('version').read().split('\n')[0]
	newest = requests.get(version_link)


	if version == newest.text.split('\n')[0]:
		print("[+] У вас самая новая версия!")

	else:
		print('[-] Версия устарела! Обновление...')
		f=open(file_to_restart,"wb") 
		ufr = requests.get(code_link) 
		f.write(ufr.content)
		f.close()
		f=open(r'version',"wb").write(newest.content)
		os.execvp(sys.executable,[sys.executable,file_to_restart,],)

checkupdates()
