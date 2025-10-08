""" Decompiled by Exotic Hridoy """

import importlib
import requests as r
from bs4 import BeautifulSoup as bs
import os, sys
import datetime, time
import platform

k = '\033[1;33m'  # Warna Kuning
a = '\033[1;30m'  # Warna Hitam/Abu-Abu
m = '\033[1;31m'  # Warna Merah
h = '\033[1;32m'  # Warna Hijau
p = '\033[1;37m'  # Warna Putih
b = '\033[1;34m'  # Warna Biru
v = '\033[1;35m'  # Warna Violet
u = '\033[1;36m'  # Warna Ungu
j = '\033[1;38;5;202m'  # Warna Jingga

# Clear Terminal
def clear():
    if 'linux' in sys.platform.lower():os.system('clear')
    elif 'win' in sys.platform.lower():os.system('cls')

logo = r"""
╔═╗┬ ┬┌─┐┬─┐┬ ┬┌─┐┌┬┐┌─┐┌┬┐┌─┐┌┬┐┌─┐
╠═╝└┬┘│  ├┬┘└┬┘├─┘ │ │ │ │││ ││││├┤  | Coded by : Ferly Afriliyan and Merch
╩   ┴ └─┘┴└─ ┴ ┴   ┴ └─┘─┴┘└─┘┴ ┴└─┘
[•] obfuscate python code with methods that are quite difficult to reverse
"""[:-1]

# Memeriksa apakah modul requests terinstall
try:
    clear()
    importlib.import_module('requests')
    requests_module_installed = True
except ImportError:
    requests_module_installed = False

# Memeriksa apakah modul Crypto (pycryptodome) terinstall
try:
    clear()
    importlib.import_module('Crypto')
    crypto_module_installed = True
except ImportError:
    crypto_module_installed = False

if not crypto_module_installed:
    print(f"{h}[{a}•{h}] {p}Modul Crypto   : ({a}pycryptodome{p}) belum terinstall.")
    print(f"{h}[{a}•{h}] {p}Ketik perintah : pip install {a}pycryptodome")

# Memeriksa apakah modul bs4 terinstall
try:
    importlib.import_module('bs4')
    bs4_module_installed = True
except ImportError:
    bs4_module_installed = False

if not crypto_module_installed or not requests_module_installed or not bs4_module_installed:
    print(f"{h}[{a}•{h}] {p}Beberapa modul belum terinstal. Anda perlu menginstal modul-modul berikut {a}:")
    if not requests_module_installed:
        print(f"  {a}- {p}pycryptodome (Crypto)")
        print(f"  {a}- {p}requests")
        print(f"  {a}- {p}bs4 (Beautiful Soup)")
    print(f"{h}[{a}•{h}] {p}Ketik perintah: pip install {a}pycryptodome bs4 requests {p}")
else:
    # Clear Terminal
    if 'linux' in platform.system().lower():os.system('clear')
    elif 'win' in platform.system().lower():os.system('cls')

    Take_the_encryption = "https://pyobfuscate.com/pyd"
    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%A, %B %d, %Y %H:%M:%S")

    # Meminta pengguna untuk memasukkan nama file input
    print(logo)
    print("")
    input_file = input(f"{h}[{a}•{h}] {p}Masukkan nama file Input {a}: {p}")
    if not input_file:
        print(f"{m}[{a}!{m}] {p}File '{input_file}' tidak ditemukan.")
        exit()
    elif not input_file.endswith(".py"):
        print(f"{m}[{a}!{m}] {p}File harus memiliki ekstensi .py {p}")
        exit()
        input_text = None

    # Membaca teks dari file input
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            input_text = file.read()
    except FileNotFoundError:
        print(f"{p}File '{input_file}' tidak ditemukan.")
        input_text = None

    # Jika teks input berhasil dibaca, maka lakukan proses enkripsi
    if input_text:
        # Kirim permintaan POST
        response = r.post('https://pyobfuscate.com/pyd', data={'input_text': input_text})

        # Parsing hasil respons
        source = bs(response.text, 'html.parser')

        # Cari elemen textarea dengan id 'myTextarea2'
        result = source.find('textarea', {'id': 'myTextarea2'})

        # Meminta pengguna untuk memasukkan nama file output
        while True:
            output_file = input(f"{h}[{a}•{h}] {p}Masukkan nama file Output {a}: {p}")
            if not output_file:
                print(f"{m}[{a}!{m}] {p}Isi dengan benar {m}! {p}")
                exit()
            elif not output_file.endswith(".py"):
                print(f"{m}[{a}!{m}] {p}File output harus memiliki ekstensi .py {p}")
                exit()
            else:
                break

        # Simpan teks yang telah dienkripsi ke dalam file output
        if result:
            encrypted_code = result.text
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(f'# Take the encryption method from the website = {Take_the_encryption}\n')
                file.write(f'created_by = "Ferly Afriliyan and Merch"\n')
                file.write(f'# Time : {current_time_str}\n')
                file.write(f'# Platform : {platform.system()}-{platform.machine()}\n' + encrypted_code)
            print(f"{h}[{a}•{h}] {p}Berhasil, file {input_file} tersimpan di {a}: {output_file} {p}")
        else:
            print(f"{m}[{a}!{m}] {p}Tidak dapat menemukan kode Obfuscate.")
    else:
        print(f"{h}[{k}+{h}] {p}Proses Obfuscate dibatalkan karena file Input tidak ditemukan.")
