import os

for i in range(0,100):
	os.system("hspice64 "+str(i)+"_delay.sp")
