import numpy as np
zm = np.arange(100000000,dtype=np.dtype('i'))
zm1 = np.power(zm, 2)
str(zm1)
np.savetxt('test.txt', zm1, fmt='%i')
# np.set_printoptions(threshold=np.nan)
print(zm1)
