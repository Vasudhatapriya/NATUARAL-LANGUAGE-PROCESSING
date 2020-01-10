#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.corpus import brown


# In[2]:


brown.categories()


# In[3]:


brown.words(categories='adventure')


# In[4]:


brown.words(categories='adventure')[:100]


# In[5]:


len(brown.words(categories='adventure'))


# In[6]:


inaugural.fileids()


# In[7]:


inaugural.fileids()


# In[8]:


from nltk.corpus import inaugural


# In[9]:


inaugural.fileids()


# In[10]:


inaugural.words(fileids='2009-Obama.txt')


# In[11]:


inaugural.words(fileids='2009-Obama.txt')


# In[12]:


inaugural.words(fileids='1865-Lincoln.txt')


# In[ ]:




