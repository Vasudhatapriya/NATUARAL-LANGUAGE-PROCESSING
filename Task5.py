#!/usr/bin/env python
# coding: utf-8

# In[1]:


(/18BCE0870)

from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
stemmerporter.stem('happiness')
#wrongly removes the suffix


# In[2]:


import nltk
from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
stemmerporter.stem('fishes')
#works in this case


# In[3]:


import nltk
from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
stemmerporter.stem('phones')


# In[4]:


import nltk
from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
stemmerporter.stem('darling')
#doesn't work in this case


# In[7]:


import nltk
from nltk.stem import LancasterStemmer
stemmerlanc=LancasterStemmer()
stemmerlanc.stem('darling')
#doesn't work here as well


# In[8]:


from nltk.stem import RegexpStemmer
regexpStemmer=RegexpStemmer('ing')
regexpStemmer.stem('dancing')
#doesn't support 


# In[10]:


import nltk 
from nltk.stem import SnowballStemmer 
SnowballStemmer.languages
frenchstemmer=SnowballStemmer('french')
frenchstemmer.stem('manges')


# In[11]:


import nltk
from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
stemmerporter.stem('beautifully')


# In[12]:


import nltk
from nltk.stem import LancasterStemmer
stemmerlanc=LancasterStemmer()
stemmerlanc.stem('beautifully')
#the word beautifully is correctly done with Lancaster but not by Porterstemmer
#works for stem


# In[17]:


from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("geese"))
#works for roots 


# In[18]:


from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("elephunts"))


# In[19]:


from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("elephants"))


# In[20]:


from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("peoples'"))


# In[22]:


from nltk.stem import PorterStemmer

stemmer=PorterStemmer()
ex="Lions love eating the lazy men"
ex=[stemmer.stem(token) for token in ex.split(" ")]
print (" ".join(ex))


# In[23]:


from nltk.stem import PorterStemmer

stemmer=PorterStemmer()
ex="Dancing is peacocks' favourite activity during rainy seasons"
ex=[stemmer.stem(token) for token in ex.split(" ")]
print (" ".join(ex))
#doesn't work here(definitely)


# In[ ]:




