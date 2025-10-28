""" Decompiled by Exotic Hridoy """

from __future__ import annotations
import os
import re
import sys
import json
import math
import time
import random
import socket
import logging
import argparse
import threading
from typing import Optional, Dict, Any, List, Tuple, Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import base64
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as executor
from fake_useragent import UserAgent
from colorama import Fore, Style, init
from tqdm import tqdm
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

init(autoreset=True)

id = []
LOG = logging.getLogger('smartdown')
LOG.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stderr)
ch.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s', '%H:%M:%S'))
LOG.addHandler(ch)


def supports_range(url, headers=None):
    try:
        r = requests.head(url, headers=headers, timeout=10)
        accept_ranges = r.headers.get('Accept-Ranges', '')
        return 'bytes' in accept_ranges.lower()
    except Exception:
        return False


def download_chunk(url, start, end, headers, part_path, timeout=15):
    h = headers.copy() if headers else {}
    h['Range'] = f'bytes={start}-{end}'
    with requests.get(url, headers=h, stream=True, timeout=timeout) as r:
        r.raise_for_status()
        with open(part_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)


def safe_download(url, dest_path, headers=None, retries=5, timeout=15):
    session = requests.Session()
    retry_strategy = Retry(
        total=retries,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504, 429],
        allowed_methods=['HEAD', 'GET']
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    with session.get(url, headers=headers, stream=True, timeout=timeout) as r:
        r.raise_for_status()
        total = int(r.headers.get('Content-Length', 0))
        progress = tqdm(
            total=total,
            unit='B',
            unit_scale=True,
            desc='Luxin-Porn',
            dynamic_ncols=True,
            miniters=1,
            leave=True,
            ascii=True
        )
        with open(dest_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    progress.update(len(chunk))
        progress.close()
    print(f'\n✅ Selesai! File tersimpan di: {dest_path}')


def adaptive_download(video_id, data_id, dest_path, num_threads=8, retries=10, timeout=30):
    print('🔍 Mengecek dukungan Range dari server...')
    headers = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://www.eporner.com/'}
    url = f'https://www.eporner.com/dload/{video_id}/360/{data_id}-360p.mp4?click=1'

    range_ok = supports_range(url, headers)
    if not range_ok:
        print('⚠️ Server tidak mendukung Range download. Gunakan mode single-stream.')
        safe_download(url, dest_path, headers=headers, retries=retries, timeout=timeout)
        return

    print('✅ Server mendukung Range. Menggunakan multi-thread download...')
    r = requests.head(url, headers=headers, timeout=timeout)
    total_size = int(r.headers.get('Content-Length', 0))
    if total_size == 0:
        print('❌ Tidak dapat mengetahui ukuran file. Beralih ke mode single-thread.')
        safe_download(url, dest_path, headers=headers, retries=retries, timeout=timeout)
        return

    part_size = total_size // num_threads
    parts = []
    for i in range(num_threads):
        start = i * part_size
        end = (i + 1) * part_size - 1 if i < num_threads - 1 else total_size - 1
        part_path = f'{dest_path}.part{i}'
        parts.append((start, end, part_path))

    with ThreadPoolExecutor(max_workers=num_threads) as ex:
        list(tqdm(ex.map(lambda p: download_chunk(url, p[0], p[1], headers, p[2], timeout), parts),
                  total=len(parts), desc='Downloading', unit='part'))

    with open(dest_path, 'wb') as final:
        for _, _, part_path in parts:
            with open(part_path, 'rb') as pf:
                final.write(pf.read())
            os.remove(part_path)

    print(f'\n✅ Selesai! File tersimpan di: {dest_path}')
    print(f'Ukuran file: {os.path.getsize(dest_path):,} bytes')


def extract_video_id(path: str) -> Optional[str]:
    if not path:
        return None
    m = re.search(r'/(?:video-|hd-video/|embed/|watch/)([A-Za-z0-9_\-]+)', path)
    if m:
        return m.group(1)
    tokens = re.findall(r'[A-Za-z0-9_\-]{6,}', path)
    return tokens[0] if tokens else None


def banner():
    print(Fore.CYAN + Style.BRIGHT + '\n██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗')
    print(Fore.CYAN + '██╔════╝ ██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗')
    print(Fore.CYAN + '██║  ███╗███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝')
    print(Fore.CYAN + '██║   ██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗')
    print(Fore.CYAN + '╚██████╔╝██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║')
    print(Fore.CYAN + ' ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝\n')
    print(Fore.MAGENTA + Style.BRIGHT + '   ✦ Eporner Downloader Video ✦')
    print(Fore.YELLOW + '   Author : Luxin x0bf')
    print(Fore.YELLOW + '   Tools  : Video Scraper & Downloader')
    print(Fore.YELLOW + '   Panel  : Input tags / Auto Fetch\n')


def msg(text: str):
    for x in text:
        print(x, end='', flush=True)
        time.sleep(0.02)
    print()


def manual():
    print(Fore.GREEN + Style.BRIGHT + '\n[ 18+ Video Downloader ]')
    print(Fore.WHITE + '\n    1. Masukkan judul video (gunakan spasi atau kata kunci).')
    print('    2. Pilih nomor dari daftar hasil pencarian.')
    print('    3. Video akan otomatis diunduh dengan progress bar.\n')


def fetch_video_id():
    try:
        judul = input(Fore.CYAN + '[+] Masukan Judul: ' + Style.RESET_ALL)
        headers = {'user-agent': UserAgent().random}
        h = judul.replace(' ', '-').lower()
        d = base64.b64decode('aHR0cHM6Ly93d3cuZXBvcm5lci5jb20vdGFnLw==').decode()
        r = requests.get(f'{d}{h}/', headers=headers)
        r.raise_for_status()
        content = parser(r.text, 'html.parser')
        if not content:
            return None
        for i, mb_div in enumerate(content.find_all('div', class_='mb')):
            data_id = mb_div.get('data-id')
            mbunder = mb_div.find('div', class_='mbunder')
            if not mbunder:
                continue
            title_tag = mbunder.find('p', class_='mbtit').find('a')
            title = title_tag.text.strip() if title_tag else 'untitled'
            href = title_tag['href'] if title_tag and title_tag.has_attr('href') else '#'
            views_tag = mbunder.find('span', class_='mbvie')
            views = views_tag.text.strip() if views_tag else '0'
            id.append({'number': i, 'judul': title, 'path': href, 'ditonton': views, 'data_id': data_id})
    except Exception as e:
        LOG.error(f"Gagal memuat hasil: {e}")
        return None


def fetch_video_number():
    fetch_video_id()
    if not id:
        msg(Fore.RED + '[!] Tidak ada hasil ditemukan.')
        return None

    print(Fore.GREEN + '\n[ Hasil Pencarian ]')
    for x in id:
        print(Fore.CYAN + f"{x['number']}. " + Fore.WHITE + f"{x['judul']} | {x['ditonton']}")

    number = input(Fore.CYAN + '\n[+] Pilih Nomor: ' + Style.RESET_ALL)
    if not number.isdigit():
        msg(Fore.RED + '[!] Input harus berupa angka.')
        return None

    number = int(number)
    selected = next((item for item in id if item['number'] == number), None)
    if not selected:
        msg(Fore.RED + '[!] Nomor Tidak Valid/Tidak Tersedia')
        return None

    vid = extract_video_id(selected.get('path') or '')
    if not vid:
        LOG.error('Could not extract video id from path: %s', selected.get('path'))
        return None

    filename_raw = f"{selected.get('judul')}.mp4"
    safe_fname = re.sub(r'[^\w\-\.\s]', '_', filename_raw).strip()
    dest_dir = os.path.expanduser('/sdcard/Download/Result')
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, safe_fname)
    adaptive_download(vid, selected['data_id'], dest)


if __name__ == '__main__':
    os.system('clear')
    banner()
    manual()
    fetch_video_number()
