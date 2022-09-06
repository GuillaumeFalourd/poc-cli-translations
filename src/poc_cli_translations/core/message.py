import i18n
import json
import locale
import os
import sys
import ctypes
from pathlib import Path
from typing import Optional
from poc_cli_translations import LANGUAGE_FILE

translations_path = str(Path.cwd()) + '/src/poc_cli_translations/core/translations'
   
    
def translate(key: str, content: Optional[str] = None):
    lang = __check_lang()
    i18n.set('locale', lang)
    i18n.load_path.append(translations_path)
    if content is not None:
        msg = i18n.t(f'stk.{key}', name=content)
    else:
        msg = i18n.t(f'stk.{key}')
    print(msg)

  
def __check_lang() -> str: 
    try:
        if not LANGUAGE_FILE.exists():
            if sys.platform in ["linux", "darwin"]:
                lang = os.environ['LANG']
            else: # win32 = windows
                windll = ctypes.windll.kernel32
                windll.GetUserDefaultUILanguage()
                lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]
            return lang.split('_')[0] # get en from en_US.UTF-8
        else:
            return __get_language_file()
            
    except Exception:
        return 'en'


def __get_language_file():
    with open(LANGUAGE_FILE, "r", encoding="utf-8") as language_file:
        return json.loads(language_file.read())
    