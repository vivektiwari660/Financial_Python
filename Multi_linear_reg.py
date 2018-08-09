
# coding: utf-8

# In[1]:


# Multiple Liner Regression
import numpy as np
import pandas as pd
import quandl
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

# Get stock prices
quandl.ApiConfig.api_key = '1RzAY_zj8KiHoywXe6xj'
spy_table  = quandl.get('BCIW/_SPXT')
amzn_table = quandl.get('WIKI/AMZN')
ebay_table = quandl.get('WIKI/EBAY')
wal_table  = quandl.get('WIKI/WMT')
aapl_table = quandl.get('WIKI/AAPL')


# In[3]:


import quandl
quandl.ApiConfig.api_key = '1RzAY_zj8KiHoywXe6xj'


# In[4]:


data = quandl.get('NSE/OIL')


# In[5]:


data.head()


# In[6]:


spy_table  = quandl.get('BCIW/_SPXT')
amzn_table = quandl.get('WIKI/AMZN')
ebay_table = quandl.get('WIKI/EBAY')
wal_table  = quandl.get('WIKI/WMT')
aapl_table = quandl.get('WIKI/AAPL')


# In[7]:


spy  = spy_table .loc['2016',['Close']]
amzn = amzn_table.loc['2016',['Close']]
ebay = ebay_table.loc['2016',['Close']]
wal  = wal_table .loc['2016',['Close']]
aapl = aapl_table.loc['2016',['Close']]


# In[8]:


spy_log  = np.log(spy.Close) .diff().dropna()
amzn_log = np.log(amzn.Close).diff().dropna()
ebay_log = np.log(ebay.Close).diff().dropna()
wal_log  = np.log(wal.Close) .diff().dropna()
aapl_log = np.log(aapl.Close).diff().dropna()
df = pd.concat([spy_log,amzn_log,ebay_log,wal_log,aapl_log],axis = 1).dropna()
df.columns = ['SPY', 'AMZN', 'EBAY', 'WAL', 'AAPL']
df.tail()


# In[9]:


simple = sm.ols(formula = 'amzn ~ spy', data = df).fit()
print (simple.summary())


# In[10]:


model = sm.ols(formula = 'amzn ~ spy + ebay + wal', data = df).fit()
print (model.summary())


# In[14]:


import urllib.request
from datetime import datetime

url = 'https://www.quantconnect.com/tutorials/wp-content/uploads/2017/08/F-F_Research_Data_5_Factors_2x3_daily.csv'
response   = urllib2.urlopen(url)
fama_table = pd.read_csv(response)

# Convert time column into index
fama_table.index = [datetime.strptime(str(x), "%Y%m%d")
                    for x in fama_table.iloc[:,0]]
# Remove time column
fama_table = fama_table.iloc[:,1]


# In[19]:


import urllib.request
from datetime import datetime

url = 'https://www.quantconnect.com/tutorials/wp-content/uploads/2017/08/F-F_Research_Data_5_Factors_2x3_daily.csv'
response   = urllib.request.urlopen(url)
fama_table = pd.read_csv(response)

# Convert time column into index
fama_table.index = [datetime.strptime(str(x), "%Y%m%d")
                    for x in fama_table.iloc[:,0]]
# Remove time column
fama_table = fama_table.iloc[:,1]


# In[20]:


fama = fama_table['2016']
fama = fama.rename(columns = {'Mkt-RF':'MKT'})
fama = fama.apply(lambda x: x/100)
fama_df = pd.concat([fama, amzn_log], axis = 1)
fama_model = sm.ols(formula = 'Close~MKT+SMB+HML+RMW+CMA', data = fama_df).fit()
print (fama_model.summary())


# In[21]:


result = pd.DataFrame({'simple regression': simple.predict(),
                       'fama_french': fama_model.predict(),
                       'sample': df.amzn}, index = df.index)

# Feel free to adjust the chart size
plt.figure(figsize = (15,7.5))
plt.plot(result['2016-7':'2016-9'].index,result.loc['2016-7':'2016-9','simple regression'])
plt.plot(result['2016-7':'2016-9'].index,result.loc['2016-7':'2016-9','fama_french'])
plt.plot(result['2016-7':'2016-9'].index,result.loc['2016-7':'2016-9','sample'])
plt.legend()
plt.show()


# In[22]:


plt.figure()
fama_model,resid.plot.density()
plt.show()


# In[23]:


print ('Residual mean:', np.mean(fama_model.resid))


# In[ ]:


from statsmodels.stats import diagnostic as dia
het = dia.het_breuschpagan(fama_model.resid,fama_df[['MKT','SMB','HML','RMW','CMA']][1:])
print ('p-value: ', het[-1])

