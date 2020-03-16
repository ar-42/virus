import os, sys
print '\x1b[1;32mSudah punya ID dan Password nya?'
print '\x1b[1;32mSilahkan Login '
import os, sys

def wa():
    os.system('xdg-open https://termux.id/cara-membuat-virus-termux-untuk-android')


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


user = raw_input('ID: ')
import getpass
sandi = raw_input('Password: ')
if sandi == 'ID' and user == 'Termux':
    print 'Anda Telah Login'
    sys.exit
else:
    print 'Login GAGAL, Silahkan ambil dulu id&passnya di website aslinya!'
    wa()
    restart()

import os, sys, time
R = '\x1b[1;31m'
N = '\x1b[0m'
Y = '\x1b[1;33m'
G = '\x1b[1;37m'

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    curdir = os.getcwd()


def banner():
    print '%s        _                            _               %s' % (R, N)
    print '%s   _ _ | |_  _ _ %s ___    _____ %s ___ | |_  ___  ___   %s' % (R, Y, R, N)
    print "%s  | | || . || | |%s| . |  |     |%s| .'|| '_|| -_||  _|  %s" % (R, Y, R, N)
    print '%s   \\_/ |___||___|%s|_  |  | |_|_|%s|__,||_,_||___||_|    %s' % (R, Y, R, N)
    print '%s __________________| |  | |_______________________   %s' % (Y, N)
    print '%s|____________________|  |_________________________| %s' % (Y, N)


clear = lambda : os.system('clear')
clear()
banner()
print
print '%sVBu%sg M%saker %s19-07-2017 %s(5:29)%s' % (R, Y, R, G, Y, N)
print '%sAuthor         : %sAyip Bontos%s' % (G, R, N)
print '%sSupport        : %sKunjungi %swebsite Kami%s' % (G, R, Y, N)
print '%sWebsite        : %shttp://Termux.id%s' % (G, Y, N)
print '%sTentang        : %sTutorial Termux%s' % (G, R, N)
print '%sEpisode        : %sMembuat%svirus%s' % (G, Y, R, N)
print '%s@___%sSelamat%sBelajar%s_____%s' % (Y, G, R, Y, N)
print '%s* %sWork hard %s-- %sDon`t give up %s*%s\n' % (Y, G, R, G, Y, N)
enter = raw_input('%s[%s~%s]%s Tekan Enter Untuk Melanjutkan...%s' % (Y, R, Y, R, N))
clear()
banner()
print '%s#%s---------------%s    VBu%sg%s--%sM%saker    %s----------------%s#%s' % (R, Y, R, Y, R, Y, R, Y, R, N)
print '%s|%s We dont take responsibility for the use of this  %s|%s' % (Y, G, Y, N)
print '%s|%s program                                          %s|%s' % (Y, G, Y, N)
print '%s#%s---------------%s    -----------    %s----------------%s#%s' % (R, Y, R, Y, R, N)
print '%s|%s VBu%sg M%saker %sv1.0 19-07-2017 %s(5:29)                |%s' % (Y, R, Y, R, G, Y, N)
print '%s|%s Author  : Ayip Bontos                 %s|%s' % (Y, G, Y, N)
print '%s|%s Website : http://Termux.id            %s|%s' % (Y, G, Y, N)
print '%s|%s Contact : wa%s+62%s 82278198738                %s|%s' % (Y, G, R, G, Y, N)
print '%s|%s Version : 1.0 -- Storiku Project               %s|%s' % (Y, G, Y, N)
print '%s|%s Copyright (c) 2019, Termux.id All rights reserved %s|%s' % (Y, G, Y, N)
print '%s#%s---------------%s    -----------    %s----------------%s#%s' % (R, Y, R, Y, R, N)
print
print '%s[%s#%s]%s Options%s' % (Y, R, Y, G, N)
print '%s   {%s01%s} %s~> %sGenerate Virus for Android%s' % (R, G, R, Y, G, N)
print '%s   {%s02%s} %s~> %sGenerate Virus for Window %s' % (R, G, R, Y, G, N)
print '%s   {%s03%s} %s~> %sGenerate Virus for MacOSX %s' % (R, G, R, Y, G, N)
print '%s   {%s04%s} %s~> %sExit%s\n' % (R, G, R, Y, G, N)
opsi = raw_input('%sVIBUM%s > %sChoose ' % (R, Y, G))
print '%s' % N
if opsi.strip() in ('01 1').split():
    try:
        import anvima
    except ImportError:
        print '%s[%s!%s]%s ERROR%s: %sanvima%s:%s not found%s' % (Y, R, Y, R, Y, G, Y, G, N)
        sys.exit()

if opsi.strip() in ('02 2').split():
    try:
        import winvima
    except ImportError:
        print '%s[%s!%s]%s ERROR%s: %swinvima%s:%s not found%s' % (Y, R, Y, R, Y, G, Y, G, N)
        sys.exit()

if opsi.strip() in ('03 3').split():
    try:
        import macvima
    except ImportError:
        print '%s[%s!%s]%s ERROR%s: %smacvima%s:%s not found%s' % (Y, R, Y, R, Y, G, Y, G, N)
        sys.exit()

if opsi.strip() in ('04 4').split():
    sys.exit()
else:
    print '%s[%s!%s]%s ERROR: Wrong Input...%s' % (Y, R, Y, G, N)
    time.sleep(2)
    restart_program()
