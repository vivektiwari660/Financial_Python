
# coding: utf-8

# In[4]:


# 

import quandl
quandl.ApiConfig.api_key = '_GjJzb3fZwmXefY3ANQy'
aapl_table = quandl.get('WIKI/AAPL')
aapl = aapl_table['Adj. Close']['2017']
print (aapl)


# In[2]:


import quandl


# In[6]:


print(aapl['2017-2':'2017-4'])


# In[7]:


print(aapl.head())


# In[10]:


print(aapl.tail())


# In[11]:


by_month = aapl.resample('M').mean()
print (by_month)


# In[12]:


by_week = aapl.resample('W').mean()
print (by_week.head())


# In[13]:


std = aapl.resample('W').std()    # standard deviation
max = aapl.resample('W').max()    # maximum value
min = aapl.resample('W').min()    # minimum value


# In[15]:


print(std.head())


# In[16]:


last_day = aapl.resample('M').agg(lambda x: x[-1])
print (last_day)


# In[17]:


monthly_return = aapl.resample('M').agg(lambda x: x[-1]/x[1] - 1)
print (monthly_return)


# In[18]:


print (monthly_return.mean())
print (monthly_return.std())
print (monthly_return.max())


# In[19]:


print (last_day.diff())
print (last_day.pct_change())


# In[20]:


print (last_day.diff())
print (last_day.pct_change())


# In[21]:


daily_return = last_day.pct_change()
print (daily_return.fillna(method = 'bfill'))


# In[22]:


daily_return = last_day.pct_change().dropna()
print (daily_return)


# In[24]:


# Pandas DataFrames
import pandas as pd
dict = {'AAPL': [143.5,  144.09, 142.73, 144.18, 143.77],
        'GOOG': [898.7,  911.71, 906.69, 918.59, 926.99],
        'IBM':  [155.58, 153.67, 152.36, 152.94, 153.49]}
dates = pd.date_range('2017-07-03', periods = 5, freq = 'D')
df = pd.DataFrame(dict, index = dates)
print (df)


# In[25]:


df = aapl_table
print (df.Close.tail(5))
print (df['Adj. Volume'].tail(5))


# In[26]:


aapl_2016 = df['2016']
aapl_month = aapl_2016.resample('M').agg(lambda x: x[-1])
print (aapl_month)


# In[28]:


aapl_bar = aapl_month[['Open', 'High', 'Low', 'Close']]
print (aapl_bar)


# In[29]:


print(aapl_month.loc['2016-03':'2016-06', ['Open', 'High', 'Low', 'Close']])


# In[31]:


import numpy as np
above = aapl_bar[aapl_bar.Close > np.mean(aapl_bar.Close)]
print (above)


# In[32]:


# Data Validation
aapl_bar['rate_return'] = aapl_bar.Close.pct_change()
print (aapl_bar)


# In[33]:


missing = aapl_bar.isnull()
print (missing)
print ('---------------------------------------------')
print (missing.describe())


# In[34]:


print (missing[missing.rate_return == True])


# In[37]:


drop = aapl_bar.dropna()
print (drop)
print ('\n--------------------------------------------------\n')
fill = aapl_bar.fillna(0)
print (fill)


# In[40]:


# DataFrame Concat
s1 = pd.Series([143.5, 144.09, 142.73, 144.18, 143.77], name = 'AAPL')
s2 = pd.Series([898.7, 911.71, 906.69, 918.59, 926.99], name = 'GOOG')
data_frame = pd.concat([s1, s2], axis = 1)
print (data_frame)


# In[41]:


log_price = np.log(aapl_bar.Close)
log_price.name = 'log_price'
print (log_price)
print ('\n--------------------------------------------\n')
concat = pd.concat([aapl_bar, log_price], axis = 1)
print (concat)


# In[42]:


df_volume = aapl_table.loc['2016-10':'2017-04', ['Volume', 'Split Ratio']].resample('M').agg(lambda x: x[-1])
print (df_volume)
print ('\n-------------------------------------------\n')
df_2017 = aapl_table.loc['2016-10':'2017-04', ['Open', 'High', 'Low', 'Close']].resample('M').agg(lambda x: x[-1])
print (df_2017)


# In[43]:


concat = pd.concat([aapl_bar, df_volume], axis = 1)
print (concat)


# In[44]:


concat = pd.concat([aapl_bar, df_volume], axis = 1, join = 'inner')
print (concat)


# In[47]:


append = aapl_bar.append(df_2017)
print (append)


# In[48]:


concat = pd.concat([aapl_bar, df_2017], axis = 0)
print (concat)


# In[49]:


df_2017.columns = ['Change', 'High', 'Low', 'Close']
concat = pd.concat([aapl_bar, df_2017], axis = 0)
print (concat)

