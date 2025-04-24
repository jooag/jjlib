import pydata_google_auth as pga
from ._util import rootdir
from pydata_google_auth.exceptions import PyDataCredentialsError
import os.path as osp
import os
import hashlib

def load_user_cred():    
    creds_path = rootdir / 'credentials.json'
    try:
        creds = pga.load_user_credentials(creds_path)
    except:
        pga.save_user_credentials(['https://www.googleapis.com/auth/bigquery'], creds_path)
        creds = pga.load_user_credentials(creds_path)
    
    return creds

default_cred = load_user_cred()