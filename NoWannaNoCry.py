from src import nwnc
import sys
if sys.platform != 'win32':
    sys.exit('This script is meant to be run on a Windows machine.'
             ' Only Windows machines are vulnerable to WCry.')

if sys.getwindowsversion().platform != 2:
    sys.exit('Your Windows version is not supported by this script'
             ' (and probably not vulnerable).')
if __name__ == '__main__':
    try:
        nwnc.mitigate()
        input('\r\nDone. Press any key to exit.')
    except Exception as e:
        sys.exit(e)