""" Decompiled by Exotic Hridoy """

try:
    import requests, json, time, os, random, re
    from rich.columns import Columns
    from rich import print
    from rich.console import Console
    from rich.panel import Panel
    from requests.exceptions import RequestException
except (Exception, KeyboardInterrupt) as e:
    exit(f"[Error] {str(e).title()}!")

Follower, Sukses, Gagal, Status, Logging = {
    "Count": 404
}, [], [], [], []

def Banner():
    os.system(
        'cls' if os.name == 'nt' else 'clear'
    )
    print(Panel("""[bold red]●[bold yellow] ●[bold green] ●[/]
[bold red]___________      .__  .__ __
\_   _____/______|  | |__|  | __ ___________  ______
 |    __)_\___   /  | |  |  |/ // __ \_  __ \/  ___/
 |        \/    /|  |_|  |    <\  ___/|  | \/\___ \ 
[bold white]/_______  /_____ \____/__|__|_ \\___  >__|  /____  >
        \/      \/            \/    \/           \/ 
     [bold white on red]Instagram Followers - Coded by Rozhak-XD""", width=56, style="bold bright_black"))
    return ("Sukses")

class Kirimkan:

    def __init__(self) -> None:
        pass

    def Delay(self, menit, detik, username):
        self.total = (menit * 60 + detik)
        while (self.total):
            menit, detik = divmod(self.total, 60)
            print(f"[bold bright_black]   ╰─>[bold green] @{str(username)[:20]}[bold white]/[bold green]{menit:02d}:{detik:02d}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Gagal)}     ", end='\r')
            time.sleep(1)
            self.total -= 1
        return ("Sukses")

    def Pengguna(self):
        try:
            with requests.Session() as r:
                response = r.get('https://justpaste.it/94j00')
                self.online = re.search('"onlineText":"(\d+)"', str(response.text)).group(1)
                self.jumlah = re.search('"viewsText":"(.*?)"', str(response.text)).group(1)
            return (self.jumlah, self.online)
        except (Exception) as e:
            return (404, 404)

    def Tanya(self):
        try:
            Banner()
            print(Panel(f"[italic white]Silahkan Masukan Username Dan Password Akun Tumbal Gunakan[italic green] \"<=>\"[italic white] Sebagai Pemisah!", width=56, style="bold bright_black", subtitle="╭─────", subtitle_align="left", title=">>> Login Diperlukan <<<"))
            username_password = Console().input("[bold bright_black]   ╰─> ")
            if '<=>' in str(username_password):
                print(Panel(f"[italic white]Silahkan Masukan Username Akun Target Pastikan Akun Tidak Terkunci, Misalnya :[italic green] @rozhak_official", width=56, style="bold bright_black", subtitle="╭─────", subtitle_align="left", title=">>> Your Username <<<"))
                target_username = Console().input("[bold bright_black]   ╰─> ").replace('@', '')
                self.username, self.password = username_password.split('<=>')[0], username_password.split('<=>')[1]
                self.Count(target_username, update = True)
                print(Panel(f"[italic white]Sedang Mengirim Pengikut Anda Bisa Menggunakan[italic green] CTRL + C[italic white] Jika Stuck Dan[italic red] CTRL + Z[italic white] Jika Ingin Berhenti!", width=56, style="bold bright_black", title=">>> Catatan <<<"))
                while True:
                    Status.clear();Logging.clear()
                    for self.host_name in ['instamoda.org', 'takipcitime.com', 'takipcikrali.com']:
                        self.Submit(self.host_name, self.username, self.password, target_username)
                    if len(Logging) == 3:
                        print(Panel(f"[italic red]Username Dan Password Yang Kamu Masukan Salah Atau Akun Terkena Checkpoint!", width=56, style="bold bright_black", title=">>> Login Gagal <<<"))
                        exit()
                    else:
                        if len(Status) != 0:
                            try:
                                self.Count(target_username, update = True)
                                self.Delay(0, 300, target_username)
                                self.followers_count = (self.Count(target_username, update = False))
                            except (Exception) as e:
                                self.followers_count = ('+300')
                            print(Panel(f"""[bold white]Status :[italic green] Success in gaining followers...[/]
[bold white]Link :[bold red] https://www.instagram.com/{str(target_username)[:18]}
[bold white]Jumlah : [bold yellow]{self.followers_count}""", width=56, style="bold bright_black", title=">>> Sukses <<<"))
                            self.Delay(0, 600, target_username)
                            continue
                        else:
                            self.Delay(0, 600, target_username)
                            continue
            else:
                print(Panel(f"[italic red]Pemisah Antara Username Dan Password Tidak Benar Silahkan Lihat Di Youtube!", width=56, style="bold bright_black", title=">>> Pemisah Salah <<<"))
                exit()
        except (Exception) as e:
            print(Panel(f"[italic red]{str(e).title()}!", width=56, style="bold bright_black", title=">>> Error <<<"))
            exit()

    def Submit(self, host_name, username, password, target_username):
        with requests.Session() as r:
            try:
                r.headers.update({
                    'cache-control': 'max-age=0',
                    'accept-encoding': 'gzip, deflate',
                    'sec-fetch-mode': 'navigate',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-user': '?1',
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-site': 'none',
                    'Host': '{}'.format(host_name),
                    'sec-fetch-dest': 'document',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                    'connection': 'keep-alive',
                })
                response = r.get('https://{}/login'.format(host_name))
                try:
                    self.antiForgeryToken = re.search('"&antiForgeryToken=(.*?)";', str(response.text)).group(1)
                except (AttributeError):
                    print(f"[bold bright_black]   ╰─>[bold red] AntiForgeryToken Tidak Ditemukan...               ", end='\r')
                    time.sleep(2.5)
                    return ("AntiForgeryToken Tidak Ditemukan")
                r.headers.update({
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'sec-fetch-site': 'same-origin',
                    'referer': 'https://{}/login'.format(host_name),
                    'sec-fetch-mode': 'cors',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'sec-fetch-dest': 'empty',
                    'cookie': "; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]),
                    'origin': 'https://{}'.format(host_name),
                })
                data = {
                    'username': username,
                    'antiForgeryToken': self.antiForgeryToken,
                    'userid': '',
                    'password': password,
                }
                response2 = r.post('https://{}/login?'.format(host_name), data = data)
                if '"status":"success"' in str(response2.text):
                    r.headers.update({
                        'referer': 'https://{}/tools/send-follower'.format(host_name),
                        'cookie': "; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]),
                    })
                    data = {
                        'username': target_username,
                    }
                    response3 = r.post('https://{}/tools/send-follower?formType=findUserID'.format(host_name), data = data)
                    if 'name="userID"' in str(response3.text):
                        self.userID = re.search('name="userID" value="(\d+)">', str(response3.text)).group(1)
                        r.headers.update({
                            'cookie': "; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]),
                        })
                        data = {
                            'userName': target_username,
                            'adet': '500',
                            'userID': self.userID,
                        }
                        response4 = r.post('https://{}/tools/send-follower/{}?formType=send'.format(host_name, self.userID), data = data)
                        if '"status":"success"' in str(response4.text):
                            Sukses.append(f'{response4.text}')
                            Status.append("Sukses")
                            return ("Sukses Menukar Pengikut")
                        elif '"code":"nocreditleft"' in str(response4.text):
                            print(f"[bold bright_black]   ╰─>[bold red] Anda Kehabisan Kredit...                       ", end='\r')
                            time.sleep(2.5)
                            return ("Tidak Ada Kredit")
                        elif '"code":"nouserleft"' in str(response4.text):
                            print(f"[bold bright_black]   ╰─>[bold red] Tidak Ada Pengguna Silahkan Coba Lagi Nanti...    ", end='\r')
                            time.sleep(2.5)
                            return ("Tidak Ada Pengguna")
                        else:
                            print(f"[bold bright_black]   ╰─>[bold red] Terjadi Kesalahan Saat Mengirim Pengikut...    ", end='\r')
                            time.sleep(2.5)
                            Gagal.append(f'{response4.text}')
                            return ("Terjadi Kesalahan")
                    else:
                        print(f"[bold bright_black]   ╰─>[bold red] Tidak Ditemukan Pengguna...                       ", end='\r')
                        time.sleep(2.5)
                        return ("Tidak Ditemukan Pengguna")
                else:
                    print(f"[bold bright_black]   ╰─>[bold red] Login Gagal...                       ", end='\r')
                    time.sleep(2.5)
                    Logging.append(f'{response2.text}')
                    return ("Login Gagal")
            except (RequestException) as e:
                print(f"[bold bright_black]   ╰─>[bold red] Koneksi Error...                             ", end='\r')
                time.sleep(4.5)
                self.Submit(host_name, username, password, target_username)

    def Count(self, target_username, update):
        with requests.Session() as r:
            r.headers.update({
                'user-agent': 'Instagram 280.0.0.18.114 Android (30/11; 320dpi; 720x1448; realme; RMX3201; RMX3201; mt6765; en_US; 368008477)',
                'Host': 'i.instagram.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            })
            response = r.get('https://i.instagram.com/api/v1/users/web_profile_info/?username={}'.format(target_username))
            if '"status":"ok"' in str(response.text):
                self.edge_followed_by = json.loads(response.text)['data']['user']['edge_followed_by']['count']
                if bool(update) == True:
                    Follower.update({
                        "Count": int(self.edge_followed_by)
                    })
                    return ("Sukses")
                else:
                    self.jumlah_masuk = (int(self.edge_followed_by) - int(Follower['Count']))
                    return (f'+{self.jumlah_masuk} > {self.edge_followed_by}')
            else:
                if bool(update) == True:
                    Follower.update({
                        "Count": "999"
                    })
                    return ("Gagal")
                else:
                    return ('+300')

if __name__ == '__main__':
    try:
        Kirimkan().Pengguna()
        Kirimkan().Tanya()
    except (Exception) as e:
        print(Panel(f"[italic red]{str(e).title()}!", width=56, style="bold bright_black", title=">>> Error <<<"))
        exit()
    except (KeyboardInterrupt):
        exit()
