
# coding: utf-8

# In[10]:


#_GjJzb3fZwmXefY3ANQy

#rate-of-return,-mean-and-variance


import quandl
quandl.ApiConfig.api_key = '_GjJzb3fZwmXefY3ANQy'
#get quandl data
aapl_table = quandl.get('WIKI/AAPL')
aapl = aapl_table.loc['2017-3',['Open','Close']]
#take log return
import numpy as np
aapl['log_price'] = np.log(aapl.Close)
#aapl['log_return'] = np.log_price.diff()
print(aapl)


# In[13]:


month_return = aapl.log_price.sum()
print(month_return)


# In[12]:


print (np.mean(aapl.log_price))


# In[8]:


print(np.var(aapl.log_price))


# In[9]:


print(np.std(aapl.log_price))


# In[14]:


# Random Variables and Distributions


# In[15]:


import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#define a function to simulate rolling a dice
def dice():
    number=  [1,2,3,4,5,6]
    return random.choice(number)

series = np.array([dice() for x in range(10000)])
print (series)


# In[16]:


plt.figure(figsize = (20,10))
plt.hist(series,bins = 11,align = 'mid')
plt.xlabel('Dice Number')
plt.ylabel('Occurences')
plt.grid()
plt.show()


# In[17]:


print (len([x for x in series if x <= 3])/float(len(series)))
print (np.mean(series))


# In[18]:


# Binomial Distribution


# In[19]:


def trial():
    number = [1,2,3,4,5,6,7,8,9,10]
    a = random.choice(number)
    if a<= 7:
        return 1
    else:
        return 0


# In[24]:


trial()


# In[25]:


res = [trial() for x in range(10)]
print (sum(res))


# In[27]:


# Binomial Distribution with 10000 samples
def binomial(number):
    l = []
    for i in range(10000):
        res = [trial() for x in range(10)]
        l.append(sum(res))
    return len([x for x in l if x == number])/float(len(l))
print (binomial(8))


# In[28]:


prob = []
for i in range(1,11):
    prob.append(binomial(i))
prob_s = pd.Series(prob,index = range(1,11))
print (prob_s)


# In[30]:


print ((float(binomial(10))/(binomial(7)*binomial(10-7)))*(0.7**7)*(0.3**3))

print ((float(binomial(10))/(binomial(8)*binomial(10-8)))*(0.7**8)*(0.3**2))


# In[31]:


plt.figure(figsize = (20,10))
plt.bar(range(1,11),prob)
plt.grid()
plt.show()


# In[32]:


# Normal Distribution 



# In[37]:


from scipy.stats import norm


# In[38]:


import matplotlib.pyplot as plt
plt.figure(figsize = (20,10))
norm.plot.density()
plt.show()


# In[39]:


import quandl
quandl.ApiConfig.api_key = '_GjJzb3fZwmXefY3ANQy'
spy_table = quandl.get('BCIW/_SPXT')
spy = spy_table.loc['2009':'2017',['Open','Close']]
spy['log_return'] = np.log(spy.Close).diff()
spy = spy.dropna()


# In[40]:


plt.figure(figsize = (20,10))
spy.log_return.plot()
plt.show()


# In[41]:


plt.figure(figsize = (20,10))
spy.log_return.plot.density()
plt.show()


# In[42]:


de_2 = pd.Series(np.random.normal(0,2,10000),name = 'μ = 0, σ = 2')
de_3 = pd.Series(np.random.normal(0,3,10000),name = 'μ = 0, σ = 3')
de_0 = pd.Series(np.random.normal(0,0.5,10000), name ='μ = 0, σ = 0.5')
mu_1 = pd.Series(np.random.normal(-2,1,10000),name ='μ = -2, σ = 1')
df = pd.concat([de_2,de_3,de_0,mu_1],axis = 1)
plt.figure(figsize=(20,10))
df.plot.density()
plt.show()

