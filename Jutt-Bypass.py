import os, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('bypass64.cpython-311.so'):
        os.system('curl https://raw.githubusercontent.com/ITX-SANAN/tt/main/bypass64.cpython-311.so > bypass64.cpython-311.so')
        import bypass64
elif bit == '32bit':
    if not os.path.isfile('bypass32.cpython-311.so'):
        os.system('curl https://raw.githubusercontent.com/ITX-SANAN/tt/main/bypass32.cpython-311.so > bypass32.cpython-311.so')
        import bypass32
