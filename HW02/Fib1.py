#!/usr/bin/env python3
import matplotlib.pyplot as plt
import time
import sys 

def dnc(n) :
    if n == 1 or n == 2 :
        return 1
    else :
        return dnc(n-1)+dnc(n-2)
x = []
y = []
time_used = 0
i = 1
while time_used < 10:
    x.append(i)
    stime = time.time()
    print(str(i)+" : "+str(dnc(i)))
    time_used = time.time()-stime
    y.append(time_used)
    i+=1
plt.suptitle('Fib(n)')
plt.plot(x,y)
plt.xlabel('n')
plt.ylabel('time used')
plt.show()
