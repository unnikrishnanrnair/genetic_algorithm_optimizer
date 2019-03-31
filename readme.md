-> run.py is the file to be run (only file to be run). It has all the commands to run all remaining files too.

-> The file pygen.py generates first generation of files with different Wn,Wp,Ln,Lp values.
-> The file mutation.py introduces random error in the values of Wn,Wp,Ln,Lp's of the files  maintaining them in results.
-> The files crossover and crossover_child.py perform crossover , produce children.
-> The file fitness.py, runs hspice on files having different values of Wn,Wp,Ln,Lp , takes values of leakagepower and delays , assigns fitness value to each file in the generation.

-> Once you run the file , run.py , 20 generations's directories are created.
In each generation's directory (genXX),  we have mutation,delay,leakage,crossover directories, text files stats.txt and next_gen.txt.

In the text file, next_gen.txt, we have files  of that generation in decreasing order of their fitness values.
In the stats.txt, file, the leakages and delays are put starting from the best file , till the worst ones in the generation. 

The change in delays and leakage powers can be known by , 
observing the delays and leakages of file with index number same as that of last number in the stats file of the initial generation(stats file in gen0 directory) and
the delays and leakages of file with index number same as that of first number in the stats file(stats file in gen19 directory) of the final generation.
 

In mutation directory (genXX/mutation),
we have "delay" and "leakage" directories , which have delay.mt0 and leakage.ms0 files(of different indices) which can be looked up for getting the values of delay and leakages of best files in that generation.
commands to run the file:
1)python run.py 
The maxdelay and average leakage are displayed on the screen for all the 100 files in each genertion
2)let k be the last generation
cat genk/next_gen.txt
The first number indicates the best child let it be i
3)cat genk/mutation/delay/i_delay.mt0
and 
cat genk/mutation/leakage/i_leakage.ms0
gives the leakage and delay results on the screen 


python fitness.py 
give no.of generations as input 
This gives us the delay and leakage of all population also gives the file with best heuristic.




 


