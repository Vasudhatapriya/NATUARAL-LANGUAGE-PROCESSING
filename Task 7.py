#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the libraries
from nltk.corpus import brown


# In[2]:


brown


# In[3]:


#printing the categories of brown corpus
brown.categories()


# In[4]:


#printing a few words
brown.words(categories = "science_fiction")[:100]


# In[5]:


#importing library
from nltk.corpus import inaugural


# In[6]:


inaugural.fileids()


# In[7]:


#printing inaugral words for some text
for i in inaugural.words('1933-Roosevelt.txt'):
    print(i, end = " ")


# In[8]:


'''
College is so hectic,I'm tired
'''


# In[9]:


#importing library from nltk.corpus
from nltk.corpus import webtext


# In[10]:


webtext.fileids()


# In[11]:


webtext.words('pirates.txt')[:20]


# In[12]:


#printing first 20 words
file_ids = webtext.fileids()
for file in file_ids:
    print(file)
    print(webtext.words(file)[:20])


# In[ ]:




