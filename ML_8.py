#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv("Iris.csv")


# In[3]:


df.info()


# In[6]:


X=df.iloc[:,1:5]
print(X)


# In[7]:


Y=df.iloc[:,5]
print(Y)


# In[8]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(Y)
print(y)


# In[9]:


from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)
print(X_scaled)


# In[10]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.3,random_state=0)


# In[20]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)


# In[22]:


from sklearn.metrics import classification_report, confusion_matrix
print((confusion_matrix(y_test,y_pred)))


# In[23]:


print((classification_report(y_test,y_pred)))
print(metrics.mean_squared_error(y_test, y_pred))


# In[24]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
print(metrics.mean_squared_error(y_test, ypredict))


# In[25]:


k_range = list(range(1, 51))
scores = []
for i in k_range:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.mean_squared_error(y_test, y_pred))
    import matplotlib.pyplot as plt
plt.plot(scores,marker='o')
plt.show()


# In[26]:


from sklearn.model_selection import GridSearchCV
k_range = list(range(1, 51))
print(k_range)


# In[27]:


param_grid = dict(n_neighbors=k_range)
print(param_grid)


# In[28]:


from sklearn.metrics import mean_squared_error, make_scorer, r2_score
#score = make_scorer(mean_squared_error)
grid = GridSearchCV(knn, param_grid, cv=10,scoring='accuracy',return_train_score=False)
grid.fit(X, y)


# In[29]:


grid_mean_scores = grid.cv_results_['mean_test_score']
print(grid_mean_scores)


# In[30]:


plt.plot(grid_mean_scores, marker='o')
plt.xlabel('Value of K for KNN')
plt.ylabel('accuracy')


# In[ ]:




