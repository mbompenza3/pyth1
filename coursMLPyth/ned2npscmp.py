import numpy as np
import math
po=0
for k in range(5):
    p=3**k*np.exp(-3)/math.factorial(k)
    print(p)
    po+=p
