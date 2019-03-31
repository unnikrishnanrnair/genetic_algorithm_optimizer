import os

gen = input('')

next_gen = []
with open('gen'+str(gen)+'/next_gen.txt') as f:
    for line in f:
        next_gen.append(int(line))

os.system('mkdir gen'+str(gen+1))
os.system('mkdir gen'+str(gen+1)+'/delay')
os.system('mkdir gen'+str(gen+1)+'/leakage')
a = 0
for i in next_gen:
    os.system('cp gen'+str(gen)+'/mutation/delay/'+str(i)+'_delay.sp gen'+str(gen+1)+'/delay/'+str(a)+'_delay.sp')
    os.system('cp gen'+str(gen)+'/mutation/leakage/'+str(i)+'_leakage.sp gen'+str(gen+1)+'/leakage/'+str(a)+'_leakage.sp')
    a = a + 1
