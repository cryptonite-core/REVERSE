""" Decompiled by Exotic Hridoy """

import os,sys,time,datetime,random,json
try:import rich
except ImportError:os.system('pip install rich')
from rich import print
from rich.panel import Panel as panel
from rich.console import Console
from rich.columns import Columns as kolom
import py_compile,base64,os,sys,zlib,marshal,shutil
from pprint import pformat
from time import sleep,strftime
import re,requests
from bs4 import BeautifulSoup as bs
import names
input = Console().input
def clear():os.system('cls' if os.name in ['nt'] else 'clear')
warna = ['[bold red]','[bold purple]','[bold yellow]','[bold green]','[bold cyan]']

def baner():
    clear()
    Console(width=50).print(panel('''[bold red] ____  __  __ _  ____[bold green]      __  ____  
[bold red](  __)(  )(  ( \(    \ [bold white]___[bold green](  )(    \ 
[bold red] ) _)  )( /    / ) D ([bold white](___)[bold green])(  ) D (
[bold red](__)  (__)\_)__)(____/[bold green]    (__)(____/''',width=50),justify='center',style='bold yellow')
class main:
    def __init__(self):
        self.minta = requests.Session()
        self.menu()
    def menu(self):
        baner()
        Console(width=50).print(panel('''[bold purple][[bold green]1[bold purple]].[bold green]Find Profile ID
[bold purple][[bold green]2[bold purple]].[bold green]Find Post ID
[bold purple][[bold green]3[bold purple]].[bold green]Find Group ID
[bold purple][[bold green]4[bold purple]].[bold green]Exit''',width=50,subtitle='╭──',subtitle_align='left',style='bold yellow'))
        option = input('   [bold yellow]╰─> ')
        if option in ['1','01']:
            self.profile()
        elif option in ['2','02']:
            self.post()
        elif option in ['3','03']:
            self.group()
        elif option in ['4','04']:
            print('   [bold yellow]╰─> [bold red]Exit. !');sleep(2);exit()
        else:
            print('   [bold yellow]╰─> [bold red]Pilih Yang Benar... !',end='');sleep(2);clear();main()
    def profile(self):
        container = []
        Console(width=50).print(panel('[bold green]Masukan Url Akun Facebook',width=50,subtitle='╭──',subtitle_align='left',style='bold yellow'),justify='center')
        url = input('   [bold yellow]╰─> ').replace('https://m.','').replace('https://mbasic.','').replace('https://free.','').replace('https://www.','').replace('https://web.','')
        try:
            with self.minta as r:
                res = bs(r.get('https://web.'+url).content,'html.parser')
                id = re.search('content="fb://profile/(.*?)"',str(res))[1]
                nama = res.find('title').text
                isi = f'{id}|{nama}'
                try:
                    lihat = open('Result/Profile.txt','r').read().splitlines()
                    if isi in str(lihat):pass
                    else:open('Result/Profile.txt','a').write(f'{id}|{nama}\n')
                except:open('Result/Profile.txt','a').write(f'{id}|{nama}\n')
                Console(width=50).print(panel(f'[bold green]{id}',width=50,style='bold yellow',title=f'[bold yellow]>[bold red]>[bold blue]>[bold green]> {nama} <[bold green]<[bold blue]<[bold red]<[bold yellow]'),justify='center')
        except TypeError:
            print('   [bold yellow]╰─> [bold red]Tidak Dapat Menemukan Akun !',end='');sleep(2);clear();main()
    def post(self):
        Console(width=50).print(panel('[bold green]Masukan Url Postingan Facebook',width=50,subtitle='╭──',subtitle_align='left',style='bold yellow'),justify='center')
        url = input('   [bold yellow]╰─> ').replace('https://m.','').replace('https://mbasic.','').replace('https://free.','').replace('https://www.','')
        try:
            with self.minta as r:
                res = r.get('https://web.'+url).text
                data = re.search('content="https://web.facebook.com/(.*?)/posts/(.*?)/"',str(res))[2]
                if '-' in str(data):
                    id = re.search('content="https://web.facebook.com/(.*?)/posts/(.*?)/(.*?)/"',str(res))[3]
                else:
                    id = re.search('content="https://web.facebook.com/(.*?)/posts/(.*?)/"',str(res))[2]
                Console(width=50).print(panel(f'[bold green]{id.replace("-(.*?)-","")}',width=50,style='bold yellow'),justify='center')
        except TypeError:
            print('   [bold yellow]╰─> [bold red]Tidak Dapat Menemukan Postingan !',end='');sleep(2);clear();main()
    def group(self):
        Console(width=50).print(panel('[bold green]Masukan Url Group Facebook',width=50,subtitle='╭──',subtitle_align='left',style='bold yellow'),justify='center')
        url = input('   [bold yellow]╰─> ').replace('https://m.','').replace('https://mbasic.','').replace('https://free.','').replace('https://','').replace('https://www.','')
        try:
            with self.minta as r:
                res = bs(r.get('https://web.'+url).content,'html.parser')
                id = re.search('content="fb://group/(.*?)"',str(res))[1]
                Console(width=50).print(panel(f'[bold green]{id}',width=50,style='bold yellow'),justify='center')
        except TypeError:
            print('   [bold yellow]╰─> [bold red]Tidak Dapat Menemukan Group !',end='');sleep(2);clear();main()

def check_size():
    try:
        t_size, _ = shutil.get_terminal_size()
        if t_size == 50 or t_size > 50:main()
        else:
            while True:
                for color in warna:
                    clear();Console(width=t_size).print(panel(f'{color}Silahkan Perkecil Layar Terminal Anda Dengan Cara Mencubit Layar,Hingga Tampilan Tidak Terlihat Putus-Putus',width=t_size),justify='center')
    except KeyboardInterrupt:print(f'')
if __name__ in ['__main__']:
    try:os.mkdir('Result')
    except:pass
    try:check_size()
    except Exception as error:print(error)
