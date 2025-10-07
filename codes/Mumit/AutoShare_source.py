""" Decompiled by Exotic Hridoy """

import os
import re
import requests
import json
import sys
import time
import random

ses = requests.Session()

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def runtxt(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo = '''\x1b[1;96m
 \x1b[1;41m\x1b[1;97m UNLIMITED AUTO \x1b[;0m\x1b[1;91m
 \x1b[1;95m
    _______ _     _ _______  ______ _______
    |______ |_____| |_____| |_____/ |______
    ______| |     | |     | |    \\_ |______   \x1b[1;92m

 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃  [\x1b[1;91m✓\x1b[1;92m]  CREATE BY    \x1b[1;91m:  \x1b[1;92mMUMIT ISLAM HIMU     ┃
 ┃  [\x1b[1;91m✓\x1b[1;92m]  TOOL         \x1b[1;91m:  \x1b[1;92mUNLIMITED SHARE      ┃
 ┃  [\x1b[1;91m✓\x1b[1;92m]  STATUS       \x1b[1;91m:  \x1b[1;92mFREE ENJOY           ┃
 ┃  [\x1b[1;91m✓\x1b[1;92m]  USE SYSTEM   \x1b[1;91m:  \x1b[1;92mDATA\x1b[1;91m/\x1b[1;92mWIFI            ┃
 ┃  [\x1b[1;91m✓\x1b[1;92m]  FACEBOOK     \x1b[1;91m:  \x1b[1;92mMUMIT ISLAM          ┃
 ┃  [\x1b[1;91m✓\x1b[1;92m]  GITHUB       \x1b[1;91m:  \x1b[1;92mMUMIT-404-CYBER      ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''

def lines():
    print('\x1b[1;37m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def mumit_menu():
    clear_screen()
    print(logo)
    print('\x1b[1;32m [\x1b[1;91m1\x1b[1;92m] AUTO SHARE')
    print('\x1b[1;32m [\x1b[1;91m2\x1b[1;92m] LOGOUT COOKIE')
    print('\x1b[1;32m [\x1b[1;91m3\x1b[1;92m] HOW TO MAKE COOKIE')
    lines()
    mumit = input(' \x1b[1;32m[\x1b[1;91m?\x1b[1;92m] SELECT MENU : ')

    if mumit in ['1', '01']:
        menu()
    elif mumit in ['2', '02']:
        try:
            os.remove('cookie.txt')
            os.remove('token.txt')
        except:
            pass
        lines()
        print(' \x1b[1;32m[\x1b[1;91m✓\x1b[1;92m] COOKIE LOGOUT SUCCESSFULL')
        time.sleep(1)
        mumit_menu()
    elif mumit in ['3', '03']:
        print(' \x1b[1;32m[\x1b[1;91m•\x1b[1;92m] Opening tutorial...')
        # os.system('xdg-open https://youtu.be/aiB2HZfbQTE')
        time.sleep(2)
        mumit_menu()
    elif mumit in ['0', '00']:
        clear_screen()
        print(logo)
        print('Exited Tools')
        exit()
    else:
        print('\x1b[1;92m [\x1b[1;91m!\x1b[1;92m]\x1b[1;91m Select A Valid Option')
        time.sleep(1.0)
        mumit_menu()

def login():
    clear_screen()
    print(logo)
    cookie = input(' \x1b[1;32m[\x1b[1;91m•\x1b[1;92m] PUT COOKIE : ')
    
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
            'referer': 'https://www.facebook.com/',
            'host': 'business.facebook.com',
            'origin': 'https://business.facebook.com',
            'upgrade-insecure-requests': '1',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'content-type': 'text/html; charset=utf-8'
        }
        
        data = ses.get('https://business.facebook.com/business_locations', 
                      headers=headers, 
                      cookies={'cookie': cookie})
        
        find_token = re.search('(EAAG\\w+)', data.text)
        if find_token:
            with open('token.txt', 'w') as f:
                f.write(find_token.group(1))
            with open('cookie.txt', 'w') as f:
                f.write(cookie)
            lines()
            print(' \x1b[1;32m[\x1b[1;91m✓\x1b[1;92m] LOGIN SUCCESSFULL ')
            time.sleep(1.5)
            menu()
        else:
            raise Exception("Token not found")
            
    except Exception as e:
        try:
            os.remove('token.txt')
            os.remove('cookie.txt')
        except:
            pass
        exit(' \x1b[1;32m[\x1b[1;91m!\x1b[1;92m] COOKIE EXPIRED OR INVALID')

def menu():
    try:
        token = open('token.txt', 'r').read()
        cok = open('cookie.txt', 'r').read()
        cookie = {'cookie': cok}
        
        response = ses.get(f'https://graph.facebook.com/me?fields=name&access_token={token}', cookies=cookie)
        nama = response.json()['name']
        
    except:
        login()
    
    clear_screen()
    print(logo)
    idt = input(' \x1b[1;32m[\x1b[1;91m?\x1b[1;92m] PUT PUBLIC POST LINK : ')
    lines()
    print(' \x1b[1;32m[\x1b[1;91m•\x1b[1;92m] EXAMPLE : 10/100/1000/10000 ETC ')
    lines()
    
    try:
        limit = int(input(' \x1b[1;32m[\x1b[1;91m?\x1b[1;92m] PUT SHARE LIMIT : '))
    except:
        print(' \x1b[1;32m[\x1b[1;91m!\x1b[1;92m] INVALID NUMBER')
        time.sleep(2)
        menu()
    
    lines()
    print(' \x1b[1;32m[\x1b[1;91m•\x1b[1;92m] PROCESS HAS STARTED.....')
    time.sleep(1)
    lines()
    
    try:
        n = 0
        headers = {
            'authority': 'graph.facebook.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36'
        }
        
        for x in range(limit):
            n += 1
            post = ses.post(f'https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}', 
                          headers=headers, cookies=cookie)
            
            if post.status_code == 200:
                data = post.json()
                if 'id' in data:
                    runtxt(f' \x1b[1;32m[\x1b[1;91m+\x1b[1;92m] SHARE SENDING BY INNOCENT BOY \x1b[1;96m• \x1b[1;92m[\x1b[1;95m{n}\x1b[1;92m] ')
                else:
                    print(f' \x1b[1;32m[\x1b[1;91m!\x1b[1;92m] Failed to share: {data}')
            else:
                print(f' \x1b[1;32m[\x1b[1;91m!\x1b[1;92m] HTTP Error: {post.status_code}')
                
            time.sleep(0.5)
            
    except Exception as e:
        print(f' \x1b[1;32m[\x1b[1;91m!\x1b[1;92m] Error: {str(e)}')
        time.sleep(2)
        mumit_menu()

if __name__ == '__main__':
    mumit_menu()
