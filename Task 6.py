#!/usr/bin/env python
# coding: utf-8

# In[1]:


#function for returning last letter of names
def gender_features(word):
    return{'last_letter':word[-1]}


# In[2]:


#testing
gender_features('Obama')


# In[3]:


#importing the libraries
from nltk.corpus import names


# 

# In[4]:


#importing the words in it
names.words()


# In[5]:


#labelling according to their gender
labeled_names=([(name,'male') for name in names.words('male.txt')] + [(name,'female') for name in names.words('female.txt')])


# In[6]:


labeled_names


# In[7]:


import random


# In[8]:


#shuffling the dataset of names
random.shuffle(labeled_names)


# In[9]:


featureSets=[(gender_features(n),gender) for (n,gender) in labeled_names]


# In[10]:


featureSets


# In[11]:


#diving into test and train set
train_set,test_set=featureSets[5000:], featureSets[:2000]


# In[12]:


#importing the text classifier
import nltk
classifier=nltk.NaiveBayesClassifier.train(train_set)


# In[13]:


#testing time on random names
classifier.classify(gender_features('Vasudha'))


# In[14]:


#testing time on random names
classifier.classify(gender_features('Tavish'))


# In[17]:


#testing time on random names
classifier.classify(gender_features('Alka'))


# In[18]:


#testing time on random names
classifier.classify(gender_features('Mohan'))


# In[ ]:




