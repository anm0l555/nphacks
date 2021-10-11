#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# In[ ]:


iris=load_iris()
X=iris.data
Y=iris.target
df=pd.DataFrame(data=X,columns=iris.feature_names)
df


# In[ ]:


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)


# In[ ]:


def multiclass(X_train,X_test,Y_train,Y_test,w):
  y_train=np.array(Y_train,copy=True)
  y_test=np.array(Y_test,copy=True)
  for i in range(len(y_train)):
    if y_train[i]==w:
      y_train[i]=1
    else:
      y_train[i]=0
  for i in range(len(y_test)):
    if y_test[i]==w:
      y_test[i]=1
    else:
      y_test[i]=0
  n=1000
  alpha=0.01
  m,k=X_train.shape
  beta=np.zeros(k)
  for i in range(n):
    cost_grad=np.zeros(k)
    z=X_train.dot(beta)
    pred=1/(1+np.exp(-z))
    diff=pred-y_train
    for j in range(k):  
      cost_grad[j]=np.sum(diff.dot(X_train[:,j]))
    for j in range(k):
      beta[j]=beta[j]-(alpha/m)*cost_grad[j]
  Y_pred=1/(1+np.exp(-(X_test.dot(beta))))
  Y_label=np.zeros(len(Y_pred))
  for i in range(len(Y_pred)):
    if(Y_pred[i]>=0.5):
      Y_label[i] = 1
  Y_pred=np.array(Y_pred,dtype=int)
  print("Beta values :",beta)
  print("Accuracy score :",accuracy_score(y_test,Y_label))
  cm=confusion_matrix(y_test,Y_label)
  print("Confusion Matrix :")
  print(cm)


# In[ ]:


for i in range(3):
  multiclass(X_train,X_test,Y_train,Y_test,i)
  print("-----------------------------------------------------------------")


# **Doing the question by using sklearn libraries**

# In[ ]:


from sklearn import linear_model
model=linear_model.LogisticRegression(max_iter=120)
model.fit(X_train,Y_train)


# In[ ]:


Y_pred=model.predict(X_test)


# In[ ]:


accuracy_score(Y_test,Y_pred)


# In[ ]:


cm=confusion_matrix(Y_test,Y_pred)
cm

