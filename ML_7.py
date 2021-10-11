#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris
import pandas as pd
import numpy as np


# In[2]:


data=load_iris()


# In[3]:


data


# In[5]:


df=pd.DataFrame(data['data'],columns=data['feature_names'])
df


# In[6]:


x = df


# In[8]:


y=pd.DataFrame(data['target'],columns=['Species'])


# In[7]:


x.head()


# In[8]:


y.head()


# In[10]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,stratify=y,test_size=0.20)


# In[11]:


from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler=scaler.fit(x_train)
x_train_s=scaler.transform(x_train)
x_test_s=scaler.transform(x_test)


# In[12]:


from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(x_train_s,np.array(y_train).flatten())


# In[13]:


y_pred=model.predict(x_test_s)
y_train.value_counts()


# In[14]:


from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


# In[16]:


from sklearn.metrics import confusion_matrix
pd.DataFrame(confusion_matrix(y_test, y_pred))


# In[ ]:




