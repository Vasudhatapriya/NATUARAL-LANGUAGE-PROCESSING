#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.corpus import stopwords


# In[2]:


stopwords.words('english')


# In[3]:


stopwords.words('hindi')


# In[4]:


stopwords.words('french')


# In[5]:


import nltk


# In[6]:


entries=nltk.corpus.cmudict.entries()


# In[7]:


len(entries)


# In[ ]:





# In[ ]:





# In[8]:


for entry in entries:
    print(entry)


# In[9]:


for entry in entries[0:50]:
    print(entry)


# In[10]:


*01.10.2020


# In[11]:


#01.10.2020


# In[12]:


from nltk.corpus import as wn


# In[13]:


from nltk.corpus import wordnet as wn


# In[14]:


wn.synsets('motorcar') 


# In[16]:


wn.synset('car.n.01').lemma_names()


# In[17]:


from nltk.corpus import wordnet as wn


# In[18]:


wn.synsets('tom cruise')


# In[19]:


import nltk 
texts='''Thomas Cruise[1] (born Thomas Cruise Mapother IV; July 3, 1962) is an American actor and film producer. He has received several accolades for his work, including three Golden Globe Awards and nominations for three Academy Awards. Cruise is one of the best-paid actors in the world,[2] and his films have grossed over $4 billion in North America and over $10.1 billion worldwide,[3] making him one of the highest-grossing box-office stars of all time.[4]'''
for text in texts:
    sentences=nltk.sent_tokenize(text)
    for sentence in sentences:
        words=nltk.word_tokenize(sentence)
        tagged_words=nltk.pos_tag(words)
        print(tagged_words)


# In[20]:


#10.1.2020


# In[21]:


import nltk 
texts='''Thomas Cruise[1] (born Thomas Cruise Mapother IV; July 3, 1962) is an American actor and film producer. He has received several accolades for his work, including three Golden Globe Awards and nominations for three Academy Awards. Cruise is one of the best-paid actors in the world,[2] and his films have grossed over $4 billion in North America and over $10.1 billion worldwide,[3] making him one of the highest-grossing box-office stars of all time.[4]'''
for text in texts:
    sentences=nltk.sent_tokenize(text)
    for sentence in sentences:
        words=nltk.word_tokenize('College is boring sometimes :D')
        tagged_words=nltk.pos_tag(words)
        print(tagged_words)


# In[22]:


import nltk
from nltk.tokenize import TweetTokenizer
text='The college is boring sometimes'
twtkn=TweetTokenizer()
twtkn.tokenize(text)


# In[23]:


import nltk
from nltk.tokenize import TweetTokenizer
text='The college is boring sometimes :D'
twtkn=TweetTokenizer()
twtkn.tokenize(text)


# In[24]:


#the tweet tokenizer is abkle to judge the emoji :D while the above tokenozer is not able to


# In[25]:


from nltk.corpus import brown
news_text=brown.words(categories='news')
fdist=nltk.FreqDist(w.lower() for w in news_text)
modals=['can','could','may','might']
for m in modals:
    print(m+':',fdist[m],end='')


# In[29]:


from nltk.corpus import brown
news_text=brown.words(categories='religion')
fdist=nltk.FreqDist(w.lower() for w in news_text)
modals=['can','hello','may','might']
for m in modals:
    print(m+':',fdist[m],end='')


# In[28]:


from nltk.corpus import brown
news_text=brown.words(categories='fiction')
fdist=nltk.FreqDist(w.lower() for w in news_text)
modals=['can','hello','may','might']
for m in modals:
    print(m+':',fdist[m],end='')


# In[ ]:


#18BCE0870
#10/01/2020

