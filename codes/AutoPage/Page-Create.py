""" Published by Exotic Hridoy """

import os,sys,time,datetime,random,json,re
import requests
import rich
import bs4
import names
import colorama
from rich import print
from rich.console import Console
from rich.panel import Panel as panel
from rich.columns import Columns as colum
from bs4 import BeautifulSoup as bs
from time import sleep,strftime
from concurrent.futures import ThreadPoolExecutor

def clear():os.system('cls' if os.name in ['nt'] else 'clear')
input = Console().input
city_id = '962001'
cate = {"categories":["1602","1114","302743949101359"]}
DefaultUAWindows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
HeadersGet  = lambda i=DefaultUAWindows : {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-True-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':i,'Viewport-Width':'924'}
HeadersPost = lambda i=DefaultUAWindows : {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':i}

def GetData(req):
    av = re.search('"actorID":"(.*?)"', str(req)).group(1)
    __user = av
    __a = str(random.randrange(1, 6))
    __hs = re.search('"haste_session":"(.*?)"', str(req)).group(1)
    dpr = '1.5'
    __ccg = re.search('"connectionClass":"(.*?)"', str(req)).group(1)
    __rev = re.search('"__spin_r":(.*?),', str(req)).group(1)
    __spin_r = __rev
    __spin_b = re.search('"__spin_b":"(.*?)"', str(req)).group(1)
    __spin_t = re.search('"__spin_t":(.*?),', str(req)).group(1)
    __hsi = re.search('"hsi":"(.*?)"', str(req)).group(1)
    __comet_req = '15'
    fb_dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}', str(req)).group(1)
    jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
    lsd = re.search('"LSD",\[\],{"token":"(.*?)"}', str(req)).group(1)
    Data = {'av': av, '__user': __user, '__a': __a, '__hs': __hs, 'dpr': dpr, '__ccg': __ccg, '__rev': __rev, '__spin_r': __spin_r, '__spin_b': __spin_b, '__spin_t': __spin_t, '__hsi': __hsi, '__comet_req': __comet_req, 'fb_dtsg': fb_dtsg, 'jazoest': jazoest, 'lsd': lsd}
    return Data

def Baner():
    clear()

class LoginCookie:

    def __init__(self):
        Baner()
        self.r______ = requests.Session()
        Console(width=70).print(panel('Masukan Cookie Akun Facebook',width=70,style='bold white',subtitle='┌─',subtitle_align='left'),justify='center')
        self.Cookie = input('   └─> ')
        self.Main()
        Menu()

    def Main(self):
        UserName,UserID = GetUserInfo(self.Cookie)
        open("Data/Cookie.txt",'w').write(self.Cookie)
        Console(width=70).print(panel(f'[bold green]{UserName}',width=70,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Anda Login Ke Facebook Sebagai [bold cyan]<[bold green]<[bold yellow]<'),justify='center')
        self.language()

    def language(self):
        try:
            with requests.Session() as r:
                r.cookies.update({'cookie':self.Cookie})
                req = r.get('https://www.facebook.com/profile.php',headers=HeadersGet(),allow_redirects=True).text
                Data = GetData(req)
                Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useCometLocaleSelectorLanguageChangeMutation','variables': json.dumps({"locale":"id_ID","referrer":"WWW_COMET_ACCOUNT_SETTINGS","fallback_locale":None}),'server_timestamps':True,'doc_id':'6451777188273168'})
                r.post('https://www.facebook.com/api/graphql/',data=Data,headers=HeadersPost()).json()
        except Exception:pass

def GetUserInfo(Cookie):
    try:
        with requests.Session() as r:
            r.cookies.update({'cookie':Cookie})
            response = bs(r.get('https://www.facebook.com/profile.php', headers=HeadersGet(),allow_redirects=True).text,'html.parser')
            UserID = re.search('"actorID":"(.*?)"',str(response)).group(1)
            UserName = re.search('"NAME":"(.*?)"',str(response)).group(1)
            return UserName,UserID
    except Exception as e:
        Console(width=70).print(panel('[bold red]Cookie Invalid',width=70,style='bold white'),justify='center');sleep(2);LoginCookie()
        sleep(2)
        LoginCookie()

def Menu():
    Baner()
    try:
        Cookie = open('Data/Cookie.txt', 'r', encoding='utf-8').read()
        name, id = GetUserInfo(Cookie)
        DumpPanel = []
        DumpPanel.clear()
        DumpPanel.append(panel("""[bold blue]Author : [bold white]%s\n[bold blue]Status : [bold white]%s"""%("Exotic Hridoy",'source'),width=34))
        DumpPanel.append(panel("""[bold blue]User Name : [bold white]%s\n[bold blue]User ID   : [bold white]%s"""%(name,id),width=35))
        Console(width=70).print(colum(DumpPanel),justify='center')
    except Exception as e:Console(width=70,style='bold white').print(panel(f'[bold red]Cookie Expired Silahkan Masukan Cookie Baru !',width=70,title=f'[bold red]>[bold yellow]>[bold green]>[bold red]Expired[bold green]<[bold yellow]<[bold red]<'),justify='center');sleep(3);LoginCookie()
    Console(width=70).print(panel(f'''[bold green][[bold white]01[bold green]].[bold white]Create New Page
[bold green][[bold white]02[bold green]].[bold white]Update Main Page
[bold green][[bold white]03[bold green]].[bold white]Create Store Page
[bold green][[bold white]04[bold green]].[bold white]Bot Menu
[bold green][[bold white]05[bold green]].[bold red]Logout''',width=70,style='bold white',subtitle='┌',subtitle_align='left'))
    choice = input('   └─> ')
    if choice in ('1','01'):
        CreateNewPage()
    elif choice in ('2','02'):
        UpdateMainPage()
    elif choice in ('3','03'):
        CreateNewPageStore()
    elif choice in ('4','04'):
        BotMenu()
    elif choice in ('5','05'):
        open("Data/Cookie.txt",'w')
        sleep(1)
        Console(width=70).print(panel('[bold green]Succes Logout',width=70,style='bold white'),justify='center')
        sleep(2)
        LoginCookie()

class CreateNewPage:
    def __init__(self):
        self.Cookie = open("Data/Cookie.txt",'r',encoding='utf-8').read()
        with requests.Session() as self.r:
            self.r.cookies.update({'cookie':self.Cookie})
            Console(width=70).print(panel('Masukan Nama Halaman, Pastikan Anda Tidak Memiliki Halaman Yang Bernama Sama.',width=70,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
            self.NewPageName = input('   └─> ')
            self.RegisterPage()
    def RegisterPage(self):
        response = bs(self.r.get("https://www.facebook.com/pages",headers=HeadersGet(),allow_redirects=True).content,'html.parser')
        Data = GetData(response)
        Variable = {
            "input":{
                    "bio":"Hello World",
                    "categories":["1109"],
                    "creation_source":"comet",
                    "name":self.NewPageName,
                    "page_referrer":"launch_point",
                    "actor_id":Data['__user'],
                    "client_mutation_id":"5"
                }
            }
        Data.update({
            '__dyn':'7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwhUKbgS3qi7UK361twYwJyE24xZ38C1twUx60GE3Qwb-q7oc81xoswIK1Rwwwg8a8465o-cwfG12wOx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzE8FU5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUaU3qxWm2CVEbUGdG1Fwh888cA0z8c84q58jyUaUcojxK2B0oobo8oC1hxB0qo4e16wWwjHDzUiw',
            '__csr':'gcAv3BRcyOsAesh6n_sJRitMzbbsybFdlsZ_NilsjmN6OZQpBbiy2_cm88JpLhAA_jRAy94HjnpaAuaTiBQKbAmmEzWAqyemqibmhLB8hebVd3-idmcGheFqgTByo8ucyC-8zUGXHGjCABwDABz8J1tam8-fxzy9p6mKax6EjBykAEgWGaBWxaha4qxOezoG8xe5E421gyoFe5o5Cexqbxmex2E2gyk1Jw8K1XwoEy1twl86O0ry0i2260aOCz8bobE5a0iS16w2MU0GS2W5o8U04Oq00-UQ1gg2Sw2h404fo21w7pg0Ce0vmu0nW3G01gyw0nyo9U5y8yFE620JU',
            '__req':'2v',
            '__s':'08ch3s:nuppxz:fxabbj',
            '__aaid':'0',
            'fb_api_caller_class':'RelayModern',
            'fb_api_req_friendly_name':'AdditionalProfilePlusCreationMutation',
            'variables':json.dumps(Variable),
            'server_timestamps':'True',
            'doc_id':'5296879960418435',
            "fb_api_analytics_tags":'["qpl_active_flow_ids=431626709"]'
        })
        response = self.r.post('https://www.facebook.com/api/graphql/',headers=HeadersPost(),allow_redirects=True,data=Data)
        if '"additional_profile_plus_create"' in response.text:
            if '"Anda baru-baru ini membuat terlalu banyak Halaman. Coba lagi nanti."' in response.text or '"Tidak bisa membuat Halaman: Anda sudah membuat terlalu banyak Halaman dalam waktu singkat. Coba lagi nanti."' in response.text:
                Console(width=70,style='bold white').print(panel(f'''Anda baru-baru ini membuat terlalu banyak Halaman. Coba lagi nanti.''',width=70,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]GAGAL CREATE PAGE [bold cyan]<[bold green]<[bold yellow]<'),justify='center')
                input('   └─> ');Menu()
            elif '"Tampaknya Anda sudah mengelola Halaman yang bernama %s. Pilih nama lainnya."'%(self.NewPageName) in response.text:
                Console(width=70,style='bold white').print(panel('''Tampaknya Anda sudah mengelola Halaman yang bernama %s. Pilih nama lainnya."'''%(self.NewPageName),width=70,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]GAGAL CREATE PAGE [bold cyan]<[bold green]<[bold yellow]<'),justify='center')
                input('   └─> ');Menu()
            else:
                id = response.json()['data']['additional_profile_plus_create']['additional_profile']['id']
                Console(width=70,style='bold white').print(panel(f'''Name : {self.NewPageName}   ID : {id}''',width=70,title='[bold yellow]>[bold green]>[bold cyan]> [bold white]SUCCESS CREATE PAGE [bold cyan]<[bold green]<[bold yellow]<'),justify='center')

class UpdateMainPage:
    def __init__(self):
        pass
    def DaftarkanHalamanUtama(self):
        URL = "https://business.facebook.com/pages/locations/whitelist/"
        Data = {
            "page_id":"109012538724701",
            "remove_address_only":False,
            "__usid":"6-Ts7vmuv52pwt:Ps7x4s718yr7zh:0-As7x4sqa02e5m-RV=6:F=",
            "__user":100088731637139,
            "__a":1,
            "__req":"j",
            "__hs":"19749.BP:DEFAULT.2.0..0.0",
            "dpr":"1",
            "__ccg":"GOOD",
            "__rev":1011065439,
            "__s":"f8bvby:qo2y5v:lcwusf",
            "__hsi":7328743589215563355,
            "__dyn":"7xeUmxa2C5rgydwCwRyU8EKmhG5UkBwCwgE98nCG6UmCyE8o88rxebzEdF8iBxa7GzU5S2WdwJzUmwq8gwqoqyoyazoO4o2vwOxa7FEd89EmwoU9FE4Wqmm2ZedwLBGEpg9BDwRyXxK261UxO4UkK6oW5oeE9oeUa8465udz87G5Ufo4-cg469DxW10BxO3Fe6rwnVUao9k2B2V8W18wRwEwiUmwoErorx2aK2a4p8y26U8U-UbE4S7VEjCx6221cwjV8rxefzobEaUiwm8Wubwk8Su6EfEO32fxiFVoa9obGwgUy1kx6bCyVUCfxq69EHyU8U3yDwbm1Lx3wlFbwCwiUWqU9E5C1dxW6U98a85O0FU",
            "__csr":"",
            "fb_dtsg":"NAcMpLN2d9qjg1rNzhlBLf3TXNl3b01h1tLrBiucJnX_pZi21bgzzBw:25:1706350929",
            "jazoest":25578,
            "lsd":"EaUD9q0EbuMOx5dvhjfTbV",
            "__aaid":0,
            "__bid":553448549653184,
            "__spin_r":1011065439,
            "__spin_b":"trunk",
            "__spin_t":1706356087,
            "__jssesw":1,
            "qpl_active_flow_ids":270206296,
        }

class CreateNewPageStore:

    def __init__(self):
        self.Cookie = open("Data/Cookie.txt",'r',encoding='utf-8').read()
        self._User = re.search('c_user=(.*?);',self.Cookie).group(1)
        self.PageID = []
        self.PageInfo = {}
        self.InputInfo = {}
        self.StoreData = {}
        self.GraphQlUrl = 'https://www.facebook.com/api/graphql'
        self.BussinesUrl = 'https://business.facebook.com/business_locations/?page_id='
        with requests.Session() as self.r:self.r.cookies.update({'cookie':self.Cookie})
        self.GetPageID()

        Eksekusi = "\n".join([f"[bold green][[bold white]{Count+1}[bold green]].[bold white]{self.InputInfo[Count+1]} [bold green]([bold yellow]{self.PageInfo[self.InputInfo[Count+1]]}[bold green]) [bold green]([bold white]{(self.GetCountStore(self.InputInfo[Count+1]) if self.GetCountStore(self.InputInfo[Count+1]) < 100 else '[bold red]0')}\n    {Info}" for Count in range(int(len(self.PageID)))])


        Console(width=70).print(panel(Eksekusi,width=70,style='bold white',subtitle='┌',subtitle_align='left'))
        ChoiceInput = input('   └─> ').split(',')
        with ThreadPoolExecutor(max_workers=35) as (V):
            for Choice in ChoiceInput:
                if int(Choice) < 10:
                    Choice = Choice.replace('0','')
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                else:
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()

    def GetPageID(self):
        response = bs(self.r.get('https://www.facebook.com/pages',headers=HeadersGet(),allow_redirects=True).content,'html.parser')
        Data = GetData(response)
        Variable = {"showUpdatedLaunchpointRedesign":True,"useAdminedPagesForActingAccount":False,"useNewPagesYouManage":True}
        Data.update({'variables': json.dumps(Variable),'doc_id': '5300338636681652'})
        response2 = self.r.post(self.GraphQlUrl,data=Data)
        Count = 0
        for Data in response2.json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']:
            Count+=1
            IDPage = Data['profile']['delegate_page_id']
            NamePage = Data['profile']['name']
            self.PageID.append(IDPage)
            self.InputInfo.update({"%s"%(Count):IDPage})
            self.PageInfo.update({"%s"%(IDPage):NamePage})

    def GetCountStore(self,Page_ID):
        response = bs(self.r.get(self.BussinesUrl+Page_ID,headers=HeadersGet(),allow_redirects=True).content,'html.parser')
        fb_dtsg_ag = re.search('"DTSGInitialData",\[\],{"token":".*?","async_get_token":"(.*?)"}', str(response)).group(1).replace(":",'%3A')
        NextResponse = self.r.get(f"https://business.facebook.com/ads/location-manager-filter-locations/?page_id={Page_ID}&limit=50&sort_column=store_number&sort_order=descending&fb_dtsg_ag={fb_dtsg_ag}&__user={self._User}&__hsi=7328444763778866303&__a=1&__req=s",headers=HeadersGet(),allow_redirects=True).text
        try:
            LID = re.search('"lid":"(.*?)"',NextResponse)[1]
            DataR = NextResponse.replace('for (;;);{"__ar":1,"payload":','').replace(',"lid":"%s"}'%(LID),'')
            Data = {f"{Page_ID}":{"StoreID":json.loads(DataR)['pageIDs'],"Count":json.loads(DataR)['estimatedCount']}}
            self.StoreData.update(Data)
            return(Data[Page_ID]['Count'])
        except:
            return(0)

    def Reason(self,PageID):
        response = bs(self.r.get(self.BussinesUrl+PageID).content,'html.parser')
        fb_dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}', str(response)).group(1)
        lsd = re.search('"LSD",\[\],{"token":"(.*?)"}', str(response)).group(1)
        Alasan = []
        Data = {
            "__usid": "6-Ts80ojk1wg8gry:Ps80pdoxpdchn:0-As80oglrjm0ia-RV=6:F=",
            "__user": self._User,
            "__a": "1",
            "__req": "s",
            "__hs": "19751.BP:DEFAULT.2.0..0.0",
            "dpr": "1",
            "__ccg": "GOOD",
            "__rev": "1011074526",
            "__s": "sretb0:k6d3ie:pl5h3d",
            "__hsi": "7329459393437049555",
            "__dyn": "7xe6EiwFxmUCdwn8K2abBAqxu59o6C2i5VGxK5FEG26226UjyUW3qi4FoixWE-1twKwXzUmwuo6C6EC4UScx60DUcEixWq3i2q5E6e2qq1eCBBwLjzobVqG6k2pofoKUfo7y78abxCexm3G2m3K2y11xmfw8u5Ufo4-cg469DxW10BxO3Gi6rwnVU4Z0Fz98W1-wEwiUmwoErorx2aK2a4p8y26UcXwKwjovCxeq4o884O1fAxK4U-dwKwHxa1oxqbwk8S2a3WcwMwAGu2Wm2WE4e8wl8hyVEKu9zUmxyqaUK2e0UFU2RwrUgU5qi2G1bzFHwCwmo4S7ErwAw8m0FU",
            "__csr":"",
            "fb_dtsg": fb_dtsg,
            "jazoest": "25411",
            "lsd": lsd,
            "__aaid": "0",
            "__spin_r": "1011074526",
            "__spin_b": "trunk",
            "__spin_t": "1706522748",
            "__jssesw": "1",
            "qpl_active_flow_ids": "270206296",        }
        response2 = self.r.post(f'https://business.facebook.com/ads/location-manager-pages-whitelist-eligibility/?page_ids[0]={PageID}',data=Data,headers=HeadersPost(),allow_redirects=True).text
        LID = re.search('"lid":"(.*?)"',response2)[1]
        DataR = response2.replace('for (;;);{"__ar":1,"payload":','').replace(',"lid":"%s"}'%(LID),'')
        Data = json.loads(DataR)
        Halaman_Bukan_Induk            = Data['%s'%(PageID)]['page_is_not_parent_already']['passes']
        Halaman_Bukan_Anak             = Data['%s'%(PageID)]['page_is_not_child_already']['passes']
        Halaman_Cukup_Umur             = Data['%s'%(PageID)]['page_is_old_enough']['passes']
        Halaman_Bukan_Root             = Data['%s'%(PageID)]['page_is_not_global_root']['passes']        
        Halaman_Memiliki_Foto_Profile  = Data['%s'%(PageID)]['page_has_profile_photo']['passes']
        Halaman_Memiliki_Foto_Sampul   = Data['%s'%(PageID)]['page_has_cover_photo']['passes']
        Izin_Pengguna                  = Data['%s'%(PageID)]['user_has_edit_permission']['passes']
        Izin_Pengguna_Root             = Data['%s'%(PageID)]['user_has_edit_permission_to_global_root_if_exists']['passes']
        Halaman_Tidak_Klasik           = Data['%s'%(PageID)]['page_is_not_classic']['passes']

        if Halaman_Bukan_Anak == True:pass
        else:Alasan.append("[bold white]- [red]Halaman Bukan Anak")
        if Halaman_Cukup_Umur == True:pass
        else:Alasan.append("[bold white]- [red]Halaman Harus Berusia 2 Hari")
        if Halaman_Bukan_Root == True:pass
        else:Alasan.append("[bold white]- [red]Halaman Bukan Root")
        if Halaman_Memiliki_Foto_Profile == True:pass
        else:Alasan.append("[bold white]- [red]Halaman Tidak Memiliki Foto Profile")
        if Halaman_Memiliki_Foto_Sampul == True:pass
        else:Alasan.append("[bold white]- [red]Halaman Tidak Memiliki Foto Sampul")
        if Izin_Pengguna == True:pass
        else:Alasan.append("[bold white]- [red]Halaman Tidak Memilik Izin")
        if Izin_Pengguna_Root == True:pass
        else:Alasan.append("[bold white]- [red]Halaman Tidak Memilik Izin Root")
        if Halaman_Tidak_Klasik == True:pass
        else:Alasan.append("[bold white]- [red]Halaman Masih Klasik")
        return(["[bold white]- [green]Halaman Bagus"] if int(len(Alasan)) == 0 else Alasan)

class BotMenu:

    def __init__(self):
        self.Cookie = open("Data/Cookie.txt",'r',encoding='utf-8').read()
        self._User = re.search('c_user=(.*?);',self.Cookie).group(1)
        self.PageID = []
        self.PageInfo = {}
        self.InputInfo = {}
        self.StoreID = []
        self.StoreData = {}
        self.Done = []
        self.Loop,self.Berhasil,self.Gagal = 0,0,0
        self.NameTypeReact = {"1635855486666999":'Like',"1678524932434102":'Love',"115940658764963":'Haha',"478547315650144":'Wow',"613557422527858":'Peduli',"908563459236466":'Sedih',"444813342392137":'Marah'}
        self.GraphQlUrl = 'https://www.facebook.com/api/graphql'
        self.BussinesUrl = 'https://business.facebook.com/business_locations/?page_id='
        with requests.Session() as self.r:
            self.r.cookies.update({'cookie':self.Cookie})
            Console(width=70).print(panel(f''' [bold green][[bold white]01[bold green]].[bold white]Bot Follow      [bold green][[bold white]04[bold green]].[bold white]Bot Share         [bold green][[bold white]07[bold green]].[bold white]Bot Report
 [bold green][[bold white]02[bold green]].[bold white]Bot Reaction    [bold green][[bold white]05[bold green]].[bold white]Bot Join Grup     [bold green][[bold white]08[bold green]].[bold white]Bot Rating Page
 [bold green][[bold white]03[bold green]].[bold white]Bot Comment     [bold green][[bold white]06[bold green]].[bold white]Bot Polling       [bold green][[bold white]09[bold green]].[bold red]Back''',width=70,style='bold white',subtitle='┌',subtitle_align='left'))
            Choice = input('   └─> ')
            if   Choice in ('1','01'):self.BotFollow()
            elif Choice in ('2','02'):self.BotReaction()
            elif Choice in ('3','03'):self.BotComment()
            elif Choice in ('4','04'):self.BotShare()
            elif Choice in ('5','05'):self.BotJoinGrup()
            elif Choice in ('6','06'):self.BotPolling()
            elif Choice in ('7','07'):self.BotReport()
            elif Choice in ('8','08'):self.BotRatingPage()
            elif Choice in ('9','09'):Menu()

    def BotFollow(self):
        self.GetPageID()
        Eksekusi = "\n".join(["[bold green][[bold white]{}[bold green]].[bold white]{} [bold green]([bold yellow]{}[bold green]) [bold green]([bold white]{}[bold green])".format(Count+1,self.InputInfo["%s"%(Count+1)],self.PageInfo[self.InputInfo["%s"%(Count+1)]],(self.GetCountStore(self.InputInfo["%s"%(Count+1)]) if self.GetCountStore(self.InputInfo["%s"%(Count+1)]) < 100 else "[bold red]UPDATE")) for Count in range(int(len(self.PageID)))])
        Console(width=70).print(panel("%s"%(Eksekusi),width=70,style='bold white',subtitle='┌',subtitle_align='left'))
        ChoiceInput = input('   └─> ').split(',')
        with ThreadPoolExecutor(max_workers=35) as (V):
            for Choice in ChoiceInput:
                if int(Choice) < 10:
                    Choice = Choice.replace('0','')
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                else:
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                V.submit(self.GetIDStorePage,self.SelectPage)
        Console(width=70).print(panel("Masukan ID Akun Yang Ingin Di Follow",width=70,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        UserFollow = input('   └─> ')
        self.FollowUser(UserFollow,"",self.Cookie)
        Console(width=70).print(panel("[bold green]Berhasil %s [white]| [red]Gagal %s"%(self.Berhasil,self.Gagal),width=70,style='bold white'),justify='center')

    def GetCountStore(self,Page_ID):
        response = bs(self.r.get(self.BussinesUrl+Page_ID,headers=HeadersGet(),allow_redirects=True).content,'html.parser')
        fb_dtsg_ag = re.search('"DTSGInitialData",\[\],{"token":".*?","async_get_token":"(.*?)"}', str(response)).group(1).replace(":",'%3A')
        NextResponse = self.r.get(f"https://business.facebook.com/ads/location-manager-filter-locations/?page_id={Page_ID}&limit=50&sort_column=store_number&sort_order=descending&fb_dtsg_ag={fb_dtsg_ag}&__user={self._User}&__hsi=7328444763778866303&__a=1&__req=s",headers=HeadersGet(),allow_redirects=True).text
        try:
            LID = re.search('"lid":"(.*?)"',NextResponse)[1]
            DataR = NextResponse.replace('for (;;);{"__ar":1,"payload":','').replace(',"lid":"%s"}'%(LID),'')
            Data = {f"{Page_ID}":{"StoreID":json.loads(DataR)['pageIDs'],"Count":json.loads(DataR)['estimatedCount']}}
            self.StoreData.update(Data)
            return(Data[Page_ID]['Count'])
        except:
            return(0)

    def GetIDStorePage(self,Page_ID):
        with ThreadPoolExecutor(max_workers=35) as (V):
            for StoreID in self.StoreData[Page_ID]['StoreID']:V.submit(self.ConvertIDStorePage,StoreID)

    def ConvertIDStorePage(self,StoreID):
        with requests.Session() as r:
            response = bs(r.get(f'https://www.facebook.com/{StoreID}').content,'html.parser')
            User = re.findall('content="fb://profile/(.*?)"',str(response))[1]
            self.StoreID.append(User)

    def GetPageID(self):
        response = bs(self.r.get('https://www.facebook.com/pages',headers=HeadersGet(),allow_redirects=True).content,'html.parser')
        Data = GetData(response)
        Variable = {"showUpdatedLaunchpointRedesign":True,"useAdminedPagesForActingAccount":False,"useNewPagesYouManage":True}
        Data.update({'variables': json.dumps(Variable),'doc_id': '5300338636681652'})
        response2 = self.r.post(self.GraphQlUrl,data=Data)
        Count = 0
        for Data in response2.json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']:
            Count+=1
            IDPage = Data['profile']['delegate_page_id']
            NamePage = Data['profile']['name']
            self.PageID.append(IDPage)
            self.InputInfo.update({"%s"%(Count):IDPage})
            self.PageInfo.update({"%s"%(IDPage):NamePage})

    def SwitchProfile(self,Profile_ID,OldCookie):
        with requests.Session() as r:
            r.cookies.update({'cookie':OldCookie})
            response = bs(r.get('https://www.facebook.com',headers=HeadersGet(),allow_redirects=True).content,'html.parser')
            Data = GetData(response)
            Variable = {"profile_id":Profile_ID}
            Data.update({
                "fb_api_caller_class":"RelayModern",
                "fb_api_req_friendly_name":"CometProfileSwitchMutation",
                "variables":json.dumps(Variable),
                "server_timestamps":True,
                "doc_id":"7240611932633722",
            })
            response = r.post(self.GraphQlUrl,headers=HeadersPost(),allow_redirects=True,data=Data)
            NewCookie = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
            return(NewCookie.replace('cookie=',''))

    def FollowUser(self,Target,Done,OldCookie):
        for Profile_ID in self.StoreID:
            if Done in self.Done:pass
            else:
                self.PrintInfo("Switch Profile")
                NewCookie = self.SwitchProfile(Profile_ID,OldCookie)
                with requests.Session() as r:
                    r.cookies.update({'cookie':NewCookie})
                    self.PrintInfo("%s"%(Profile_ID))
                    response = bs(r.get('https://www.facebook.com/%s'%(Target),headers=HeadersGet(),allow_redirects=True).content,'html.parser')
                    Data = GetData(response)
                    Variable = {"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1706281803231,501997,190055527696468,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,1706281799141,676215,391724414624676,3,","is_tracking_encrypted":False,"subscribe_location":"PROFILE","subscribee_id":Target,"tracking":None,"actor_id":Data['__user'],"client_mutation_id":3,},"scale":1}
                    Data.update({
                        "fb_api_caller_class":"RelayModern",
                        "fb_api_req_friendly_name":"CometUserFollowMutation",
                        "variables":json.dumps(Variable),
                        "server_timestamps":True,
                        "doc_id":"6742670285862232",
                    })
                    My_Facebook = "1318874900"
                    response2 = r.post(self.GraphQlUrl,headers=HeadersPost(),allow_redirects=True,data=Data)
                    NewCookie2 = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
                    if '"actor_subscribe"' in response2.text:
                        if '"Mengikuti"' in response2.text:
                            self.Berhasil += 1
                            self.PrintInfo("Berhasil Mengikuti");sleep(1)
                        elif '"Ikuti"' in response2.text:
                            self.Gagal += 1
                            self.PrintInfo("Gagal Mengikuti");sleep(1)
                    else:
                        self.Gagal += 1
                        self.PrintInfo("Terjadi Kesalahan");sleep(1)
                    self.Done.append(Profile_ID)
                    self.FollowUser(Target,Profile_ID,NewCookie2)

    def BotComment(self):
        self.GetPageID()
        Eksekusi = "\n".join(["[bold green][[bold white]{}[bold green]].[bold white]{} [bold green]([bold yellow]{}[bold green]) [bold green]([bold white]{}[bold green])".format(Count+1,self.InputInfo["%s"%(Count+1)],self.PageInfo[self.InputInfo["%s"%(Count+1)]],(self.GetCountStore(self.InputInfo["%s"%(Count+1)]) if self.GetCountStore(self.InputInfo["%s"%(Count+1)]) < 100 else "[bold red]UPDATE")) for Count in range(int(len(self.PageID)))])
        Console(width=70).print(panel("%s"%(Eksekusi),width=70,style='bold white',subtitle='┌',subtitle_align='left'))
        ChoiceInput = input('   └─> ').split(',')
        for Choice in ChoiceInput:
            if int(Choice) < 10:
                Choice = Choice.replace('0','')
                try:self.SelectPage = self.InputInfo[Choice]
                except TypeError:Console().print("   └─> [yellow]Pilihan %s Tidak Diketahui !"%(Choice),end='\r');sleep(1)
            else:
                try:self.SelectPage = self.InputInfo[Choice]
                except TypeError:Console().print("   └─> [yellow]Pilihan %s Tidak Diketahui !"%(Choice),end='\r');sleep(1)
            self.GetIDStorePage(self.SelectPage)
        Console(width=70).print(panel("Masukan Link Postingan, Pastikan Tombol Komentar Pada Postingan Aktif",width=70,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        LinkPost = input('   └─> ')
        PostID = FindAllID(LinkPost)
        self.PrintInfo("Post ID : %s"%(PostID))
        sleep(1)
        Console(width=70).print(panel("Masukan Komentar, Gunakan '|' Sebagai Pemisah.",width=70,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        InputText = input('   └─> ').split('|')
        self.CommentPost(PostID,InputText,"",self.Cookie)
        Console(width=70).print(panel("[bold green]Berhasil %s [white]| [red]Gagal %s"%(self.Berhasil,self.Gagal),width=70,style='bold white'),justify='center')

    def CommentPost(self,PostID,InputText,Done,OldCookie):
        for Profile_ID in self.StoreID:
            CommentText = random.choice(InputText)
            if Done in self.Done:pass
            else:
                self.PrintInfo("Switch Profile")
                NewCookie = self.SwitchProfile(Profile_ID,OldCookie)
                with requests.Session() as r:
                    r.cookies.update({'cookie':NewCookie})
                    self.PrintInfo("%s"%(Profile_ID))
                    response = bs(r.get('https://www.facebook.com/%s'%(PostID),headers=HeadersGet(),allow_redirects=True,timeout=(10,20)).content,'html.parser')
                    try:SessionID = re.search('{"sessionID":"(.*?)",',str(response)).group(1)
                    except Exception:SessionID = re.search('{"sessionID":"(.*?)",',str(response)).group(1)
                    try:ClientID = re.search('{"clientID":"(.*?)"}',str(response)).group(1)
                    except Exception:ClientID = re.search('{clientID:"(.*?)"}',str(response)).group(1)
                    try:FeedbackID = re.search('"feedback":{"associated_group":null,"id":"(.*?)"},"is_story_civic":null',str(response)).group(1)
                    except Exception:FeedbackID = re.search('"feedback":{"id":"(.*?)"',str(response)).group(1)
                    try:encrypted_tracking = re.findall('{"action_link":null,"badge":null,"follow_button":null},"encrypted_tracking":"(.*?)"},"__module_operation_CometFeedStoryTitleSection_story"',str(response))[-1]
                    except Exception as e:encrypted_tracking = re.findall('"encrypted_tracking":"(.*?)"',str(response))[0]
                    Data = GetData(response)
                    Variable = {
                        "feedLocation":"COMET_MEDIA_VIEWER",
                        "feedbackSource":65,
                        "groupID":None,
                        "input":{"client_mutation_id":"1",
                            "actor_id":Data['__user'],
                            "attachments":None,
                            "feedback_id":FeedbackID,
                            "formatting_style":None,
                            "message":{
                                "ranges":[],
                                "text":CommentText
                                },
                            "attribution_id_v2":"CometPhotoRoot.react,comet.mediaviewer.photo,unexpected,1706457575166,38367,,,;ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1706457544866,777223,190055527696468,12#15#301,1318874900;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,1706457533920,191985,391724414624676,3,",
                            "vod_video_timestamp":None,
                            "feedback_referrer":"/photo",
                            "is_tracking_encrypted":True,
                            "tracking":["%s"%(encrypted_tracking),"%s"%(json.dumps({"assistant_caller":"comet_above_composer","conversation_guide_session_id":None,"conversation_guide_shown":None}))],
                            "feedback_source":"MEDIA_VIEWER",
                            "idempotence_token":f"client:{ClientID}",
                            "session_id":SessionID
                        },"inviteShortLinkKey":None,
                        "renderLocation":None,
                        "scale":1,
                        "useDefaultActor":False,
                        "focusCommentID":None
                    }
                    Data.update({
                        "fb_api_caller_class":"RelayModern",
                        "fb_api_req_friendly_name":"useCometUFICreateCommentMutation",
                        "variables":json.dumps(Variable),
                        "server_timestamps":True,
                        "doc_id":"7168916536529458",
                    })
                    response2 = r.post(self.GraphQlUrl,headers=HeadersPost(),allow_redirects=True,data=Data)
                    NewCookie2 = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
                    if '"comment_create"' in response2.text:
                        if '"Edit atau hapus ini"' in response2.text:
                            self.Berhasil += 1
                            self.PrintInfo("Berhasil Komen");sleep(1)
                        else:
                            self.Gagal += 1
                            self.PrintInfo("Gagal Komen");sleep(1)
                    else:
                        self.Gagal += 1
                        self.PrintInfo("Terjadi Kesalahan");sleep(1)
                    self.Done.append(Profile_ID)
                    self.CommentPost(PostID,InputText,Profile_ID,NewCookie2)

    def BotReaction(self):
        self.GetPageID()
        ReactType = []
        Eksekusi = "\n".join(["[bold green][[bold white]{}[bold green]].[bold white]{} [bold green]([bold yellow]{}[bold green]) [bold green]([bold white]{}[bold green])".format(Count+1,self.InputInfo["%s"%(Count+1)],self.PageInfo[self.InputInfo["%s"%(Count+1)]],(self.GetCountStore(self.InputInfo["%s"%(Count+1)]) if self.GetCountStore(self.InputInfo["%s"%(Count+1)]) < 100 else "[bold red]UPDATE")) for Count in range(int(len(self.PageID)))])
        Console(width=70).print(panel("%s"%(Eksekusi),width=70,style='bold white',subtitle='┌',subtitle_align='left'))
        ChoiceInput = input('   └─> ').split(',')
        for Choice in ChoiceInput:
            if int(Choice) < 10:
                Choice = Choice.replace('0','')
                try:self.SelectPage = self.InputInfo[Choice]
                except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
            else:
                try:self.SelectPage = self.InputInfo[Choice]
                except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
            self.GetIDStorePage(self.SelectPage)
        Console(width=70).print(panel("Masukan ID Postingan, Pastikan Tombol Komentar Pada Postingan Aktif",width=70,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        PostID = input('   └─> ')
        Console(width=70).print(panel("""            [bold green][[bold white]01[bold green]].[bold white]Sukai                  [bold green][[bold white]05[bold green]].[bold white]Peduli
[bold green]            [[bold white]02[bold green]].[bold white]Love                   [bold green][[bold white]06[bold green]].[bold white]Sedih
[bold green]            [[bold white]03[bold green]].[bold white]Haha                   [bold green][[bold white]07[bold green]].[bold white]Marah
[bold green]            [[bold white]04[bold green]].[bold white]Wow""",width=70,style='bold white',subtitle='┌',subtitle_align='left'))
        InputType = input('   └─> ').split(',')
        for ChoiceType in InputType:
            if ChoiceType in ['1','01']:Type = '1635855486666999'
            if ChoiceType in ['2','02']:Type = '1678524932434102'
            if ChoiceType in ['3','03']:Type = '115940658764963'
            if ChoiceType in ['4','04']:Type = '478547315650144'
            if ChoiceType in ['5','05']:Type = '613557422527858'
            if ChoiceType in ['6','06']:Type = '908563459236466'
            if ChoiceType in ['7','07']:Type = '444813342392137'
            ReactType.append(Type)
        self.ReactPost(PostID,ReactType,"",self.Cookie)

    def ReactPost(self,PostID,ListReact,Done,OldCookie):
        for Profile_ID in self.StoreID:
            Type = random.choice(ListReact)
            if Done in self.Done:pass
            else:
                self.PrintInfo("Switch Profile")
                NewCookie = self.SwitchProfile(Profile_ID,OldCookie)
                with requests.Session() as r:
                    r.cookies.update({'cookie':NewCookie})
                    self.PrintInfo("%s"%(Profile_ID))
                    response = bs(r.get('https://www.facebook.com/%s'%(PostID),headers=HeadersGet(),allow_redirects=True,timeout=(10,20)).content,'html.parser')
                    try:SessionID = re.search('{"sessionID":"(.*?)",',str(response)).group(1)
                    except Exception:SessionID = re.search('{"sessionID":"(.*?)",',str(response)).group(1)
                    try:FeedbackID = re.search('"feedback":{"associated_group":null,"id":"(.*?)"},"is_story_civic":null',str(response)).group(1)
                    except Exception:FeedbackID = re.search('"feedback":{"id":"(.*?)"',str(response)).group(1)
                    try:encrypted_tracking = re.findall('{"action_link":null,"badge":null,"follow_button":null},"encrypted_tracking":"(.*?)"},"__module_operation_CometFeedStoryTitleSection_story"',str(response))[-1]
                    except Exception as e:encrypted_tracking = re.findall('"encrypted_tracking":"(.*?)"',str(response))[0]
                    Data = GetData(response)
                    Variable = {
                        "input":{
                            "attribution_id_v2":"CometPhotoRoot.react,comet.mediaviewer.photo,unexpected,1706462471862,665130,,,;ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1706462463063,7862,190055527696468,12#15#301,10232639418350748;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,1706462413836,749164,391724414624676,3,",
                            "feedback_id":FeedbackID,
                            "feedback_reaction_id":Type,
                            "feedback_source":"MEDIA_VIEWER",
                            "is_tracking_encrypted":True,
                            "tracking":[encrypted_tracking],
                            "session_id":SessionID,
                            "actor_id":Data['__user'],
                            "client_mutation_id":"3"
                        },
                        "useDefaultActor":False,
                        "scale":1
                    }
                    Data.update({
                        "fb_api_caller_class":"RelayModern",
                        "fb_api_req_friendly_name":"CometUFIFeedbackReactMutation",
                        "variables":json.dumps(Variable),
                        "server_timestamps":True,
                        "doc_id":"6880473321999695",
                    })
                    response2 = r.post(self.GraphQlUrl,headers=HeadersPost(),allow_redirects=True,data=Data)
                    NewCookie2 = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
                    open("react.json",'w').write(response2.text)
                    if "'can_viewer_react': True" in str(response2.json()) and Data['__user'] in str(response2.json()):
                        self.Berhasil += 1
                        self.PrintInfo("Reaction : %s"%(self.NameTypeReact[Type]));sleep(1)
                    else:
                        self.Gagal += 1
                        self.PrintInfo("Gagal Menanggapi");sleep(1)
                    self.Done.append(Profile_ID)
                    self.ReactPost(PostID,ListReact,Profile_ID,NewCookie2)

    def BotJoinGrup(self):
        self.GetPageID()
        Eksekusi = "\n".join(["[bold green][[bold white]{}[bold green]].[bold white]{} [bold green]([bold yellow]{}[bold green]) [bold green]([bold white]{}[bold green])".format(Count+1,self.InputInfo["%s"%(Count+1)],self.PageInfo[self.InputInfo["%s"%(Count+1)]],(self.GetCountStore(self.InputInfo["%s"%(Count+1)]) if self.GetCountStore(self.InputInfo["%s"%(Count+1)]) < 100 else "[bold red]UPDATE")) for Count in range(int(len(self.PageID)))])
        Console(width=70).print(panel("%s"%(Eksekusi),width=70,style='bold white',subtitle='┌',subtitle_align='left'))
        ChoiceInput = input('   └─> ').split(',')
        with ThreadPoolExecutor(max_workers=35) as (V):
            for Choice in ChoiceInput:
                if int(Choice) < 10:
                    Choice = Choice.replace('0','')
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                else:
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                V.submit(self.GetIDStorePage,self.SelectPage)
        Console(width=70).print(panel("Masukan ID Grup Facebook",width=70,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        GrupID = input('   └─> ')
        self.AutoJoinGrup(GrupID,"",self.Cookie)
        Console(width=70).print(panel("[bold green]Berhasil %s [white]| [red]Gagal %s"%(self.Berhasil,self.Gagal),width=70,style='bold white'),justify='center')

    def AutoJoinGrup(self,GrupID,Done,OldCookie):
        for Profile_ID in self.StoreID:
            if Done in self.Done:pass
            else:
                self.PrintInfo("Switch Profile")
                NewCookie = self.SwitchProfile(Profile_ID,OldCookie)
                with requests.Session() as r:
                    r.cookies.update({'cookie':NewCookie})
                    self.PrintInfo("%s"%(Profile_ID))
                    response = bs(r.get('https://www.facebook.com/%s'%(GrupID),headers=HeadersGet(),allow_redirects=True).content,'html.parser')
                    Data = GetData(response)
                    Variable = {
                        "feedType":"DISCUSSION",
                        "groupID":GrupID,
                        "imageMediaType":"image/x-auto",
                        "input":{
                            "action_source":"GROUP_MALL",
                            "attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,unexpected,1706613170976,709735,2361831622,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,via_cold_start,1706613153354,730012,391724414624676,,",
                            "group_id":GrupID,
                            "group_share_tracking_params":{
                                "app_id":"2220391788200892",
                                "exp_id":"null",
                                "is_from_share":False
                            },
                            "actor_id":Data['__user'],
                            "client_mutation_id":"1"
                        },
                        "inviteShortLinkKey":None,
                        "isChainingRecommendationUnit":False,
                        "scale":1,
                        "source":"GROUP_MALL",
                        "renderLocation":"group_mall",
                        "__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":False
                    }
                    Data.update({
                        "fb_api_caller_class":"RelayModern",
                        "fb_api_req_friendly_name":"GroupCometJoinForumMutation",
                        "variables":json.dumps(Variable),
                        "server_timestamps":True,
                        "doc_id":"7732956370117476",
                        'fb_api_analytics_tags': ["qpl_active_flow_ids=431626709"]
                    })
                    My_Facebook = "1318874900"
                    response2 = r.post(self.GraphQlUrl,headers=HeadersPost(),allow_redirects=True,data=Data)
                    NewCookie2 = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
                    if '"Bergabung"' in response2.text:
                        self.Berhasil += 1
                        self.PrintInfo("Berhasil Bergabung");sleep(1)
                    elif '"Gabung"' in response2.text:
                        self.Gagal += 1
                        self.PrintInfo("Gagal Bergabung");sleep(1)
                    else:
                        self.Gagal += 1
                        self.PrintInfo("Terjadi Kesalahan");sleep(1)
                    self.Done.append(Profile_ID)
                    self.AutoJoinGrup(GrupID,Profile_ID,NewCookie2)

    def BotShare(self):
        self.GetPageID()
        Eksekusi = "\n".join(["[bold green][[bold white]{}[bold green]].[bold white]{} [bold green]([bold yellow]{}[bold green]) [bold green]([bold white]{}[bold green])".format(Count+1,self.InputInfo["%s"%(Count+1)],self.PageInfo[self.InputInfo["%s"%(Count+1)]],(self.GetCountStore(self.InputInfo["%s"%(Count+1)]) if self.GetCountStore(self.InputInfo["%s"%(Count+1)]) < 100 else "[bold red]UPDATE")) for Count in range(int(len(self.PageID)))])
        Console(width=70).print(panel("%s"%(Eksekusi),width=70,style='bold white',subtitle='┌',subtitle_align='left'))
        ChoiceInput = input('   └─> ').split(',')
        with ThreadPoolExecutor(max_workers=35) as (V):
            for Choice in ChoiceInput:
                if int(Choice) < 10:
                    Choice = Choice.replace('0','')
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                else:
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                V.submit(self.GetIDStorePage,self.SelectPage)
        Console(width=70).print(panel("Masukan ID Atau Link Postingan",width=70,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        InputID = input('   └─> ')
        if "https" in str(InputID):
            PostID = FindAllID(InputID)
        else:
            PostID = InputID
        self.AutoShare(PostID,"",self.Cookie)
        Console(width=70).print(panel("[bold green]Berhasil %s [white]| [red]Gagal %s"%(self.Berhasil,self.Gagal),width=70,style='bold white'),justify='center')

    def AutoShare(self,PostID,Done,OldCookie):
        for Profile_ID in self.StoreID:
            if Done in self.Done:pass
            else:
                self.PrintInfo("Switch Profile")
                NewCookie = self.SwitchProfile(Profile_ID,OldCookie)
                with requests.Session() as r:
                    r.cookies.update({'cookie':NewCookie})
                    self.PrintInfo("%s"%(Profile_ID))
                    response = bs(r.get('https://www.facebook.com/%s'%(PostID),headers=HeadersGet(),allow_redirects=True).content,'html.parser')
                    Data = GetData(response)
                    Params = re.search('"params":{"fbid":"(.*?)"',str(response)).group(1)
                    Token = re.search('"sessionID":"(.*?)"',str(response)).group(1)
                    Variable = {
                        "input":{
                            "attachments":{
                                "link":{
                                    "share_scrape_data":"{\"share_type\":2,\"share_params\":[%s]}"%(Params)
                                }
                            },
                            "audiences":{
                                "undirected":{
                                    "privacy":{
                                        "allow":[],"base_state":"EVERYONE",
                                        "deny":[],
                                        "tag_expansion_state":"UNSPECIFIED"
                                    }
                                }
                            },
                            "idempotence_token":Token,
                            "is_tracking_encrypted":True,
                            "navigation_data":{
                                "attribution_id_v2":"CometPhotoRoot.react,comet.mediaviewer.photo,via_cold_start,1699124635808,90556,,"
                            },
                            "source":"www",
                            "tracking":[],
                            "actor_id":Data['__user'],
                            "client_mutation_id":"1"
                        },
                        "scale":1,
                        "feedbackSource":1,
                        "focusCommentID":None,
                        "useDefaultActor":False,
                        "feedLocation":"NEWSFEED",
                        "renderLocation":"homepage_stream",
                        "displayCommentsFeedbackContext":None,
                        "displayCommentsContextIsStorySet":None,
                        "displayCommentsContextIsAdPreview":None,
                        "displayCommentsContextEnableComment":None,
                        "displayCommentsContextIsAggregatedShare":None,
                        "privacySelectorRenderLocation":"COMET_STREAM",
                        "UFI2CommentsProvider_commentsKey":"CometModernHomeFeedQuery",
                        "__relay_internal__pv__IsWorkUserrelayprovider":False,
                        "__relay_internal__pv__IsMergQAPollsrelayprovider":False,
                        "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,
                        "__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,
                        "__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,
                        "__relay_internal__pv__StoriesRingrelayprovider":False
                    }
                    Data.update({
                        'fb_api_caller_class':'RelayModern',
                        'fb_api_req_friendly_name':'useCometFeedToFeedReshare_FeedToFeedMutation',
                        'variables':json.dumps(Variable),
                        'server_timestamps':True,
                        'doc_id':'6509593895832866'
                    })
                    response2 = r.post(self.GraphQlUrl,headers=HeadersPost(),allow_redirects=True,data=Data)
                    NewCookie2 = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
                    if '"story_create"' in response2.text:
                        self.Berhasil += 1
                        self.PrintInfo("Share +1")
                        sleep(1)
                    else:
                        self.Gagal += 1
                        self.PrintInfo("Gagal Share")
                        sleep(1)
                    self.Done.append(Profile_ID)
                    self.AutoShare(PostID,Profile_ID,NewCookie2)

    def BotPolling(self):
        self.GetPageID()
        Eksekusi = "\n".join(["[bold green][[bold white]{}[bold green]].[bold white]{} [bold green]([bold yellow]{}[bold green]) [bold green]([bold white]{}[bold green])".format(Count+1,self.InputInfo["%s"%(Count+1)],self.PageInfo[self.InputInfo["%s"%(Count+1)]],(self.GetCountStore(self.InputInfo["%s"%(Count+1)]) if self.GetCountStore(self.InputInfo["%s"%(Count+1)]) < 100 else "[bold red]UPDATE")) for Count in range(int(len(self.PageID)))])
        Console(width=70).print(panel("%s"%(Eksekusi),width=70,style='bold white',subtitle='┌',subtitle_align='left'))
        ChoiceInput = input('   └─> ').split(',')
        with ThreadPoolExecutor(max_workers=35) as (V):
            for Choice in ChoiceInput:
                if int(Choice) < 10:
                    Choice = Choice.replace('0','')
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                else:
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                V.submit(self.GetIDStorePage,self.SelectPage)
        Console(width=70).print(panel("Masukan ID Atau Link Postingan",width=70,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        InputID = input('   └─> ')
        if "https" in str(InputID):
            PostID = FindAllID(InputID)
        else:
            PostID = InputID
        response = bs(requests.get("https://www.facebook.com/%s"%(PostID),cookies={'cookie':self.Cookie}).content,'html.parser')
        Caption = re.search(r'"should_host_actor_link_in_watch":.*?,"message":{"text":"(.*?)","__typename":"TextWithEntities"}',str(response)).group(1)
        Nodes = re.search('"orderedOptions":{"nodes":(.*?)},"is_poll_closed"',str(response)).group(1)
        Option = re.findall('{"id":"(.*?)","text":"(.*?)","viewer_has_voted":.*?,"associated_image":.*?,"owner"',str(Nodes))
        Vote = [ {'option_id':list(x)[0], 'text':list(x)[1]} for x in Option]
        Eksekusi2 = "\n".join([f"[bold white]{Caption}\n\n[green][[white]{str(Count+1)}[green]].{Text['text']}" for Count,Text in enumerate(Vote)])
        Console(width=70).print(panel("%s"%(Eksekusi2),width=70,style='bold white',subtitle='┌',subtitle_align='left'))
        OptionInput = input('   └─> ')
        Pilihan = Vote[int(OptionInput)-1]
        self.AutoPolling(Pilihan['option_id'],PostID,"",self.Cookie)
        Console(width=70).print(panel("[bold green]Berhasil %s [white]| [red]Gagal %s"%(self.Berhasil,self.Gagal),width=70,style='bold white'),justify='center')

    def AutoPolling(self,Option,PostID,Done,OldCookie):
        for Profile_ID in self.StoreID:
            if Done in self.Done:pass
            else:
                self.PrintInfo("Switch Profile")
                NewCookie = self.SwitchProfile(Profile_ID,OldCookie)
                with requests.Session() as r:
                    r.cookies.update({'cookie':NewCookie})
                    self.PrintInfo("%s"%(Profile_ID))
                    response = bs(r.get('https://www.facebook.com/%s'%(PostID),headers=HeadersGet(),allow_redirects=True).content,'html.parser')
                    Data = GetData(response)
                    QuestionID = re.search('"questionID":"(.*?)"',str(response)).group(1)
                    Tracking = re.findall('"encrypted_tracking":"(.*?)"',str(response))[0]
                    Variable = {
                        "input":{
                            "is_tracking_encrypted":True,
                            "option_id":Option,
                            "question_id":QuestionID,
                            "tracking":[Tracking],
                            "actor_id":Data['__user'],
                            "client_mutation_id":"1"
                        },
                        "scale":1.5,
                        "__relay_internal__pv__IsWorkUserrelayprovider":False
                    }
                    Data.update({
                        'fb_api_caller_class':'RelayModern',
                        'fb_api_req_friendly_name':'useCometPollAddVoteMutation',
                        'variables':json.dumps(Variable),
                        'server_timestamps':True,
                        'doc_id':'6681967255191860'
                    })
                    response2 = r.post(self.GraphQlUrl,headers=HeadersPost(),allow_redirects=True,data=Data)
                    NewCookie2 = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
                    if '"question_add_vote"' in response2.text:
                        self.Berhasil += 1
                        self.PrintInfo("Polling +1")
                        sleep(1)
                    else:
                        self.Gagal += 1
                        self.PrintInfo("Gagal Polling")
                        sleep(1)
                    self.Done.append(Profile_ID)
                    self.AutoPolling(Option,PostID,Profile_ID,NewCookie2)

    def BotRatingPage(self):
        self.GetPageID()
        Eksekusi = "\n".join(["[bold green][[bold white]{}[bold green]].[bold white]{} [bold green]([bold yellow]{}[bold green]) [bold green]([bold white]{}[bold green])".format(Count+1,self.InputInfo["%s"%(Count+1)],self.PageInfo[self.InputInfo["%s"%(Count+1)]],(self.GetCountStore(self.InputInfo["%s"%(Count+1)]) if self.GetCountStore(self.InputInfo["%s"%(Count+1)]) < 100 else "[bold red]UPDATE")) for Count in range(int(len(self.PageID)))])
        Console(width=70).print(panel("%s"%(Eksekusi),width=70,style='bold white',subtitle='┌',subtitle_align='left'))
        ChoiceInput = input('   └─> ').split(',')
        with ThreadPoolExecutor(max_workers=35) as (V):
            for Choice in ChoiceInput:
                if int(Choice) < 10:
                    Choice = Choice.replace('0','')
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                else:
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                V.submit(self.GetIDStorePage,self.SelectPage)
        Console(width=70).print(panel("Masukan ID Halaman",width=70,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        TargetID = input('   └─> ')
        Console(width=70).print(panel("""      [bold green][[bold white]01[bold green]].[bold white]Rating Positif              [bold green][[bold white]02[bold green]].[bold white]Rating Negatif""",width=70,style='bold white',subtitle='┌',subtitle_align='left'))
        Rating = input('   └─> ')
        if Rating in ['1','01','a']:Type = "POSTIVE"
        else:Type = "NEGATIVE"
        Console(width=70).print(panel("""Masukan Text, Gunakan '|' Sebagai Pemisah""",width=70,style='bold white',subtitle='┌',subtitle_align='left'),justify="center")
        InputText = input('   └─> ').split('|')
        self.AutoRatingPage(TargetID,Type,InputText,"",self.Cookie)
        Console(width=70).print(panel("[bold green]Berhasil %s [white]| [red]Gagal %s"%(self.Berhasil,self.Gagal),width=70,style='bold white'),justify='center')

    def AutoRatingPage(self,TargetID,Type,ListText,Done,OldCookie):
        for Profile_ID in self.StoreID:
            Caption = random.choice(ListText)
            if Done in self.Done:pass
            else:
                self.PrintInfo("Switch Profile")
                NewCookie = self.SwitchProfile(Profile_ID,OldCookie)
                with requests.Session() as r:
                    r.cookies.update({'cookie':NewCookie})
                    self.PrintInfo("%s"%(Profile_ID))
                    response = bs(r.get('https://www.facebook.com/%s'%(TargetID),headers=HeadersGet(),allow_redirects=True).content,'html.parser')
                    Data = GetData(response)
                    target = re.search('{"is_business_page_active":.*?,"id":"(\d+)"}',str(response)).group(1)
                    session_id = re.search('"sessionID":"(.*?)"',str(response)).group(1)
                    aud = {'privacy':{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}}
                    mes = {"ranges":[],"text":Caption}
                    rec = {
                        "page_id":TargetID,
                        "rec_type":Type
                    }
                    put = {
                        "tracking":[None],
                        "with_tags_ids":[],
                        "actor_id":Profile_ID,
                        "message":json.dumps(mes),
                        "audience":json.dumps(aud),
                        "page_recommendation":json.dumps(rec),
                        "idempotence_token":f"{session_id}_FEED",
                        "logging":{'composer_session_id':session_id},
                        "source":"WWW","client_mutation_id":"1","text_format_preset_id":"0",
                        "composer_entry_point":"inline_composer","event_share_metadata":{'surface':'newsfeed'},
                        "composer_source_surface":"page_recommendation_tab",
                        "navigation_data":{
                            'attribution_id_v2':'ProfileCometReviewsTabRoot.react,comet.profile.reviews,via_cold_start,1697712264297,368069,250100865708545,'
                        },}
                    Variable = {
                        "input":json.dumps(put),"hashtag":None,"groupID":None,"focusCommentID":None,"gridMediaWidth":None,"inviteShortLinkKey":None,"displayCommentsFeedbackContext":None,"displayCommentsContextIsStorySet":None,"displayCommentsContextIsAdPreview":None,"displayCommentsContextEnableComment":None,"displayCommentsContextIsAggregatedShare":None,"scale":1,"feedbackSource":0,"renderLocation":"timeline","feedLocation":"PAGE_SURFACE_RECOMMENDATIONS","privacySelectorRenderLocation":"COMET_STREAM","UFI2CommentsProvider_commentsKey":"ProfileCometReviewsTabRoute","isTimeline":True,"isProfileReviews":True,"isFeed":False,"isGroup":False,"isEvent":False,"isFundraiser":False,"isFunFactPost":False,"isPageNewsFeed":False,"useDefaultActor":False,"isSocialLearning":False,"isWorkSharedDraft":False,"canUserManageOffers":False,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,"__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__StoriesRingrelayprovider":False}
                    Data.update({
                        "fb_api_caller_class":"RelayModern",
                        "fb_api_req_friendly_name":"ComposerStoryCreateMutation",
                        "variables":json.dumps(Variable),
                        "server_timestamps":True,
                        "doc_id":"6308506282588750",
                    })
                    response2 = r.post(self.GraphQlUrl,headers=HeadersPost(),allow_redirects=True,data=Data)
                    NewCookie2 = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
                    if '"story_id"' in response2.text:
                        self.Berhasil += 1
                        self.PrintInfo("Berhasil Rating");sleep(1)
                    else:
                        self.Gagal += 1
                        self.PrintInfo("Gagal Rating");sleep(1)
                    self.Done.append(Profile_ID)
                    self.AutoRatingPage(TargetID,Type,ListText,Profile_ID,NewCookie2)

    def BotReport(self):
        self.GetPageID()
        Eksekusi = "\n".join(["[bold green][[bold white]{}[bold green]].[bold white]{} [bold green]([bold yellow]{}[bold green]) [bold green]([bold white]{}[bold green])".format(Count+1,self.InputInfo["%s"%(Count+1)],self.PageInfo[self.InputInfo["%s"%(Count+1)]],(self.GetCountStore(self.InputInfo["%s"%(Count+1)]) if self.GetCountStore(self.InputInfo["%s"%(Count+1)]) < 100 else "[bold red]UPDATE")) for Count in range(int(len(self.PageID)))])
        Console(width=70).print(panel("%s"%(Eksekusi),width=70,style='bold white',subtitle='┌',subtitle_align='left'))
        ChoiceInput = input('   └─> ').split(',')
        with ThreadPoolExecutor(max_workers=35) as (V):
            for Choice in ChoiceInput:
                if int(Choice) < 10:
                    Choice = Choice.replace('0','')
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                else:
                    try:self.SelectPage = self.InputInfo[Choice]
                    except TypeError:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);Menu()
                V.submit(self.GetIDStorePage,self.SelectPage)
        Console(width=70).print(panel("Masukan ID Yang Ingin Di Report",width=70,style='bold white',subtitle='┌',subtitle_align='left'),justify='center')
        TargetID = input('   └─> ')
        self.AutoReport(TargetID,"",self.Cookie)

    def AutoReport(self,TargetID,Done,OldCookie):
        for Profile_ID in self.StoreID:
            if Done in self.Done:pass
            else:
                self.PrintInfo("Switch Profile")
                NewCookie = self.SwitchProfile(Profile_ID,OldCookie)
                with requests.Session() as r:
                    r.cookies.update({'cookie':NewCookie})
                    self.PrintInfo("%s"%(Profile_ID))
                    response = bs(r.get('https://www.facebook.com/%s'%(TargetID),headers=HeadersGet(),allow_redirects=True).content,'html.parser')
                    Data = GetData(response)
                    SessionID = re.search('"sessionID":"(.*?)"',str(response)).group(1)
                    var1 = {
                        "input":{
                            "content_id":TargetID,
                            "entry_point":"PROFILE_REPORT_BUTTON",
                            "location":"PROFILE_SOMEONE_ELSE",
                            "trigger_event_type":"REPORT_BUTTON_CLICKED",
                            "nt_context":None,
                            "trigger_session_id":SessionID},
                            "scale":1}
                    Data.update({
                        'fb_api_caller_class':'RelayModern',
                        'fb_api_req_friendly_name':'CometIXTFacebookContentTriggerRootQuery',
                        'variables':json.dumps(var1),
                        'server_timestamps':True,
                        'doc_id':'6769900669784116'
                    })
                    pos1 = r.post('https://www.facebook.com/api/graphql/',data=Data,headers=HeadersPost()).json()
                    Data.update({
                        'fb_api_caller_class':'RelayModern',
                        'fb_api_req_friendly_name':'CometFacebookIXTNextMutation',
                        'server_timestamps':True,
                        'doc_id':'6914576615289569'
                    })

                    context = pos1['data']['ixt_content_trigger']['screen']['view_model']['context']
                    serial  = pos1['data']['ixt_content_trigger']['screen']['view_model']['serialized_state']
                    var2 = {"input":{"frx_tag_selection_screen":{"context":context,"serialized_state":serial,"show_tag_search":False,"tags":["PROFILE_FAKE_ACCOUNT"]},"actor_id":Data['__user'],"client_mutation_id":"1"},"scale":1}
                    Data.update({'variables':json.dumps(var2)})
                    pos2 = r.post('https://www.facebook.com/api/graphql/',data=Data,headers=HeadersPost()).json()

                    context = pos2['data']['ixt_screen_next']['view_model']['context']
                    serial  = pos2['data']['ixt_screen_next']['view_model']['serialized_state']
                    var3 = {"input":{"frx_report_confirmation_screen":{"context":context,"serialized_state":serial},"actor_id":Data['__user'],"client_mutation_id":"3"},"scale":1}
                    Data.update({'variables':json.dumps(var3)})
                    pos3 = r.post('https://www.facebook.com/api/graphql/',data=Data,headers=HeadersPost()).json()

                    context = pos3['data']['ixt_screen_next']['view_model']['context']
                    serial  = pos3['data']['ixt_screen_next']['view_model']['serialized_state']
                    var4 = {"input":{"frx_post_report_process_timeline":{"context":context,"serialized_state":serial},"actor_id":Data['__user'],"client_mutation_id":"4"},"scale":1}
                    Data.update({'variables':json.dumps(var4)})
                    pos4 = r.post('https://www.facebook.com/api/graphql/',data=Data,headers=HeadersPost()).json()
                    self.PrintInfo("Success Report");sleep(1)

    def PrintInfo(self,Info):print(f"   [bold white]---> [green][[white]{Info}[green]]: [white]{len(self.Done)}/{len(self.StoreID)} Berhasil:-[green]{self.Berhasil} [white]Gagal:-[red]{self.Gagal}                      ",end='\r')

def FindAllID(Link):
    HeadersTradoisub = {"accept": "application/json, text/javascript, */*; q=0.01","accept-language": "id,id-ID;q=0.9,en;q=0.8","content-length": "49","content-type": "application/x-www-form-urlencoded; charset=UTF-8","origin": "https://id.traodoisub.com","referer": "https://id.traodoisub.com/","sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',"sec-ch-ua-mobile": "?0","sec-ch-ua-platform": "Windows","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36","x-requested-with": "XMLHttpRequest",}
    with requests.Session() as r:r.headers.update(HeadersTradoisub)
    response = r.post("https://id.traodoisub.com/api.php",data={"link":Link}).json()
    try:Result = response['id'];return(Result)
    except KeyError:return(None)

class FindID:
    def __init__(self):
        HeadersTradoisub = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "id,id-ID;q=0.9,en;q=0.8",
            "content-length": "49",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://id.traodoisub.com",
            "referer": "https://id.traodoisub.com/",
            "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }
        with requests.Session() as self.r:self.r.headers.update(HeadersTradoisub)
    def FindFacebookID(self):
        Console(width=70).print(panel('Masukan Link Akun Facebook',width=70,style='bold white',subtitle='┌─',subtitle_align='left'),justify='center')
        Link = input('   └─> ')
        Data = {"link":Link}
        response = self.r.post("https://id.traodoisub.com/api.php",data=Data)
        if '"error"' in response.text:Console(width=70).print(panel('Gagal Menemukan Akun',width=70,style='bold white'),justify='center')
        else:Console(width=70).print(panel('ID : %s'%(response['id']),width=70,style='bold white'),justify='center')
        exit()

if __name__ in ['__main__']:
    try:os.mkdir('Data')
    except:pass
    Menu()
