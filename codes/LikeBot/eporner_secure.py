""" Decompiled by Exotic Hridoy """

import base64
import zlib
import marshal
import sys

def _X1O0X():
    import os as m
    import time
    import hashlib
    import json
    import tempfile
    import builtins
    import types
    import inspect
    import threading
    import importlib

    s = 0
    R = []
    W = 0

    try:
        MON = m.getenv('SECURE_MONITOR')
    except SystemExit:
        pass

    try:
        a = builtins.exec
        b = __builtins__['exec'] if isinstance(__builtins__, dict) else getattr(__builtins__, 'exec', None)
        c = getattr(sys.modules.get('builtins', builtins), 'exec', None)

        if not (a is b is c):
            s += 2
            R.append('exec_refs_inconsistent')

        if not callable(a):
            s += 2
            R.append('exec_not_callable')

        if not isinstance(a, types.BuiltinFunctionType):
            s += 2
            R.append('exec_not_builtin_type')

        if getattr(a, '__name__', '') != 'exec' or getattr(a, '__module__', '') not in ('builtins', '__builtin__'):
            s += 1
            R.append('exec_meta')

        tg = {}
        t0 = time.perf_counter()
        try:
            a('___X__=1', tg)
            dur = time.perf_counter() - t0
            if tg.get('___X__') != 1:
                s += 2
                R.append('exec_fun_mismatch')
            if dur > 0.1:
                W += 1
                R.append('exec_slow')
        except Exception as e:
            s += 2
            R.append('exec_call_exc:' + type(e).__name__)

        gt = getattr(sys, 'gettrace', None)
        if gt and gt() is not None:
            s += 1
            R.append('sys_gettrace_set')

        gp = getattr(sys, 'getprofile', None)
        if gp and gp() is not None:
            s += 1
            R.append('sys_getprofile_set')

        for th in threading.enumerate():
            if getattr(th, '_trace_hook', None):
                continue
            if getattr(th, '_target', None) and getattr(th, 'daemon', False) == False:
                pass

        mods = set(k.lower() for k in sys.modules.keys())
        suspicious_modules = [
            'pydevd', 'pdb', 'debugpy', 'frida', 'ptrace', 'gdb',
            'ltrace', 'bpython', 'ipykernel', 'rr', 'rrtrace'
        ]
        hits = [m for m in suspicious_modules if any(m in k for k in mods)]
        if hits:
            s += 1
            R.append('susp_modules:' + ','.join(hits))

        odd = 0
        mp = getattr(sys, 'meta_path', [])
        for it in mp:
            modn = (getattr(it, '__module__', '') or '').lower()
            if modn.startswith('importlib') or '_frozen_importlib' in modn or 'pkgutil' in modn:
                continue
            if 'pkg_resources' in modn or 'importlib_metadata' in modn:
                continue
            odd += 1
            R.append('meta_path_unusual:' + modn)
        if odd > 1:
            s += 1

        lp = m.getenv('LD_PRELOAD')
        if lp:
            parts = [p for p in lp.split(':') if p]
            missing = 0
            badname = 0
            sysok = 0

            safe_prefixes = (
                '/lib', '/usr/lib', '/system', '/vendor',
                '/data/data/com.termux', '/data/adb/modules'
            )
            suspect_names = (
                'frida', 'inject', 'ltrace', 'ptrace', 'gdb',
                'frida-agent', 'substrate', 'xposed'
            )

            for p in parts:
                if not p or not m.path.isabs(p) or not m.path.exists(p):
                    missing += 1

                n = m.path.basename(p).lower()
                for sn in suspect_names:
                    if sn in n:
                        badname += 1
                        break

                for sp in safe_prefixes:
                    if p.startswith(sp):
                        sysok += 1
                        break

            if (missing > 0 or badname > 0) and sysok != len(parts):
                s += 2
                R.append(f'LD_PRELOAD_susp missing={missing} badname={badname}')

        if sys.platform.startswith('linux'):
            p = '/proc/self/status'
            if m.path.exists(p):
                try:
                    for L in open(p, 'r').read().splitlines():
                        if L.startswith('TracerPid:'):
                            tp = int(L.split(':', 1)[1].strip())
                            if tp > 0:
                                s += 3
                                R.append('ptrace_attached')
                            break
                except Exception:
                    pass

        bd = getattr(builtins, '__dict__', None)
        if not isinstance(bd, dict):
            s += 2
            R.append('builtins_not_dict')
        else:
            miss = []
            for k in ['exec', 'eval', 'compile', 'open', '__import__']:
                if k not in bd:
                    miss.append(k)
                elif k in ['exec', 'eval', 'compile', '__import__'] and not callable(bd.get(k)):
                    miss.append(k + '_not_callable')
            if miss:
                s += 2
                R.append('builtins_core_miss:' + ','.join(miss))

        mp = getattr(sys, 'meta_path', [])
        unusual = [
            getattr(i, '__class__', type(i)).__name__
            for i in mp
            if not (getattr(i, '__module__', '') or '').startswith('importlib')
            and 'pkgutil' not in (getattr(i, '__module__', '') or '')
        ]
        if len(unusual) > 2:
            s += 1
            R.append('meta_path_unusual_classes:' + ','.join(unusual[:5]))

        try:
            g = {}
            c = compile('z=1', '<g>', 'exec')
            exec(c, g)
            if g.get('z') != 1:
                s += 2
                R.append('compile_exec_fail')
        except Exception:
            pass

        try:
            t0 = time.perf_counter()
            total = 0
            for i in range(3):
                a = compile('x=1', '<t>', 'exec')
                exec(a, {})
                total += 1
            dur = time.perf_counter() - t0
            if dur > 0.5:
                W += 1
                R.append('timing_slow')
            if W and s > 0:
                s += 1
        except Exception:
            pass

        try:
            pfn = m.path.abspath(sys.argv[0]) if sys.argv else None
            if pfn and m.path.exists(pfn):
                d = open(pfn, 'rb').read()
                h = hashlib.sha256(d).hexdigest()
                REF = None
                if REF and h != REF:
                    s += 3
                    R.append('self_hash_mismatch')
        except Exception:
            pass

        th = 4
        try:
            if any(x in (m.getenv('PREFIX') or '') for x in ['com.termux', '/data/data/com.termux']):
                th = 5
        except Exception:
            pass

        diag = {
            'susp': s,
            'reasons': R,
            'time': time.time(),
            'env': {
                'ld': m.getenv('LD_PRELOAD'),
                'trace': bool(sys.gettrace())
            }
        }

        try:
            td = tempfile.gettempdir()
            fn = m.path.join(td, 'secure_diag.json')
            open(fn, 'w').write(json.dumps(diag))
        except Exception:
            pass

        if s >= th:
            msg = f'[SECURE-ADV] suspicious={s} reasons={R}'
            sys.stderr.write(msg + '\n')
            if MON:
                return (False, diag)
            sys.exit(1)

        return (True, diag)

    except Exception as e:
        sys.stderr.write(f'[SECURE-ADV-ERR]{e}\n')
        try:
            return (True, {'err': str(e)})
        except Exception:
            return (True, {})


__PAYLOAD_B64__ = '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'

def _run():

    _ok, _diag = _X1O0X()
    if not _ok:
        sys.stderr.write('[LOADER] monitor-mode: secure check failed, dumping diag\n')
        sys.stderr.write(str(_diag) + '\n')
        sys.exit(1)

    payload = base64.b64decode(__PAYLOAD_B64__)
    data = zlib.decompress(payload)
    co = marshal.loads(data)
    glb = {
        '__name__': '__main__',
        '__file__': sys.argv[0] if len(sys.argv) > 0 else '<stdin>'
    }
    exec(co, glb)

if __name__ == '__main__':
    _run()
