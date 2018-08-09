
# coding: utf-8

# In[1]:


# Linear Algebra
import numpy as np
a = np.array([1,2,3])
b = np.array([2,2,2])
c = np.array([3,1,1])
matrix = np.column_stack((a,b,c))
print (matrix)
print (type(matrix))


# In[2]:


A = np.array([[2,3],[4,2],[2,2]])
B = np.array([[4,2],[4,6]])
x = np.dot(A,B)
print (x)


# In[3]:


x = np.dot(B,A)


# In[4]:


print (matrix)
print ('\n-------------------------\n')
print (np.linalg.inv(matrix))


# In[5]:


inverse = np.linalg.inv(matrix)
print (np.dot(matrix, inverse))
print ('\n-------------------------\n')
print (np.dot(inverse,matrix))


# In[6]:


singular = np.array([[1,2,3],[1,2,3],[3,3,3]])
inv = np.linalg.inv(singular)


# In[7]:


A = np.array([[2,1,-1],[-3,-1,2],[-2,1,2]])
b = np.array([[8],[-11],[-3]])
inv_A = np.linalg.inv(A)
print (np.dot(inv_A, b))


# In[8]:


print (np.linalg.solve(A, b))

