
# coding: utf-8

# In[1]:


# Simple Linear Regression


# In[4]:


import numpy as np
import pandas as pd
import quandl
quandl.ApiConfig.api_key = '1RzAY_zj8KiHoywXe6xj'
#get data from quandl
quandl.get("FINRA/FNSQ_AMZN", authtoken="1RzAY_zj8KiHoywXe6xj")
spy_table = quandl.get('BCIW/_SPXT')
amzn_table = quandl.get('WIKI/AMZN')
#fetch data from Jan 2017 to Jun 2017
spy = spy_table.loc['2017':'2017-6',['Close']]
amzn = amzn_table.loc['2017':'2017-6',['Close']]
#calculate log return
spy_log = np.log(spy.Close).diff().dropna()
amzn_log = np.log(amzn.Close).diff().dropna()
df = pd.concat([spy_log,amzn_log],axis = 1).dropna()
df.columns = ['spx','amzn']
print (df.tail())


# In[5]:


import matplotlib.pyplot as plt
plt.figure(figsize = (15,10))
plt.scatter(df.spy,df.amzn)
plt.show()


# In[6]:


import statsmodels.formula.api as sm
model = sm.ols(formula = 'amzn~spy',data = df).fit()
print (model.summary())


# In[7]:


print ('pamameters: ',model.params)


# In[8]:


print ('residual: ', model.resid.tail())
print ('fitted values: ',model.predict())


# In[ ]:


plt.figure(figsize = (15,10))
plt.scatter(df.spy,df.amzn)
plt.xlabel('spx_return')
plt.ylabel('amzn_return')
plt.plot(df.spy,model.predict(),color = 'red')
plt.show()

