#coding=utf-8

import os,sys,time,json,urllib

os.system('clear')

print """██████\033[0;30m╗       \033[30;1m╔\033[30;1m•\033[0;37m]\033[30;1m>
\033[30;1m██\033[0;30m\033[0;30m╔══\033[30;1m██\033[0;30m╗      \033[30;1m║  \033[30;1m<\033[31;1m•\033[30;1m[ \033[0;30mDEC PYTHON \033[30;1m]\033[31;1m•\033[30;1m>
\033[30;1m██\033[0;30m\033[0;30m║  \033[30;1m██\033[0;30m║      \033[30;1m║   \033[30;1m<\033[31;1m•\033[30;1m[  \033[0;30mMARSHAL \033[30;1m]\033[31;1m•\033[30;1m>
\033[30;1m██\033[0;30m\033[0;30m║  \033[30;1m██\033[0;30m║      \033[30;1m║═[\033[0;31m•\033[30;1m] Author \033[31;1m: \033[30;1mNemuv
\033[30;1m██████\033[0;30m╔╝  \033[30;1mEC  \033[30;1m║=[\033[0;31m•\033[30;1m] Github \033[31;1m: \033[30;1mhttps://github.com/NemuvSpZi
\033[0;30m╚═════╝	  \033[30;1m<\033[31;1m•\033[30;1m>\033[30;1m═╚══════════════════════════════════════════•>
"""
def decom():
	time.sleep(1)
	print ("")
	file = open(raw_input(" \033[30;1m[\033[31;1m•\033[30;1m] \033[0;33mInput \033[0;37mFile \033[31;1m•\033[0;37m>\033[30;1m> \033[30;1m")).read()
	print ("")
	while True:
		if "exec" in file and "marshal" in file and "import" in file:
			out = file.replace("exec", "x =")
			time.sleep(1)
		else:
			print ("\n")
			try:
				os.remove("sc.py")
				print (" \033[30;1m[\033[31;1m•\033[30;1m] \033[0;33mDec \033[0;37mBerhasil\033[30;1m!\033[0;31m..")
				print (" \033[30;1m[\033[31;1m•\033[30;1m] \033[0;37mDengan Nama \033[0;33m\033[0;37mFile \033[30;1m<\033[31;1m•\033[30;1m> \033[0;33mHasil.py ")
			except:
				print (" [•] Dec Gagal! ")
				decom()
			break
		sc = """from sys import stdout
import marshal
from uncompyle6.main import decompile
"""+out+"""
decompile(2.7,x, stdout) """
		open("sc.py","w").write(sc)
		os.system("python2 sc.py > hasil.py")
		file = open("hasil.py").read()
decom()
