import matplotlib.pyplot as pl
import matplotlib.gridspec as gridspec

x = range(10)
y = range(10)

delay=[]
leakage=[]
with open('data','r') as f:
    lno  = 1
    for line in f:
        a = float(line)
        if lno%2 == 1:
            delay.append(a)
        else:
            leakage.append(a)
        lno = lno + 1

# fig, ax = plt.subplots(nrows=3, ncols=1)
k = 1

def heuristic_function(delay, leakage):
    return -0.7*delay + 0.3*leakage

heuro=[]
for i in range(0,len(delay)):
    heuro.append(heuristic_function(delay[i],leakage[i]))

# for row in ax:
#     for col in row:
#         if k ==1:
#             col.plot(range(0,len(delay)),delay)
#         if k == 2:
#             col.plot(range(0,len(leakage)),leakage)
#         if k==3:
#             col.plot(range(0,len(heuro)),heuro)
#         k = k + 1

gs = gridspec.GridSpec(2, 2)

fig = pl.figure()
ax = pl.subplot(gs[0, 0]) # row 0, col 0
#ax.set_window_title("Delay vs Gen")
ax.set_xlabel("Generations")
ax.set_ylabel("Delay")
pl.plot(range(0,len(delay)),delay)

ax = pl.subplot(gs[0, 1]) # row 0, col 1
pl.plot(range(0,len(leakage)),leakage)
ax.set_xlabel("Generations")
ax.set_ylabel("Leakage")
ax = pl.subplot(gs[1, :]) # row 1, span all columns
pl.plot(range(0,len(heuro)),heuro)
ax.set_xlabel("Generations")
ax.set_ylabel("Profit Fn.")
fig.canvas.set_window_title('Genetic algorithm analysis/results')
pl.show()
