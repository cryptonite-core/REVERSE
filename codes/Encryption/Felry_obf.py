""" Decompiled by Exotic Hridoy """

import sys
import os
import random
from pystyle import*
import marshal as marshal
import base64
import time

def clear():
    if "linux" in sys.platform.lower():
        os.system("clear")
    elif "win" in sys.platform.lower():
        os.system("cls")
k="[1;33m"  # Warna Kuning
a="[1;30m"  # Warna Hitam/Abu-Abu
m="[1;31m"  # Warna Merah
h="[1;32m"  # Warna Hijau
p="[1;37m"  # Warna Putih
b="[1;34m"  # Warna Biru
v="[1;35m"  # Warna Violet
u="[1;36m"  # Warna Ungu
j="[1;38;5;202m"  # Warna Jingga

class Hyperion():
    serializer=marshal
    def Alt(text:str,evalCode:bool=True)->str:
        formated="+".join(f'chr({char})'for char in[ord(char_)for char_ in text])
        return f'eval(eval({formated!r}))'if evalCode else f'eval({formated!r})'
    hhidedText="GG! You deobfuscated the code! obfuscated by Hyperion"
    exceptionCode="input(\"Don't try to skid Hyperion obfuscation !\");exit(0)"
    GithubLink="https://github.com/ferlyafriliyan/Hyperion"
    infos={
        "__author__":"Ferly Afriliyan",
        "__madeBy__":"Hyperion",
        "__git__":GithubLink,
}
    gatewayKey=random.randint(0,10000)

    def Gateway()->str:
        obj=globals()["__selfObject__"]
        interpreterObj=globals()["__InterpreterObject__"]
        key=globals()["__key__"]
        code=interpreterObj.code["bytes"]
        obj.executed=True
        return((key*8/1.5),code)
    comment="Obfuscated with Hyperion"
    encCommend=" + ".join(f'chr({char})'for char in[ord(char_)for char_ in comment])
    checkInfos=" and ".join(f'globals().get("{key}") == {value!r}'for key,value in infos.items())+\
        f' and ("# " and {encCommend}) in open(__import__("os").path.abspath(__file__), "r", encoding = "utf-8").read() '
    interpreterClass="\nclass Interpreter():\n    def __init__(self, code: str, layersFunction: bytes, module, globals_, backend: bytes = b'') -> None:\n        self.__module = module\n        self.layersFunction = layersFunction\n        self.__globals = globals_\n        self.code = {'bytes': code, 'str': str(code)}\n        self.__backend = backend\n\n    def __tunnel(self) -> Gateway: return Gateway(self.__backend, 7605, __module = self.__module, __globals = self.__globals, interpreter = self)\n\n    def Run(self) -> None:\n        decoder = self.__getobject__()\n        gate = self.__tunnel().Pass()\n        exec(eval(MARSHALMODULE.loads(decoder),\n                  {'__selfObject__': self, '__module': self.__module, '__sr_m': eval(eval('chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(109)+chr(97)+chr(114)+chr(115)+chr(104)+chr(97)+chr(108)+chr(34)+chr(41)')), '__globals': self.__globals, 'gate': gate}),\n                  self.__globals)\n\n    def __getobject__(self) -> object:\n        func = self.layersFunction\n        return self.__module.b64decode(func)\n        "[1:-1].replace("MARSHALMODULE",Alt("__import__(\"marshal\")")).replace("GATEWAYKEY",str(gatewayKey))
    gatewayClass="\nclass Gateway():\n    def __init__(self, way: bytes, key: int, **ext) -> None:\n        self.way = way\n        self.key = key\n        self.module__ = ext.get('__module', None)\n        self.__globals = ext.get('__globals', None)\n        self.__module = ext.get('__module', None)\n        self.__interpreter = ext.get('interpreter', None)\n\n    def Pass(self):\n        exec(MARSHALMODULE.loads(self.module__.b16decode(self.way)),\n             {'__selfObject__': self, '__key__': self.key, '__module': self.module__, '__globals': self.__globals, '__InterpreterObject__': self.__interpreter})\n        return self\n    "[1:-1].replace("MARSHALMODULE",Alt("__import__(\"marshal\")"))

    def RemoveLayers()->str:
        _globals=globals()["__globals"]
        if not globals().get("gate"):
            return
        obj=globals()["__selfObject__"]
        module=globals()["__module"]
        code=obj.code["bytes"]
        code=module.b85decode(code)
        code=module.b64decode(code)
        code=module.b32decode(code)
        code=module.b16decode(code)
        code=globals()["__sr_m"].loads(code)
        return code

    def Obfuscate(code:str)->str:
        sys.setrecursionlimit(1000000)
        _code=code
        program="{'__name__': '__main__'}"
        runCode=f"""
if not ({Hyperion.checkInfos}): {Hyperion.exceptionCode}
exec({_code!r}, {program})
"""[1:-1]
        code__=Hyperion.serializer.dumps(compile(runCode,"Hyperion","exec"))
        infos_="\n".join(f'{key} = {value!r}'for key,value in Hyperion.infos.items())
        code__=base64.b16encode(code__)
        code__=base64.b32encode(code__)
        code__=base64.b64encode(code__)
        code__=base64.b85encode(code__)
        code_=f"""
{infos_}

# {Hyperion.comment}
import marshal, base64
{Hyperion.gatewayClass}
{Hyperion.interpreterClass}

if __name__ == '__main__':
    try:
        Interpreter({code__!r},
            {base64.b64encode(Hyperion.serializer.dumps(Hyperion.RemoveLayers.__code__))!r},
            {Hyperion.Alt('__import__("base64")')}, globals(),
            {base64.b16encode(Hyperion.serializer.dumps(Hyperion.Gateway.__code__))!r}
        ).Run()
    except (KeyboardInterrupt, Exception) as e:
        exit(f"[Error] {{str(e).capitalize()}}!")
# Lu Kontool
"""[1:-1]
        return code_

colors=Col.red_to_purple
input_=0.01
interval=0.1
banner="\n██╗  ██╗██╗   ██╗██████╗ ███████╗██████╗ ██╗ ██████╗ ███╗   ██╗\n██║  ██║╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██║██╔═══██╗████╗  ██║\n███████║ ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║██║   ██║██╔██╗ ██║\n██╔══██║  ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗██║██║   ██║██║╚██╗██║\n██║  ██║   ██║   ██║     ███████╗██║  ██║██║╚██████╔╝██║ ╚████║\n╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n"[:-1]

def Main():
    whiteChars=list("═╝╚╔╗║")
    print(Colorate.Format(banner,whiteChars,Colorate.Vertical,colors,Col.white))
    path=input(f"{m}Drag and drop the file to obfuscate => {p}")
    path=os.path.normpath(path)
    if not os.path.exists(path):
        Colorate.Error("File not found.")
        time.sleep(input_)
        exit()
    if not os.path.isfile(path):
        print("Not a file. !")
        time.sleep(interval)
        exit()
    output_filename=input(f"{m}Enter the output file name ({u}including {p}'{b}.py{p}' {u}extension): {p}")
    time.sleep(input_)
    code=""
    print(f"{k}[{a}!{k}] {p}WARN: The __name__ variable will be set to '__main__'. Press Enter to continue...")
    time.sleep(0.1)
    with open(path,"r",encoding="utf-8")as file:
        code=file.read()
    code=Hyperion.Obfuscate(code)
    with open(output_filename,"w",encoding="utf-8")as file:
        file.write(code)
    print(f"{h}[{a}!{h}] {p}Successfully obfuscated and saved to {j}{output_filename}{p}!")
    time.sleep(0.01)
    exit()
if __name__=="__main__":
    System.Title("Hyperion - By Ferly Afriliyan_")
    System.Size(150,47)
    try:
        Main()
    except(KeyboardInterrupt,Exception)as e:
        exit(f"[Error] {str(e).capitalize()}!")
