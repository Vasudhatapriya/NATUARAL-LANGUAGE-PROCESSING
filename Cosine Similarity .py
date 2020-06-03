#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize


# In[8]:


#entering 2 sentences
X ="weekends are so fun"
Y ="no, we have a lot of words on weekends"


# In[9]:


# tokenization 
X_list = word_tokenize(X)  
Y_list = word_tokenize(Y)


# In[10]:


# sw contains the list of stopwords 
sw = stopwords.words('english')  
l1 =[];l2 =[] 


# In[11]:


# remove stop words from string 
X_set = {w for w in X_list if not w in sw}  
Y_set = {w for w in Y_list if not w in sw}


# In[12]:


# form a set containing keywords of both strings  
rvector = X_set.union(Y_set)  
for w in rvector: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0) 
c = 0


# In[13]:


# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 
print("similarity: ", cosine) 


# In[ ]:




