# -*- coding: utf-8 -*-
from src import nwnc
import sys
if sys.platform != 'win32':
    sys.exit('This script is meant to be run on a Windows machine.'
             ' Only Windows machines are vulnerable to WCry.')

if sys.getwindowsversion().platform != 2:
    sys.exit('Your Windows version is not supported by this script'
             ' (and probably not vulnerable).')
def action(str):
    name = raw_input('\rDo you want to %s? [Y/n]' % str)
    if name.lower() != 'n':
        if str == 'install':
            nwnc.fix()
        elif str == 'disable':
            nwnc.mitigate()
if __name__ == '__main__':
    print('NoWannaNoCry to help mitigate against the WCry/WannaCry malware.\nSource code: https://github.com/thienphung/NoWannaNoCry \n')
    try:
        fix_installed = nwnc.check_installed_kbs()
        if fix_installed is not True:
            action('install')
        smb_v1_disabled = nwnc.check_smb_v1()
        if smb_v1_disabled is not True:
            action('disable', nwnc.mitigate())
        not_vulnerable = fix_installed or smb_v1_disabled
        print('The system is {}vulnerable.'.format('not ' if not_vulnerable else ''))
        input('\r\nDone. Press any key to exit.')
    except Exception as e:
        sys.exit(e)