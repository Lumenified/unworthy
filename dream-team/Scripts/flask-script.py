#!d:\projects\worksp~1\secret\mbithe~1\dream-~1\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'flask==0.12','console_scripts','flask'
__requires__ = 'flask==0.12'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('flask==0.12', 'console_scripts', 'flask')()
    )
