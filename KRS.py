#coding=utf-8

import os, sys, platform

os.system('xdg-open https://www.facebook.com/groups/207678473842318/')

try:

    if sys.argv[1]=='update':

        os.system('rm -rf FILE64.cpython-311.so FILE32.cpython-311.so')

except:

    pass

os.system('rm -rf FILE64.cpython-311.so FILE32.cpython-311.so')

os.system('git pull')

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('FILE64.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/TEAM-KRS/DATA/main/FILE64.cpython-311.so > FILE64.cpython-311.so') 

        os.system("chmod 777 FILE64*")
        
        import FILE64

    else:

        import FILE64

elif bit == '32bit':

    if not os.path.isfile('FILE32.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/TEAM-KRS/DATA/main/FILE32.cpython-311.so > FILE32.cpython-311.so')

        os.system("chmod 777 FILE32*")

        import FILE32

    else:

        import FILE32
