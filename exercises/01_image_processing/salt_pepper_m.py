import numpy as np


def salt_pepper(p_sp,sigma,rows,cols):
    noise=np.random.randn(rows,cols)*sigma
    noise[np.random.rand(rows,cols)>=p_sp]=0

    return noise

print(salt_pepper(0.1,1,2,2))
