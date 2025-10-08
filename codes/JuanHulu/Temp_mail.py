""" Decompiled by Exotic Hridoy """

import os
try:
    import requests,wget,bs4,rich
except ImportError:
    print('\t#=====> INSTALLING MODULE <=====#')
    os.system('pip install requests bs4 wget rich')
import datetime,json
from rich import print
from rich.console import Console
from rich.columns import Columns as kolom
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as bs
from time import sleep,strftime
from random import choice

def clear():os.system('cls' if os.name == 'nt' else 'clear')
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year

hri = {'Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu','Sunday':'Minggu'}
hari = hri[(str(strftime("%A")))]
jam = strftime('%T')
gbg = f'{hari}-{tgl}-{bln}-{thn}'
biogua = f'{hari}-{tgl}-{bln}-{thn} Jam : {jam} Wib'
no_of_msgs=''
mailid=''
domain=''
id=''
gogo = []

def logo():
    Console(width=60).print(panel(f'''[bold magenta]
┏━╸┏━┓╻┏ ┏━╸   ┏━╸┏┳┓┏━┓╻╻     ┏━┓╺┳┓╺┳┓┏━┓┏━╸┏━┓┏━┓
┣╸ ┣━┫┣┻┓┣╸ ╺━╸┣╸ ┃┃┃┣━┫┃┃     ┣━┫ ┃┃ ┃┃┣┳┛┣╸ ┗━┓┗━┓
╹  ╹ ╹╹ ╹┗━╸   ┗━╸╹ ╹╹ ╹╹┗━╸   ╹ ╹╺┻┛╺┻┛╹┗╸┗━╸┗━┛┗━┛
''',width=60,style='bold purple',title=f'[bold red]>[bold blue]>[bold cyan]>[bold yellow]([bold green]{gbg}[bold yellow])[bold cyan]<[bold blue]<[bold red]<'),justify='center')
def menu():
    clear()
    logo()
    print(panel('''[bold red][[bold green]1[bold red]].[bold yellow]Buat Email Random
[bold red][[bold green]2[bold red]].[bold yellow]Buat Email Manual
[bold red][[bold green]3[bold red]].[bold yellow]Exit''',width=60,style='bold purple',subtitle='┌─',subtitle_align='left',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Menu Create Email[bold cyan]<[bold blue]<[bold red]<'))
    pil = Console().input('[bold purple]   └─> ')
    if pil in ('1','01'):
        random_mail()
    elif pil in ('2','02'):
        manual()
    elif pil in ('3','03'):
        try:
            ext = 4
            for qq in range(ext):
                sleep(1)
                ext-=1
                Console().print(f'[bold purple]   └─>[bold red] {ext}',end='\r')
        except KeyboardInterrupt:
            sleep(2);menu()
    else:
        Console().print(f'[bold purple]   └─>[bold red] Pilh Yang Benar');sleep(2);menu()

def random_mail():
    try:
        with requests.Session() as r:
            response = r.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
            hasil = response.json()[0]
            user,domain = hasil.split('@')[0],hasil.split('@')[1]
            Console(width=60).print(panel(f'[bold yellow]Email Anda [bold cyan]{hasil}',width=60,style='bold purple',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Email Sementara Anda[bold cyan]<[bold blue]<[bold red]<'),justify='center')
            open('Data/Gmail.txt','a').write(f'{hasil}\n')
            for www in range(1000):
                try:
                    Console(width=60).print(panel(f'[bold yellow]Klik Enter untuk Refresh Pesan Masuk, Ctrl+C Untuk Berhenti, Ketik Clear Untuk Bersihkan Layar',subtitle='┌─',subtitle_align='left',width=60,style='bold purple',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Catatan[bold cyan]<[bold blue]<[bold red]<'),justify='center')
                    refr = Console().input('[bold purple]   └─> ')
                    if refr in ['clear','CLEAR','Clear','Cls','cls','CLS']:
                        clear()
                    else:
                        pesan_masuk(user,domain)
                except KeyboardInterrupt:
                    Console(width=60).print(panel('[bold green]Berhenti',width=60,style='bold purple'),justify='center');exit()
    except Exception as error:
        Console(width=60).print(panel(f'[bold red]{error}',width=60,style='bold purple',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Error[bold cyan]<[bold blue]<[bold red]<'),justify='center')
def manual():
    try:
        Console(width=60).print(panel('[bold yellow]Masukan Username Email',width=60,style='bold purple',subtitle='┌─',subtitle_align='left',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Masukan @username[bold cyan]<[bold blue]<[bold red]<'),justify='center')
        user = Console().input('[bold purple]   └─> ')
        Console(width=60).print(panel('''[bold red][[bold green]1[bold red]].[bold yellow]@1secmail.com           [bold red][[bold green]7[bold red]].[bold yellow]@qiott.com
[bold red][[bold green]2[bold red]].[bold yellow]@1secmail.org           [bold red][[bold green]8[bold red]].[bold yellow]@wuuvo.com
[bold red][[bold green]3[bold red]].[bold yellow]@1secmail.net           [bold red][[bold green]9[bold red]].[bold yellow]@wwjmp.com
[bold red][[bold green]4[bold red]].[bold yellow]@bheps.com             [bold red][[bold green]10[bold red]].[bold yellow]@esiix.com
[bold red][[bold green]5[bold red]].[bold yellow]@dcctb.com             [bold red][[bold green]11[bold red]].[bold yellow]@oosln.com
[bold red][[bold green]6[bold red]].[bold yellow]@kzccv.com             [bold red][[bold green]12[bold red]].[bold yellow]@vddaz.com''',width=60,style='bold purple',subtitle='┌─',subtitle_align='left',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Pilih Domain[bold cyan]<[bold blue]<[bold red]<'),justify='center')
        alamat_email = Console().input('[bold purple]   └─> ')
        if alamat_email in ['1','01']:
            domain='1secmail.com'
        elif alamat_email in ['2','02']:
            domain='1secmail.org'
        elif alamat_email in ['3','03']:
            domain='1secmail.net'
        elif alamat_email in ['4','04']:
            domain='bheps.com'
        elif alamat_email in ['5','05']:
            domain='dcctb.com'
        elif alamat_email in ['6','06']:
            domain='kzccv.com'
        elif alamat_email in ['7','07']:
            domain='qiott.com'
        elif alamat_email in ['8','08']:
            domain='wuuvo.com'
        elif alamat_email in ['9','09']:
            domain='wwjmp.com'
        elif alamat_email in ['10','010']:
           domain='esiix.com'
        elif alamat_email in ['11','011']:
            domain='oosln.com'
        elif alamat_email in ['12','012']:
            domain='vddaz.com'
        else:
            Console(width=60).print(panel('[bold red]Pilih Yang Benar',width=60,style='bold purple',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Pilihan Tidak Di Ketahui[bold cyan]<[bold blue]<[bold red]<'),justify='center');exit()
        Console(width=60).print(panel(f'[bold yellow]Email Anda [bold cyan]{user}@{domain}',width=60,style='bold purple',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Email Sementara Anda[bold cyan]<[bold blue]<[bold red]<'),justify='center')
        open('Data/Gmail.txt','a').write(f'{user}@{domain}\n')
        for www in range(1000):
            try:
                Console(width=60).print(panel(f'[bold yellow]Klik Enter untuk Refresh Pesan Masuk, Ctrl+C Untuk Berhenti, Ketik Clear Untuk Bersihkan Layar',subtitle='┌─',subtitle_align='left',width=60,style='bold purple',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Catatan[bold cyan]<[bold blue]<[bold red]<'),justify='center')
                refr = Console().input('[bold purple]   └─> ')
                if refr in ['clear','CLEAR','Clear','Cls','cls','CLS']:
                    clear()
                else:
                    pesan_masuk(user,domain)
            except KeyboardInterrupt:
                Console(width=60).print(panel('[bold green]Berhenti',width=60,style='bold purple'),justify='center');exit()
    except Exception as error:
        Console(width=60).print(panel(f'[bold red]{error}',width=60,style='bold purple',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Error[bold cyan]<[bold blue]<[bold red]<'),justify='center')

def pesan_masuk(user,domain):
    try:
        with requests.Session() as r:
            response = r.get('https://www.1secmail.com/api/v1/?action=getMessages&login={}&domain={}'.format(user,domain))
            data = json.loads(response.text)
            reneg = len(data)
            Console(width=60).print(panel(f'[bold yellow]Jumlah Pesan Diterima : [bold green]{str(reneg)}',width=60,style='bold purple',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Pesan Diterima[bold cyan]<[bold blue]<[bold red]<'),justify='center')
            if '[]' in str(data):
                Console(width=60).print(panel(f'[bold yellow]Belum Ada Pesan Masuk',width=60,style='bold purple',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Refres Kembali[bold cyan]<[bold blue]<[bold red]<'),justify='center')
            else:
                for i in range(reneg):
                    emailid=data[i]['id']
                    dari=data[i]['from']
                    pesan=data[i]['subject']
                    tanggal=data[i]['date']
                    Console().print(panel(f'''[bold yellow]Nomor Email   : [bold green]{emailid}
[bold yellow]Pesan Dari    : [bold green]{dari}
[bold yellow]Tanggal Masuk : [bold green]{tanggal}
[bold yellow]Pesan         : [bold green]{pesan}''',width=60,style='bold purple',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Pesan Masuk[bold cyan]<[bold blue]<[bold red]<'))
    except Exception as error:
        Console(width=60).print(panel(f'[bold red]{error}',width=60,style='bold purple',title='[bold red]>[bold blue]>[bold cyan]>[bold green]Error[bold cyan]<[bold blue]<[bold red]<'),justify='center')

if __name__ in '__main__':
    try:os.mkdir('Data')
    except:pass
    os.system('git pull')
    menu()
