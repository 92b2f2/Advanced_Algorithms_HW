#!/usr/bin/env python3
import matplotlib.pyplot as plt
import time
import sys 
import scipy
import numpy as np
from scipy import constants

phi = constants.golden

def naive(n) :
    return (phi**n)/scipy.sqrt(5)

x = []
y = []
time_used = 0
i = 100000
while i <= 100000:
    ans = int(np.round(naive(i)))
    print(ans)
    #if ans == 308061521170130:
    #    print(i)
    #    break
    i += 1


"""
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
"""
