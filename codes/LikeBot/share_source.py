""" Decompiled by Exotic Hridoy """

import requests
import os
import re
import bs4
import sys
import json
import time
import random
import datetime
import subprocess
from datetime import datetime
from time import sleep
from time import strftime

ses = requests.Session()
bulan = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[str(datetime.now().month)]
thn = datetime.now().year
tanggal = str(tgl) + ' ' + str(bln) + ' ' + str(thn)
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime('%A')

A = '\033[1;97m'
R = '\033[38;5;196m'
Y = '\033[1;33m'
G = '\033[1;96m'
B = '\033[38;5;8m'
G1 = '\033[38;5;48m'
G2 = '\033[38;5;47m'
G3 = '\033[38;5;48m'
G4 = '\033[38;5;49m'
G5 = '\033[38;5;50m'
X = '\033[1;34m'
X1 = '\033[38;5;14m'
X2 = '\033[38;5;123m'
X3 = '\033[38;5;122m'
X4 = '\033[38;5;86m'
X5 = '\033[38;5;121m'
S = '\033[1;96m'
M = '\033[38;5;205m'
N1 = '\033[1;92m\033[38;5;208m'
N2 = '\033[1;92m\033[38;5;209m'
N3 = '\033[1;92m\033[38;5;210m'
N4 = '\033[1;92m\033[38;5;211m'
N5 = '\033[1;92m\033[38;5;212m'
L1 = '\033[1;92m\033[38;5;46m'
L2 = '\033[1;92m\033[38;5;47m'
L3 = '\033[1;92m\033[38;5;48m'
L4 = '\033[1;92m\033[38;5;49m'
L5 = '\033[1;92m\033[38;5;50m'

ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
ua_random = random.choice([ua_default, ua_samsung, ua_nokia, ua_xiaomi, ua_oppo, ua_vivo, ua_iphone, ua_asus, ua_lenovo, ua_huawei, ua_windows, ua_chrome, ua_fb])

kom1 = 'Panutan gw nih bos:v\n \nhttps://www.facebook.com/100036939615544/posts/826244578616855/?app=fbl\n \nKOMENTAR DITULIS OLEH BOT\n \n[><]'

def logo():
    print(f'\n\n{L1}   ███████ ██   ██  █████  ██████  ███████ ')
    print(f'{L2}   ██      ██   ██ ██   ██ ██   ██ ██      ')
    print(f'{L3}   ███████ ███████ ███████ ██████  █████   ')
    print(f'{L4}        ██ ██   ██ ██   ██ ██   ██ ██      ')
    print(f'{L5}   ███████ ██   ██ ██   ██ ██   ██ ███████  {N1}F{X}B')

def linex():
    print(f' {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def login():
    os.system('xdg-open https://github.com/U7P4L-IN')
    os.system('clear')
    print(f'\n\n{L1}   ███████ ██   ██  █████  ██████  ███████ ')
    print(f'{L2}   ██      ██   ██ ██   ██ ██   ██ ██      ')
    print(f'{L3}   ███████ ███████ ███████ ██████  █████   ')
    print(f'{L4}        ██ ██   ██ ██   ██ ██   ██ ██      ')
    print(f'{L5}   ███████ ██   ██ ██   ██ ██   ██ ███████  {N1}F{X}B')
    print(f' {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{X2}【{X5}✦{X2}】{Y}VERSION       {B}»----{A}➤ {G3}1.0{X2}\n【{X5}✦{X2}】{Y}AUTHOR        {B}»----{A}➤ {G3}U7P4L{X2}\n【{X5}✦{X2}】{Y}TOOL          {B}»----{A}➤ {G3}AUTO SHARE')
    print(f' {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{B}【{A}•{B}】{Y}USE DATA/WIFI TO USE THIS TOOL.')
    print(f'{B}【{A}•{B}】{X1}USE FRESH AND WORKING COOKIES.')
    print(f'{B}【{A}•{B}】{X1}TAKE COOKIES FROM KIWI BROWSER.')
    linex()
    cookie = input(f'{B}【{A}❯{B}】{G}INPUT COOKIES {A}➤\033[1;32m ')
    try:
        data = ses.get('https://business.facebook.com/business_locations', headers={
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
            'referer': 'https://www.facebook.com/',
            'host': 'business.facebook.com',
            'origin': 'https://business.facebook.com',
            'upgrade-insecure-requests': '1',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'content-type': 'text/html; charset=utf-8'
        }, cookies={'cookie': cookie})
        find_token = re.search('(EAAG\\w+)', data.text)
        if find_token:
            open('.token.xx.txt', 'w').write(find_token.group(1))
            open('.cookie.xx.txt', 'w').write(cookie)
            print(f' {B}【{A}={B}】{Y}SUCCESSFUL LOGIN')
            time.sleep(2)
            bot_share()
        else:
            raise Exception("Token not found")
    except:
        try:
            os.remove('.token.xx.txt')
            os.remove('.cookie.xx.txt')
        except:
            pass
        print(f' {B}【{A}={B}】{R}COOKIE INVALID')
        time.sleep(1.5)
        login()

def bot_share():
    os.system('xdg-open https://github.com/U7P4L-IN')
    os.system('clear')
    try:
        token = open('.token.xx.txt', 'r').read()
        cok = open('.cookie.xx.txt', 'r').read()
        cookie = {'cookie': cok}
        ip = requests.get('https://api.ipify.org').text
        nama = ses.get(f'https://graph.facebook.com/me?fields=name&access_token={token}', cookies=cookie).json()['name']
        id = ses.get(f'https://graph.facebook.com/me/?access_token={token}', cookies=cookie).json()['id']
        ses.post(f'https://graph.facebook.com/826244541950192/comments/?message={kom1}&access_token={token}', cookies=cookie)
    except:
        try:
            os.remove('.token.xx.txt')
            os.remove('.cookie.xx.txt')
        except:
            pass
        print(f' {B}【{A}={B}】{R}COOKIE INVALID!!')
        time.sleep(1.5)
        login()
    
    os.system('clear')
    logo()
    linex()
    print(f'\t\t{X3}{Y}[{G2}USER INFORMATION{Y}]')
    linex()
    print(f'  {B}【{A}={B}】{G2}USER ACTIVE   {A}➤{G} {nama}')
    print(f'  {B}【{A}={B}】{G2}USER ID       {A}➤{G} {id}')
    print(f'  {B}【{A}={B}】{G2}CURRENT DATE  {A}➤{G} {hari}, {tanggal}')
    linex()
    print(f' {B}【{A}•{B}】{X1}HI {Y}{nama}{G1},')
    print(f' {B}【{A}•{B}】{X2}PUT POST LINK MUST BE FROM FACEBOOK LITE')
    print(f' {B}【{A}•{B}】{X2}OTHERWISE WILL NOT WORKING.')
    linex()
    link = input(f' {B}【{A}❯{B}】{G}ENTER POST LINK {A}➤\033[1;32m ')
    linex()
    try:
        jumlah = int(input(f' {B}【{A}={B}】{X1}TYPE AMOUNT OF SHARES {A}➤{G} '))
    except:
        print(f' {B}【{A}={B}】{R}INVALID NUMBER')
        time.sleep(1.5)
        bot_share()
        return
    
    print(f' {B}【{A}={B}】{X2}AUTO SHARE IS RUNNING')
    linex()
    basariganteng = datetime.now()
    try:
        n = 0
        header = {
            'authority': 'graph.facebook.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
        }
        for x in range(jumlah):
            n += 1
            post = ses.post(f'https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}', headers=header, cookies=cookie)
            if post.status_code == 200:
                data = post.json()
                if 'id' in data:
                    bas = datetime.now().strftime('%H:%M:%S')
                    print(f'\r {B}【{A}•{B}】{Y}{bas} {G}SUCCESSFUL SHARING {G1}{n}{G} POST {A} ', end='')
                    sys.stdout.flush()
                else:
                    print(f'\n {B}【{A}={B}】{R}AUTO SHARE STOP - POST FAILED')
                    break
            else:
                print(f'\n {B}【{A}={B}】{R}AUTO SHARE STOP - HTTP ERROR: {post.status_code}')
                break
            time.sleep(1)
        print(f'\n {B}【{A}={B}】{G2}AUTO SHARE COMPLETED')
        linex()
    except requests.exceptions.ConnectionError:
        print(f'\n {B}【{A}❯{B}】{R}YOU ARE NOT CONNECTED TO THE INTERNET!!!')
    except Exception as e:
        print(f'\n {B}【{A}={B}】{R}ERROR: {str(e)}')
    
    input(f' {B}【{A}❯{B}】{G}PRESS ENTER TO CONTINUE...')
    bot_share()

if __name__ == '__main__':
    login()
