""" Decompiled by Exotic Hridoy """

# coding=utf-8
# Author: Kiansantang Dev
# python 3.12

from __future__ import annotations
from colorama import init as _cinit, Fore as F, Style as S
import os, sys, time, uuid, platform, hashlib, threading, dataclasses, random, socket, httpx, getpass, locale, shutil, psutil, base64
import ctypes, subprocess
import requests
import argparse
import random
import ssl, json
import hashlib
import datetime
import certifi
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote, parse_qsl, urlencode
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich import box
from datetime import datetime
import os, subprocess, importlib, sys
import threading
from urllib.parse import urlparse, unquote
from urllib3.exceptions import InsecureRequestWarning
from bs4 import XMLParsedAsHTMLWarning
import re
from urllib.parse import urlparse, unquote
import urllib.parse
from bs4 import XMLParsedAsHTMLWarning
import warnings
import concurrent.futures
import urllib.request
import warnings
from bs4 import XMLParsedAsHTMLWarning
import urllib3
from requests import exceptions
from typing import Optional, Iterable, Dict, Any, Tuple, List, Callable, cast, Union
from colorama import Fore, Style
from colorama import Style, Fore
from colorama import init as _cinit, Fore as F, Style as S

_cinit(autoreset=True)
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl_context = ssl.create_default_context(cafile=certifi.where())

USE_PROXY = True
PROXY_FILE = "proxies.txt"
USER_AGENTS_FILE = "user_agents.txt"
MAX_PAGES = 30
PROXY_TIMEOUT = 6
MAX_THREADS = 500
MAX_RETRIES = 5
DELAY_BETWEEN_REQUESTS = (3, 20)

lock = threading.Lock()


try:
    import pyfiglet, requests, aiohttp, colorama, faker, psutil
except ImportError:
    os.system(
        "pip install requests asyncio aiohttp faker colorama pyfiglet httpx pycryptodome psutil &> /dev//null"
    )
    print("\nRun again this tools\n")
    sys.exit()

# ===================== DEFAULTS =====================
LABEL = "DORKPASS"
ENDPOINTS = ["https://verif.stecu.cloud"]
HEARTBEAT_SEC = 5
VERIFY_TLS = True
TIMEOUT = 7.0
CONNECT_TO = 5.0
CACHE_FILE = os.path.expanduser("~/.license_saved-DORKPASS")
DID_FILE = os.path.expanduser("~/.license_device_id-DORKPASS")
UA_EXTRA = ""
APP_VER = "2.3"

# retry/backoff
RETRIES = 5
BACKOFF_BASE = 0.25
BACKOFF_CAP = 2.5

_HARD_DROP = {"disabled", "expired", "invalid", "label_mismatch", "deleted"}


# ===================== STATE =====================
@dataclasses.dataclass
class Info:
    status: str = "unknown"
    expires: Optional[str] = None
    owner: str = ""
    devices_used: int = 0
    devices_allowed: int = 0
    endpoint: str = ""
    masked_key: str = ""


_INFO = Info()
_LOCK = threading.RLock()
_CLI: Optional["Client"] = None


# ===================== UTIL ======================
def _cls() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def _sleep_retry(i: int) -> None:
    d = min(BACKOFF_CAP, BACKOFF_BASE * (2**i))
    d = d * (0.7 + 0.6 * random.random())
    time.sleep(d)


def _mask(k: str) -> str:
    p = [x for x in (k or "").split("-") if x]
    if len(p) >= 3:
        return f"{p[0]}-{p[1]}-{p[2]}-XXXX-XXXXX"
    return (k[:4] if k else "LIC") + "-XXXX-XXXXX"


def _cstatus(s: str) -> str:
    s = (s or "unknown").lower()
    if s in {"actived", "active"}:
        return f"{F.GREEN}{s}{S.RESET_ALL}"
    if s in {"disabled", "expired", "invalid", "label_mismatch", "deleted"}:
        return f"{F.RED}{s}{S.RESET_ALL}"
    return f"{F.YELLOW}{s}{S.RESET_ALL}"


def _hint(e: Exception) -> str:
    if isinstance(e, httpx.ConnectTimeout):
        return "Connection timed out"
    if isinstance(e, httpx.ReadTimeout):
        return "Server slow"
    if isinstance(e, httpx.ConnectError):
        return "Connect failed"
    if isinstance(e, httpx.HTTPStatusError):
        return f"HTTP {getattr(e, 'response', None) and e.response.status_code}"
    if isinstance(e, httpx.TransportError):
        return "Transport/TLS error"
    if isinstance(e, socket.gaierror):
        return "DNS resolve failed"
    return "Unknown error"


def _owner_from(p: Dict[str, Any]) -> str:
    return (
        p.get("owner")
        or p.get("name")
        or p.get("user")
        or p.get("username")
        or p.get("customer")
        or p.get("display_name")
        or ""
    )


def _status_from(p: Dict[str, Any]) -> str:
    st = str(p.get("status") or "").lower()
    if st in {"actived", "active"}:
        return "actived"
    if st in _HARD_DROP:
        return st
    err = str(p.get("error") or "").lower()
    if "label" in err:
        return "label_mismatch"
    if "expired" in err:
        return "expired"
    if "disabled" in err or "not active" in err:
        return "disabled"
    if "invalid" in err or "not found" in err:
        return "invalid"
    return "unknown"


def _b64u(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).decode("ascii").rstrip("=")


def _json(obj: Any) -> str:
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=False)


def _is_container() -> bool:
    try:
        if os.path.exists("/.dockerenv"):
            return True
        with open("/proc/1/cgroup", "r", encoding="utf-8", errors="ignore") as f:
            t = f.read()
            return ("docker" in t) or ("containerd" in t) or ("kubepods" in t)
    except Exception:
        return False


def _lang_enc() -> tuple[str, str]:
    try:
        try:
            locale.setlocale(locale.LC_ALL, "")
        except Exception:
            pass
        loc = locale.getlocale()
        lang = "-".join([x for x in (loc or ()) if x]) or ""
        enc = (
            locale.getencoding()
            if hasattr(locale, "getencoding")
            else locale.getpreferredencoding(False)
        )
        return lang, enc or ""
    except Exception:
        return "", ""


def _is_termux() -> bool:
    return bool(os.getenv("TERMUX_VERSION") or os.getenv("ANDROID_ROOT"))


def _mem_total_bytes() -> Optional[int]:
    try:
        import psutil  # type: ignore

        return int(psutil.virtual_memory().total)
    except Exception:
        pass

    sysname = platform.system()

    if sysname == "Windows":
        try:

            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [
                    ("dwLength", ctypes.c_ulong),
                    ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong),
                    ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong),
                    ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong),
                    ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
                ]

            stat = MEMORYSTATUSEX()
            stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
                return int(stat.ullTotalPhys)
        except Exception:
            pass
        try:
            kb = ctypes.c_ulonglong(0)
            if ctypes.windll.kernel32.GetPhysicallyInstalledSystemMemory(
                ctypes.byref(kb)
            ):
                return int(kb.value) * 1024
        except Exception:
            pass
        return None

    if sysname == "Darwin":
        try:
            libc = ctypes.CDLL("libc.dylib")
            val = ctypes.c_uint64()
            size = ctypes.c_size_t(ctypes.sizeof(val))
            if (
                libc.sysctlbyname(
                    b"hw.memsize", ctypes.byref(val), ctypes.byref(size), None, 0
                )
                == 0
            ):
                return int(val.value)
        except Exception:
            pass
        try:
            out = subprocess.check_output(["sysctl", "-n", "hw.memsize"]).strip()
            return int(out)
        except Exception:
            pass

    try:
        sysconf_obj: Any = getattr(os, "sysconf", None)
        if callable(sysconf_obj):
            sysconf = cast(Callable[[str], int], sysconf_obj)
            page_size = int(sysconf("SC_PAGE_SIZE"))
            phys_pages = int(sysconf("SC_PHYS_PAGES"))
            return page_size * phys_pages
    except Exception:
        pass
    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    kb = int(line.split()[1])
                    return kb * 1024
    except Exception:
        pass

    return None


def _dev_info() -> Dict[str, Any]:
    sysn = platform.system()
    rel = platform.release()
    ver = platform.version()
    mach = platform.machine()
    arch = platform.architecture()[0]
    node = platform.node()
    pyver = platform.python_version()
    pyimpl = platform.python_implementation()
    user = os.getenv("USERNAME") or os.getenv("USER") or ""
    try:
        lang, enc = _lang_enc()
    except Exception:
        lang = ""
        enc = ""
    cpu = os.cpu_count() or 0
    ram = _mem_total_bytes()
    termux = _is_termux()
    cont = _is_container()
    disks = {}
    try:
        du = shutil.disk_usage(os.path.expanduser("~"))
        disks = {"home_total": du.total, "home_used": du.used}
    except Exception:
        pass
    return {
        "os": {
            "name": sysn,
            "release": rel,
            "version": ver,
            "arch": arch,
            "machine": mach,
        },
        "host": {"name": node, "user": user, "lang": lang, "enc": enc},
        "python": {"version": pyver, "impl": pyimpl},
        "hw": {"cpu_count": cpu, "mem_bytes": ram},
        "env": {"termux": termux, "container": cont},
        "disk": disks,
        "app": {"label": LABEL, "ver": APP_VER, "ua_extra": UA_EXTRA or None},
        "did_file": DID_FILE,
    }


def _ua(did: str) -> str:
    sysn = platform.system()
    rel = platform.release()
    mach = platform.machine()
    node = platform.node()
    py = platform.python_version()
    ua = (
        f"license-client/{APP_VER} ({sysn} {rel}; {mach}; {node}) Python/{py} DID/{did}"
    )
    return f"{ua} {UA_EXTRA}".strip()


def _did() -> str:
    try:
        os.makedirs(os.path.dirname(DID_FILE), exist_ok=True)
        if os.path.isfile(DID_FILE):
            v = open(DID_FILE, "r", encoding="utf-8").read().strip()
            if v:
                return v
    except Exception:
        pass
    raw = f"{uuid.getnode()}_{platform.node()}"
    d = "LCL-" + hashlib.sha1(raw.encode()).hexdigest()[:20].upper()
    try:
        open(DID_FILE, "w", encoding="utf-8").write(d)
        os.chmod(DID_FILE, 0o600)
    except Exception:
        pass
    return d


def _load_key() -> Optional[str]:
    try:
        if os.path.isfile(CACHE_FILE):
            return open(CACHE_FILE, "r", encoding="utf-8").read().strip() or None
    except Exception:
        return None
    return None


def _save_key(k: str) -> None:
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    open(CACHE_FILE, "w", encoding="utf-8").write(k.strip())
    try:
        os.chmod(CACHE_FILE, 0o600)
    except Exception:
        pass


def _drop_key() -> None:
    try:
        os.remove(CACHE_FILE)
    except Exception:
        pass


def _set_info(**kw) -> None:
    with _LOCK:
        for k, v in kw.items():
            setattr(_INFO, k, v)


def get_info() -> Info:
    with _LOCK:
        return dataclasses.replace(_INFO)


# ===================== CLIENT ======================
class Client:
    def __init__(self, key: str, endpoints: Iterable[str]):
        v = [e.strip().rstrip("/") for e in endpoints if str(e).strip()]
        if not v:
            raise ValueError("ENDPOINTS kosong")
        self.key = key.strip()
        if not self.key:
            raise ValueError("Lisensi wajib diisi")
        self.did = _did()
        self.eps = v
        self.idx = 0
        self.cli = httpx.Client(
            http2=True,
            timeout=httpx.Timeout(TIMEOUT, connect=CONNECT_TO),
            verify=VERIFY_TLS,
            headers={"User-Agent": _ua(self.did)},
        )
        self.stop = threading.Event()
        self.th: Optional[threading.Thread] = None

    def _ep(self) -> str:
        return self.eps[self.idx % len(self.eps)]

    def _next(self) -> None:
        self.idx = (self.idx + 1) % len(self.eps)

    def _rebuild(self, *, http2: Optional[bool] = None) -> None:
        try:
            self.cli.close()
        except Exception:
            pass
        h2 = True if http2 is None else bool(http2)
        self.cli = httpx.Client(
            http2=h2,
            timeout=httpx.Timeout(TIMEOUT, connect=CONNECT_TO),
            verify=VERIFY_TLS,
            headers={"User-Agent": _ua(self.did)},
        )

    def _post(self, path: str, js: Dict[str, Any]) -> Tuple[Dict[str, Any], str]:
        dev = _dev_info()
        hdr_dev = {
            "os": dev["os"]["name"],
            "rel": dev["os"]["release"],
            "arch": dev["os"]["arch"],
            "mach": dev["os"]["machine"],
            "node": dev["host"]["name"],
            "py": dev["python"]["version"],
            "app": APP_VER,
        }
        enc_hdr = _b64u(_json(hdr_dev).encode("utf-8"))

        total = max(1, RETRIES) * max(1, len(self.eps))
        h2_downgraded = False

        for i in range(total):
            ep = self._ep()
            try:
                r = self.cli.post(
                    f"{ep}{path}",
                    json={**js, "device": dev},
                    headers={
                        "X-Device-ID": self.did,
                        "X-Device-Info": enc_hdr,
                    },
                )
                ctype = r.headers.get("content-type", "").lower()
                if "application/json" in ctype:
                    data = r.json()
                else:
                    try:
                        data = json.loads(r.text) if (r.text or "").strip() else {}
                    except Exception:
                        data = {"ok": False, "error": "bad_response"}

                if r.status_code >= 500:
                    self._next()
                    _sleep_retry(i)
                    continue

                return (
                    (
                        data
                        if isinstance(data, dict)
                        else {"ok": False, "error": "bad_response"}
                    ),
                    ep,
                )

            except (httpx.ConnectTimeout, httpx.ReadTimeout):
                self._next()
                _sleep_retry(i)
                continue

            except httpx.ConnectError:
                try:
                    self._rebuild(http2=True)
                except Exception:
                    pass
                self._next()
                _sleep_retry(i)
                continue

            except httpx.TransportError:
                if not h2_downgraded:
                    try:
                        self._rebuild(http2=False)
                        h2_downgraded = True
                        continue
                    except Exception:
                        pass
                self._next()
                _sleep_retry(i)
                continue

            except Exception:
                self._next()
                _sleep_retry(i)
                continue

        return {"ok": False, "error": "network_failed"}, ",".join(self.eps)

    def verify(self) -> Dict[str, Any]:
        d, ep = self._post(
            "/api/verify",
            {"license_key": self.key, "label": LABEL, "device_id": self.did},
        )
        st = _status_from(d)
        _set_info(
            status=st,
            expires=d.get("expires_at"),
            owner=_owner_from(d),
            devices_used=int(d.get("devices_used") or 0),
            devices_allowed=int(d.get("devices_allowed") or 0),
            endpoint=ep,
            masked_key=_mask(self.key),
        )
        ok = bool(d.get("ok")) and st == "actived"
        d["ok"] = ok
        d["status"] = st
        d["endpoint"] = ep
        return d

    def hb(self) -> Dict[str, Any]:
        d, ep = self._post(
            "/api/heartbeat", {"license_key": self.key, "device_id": self.did}
        )
        st = _status_from(d)
        if st != "actived":
            _set_info(status=st, endpoint=ep)
        return {"ok": st == "actived", "status": st, "endpoint": ep}

    def start_bg(self, sec: int) -> None:
        if self.th and self.th.is_alive():
            return
        self.stop.clear()

        def loop():
            v = self.verify()
            if not v.get("ok"):
                return
            while not self.stop.is_set():
                try:
                    self.hb()
                    v = self.verify()
                    if not v.get("ok"):
                        break
                except Exception:
                    pass
                self.stop.wait(max(5, int(sec)))

        self.th = threading.Thread(target=loop, name="lic-heartbeat", daemon=True)
        self.th.start()

    def stop_bg(self, *, join: bool = False) -> None:
        self.stop.set()
        if join and self.th and self.th.is_alive():
            self.th.join(timeout=3)


# ===================== UI BASE ======================
def _banner(title: str) -> None:
    try:
        from pyfiglet import figlet_format  # pip install pyfiglet

        print(F.CYAN + figlet_format(title, font="slant") + S.RESET_ALL)
    except Exception:
        print(f"{F.CYAN}{'='*10} {title} {'='*10}{S.RESET_ALL}")


def _hr() -> None:
    print(F.MAGENTA + "-" * 60 + S.RESET_ALL)


def print_info() -> None:
    i = get_info()
    k = i.masked_key or "(none)"
    exp = i.expires or "–"
    dvc = (
        f"{i.devices_used}/{i.devices_allowed}"
        if (i.devices_used or i.devices_allowed)
        else "0/0"
    )

    print(f"{F.GREEN}[+]{S.RESET_ALL} License     : {F.YELLOW}{k}{S.RESET_ALL}")
    print(f"{F.GREEN}[+]{S.RESET_ALL} Status      : {_cstatus(i.status)}")
    print(f"{F.GREEN}[+]{S.RESET_ALL} Expired     : {F.YELLOW}{exp}{S.RESET_ALL}")
    print(f"{F.GREEN}[+]{S.RESET_ALL} Device log  : {F.MAGENTA}{dvc}{S.RESET_ALL}")
    if i.owner:
        print(
            f"{F.GREEN}[+]{S.RESET_ALL} Owner       : {F.WHITE}{i.owner}{S.RESET_ALL}"
        )


def _error(msg: str, *, hint: str | None = None) -> None:
    print(f"{F.RED}[ERROR]{S.RESET_ALL} {msg}")
    if hint:
        print(f"{F.YELLOW}[HINT]{S.RESET_ALL} {hint}")


# ===================== PUBLIC API (config) ======================
def init(
    *,
    label: Optional[str] = None,
    endpoints: Optional[Iterable[str]] = None,
    heartbeat_sec: Optional[int] = None,
    verify_tls: Optional[bool] = None,
    cache_file: Optional[str] = None,
    did_file: Optional[str] = None,
    timeout: Optional[float] = None,
    connect_timeout: Optional[float] = None,
    ua_extra: Optional[str] = None,
) -> None:
    global LABEL, ENDPOINTS, HEARTBEAT_SEC, VERIFY_TLS, CACHE_FILE, DID_FILE, TIMEOUT, CONNECT_TO, UA_EXTRA
    if label is not None:
        LABEL = label
    if endpoints:
        ENDPOINTS = [e.strip().rstrip("/") for e in endpoints if str(e).strip()]
    if heartbeat_sec:
        HEARTBEAT_SEC = int(heartbeat_sec)
    if verify_tls is not None:
        VERIFY_TLS = bool(verify_tls)
    if cache_file:
        CACHE_FILE = os.path.expanduser(cache_file)
    if did_file:
        DID_FILE = os.path.expanduser(did_file)
    if timeout:
        TIMEOUT = float(timeout)
    if connect_timeout:
        CONNECT_TO = float(connect_timeout)
    if ua_extra is not None:
        UA_EXTRA = ua_extra.strip()


# ===================== STORE FRONT DATA + THEME ======================
# Plans: satu harga, murah, lifetime max $40
# (label, months, total_price_usd). months=None => Lifetime
PLANS = [
    ("1 Month", 1, 9),
    ("2 Months", 2, 15),
    ("3 Months", 3, 18),
    ("5 Months", 5, 25),
    ("8 Months", 8, 29),
    ("10 Months", 10, 34),
    ("Lifetime", None, 40),
]

CONTACT_SALES = {
    "Telegram": "@xqndrs66, @xqndrs",
    "YouTube": "youtube.com/@kiansantang_welitt",
    "GitHub": "github.com/KianSantang777",
}

# Warranty dynamic:
GARANSI_LABEL = "30-day Guarantee"  # ≥ 5 months & lifetime

# Theme (subtle)
HEADER_STYLE = F.WHITE + S.BRIGHT
PRICE_STYLE = F.YELLOW + S.BRIGHT
DURATION_STYLE = F.WHITE
GARANSI_STYLE = F.GREEN
META_STYLE = F.CYAN
ACCENT = F.MAGENTA


# ===================== SINGLE-FUNCTION STORE FRONT (10 DESIGNS) ======================
def ui_storefront(style: str = "v1") -> None:
    # ---------- local helpers ----------
    import re

    def strip_ansi(s: str) -> str:
        return re.sub(r"\x1b\[[0-9;]*m", "", s)

    def apply(text: str, style: str | None) -> str:
        return (style or "") + str(text) + S.RESET_ALL

    def ljust_vis(text: str, width: int) -> str:
        vis = len(strip_ansi(text))
        return text + (" " * max(0, width - vis))

    def center_vis(text: str, width: int) -> str:
        vis = len(strip_ansi(text))
        pad = max(0, width - vis)
        left = pad // 2
        right = pad - left
        return (" " * left) + text + (" " * right)

    def dim(text: str) -> str:
        return S.DIM + str(text) + S.RESET_ALL

    def rule(w: int) -> str:
        return dim("─" * w)

    def fmt_money(v: float) -> str:
        s = f"{v:.2f}".rstrip("0").rstrip(".")
        return f"${s}"

    def warranty(months: Optional[int]) -> str:
        return (
            "Two-week Guarantee"
            if (months is not None and months < 5)
            else GARANSI_LABEL
        )

    def rows() -> list[tuple[str, str, str]]:
        out = []
        for label, months, total in PLANS:
            price = apply(fmt_money(total), PRICE_STYLE)
            duration = apply(label, DURATION_STYLE)
            guar = apply(warranty(months), GARANSI_STYLE)
            out.append((price, duration, guar))
        return out

    def contacts() -> list[str]:
        out = []
        for k, v in CONTACT_SALES.items():
            out.append(f"{apply(k, HEADER_STYLE)}{dim(': ')}{apply(v, META_STYLE)}")
        return out

    items = rows()
    w_price = max((len(strip_ansi(p)) for p, _, _ in items), default=5)
    w_dur = max((len(strip_ansi(d)) for _, d, _ in items), default=8)
    w_war = max((len(strip_ansi(w)) for _, _, w in items), default=12)
    sep_dot = dim("  ·  ")
    sep_w = len(strip_ansi(sep_dot))

    # ---------- 10 designs ----------
    def v1() -> None:
        # Minimalist dotted list with vertical accent
        total_w = 2 + w_price + sep_w + w_dur + sep_w + w_war
        title = apply("SUBSCRIPTION PLANS", HEADER_STYLE)
        print(center_vis(title, total_w))
        print(rule(total_w))
        bar = ACCENT + "│" + S.RESET_ALL
        for i, (p, d, g) in enumerate(items):
            line = f"{bar} {ljust_vis(p, w_price)}{sep_dot}{ljust_vis(d, w_dur)}{sep_dot}{ljust_vis(g, w_war)}"
            print(line)
            if i != len(items) - 1:
                print(rule(total_w))
        print()
        t = apply("CONTACT DEVELOPER", HEADER_STYLE)
        print(center_vis(t, total_w))
        print(rule(total_w))
        for i, c in enumerate(contacts()):
            print(f"{bar} {c}")
            if i != len(CONTACT_SALES) - 1:
                print(rule(total_w))

    def v2() -> None:
        # Rounded cards stacked
        inner = max(28, min(54, max(w_price, w_dur, w_war)))
        tw = inner + 4
        print(center_vis(apply("SUBSCRIPTION PLANS", HEADER_STYLE), tw))
        print(rule(tw))
        top = "╭" + "─" * (inner + 2) + "╮"
        bot = "╰" + "─" * (inner + 2) + "╯"
        for i, (p, d, g) in enumerate(items):
            print(ACCENT + top + S.RESET_ALL)
            print("│ " + center_vis(p, inner) + " │")
            print("│ " + center_vis(d, inner) + " │")
            print("│ " + center_vis(g, inner) + " │")
            print(ACCENT + bot + S.RESET_ALL)
            if i != len(items) - 1:
                print()
        print()
        t = apply("CONTACT DEVELOPER", HEADER_STYLE)
        print(center_vis(t, tw))
        print(rule(tw))
        for k in contacts():
            print("│ " + ljust_vis(k, inner) + " │")

    def v3() -> None:
        # Clean lines, price badge first
        total_w = 4 + w_price + w_dur + w_war
        print(center_vis(apply("SUBSCRIPTION PLANS", HEADER_STYLE), total_w))
        print(rule(total_w))
        bullet = ACCENT + "•" + S.RESET_ALL
        for i, (p, d, g) in enumerate(items):
            print(f"{bullet} {p}  {d}")
            print(dim("   " + g))
            if i != len(items) - 1:
                print(rule(total_w))

        print()
        print(center_vis(apply("CONTACT DEVELOPER", HEADER_STYLE), total_w))
        print(rule(total_w))
        for c in contacts():
            print(f"{bullet} {c}")

    def v4() -> None:
        # Double-lines header + compact rows
        total_w = 2 + w_price + 2 + w_dur + 2 + w_war
        print(center_vis(apply("SUBSCRIPTION PLANS", HEADER_STYLE), total_w))
        print(dim("═" * total_w))
        sep = dim("  |  ")
        for i, (p, d, g) in enumerate(items):
            print(f"{p}{sep}{d}{sep}{g}")
            if i != len(items) - 1:
                print(rule(total_w))
        print(dim("═" * total_w))
        print(center_vis(apply("CONTACT DEVELOPER", HEADER_STYLE), total_w))
        print(rule(total_w))
        for c in contacts():
            print(c)

    def v5() -> None:
        # Tags style
        def tag(txt: str) -> str:
            return ACCENT + "▕" + S.RESET_ALL + " " + txt

        total_w = 4 + w_price + sep_w + w_dur + sep_w + w_war
        print(center_vis(apply("SUBSCRIPTION PLANS", HEADER_STYLE), total_w))
        print(rule(total_w))
        for i, (p, d, g) in enumerate(items):
            print(tag(p) + sep_dot + d + sep_dot + g)
            if i != len(items) - 1:
                print(rule(total_w))
        print()
        print(center_vis(apply("CONTACT DEVELOPER", HEADER_STYLE), total_w))
        print(rule(total_w))
        for c in contacts():
            print(tag(c))

    def v6() -> None:
        # Left rail with dim timeline
        total_w = 4 + w_price + w_dur + w_war
        rail = ACCENT + "│" + S.RESET_ALL
        print(center_vis(apply("SUBSCRIPTION PLANS", HEADER_STYLE), total_w))
        print(rule(total_w))
        for i, (p, d, g) in enumerate(items):
            print(f"{rail} {p}  {d}")
            print(f"{rail} {dim(g)}")
            if i != len(items) - 1:
                print(f"{rail} {dim('—' * (total_w - 2))}")
        print()
        print(center_vis(apply("CONTACT DEVELOPER", HEADER_STYLE), total_w))
        print(f"{rail} {dim('contacts')}")
        for c in contacts():
            print(f"{rail} {c}")

    def v7() -> None:
        # Inline chips: [ $ ]  duration — guarantee
        total_w = 6 + w_price + w_dur + w_war

        def chip(s: str) -> str:
            return ACCENT + "[" + S.RESET_ALL + s + ACCENT + "]" + S.RESET_ALL

        print(center_vis(apply("SUBSCRIPTION PLANS", HEADER_STYLE), total_w))
        print(rule(total_w))
        for i, (p, d, g) in enumerate(items):
            print(f"{chip(p)}  {d}  {dim('—')}  {g}")
            if i != len(items) - 1:
                print(rule(total_w))
        print()
        print(center_vis(apply("CONTACT DEVELOPER", HEADER_STYLE), total_w))
        print(rule(total_w))
        for c in contacts():
            print(f"{chip(apply('i', HEADER_STYLE))} {c}")

    def v8() -> None:
        # Underlined header + indented chevrons
        total_w = 2 + w_price + sep_w + w_dur + sep_w + w_war
        title = apply("SUBSCRIPTION PLANS", HEADER_STYLE)
        print(center_vis(title, total_w))
        print(center_vis(dim("¯" * len(strip_ansi(title))), total_w))
        chev = ACCENT + "›" + S.RESET_ALL
        for i, (p, d, g) in enumerate(items):
            print(f"  {chev} {p}{sep_dot}{d}{sep_dot}{g}")
            if i != len(items) - 1:
                print(rule(total_w))
        print()
        t = apply("CONTACT DEVELOPER", HEADER_STYLE)
        print(center_vis(t, total_w))
        print(center_vis(dim("¯" * len(strip_ansi(t))), total_w))
        for c in contacts():
            print(f"  {chev} {c}")

    def v9() -> None:
        # Clean aligned columns (no borders), small header row
        col1, col2, col3 = max(10, w_price), max(12, w_dur), max(14, w_war)
        total_w = col1 + 2 + col2 + 2 + col3
        print(center_vis(apply("SUBSCRIPTION PLANS", HEADER_STYLE), total_w))
        print(
            dim(
                " "
                + ljust_vis("Price", col1)
                + "  "
                + ljust_vis("Duration", col2)
                + "  "
                + ljust_vis("Guarantee", col3)
            )
        )
        print(rule(total_w))
        for i, (p, d, g) in enumerate(items):
            print(
                ljust_vis(p, col1)
                + "  "
                + ljust_vis(d, col2)
                + "  "
                + ljust_vis(g, col3)
            )
        print()
        print(center_vis(apply("CONTACT DEVELOPER", HEADER_STYLE), total_w))
        print(rule(total_w))
        for c in contacts():
            print(c)

    def v10() -> None:
        # Boxed minimal panel with bullet lines
        inner = max(36, w_price + sep_w + w_dur + sep_w + w_war)
        tw = inner + 4
        top = "┌" + "─" * (inner + 2) + "┐"
        mid = "├" + "─" * (inner + 2) + "┤"
        bot = "└" + "─" * (inner + 2) + "┘"
        print(ACCENT + top + S.RESET_ALL)
        print(
            "│ " + center_vis(apply("SUBSCRIPTION PLANS", HEADER_STYLE), inner) + " │"
        )
        print(ACCENT + mid + S.RESET_ALL)
        bullet = ACCENT + "•" + S.RESET_ALL
        for i, (p, d, g) in enumerate(items):
            line = f"{bullet} {p}{sep_dot}{d}{sep_dot}{g}"
            print("│ " + ljust_vis(line, inner) + " │")
        print(ACCENT + mid + S.RESET_ALL)
        print("│ " + center_vis(apply("CONTACT DEVELOPER", HEADER_STYLE), inner) + " │")
        for c in contacts():
            print("│ " + ljust_vis(c, inner) + " │")
        print(ACCENT + bot + S.RESET_ALL)

    registry: Dict[str, Callable[[], None]] = {
        "v1": v1,
        "v2": v2,
        "v3": v3,
        "v4": v4,
        "v5": v5,
        "v6": v6,
        "v7": v7,
        "v8": v8,
        "v9": v9,
        "v10": v10,
    }
    renderer = registry.get(style.lower(), v1)
    renderer()


# ===================== SHOWCASE (optional) ======================
def showcase_all() -> None:
    styles = [f"v{i}" for i in range(1, 11)]
    for idx, st in enumerate(styles, 1):
        _cls()
        _banner(f"{LABEL} — {st.upper()}")
        ui_storefront(style=st)
        print(
            F.CYAN
            + f"[DEMO] Style: {st}  ({idx}/10). Press Enter for next..."
            + S.RESET_ALL
        )
        try:
            input()
        except KeyboardInterrupt:
            break


# ===================== GATE (uses single-function UI) ======================
def gate(app_title: str = LABEL, *, ui_style: str = "v1") -> bool:
    global _CLI
    while True:
        _cls()
        _banner(app_title)
        ui_storefront(style=ui_style)

        k = _load_key()
        if k:
            print(f"{F.CYAN}[INFO]{S.RESET_ALL} Using saved license")
        else:
            try:
                k = input(
                    f"\n{F.LIGHTBLUE_EX}[+] {F.WHITE}Enter license key:{F.YELLOW} "
                ).strip()
            except KeyboardInterrupt:
                print()
                return False
            if not k:
                continue

        try:
            cli = Client(k, ENDPOINTS)
            _CLI = cli
            _hr()
            print(f"{F.CYAN}[INFO]{S.RESET_ALL} Verifying...")
            _hr()
            r = cli.verify()
        except Exception as e:
            _error(str(e), hint=_hint(e))
            time.sleep(1.0)
            continue

        print_info()

        if r.get("ok"):
            _save_key(k)
            try:
                cli.start_bg(HEARTBEAT_SEC)
            except Exception:
                pass
            return True

        st = r.get("status", "unknown")
        if st in _HARD_DROP:
            if st == "disabled":
                print(
                    f"{F.RED}[LOGOUT]{S.RESET_ALL} License was disabled by admin. Enter a new license."
                )
            else:
                print(
                    f"{F.RED}[LOGOUT]{S.RESET_ALL} License is {st}. Enter a new license."
                )
            _drop_key()
        else:
            _error(f"Verification failed ({st})")
        try:
            input(f"{F.YELLOW}Press Enter...{S.RESET_ALL}")
        except KeyboardInterrupt:
            print()
            return False


# ===================== PUBLIC API (hb helpers) ======================
def start_heartbeat() -> None:
    if _CLI:
        _CLI.start_bg(HEARTBEAT_SEC)


def stop_heartbeat(join: bool = False) -> None:
    if _CLI:
        _CLI.stop_bg(join=join)


def status() -> str:
    return get_info().status


def load_user_agents():
    try:
        with open(USER_AGENTS_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]

    except FileNotFoundError:
        return [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/537.36 Chrome/58.0.3029.110 Safari/537.3",
        ]


USER_AGENTS = load_user_agents()


# Youtube: https://youtube.com/@keysean891
# My Telegram: https://t.me/xqndrs666
# Github: https://github.com/KianSantang777
# Channel Telegram: https://t.me/kiansantangsvb
# Author: Kiansantang Dev


try:
    from googlesearch import search
except ImportError:
    os.system("pip install googlesearch-python &> /dev/null")


EXCLUDED_PATHS = [
    "/search",
    "/results",
    "/query",
    "/find",
    "/lookup",
    "/browse",
    "/click",
    "/rdclks",
    "/redirect",
    "/out",
    "/external",
    "/outbound",
    "/exit",
    "/videos",
    "/video",
    "/watch",
    "/media",
    "/play",
    "/news",
    "/newsroom",
    "/latest-news",
    "/press",
    "/stories",
    "/maps",
    "/map",
    "/directions",
    "/place",
    "/location",
    "/images",
    "/image",
    "/gallery",
    "/photo",
    "/photos",
    "/img",
    "/media",
    "/privacy",
    "/privacy-policy",
    "/privacy-please",
    "/confidentiality",
    "/settings",
    "/preferences",
    "/do/settings",
    "/hc/en-us",
    "/account/settings",
    "/help",
    "/support",
    "/faq",
    "/hc/",
    "/customer-service",
    "/assistance",
    "/feedback",
    "/calendar",
    "/events",
    "/event",
    "/schedule",
    "/appointment",
    "/rpc",
    "/endpoint",
    "/service",
    "/services",
    "/feed",
    "/atom",
    "/rss",
]

EXCLUDED_CONTENT_PATHS = [
    "/blog",
    "/blogs",
    "/post",
    "/posts",
    "/posting",
    "/artikel",
    "/articles",
    "/articulos",
    "/news",
    "/noticias",
    "/notizie",
    "/actualites",
    "/forum",
    "/forums",
    "/foros",
    "/discuss",
    "/discussion",
    "/discussions",
    "/discussioni",
    "/thread",
    "/threads",
    "/tema",
    "/sujet",
    "/viewtopic",
    "/topic",
    "/topics",
    "/help",
    "/faqs",
    "/support",
    "/docs",
    "/document",
    "/documents",
    "/documentation",
    "/mail",
    "/mailing",
    "/email",
    "/emails",
    "/listserv",
    "/newsletter",
    "/subscribe",
    "/contact",
    "/community",
    "/communities",
    "/groups",
    "/group",
    "/club",
    "/clubs",
    "/user",
    "/users",
    "/member",
    "/members",
    "/profile",
    "/profiles",
    "/message",
    "/messages",
    "/msg",
    "/msgs",
    "/comment",
    "/comments",
    "/replies",
    "/reply",
    "/announce",
    "/announcement",
    "/announcements",
    "/press",
    "/pressroom",
    "/press-release",
    "/campaign",
    "/event",
    "/events",
    "/calendar",
    "/about",
    "/aboutus",
    "/about-us",
    "/team",
    "/staff",
    "/people",
    "/policy",
    "/privacy",
    "/terms",
    "/legal",
    "/disclaimer",
    "/cookies",
    "/feedback",
    "/testimonials",
    "/reviews",
    "/rating",
    "/ratings",
    "/vote",
    "/voting",
    "/survey",
    "/poll",
    "/enquete",
    "/questionnaire",
    "/wiki",
    "/knowledge",
    "/glossary",
    "/encyclopedia",
    "/reference",
    "/bibliography",
    "/press",
    "/story",
    "/stories",
    "/case-study",
    "/case-studies",
    "/journal",
    "/journals",
    "/publication",
    "/publications",
    "/issue",
    "/issues",
    "/magazine",
    "/magazines",
    "/newsroom",
    "/blogroll",
    "/rss",
    "/atom",
    "/feed",
    "/history",
    "/archives",
    "/archive",
    "/past",
    "/old",
    "/campaigns",
    "/petition",
    "/petitions",
]


EXCLUDED_PATTERNS = [
    "_ylt=",
    "_ylu=",
    "v_t=na",
    "fr2=p:",
    "ei=UTF-8",
    "d={",
    "RK=0",
    "RS=",
    "/click/rdclks",
    "rdclks",
    "click",
    "/out?",
    "/outbound?",
    "/external?",
    "/exit?",
    "/redirect?",
    "/redir?",
    "/goto?",
    "/go?",
    "/visit?",
    "/track?",
    "/tr?",
    "/tracker?",
    "random=",
    "callback=",
    "jsonp=",
    "jsonpCallback=",
    "jsonpcallback=",
]


INTERNAL_SEARCH_DOMAINS = [
    "r.search.aol.com",
    "www.wow.com/click",
    "www.google.com/search",
    "www.bing.com/search",
    "search.yahoo.com",
    "yandex.com/search",
    "duckduckgo.com/?q=",
    "search.brave.com",
    "www.ecosia.org/search",
    "www.startpage.com/do/search",
    "www.metacrawler.com/serp",
    "www.wow.com/search",
    "search.aol.com",
    "r.search.aol.com",
    "www.wow.com/click",
    "www.wow.com/search?q=",
]

googletld = [
    "google.com",
    "google.ad",
    "google.ae",
    "google.com.af",
    "google.com.ag",
    "google.al",
    "google.am",
    "google.co.ao",
    "google.com.ar",
    "google.as",
    "google.at",
    "google.com.au",
    "google.com.bd",
    "google.be",
    "google.bf",
    "google.bg",
    "google.com.bh",
    "google.bi",
    "google.bj",
    "google.com.bn",
    "google.com.bo",
    "google.com.br",
    "google.bs",
    "google.bt",
    "google.co.bw",
    "google.by",
    "google.com.bz",
    "google.ca",
    "google.com.kh",
    "google.cm",
    "google.cn",
    "google.com.co",
    "google.co.cr",
    "google.com.cu",
    "google.cv",
    "google.com.cy",
    "google.cz",
    "google.de",
    "google.dj",
    "google.dk",
    "google.dm",
    "google.com.do",
    "google.dz",
    "google.com.ec",
    "google.ee",
    "google.com.eg",
    "google.es",
    "google.com.et",
    "google.fi",
    "google.fr",
    "google.ga",
    "google.ge",
    "google.com.gh",
    "google.com.gi",
    "google.gl",
    "google.gm",
    "google.gr",
    "google.com.gt",
    "google.gy",
    "google.com.hk",
    "google.hn",
    "google.hr",
    "google.ht",
    "google.hu",
    "google.co.id",
    "google.ie",
    "google.co.il",
    "google.im",
    "google.co.in",
    "google.iq",
    "google.is",
    "google.it",
    "google.je",
    "google.com.jm",
    "google.jo",
    "google.co.jp",
    "google.co.ke",
    "google.ki",
    "google.kg",
    "google.co.kr",
    "google.kz",
    "google.la",
    "google.com.lb",
    "google.li",
    "google.lk",
    "google.co.ls",
    "google.lt",
    "google.lu",
    "google.lv",
    "google.com.ly",
    "google.co.ma",
    "google.md",
    "google.me",
    "google.mg",
    "google.mk",
    "google.ml",
    "google.mn",
    "google.ms",
    "google.com.mt",
    "google.mu",
    "google.mv",
    "google.mw",
    "google.com.mx",
    "google.com.my",
    "google.co.mz",
    "google.com.na",
    "google.com.ng",
    "google.com.ni",
    "google.ne",
    "google.nl",
    "google.no",
    "google.com.np",
    "google.nr",
    "google.nu",
    "google.co.nz",
    "google.com.om",
    "google.com.pa",
    "google.com.pe",
    "google.com.ph",
    "google.com.pk",
    "google.pl",
    "google.pn",
    "google.com.pr",
    "google.ps",
    "google.pt",
    "google.com.py",
    "google.com.qa",
    "google.ro",
    "google.ru",
    "google.rw",
    "google.com.sa",
    "google.com.sb",
    "google.sc",
    "google.se",
    "google.com.sg",
    "google.sh",
    "google.si",
    "google.sk",
    "google.com.sl",
    "google.sn",
    "google.so",
    "google.sm",
    "google.sr",
    "google.st",
    "google.com.sv",
    "google.td",
    "google.tg",
    "google.co.th",
    "google.com.tj",
    "google.tk",
    "google.tl",
    "google.tm",
    "google.tn",
    "google.to",
    "google.com.tr",
    "google.tt",
    "google.com.tw",
    "google.co.tz",
    "google.com.ua",
    "google.co.ug",
    "google.co.uk",
    "google.us",
    "google.com.uy",
    "google.co.uz",
    "google.com.vc",
    "google.co.ve",
    "google.vg",
    "google.co.vi",
    "google.com.vn",
    "google.vu",
    "google.ws",
    "google.co.za",
    "google.co.zm",
    "google.co.zw",
]


def get_google_url(query, page, timestamp):
    google_domain = random.choice(googletld)
    return f"http://www.{google_domain}/search?q={query}&start={page}&t={timestamp}&safe=off"


SEARCH_ENGINES = {
    "Bing": "https://www.bing.com/search?q={query}&first={page}&t={timestamp}&adlt=off",
    "Google ": "http://google.com/search?q={query}&start={page}&t={timestamp}",
    "Google Actld": get_google_url,
    "Baidu": "http://www.baidu.com/s?wd={query}&base_query={query}&t={timestamp}",
    "Google Api's": lambda query, page, timestamp: [
        url for url in search(query, num_results=200, lang="en", tld="com", safe="off")
    ],
    "Yandex": "http://yandex.com/search/?text={query}&p={page}&t={timestamp}&safesearch=0",
    "StartPage": "http://www.startpage.com/search?q={query}&start={page}&t={timestamp}",
    "Bing News": "http://www.bing.com/news/search?q={query}&first={page}&t={timestamp}",
    "DuckDuckGo": "http://duckduckgo.com/?q={query}&s={page}&t={timestamp}&kp=-2",
    "Brave": "http://search.brave.com/search?q={query}&source=web&offset={page}&t={timestamp}&safesearch=off",
    "Ask": "http://www.ask.com/web?q={query}&page={page}&t={timestamp}",
    "T-Online": "http://www.t-online.de/suche/?q={query}&page={page}&t={timestamp}",
    "Naver": "http://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=dsa{query}",
    "Yahoo": "http://search.yahoo.com/search?p={query}&b={page}&t={timestamp}&vm=r",
    "Yahoo Japan": "http://search.yahoo.co.jp/search?p={query}&b={page}&t={timestamp}&ei=UTF-8&vm=r",
    "AOL": "http://search.aol.com/aol/search?q={query}&b={page}&t={timestamp}",
    "Wow": "http://www.wow.com/search?q={query}&b={page}&t={timestamp}",
    "MetaCrawler": "http://www.metacrawler.com/serp?q={query}&start={page}&t={timestamp}",
    "Ecosia": "http://www.ecosia.org/search?q={query}&start={page}&t={timestamp}",
}


dork_count = 0
found_urls = set()
request_count = {engine: 0 for engine in SEARCH_ENGINES}
valid_url_per_engine = {engine: 0 for engine in SEARCH_ENGINES}
all_url_count = 0
valid_url_count = 0
error_count = 0
retry_count = 0
proxies = []
proxies_count = 0
start_time = time.time()
seen_urls = set()
parsed_dork_count = 0

# dork_count = 0
# found_urls = set()
# lock = threading.Lock()
# request_count = {engine: 0 for engine in SEARCH_ENGINES}
# all_url_count = 0
# valid_url_count = 0
# error_count = 0
# retry_count = 0
# proxies = []
# proxies_http_https = []
# proxies_socks4 = []
# proxies_socks5 = []
# proxies_count = 0
# start_time = time.time()

CERT_URL = "https://curl.se/ca/cacert.pem"
CERT_DIR = "certi"
DER_PATH = os.path.join(CERT_DIR, "cacert.der")
PEM_PATH = os.path.join(CERT_DIR, "cacert.pem")
try:
    os.makedirs(CERT_DIR, exist_ok=True)

    if not os.path.exists(DER_PATH):
        resp = requests.get(CERT_URL, timeout=10, verify=certifi.where())
        if resp.status_code == 200:
            with open(DER_PATH, "wb") as cert_file:
                cert_file.write(resp.content)
        else:
            raise Exception(f"Failed download cert. Status Code: {resp.status_code}")

    if not os.path.exists(PEM_PATH) and os.path.exists(DER_PATH):
        subprocess.run(
            ["openssl", "x509", "-inform", "der", "-in", DER_PATH, "-out", PEM_PATH],
            check=True,
        )

    for engine in SEARCH_ENGINES:
        try:
            test_headers = {"User-Agent": random.choice(USER_AGENTS)}
            template = SEARCH_ENGINES[engine]
            if callable(template):
                try:
                    candidate = template("test", 1, int(time.time()))
                    test_url = (
                        candidate[0]
                        if isinstance(candidate, (list, tuple)) and candidate
                        else (candidate if isinstance(candidate, str) else None)
                    )
                except Exception:
                    test_url = None
            else:
                try:
                    test_url = template.format(
                        query="test", page=1, timestamp=int(time.time())
                    )
                except Exception:
                    test_url = None

            # HANYA lanjut jika test_url benar2 str!
            if not (isinstance(test_url, str) and test_url.strip()):
                with lock:
                    error_count += 1
                continue

            verify_path = PEM_PATH if os.path.exists(PEM_PATH) else certifi.where()

            resp = requests.get(
                test_url, headers=test_headers, timeout=10, verify=verify_path
            )

            if resp.status_code == 200:
                with lock:
                    request_count[engine] += 1
            else:
                with lock:
                    error_count += 1

        except requests.exceptions.SSLError:
            try:
                if not (isinstance(test_url, str) and test_url.strip()):
                    with lock:
                        error_count += 1
                    continue

                resp = requests.get(
                    test_url, headers=test_headers, timeout=10, verify=certifi.where()
                )
                if resp.status_code == 200:
                    with lock:
                        request_count[engine] += 1
                else:
                    with lock:
                        error_count += 1
            except requests.RequestException:
                with lock:
                    error_count += 1

        except requests.RequestException:
            with lock:
                error_count += 1

except subprocess.CalledProcessError:
    with lock:
        error_count += 1
except Exception:
    with lock:
        error_count += 1
except KeyboardInterrupt:
    print("\n❌ [red bold]CTRL + C detected, parsing stopped...[/red bold]")
    sys.exit(2)

console = Console()


EXCLUDED_DOMAINS = [
    "github.com",
    "zhihu.com",
    "policies.google",
    "chromewebstore.google.com",
    "news.google",
    "drive.google",
    "www.t-online.de",
    "developers.google.com",
    "payments.google.com",
    "tarifbestellen.t-online.de",
    "lotto.t-online.de",
    "support.yahoo-net.jp",
    "www.yahoo.co.jp",
    "www.yahoo.com",
    "stamp.yahoo.co.jp",
    "www.yahoo.com.tw",
    "www.yahoo-net.jp",
    "beian.miit.gov.cn",
    "dxzhgl.miit.gov.cn",
    "www.beian.gov.cn",
    "brand.story.t-online.de",
    "guce.yahoo.com",
    "yahoo.uservoice.com",
    "microsoft.com",
    "pay.google.com",
    "help.microsoft.com",
    "outlook.com",
    "go.microsoft.com",
    "help.google.com",
    "play.google.com",
    "support.google.com",
    "mail.google.com",
    "support.microsoft.com",
    "stripe.com",
    "docs.stripe.com",
    "linkedIn.com",
    "maps.google.com",
    "facebook.com",
    "instagram.com",
    "www.amazon.com",
    "www.paypal.com",
    "www.shopify.com",
    "support.stripe.com",
    "developer.cybersource.com",
    "www.cybersource.com",
    "stackoverflow.com",
    "www.stackoverflow.com",
    "community.developer.cybersource.com",
    "finance.yahoo.com",
    "woocommerce.com",
    "wordpress.org/support",
    "wordpress.org/",
    "www.youtube.com",
    "www.exploit-db.com",
    "www.ask.com",
    "en.wikipedia.org",
    "razorpay.com",
    "dashboard.razorpay.com",
    "login.authorize.net",
    "www.authorize.net",
    "trends.builtwith.com",
    "support.authorize.net",
    "sandbox.aaronline.com",
    "braintree.github.io",
    "www.cdn.amazon.in",
    "www.amazon.com.be",
    "www.google.com",
    "gemini.google",
    "youtubekids.com",
    "www.tradingview.com",
    "zhidao.baidu.com",
    "www.investing.com",
    "www.adyen.com",
    "www.clay.com",
    "apps.apple.com",
    "sg.finance.yahoo.com",
    "accounts.swisscows.com",
    "support.swisscows.com",
    "company.swisscows.com",
    "www.msn.com",
    "www.checkout.com",
    "fr.wikipedia.org",
    "payu.in",
    "www.bing.com",
    "www.worldpay.com",
    "payment.ipay88.com",
    "www.skrill.com",
    "www.payoneer.com",
    "mathematica.stackexchange.com",
    "cloud.google.com",
    "help.disneyplus.com",
    "www.facebook.com",
    "auth.alipay.com",
    "www.sci-tech-today.com",
    "intl.alipay.com",
    "render.alipay.com",
    "globalprod.alipay.com",
    "www.uber.com",
    "www.2checkout.com",
    "www.ipay88.com.ph",
    "https://search.yahoo.co.jp",
    "www.mikrotik.com",
    "mikrotik.com",
    "www.sezzle.com",
    "ipay88.co.id",
    "au.finance.yahoo.com",
    "www.epay.com",
    "www.linkedin.com",
    "www.braintreepayments.com",
    "developer.paypal.com",
    "demo.activeitzone.com",
    "www.reddit.com",
    "www.twitter.com",
    "support.enom.com",
    "www.godaddy.com",
    "support.spotify.com",
    "help.zoho.com",
    "discussions.apple.com",
    "help.dropbox.com",
    "www.bigcommerce.com",
    "pay.amazon.com",
    "gitlab.com",
    "wallet-docs.brave.com/",
    "support.brave.com",
    "help.brave.com",
    "www.brave.com",
    "www.laptop-updates.brave.com",
    "documentation.brave.com",
    "community.brave.com",
    "status.brave.app",
    "store.brave.com",
    "twitter.com",
    "creators.brave.com",
    "account.brave.com",
    "ads.brave.com",
    "api-dashboard.search.brave.com",
    "ads-help.brave.com",
    "www.zhihu.com",
    "developers.meta.com",
    "www.namecheap.com",
    "https://wordpress.org/support/topic",
    "mail.yahoo.com",
    "help.yahoo.com",
    "login.yahoo.com",
    "images.search.yahoo.com",
    "video.search.yahoo.com",
    "news.search.yahoo.com",
    "r.search.yahoo.com",
    "search.yahoo.com",
    "shopify.dev",
    "brave.com",
    "search.brave.com",
    "laptop-updates.brave.com",
    "wallet-docs.brave.com",
    "codeshack.io",
    "donate.wikimedia",
    "baidu.com",
    "yandex.com",
    "cloud.yandex.com",
    "apps.microsoft.com",
    "www.microsoft.com",
    "hackerone.com/brave",
    "mastodon.social",
    "yandex.ru",
    "alice.yandex.ru",
    "passport.yandex.ru",
    "help.yandex.ru",
    "mail.yandex.ru",
    "support.yandex.ru",
    "cloud.yandex.ru",
    "alice.yandex.com",
    "passport.yandex.com",
    "help.yandex.com",
    "mail.yandex.com",
    "support.yandex.com",
    "www.yandex.com",
    "www.yandex.ru",
    "us.mail.yahoo.com",
    "sports.yahoo.com",
    "chat.yahoo.com",
    "shopping.yahoo.com",
    "advertising.yahoo.com",
    "devforum.roblox.com",
    "rewards.bing.com",
    "yahoo.co.jp",
    "https://search.yahoo.com",
    "www.search.yahoo.co.jp",
    "https://www.search.yahoo.co.jp",
    "search.yahoo.co.jp",
    "www.lycorp.co.jp",
    "moniker.com",
    "btoptout.yahoo.co.jp",
    "help.yahoo.co.jp",
    "support.yahoo.co.jp",
    "forum.yahoo.co.jp",
    "shopping.yahoo.co.jp",
    "mail.yahoo.co.jp",
    "auctions.yahoo.co.jp",
    "paypayfleamarket.yahoo.co.jp",
    "news.yahoo.co.jp",
    "r.search.aol.com",
    "www.wow.com/click",
    "www.google.com/search",
    "www.bing.com/search",
    "yandex.com/search",
    "duckduckgo.com/?q=",
    "www.ecosia.org/search",
    "www.startpage.com/do/search",
    "www.metacrawler.com/serp",
    "google.com",
    "bing.com",
    "yahoo.com",
    "duckduckgo.com",
    "startpage.com",
    "reddit.com",
    "search.aol.com",
    "https://search.aol.com/click/rdclks/",
    "aol.com",
    "wow.com",
    "https://www.wow.com/search",
    "bing.com/aclick",
    "google.com/url",
    "search.yahoo.com/click",
    "yandex.com/clck",
    "startpage.com/do/search",
    "search.brave.com/redirect",
    "ask.com/web?",
    "t-online.de/suche?",
    "wow.com/click",
    "metacrawler.com/serp",
    "ecosia.org/search",
    "yandex.ru/clck",
    "yahoo.co.jp/clck",
    "https://www.t-online.de",
    "https://www.ask.com",
    "https://yandex.ru/clck",
    "https://yahoo.co.jp/clck",
    "fankui.sogou.com",
    "wap.sogou.com",
    "weixin.sogou.com",
    "sogou.com",
    "sogou.com/web",
    "mingyi.sogou.com",
    "scholar.sogou.com",
    "wap.gouwu.sogou.com",
    "m.v.sogou.com",
    "english.sogou.com",
    "zhihu.sogou.com",
    "www.lycbiz.com",
    "corp.sogou.com",
    "m.yahoo.co.jp",
    "support.yahoo-net.jp/SccSearch",
    "www.impots.gouv.fr",
    "msn.com",
    "www.wow.com/search",
    "policies.google.com",
    "help.bing.microsoft.com",
    "jingyan.baidu.com",
    "https://www.wow.com/click",
    "myaccount.microsoft.com",
    "www.wow.com/search?q=",
    "uzone.id",
    "english.stackexchange.com",
    "vulnweb.com",
    "www.googleguide.com",
    "community.sap.com",
    "ahrefs.com",
    "www.ntt-finance.co.jp",
    "youtube.com",
    "youtu.be",
    "tiktok.com",
    "www.tiktok.com",
    "vk.com",
    "www.vk.com",
    "pinterest.com",
    "www.pinterest.com",
    "old.reddit.com",
    "np.reddit.com",
    "quora.com",
    "www.quora.com",
    "tumblr.com",
    "www.tumblr.com",
    "medium.com",
    "www.medium.com",
    "flickr.com",
    "www.flickr.com",
    "dribbble.com",
    "www.dribbble.com",
    "behance.net",
    "www.behance.net",
    "discord.com",
    "discord.gg",
    "www.discord.com",
    "canary.discord.com",
    "www.mastodon.social",
    "slack.com",
    "www.slack.com",
    "stackexchange.com",
    "math.stackexchange.com",
    "superuser.com",
    "serverfault.com",
    "www.github.com",
    "gist.github.com",
    "api.github.com",
    "www.gitlab.com",
    "bitbucket.org",
    "www.bitbucket.org",
    "npmjs.com",
    "www.npmjs.com",
    "yarnpkg.com",
    "www.yarnpkg.com",
    "pypi.org",
    "www.pypi.org",
    "dict.naver.com",
    "msearch.shopping.naver.com",
    "m.kin.naver.com",
    "naver.com",
    "nid.naver.com",
    "m.cafe.naver.com",
    "aws.amazon.com",
    "console.aws.amazon.com",
    "s3.amazonaws.com",
    "cloudflare.com",
    "www.cloudflare.com",
    "heroku.com",
    "www.heroku.com",
    "netlify.com",
    "www.netlify.com",
    "vercel.com",
    "www.vercel.com",
    "digitalocean.com",
    "www.digitalocean.com",
    "azure.com",
    "portal.azure.com",
    "firebase.google.com",
    "cloudfunctions.net",
    "bbc.com",
    "www.bbc.com",
    "cnn.com",
    "www.cnn.com",
    "nytimes.com",
    "www.nytimes.com",
    "bloomberg.com",
    "www.bloomberg.com",
    "theguardian.com",
    "www.theguardian.com",
    "reuters.com",
    "www.reuters.com",
    "forbes.com",
    "www.forbes.com",
    "ebay.com",
    "www.ebay.com",
    "aliexpress.com",
    "www.aliexpress.com",
    "alibaba.com",
    "www.alibaba.com",
    "tokopedia.com",
    "www.tokopedia.com",
    "bukalapak.com",
    "www.bukalapak.com",
    "shopee.com",
    "www.shopee.com",
    "paypal.com",
    "venmo.com",
    "www.venmo.com",
    "www.stripe.com",
    "adyen.com",
    "support.apple.com",
    "developer.apple.com",
    "developer.microsoft.com",
    "docs.microsoft.com",
    "help.netflix.com",
    "forum.gamer.com",
    "help.spotify.com",
    "community.spotify.com",
    "help.twitter.com",
    "support.twitter.com",
    "help.instagram.com",
    "help.facebook.com",
    "support.facebook.com",
    "help.pinterest.com",
    "help.reddit.com",
    "support.reddit.com",
    "wikipedia.org",
    "es.wikipedia.org",
    "de.wikipedia.org",
    "wiktionary.org",
    "wikidata.org",
    "wikivoyage.org",
    "wikinews.org",
    "archive.org",
    "www.archive.org",
    "wayback.archive.org",
    "change.org",
    "www.change.org",
    "avaaz.org",
    "www.avaaz.org",
    "sourceforge.net",
    "www.sourceforge.net",
    "osdn.net",
    "www.osdn.net",
    "softonic.com",
    "www.softonic.com",
    "uptodown.com",
    "www.uptodown.com",
    "filehippo.com",
    "www.filehippo.com",
    "cnet.com",
    "download.cnet.com",
    "wordpress.com",
    "www.wordpress.com",
    "wordpress.org",
    "www.wordpress.org",
    "blogspot.com",
    "www.blogspot.com",
    "blogger.com",
    "www.blogger.com",
    "dev.to",
    "www.dev.to",
    "tinyurl.com",
    "bit.ly",
    "goo.gl",
    "t.co",
    "ow.ly",
    "buff.ly",
    "is.gd",
    "rebrand.ly",
    "shorte.st",
    "archive.is",
    "archive.today",
    "pastebin.com",
    "www.pastebin.com",
    "linktr.ee",
    "about.me",
    "docs.google.com",
    "drive.google.com",
    "sites.google.com",
]


def load_proxies():
    global proxies, proxies_count

    proxies = []
    try:
        with open("proxies.txt", "r", encoding="utf-8") as file:
            for line in file:
                proxy = line.strip()
                if not proxy or proxy.startswith("#"):
                    continue

                if not re.match(r"^\w+://", proxy):
                    proxy = "http://" + proxy

                match = re.match(
                    r"^(?P<scheme>\w+)://(?:(?P<user>[^:@]+):(?P<pass>[^@]+)@)?(?P<host>[^:]+):(?P<port>\d+)$",
                    proxy,
                )
                if match:
                    proxies.append(proxy)

        proxies_count = len(proxies)
        if proxies_count == 0:
            proxies = []
            proxies_count = 0

    except FileNotFoundError:
        proxies = []
        proxies_count = 0


def parsed_dork_done():
    global dork_count, parsed_dork_count
    with lock:
        dork_count += 1
        parsed_dork_count += 1


def get_random_proxy():
    if proxies:
        return random.choice(proxies)
    return None


proxy = get_random_proxy()
if proxy:
    if "@" in proxy:
        proxy_auth = f"http://{proxy}"
    else:
        parts = proxy.split(":")
        if len(parts) == 4:
            ip, port, user, password = parts
            proxy_auth = f"http://{user}:{password}@{ip}:{port}"
        else:
            proxy_auth = f"http://{proxy}"
else:
    proxy_auth = None

proxies_dict = {"http": proxy_auth, "https": proxy_auth} if proxy_auth else None


def update_metrics(
    engine=None,
    requests=0,
    valid_urls=0,
    all_urls=0,
    errors=0,
    retries=0,
    dorks=0,
    parsed_dorks=0,
):
    global valid_url_count, all_url_count, error_count, retry_count, dork_count
    global request_count, parsed_dork_count

    with lock:
        if engine:
            request_count[engine] += requests
        valid_url_count += valid_urls
        all_url_count += all_urls
        error_count += errors
        retry_count += retries
        dork_count += dorks
        parsed_dork_count += parsed_dorks


def generate_stats_table():

    load_proxies()

    elapsed_time = time.time() - start_time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    table = Table(box=box.MINIMAL, style="grey93")
    table.add_column(
        "[bold yellow]Information[/bold yellow]", justify="left", style="grey93"
    )
    table.add_column(
        "[bold yellow]Value[/bold yellow]", justify="right", style="grey93"
    )

    table.add_row(
        "[light_goldenrod1]⟡ Time[/light_goldenrod1]",
        f"[purple]{current_time}[/purple]",
    )
    table.add_row(
        "[grey93]──────────────────────[/grey93]", "[grey93]──────────────[/grey93]"
    )

    for engine, count in request_count.items():
        rpm = (count / elapsed_time) * 60 if elapsed_time > 0 else 0
        table.add_row(f"[yellow]{engine}[/yellow]", f"[white]{rpm:.2f} RPM[/white]")

    table.add_row(
        "[grey93]──────────────────────[/grey93]", "[grey93]──────────────[/grey93]"
    )
    table.add_row(
        "[white]▣[/white][white] Total Dorks[/white]", f"[white]{total_dorks:,}[/white]"
    )
    table.add_row(
        "[white]▣[/white][white] Proxies[/white]", f"[white]{proxies_count:,}[/white]"
    )
    table.add_row(
        "[white]▣[/white][green3] All URLs[/green3]",
        f"[green3]{all_url_count:,}[/green3]",
    )
    table.add_row(
        "[white]▣[/white][green1] Valid URLs[/green1]",
        f"[green1]{valid_url_count:,}[/green1]",
    )
    table.add_row(
        "[white]▣[/white][orange_red1] Retries[/orange_red1]",
        f"[orange_red1]{retry_count:,}[/orange_red1]",
    )
    table.add_row(
        "[white]▣[/white][red3] Errors[/red3]", f"[red3]{error_count:,}[/red3]"
    )

    return table


seen_urls = set()


def is_valid_scheme(url):
    return url.scheme in {"http", "https"}


def has_query_params(url):
    return bool(url.query)


def is_redirect_url(url, href, excluded_redirects):
    return any(pattern in href for pattern in excluded_redirects)


def is_excluded_domain(main_domain, excluded_domains):
    return main_domain in excluded_domains


def is_excluded_path(url_path, excluded_paths):
    return any(url_path.startswith(path) for path in excluded_paths)


def is_excluded_content_path(url_path, excluded_content_paths):
    return any(p in url_path.lower() for p in excluded_content_paths)


def is_excluded_pattern(href, patterns):
    return any(p in href for p in patterns)


def normalize_url(parsed_url):
    query_tuples = sorted(parse_qsl(parsed_url.query))
    normalized_query = urlencode(query_tuples)
    return (
        f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{normalized_query}"
    )


RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%d-%m-%y")
RESULTS_FILENAME = os.path.join(RESULTS_DIR, f"results-{timestamp}.txt")


def extract_and_save_links(soup, filename=RESULTS_FILENAME):
    global all_url_count, valid_url_count

    raw_links_found = soup.find_all("a", href=True)
    raw_count = len(raw_links_found)

    EXCLUDED_REDIRECTS = {
        "bing.com/aclick",
        "google.com/url",
        "search.yahoo.com/click",
        "yandex.com/clck",
        "startpage.com/do/search",
        "search.brave.com/redirect",
        "ask.com/web?",
        "t-online.de/suche?",
        "wow.com/click",
        "metacrawler.com/serp",
        "ecosia.org/search",
        "support.yahoo-net.jp",
        "fankui.sogou.com",
        "wap.sogou.com",
        "weixin.sogou.com",
        "sogou.com",
        "sogou.com/web",
        "mingyi.sogou.com",
        "scholar.sogou.com",
        "wap.gouwu.sogou.com",
        "m.v.sogou.com",
        "english.sogou.com",
        "zhihu.sogou.com",
        "www.lycbiz.com",
        "btoptout.yahoo.co.jp",
        "corp.sogou.com",
        "m.yahoo.co.jp",
        "www.wow.com/search",
        "www.wow.com/click",
        "myaccount.microsoft.com",
        "www.wow.com/search?q=",
    }

    urls_saved = set()

    with lock:
        all_url_count += raw_count

    for link in raw_links_found:
        href = unquote(link["href"])
        parsed_url = urlparse(href)

        if not is_valid_scheme(parsed_url):
            continue
        if not has_query_params(parsed_url):
            continue

        domain_parts = parsed_url.netloc.split(".")
        main_domain = (
            ".".join(domain_parts[-2:]) if len(domain_parts) > 1 else parsed_url.netloc
        )

        if is_excluded_domain(main_domain, EXCLUDED_DOMAINS):
            continue
        if is_excluded_path(parsed_url.path, EXCLUDED_PATHS):
            continue
        if is_excluded_content_path(parsed_url.path, EXCLUDED_CONTENT_PATHS):
            continue
        if is_excluded_pattern(href, EXCLUDED_PATTERNS):
            continue
        if is_excluded_pattern(href, EXCLUDED_REDIRECTS):
            continue

        normalized_url = normalize_url(parsed_url)

        with lock:
            if normalized_url in seen_urls:
                continue
            seen_urls.add(normalized_url)

            with open(filename, "a", encoding="utf-8") as file:
                file.write(normalized_url + "\n")
                file.flush()
                os.fsync(file.fileno())

            valid_url_count += 1
            urls_saved.add(normalized_url)

    return urls_saved


def search_dork(engine, dork, live):
    global retry_count, error_count, dork_count, ssl_context, MAX_PAGES

    for page in range(1, MAX_PAGES + 1):
        timestamp = int(time.time())

        formatted_page = (
            (page - 1) * 10
            if engine
            in [
                "Google",
                "Bing",
                "Yahoo",
                "Yandex",
                "StartPage",
                "Brave",
                "Bing News",
                "DuckDuckGo",
            ]
            else page
        )

        platforms = [
            '"Windows"',
            '"macOS"',
            '"Linux"',
            '"Android"',
            '"iOS"',
            '"Chrome OS"',
        ]
        asw = random.choice(platforms)

        ref = random.choice(EXCLUDED_DOMAINS)

        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0, no-cache, no-store, must-revalidate",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-language": "en-US,en;q=0.6",
            "Pragma": "no-cache",
            "Accept": "*/*",
            "Referer": ref,
            "Expires": "0",
            "DNT": "1",
            "date": datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT"),
            "Upgrade-Insecure-Requests": "1",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Ch-Ua-Platform": asw,
        }

        if engine not in SEARCH_ENGINES:
            with lock:
                error_count += 1
            live.update(generate_stats_table())
            continue

        search_url = SEARCH_ENGINES[engine].format(
            query=dork, page=formatted_page, timestamp=timestamp
        )

        proxy_handler = urllib.request.ProxyHandler(
            {"http": f"http://{proxy}", "https": f"https://{proxy}"}
        )
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)

        try:
            with requests.Session() as session:
                response = session.get(
                    search_url,
                    headers=headers,
                    proxies=proxies_dict,
                    timeout=PROXY_TIMEOUT,
                    verify=(PEM_PATH if os.path.exists(PEM_PATH) else certifi.where()),
                )

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "lxml")
                    links = extract_and_save_links(soup, RESULTS_FILENAME)

                    if links:
                        update_metrics(
                            engine,
                            requests=1,
                            valid_urls=len(links),
                            all_urls=len(links),
                        )

                    live.update(generate_stats_table())

                elif response.status_code in [403, 429]:
                    with lock:
                        retry_count += 1
                    sleep_time = min(2**retry_count, 32)
                    time.sleep(sleep_time)
                    live.update(generate_stats_table())

        except requests.Timeout:
            with lock:
                retry_count += 1
            sleep_time = min(2**error_count, 32)
            time.sleep(sleep_time)

        except requests.exceptions.SSLError:
            try:
                with requests.Session() as session:
                    response = session.get(
                        search_url,
                        headers=headers,
                        proxies=proxies_dict,
                        timeout=PROXY_TIMEOUT,
                        verify=certifi.where(),
                    )

                    if response.status_code == 200:
                        warnings.filterwarnings(
                            "ignore", category=XMLParsedAsHTMLWarning
                        )
                        soup = BeautifulSoup(response.text, "lxml")
                        links = extract_and_save_links(soup, RESULTS_FILENAME)

                        if links:
                            update_metrics(
                                engine,
                                requests=1,
                                valid_urls=len(links),
                                all_urls=len(links),
                            )

                        live.update(generate_stats_table())

            except requests.RequestException:
                with lock:
                    error_count += 1
                live.update(generate_stats_table())

        except requests.exceptions.RequestException:
            with lock:
                error_count += 1
            live.update(generate_stats_table())
        except subprocess.CalledProcessError:
            with lock:
                error_count += 1
            live.update(generate_stats_table())
        except Exception:
            with lock:
                error_count += 1
            live.update(generate_stats_table())

        # Setelah dork diproses, update counter (parsed_dork_count)
        with lock:
            dork_count += 1
            parsed_dork_count += 1
            live.update(generate_stats_table())

    with lock:
        if dork_count >= total_dorks:
            parsing_active = False


def load_dorks(dork_file):

    global total_dorks
    try:
        with open(dork_file, "r", encoding="utf-8") as file:
            dorks = [line.strip() for line in file if line.strip()]
            total_dorks = len(dorks)
        return dorks
    except FileNotFoundError:
        total_dorks = 0
        return []


def run_dork_parser(dork_file):
    global total_dorks, dork_count, error_count
    parsing_active = True

    dorks = load_dorks(dork_file)
    total_dorks = len(dorks)

    if not dorks:
        return

    with Live(generate_stats_table(), refresh_per_second=1, console=console) as live:

        def update_live():
            while parsing_active:
                time.sleep(1)
                with lock:
                    live.update(generate_stats_table())

        threading.Thread(target=update_live, daemon=True).start()

        futures = []
        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            engines = list(SEARCH_ENGINES.keys())

            futures = [
                executor.submit(
                    search_dork, engine, urllib.parse.quote_plus(dork), live
                )
                for dork in dorks
                for engine in engines
            ]

            for future in concurrent.futures.as_completed(futures):
                future.result()

            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    error_count += 1

            dork_count += 1

    parsing_active = False
    console.print(
        "\n✅ [green bold]Parsing success! Results saved to 'results.txt'[/green bold]"
    )


def _run(cmd, *, check=True):
    r = subprocess.run(cmd, text=True, capture_output=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} -> {r.returncode}\n{r.stderr.strip()}")
    return r.stdout.strip()


def self_update_from_git() -> None:
    try:
        _run(["git", "rev-parse", "--is-inside-work-tree"])
        before = _run(["git", "rev-parse", "HEAD"])
    except Exception as e:
        print(f"[SELF-UPDATE] Skip (not a git repo?): {e}")
        return

    try:
        # 2) fetch
        _run(["git", "fetch", "--all", "--prune"])

        # 3) try safe pull (tracking branch)
        try:
            _run(["git", "pull", "--rebase", "--autostash"])
        except Exception as e_pull:
            print(f"[SELF-UPDATE] pull failed, trying hard reset: {e_pull}")

            # 4) fallback reset --hard ke upstream
            upstream = None
            # coba HEAD@{upstream}
            try:
                upstream = _run(
                    ["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"]
                )
            except Exception:
                pass
            # fallback origin/main
            if not upstream:
                try:
                    _run(
                        [
                            "git",
                            "show-ref",
                            "--verify",
                            "--quiet",
                            "refs/remotes/origin/main",
                        ]
                    )
                    upstream = "origin/main"
                except Exception:
                    pass
            # fallback origin/master
            if not upstream:
                try:
                    _run(
                        [
                            "git",
                            "show-ref",
                            "--verify",
                            "--quiet",
                            "refs/remotes/origin/master",
                        ]
                    )
                    upstream = "origin/master"
                except Exception:
                    pass

            if not upstream:
                print("[SELF-UPDATE] No upstream found. Skip update.")
            else:
                try:
                    _run(["git", "reset", "--hard", upstream])
                    _run(["git", "clean", "-fd"])
                except Exception as e_reset:
                    print(f"[SELF-UPDATE] hard reset failed: {e_reset}")

        after = _run(["git", "rev-parse", "HEAD"])
        if before == after:
            print("[SELF-UPDATE] Up to date.")
            return

        print(f"[SELF-UPDATE] Updated: {before[:7]} -> {after[:7]}. Restarting...")

        # hentikan background task dengan aman jika ada
        for stopper in ("stop_autoupdate", "stop_heartbeat"):
            try:
                mod = sys.modules.get("__main__") or sys.modules[__name__]
                func = getattr(mod, stopper, None)
                if callable(func):
                    func(join=False)
            except Exception:
                pass

        # 5) restart proses
        os.execv(sys.executable, [sys.executable] + sys.argv)

    except Exception as e:
        pass


if __name__ == "__main__":
    try:
        self_update_from_git()
    except:
        pass
    if "--showcase" in sys.argv:
        showcase_all()
        sys.exit(0)

    init(label="DORKPASS", endpoints=["https://verif.stecu.cloud"], heartbeat_sec=7)

    if not gate(ui_style="v4"):
        sys.exit(1)

    try:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n      \x1b[1;37;41m   Dork Parser - KIANSANTANG DEV  \x1b[0m\n")
        print_info()

        # Input path dari user
        dork_path = input(
            f"\n {Fore.YELLOW}[+]{Fore.WHITE} Enter path to dork file ({Fore.RED}UTF-8{Fore.WHITE}): "
        ).strip()
        proxy_path = input(
            f"{Fore.YELLOW}[+]{Fore.WHITE} Enter path to proxy file ({Fore.RED}UTF-8{Fore.WHITE}) {Fore.RED}[press Enter to skip]{Fore.WHITE}: "
        ).strip()
        os.system("cls" if os.name == "nt" else "clear")

        # Update file proxy jika diberikan
        if proxy_path:
            PROXY_FILE = proxy_path

        # Load proxies dari file yang diberikan
        load_proxies()

        run_dork_parser(dork_path)

    except KeyboardInterrupt:
        print("\n❌ [red bold]CTRL + C detected, exiting...[/red bold]")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ [red bold]An error occurred: {e}[/red bold]")
        sys.exit(1)
    finally:
        stop_heartbeat(join=True)

    # os.system('git pull')

    # if os.path.exists("license.txt"):
    #     with open("license.txt", "r") as f:
    #         saved_license = f.read().strip()
    #     print("\n\n[\033[92m+\033[0m]   Verifying saved license...")
    #     name, remaining_days = verify_license_key(saved_license)
    #     if name:
    #         os.system("cls" if os.name == "nt" else "clear")
    #         print(f"\n\n      \x1b[1;37;41m   Dork Parser - KIANSANTANG DEV  \x1b[0m\n")
    #         print(f"\033[97m    Name: \033[92m{name}\033[97m\n   Expired: \033[92m{remaining_days}\033[0m\n")
    #         run_dork_parser("dorks.txt")
    #     else:
    #         print("Saved license is invalid or expired.")
    #         os.remove("license.txt")

    # else:
    #     print("No saved license found. Please enter your license key.")

    # os.system("cls" if os.name == "nt" else "clear")
    # os.system('git pull')
    # print(LOG)

    # user_input = input("\n\n[\033[92m#\033[0m] Enter License Key: ")

    # name, expiration_date = verify_license_key(user_input)

    # if name:
    #     os.system('git pull')
    #     os.system("cls" if os.name == "nt" else "clear")
    #     print(f"\n\n      \x1b[1;37;41m   Dork Parser - KIANSANTANG DEV  \x1b[0m\n")
    #     print(f"\033[97m    Name: \033[92m{name}\033[97m\n   Expired: \033[92m{expiration_date}\033[0m\n")
    #     run_dork_parser("dorks.txt")
    # else:
    #     print("Invalid or expired license key. Exiting...")

