""" Decompiled by Exotic Hridoy """

try:
    import requests, random, uuid, time, urllib, re, os, json
    from rich.panel import Panel
    from rich import print
    from requests.exceptions import RequestException
    from rich.console import Console
except (Exception, KeyboardInterrupt) as e:
    exit(f"[Error]{str(e).capitalize()}!")

def Banner():
    os.system('cls' if os.name=='nt' else 'clear')
    print(Panel("""[bold red]●[bold yellow] ●[bold green] ●[/]
[bold red]   __  ___         __   _          __   _ __          
  /  |/  /__ _____/ /  (_)__  ___ / /  (_) /_____ ____
 / /|_/ / _ `/ __/ _ \/ / _ \/ -_) /__/ /  '_/ -_) __/
[bold white]/_/  /_/\_,_/\__/_//_/_/_//_/\__/____/_/_/\_\\__/_/  
 
      [bold white on red] Free Facebook Likes - Coded by Rozhak-XD""", width=58, style="bold bright_black"))
    return ("Sukses Memunculkan Banner")

Sukses, Gagal = [], []

class Login:

    def __init__(self) -> None:
        pass

    def Token(self, username, password):
        with requests.Session() as r:
            self.x_fb_hni = (str(random.randint(30000, 40000)))
            self.x_fb_ta_logging_ids = str(uuid.uuid4())
            self.device_id = str(uuid.uuid4())
            self.family_device_id = str(uuid.uuid4())
            r.headers.update({
                'x-fb-connection-type': 'MOBILE.LTE',
                'analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
                'connection': 'keep-alive',
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
                'x-tigon-is-retry': 'False',
                'x-fb-ta-logging-ids': 'graphql:{}'.format(self.x_fb_ta_logging_ids),
                'x-fb-privacy-context': '3643298472347298',
                'x-fb-net-hni': '{}'.format(self.x_fb_hni),
                'x-fb-server-cluster': 'True',
                'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'accept-encoding': 'gzip, deflate',
                'x-fb-client-ip': 'True',
                'x-graphql-client-library': 'graphservice',
                'x-fb-device-group': '{}'.format(str(random.randint(1000, 4000))),
                'Host': 'b-graph.facebook.com',
                'x-graphql-request-purpose': 'fetch',
                'x-fb-http-engine': 'Liger',
                'user-agent': '[FBAN/FB4A;FBAV/429.0.0.0.9;FBBV/475991488;FBDM/{density=3.0,width=1080,height=1920};FBLC/id_ID;FBRV/0;FBCR/INDOSAT;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1941;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
                'x-fb-sim-hni': '{}'.format(self.x_fb_hni),
            })
            data = (f'method=post&pretty=false&format=json&server_timestamps=true&locale=id_ID&purpose=fetch&fb_api_req_friendly_name=FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request&fb_api_caller_class=graphservice&client_doc_id=11994080429476855663503865341&variables=%7B%22params%22%3A%7B%22params%22%3A%22%7B%5C%22params%5C%22%3A%5C%22%7B%5C%5C%5C%22client_input_params%5C%5C%5C%22%3A%7B%5C%5C%5C%22device_id%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(self.device_id)}%5C%5C%5C%22%2C%5C%5C%5C%22sim_phones%5C%5C%5C%22%3A%5B%5D%2C%5C%5C%5C%22login_attempt_count%5C%5C%5C%22%3A1%2C%5C%5C%5C%22secure_family_device_id%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(str(uuid.uuid4()))}%5C%5C%5C%22%2C%5C%5C%5C%22machine_id%5C%5C%5C%22%3A%5C%5C%5C%22Zz3wZEUXl5QTtZtfca2kXYVU%5C%5C%5C%22%2C%5C%5C%5C%22accounts_list%5C%5C%5C%22%3A%5B%5D%2C%5C%5C%5C%22auth_secure_device_id%5C%5C%5C%22%3A%5C%5C%5C%22%5C%5C%5C%22%2C%5C%5C%5C%22password%5C%5C%5C%22%3A%5C%5C%5C%22%23PWD_FB4A%3A0%3A{str(int(time.time()))}%3A{urllib.request.quote(str(password))}%5C%5C%5C%22%2C%5C%5C%5C%22family_device_id%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(str(self.family_device_id))}%5C%5C%5C%22%2C%5C%5C%5C%22fb_ig_device_id%5C%5C%5C%22%3A%5B%5D%2C%5C%5C%5C%22device_emails%5C%5C%5C%22%3A%5B%5D%2C%5C%5C%5C%22try_num%5C%5C%5C%22%3A1%2C%5C%5C%5C%22event_flow%5C%5C%5C%22%3A%5C%5C%5C%22login_manual%5C%5C%5C%22%2C%5C%5C%5C%22event_step%5C%5C%5C%22%3A%5C%5C%5C%22home_page%5C%5C%5C%22%2C%5C%5C%5C%22sim_serials%5C%5C%5C%22%3A%5B%5D%2C%5C%5C%5C%22openid_tokens%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22client_known_key_hash%5C%5C%5C%22%3A%5C%5C%5C%22%5C%5C%5C%22%2C%5C%5C%5C%22contact_point%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(str(username))}%5C%5C%5C%22%2C%5C%5C%5C%22encrypted_msisdn%5C%5C%5C%22%3A%5C%5C%5C%22%5C%5C%5C%22%7D%2C%5C%5C%5C%22server_params%5C%5C%5C%22%3A%7B%5C%5C%5C%22should_trigger_override_login_2fa_action%5C%5C%5C%22%3A0%2C%5C%5C%5C%22username_text_input_id%5C%5C%5C%22%3A%5C%5C%5C%22uw4uv7%3A56%5C%5C%5C%22%2C%5C%5C%5C%22should_trigger_override_login_success_action%5C%5C%5C%22%3A0%2C%5C%5C%5C%22device_id%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(self.device_id)}%5C%5C%5C%22%2C%5C%5C%5C%22server_login_source%5C%5C%5C%22%3A%5C%5C%5C%22login%5C%5C%5C%22%2C%5C%5C%5C%22waterfall_id%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(str(uuid.uuid4()))}%5C%5C%5C%22%2C%5C%5C%5C%22login_source%5C%5C%5C%22%3A%5C%5C%5C%22Login%5C%5C%5C%22%2C%5C%5C%5C%22INTERNAL__latency_qpl_instance_id%5C%5C%5C%22%3A186795961900225%2C%5C%5C%5C%22reg_flow_source%5C%5C%5C%22%3A%5C%5C%5C%22login_home_native_integration_point%5C%5C%5C%22%2C%5C%5C%5C%22is_caa_perf_enabled%5C%5C%5C%22%3A1%2C%5C%5C%5C%22is_platform_login%5C%5C%5C%22%3A0%2C%5C%5C%5C%22credential_type%5C%5C%5C%22%3A%5C%5C%5C%22password%5C%5C%5C%22%2C%5C%5C%5C%22pw_encryption_try_count%5C%5C%5C%22%3A1%2C%5C%5C%5C%22caller%5C%5C%5C%22%3A%5C%5C%5C%22gslr%5C%5C%5C%22%2C%5C%5C%5C%22INTERNAL__latency_qpl_marker_id%5C%5C%5C%22%3A36707139%2C%5C%5C%5C%22family_device_id%5C%5C%5C%22%3A%5C%5C%5C%22{urllib.request.quote(str(self.family_device_id))}%5C%5C%5C%22%2C%5C%5C%5C%22offline_experiment_group%5C%5C%5C%22%3A%5C%5C%5C%22caa_iteration_v6_perf_fb_2%5C%5C%5C%22%2C%5C%5C%5C%22INTERNAL_INFRA_THEME%5C%5C%5C%22%3A%5C%5C%5C%22harm_f%5C%5C%5C%22%2C%5C%5C%5C%22password_text_input_id%5C%5C%5C%22%3A%5C%5C%5C%22uw4uv7%3A57%5C%5C%5C%22%2C%5C%5C%5C%22ar_event_source%5C%5C%5C%22%3A%5C%5C%5C%22login_home_page%5C%5C%5C%22%7D%7D%5C%22%7D%22%2C%22bloks_versioning_id%22%3A%22b40360fc842962f2f20ae862b9e33d66b5e55ab09792c32e443420306f864be6%22%2C%22app_id%22%3A%22com.bloks.www.bloks.caa.login.async.send_login_request%22%7D%2C%22scale%22%3A%222%22%2C%22nt_context%22%3A%7B%22using_white_navbar%22%3Atrue%2C%22pixel_ratio%22%3A2%2C%22is_push_on%22%3Atrue%2C%22styles_id%22%3A%22b5bbf1cf43ecf97d36d17b628ba4fc34%22%2C%22bloks_version%22%3A%22b40360fc842962f2f20ae862b9e33d66b5e55ab09792c32e443420306f864be6%22%7D%7D&\
                    fb_api_analytics_tags=%5B%22GraphServices%22%5D&client_trace_id={urllib.request.quote(self.x_fb_ta_logging_ids)}')
            response = r.post('https://b-graph.facebook.com/graphql', data=data, allow_redirects=True)
            if '"access_token":"' in str(response.text.replace('\\', '')) or '"session_key":"' in str(response.text.replace('\\', '')):
                self.access_token = re.search('"access_token":"(.*?)"', str(response.text.replace('\\', ''))).group(1)
                self.user_ids = re.search('"uid":(\d+),', str(response.text.replace('\\', ''))).group(1)
                self.session_key = re.search('"session_key":"(.*?)"', str(response.text.replace('\\', ''))).group(1)
                return (self.access_token, self.user_ids, self.session_key)
            elif 'https://www.facebook.com/checkpoint/' in str(response.text.replace('\\', '')) or 'User must verify their account on' in str(response.text):
                print(Panel(f"[italic red]Akun Facebook Kamu Terkena Checkpoint Atau Terkunci!", width=58, style="bold bright_black", title=">>> Login Checkpoint <<<"))
                exit()
            else:
                print(Panel(f"[italic red]Password Yang Kamu Salah Atau Akun Checkpoint Silahkan Hidupkan Mode Pesawat Lalu Login Ulang!", width=58, style="bold bright_black", title=">>> Terkena Spam <<<"))
                exit()

class Submit:

    def __init__(self) -> None:
        pass

    def Pengguna(self):
        try:
            with requests.Session() as r:
                response = r.get('https://justpaste.it/c1n7s')
                self.online = re.search('"onlineText":"(\d+)"', str(response.text)).group(1)
                self.jumlah = re.search('"viewsText":"(.*?)"', str(response.text)).group(1)
            return (self.jumlah, self.online)
        except (Exception) as e:
            return (404, 404)

    def Your_Account(self):
        try:
            Banner()
            print(Panel(f"[italic white]Silahkan Masukan Username Dan Password Akun Facebook Tumbal, Gunakan \"[italic red]<=>[italic white]\" Sebagai Pemisah!", width=58, style="bold bright_black", title=">>> Username & Password <<<", subtitle="╭──────", subtitle_align="left"))
            your_account = Console().input("[bold bright_black]   ╰─> ")
            if '<=>' in str(your_account):
                self.username, self.password = your_account.split('<=>')[0], your_account.split('<=>')[1]
                self.access_token, self.user_ids, self.session_key = Login().Token(self.username, self.password)
                print(Panel(f"[italic white]Silahkan Masukan Link Postingan Facebook, Misalnya :[italic green] https://m.facebook.com/story.php?story_fbid=pfbid0F6KrzQC1QsdqnmCde9trcDt3s7CqPpENPq6uNAPpnDhHP8xwyT1Baa8HRGNthPXol&id=100006609458697&mibextid=2JQ9oc", width=58, style="bold bright_black", title=">>> Link Postingan <<<", subtitle="╭──────", subtitle_align="left"))
                your_post = Console().input("[bold bright_black]   ╰─> ")
                if 'mibextid=' in str(your_post):
                    print(Panel(f"[italic white]Sedang Mengirim Likes Kamu Bisa Menggunakan[italic red] CTRL + Z[italic white] Untuk Berhenti Dan[italic green] CTRL + C[italic white] Jika Stuck!", width=58, style="bold bright_black", title=">>> Catatan <<<"))
                    while True:
                        try:
                            self.Likes(self.access_token, self.user_ids, self.session_key, your_post)
                        except (RequestException):
                            print("\r                                                    ", end='\r')
                            time.sleep(1.5)
                            print(f"[bold bright_black]   ╰─>[bold red] KONEKSI ERROR!", end='\r')
                            time.sleep(7.5)
                            continue
                        except (KeyboardInterrupt):
                            print("\r                                                    ", end='\r')
                            time.sleep(2.5)
                            continue
                        except (Exception) as e:
                            print("\r                                                    ", end='\r')
                            time.sleep(1.5)
                            print(f"[bold bright_black]   ╰─>[bold red] {str(e).upper()}!", end='\r')
                            time.sleep(3.5)
                            continue
                else:
                    print(Panel(f"[italic red]Link Yang Kamu Masukan Salah Silahkan Untuk Mengambil Link Postingan Di Aplikasi Facebook!", width=58, style="bold bright_black", title=">>> Link Salah <<<"))
                    exit()
            else:
                print(Panel(f"[italic red]Pemisah Anatara Username Dan Password Yang Kamu Masukan Salah!", width=58, style="bold bright_black", title=">>> Pemisah Salah <<<"))
                exit()
        except (Exception) as e:
            print(Panel(f"[italic red]{str(e).title()}!", width=58, style="bold bright_black", title=">>> Error <<<"))
            exit()

    def Likes(self, access_token, user_id, session_key, your_post):
        global Sukses, Gagal
        with requests.Session() as r:
            r.headers.update({
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'Referer': 'https://machine-likers.com/autoliker.php',
                'Upgrade-Insecure-Requests': '1',
                'Connection': 'keep-alive',
                'Origin': 'https://machine-likers.com',
                'Cache-Control': 'max-age=0',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Host': 'machine-likers.com',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-User': '?1',
                'Accept-Language': 'en-US,en;q=0.9',
                'Sec-Fetch-Dest': 'document',
                'Cookie': f'access_token={access_token}; user_id={user_id}; session_key={session_key};',
            })
            data = ({
                'token': access_token,
                'id': your_post,
            })
            response = r.post('https://machine-likers.com/autoliker.php', data=data)
            if 'LIKE FAILED!' in str(response.text) and 'Please Wait' in str(response.text):
                print(f"[bold bright_black]   ╰─>[bold red] SILAHKAN TUNGGU 30 MENIT!", end='\r')
                time.sleep(2.5)
                self.Delay(0, 1800, user_id)
                return ("Delay Telah Selesai")
            elif 'Likes Sent Successfully.' in str(response.text):
                self.story_fbid = (your_post.split('facebook.com/')[1])
                print(Panel(f"""[bold white]Status :[italic green] Likes Sent Successfully...[/]
[bold white]Link :[bold red] https://m.facebook.com/\n{self.story_fbid}
[bold white]Jumlah :[bold yellow] -+ 30[bold white] *[italic green]Sedang diproses[/]""", width=58, style="bold bright_black", title=">>> Sukses <<<"))
                Sukses.append(f'{response.text}')
                return ("Berhasil Mendapatkan Likes")
            else:
                print(f"[bold bright_black]   ╰─>[bold red] GAGAL MENGIRIM LIKES!", end='\r')
                time.sleep(3.5)
                Gagal.append(f'{response.text}')
                return ("Gagal Mengirim Likes")

    def Delay(self, menit, detik, user_ids):
        global Sukses, Gagal
        self.total = (menit * 60 + detik)
        while (self.total):
            menit, detik = divmod(self.total, 60)
            print(f"[bold bright_black]   ╰─>[bold green] {str(user_ids)[:20]}[bold white]/[bold green]{menit:02d}:{detik:02d}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Gagal)}     ", end='\r')
            time.sleep(1)
            self.total -= 1
        return ("Sukses")

if __name__=='__main__':
    try:
        Submit().Your_Account()
    except (Exception) as e:
        print(Panel(f"[italic red]{str(e).title()}!", width=58, style="bold bright_black", title=">>> Error <<<"))
        exit()
    except (KeyboardInterrupt):
        exit()
