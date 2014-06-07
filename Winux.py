##====================================== Information ======================================
# Name                         : Winux
# Author                       : Daxeel Soni
# Currently supported commands : ls, echo, cal, cat, cd, mkdir, pwd ,cd, mv, rm, rmdir, date
# Version                      : 1.0.0 (Initial Release)
# Language                     : Python 3.3.3
##======================================= Source Code ======================================
#----------------------------------------IMPORTING MODULES---------------------------------
import os
import calendar
import time
#----------------------------------------LS COMMAND----------------------------------------
def ls():
    if ' ' not in x:
        for i in os.listdir():
            print(i)
#----------------------------------------ECHO COMMAND--------------------------------------
def echo():
    if x[5::] == '$HOME':
        print(os.path.expanduser('~'))
    elif x.count('"') == 2 and x[-1] == '"' and x[5] == '"':
            print(x[6:-1])
    else:
         print('Invalid syntax')
#----------------------------------------CAL COMMAND---------------------------------------
def cal(y,m):
    obj = calendar.TextCalendar(calendar.SUNDAY)
    obj.prmonth(y, m)
#----------------------------------------CAT COMMAND---------------------------------------
def cat():
    if x[3:6] == ' > ':
        if x[3] == ' ' and x[5] == ' ':
            f = open(x[6::] + '.txt','a')
            text = input('')
            if 'CLOSE' in text:
                f.write(text[0:-5])
            else:
                print('You forgot to write CLOSE at the end of text')
            f.close()
        else:
            print('Invalid syntax')
    elif x[3:7] == ' >> ':
        if os.path.isfile(x[7::] + '.txt') == True:
            f = open(x[6::] + '.txt','a')
            text = input('')
            if 'CLOSE' in text:
                f.write('\n' + text[0:-5])
                f.close()
            else:
                print('You forgot to write CLOSE at the end of text')
        else:
            print('No such file exists')
    elif x.count(' ') == 1 and '>' not in x and '>>' not in x:
        if os.path.isfile(x[4::]) == True:
            f = open(x[4::],'r')
            for i in f:
                print(i)
            f.close()
        else:
            print('No such file exists')
    else:
        print('Invalid syntax')
#----------------------------------------CD COMMAND----------------------------------------
def cd():
    if x[0:2] == 'cd' and x[2] == ' ':
        if '..' not in x:
            if os.path.isdir(x[3::]) == True:
                os.chdir(x[3::])
            else:
                print('No such directory exists')
        else:
            if x[3::] == '..':
                os.chdir('..')
            else:
                if x.count('..') % 2 != 0:
                    if x.count('/') == x.count('..') - 1:
                        i = 1
                        while i <= x.count('..'):
                            os.chdir('..')
                            i = i + 1
                    else:
                        print('Invalid syntax')
                else:
                    print('Invalid syntax')
    else:
        print('Invalid syntax')
#----------------------------------------MKDIR COMMAND-------------------------------------
def mkdir():
    if x[5] == ' ':
        lst = x.split()
        i = 1
        while i < len(lst):
            if os.path.isdir(lst[i]) == False:
                os.makedirs(lst[i])
            else:
                print('Directory named ' + lst[i] + ' already exists')
            i = i + 1
    else:
        print('Invalid syntax')
#----------------------------------------CP COMMAND----------------------------------------
def cp():
    if len(x.split()) == 3:
        lst = x.split()
        if os.path.isfile(lst[1] + '.txt') == True:
            if os.path.isfile(lst[2] + '.txt') == False:
                old = open(lst[1] + '.txt','r')
                new = open(lst[2] + '.txt','a')
                for i in old:
                    new.write(i)
                new.close()
                old.close()
            else:
                print('File named ' + lst[2] + ' already exists')
        else:
            print('No such file named ' + lst[1] + ' exists')
    else:
        lst = x.split()
        if os.path.isdir(lst[-1]) == True:
            folder = lst[-1]
            ii = 1
            while ii < len(lst) - 1:
                if os.path.isfile(lst[ii] + '.txt') == True:
                    os.chdir(folder)
                    new = open(lst[ii] + '.txt','a')
                    os.chdir('..')
                    old = open(lst[ii] + '.txt','r')
                    for i in old:
                        os.chdir(folder)
                        new.write(i)
                        os.chdir('..')
                    old.close()
                    new.close()
                else:
                    print('No such file named ' + lst[i] + ' exists')
                ii = ii + 1
        else:
            print('Directory named ' + lst[-1] + ' doesnot extst')
#----------------------------------------MV COMMAND----------------------------------------
def mv():
    if len(x.split()) == 3 and x.count(' ') == 2:
        if os.path.isfile(x.split()[1] + '.txt') == True:
            if os.path.isfile(x.split()[2] + '.txt') == False:
                old = open(x.split()[1] + '.txt','r')
                new = open(x.split()[2] + '.txt','a')
                for i in old:
                    new.write(i)
                new.close()
                old.close()
                os.remove(x.split()[1] + '.txt')
            else:
               print('File named ' + x.split()[2] + ' already exists') 
        else:
            print('No such file named ' + x.split()[1] + ' exists')
    else:
        print('Invalid syntax')
#----------------------------------------RM COMMAND----------------------------------------
def rm():
    i = 1
    while i < len(x.split()):
        if os.path.isfile(x.split()[i] + '.txt') == True:
            os.remove(x.split()[i] + '.txt')
        else:
            print('No such file named ' + x.split()[i] + ' exists')
        i = i + 1
#----------------------------------------RMDIR COMMAND-------------------------------------
def rmdirr():
    i = 1
    while i < len(x.split()):
        if os.path.isdir(x.split()[i]) == True:
            if os.listdir(x.split()[i]) == []:
                os.rmdir(x.split()[i])
            else:
                print('Directory named ' + x.split()[i] + ' is not empty')
        else:
            print('Directory named ' + x.split()[i] + ' doesnot extst')
        i = i + 1
#----------------------------------------PWD COMMAND---------------------------------------
def pwd():
    if len(x) == 3:
        print(os.getcwd())
    else:
        print('Invalid syntax')
#---------------------------------------DATE COMMAND---------------------------------------
def date():
    if x == 'date':
        print(time.strftime('%a %b %d %H:%M:%S %z %Y'))
    else:
        print('Invalid syntax')                                    
#----------------------------------------MAIN LOOP-----------------------------------------
print("""Winux is a program which executes Linux Shell Commands on windows OS.
    - Name                         : Winux 1.0.0 intial release
    - Currently supported commands : ls, echo, cal, cat, cd, mkdir, pwd ,cd,
                                     mv, rm, rmdir, date
    - Creator                      : Daxeel Soni
    - Source                       : github.com/daxeel/Winux\n""")
while True:
    x = input('Winux_Shell~$ ')
    if 'ls' in x:
        ls()
    elif 'echo' in x:
        echo()
    elif 'cal' in x:
        cal(int(x[6::]),int(x[4]))
    elif 'cat' in x:
        cat()
    elif 'pwd' in x:
        pwd()
    elif 'cd' in x:
        cd()
    elif 'mkdir' in x:
        mkdir()
    elif 'cp' in x:
        cp()
    elif 'mv' in x:
        mv()
    elif 'rm' in x and 'dir' not in x:
        rm()
    elif 'rmdir' in x:
        rmdirr()
    elif 'date' in x:
        date()
#----------------------------------------END----------------------------------------
