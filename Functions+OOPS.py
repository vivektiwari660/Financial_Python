
# coding: utf-8

# In[1]:


squares = []
for i in [1,2,3,4,5]:
    squares.append(i**2)
print(squares)


# In[3]:


stocks = ['AAPL','GOOG','IBM','FB','F','V','G','GE']
selected = ['AAPL','IBM']
new_list = []
for stock in stocks:
    if stock in selected:
        new_list.append(stock)
print(new_list)
    


# In[4]:


stocks = ['AAPL','GOOG','IBM','FB','F','V','G','GE']
for stock in stocks:
    print(stock)
    if stock == 'FB':
        break;


# In[7]:


stocks = ['AAPL','GOOG','IBM','FB','F','V','G','GE']
for stock in stocks:
    if stock == 'FB':
        continue
print(stock)
    


# In[9]:


stocks = ['AAPL','GOOG','IBM','FB','F','V','G','GE']
for stock in stocks:
    if stocks == 'FB':
        continue
print(stock)


# In[11]:


stocks = ['AAPL','GOOG','IBM','FB','F','V','G','GE']
for stock in stocks:
    if stocks == 'FB':
        continue
print(stocks)


# In[12]:


foo = [1,2,3,4,5]
squares = [x**2 for x in foo]
print(squares)


# In[13]:


new_list = [x for x in stocks if x not in selected]
print (new_list)


# In[14]:


print ([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print ([str(x) + ' vs ' + str(y) for x in ['AAPL','GOOG','IBM','FB']
                                for y in ['F','V','G','GE'] if x != y])


# In[15]:


def product(x,y):
    return x*y
print(product(45,7))


# In[17]:


print (range(1, 11))


# In[18]:


print(range(10))


# In[19]:


print range(1, 11)


# In[20]:


print (range(1, 11))


# In[21]:


tickers = ['AAPL','GOOG','IBM','FB','F','V', 'G', 'GE']
print((list(map(len,tickers))))


# In[22]:


map(lambda x: x**2, range(10))


# In[23]:


print(map(lambda x: x**2, range(10)))


# In[25]:


x = map(lambda x: x**2, range(10))
print(x.values)


# In[26]:


price_list = [('AAPL', 144.09), ('GOOGL', 911.71), ('MSFT', 69), ('FB', 150), ('WMT', 75.32)]
sorted(price_list, key = lambda x: x[1])


# In[27]:


class Stock:
    def __init__(self, ticker, open, close, volume):
        self.ticker = ticker
        self.open = open
        self.close = close
        self.volume = volume
        self.rate_return = float(close)/open - 1

    def update(self, open, close):
        self.open = open
        self.close = close
        self.rate_return = float(self.close)/self.open - 1

    def print_return(self):
        print (self.rate_return)
        


# In[28]:


apple = Stock('AAPL',143.69,144.09,20109375)


# In[29]:


google = Stock('GOOGL',898.7,911.7,1561616)


# In[30]:


apple.ticker


# In[32]:


google.print_return()


# In[34]:


google.update(912.8,913.4)


# In[35]:


google.update(912.8,913.4)
google.print_return()


# In[36]:


dir(apple)


# In[37]:


class Child(Stock):
    def __init__(self, name):
        self.name = name


# In[38]:


aa = Child('AA')
print (aa.name)


# In[39]:


aa.update(100, 102)
print (aa.open)


# In[40]:


aa.print_return()

