import numpy as np
import random
import time
n = int(1e4)
a =  np.random.random((n,n))

res = 0
t = time.time()
for i in range(n):
    for j in range(n):
        res+= a[i][j]
use_time1 = time.time() - t

t = time.time()
res2 = a.sum()
use_time2 = time.time() - t

print(res == res2,res,res2)
print(use_time1,use_time2)