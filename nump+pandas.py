
# coding: utf-8

# In[2]:


import numpy as np
price_list = [143.73, 145.83, 143.68, 144.02, 143.5, 142.62]
price_array = np.array(price_list)
print (price_array, type(price_array))


# In[3]:


Ar = np.array([[1,3], [2,4]])
print (Ar, type(Ar))


# In[4]:


print(Ar.shape)


# In[8]:


print (Ar[1])   # Accessing by row


# In[9]:


print ('Second column:', Ar[:,1]) # Accessing by column


# In[10]:


np.log(price_array)


# In[11]:


np.mean(price_array)

print (np.std(price_array))

print (np.sum(price_array))

print (np.max(price_array))


# In[12]:


import pandas as pd


# In[13]:


price = [143.73, 145.83, 143.68, 144.02, 143.5, 142.62]
s = pd.Series(price)
print (s)


# In[14]:


price = [143.73, 145.83, 143.68, 144.02, 143.5, 142.62]
s = pd.Series(price, index=['a','b','c','d','e','f'])
print (s)


# In[15]:


s.index = [6,5,4,3,2,1]
print (s)


# In[16]:


print (s[1:])
print (s[:-2])


# In[17]:


print (s[4])
s[4] = 0
print (s)


# In[18]:


print (s.describe())


# In[19]:


# Time Index
time_index = pd.date_range('2017-01-01', periods = len(s), freq = 'D')
print (time_index)
s.index = time_index
print (s)


# In[20]:


s.index = [6,5,4,3,2,1]
print (s)
print (s[1])


# In[21]:


print (s.iloc[1])


# In[22]:


s.index = time_index
print (s['2017-01-03'])


# In[23]:


s['2017-01-02':'2017-01-05']


# In[24]:


print (s[s < np.mean(s)])
print (s[(s > np.mean(s)) & (s < np.mean(s) + 1.64*np.std(s))])


# In[26]:




