#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Jutt.so brand.so')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Jutt.so'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/Jutt.cpython-311.so?raw=true -o Jutt.so')
        from Jutt import reg
        reg()
    else:
        from Jutt import reg
        reg()
elif bit == '32bit':
    if not os.path.isfile('brand.so'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/brand.cpython-311.so?raw=true -o brand.so')
        from brand import reg
        reg()
    else:
        from brand import reg
        reg()
