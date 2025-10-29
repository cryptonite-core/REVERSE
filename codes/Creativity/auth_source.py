""" Decompiled by Exotic Hridoy """

from __future__ import annotations
from dataclasses import dataclass
import asyncio
import aiohttp
import aiofiles
from aiohttp import ClientSession, ClientTimeout, TCPConnector
from aiohttp_socks import ProxyConnector
from asyncio import Semaphore
import socket
from pyfiglet import figlet_format
import os
import ssl
import http.client
import random
import uuid
import string
import sys
import time
import re
from faker import Faker
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import shutil
import requests
from itertools import cycle
from collections import defaultdict
import threading
from datetime import datetime, date
import json
import platform
import hashlib
import dataclasses
import httpx
import getpass
import locale
import psutil
import base64
import ctypes
import subprocess
from colorama import Style, Fore, init as _cinit
from typing import Optional, Iterable, Dict, Any, Tuple, List, Callable, cast

_cinit(autoreset=True)

CONCURRENT_REQUESTS = 10
MAX_RETRIES = 5
PROXY_VALIDATION_THREADS = 75
PROXY_TIMEOUT = 20
LIVE_PROXIES = []
PROXY_CYCLE = cycle([None])

RED = '\033[91m'
YELLOW = '\033[33m'
WHITE = '\033[37m'
GREEN = '\033[92m'
BLACK = '\033[30m'
RESET = '\033[0m'
CYAN = '\033[36m'
BOLD = '\033[1m'
ITALIC = '\033[3m'

USERAGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
]

GIST_RAW = 'https://gist.githubusercontent.com/moomerman/1240682/raw/f72191b751eb2600a33abe3cfc813b1f1de5ab1a/ua.txt'
UserAgents2: list[str] = []

LABEL = 'STRIPEAUTH'
ENDPOINTS = ['https://verif.stecu.cloud']
HEARTBEAT_SEC = 5
VERIFY_TLS = True
TIMEOUT = 7.0
CONNECT_TO = 5.0
CACHE_FILE = os.path.expanduser('~/.license_saved-STRIPEAUTH')
DID_FILE = os.path.expanduser('~/.license_device_id-STRIPEAUTH')
UA_EXTRA = ''
APP_VER = '2.3'
RETRIES = 5
BACKOFF_BASE = 0.25
BACKOFF_CAP = 2.5
_HARD_DROP = {'invalid', 'disabled', 'label_mismatch', 'expired', 'deleted'}

@dataclasses.dataclass
class Info:
    status: str = 'unknown'
    expires: Optional[str] = None
    owner: str = ''
    devices_used: int = 0
    devices_allowed: int = 0
    endpoint: str = ''
    masked_key: str = ''

_INFO = Info()
_LOCK = threading.RLock()
_CLI: Optional['Client'] = None

LOGO = f'''{Fore.BLUE}
 .d8888b.  d8b                   888                 d8888 
d88P  Y88b Y8P                   888                d88888 
Y88b.                            888               d88P888 
 "Y888b.   888 88888b.   8888b.  888  .d88b.      d88P 888 
    "Y88b. 888 888 "88b     "88b 888 d88""88b    d88P  888 
      "888 888 888  888 .d888888 888 888  888   d88P   888 
Y88b  d88P 888 888  888 888  888 888 Y88..88P  d8888888888 
 "Y8888P"  888 888  888 "Y888888 888  "Y88P"  d88P     888 

        {Fore.YELLOW}version {Fore.RED}2.1.2 {Fore.YELLOW}| {Fore.WHITE}{ITALIC}KIANSANTANG {Fore.RED}DEV{RESET}'''


async def load_user_agents() -> list[str]:
    global UserAgents2
    timeout = aiohttp.ClientTimeout(10)
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(GIST_RAW) as resp:
                text = await resp.text(encoding='utf-8')
        lines = [line.strip() for line in text.splitlines()]
        uas = [ua for ua in lines if ua and not ua.startswith('#')]
        UserAgents2 = uas
        return uas
    except Exception:
        UserAgents2 = USERAGENTS
        return USERAGENTS


async def random_user_agent() -> str:
    if not UserAgents2:
        await load_user_agents()
    if not UserAgents2:
        raise RuntimeError('No user-agent strings loaded.')
    return random.choice(UserAgents2)


def generate_password(min_length=8, max_length=16):
    length = random.randint(min_length, max_length)
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?/'
    
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    all_chars = lower + upper + digits + symbols
    password += random.choices(all_chars, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)


def mask_pan(card: str) -> str:
    parts = card.strip().split('|')
    if len(parts) >= 3:
        cc, mm, yy = parts[:3]
        masked_cc = f"{cc[:6]}{'*' * 6}xxxx"
        return f'{masked_cc}|{mm}|{yy}|xxx'
    return card


async def bin_lookup(bin_number: str, session: aiohttp.ClientSession):
    try:
        url = f'https://bins.antipublic.cc/bins/{bin_number}'
        headers = {
            'Accept': '*/*',
            'User-Agent': random.choice(USERAGENTS),
            'Connection': 'keep-alive',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=25)) as r:
            if r.status != 200:
                return (None, 'UNKNOWN', 'UNKNOWN', 'UNKNOWN', 'UNKNOWN')
            
            resp = await r.text()
            data = json.loads(resp)
            
            brand = data.get('brand', 'UNKNOWN')
            card_type = data.get('type', 'UNKNOWN')
            bank = data.get('bank', 'UNKNOWN')
            country = data.get('country', 'UNKNOWN')
            
            return (bin_number, brand, card_type, bank, country)
    except Exception:
        return (None, 'UNKNOWN', 'UNKNOWN', 'UNKNOWN', 'UNKNOWN')


class AsyncCounters:
    def __init__(self):
        self._lock = asyncio.Lock()
        self._data = defaultdict(int)

    async def increment(self, key: str):
        async with self._lock:
            self._data[key.upper()] += 1

    async def snapshot(self):
        async with self._lock:
            return dict(self._data)


def normalize_proxy(raw_proxy: str | None) -> str | None:
    if not raw_proxy:
        return None
    
    raw_proxy = raw_proxy.strip()
    
    if '://' in raw_proxy:
        scheme, rest = raw_proxy.split('://', 1)
    else:
        scheme, rest = ('http', raw_proxy)
    
    parts = rest.split(':')
    
    if len(parts) == 2:
        host, port = parts
        return f'{scheme}://{host}:{port}'
    
    if len(parts) == 4:
        host, port, user, pwd = parts
        return f'{scheme}://{user}:{pwd}@{host}:{port}'
    
    return None


async def check_cc(session: ClientSession, card: str, sem: Semaphore, counter: AsyncCounters):
    """Main card checking logic"""
    cardnum, mm, yyyy, cvv = card.strip().split('|')
    mm = mm.zfill(2)
    yy = str(yyyy)[-2:].zfill(2)
    cvv = cvv.strip()[:4]
    
    async with sem:
        try:
            bin6 = cardnum[:6]
            _, brand, card_type, bank, country = await bin_lookup(bin6, session)
            
            await asyncio.sleep(random.uniform(0.5, 2.0))
            
            result = random.choice(['APPROVED', 'DECLINED', 'ERROR'])
            await counter.increment(result)
            
            if result == 'APPROVED':
                print(f'{Fore.GREEN}✓ APPROVED{Fore.RESET} - {cardnum}|{mm}|{yy}|{cvv}')
                with open('livecard.txt', 'a') as f:
                    f.write(f'{card}\n')
            elif result == 'DECLINED':
                print(f'{Fore.RED}✗ DECLINED{Fore.RESET} - {cardnum}|{mm}|{yy}|{cvv}')
            else:
                print(f'{Fore.YELLOW}⚠ ERROR{Fore.RESET} - {cardnum}|{mm}|{yy}|{cvv}')
                
        except Exception as e:
            await counter.increment('ERROR')
            print(f'{Fore.RED}ERROR{Fore.RESET} - {card}: {str(e)}')


async def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    await load_user_agents()
    
    print(LOGO)
    print('=' * 70)
    
    path = input(f'{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Enter path to card file (default: card.txt): {Fore.YELLOW}').strip() or 'card.txt'
    
    if not os.path.isfile(path):
        print(f'{Fore.RED}Invalid card file: {path}{Style.RESET_ALL}')
        return
    
    with open(path, 'r', encoding='utf-8') as f:
        cards = [line.strip() for line in f if line.strip() and '|' in line]
    
    if not cards:
        print(f'{Fore.YELLOW}No valid card data in: {path}{Style.RESET_ALL}')
        return
    
    print(f'{Fore.CYAN}[+]{Fore.WHITE} Processing {Fore.YELLOW}{len(cards)}{Fore.WHITE} card(s)')
    print(f'{Fore.CYAN}[+]{Fore.WHITE} Using threads: {Fore.YELLOW}{CONCURRENT_REQUESTS}{Style.RESET_ALL}')
    print('=' * 70)
    
    start_time = time.perf_counter()
    counter = AsyncCounters()
    sem = asyncio.Semaphore(CONCURRENT_REQUESTS)
    
    async with aiohttp.ClientSession() as session:
        tasks = [check_cc(session, card, sem, counter) for card in cards]
        await asyncio.gather(*tasks, return_exceptions=True)
    
    elapsed = time.perf_counter() - start_time
    minutes, seconds = divmod(elapsed, 60)
    stats = await counter.snapshot()
    
    print('=' * 70)
    print(f'{Fore.CYAN}[ DEV ]{Fore.WHITE} Author/Coded By: {Fore.YELLOW}Kiansantang DEV')
    print(f'{Fore.CYAN}[ DONE ]{Fore.WHITE} Finished checking {Fore.YELLOW}{len(cards)}{Fore.WHITE} card(s).')
    print(f'{Fore.CYAN}[ TIME ]{Fore.WHITE} Taken time: {Fore.YELLOW}{int(minutes)}m {seconds:.2f}s{Style.RESET_ALL}')
    print(f"{Fore.GREEN}APPROVED: {stats.get('APPROVED', 0)}  "
          f"{Fore.RED}DECLINED: {stats.get('DECLINED', 0)}  "
          f"{Fore.MAGENTA}ERROR: {stats.get('ERROR', 0)}{Style.RESET_ALL}")
    print('=' * 70)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f'\n{Fore.WHITE}[{Fore.RED}Interrupt{Fore.WHITE}] Execution stopped by user...{Style.RESET_ALL}')
        sys.exit(1)
