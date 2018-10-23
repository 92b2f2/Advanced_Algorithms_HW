#!/usr/bin/env python3
import matplotlib.pyplot as plt
import time
import sys 
import scipy
import numpy as np
from scipy import constants
from numpy.linalg import matrix_power

x = []
y = []

f1 = np.array([[1,1],[1,0]], dtype=object)

time_used = 0
i = 2
ans = 0

while i <= 50000000 and time_used <= 10:
    x.append(i)
    stime = time.time()
    ans = matrix_power(f1,i)[0][0]
    #print(matrix_power(f1,i)[0][0])
    time_used = time.time() - stime
    y.append(time_used)
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
"""
plt.suptitle('Fib(n)')
plt.plot(x,y)
plt.xlabel('n')
plt.ylabel('time used')
#plt.show()
plt.savefig("f5.png")
f = open("ans","w")
f.write(ans)
