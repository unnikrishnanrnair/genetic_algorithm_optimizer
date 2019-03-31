*****************************************************
.param gflag__totalflag_mos__mos__cmos040lp=0
.param gflag__globalflag_mos__mos__cmos040lp=1
.param svtlp_dev=1

.include './45nm_MGK.pm'
.option parhier=local   *$ *** Required by WiCkeD ***
.DC dummy 1 1 1
.temp 25
.options GMIN=1e-30
.options POST
.options AUTOSTOP
.options INGOLD=2
.options DCON=1
.options GSHUNT=1e-15
.options RMIN=1e-15
.options ABSTOL=1e-25
.options ABSVDC=1e-25
.options RELTOL=1e-20
.options RELVDC=1e-2                                                                                                                                                                                                               
.options NUMDGT=4
.options PIVOT=1e-13
.options MEASDGT=6
.option measform=1
*****Parameters*********************
.Param
+   trfck=10p       $ rise and fall times for clk and data input
+   tr=10p
+   cqload=0.2f     $ capacitive loads on FF Q and Qn
+   pvdd=1.0        $ voltage supply
+   tsetup=1n       $ conservative Tsetup
+   thold=3n        $ conservative Thold

Mp1    1   nodea   vdd   vdd   pmos  l=45.0n w=720.0n 
Mp2    1   nodeb   vdd   vdd   pmos  l=45.0n w=720.0n 
Mp3    nodecon nodec   1   vdd   pmos l=45.0n w=720.0n 
Mn1    5   nodea   gnd   gnd   nmos  l=45.0n w=360.0n 
Mn2    5   nodeb   gnd   gnd   nmos  l=45.0n w=360.0n 
Mn3    nodecon nodec   5   gnd   nmos l=45.0n w=360.0n 
Mp4    4   nodea   vdd   vdd   pmos  l=45.0n w=720.0n 
Mp5    nodecon nodeb   4   vdd   pmos  l=45.0n w=720.0n 
Mn4    nodecon nodeb   node4   gnd   nmos l=45.0n w=360.0n 
Mn5    node4   nodea   gnd   gnd   nmos l=45.0n w=360.0n 
Mp6    2   nodea   vdd   vdd   pmos  l=45.0n w=720.0n 
Mp7    2   nodeb   vdd   vdd   pmos l=45.0n w=720.0n 
Mp8    2   nodec   vdd   vdd   pmos l=45.0n w=720.0n 
Mp9    nodes0n nodecon 2   vdd   pmos l=45.0n w=720.0n 
Mn6    3   nodea   gnd   gnd   nmos l=45.0n w=360.0n 
Mn7    3   nodeb   gnd   gnd   nmos l=45.0n w=360.0n 
Mn8    3   nodec   gnd   gnd   nmos l=45.0n w=360.0n 
Mn9    nodes0n nodecon 3   gnd   nmos l=45.0n w=360.0n 
Mp10   9   nodea   vdd   vdd   pmos  l=45.0n w=1080.0n 
Mp11   8   nodeb   9   vdd   pmos    l=45.0n w=1080.0n 
Mp12   nodes0n nodec   8   vdd   pmos l=45.0n w=1080.0n 
Mn10   7   nodea   gnd   gnd   nmos  l=45.0n w=540.0n 
Mn11   6   nodeb   7   gnd   nmos    l=45.0n w=540.0n 
Mn12   nodes0n nodec   6   gnd   nmos  l=45.0n w=540.0n 
Mp13   nodeco  nodecon vdd   vdd   pmos l=45.0n w=720.0n 
Mn13   nodeco  nodecon gnd   gnd   nmos l=45.0n w=360.0n 
Mp14   nodes0  nodes0n vdd   vdd   pmos l=45.0n w=720.0n 
Mn14   nodes0  nodes0n gnd   gnd   nmos  l=45.0n w=360.0n  


cq1 nodes0 0 c='cqload' ic=0
cq2 nodeco 0 c='cqload' ic=0
**************************supply digital power rails*******************
vgnd gnd 0 dc=0
vvdd vdd 0 dc='pvdd'
**************************stimulus waveforms**************************
Vina nodea 0 PWL(0  0   600p    0   '600p+tr'   'pvdd'  1200p   'pvdd'  '1200p+tr'  0       3000p   0       '3000p+tr'  'pvdd'  3600p   'pvdd'  '3600p+tr'  0       6600p   0       '6600p+tr'      'pvdd'  10200p      'pvdd'      '10200p+tr'     0       12600p      0)
Vinb nodeb 0 PWL(0  'pvdd'  1800p   'pvdd'  '1800p+tr'  0   4800p    0  '4800p+tr'  'pvdd'  5400p   'pvdd'  '5400p+tr'  0       7200p   0       '7200p+tr'  'pvdd'  7800p   'pvdd'  '7800p+tr'      0       10800p      0           '10800p+tr'     'pvdd'  12600p  'pvdd') 
Vinc nodec 0 PWL(0  0   2400p   0   '2400p+tr'  'pvdd'  6000p   'pvdd'  '6000p+tr'  0       9000p   0       '9000p+tr'  'pvdd'  9600p   'pvdd'  '9600p+tr'  0       11400p  0       '11400p+tr'     'pvdd'  12000p      'pvdd'      '12000p+tr'     0)
***************************Measurements*********************************

.tran 6e-12 12e-9
.measure tran delay_lh_nodeaCo  trig v(nodea) val='0.5*pvdd' rise=1 targ v(nodeco) val='0.5*pvdd' rise=1
.measure tran delay_hl_nodeaCo  trig v(nodea) val='0.5*pvdd' fall=1 targ v(nodeco) val='0.5*pvdd' fall=1 

.measure tran delay_lh_nodebCo  trig v(nodeb) val='0.5*pvdd' rise=1 targ v(nodeco) val='0.5*pvdd' rise=3 
.measure tran delay_hl_nodebCo  trig v(nodeb) val='0.5*pvdd' fall=2 targ v(nodeco) val='0.5*pvdd' fall=3 

.measure tran delay_lh_nodecCo  trig v(nodec) val='0.5*pvdd' rise=2 targ v(nodeco) val='0.5*pvdd' rise=5
.measure tran delay_hl_nodecCo  trig v(nodec) val='0.5*pvdd' fall=2 targ v(nodeco) val='0.5*pvdd' fall=5

.end                                                                                  

