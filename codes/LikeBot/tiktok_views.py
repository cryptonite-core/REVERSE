""" Decompiled by Exotic Hridoy """

import os
import re
import sys
import json
import time
import base64
import random
import threading
import ctypes
import socket
from time import sleep, strftime
from datetime import date, datetime
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits
from prettytable import PrettyTable
from colorama import init, Fore
from random import choice, randint, shuffle
from concurrent.futures import ThreadPoolExecutor

try:
    import requests
    import colorama
    import prettytable
    import pystyle
except:
    os.system("pip install requests colorama prettytable pystyle")

from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

biru = '\x1b[1;96m'
mati = '\x1b[0m'
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red = '\u001b[31;1m'
yellow = '\u001b[33;1m'
green = '\u001b[32;1m'
blue = '\u001b[34;1m'
tim = '\033[1;35m'
xanhlam = '\033[1;36m'
xam = '\033[1;30m'
black = '\033[1;19m'

def jalan(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)

def logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo = f"""
        [ {yellow}Tiktok Auto Views{mati} ]
    """
    jalan(logo)

def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address

class Zefoy:
    def __init__(self):
        self.base_url = 'https://zefoy.com/'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/112.0.0.0 Safari/537.36'
        }
        self.session = requests.Session()
        self.captcha_ = {}
        self.service = 'Views'
        self.services = {}
        self.services_ids = {}
        self.services_status = {}
        self.url = input(f" {trang}[{do}{trang}] Enter TikTok video URL: ")

    def check_config(self):
        while True:
            try:
                last_url = self.url
                if last_url != self.url:
                    self.get_video_id()
            except Exception as e:
                print(e)
            time.sleep(4)

    def get_captcha(self):
        if os.path.exists('session'):
            self.session.cookies.set(
                "PHPSESSID",
                open('session', encoding='utf-8').read(),
                domain='zefoy.com'
            )
        request = self.session.get(self.base_url, headers=self.headers)
        if 'Enter Video URL' in request.text:
            self.video_key = (
                request.text.split('" placeholder="Enter Video URL"')[0]
                .split('name="')[-1]
            )
            return True

        try:
            for x in re.findall(r'<input type="hidden" name="(.*)" value="(.*)">', request.text):
                self.captcha_[x[0]] = x[1]

            self.captcha_1 = (
                request.text.split('type="text" name="')[1]
                .split('" oninput="this.value=this.value.toLowerCase()"')[0]
            )
            captcha_url = (
                request.text.split('<img src="')[1]
                .split('" onerror="imgOnError()" class="')[0]
            )
            req = self.session.get(f"{self.base_url}{captcha_url}", headers=self.headers)
            open('captcha.png', 'wb').write(req.content)
            print(f" {trang}[{do}{trang}] Bypassing captcha... please wait")
            return False
        except Exception as e:
            print(f" {trang}[{do}{trang}] Captcha error: {e}")
            time.sleep(2)
            self.get_captcha()

    def send_captcha(self, new_session=False):
        if new_session:
            self.session = requests.Session()
            os.remove('session')
            time.sleep(2)
        if self.get_captcha():
            print(f" {trang}[{do}{trang}] Captcha already bypassed.")
            return (True, 'Existing session')
        captcha_solve = self.solve_captcha('captcha.png')[1]
        self.captcha_[self.captcha_1] = captcha_solve
        request = self.session.post(self.base_url, headers=self.headers, data=self.captcha_)
        if 'Enter Video URL' in request.text:
            open('session', 'w', encoding='utf-8').write(self.session.cookies.get('PHPSESSID'))
            self.video_key = (
                request.text.split('" placeholder="Enter Video URL"')[0]
                .split('name="')[-1]
            )
            return (True, captcha_solve)
        return (False, captcha_solve)

    def solve_captcha(self, path_to_file=None, b64=None):
        if path_to_file:
            task = path_to_file
        else:
            open('temp.png', 'wb').write(base64.b64decode(b64))
            task = 'temp.png'
        req = self.session.post(
            'https://api.ocr.space/parse/image?K87899142388957',
            headers={'apikey': 'K87899142388957'},
            files={'task': open(task, 'rb')}
        ).json()
        solved_text = req['ParsedResults'][0]['ParsedText']
        return True, solved_text.strip()

    def update_name(self):
        while True:
            try:
                ctypes.windll.kernel32.SetConsoleTitleA(self.text.encode())
                video_info = self.get_video_info()
                self.text = f" [Vchh/] | Views: {video_info['viewCount']} "
            except:
                pass
            time.sleep(5)

    def get_video_info(self):
        return {"viewCount": 1234}

    def get_table(self):
        pass

    def use_service(self):
        pass

os.system('cls' if os.name == 'nt' else 'clear')

today = date.today()
now = datetime.now()
ip = get_ip_from_url("http://kiemtraip.com/raw.php")

logo()

if __name__ == "__main__":
    Z = Zefoy()
    threading.Thread(target=Z.check_config).start()
    threading.Thread(target=Z.update_name).start()
    Z.send_captcha()
    Z.get_table()

    while True:
        try:
            if 'Service is currently not working' in str(Z.use_service()):
                print(f'{do}{trang} Service not found, retrying...')
                time.sleep(5)
        except Exception as e:
            print(f'{red}Service down: {e}{mati}')
            time.sleep(10)
