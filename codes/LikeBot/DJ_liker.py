#!/data/data/com.termux/files/usr/bin/python3.11
# -*- coding: utf-8 -*-

try:
    from requests.exceptions import RequestException
    from rich.console import Console
    import requests, re, time, os, json
    from rich.panel import Panel
    from rich import print as printf
except (ModuleNotFoundError) as e:
    exit(f"[Error] {str(e).capitalize()}!")

GAGAL, COOKIES, SUKSES, JUMLAH = [], {
    "DJ-LIKER": "null"
}, [], 0

class DJ_LIKER:

    def __init__(self) -> None:
        pass

    def DELAY(self, times):
        global SUKSES, GAGAL, JUMLAH
        for sleep in range(int(times), 0, -1):
            time.sleep(1.0)
            printf(f"[bold bright_white]   --->[bold white] RUNNING[bold green] {sleep}[bold white]/[bold green]{JUMLAH}[bold white] SUKSES :[bold yellow] {len(SUKSES)}[bold white] GAGAL :[bold red] {len(GAGAL)}[bold white]     ", end='\r')
        return ("0_0")

    def SEND_REACTION(self, link_postingan, type_reaction):
        global SUKSES, GAGAL, JUMLAH
        with requests.Session() as r:
            r.headers.update({
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7",
                "Connection": "keep-alive",
                "Cookie": "{}".format(COOKIES['DJ-LIKER']),
                "Host": "dj.yogram.net",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
            })
            response = r.get('https://dj.yogram.net/autolike.php?type=custom')
            if '/index.php?error=Login' in str(response.text):
                printf(f"[bold bright_white]   --->[bold red] COOKIES EXPIRED, TRY RELOGIN!             ", end='\r')
                time.sleep(2.0)
                return ("-_-")
            elif 'Time Limit Reached!' in str(response.text):
                printf(f"[bold bright_white]   --->[bold yellow] TIME LIMIT REACHED, TRY AGAIN!             ", end='\r')
                self.DELAY(900)
                return ("0_0")
            else:
                self.form_control = re.search(r'class="form-control"\s+.*?\s+name="(.*?)"', str(response.text)).group(1)
                self.djkey = re.search(r'type="hidden" name="([^"]+)"[^>]*value="([^"]+)"', str(response.text))
                self.key, self.value = self.djkey.group(1), self.djkey.group(2)
                self.type_submit = re.search(r'type="submit"[^>]*name="([^"]+)"', str(response.text)).group(1)
                self.sitekey = re.search('data-sitekey="(.*?)"', str(response.text)).group(1)

                data = {
                    f'{self.form_control}': f'{link_postingan}',
                    f'{self.key}': f'{self.value}',
                    'type': 'LOVE', #
                    'g-recaptcha-response': f'{BYPASS().reCAPTCHA(sitekey=self.sitekey)}',
                    f'{self.type_submit}': 'Submit',
                }

                r.headers.update({
                    "Referer": "https://dj.yogram.net/autolike.php?type=custom",
                    "Cache-Control": "max-age=0",
                    "Connection": "keep-alive",
                    "Content-Length": "{}".format(str(len(data))),
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Origin": "https://dj.yogram.net",
                    "Sec-Fetch-Site": "same-origin",
                })
                response2 = r.post('https://dj.yogram.net/autolike.php?type=custom', data=data)
                JUMLAH += 1
                if 'https://dj.yogram.net/?i=' in str(response2.url):
                    try:
                        self.jumlah = re.search('/?i=([0-9]+)', str(response2.url)).group(1)
                    except:
                        self.jumlah = (20)
                    printf(f"[bold bright_white]   --->[bold green] SUCCESSFULLY SENDING REACTION!        ", end='\r')
                    time.sleep(1.5)
                    printf(Panel(f"""[bold white]Status :[bold green] Likes are being processed...[/]
[bold white]Conclusion :[bold purple] +{self.jumlah}[bold white] >[bold purple] {str(type_reaction).upper()}""", width=59, style="bold bright_white", title="[Success]"))
                    SUKSES.append('{}'.format(response2.url))
                    return ("0_0")
                elif 'https://dj.yogram.net/?error=Invalid%20Captcha,%20Please%20Try%20Again' in str(response2.url):
                    printf(f"[bold bright_white]   --->[bold red] YOUR CAPTCHA IS WRONG!                ", end='\r')
                    time.sleep(3.5)
                    return ("-_-")
                elif 'https://dj.yogram.net/?error=Invalid%20URL%20or%20Post%20not%20Public,%20Try%20Again' in str(response2.url):
                    printf(f"[bold bright_white]   --->[bold red] POST LINKS ARE NOT PUBLIC!                ", end='\r')
                    time.sleep(3.5)
                    return ("-_-")
                else:
                    printf(f"[bold bright_white]   --->[bold red] FAILED TO SEND REACTION!              ", end='\r')
                    time.sleep(3.5)
                    GAGAL.append('{}'.format(response2.url))
                    return ("-_-")

    def LOGIN_COOKIES(self):
        try:
            TAMPILKAN_BANNER()
            printf(Panel(f"[italic white]Please fill in your Facebook cookies, please use a fake account to log in. If you experience\nproblems, try logging into the application first!", width=59, style="bold bright_white", title="[Login Cookies]", subtitle="╭──────", subtitle_align="left"))
            self.YOUR_COOKIES = Console().input("[bold bright_white]   ╰─> ")
            if 'c_user=' in str(self.YOUR_COOKIES) or 'xs=' in str(self.YOUR_COOKIES):
                self.VALIDASI_LOGIN(self.YOUR_COOKIES)
                printf(Panel(f"[italic white]Please fill in the link for your post, make sure the link can be liked and the account is not private!", width=59, style="bold bright_white", title="[Post Link]", subtitle="╭──────", subtitle_align="left"))
                self.LINK = Console().input("[bold bright_white]   ╰─> ")
                printf(Panel(f"[italic white]Please enter the reaction type of your post", width=59, style="bold bright_white", title="[Reaction Type]", subtitle="╭──────", subtitle_align="left"))
                self.REACTION = Console().input("[bold bright_white]   ╰─> ")
                if str(self.REACTION) in ["LIKE","LOVE","CARE","HAHA","WOW","SAD","ANGRY"]:
                    printf(Panel(f"[italic white]You can use[italic green] CTRL + C[italic white] if stuck and[italic red] CTRL + Z[italic white] if you want to stop. You have to change\nthe key to be able to bypass the captcha!", width=59, style="bold bright_white", title="[Notes]"))
                    while True:
                        try:
                            if str(COOKIES["DJ-LIKER"]) == 'null':
                                printf(f"[bold bright_white]   --->[bold red] COOKIES EXPIRED, TRY RELOGIN!             ", end='\r')
                                time.sleep(2.0)
                                self.VALIDASI_LOGIN(self.YOUR_COOKIES)
                                continue
                            else:
                                self.SEND_REACTION(self.LINK, self.REACTION)
                                continue
                        except (KeyboardInterrupt):
                            printf(f"                                    ", end='\r')
                            time.sleep(1.5)
                            continue
                        except (RequestException):
                            printf(f"[bold bright_white]   --->[bold red] COOKIES EXPIRED, TRY RELOGIN!             ", end='\r')
                            time.sleep(9.5)
                            continue
                        except (Exception) as e:
                            printf(f"[bold bright_white]   --->[bold red] {str(e).upper()}!", end='\r')
                            time.sleep(2.5)
                            continue
                else:
                    printf(Panel(f"[italic red]You must fill in the reaction type correctly, choose one, not all of them!", width=59, style="bold bright_white", title="[Wrong Reaction]"))
                    exit()
            else:
                printf(Panel(f"[italic red]Please enter Facebook cookies correctly, you can see YouTube for how to use this program!", width=59, style="bold bright_white", title="[Wrong Cookies]"))
                exit()
        except (Exception) as e:
            printf(Panel(f"[italic red]{str(e).capitalize()}", width=59, style="bold bright_white", title="[Error]"))
            exit()

    def VALIDASI_LOGIN(self, cookies):
        with requests.Session() as r:
            r.headers.update({
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7",
                "Connection": "keep-alive",
                "Host": "dj.yogram.net",
                "Sec-Fetch-Dest": "document",
                "X-Requested-With": "djliker.app",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
            })
            response = r.get('https://dj.yogram.net/')
            params = {
                "device_name": "SM-S908U",
                "cookie": cookies,
                "token": "",
                "manufacturer": "SAMSUNG",
            }
            r.headers.update({
                "Cookie": "{}".format("; ".join([str(x) + "=" + str(y) for x, y in r.cookies.get_dict().items()])),
                "v": "3.1" #
            })
            response2 = r.get('https://dj.yogram.net/login.php', params=params)
            if 'https://dj.yogram.net/update.php?error=' in str(response2.url):
                printf(Panel(f"[italic red]This application requires an update, please change the version header of this program to the latest version!", width=59, style="bold bright_white", title="[Invalid Version]"))
                exit()
            elif 'https://dj.yogram.net/?i=Welcome' in str(response2.url):
                COOKIES.update({
                    "DJ-LIKER": "; ".join([str(x) + "=" + str(y) for x, y in r.cookies.get_dict().items()])
                })
                return ("0_0")
            else:
                printf(Panel(f"[italic red]Failed when logging in, maybe your cookies are invalid or your Facebook account\nhas been checkpointed, take cookies again!", width=59, style="bold bright_white", title="[Expired Cookies]"))
                exit()

def TAMPILKAN_BANNER():
    os.system('cls' if os.name == 'nt' else 'clear')
    printf(Panel("""[bold white]       facebook reactions scrapper api based   """, width=59, style="bold bright_white"))

class BYPASS:

    def __init__(self) -> None:
        pass

    def reCAPTCHA(self, sitekey):
        with requests.Session() as r:
            self.key = "b3lXFanWM7fhcoBREHkLjQtVxK1N6SO8"
            response = r.get(f'http://api.multibot.in/in.php?key={self.key}&method=userrecaptcha&googlekey={sitekey}&pageurl=https://dj.yogram.net/autolike.php?type=custom')
            self.status, self.id = str(response.text).split('|')[0], str(response.text).split('|')[1]
            if 'OK' in str(response.text):
                while True:
                    response2 = requests.get(f'http://api.multibot.in/res.php?key={self.key}&id={self.id}')
                    if 'OK|' in str(response2.text):
                        printf(f"[bold bright_white]   --->[bold green] SUCCESSFULLY BYPASS CAPTCHA!             ", end='\r')
                        time.sleep(1.5)
                        return (str(response2.text).split('|')[1])
                    elif 'CAPCHA_NOT_READY' in str(response2.text):
                        for sleep in range(60, 0, -1):
                            time.sleep(1.0)
                            printf(f"[bold bright_white]   --->[bold white] Bypassing[bold green] {sleep}[bold white] wait ...                           ", end='\r')
                        continue
                    else:
                        printf(f"[bold bright_white]   --->[bold yellow] TRY BYPASS CAPTCHA!                  ", end='\r')
                        time.sleep(1.5)
                        self.reCAPTCHA(sitekey)
            else:
                printf(f"[bold bright_white]   --->[bold red] CAPTCHA NOT FOUND!                  ", end='\r')
                time.sleep(3.5)
                self.reCAPTCHA(sitekey)

if __name__ == '__main__':
    try:
        DJ_LIKER().LOGIN_COOKIES()
    except (Exception) as e:
        printf(Panel(f"[italic red]{str(e).capitalize()}", width=59, style="bold bright_white", title="[Error]"))
        exit()
    except (KeyboardInterrupt):
        exit()
