from pathlib import Path
import platform
import os
import os.path as osp
import hashlib

plat = platform.system().upper()
rootdir = Path.home()
match plat:
    case 'LINUX':
        rootdir /= '.config'
    case 'DARWIN':
        rootdir /= '.config'
    case 'WINDOWS':
        rootdir /= 'AppData' / 'Roaming'
venv_id = ''    
if 'VIRTUAL_ENV' in os.environ:
    venv_id = os.environ['VIRTUAL_ENV']
    hs = hashlib.md5()
    hs.update(venv.encode('ascii'))
    venv_id = hs.hexdigest()
rootdir /= 'JJLIB' / venv_id

