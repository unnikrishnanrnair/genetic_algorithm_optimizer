from __future__ import print_function
from random import randint
import os

gen = input('')

def get_lw_value(s):
    arr = s.split(' ')
    l=float([s for s in arr if 'l=' in s][0].split('=')[1].split('n')[0])
    w=float([s for s in arr if 'w=' in s][0].split('=')[1].split('n')[0])
    return (l,w)

def get_lw_arr(data):
    ll = []
    wl = []
    for i in range(34,62):
        (l,w) = get_lw_value(data[i])
        ll.append(l)
        wl.append(w)
    return (ll,wl)

def get_lw_from_file(i):
    f = open('gen'+str(gen)+'/leakage/'+str(i)+'_leakage.sp')
    data = f.readlines()
    f.close()
    return get_lw_arr(data)

def getDataL(data, l, w):
    for i in range(34,62):
        arr = data[i].split(' ')
        temp = [s for s in arr if 'l=' in s][0]
        li = arr.index(temp)
        arr[li] = 'l=' + str(l[i-34]) +'n'
        temp = [s for s in arr if 'w=' in s][0]
        wi = arr.index(temp)
        arr[wi] = 'w=' + str(w[i-34]) +'n'
        data[i] = ' '.join(arr)
    return data

def getDataD(data, l, w):
    for i in range(33,61):
        arr = data[i].split(' ')
        temp = [s for s in arr if 'l=' in s][0]
        li = arr.index(temp)
        arr[li] = 'l=' + str(l[i-33]) +'n'
        temp = [s for s in arr if 'w=' in s][0]
        wi = arr.index(temp)
        arr[wi] = 'w=' + str(w[i-33]) +'n'
        data[i] = ' '.join(arr)
    return data


f=open('fa_leak_25,1.sp')
ldata=f.readlines()
f.close()

(ll,wl) = get_lw_arr(ldata)

f=open('fa_del_25,1.sp')
ddata=f.readlines()
f.close()


def get_hash(a,b):
    return int((a+b)*(a+b+1)/2 + b)

hassh={}
path, dirs, files = next(os.walk('gen'+str(gen)+'/leakage/'))
num = len(files)
os.system('mkdir gen'+str(gen)+'/crossover')
os.system('mkdir gen'+str(gen)+'/crossover/delay')
os.system('mkdir gen'+str(gen)+'/crossover/leakage')
import sys
for i in range(0,100):
    a=0
    b=0
    while True:
        a=randint(0,num-1)
        b=randint(0,num-1)
        if a==b or get_hash(a,b) in hassh or get_hash(b,a) in hassh:
            continue
        else:
            break

    (tll1,twl1) = get_lw_from_file(a)
    (tll2,twl2) = get_lw_from_file(b)

    nwl = []
    nll = []
    length = len(tll1)

    for j in range(0,length):
        nwl.append((twl1[j]+twl2[j])/2)
        nll.append((tll1[j]+tll2[j])/2)

    data_new = getDataD(ddata, nll, nwl)
    data_new_l = getDataL(ldata, nll, nwl)
    #sys.stderr.write('Did crossover for '+str(i) + 'in gen '+str(gen)+'\n') 
    thefile = open('gen'+str(gen)+'/crossover/delay/'+str(i) + '_delay.sp', 'w')
    for item in data_new:
        thefile.write("%s" % item)
    hassh[get_hash(a,b)] = True

    thefile = open('gen'+str(gen)+'/crossover/leakage/'+str(i) + '_leakage.sp', 'w')
    for item in data_new_l:
        thefile.write("%s" % item)
