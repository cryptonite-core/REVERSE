""" Decompiled by Exotic Hridoy """

import os
import sys
import time
import marshal
import zlib
import base64
import cython
import compileall
import shutil

def display_banner():
    os.system('clear')
    print("""\033[1;95m
          \033[1;92m┏━━━━━━━━━━━━━━━━━━━━━━━━┓
          \033[1;92m┃ \033[1;95m┏━┓┏━┓┏┳┓┏━┓┳╻  ┏━╸ \033[1;96m𝐏\033[1;92m  ┃
          \033[1;92m┃ \033[1;95m┃  ┃ ┃┃┃┃┣━┛┃┃  ┣━╸ \033[1;96m𝐑\033[1;92m  ┃
          \033[1;92m┃ \033[1;95m┗━┛┗━┛╹ ╹╹  ┻┗━┛┗━╸ \033[1;96m𝐎\033[1;92m  ┃\033[1;92m
 ┏━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━┓
 ┃  [\033[1;91m•\033[1;92m]  CREATED BY  \033[1;93m:  \033[1;92mMUMIT ISLAM HIMU    ┃
 ┃  [\033[1;91m•\033[1;92m]  TOOLS FOR   \033[1;93m:  \033[1;92mENCRYPTOR           ┃
 ┃  [\033[1;91m•\033[1;92m]  STATUS      \033[1;93m:  \033[1;92mFREE                ┃
 ┃  [\033[1;91m•\033[1;92m]  GITHUB      \033[1;93m:  \033[1;92mMUMIT-404-CYBER     ┃
 ┃  [\033[1;91m•\033[1;92m]  FACEBOOK    \033[1;93m:  \033[1;92mMUMIT ISLAM HIMU    ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m""")

def animated_text(text):
    for char in text + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)

def loading_animation(message):
    spinner = ['/', '-', '\\', '|', '/', '-', '\\', '|', '/', '-', '\\', '|', '/', '-', '\\', '✓']
    for frame in spinner:
        sys.stdout.write(f'\r{message} {frame}')
        time.sleep(0.1)
        sys.stdout.flush()

def get_user_input(prompt):
    try:
        if sys.version_info[0] < 3:
            return raw_input(prompt)
        else:
            return input(prompt)
    except NameError:
        return input(prompt)

def encode_marshal(source_code):
    compiled = compile(source_code, '___INNOCENT-BOY___', 'exec')
    marshaled = marshal.dumps(compiled)
    header = '''# ENCODED BY : MUMIT ISLAM HIMU
# ENCRYPTION : Py3 MARSHAL
# GITHUB : https://github.com/MUMIT-404-CYBER
# ----------------------------------------------
import marshal
exec(marshal.loads('''
    footer = '))'
    return header + repr(marshaled) + footer

def encode_base64(source_code):
    encoded = base64.b64encode(source_code.encode())
    header = '''# ENCODED BY : MUMIT ISLAM HIMU
# ENCRYPTION : Py3 BASE64
# GITHUB : https://github.com/MUMIT-404-CYBER
# ----------------------------------------------
import base64
exec(base64.b64decode('''
    footer = '))'
    return header + repr(encoded) + footer

def encode_zlib(source_code):
    compressed = zlib.compress(source_code.encode(), 2)
    header = '''# ENCODED BY : MUMIT ISLAM HIMU
# ENCRYPTION : Py3 ZLIB
# GITHUB : https://github.com/MUMIT-404-CYBER
# ----------------------------------------------
import zlib
exec(zlib.decompress('''
    footer = '))'
    return header + repr(compressed) + footer

def encode_marshal_base64(source_code):
    compiled = compile(source_code, '___INNOCENT-BOY___', 'exec')
    marshaled = marshal.dumps(compiled)
    encoded = base64.b64encode(marshaled)
    header = '''# ENCODED BY : MUMIT ISLAM HIMU
# ENCRYPTION : Py3 MARSHAL+BASE64
# GITHUB : https://github.com/MUMIT-404-CYBER
# ----------------------------------------------
import marshal, base64
exec(marshal.loads(base64.b64decode('''
    footer = ')))'
    return header + repr(encoded) + footer

def encode_all_methods(source_code):
    compiled = compile(source_code, '___INNOCENT-BOY___', 'exec')
    marshaled = marshal.dumps(compiled)
    compressed = zlib.compress(marshaled)
    encoded = base64.b64encode(compressed)
    header = '''# ENCODED BY : MUMIT ISLAM HIMU
# ENCRYPTION : Py3 MARSHAL+ZLIB+B64
# GITHUB : https://github.com/MUMIT-404-CYBER
# ----------------------------------------------
import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode('''
    footer = '))))'
    return header + repr(encoded) + footer

def compile_to_pyc(source_code):
    temp_file = 'temp.py'
    with open(temp_file, 'w') as f:
        f.write(source_code)

    if sys.version_info[0] < 3:
        compileall.compile_file(temp_file)
    else:
        compileall.compile_file(temp_file, legacy=True)
    return True

def get_source_file():
    file_path = get_user_input('\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m Enter file path: \033[32m')
    print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')

    while not os.path.exists(file_path):
        print('\033[1;92m [\033[1;91m!\033[1;92m]\033[1;91m File not found!')
        print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')
        time.sleep(0.4)
        file_path = get_user_input('\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m Enter file path: \033[32m')
        print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')

    with open(file_path, 'r') as f:
        content = f.read()

    if '/' in file_path:
        filename = file_path.split('/')[-1]
    else:
        filename = file_path

    return content, filename

def save_encoded_file(encoded_content, original_filename):
    if '.py' in original_filename:
        new_filename = original_filename.replace('.py', '_enc.py')
    else:
        new_filename = original_filename + '_enc.py'

    save_path = f'/sdcard/{new_filename}'
    with open(save_path, 'w') as f:
        f.write(encoded_content)

    return save_path

def process_encoding(encoding_type):
    source_code, filename = get_source_file()

    if encoding_type != 'hard':
        loading_animation('\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m Encoding your file')
        print('\n\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')

    if encoding_type == 'marshal':
        encoded = encode_marshal(source_code)
    elif encoding_type == 'zlib':
        encoded = encode_zlib(source_code)
    elif encoding_type == 'base64':
        encoded = encode_base64(source_code)
    elif encoding_type == 'mb':
        encoded = encode_marshal_base64(source_code)
    elif encoding_type == 'all':
        encoded = encode_all_methods(source_code)
    elif encoding_type == 'hard':
        iterations = get_user_input('\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m Enter encryption strength [MAX:99]: \033[32m')
        print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')

        try:
            iterations = int(iterations)
        except ValueError:
            iterations = 1

        iterations = min(iterations, 99)

        loading_animation('\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m Encoding your file')
        print('\n\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')

        encoded_data = source_code
        for _ in range(iterations):
            encoded_data = encode_all_methods(encoded_data)

        compile_to_pyc(encoded_data)

        if '.py' in filename:
            new_filename = filename.replace('.py', '_enc.py')
        else:
            new_filename = filename + '_enc.py'

        save_path = f'/sdcard/{new_filename}'
        os.system(f'mv temp.pyc {save_path} >/dev/null 2>&1')
        os.system('rm -f temp.py > /dev/null 2>&1')

        time.sleep(1)
        print('\033[1;92m [\033[1;91m✓\033[1;92m]\033[1;97m File encoding completed!')
        print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')
        print(f'\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m File saved as: \033[32m{save_path}\033[0m')
        print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')
        get_user_input('\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m Press Enter to continue...')
        return

    save_path = save_encoded_file(encoded, filename)

    time.sleep(1)
    print('\033[1;92m [\033[1;91m✓\033[1;92m]\033[1;97m File encoding completed!')
    print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')
    print(f'\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m File saved as: \033[32m{save_path}\033[0m')
    print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')
    get_user_input('\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m Press Enter to continue...')

def main_menu():
    os.system('clear')
    os.system('pip install cython >/dev/null 2>&1')
    animated_text(' \033[1;92m[\033[1;91m•\033[1;92m]\033[1;97m Follow My GitHub Account...')
    time.sleep(0.8)
    os.system('xdg-open https://github.com/MUMIT-404-CYBER/ >/dev/null 2>&1')

    while True:
        display_banner()
        print("""
\033[1;92m [\033[1;91m1\033[1;92m]\033[1;97m Encode Marshal
\033[1;92m [\033[1;91m2\033[1;92m]\033[1;97m Encode Zlib
\033[1;92m [\033[1;91m3\033[1;92m]\033[1;97m Encode Base64
\033[1;92m [\033[1;91m4\033[1;92m]\033[1;97m Encode Marshal+Base64
\033[1;92m [\033[1;91m5\033[1;92m]\033[1;97m Encode Marshal+Zlib+Base64
\033[1;92m [\033[1;91m6\033[1;92m]\033[1;97m Advanced Encryption
\033[1;92m [\033[1;91m7\033[1;92m]\033[1;97m Compile with Cython
\033[1;92m [\033[1;91m0\033[1;92m]\033[1;97m Exit
\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-""")

        choice = get_user_input('\033[1;92m [\033[1;91m?\033[1;92m]\033[1;97m Select option: \033[32m').strip()
        print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')

        if choice == '1':
            process_encoding('marshal')
        elif choice == '2':
            process_encoding('zlib')
        elif choice == '3':
            process_encoding('base64')
        elif choice == '4':
            process_encoding('mb')
        elif choice == '5':
            process_encoding('all')
        elif choice == '6':
            process_encoding('hard')
        elif choice == '7':
            print('\033[1;92m [\033[1;91m!\033[1;92m]\033[1;96m NOTE: \033[1;93mFirst encode with Marshal, then use')
            print('            the encoded file for Cython compilation...!!')
            print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')
            file_path = get_user_input('\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m Enter encoded file: \033[32m')
            print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')

            try:
                with open(file_path, 'r') as f:
                    f.read()
            except:
                print('\033[1;92m [\033[1;91m!\033[1;92m]\033[1;91m File not found!\033[1;97m')
                print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')
                get_user_input('\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m Press Enter to continue...')
                continue

            loading_animation('\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m Compiling with Cython')
            print('\n\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')
            os.system(f'cythonize -i -3 {file_path} > /dev/null 2>&1')
            print('\033[1;92m [\033[1;91m✓\033[1;92m]\033[1;97m Cython compilation completed!')
            print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')
            get_user_input('\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m Press Enter to continue...')
        elif choice == '0':
            print('\033[1;92m [\033[1;91m•\033[1;92m]\033[1;97m Thank you for using the tool!')
            break
        else:
            print('\033[1;92m [\033[1;91m!\033[1;92m]\033[1;91m Invalid option!')
            print('\033[38;5;46m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[1;32m-\033[1;35m-\033[1;34m-\033[1;97m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[1;34m-\033[1;33m-\033[1;32m-\033[1;97m-\033[38;5;196m-\033[38;5;46m-\033[38;5;196m-\033[1;32m-\033[1;97m-\033[1;35m-\033[1;34m-\033[1;33m-\033[38;5;46m-\033[1;97m-\033[1;32m-\033[1;33m-\033[38;5;196m-\033[1;35m-\033[38;5;196m-\033[38;5;46m-')
            time.sleep(1)

if __name__ == '__main__':
    main_menu()
