#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
N = 10
print (np.arange( N - 1, 0 -1 , -1))


# In[2]:



import numpy as np
N = 10
A = np.diag(np.arange( N, 0-1, -1), k = 0 )
print (A)
np.sum (np.diagonal (A))


# In[3]:


import numpy as np
A = np.array ([[4.,2.,1.],[1., 3., 0.],[0., 5., 4.]])
B = np.array ([4., 12., -3.])
np.linalg.solve(A, B)


# In[ ]:




