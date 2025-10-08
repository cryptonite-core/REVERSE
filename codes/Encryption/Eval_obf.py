""" Decompiled by Exotic Hridoy """

import os
import time,sys
import base64
import marshal
import zlib
import platform
import datetime
import random
from random import randint
from rich.panel import Panel
from rich import print as tulis
from rich import print

Hitam="[30m"
Merah="[31m"
Hijau="[32m"
Kuning="[33m"
Orange="[38;5;208m"
Biru="[34m"
Biru_muda="[36m"
Pink="[38;5;205m"
Violet="[35m"
Abu="[90m"
Orange_muda="[38;5;214m"
Putih="[37m"

Z2="[#000000]"  # Hitam
M2="[#FF0000]"  # Merah
H2="[#00FF00]"  # Hijau
K2="[#FFFF00]"  # Kuning
B2="[#00C8FF]"  # Biru
U2="[#AF00FF]"  # Ungu
N2="[#FF00FF]"  # Pink
O2="[#00FFFF]"  # Biru Muda
P2="[#FFFFFF]"  # Putih
J2="[#FF8F00]"  # Jingga
A2="[#AAAAAA]"  # Abu-Abu
T2="[#FFA500]"  # Oranye

def clear():
    if "linux" in sys.platform.lower():
        os.system("clear")
    elif "win" in sys.platform.lower():
        os.system("cls")# clear()

class LambdaObfuscators:
    def __init__(self):
        current_time=datetime.datetime.now()
        current_time_str=current_time.strftime("%A, %B %d, %Y %H:%M:%S")
        self.mzb=f'''# Time : {current_time_str}
# Platform : {platform.system()}-{platform.machine()}
# Obfuscated by : Ferly Afriliyan (Ryougaa Hideki)

Ryougaa_ = (\n'''
        denventa_lines=[f'"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000", {str(["import", "as", "from", "marshal", "zlib", "base64"])}, "Ryougaa_Hidekii__=(eval((lambda", "exec(", ";exec(Ryougaa_Hidekii__)"'for _ in range(140,1409)]
        self.mzb+=",\n".join(denventa_lines)
        self.mzb+=f'''\n)

# Time : {current_time_str}
# Platform : {platform.system()}-{platform.machine()}
# Obfuscated by : Ferly Afriliyan (Ryougaa Hideki)
# Variable teks : {len(denventa_lines)} Line


recode_kontol = %s;Ryougaa_Hidekii__=(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(recode_kontol));exec(Ryougaa_Hidekii__)

Hidekii_ = (\n'''
        denventa_lines=[f'"000000000000000","000000000000000","000000000000000","000000000000000","000000000000000", {str(["import", "as", "from", "marshal", "zlib", "base64"])}, "Ryougaa_Hidekii__=(eval((lambda", "exec(", ";exec(Ryougaa_Hidekii__)"'for _ in range(140,1409)]
        self.mzb+=",\n".join(denventa_lines)
        self.mzb+=f'''\n)'''

    def encrypt_file(self,input_file,output_file,count):
        try:
            __obf=open(input_file,"rb").read()
            __com=compile(__obf,"","exec")
            __repr__=repr(marshal.dumps(__com))
            with open(output_file,"w")as f:
                f.write(self.mzb % __repr__)
            total_iterations=count
            current_iteration=0
            while current_iteration<total_iterations:
                obf__=open(output_file,"rb").read()
                ___compile__=compile(obf__,"","exec")
                ___repr_compile___=repr(marshal.dumps(___compile__))
                with open(output_file,"w")as f:
                    f.write(self.mzb % ___repr_compile___)
                current_iteration+=1
                loading_percentage=(current_iteration/total_iterations)*100
                print(f"Encrypting: [{loading_percentage:.2f}%]",end="\r")
                time.sleep(0.0)
            print(f"\n{H2}[{A2}!!{H2}]{P2} Berhasil, File tersimpan di {A2}: {output_file}")
            exit()
        except Exception as e:
            print(f"{M2}[{A2}•{M2}]{P2} Error : {P2}\n└──>{M2}[{A2}•{M2}] {P2}Isi Yang Benar {M2}!")

if __name__=="__main__":
    encryptor=LambdaObfuscators()
    clear()
    tulis(Panel("[#00BFFF]    ╔═╗┬  ┬┌─┐┬   ┌─┐┌┐ ┌─┐[#808080]Python3 with lambda[#00BFFF]\n    ║╣ └┐┌┘├─┤│───│ │├┴┐├┤\n    ╚═╝ └┘ ┴ ┴┴─┘ └─┘└─┘└ \n        ",title="[#FF8F00][ [#00FF33]By Ferly Afriliyan [#FF8F00]]",
        subtitle="[#FF8F00][ [#00FF33]Obfuscate Your Python File [#FF8F00]]",style="#FFFFFF"))
    input_file=input(f"└──>{Hijau}[{Abu}•{Hijau}]{Putih} Input File {Abu}: {Putih}")
    count=int(input(f"     └──>{Biru}[{Abu}+{Biru}]{Putih} Count {Orange_muda}({Putih}Ex{Orange_muda}) •4• : {Putih}"))
    if count<11:
        output_file=input(f"     └──>{Hijau}[{Abu}•{Hijau}]{Putih} Output File {Abu}: {Putih}")
        encryptor.encrypt_file(input_file,output_file,count)
    else:
        print(f"{B2}[{A2}!{B2}]{P2} Count must be < 10")
