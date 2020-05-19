""" coloring with matplotlib """ 

import matplotlib.pyplot as plt
import numpy as np
import random as rd
import seaborn as sns

#L1 contains your data, with heights for example.
#L1 size : nxm; type : numpy.ndarray

M = np.rd.randint(0,100,[10,20]) # random matrix

n = M.shape[0]
m = M.shape[1]

sns.heatmap(A, cmap='terrain')
plt.show()
