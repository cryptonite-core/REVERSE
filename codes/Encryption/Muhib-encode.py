""" Decompiled by Exotic Hridoy """

import os
import sys
import zlib
import time
import base64
import marshal
import py_compile

if sys.version_info[0] == 2:
    _input = 'raw_input(\'%s\')'
elif sys.version_info[0] == 3:
    _input = 'input(\'%s\')'
else:
    sys.exit('\n Your Python Version is not Supported!')

zlb = lambda in_: zlib.compress(in_)
b16 = lambda in_: base64.b16encode(in_)
b32 = lambda in_: base64.b32encode(in_)
b64 = lambda in_: base64.b64encode(in_)
mar = lambda in_: marshal.dumps(compile(in_, '<x>', 'exec'))
note = f'# Obfuscated with PyObfuscate\n# https://www.github.com/htr-tech\n# Time : {time.ctime()}\n# -------------------------------\n'

def banner():
    print('\033[1;92m   ███    ███\033[1;93m ██     ██\033[38;5;208m ██   ██\033[1;97m ██\033[1;91m ██████')
    print('\033[1;92m   ████  ████\033[1;93m ██     ██\033[38;5;208m ██   ██\033[1;97m ██\033[1;91m ██   ██')
    print('\033[1;92m   ██ ████ ██\033[1;93m ██     ██\033[38;5;208m ███████\033[1;97m ██\033[1;91m ██████')
    print('\033[1;92m   ██  ██  ██\033[1;93m ██     ██\033[38;5;208m ██   ██\033[1;97m ██\033[1;91m ██   ██')
    print('\033[1;92m   ██      ██\033[1;93m █████████\033[38;5;208m ██   ██\033[1;97m ██\033[1;91m ██████\033[0;m')
    print('\033[1;96m╔══\033[1;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;92m')
    print('\033[1;96m╠══\033[1;91m[>] \033[1;96mDEVOLPER\033[1;92m--------------------\033[1;96mMH-MUHIB')
    print('\033[1;96m╠══\033[1;91m[>] \033[1;92mFACEBOOK\033[1;96m--------------------\033[1;92m/its.muhib.7')
    print('\033[1;96m╠══\033[1;91m[>] \033[1;93mGITHUB\033[1;92m----------------------\033[1;93mMUHIB-143')
    print('\033[1;96m╠══\033[1;91m[>] \033[1;95mTOOLS\033[1;96m-----------------------\033[1;95mPYTHON ENCODE')
    print('\033[1;96m╚══\033[1;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;92m\n')

def menu():
    print('\033[1;92m[01] MARSHAL')
    print('\033[1;92m[02] ZLIB')
    print('\033[1;92m[03] BASE16')
    print('\033[1;92m[04] BASE32')
    print('\033[1;92m[05] BASE64')
    print('\033[1;92m[06] ZLIB + BASE16')
    print('\033[1;92m[07] ZLIB + BASE32')
    print('\033[1;92m[08] ZLIB + BASE64')
    print('\033[1;92m[09] MARSHAL + ZLIB')
    print('\033[1;92m[10] MARSHAL + BASE16')
    print('\033[1;92m[11] MARSHAL + BASE32')
    print('\033[1;92m[12] MARSHAL + BASE64')
    print('\033[1;92m[13] MARSHAL + ZLIB + BASE16')
    print('\033[1;92m[14] MARSHAL + ZLIB + BASE32')
    print('\033[1;92m[15] MARSHAL + ZLIB + BASE64')
    print('\033[1;92m[16] SUPER ENCODE')
    print('\033[1;92m[17] EXIT\n')

class FileSize:
    def datas(self, z):
        for x in ['Byte', 'KB', 'MB', 'GB']:
            if z < 1024.0:
                return '%3.1f %s' % (z, x)
            z = z / 1024.0

    def __init__(self, path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(' \033[1;91m[>] \033[1;97mENC FILE SIZE : \033[1;92m%s\n' % self.datas(dts))

def Encode(option, data, output):
    try:
        loop = int(eval(_input % ' [-] Encode Count : '))
    except:
        loop = 1

    if option == 1:
        xx = 'mar(data.encode(\'utf8\'))[::-1]'
        heading = '_ = lambda __ : __import__(\'marshal\').loads(__[::-1]);'
    elif option == 2:
        xx = 'zlb(data.encode(\'utf8\'))[::-1]'
        heading = '_ = lambda __ : __import__(\'zlib\').decompress(__[::-1]);'
    elif option == 3:
        xx = 'b16(data.encode(\'utf8\'))[::-1]'
        heading = '_ = lambda __ : __import__(\'base64\').b16decode(__[::-1]);'
    elif option == 4:
        xx = 'b32(data.encode(\'utf8\'))[::-1]'
        heading = '_ = lambda __ : __import__(\'base64\').b32decode(__[::-1]);'
    elif option == 5:
        xx = 'b64(data.encode(\'utf8\'))[::-1]'
        heading = '_ = lambda __ : __import__(\'base64\').b64decode(__[::-1]);'
    elif option == 6:
        xx = 'b16(zlb(data.encode(\'utf8\')))[::-1]'
        heading = '_ = lambda __ : __import__(\'zlib\').decompress(__import__(\'base64\').b16decode(__[::-1]));'
    elif option == 7:
        xx = 'b32(zlb(data.encode(\'utf8\')))[::-1]'
        heading = '_ = lambda __ : __import__(\'zlib\').decompress(__import__(\'base64\').b32decode(__[::-1]));'
    elif option == 8:
        xx = 'b64(zlb(data.encode(\'utf8\')))[::-1]'
        heading = '_ = lambda __ : __import__(\'zlib\').decompress(__import__(\'base64\').b64decode(__[::-1]));'
    elif option == 9:
        xx = 'zlb(mar(data.encode(\'utf8\')))[::-1]'
        heading = '_ = lambda __ : __import__(\'marshal\').loads(__import__(\'zlib\').decompress(__[::-1]));'
    elif option == 10:
        xx = 'b16(mar(data.encode(\'utf8\')))[::-1]'
        heading = '_ = lambda __ : __import__(\'marshal\').loads(__import__(\'base64\').b16decode(__[::-1]));'
    elif option == 11:
        xx = 'b32(mar(data.encode(\'utf8\')))[::-1]'
        heading = '_ = lambda __ : __import__(\'marshal\').loads(__import__(\'base64\').b32decode(__[::-1]));'
    elif option == 12:
        xx = 'b64(mar(data.encode(\'utf8\')))[::-1]'
        heading = '_ = lambda __ : __import__(\'marshal\').loads(__import__(\'base64\').b64decode(__[::-1]));'
    elif option == 13:
        xx = 'b16(zlb(mar(data.encode(\'utf8\'))))[::-1]'
        heading = '_ = lambda __ : __import__(\'marshal\').loads(__import__(\'zlib\').decompress(__import__(\'base64\').b16decode(__[::-1])));'
    elif option == 14:
        xx = 'b32(zlb(mar(data.encode(\'utf8\'))))[::-1]'
        heading = '_ = lambda __ : __import__(\'marshal\').loads(__import__(\'zlib\').decompress(__import__(\'base64\').b32decode(__[::-1])));'
    elif option == 15:
        xx = 'b64(zlb(mar(data.encode(\'utf8\'))))[::-1]'
        heading = '_ = lambda __ : __import__(\'marshal\').loads(__import__(\'zlib\').decompress(__import__(\'base64\').b64decode(__[::-1])));'
    else:
        sys.exit('\n Invalid Option!')

    for x in range(loop):
        try:
            data = 'exec((_)(%s))' % repr(eval(xx))
        except TypeError as s:
            sys.exit(' TypeError : ' + str(s))

    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()

def SEncode(data, output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = 'exec(__import__(\'marshal\').loads(__import__(\'zlib\').decompress(__import__(\'base64\').b64decode(%s[::-1]))))' % method

    z = []
    for i in data:
        z.append(ord(i))

    sata = '_ = %s\nexec(\'\'.join(chr(__) for __ in _))' % z

    with open(output, 'w') as f:
        f.write(note)
        f.write(sata)
        f.close()

    py_compile.compile(output, output)

def MainMenu():
    try:
        os.system('clear')
        banner()
        menu()

        try:
            option = int(eval(_input % ' \033[1;97m[>]\033[1;92m SELECT OPTION : \033[1;97m'))
        except:
            sys.exit('\n Invalid Option !')

        if option > 0 and option <= 17:
            if option == 17:
                sys.exit('\n Thanks For Using this Tool')

            os.system('clear')
            banner()

            try:
                file = eval(_input % ' \033[1;97m[>]\033[1;92m FILE PATH  : \033[1;97m')
                data = open(file).read()
            except:
                sys.exit('\n FILE NOT FOUND !')

            output = file.lower().replace('.py', '') + '_enc.py'

            if option == 16:
                SEncode(data, output)
            else:
                Encode(option, data, output)

            print('\n \033[1;91m[>] \033[1;97mENCODE-ED\033[1;92m  %s' % file)
            print(' \033[1;91m[>] \033[1;97mSAVED AS\033[1;92m  %s' % output)
            FileSize(output)
        else:
            sys.exit('\n Invalid Option !')

    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == '__main__':
    MainMenu()
