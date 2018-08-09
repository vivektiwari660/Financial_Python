
# coding: utf-8

# In[1]:


# Confidence Interval & Hypothesis Testing


# In[3]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import quandl
quandl.ApiConfig.api_key = '1RzAY_zj8KiHoywXe6xj'
#get data from quandl
spy_table = quandl.get('BCIW/_SPXT')
spy_total = spy_table[['Open','Close']]
#calculate log returns
spy_log_return = np.log(spy_total.Close).diff().dropna()
print ('Population mean:', np.mean(spy_log_return))
print ('Population standard deviation:',np.std(spy_log_return))


# In[4]:


# recent 10 days sample and recent 1000 days sample:
print ('10 days sample returns:', np.mean(spy_log_return.tail(10)))

print ('10 days sample standard deviation:', np.std(spy_log_return.tail(10)))

print ('1000 days sample returns:', np.mean(spy_log_return.tail(1000)))

print ('1000 days sample standard deviation:', np.std(spy_log_return.tail(1000)))


# In[5]:


#apply the formula above to calculate confidence interval
bottom_1 = np.mean(spy_log_return.tail(10))-1.96*np.std(spy_log_return.tail(10))/(np.sqrt(len((spy_log_return.tail(10)))))
upper_1 = np.mean(spy_log_return.tail(10))+1.96*np.std(spy_log_return.tail(10))/(np.sqrt(len((spy_log_return.tail(10)))))
bottom_2 = np.mean(spy_log_return.tail(1000))-1.96*np.std(spy_log_return.tail(1000))/(np.sqrt(len((spy_log_return.tail(1000)))))
upper_2 = np.mean(spy_log_return.tail(1000))+1.96*np.std(spy_log_return.tail(1000))/(np.sqrt(len((spy_log_return.tail(1000)))))
#print the outcomes
print ('10 days 95% confidence inverval:', (bottom_1,upper_1))
print ('1000 days 95% confidence inverval:', (bottom_2,upper_2))


# In[6]:


# Hypothesis testing


# In[7]:


mean_1000 = np.mean(spy_log_return.tail(1000))
std_1000 = np.std(spy_log_return.tail(1000))
mean_10 = np.mean(spy_log_return.tail(10))
std_10 = np.std(spy_log_return.tail(10))
s = pd.Series([mean_10,std_10,mean_1000,std_1000],index = ['mean_10', 'std_10','mean_1000','std_1000'])
print (s)


# In[8]:


bottom = 0 - 1.64*std_1000/np.sqrt(1000) # with 90% Confidence Interval
upper = 0 + 1.64*std_1000/np.sqrt(1000)
print (bottom, upper)


# In[9]:


bottom = 0 - 1.96*std_1000/np.sqrt(1000)  # 95% Confidence Interval
upper = 0 + 1.96*std_1000/np.sqrt(1000)
print (bottom, upper)


# In[10]:


print (np.sqrt(1000)*(mean_1000 - 0)/std_1000)


# In[11]:


import scipy.stats as st
print (1 - st.norm.cdf(1.9488))


# In[12]:


mean_1200 = np.mean(spy_log_return.tail(1200))
std_1200 = np.std(spy_log_return.tail(1200))
z_score = np.sqrt(1200)*(mean_1200 - 0)/std_1200
print ('z-score = ',z_score)
p_value = (1 - st.norm.cdf(z_score))
print ('p_value = ',p_value)

