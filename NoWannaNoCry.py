from src import nwnc
import sys
if sys.platform != 'win32':
    sys.exit('This script is meant to be run on a Windows machine.'
             ' Only Windows machines are vulnerable to WCry.')

if sys.getwindowsversion().platform != 2:
    sys.exit('Your Windows version is not supported by this script'
             ' (and probably not vulnerable).')
def action():
    name = raw_input('\r\nDo you want to continue? \r\n[D]isable SMB\r\n[F]ix SMB \r\n[A]ll\n')
    if name.lower() == 'd':
        nwnc.mitigate()
    elif name.lower() == 'f':
        nwnc.fix()
    elif name.lower() == 'a':
        nwnc.mitigate()
        nwnc.fix()
    else:
        action()
if __name__ == '__main__':
    print('NoWannaNoCry to help mitigate against the WCry/WannaCry malware.\nSource code: https://github.com/thienphung/NoWannaNoCry \n')
    try:
        if nwnc.check() is not True:
            action()
        input('\r\nDone. Press any key to exit.')
    except Exception as e:
        sys.exit(e)