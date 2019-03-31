from __future__ import print_function
from random import randint
import collections

del_bound = 0
gen = input('')
val_arr = {}
for i in range(0,100):
    fname = './gen'+str(gen)+'/mutation/leakage/'+str(i)+'_leakage.ms0'
    f = open(fname,'r')
    lis = f.readlines()
    f.close()
    needed_lis = [7*j for j in range(2,10)]
    val_arr[i] = {}
    lval = []
    for j in needed_lis:
        x = lis[j].split()
        lval.append(float(x[0]))
	
    val_arr[i]['leakage'] = sum(lval) / float(len(lval))

    fname = 'gen'+str(gen)+'/mutation/delay/'+str(i)+'_delay.mt0'
    f = open(fname,'r')
    lis = f.readlines()
    f.close()
    needed_lis = [4,5]
    dval = []
    for j in needed_lis:
        x = lis[j].split()
        print(i,j,x)
        dval+=map(float,x)
    dval.pop()
    dval.pop()
    val_arr[i]['delay'] = max(dval)

def heuristic_function(delay, leakage):
    delay_weight = delay
    if delay > del_bound:
	delay_weight = -100000
    return -1.0 * delay_weight + 0.5 * leakage

heuristics = {}

min_delay = max_delay = val_arr[0]['delay']
min_leakage = max_leakage = val_arr[0]['leakage']

for i in range(0,100):
    max_delay = max(max_delay , val_arr[i]['delay'])
    max_leakage = max(max_leakage , val_arr[i]['leakage'])
    min_leakage = min(min_leakage , val_arr[i]['leakage'])
    min_delay = min(min_delay , val_arr[i]['delay'])

delay_range = max_delay - min_delay
leakage_range = max_leakage - min_leakage
del_bound = (1.3e-11-min_delay)/delay_range
values = []
for i in range(0,100):
    heuristics[i] = heuristic_function((val_arr[i]['delay'] - min_delay)/delay_range, (val_arr[i]['leakage'] - min_leakage)/leakage_range)
    values.append((heuristics[i],(val_arr[i]['delay'] - min_delay)/delay_range, (val_arr[i]['leakage'] - min_leakage)/leakage_range))
for i in range(100):
 print(i,values[i], val_arr[i])
#od = collections.OrderedDict(sorted(heuristics.items()))
od = sorted(heuristics.items(), key=lambda kv: kv[1])

print(od)
new_gen = []
for i in range(0,60):
       if od[i][1] < 10000:
           new_gen.append(od[i][0])

thefile = open('gen'+str(gen)+'/next_gen.txt', 'w')
for item in new_gen:
  thefile.write("%s\n" % item)

thefile = open('gen'+str(gen)+'/stats.txt', 'w')
thefile.write("%s\n" % min_delay)
thefile.write("%s\n" % max_delay)
thefile.write("%s\n" % min_leakage)
