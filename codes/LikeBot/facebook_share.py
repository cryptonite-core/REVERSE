""" Decompiled by Exotic Hridoy """

import os,sys,requests
import re,base64,rich,time,calendar,datetime,platform,random,json
from concurrent.futures import ThreadPoolExecutor as TheEND
from rich.console import Console as UsydConsole
from rich.panel import Panel as UsydPanel
from datetime import datetime
from time import strftime

(p, m, h, k, b, u, o, n, a) = ('\x1b[1;97m', '\x1b[1;31m', '\x1b[38;5;46m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[0m', '\x1b[90;1m')
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")
now = datetime.now()
hour = now.hour

def Bajingan_Z(TypePlatform):
    if 'win' in TypePlatform:
       return os.system('cls')
    else:
       return os.system('clear')

class RAKA_XYZ:
    def __init__(self):
        try:
             cokie = open('data/cookie.txt','r').read()
             token = open('data/tooken.txt','r').read()
        except FileNotFoundError:
             time.sleep(3)
             self.fox()
        self.menu(cokie, token)

    def fox(self):
        coki = input(f'\n {m}• {p}input cookie : {h}')
        try:
            cari = requests.get("https://business.facebook.com/business_locations",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","cookie":coki})
            toke = re.search("(EAAG\w+)", cari.text).group(1)
            if "EAAG" in str(toke):
                open("data/cookie.txt","w").write(coki)
                open("data/tooken.txt","w").write(toke)
                exit(print(f'\n {m}• {p}login successful\n'))
        except AttributeError:
            exit(print(f'\n {m}• {p}cookie expired\n'))
        except requests.exceptions.ConnectionError:
            exit(print(f'\n {m}• {p}internet error\n'))

    def menu(self, kuki, token):
        Bajingan_Z(sys.platform) ; print (rakaxyz)
        try:nama = requests.get("https://graph.facebook.com/me?access_token={}".format(token),cookies={"cookie":kuki}).json()['name']
        except KeyError:self.mask()
        except requests.exceptions.ConnectionError:exit(print(f' {m}>_ {p}Pastikan Koneksinya Aman Goblog'))
        print(f' {m}• {p}Account {h}{nama}\n')
        print(f' {p}1. Auto Share with ({m}graph{p}) \n {p}2. logout and delete all data\n')
        rakaxyzzz = input(f' {m}• {p}select : {h}')
        if rakaxyzzz in ['1','A','a']:
             print()
             link = input(f' {m}• {p}Enter link : {h}')
             print()
             try:limit = int(input(f' {m}• {p}Enter Limit : {h}'))
             except:limit=50
             print()
             self.share(link,limit,token,kuki)
        elif rakaxyzzz in ['2','L','02']:
             os.system('rm -rf data/cookie.txt && rm -rf data/tooken.txt')
             os.system('exit')
        else:
             exit()

    def share(self, link, limit, token, rakaexde):
        sukses,gagal=[],[]
        try:
              headers = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":self.useragent()}
              for i in range(limit):
                  link_pos = requests.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=headers, cookies={'cookie':rakaexde})
                  response = json.loads(link_pos.text)
                  xyz = random.choice([m,k,h,p])
                  print(f"\r {m}• {p}running{h} {len(sukses)} {p}success", end=" ");
                  sys.stdout.flush()
                  if "id" in response:
                      sukses.append("Share")
                  else:
                      sukses.append("Tolol")
        except Exception as e:
             exit(print(f' {m} • {p}cookie expired'))

    def useragent(self):
        return ('Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36')

rakaxyz = ('')

def Cetak(Text, Type, Warna):
    if 'banner' in Type:
        return UsydConsole(width=50, style=Warna).print(UsydPanel(Text),justify='center')
    else:
        return UsydConsole(width=50, style=Warna).print(UsydPanel(Text))

if __name__ == '__main__':
   RAKA_XYZ()
