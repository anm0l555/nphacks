#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np


# In[3]:


data = pd.read_csv('/home/akshat/Downloads/linear - Sheet1.csv')
data


# In[4]:


data.plot(kind='scatter',x='X',y='Y')
plt.show()


# In[5]:


X = np.array(data[['X']])
Y = np.array(data[['Y']])


# In[6]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.25)


# In[7]:


x_mean = np.mean(X)
y_mean = np.mean(Y)
print(x_mean, y_mean)


# In[8]:


num=0
den=0
for i in range(len(X)):
    num+=(X[i]-x_mean)*(Y[i]-y_mean)
    den+=(X[i]-x_mean)**2
b1 = num/den
b0 = y_mean - (b1*x_mean)
print(b1, b0)


# In[9]:


def predicter(x):
    pred = b0 + b1*x
    return pred
# y_pred = b0 + b1*X
# y_pred


# In[10]:


plt.scatter(X,Y)
plt.plot(X, y_pred)
plt.show()


# In[11]:


predicter(3000)


# In[12]:


# R squared value tells the goodness of fit of that model
num_r=0
den_r=0
y_pred = b0 + b1*X
for i in range(len(X)):
    num_r+=(Y[i]-y_pred[i])**2
    den_r+=(Y[i]-y_mean)**2
r_sq = 1 - (num_r/den_r)
r_sq


# Assignment 5 Question 2 MLR

# In[13]:


df = pd.read_csv('/home/akshat/Downloads/dataset5ii.csv')
df


# In[14]:


df = df.drop(columns=['Year','Month'])
x = df[['Interest_Rate','Unemployement_Rate']]
y = df['Stock_Index_Price']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)


# In[15]:


one = np.ones(len(x_train))
x = np.matrix([one,np.array(x_train['Interest_Rate']),np.array(x_train['Unemployement_Rate'])]).T
y = np.array(y_train).reshape(-1,1)


# In[16]:


b = np.linalg.inv(x.T*x)*x.T*y
print(b)
print(b[0])
print(b[1][0])


# In[17]:


sum=0
sum=sum+b[0][0]
x = [1.5,5.8]
i=1
while i<len(b):
  sum=sum+b[i][0]*x[i-1]
  i=i+1
print(sum)


# In[ ]:




