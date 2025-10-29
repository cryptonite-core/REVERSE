""" Decompiled by Exotic Hridoy """

import sys
import os
import subprocess
import base64
import marshal
import zlib
import lzma
import bz2
import binascii
import gzip
import pickle
import codecs
import aiofiles
import asyncio
import pyfiglet
from typing import Union
import tempfile
import shutil
from shutil import which
from colorama import init, Fore, Style
from tqdm import tqdm
from datetime import datetime
import time
import requests
import pytz
import glob
import shlex
import re
import textwrap
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# Init Colorama
init(autoreset=True)

# ============================== Helpers ==============================


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


async def save_file_py(code_block: str, method: str, original_name: str) -> str:
    """
    Simpan satu file .py yang runnable (runner+payload) ke:
    results/<method>/<base>_encode.py
    """
    base = os.path.splitext(os.path.basename(original_name))[0]
    out_dir = os.path.join("results", method)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{base}_encode.py")
    try:
        async with aiofiles.open(out_path, "w", encoding="utf-8") as f:
            await f.write(code_block.strip() + "\n")
        return out_path
    except Exception as e:
        print(Fore.RED + f"Failed to save file: {e}")
        return ""


def get_local_time_from_ip():
    try:
        res = requests.get("https://ipapi.co/json/", timeout=5)
        data = res.json()
        tz_name = data.get("timezone", "UTC")
        timezone = pytz.timezone(tz_name)
        now = datetime.now(timezone)
        offset = now.strftime("%z")
        formatted_offset = f"UTC{offset[:3]}:{offset[3:]}"
        formatted_time = now.strftime("%d-%m-%y %H:%M") + f" {formatted_offset}"
        return tz_name, formatted_time
    except Exception:
        now = datetime.utcnow()
        return "UTC", now.strftime("%d-%m-%y %H:%M UTC+00:00")


def print_banner_with_timezone():
    _, time_str = get_local_time_from_ip()
    print(Fore.WHITE + "-" * 60)
    print(
        Fore.LIGHTMAGENTA_EX
        + f"{Fore.LIGHTWHITE_EX}(+){Fore.LIGHTWHITE_EX} Author: Kiansantang DEV"
    )
    print(
        Fore.LIGHTMAGENTA_EX
        + f"{Fore.LIGHTWHITE_EX}(+){Fore.LIGHTWHITE_EX} Timezone: {Fore.LIGHTWHITE_EX}{time_str}"
    )
    print(Fore.WHITE + "-" * 60, "\n")


def print_banner():
    ascii_banner = pyfiglet.figlet_format("Xan-Encoder")
    print(Fore.CYAN + Style.BRIGHT + ascii_banner)


# ============================== Config ==============================

HEX_EMOJI_MAP = {
    "0": "😀",
    "1": "😁",
    "2": "😂",
    "3": "🤣",
    "4": "😃",
    "5": "😄",
    "6": "😅",
    "7": "😆",
    "8": "😉",
    "9": "😊",
    "a": "😋",
    "b": "😎",
    "c": "😍",
    "d": "😘",
    "e": "😗",
    "f": "😙",
}


def hex_to_emoji(hex_str):
    return "".join(HEX_EMOJI_MAP.get(c, "") for c in hex_str.lower())


MAX_LAYERS = 100
THREADS = 25

# ============================== Encoders (inner+wrap) ==============================
# Prinsip layering untuk semua 1–23:
# - Untuk metode murni string (1,2,3,5,6,7,8,9,16): setiap layer pakai transform yg sama (wrap==inner).
# - Untuk metode berbasis marshal (10–15,17–23):
#     * Layer-1 (inner): compile -> marshal -> (compress) -> (encode)
#     * Layer-2..L (wrap): hanya bungkus string s dengan (compress)->(encode) TANPA marshal/compile ulang
# - Runner: lakukan (wrap-decode) sebanyak L-1 kali, lalu langkah final melakukan inner-decode ke code object (marshal.loads) dan exec.

# ---------- Methods (1,2,3,5,6,7,8,9,16): inner == wrap ----------


def inner_rot13(s):
    return codecs.encode(s, "rot_13")


def wrap_rot13(s):
    return codecs.encode(s, "rot_13")


def inner_zlib_hex(s):
    return zlib.compress(s.encode()).hex()


def wrap_zlib_hex(s):
    return zlib.compress(s.encode()).hex()


def inner_gzip_hex(s):
    return gzip.compress(s.encode()).hex()


def wrap_gzip_hex(s):
    return gzip.compress(s.encode()).hex()


def inner_base85(s):
    return base64.a85encode(s.encode()).decode()


def wrap_base85(s):
    return base64.a85encode(s.encode()).decode()


def inner_base16(s):
    return base64.b16encode(s.encode()).decode()


def wrap_base16(s):
    return base64.b16encode(s.encode()).decode()


def inner_base64(s):
    return base64.b64encode(s.encode()).decode()


def wrap_base64(s):
    return base64.b64encode(s.encode()).decode()


def inner_base32(s):
    return base64.b32encode(s.encode()).decode()


def wrap_base32(s):
    return base64.b32encode(s.encode()).decode()


def inner_xor_base64(s):
    key = 23
    return base64.b64encode(bytes([b ^ key for b in s.encode()])).decode()


def wrap_xor_base64(s):
    key = 23
    return base64.b64encode(bytes([b ^ key for b in s.encode()])).decode()


def inner_b32_binascii(s):
    return binascii.b2a_hex(base64.b32encode(s.encode())).decode()


def wrap_b32_binascii(s):
    return binascii.b2a_hex(base64.b32encode(s.encode())).decode()


# ---------- Methods (marshal-based): inner (marshal+...) + wrap (tanpa marshal) ----------


def inner_marshal_gzip_hex(src):
    code_obj = compile(src, "<string>", "exec")
    return gzip.compress(marshal.dumps(code_obj)).hex()


def wrap_marshal_gzip_hex(s):  # gzip-hex string
    return gzip.compress(s.encode()).hex()


def inner_marshal_zlib_hex(src):
    code_obj = compile(src, "<string>", "exec")
    return zlib.compress(marshal.dumps(code_obj)).hex()


def wrap_marshal_zlib_hex(s):
    return zlib.compress(s.encode()).hex()


def inner_marshal_b16(src):
    code_obj = compile(src, "<string>", "exec")
    return base64.b16encode(marshal.dumps(code_obj)).decode()


def wrap_marshal_b16(s):
    return base64.b16encode(s.encode()).decode()


def inner_marshal_b64(src):
    code_obj = compile(src, "<string>", "exec")
    return base64.b64encode(marshal.dumps(code_obj)).decode()


def wrap_marshal_b64(s):
    return base64.b64encode(s.encode()).decode()


def inner_marshal_b85(src):
    code_obj = compile(src, "<string>", "exec")
    return base64.a85encode(marshal.dumps(code_obj)).decode()


def wrap_marshal_b85(s):
    return base64.a85encode(s.encode()).decode()


def inner_pickle_b64(src):
    return base64.b64encode(pickle.dumps(src.encode())).decode()


def wrap_pickle_b64(s):
    return base64.b64encode(s.encode()).decode()


def inner_marshal_lzma_b64(src):
    code_obj = compile(src, "<string>", "exec")
    return base64.b64encode(lzma.compress(marshal.dumps(code_obj))).decode()


def wrap_marshal_lzma_b64(s):
    return base64.b64encode(lzma.compress(s.encode())).decode()


def inner_marshal_zlib_b16(src):
    code_obj = compile(src, "<string>", "exec")
    return base64.b16encode(zlib.compress(marshal.dumps(code_obj))).decode()


def wrap_marshal_zlib_b16(s):
    return base64.b16encode(zlib.compress(s.encode())).decode()


def inner_marshal_zlib_b64(src):
    code_obj = compile(src, "<string>", "exec")
    return base64.b64encode(zlib.compress(marshal.dumps(code_obj))).decode()


def wrap_marshal_zlib_b64(s):
    return base64.b64encode(zlib.compress(s.encode())).decode()


def inner_marshal_zlib_b32(src):
    code_obj = compile(src, "<string>", "exec")
    return base64.b32encode(zlib.compress(marshal.dumps(code_obj))).decode()


def wrap_marshal_zlib_b32(s):
    return base64.b32encode(zlib.compress(s.encode())).decode()


def inner_b64_marshal_zlib_lzma(src):
    code_obj = compile(src, "<string>", "exec")
    b = marshal.dumps(code_obj)
    b = zlib.compress(b)
    b = lzma.compress(b)
    return base64.b64encode(b).decode()


def wrap_b64_zlib_lzma(s):
    b = s.encode()
    b = zlib.compress(b)
    b = lzma.compress(b)
    return base64.b64encode(b).decode()


def inner_b64_marshal_lzma_zlib(src):
    code_obj = compile(src, "<string>", "exec")
    b = marshal.dumps(code_obj)
    b = lzma.compress(b)
    b = zlib.compress(b)
    return base64.b64encode(b).decode()


def wrap_b64_lzma_zlib(s):
    b = s.encode()
    b = lzma.compress(b)
    b = zlib.compress(b)
    return base64.b64encode(b).decode()


def inner_b64_marshal_bz2_zlib(src):
    code_obj = compile(src, "<string>", "exec")
    b = marshal.dumps(code_obj)
    b = bz2.compress(b)
    b = zlib.compress(b)
    return base64.b64encode(b).decode()


def wrap_b64_bz2_zlib(s):
    b = s.encode()
    b = bz2.compress(b)
    b = zlib.compress(b)
    return base64.b64encode(b).decode()


# ---------- Method 4 (pyc emoji): inner only (tidak masuk multilayer by design) ----------
def inner_pyc_emoji(src):
    code_obj = compile(src, "<string>", "exec")
    return hex_to_emoji(marshal.dumps(code_obj).hex())


# ============================== Encoder dispatch ==============================

# Map choice -> (inner_func, wrap_func, method_name)
ENCODER_TABLE = {
    1: (inner_rot13, wrap_rot13, "rot13"),
    2: (inner_zlib_hex, wrap_zlib_hex, "zlib"),
    3: (inner_gzip_hex, wrap_gzip_hex, "gzip"),
    4: (inner_pyc_emoji, None, "pyc_emoji"),  # khusus
    5: (inner_base85, wrap_base85, "base85"),
    6: (inner_base16, wrap_base16, "base16"),
    7: (inner_base64, wrap_base64, "base64"),
    8: (inner_base32, wrap_base32, "base32"),
    9: (inner_xor_base64, wrap_xor_base64, "xor_base64"),
    10: (inner_marshal_gzip_hex, wrap_marshal_gzip_hex, "marshal_gzip"),
    11: (inner_marshal_zlib_hex, wrap_marshal_zlib_hex, "marshal_zlib"),
    12: (inner_marshal_b16, wrap_marshal_b16, "marshal_base16"),
    13: (inner_marshal_b64, wrap_marshal_b64, "marshal_base64"),
    14: (inner_marshal_b85, wrap_marshal_b85, "marshal_base85"),
    15: (inner_pickle_b64, wrap_pickle_b64, "pickle_base64"),
    16: (inner_b32_binascii, wrap_b32_binascii, "base32_binascii"),
    17: (inner_marshal_lzma_b64, wrap_marshal_lzma_b64, "marshal_lzma_base64"),
    18: (inner_marshal_zlib_b16, wrap_marshal_zlib_b16, "marshal_zlib_base16"),
    19: (inner_marshal_zlib_b64, wrap_marshal_zlib_b64, "marshal_zlib_base64"),
    20: (inner_marshal_zlib_b32, wrap_marshal_zlib_b32, "marshal_zlib_base32"),
    21: (inner_b64_marshal_zlib_lzma, wrap_b64_zlib_lzma, "base64_marshal_zlib_lzma"),
    22: (inner_b64_marshal_lzma_zlib, wrap_b64_lzma_zlib, "base64_marshal_lzma_zlib"),
    23: (inner_b64_marshal_bz2_zlib, wrap_b64_bz2_zlib, "base64_marshal_bz2_zlib"),
}

# ============================== Multilayer encoding (threads + progress) ==============================


def encode_multilayer(choice: int, source: str, layers: int):
    """
    Semua metode 1–23 dilayer:
      - layer1: inner_func(source)
      - layer2..L: wrap_func(string) berulang
    Pakai ThreadPoolExecutor(15) untuk offload tiap step (dependensial, tetap sequential by result),
    progress bar animasi via tqdm.
    """
    if layers < 1:
        layers = 1
    if layers > MAX_LAYERS:
        layers = MAX_LAYERS
    entry = ENCODER_TABLE.get(choice)
    if not entry:
        return None, None, 1
    inner, wrap, method = entry

    # khusus method 4 (pyc_emoji) -> tidak wrap (layer=1)
    if choice == 4:
        out = inner(source)
        return out, method, 1

    # layer 1
    out = inner(source)
    if layers == 1 or wrap is None:
        return out, method, 1

    current = out
    with ThreadPoolExecutor(max_workers=THREADS) as ex:
        with tqdm(
            total=layers - 1,
            desc="Layering",
            ncols=70,
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
        ) as pbar:
            for _ in range(layers - 1):
                fut = ex.submit(wrap, current)
                current = fut.result()
                pbar.update(1)
    return current, method, layers


# ============================== Runner generator (1 file) ==============================


def runner_header(layers: int) -> str:
    return f"""# Encrypted : Kiansantang DEV
# Time Encrypted: {datetime.now().strftime('%d-%m-%y %H:%M %p')}
# Telegram : t.me/xqndrs66 && t.me/xqndrs
# Github : github.com/KianSantang777
"""


def _encoded_int_expr(n: int) -> str:
    token = base64.b64encode(str(n).encode()).decode()
    return f"int(__import__('base64').b64decode('{token}').decode())"


def generate_runner(choice: int, payload: str, layers: int) -> str:
    h = runner_header(layers)

    def loop(body: str) -> str:
        return (
            "for _ in range(layers-1):\n" + textwrap.indent(body.strip(), "    ") + "\n"
        )

    imports = {
        1: (
            "import codecs\n",
            "exec(codecs.decode(s, 'rot_13'))\n",
            "s = codecs.decode(s, 'rot_13')",
        ),
        2: (
            "import zlib, base64\n",
            "exec(zlib.decompress(base64.b64decode(s)).decode('utf-8'))\n",
            "s = zlib.decompress(base64.b64decode(s)).decode('utf-8')",
        ),
        3: (
            "import gzip, base64\n",
            "exec(gzip.decompress(base64.b64decode(s)).decode('utf-8'))\n",
            "s = gzip.decompress(base64.b64decode(s)).decode('utf-8')",
        ),
        4: (None, None, None),
        5: (
            "import base64\n",
            "exec(base64.a85decode(s).decode('utf-8'))\n",
            "s = base64.a85decode(s).decode('utf-8')",
        ),
        6: (
            "import base64\n",
            "exec(base64.b16decode(s.encode()).decode('utf-8'))\n",
            "s = base64.b16decode(s.encode()).decode('utf-8')",
        ),
        7: (
            "import base64\n",
            "exec(base64.b64decode(s.encode()).decode('utf-8'))\n",
            "s = base64.b64decode(s.encode()).decode('utf-8')",
        ),
        8: (
            "import base64\n",
            "exec(base64.b32decode(s.encode()).decode('utf-8'))\n",
            "s = base64.b32decode(s.encode()).decode('utf-8')",
        ),
        9: (
            "import base64\n",
            "exec(bytes([b^key for b in raw]).decode('utf-8'))\n",
            "raw = base64.b64decode(s)\ns = bytes([b ^ key for b in raw]).decode('utf-8')",
        ),
        10: (
            "import marshal, gzip, base64\n",
            "exec(marshal.loads(gzip.decompress(base64.b64decode(s))))\n",
            "s = gzip.decompress(base64.b64decode(s))",
        ),
        11: (
            "import marshal, zlib, base64\n",
            "exec(marshal.loads(zlib.decompress(base64.b64decode(s))))\n",
            "s = zlib.decompress(base64.b64decode(s))",
        ),
        12: (
            "import marshal, binascii\n",
            "exec(marshal.loads(binascii.unhexlify(s)))\n",
            "s = binascii.unhexlify(s)",
        ),
        13: (
            "import marshal, base64\n",
            "exec(marshal.loads(base64.b64decode(s)))\n",
            "s = base64.b64decode(s)",
        ),
        14: (
            "import marshal, base64\n",
            "exec(marshal.loads(base64.a85decode(s)))\n",
            "s = base64.a85decode(s)",
        ),
        15: (
            "import pickle, base64\n",
            "exec(pickle.loads(base64.b64decode(s)))\n",
            "s = base64.b64decode(s)",
        ),
        16: (
            "import base64\n",
            "exec(base64.b32decode(base64.b64decode(s)).decode('utf-8'))\n",
            "s = base64.b32decode(base64.b64decode(s)).decode('utf-8')",
        ),
        17: (
            "import marshal, base64, lzma\n",
            "exec(marshal.loads(lzma.decompress(base64.b64decode(s))))\n",
            "s = lzma.decompress(base64.b64decode(s))",
        ),
        18: (
            "import marshal, binascii, zlib\n",
            "exec(marshal.loads(zlib.decompress(binascii.unhexlify(s))))\n",
            "s = zlib.decompress(binascii.unhexlify(s))",
        ),
        19: (
            "import marshal, base64, zlib\n",
            "exec(marshal.loads(zlib.decompress(base64.b64decode(s))))\n",
            "s = zlib.decompress(base64.b64decode(s))",
        ),
        20: (
            "import marshal, base64, zlib\n",
            "exec(marshal.loads(zlib.decompress(base64.b32decode(s))))\n",
            "s = zlib.decompress(base64.b32decode(s))",
        ),
        21: (
            "import marshal, base64, lzma, zlib\n",
            "exec(marshal.loads(lzma.decompress(zlib.decompress(base64.b64decode(s)))))\n",
            "s = lzma.decompress(zlib.decompress(base64.b64decode(s)))",
        ),
        22: (
            "import marshal, base64, lzma, zlib\n",
            "exec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(s)))))\n",
            "s = zlib.decompress(lzma.decompress(base64.b64decode(s)))",
        ),
        23: (
            "import marshal, base64, bz2, zlib\n",
            "exec(marshal.loads(zlib.decompress(bz2.decompress(base64.b64decode(s)))))\n",
            "s = zlib.decompress(bz2.decompress(base64.b64decode(s)))",
        ),
    }

    if choice == 4:
        return (
            h
            + "HEX_EMOJI_MAP={'0':'😀','1':'😁','2':'😂','3':'🤣','4':'😃','5':'😄','6':'😅','7':'😆','8':'😉','9':'😊','a':'😋','b':'😎','c':'😍','d':'😘','e':'😗','f':'😙'}\n"
            + "EMOJI_HEX_MAP={v:k for k,v in HEX_EMOJI_MAP.items()}\n"
            + "def emoji_to_hex(e):\n    return ''.join(EMOJI_HEX_MAP[ch] for ch in e)\n"
            + "import marshal, binascii\n"
            + "hex_str=emoji_to_hex(r'''{payload}''')\n"
            + "pyc_bytes=binascii.unhexlify(hex_str)\n"
            + "exec(marshal.loads(pyc_bytes))\n"
        )

    conf = imports.get(choice)
    if not conf:
        return str(h + "\nraise SystemExit('Unsupported encoding method')\n")

    imp_line, final_exec, inner_line = conf
    imp_line = imp_line or ""
    payload_line = f"s = r'''{payload}'''\n"
    body = h + imp_line + payload_line + loop(inner_line) + final_exec
    return str(body)


# ============================== AES+Marshal+XOR (24) ==============================


def encode_choice_24(source: str):
    for _ in tqdm(
        range(50), desc="Encrypting AES", ncols=70, bar_format="{l_bar}{bar}| {n_fmt}%"
    ):
        time.sleep(0.01)
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad

    code_obj = compile(source, "<encrypted>", "exec")
    marshalled = marshal.dumps(code_obj)
    key = os.urandom(16)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(marshalled, AES.block_size))
    key_encoded = "+".join(str(b ^ 0x42) for b in key)
    iv_encoded = "*".join(str(b ^ 0x37) for b in iv)
    payload_b64 = base64.b64encode(ciphertext).decode()
    encoded_block = f"""
# AES+Marshal+XOR runner (single-file)
import marshal, base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
def d(s, k): return bytes(int(x)^k for x in s.split('+'))
def v(s, k): return bytes(int(x)^k for x in s.split('*'))
k = d('{key_encoded}', 0x42)
i = v('{iv_encoded}', 0x37)
data = base64.b64decode('{payload_b64}')
exec(marshal.loads(unpad(AES.new(k, AES.MODE_CBC, i).decrypt(data), 16)))
"""
    return encoded_block.strip(), "aes_marshal_xor"


# ============================== Cython single-file (29) ==============================


def generate_cython_singlefile_runner(source_code: str, base_name: str):
    return textwrap.dedent(
        f"""\
# Single-file Cython runner
import os, sys, tempfile, shutil, importlib.util, glob, textwrap, subprocess
from pathlib import Path
SRC_NAME = "{base_name}.py"
# gunakan repr agar aman untuk semua isi
SOURCE = {source_code!r}

def build_and_run():
    try:
        import Cython  # noqa
        from setuptools import setup  # noqa
    except Exception:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cython", "setuptools", "wheel"])

    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / SRC_NAME
        src.write_text(SOURCE, encoding="utf-8")

        setup_py = Path(tmp) / "setup.py"
        setup_py.write_text(textwrap.dedent(f\"\"\"
            from setuptools import setup
            from Cython.Build import cythonize
            setup(
                name="{base_name}_ext",
                ext_modules=cythonize("{base_name}.py", compiler_directives={{"language_level": "3"}}),
                zip_safe=False,
            )
        \"\"\"), encoding="utf-8")

        cmd = [sys.executable, "setup.py", "build_ext", "--inplace"]
        res = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True)
        if res.returncode != 0:
            print("Cython build failed:", res.stderr)
            return

        mod_file = None
        for p in glob.glob(str(Path(tmp) / f"{base_name}.*")):
            if p.endswith(".so") or p.endswith(".pyd"):
                mod_file = p
                break
        if not mod_file:
            print("Compiled module not found.")
            return

        spec = importlib.util.spec_from_file_location("{base_name}", mod_file)
        if spec is None or spec.loader is None:
            print("Cannot load compiled module spec.")
            return
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, "main"):
            mod.main()

if __name__ == "__main__":
    build_and_run()
"""
    )


# ============================== UI / Flow ==============================


def print_helper():
    clear_screen()
    print_banner()
    print(
        Fore.CYAN
        + """
Helper - Usage & Info:

- Output 1 file .py: 'results/<method>/<nama>_encode.py'
- Metode 1–23: multilayer (1–100) dengan 15 threads + progress bar animasi (layer-by-layer).
- Semua 1–23 sudah didukung multilayer (termasuk marshal-based, dibungkus berulang sebagai string).
- (24) Marshal + AES + XOR → code-block 1 file.
- (29) Cython: 1 file .py yang compile sendiri saat dijalankan.
- Input menu mendukung 01/1.
"""
    )


def print_menu():
    try:
        print_banner_with_timezone()
        labels = [
            "Exit",
            "ROT13",
            "Zlib",
            "Gzip",
            "Pyc (Emoji)",
            "Base85",
            "Base16",
            "Base64",
            "Base32",
            "XOR + Base64",
            "Marshal + Gzip",
            "Marshal + Zlib",
            "Marshal + Base16",
            "Marshal + Base64",
            "Marshal + Base85",
            "Pickle + Base64",
            "Base32 + BinAscii",
            "Marshal + Lzma + Base64",
            "Marshal + Zlib + Base16",
            "Marshal + Zlib + Base64",
            "Marshal + Zlib + Base32",
            "Base64 + Marshal + Zlib + Lzma",
            "Base64 + Marshal + Lzma + Zlib",
            "Base64 + Marshal + Bz2 + Zlib",
            "Marshal + AES + XOR",
            "Install all required packages",
            "Helper - Usage & Info",
            "Python script to EXE (PyInstaller)",
            "PyArmor + EXE (Obfuscate + PyInstaller)",
            "Cython build (single-file runner)",
        ]
        col_width = 55
        total = len(labels)
        half = (total + 1) // 2

        def colored_option(idx, label):
            if idx == 0:
                return (
                    f"{Fore.WHITE}({Fore.RED}00{Fore.WHITE}) {Fore.RED}Exit{Fore.RESET}"
                )
            return f"{Fore.YELLOW}({Fore.MAGENTA}{str(idx).zfill(2)}{Fore.YELLOW}){Fore.LIGHTWHITE_EX} {label}{Fore.RESET}"

        for i in range(half):
            left_idx = i
            right_idx = i + half
            left = colored_option(left_idx, labels[left_idx]).ljust(col_width)
            right = (
                colored_option(right_idx, labels[right_idx])
                if right_idx < total
                else ""
            )
            print(left + right)

    except KeyboardInterrupt:
        print(Fore.MAGENTA + "\nInterrupted by user. Exiting...")
        sys.exit()


async def process_encoding_choice(choice):
    clear_screen()
    print_banner()
    file_path = await asyncio.to_thread(
        input, Fore.YELLOW + f"Enter path to .py file: {Fore.LIGHTBLUE_EX}"
    )
    if not os.path.isfile(file_path) or not file_path.endswith(".py"):
        print(Fore.RED + "Invalid Python file path.")
        input(Fore.CYAN + "Press Enter to return to menu...")
        return

    async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
        user_input = await f.read()

    if choice == 29:
        base = os.path.splitext(os.path.basename(file_path))[0]
        code = generate_cython_singlefile_runner(user_input, base)
        out = await save_file_py(code, "cython", file_path)
        print(Fore.GREEN + f"Saved:\n  {out}")
        input(Fore.CYAN + "Press Enter to return to menu...")
        return

    layers = 1
    if 1 <= choice <= 23:
        raw = await asyncio.to_thread(
            input, Fore.YELLOW + "Enter layers (1-100, default 1): "
        )
        raw = raw.strip()
        if raw.isdigit():
            layers = max(1, min(MAX_LAYERS, int(raw)))
        else:
            try:
                layers = max(1, min(MAX_LAYERS, int(raw.lstrip("0") or "1")))
            except:
                layers = 1

    if choice == 24:
        encoded_block, method = encode_choice_24(user_input)
        runner_code = f"""# Single-file output\n{encoded_block}"""
        out = await save_file_py(runner_code, method, file_path)
        print(Fore.GREEN + f"Saved:\n  {out}")
        input(Fore.CYAN + "Press Enter to return to menu...")
        return

    # 1–23: advanced multilayer (semua metode)
    payload, method, actual_layers = encode_multilayer(choice, user_input, layers)
    if not (payload and method):
        print(Fore.RED + "Encoding failed or unsupported method.")
        input(Fore.CYAN + "Press Enter to return to menu...")
        return

    runner_code = generate_runner(choice, payload, actual_layers)
    out = await save_file_py(runner_code, method, file_path)
    print(Fore.GREEN + f"Saved:\n  {out}")
    input(Fore.CYAN + "Press Enter to return to menu...")


def install_packages():
    clear_screen()
    print_banner()
    print(Fore.CYAN + "Installing required packages...\n")
    packages = [
        "colorama",
        "pyfiglet",
        "pyarmor==9.1.8",
        "pyinstaller",
        "tqdm",
        "pytz",
        "requests",
        "pycryptodome",
        "aiofiles",
        "cython",
        "setuptools",
        "wheel",
    ]
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"]
        )
        for pkg in tqdm(packages, desc="Installing packages", ncols=70):
            print(Fore.YELLOW + f"Installing {pkg}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
            time.sleep(0.2)
        print(Fore.GREEN + "\nAll packages installed successfully!")
    except Exception as e:
        print(Fore.RED + f"Package installation error: {e}")


def check_pyinstaller_installed():
    return which("pyinstaller") is not None


def pyinstaller_build():
    if not check_pyinstaller_installed():
        print(Fore.RED + "PyInstaller not installed.")
        return
    filepath = input(
        Fore.CYAN + "Enter path to Python (.py) file to build EXE: "
    ).strip()
    if not os.path.isfile(filepath) or not filepath.endswith(".py"):
        print(Fore.RED + "Invalid Python file path.")
        return
    output_folder = os.path.join("results", "pyinstaller_output")
    os.makedirs(output_folder, exist_ok=True)
    if os.path.exists("build"):
        shutil.rmtree("build")
    print(Fore.YELLOW + "Running PyInstaller...")
    result = subprocess.run(
        ["pyinstaller", "--onefile", "--distpath", output_folder, filepath],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print(Fore.GREEN + f"PyInstaller build successful, output in {output_folder}")
    else:
        print(Fore.RED + "PyInstaller build failed:")
        print(Fore.RED + result.stderr)
        print(Fore.RED + result.stdout)


def check_pyarmor_version():
    try:
        result = subprocess.run(
            ["pyarmor", "--version"], capture_output=True, text=True
        )
        return result.stdout.strip() if result.returncode == 0 else None
    except Exception:
        return None


def get_pyarmor_command(base_command, output_folder, filepath):
    version = check_pyarmor_version()
    if version is None:
        raise RuntimeError(
            "PyArmor tidak terdeteksi. Install dengan: pip install pyarmor==7.6.0"
        )
    match = re.search(r"(\d+)", version)
    if not match:
        raise RuntimeError(f"Gagal membaca versi PyArmor: {version}")
    major = int(match.group(1))
    quoted_output = shlex.quote(output_folder)
    quoted_file = shlex.quote(filepath)
    if major <= 7:
        return ["pyarmor", "obfuscate", "--output", quoted_output, quoted_file]
    else:
        return ["pyarmor", "gen", "obf", "--output", quoted_output, quoted_file]


def pyarmor_plus_pyinstaller():
    version = check_pyarmor_version()
    if not version:
        print(Fore.RED + "❌ PyArmor not found or not installed.")
        return
    if not check_pyinstaller_installed():
        print(Fore.RED + "❌ PyInstaller not installed.")
        return
    filepath = input(Fore.CYAN + "📄 Enter path to Python (.py) file: ").strip()
    if not os.path.isfile(filepath) or not filepath.endswith(".py"):
        print(Fore.RED + "❌ Invalid Python file path.")
        return
    filename = os.path.basename(filepath).replace(".py", "")
    with tempfile.TemporaryDirectory() as tmpdir:
        dist_dir = os.path.join(tmpdir, "dist")
        os.makedirs(dist_dir, exist_ok=True)
        print(Fore.YELLOW + "🔐 Obfuscating with PyArmor...")
        for _ in tqdm(
            range(30),
            desc="Running PyArmor",
            ncols=70,
            bar_format="{l_bar}{bar}| {remaining}s",
        ):
            time.sleep(0.02)
        cmd = get_pyarmor_command("obfuscate", dist_dir, filepath)
        obf = subprocess.run(cmd, capture_output=True, text=True)
        if obf.returncode != 0:
            print(Fore.RED + "❌ PyArmor obfuscation failed:")
            print(Fore.RED + obf.stderr.strip())
            return
        print(Fore.GREEN + "✅ PyArmor obfuscation completed.\n")
        obf_files = glob.glob(os.path.join(dist_dir, "**", "*.py"), recursive=True)
        obf_script = obf_files[0] if obf_files else None
        if not obf_script:
            print(Fore.RED + "❌ Obfuscated .py file not found.")
            print(Fore.YELLOW + f"🔍 Check contents of: {dist_dir}")
            return
        output_folder = os.path.join("results", "pyarmor_pyinstaller_output")
        os.makedirs(output_folder, exist_ok=True)
        print(Fore.YELLOW + "⚙️  Building EXE with PyInstaller...")
        for _ in tqdm(
            range(50),
            desc="Packaging EXE",
            ncols=70,
            bar_format="{l_bar}{bar}| {remaining}s",
        ):
            time.sleep(0.015)
        exe = subprocess.run(
            ["pyinstaller", "--onefile", "--distpath", output_folder, obf_script],
            capture_output=True,
            text=True,
        )
        if exe.returncode != 0:
            print(Fore.RED + "❌ PyInstaller build failed:")
            print(Fore.RED + exe.stderr.strip())
        else:
            output_exe = os.path.join(
                output_folder, os.path.basename(obf_script).replace(".py", ".exe")
            )
            print(Fore.GREEN + f"✅ EXE build complete:")
            print(Fore.CYAN + f"📦 Output: {output_exe}\n")


async def main():
    try:
        while True:
            try:
                clear_screen()
                print_banner()
                print_menu()
                choice_raw = await asyncio.to_thread(
                    input,
                    f"\n{Fore.YELLOW}({Fore.MAGENTA}+{Fore.YELLOW}){Fore.LIGHTWHITE_EX} ( {Fore.LIGHTYELLOW_EX}Choose option {Fore.LIGHTYELLOW_EX}0{Fore.LIGHTWHITE_EX}-{Fore.LIGHTYELLOW_EX}29{Fore.LIGHTWHITE_EX} )--{Fore.LIGHTMAGENTA_EX}> {Fore.YELLOW}",
                )
                choice_raw = choice_raw.strip()
                if choice_raw.isdigit():
                    choice = int(choice_raw)
                else:
                    try:
                        choice = int(choice_raw.lstrip("0") or "0")
                    except:
                        choice = -1

                if choice == 0:
                    print(Fore.MAGENTA + "Goodbye!")
                    break
                elif choice == 25:
                    install_packages()
                    input(Fore.CYAN + "Press Enter to return to menu...")
                elif choice == 26:
                    print_helper()
                    input(Fore.CYAN + "Press Enter to return to menu...")
                elif choice == 27:
                    clear_screen()
                    pyinstaller_build()
                    input(Fore.CYAN + "Press Enter to return to menu...")
                elif choice == 28:
                    clear_screen()
                    pyarmor_plus_pyinstaller()
                    input(Fore.CYAN + "Press Enter to return to menu...")
                elif choice == 29:
                    clear_screen()
                    await process_encoding_choice(29)
                elif 1 <= choice <= 24:
                    await process_encoding_choice(choice)
                else:
                    print(Fore.RED + "Invalid choice.")
                    input(Fore.CYAN + "Press Enter to continue...")

            except KeyboardInterrupt:
                print(Fore.MAGENTA + "\nInterrupted by user. Exiting...")
                break
            except Exception as e:
                print(Fore.RED + f"Unexpected error: {e}")
                input(Fore.CYAN + "Press Enter to continue...")

    except KeyboardInterrupt:
        print(Fore.MAGENTA + "\nInterrupted by user. Exiting...")


if __name__ == "__main__":
    asyncio.run(main())
