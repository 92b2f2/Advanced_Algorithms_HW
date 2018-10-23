#!/usr/bin/env python3
import matplotlib.pyplot as plt
import time
import sys 

f = open('f2_ans','w')
x = []
y = []
time_used = 0
i = 0
stime = time.time()
f1 = 1
f2 = 1
f3 = 0
#print(f1)
#print(f2)
while time_used <= 10:
#while i < 1003:
    x.append(i+3)
    f3 = f1 + f2
    time_used = time.time()-stime
    #print(str(i)+" : "+str(f3))
    #print(f3)
    f1 , f2 = f2 , f3
    y.append(time_used)
    i += 1

for _ in range(0,2):
    f1=1
    f2=2
    f3=0
    stime = time.time()
    for n in range(0,i):
        f3 = f1 + f2
        time_used = time.time()-stime
        f1 , f2 = f2 , f3
        y[n] += time_used

for n in range(0,i):
    y[n] /= 3
    
plt.suptitle('Fib(n)')
plt.plot(x,y)
plt.xlabel('n')
plt.ylabel('time used')
#plt.show()
plt.savefig("f2.png")
f.write("{} : {}".format(i+3,f3))


