import os
print('Generation 0')
os.system('echo 0 | python pygen.py')
os.system('cp 45nm_MGK.pm gen0/mutation/delay/')
os.system('cp 45nm_MGK.pm gen0/mutation/leakage/')

os.system('cp hspice_delay.py gen0/mutation/delay/')
os.system('cp hspice_leakage.py gen0/mutation/leakage/')

os.system('cd ~/ruc/ruc/gen0/mutation/delay && python hspice_delay.py > /dev/null')
# os.system('cd ' + cdir + 'gen0/mutation/leakage && python hspice_leakage.py')
os.system('cd ~/ruc/ruc/gen0/mutation/leakage && python hspice_leakage.py &> /dev/null')
# os.system('cd ' + cdir)
os.system('cd ~/ruc/ruc')
os.system('echo 0 | python fitness.py')

os.system('cp gen0/stats.txt .')


for i in range(1,2000):
    print('Generation',i)
    os.system('echo '+str(i-1)+' | python promote.py')
    os.system('echo '+str(i)+' | python crossover_child.py')
    os.system('echo '+str(i)+' | python mutation.py')

    os.system('cp 45nm_MGK.pm gen'+str(i)+'/mutation/delay/')
    os.system('cp 45nm_MGK.pm gen'+str(i)+'/mutation/leakage/')

    os.system('cp hspice_delay.py gen'+str(i)+'/mutation/delay/')
    os.system('cp hspice_leakage.py gen'+str(i)+'/mutation/leakage/')

    os.system('cd ~/ruc/ruc/gen'+str(i)+'/mutation/delay && python hspice_delay.py > /dev/null')
    # os.system('cd ' + cdir + 'gen' + str(i) + '/mutation/leakage && python hspice_leakage.py')
    # os.system('cd ' + cdir)
    os.system('cd ~/ruc/ruc/gen'+str(i)+'/mutation/leakage && python hspice_leakage.py > /dev/null')
    os.system('cd ~/ruc/')
    os.system('echo '+str(i)+' | python fitness.py')
    os.system('cat gen'+str(i)+'/stats.txt >> stats.txt')
