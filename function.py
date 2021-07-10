#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re #regular expression
import xlwt #library untuk membaca data pada excel
from nltk.tokenize import word_tokenize #libray untuk tokenizing
#Sastrawi Library untuk Stemming dan Stopword Removal Data Set Bahasa Indonesia
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory 
factori = StemmerFactory()
stemmer = factori.create_stemmer()
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
class hadisClass(object):
    def __init__(self,hadis,k1,k2,k3):
        self.hadis = hadis
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3   
        
def openFile(wb):  
    hadisContent = []
    items= []
    for sheet in wb.sheets():
        num_row, num_col = sheet.nrows,4
        for row in range(num_row):
            values = []
            for col in range(num_col):
                if col == 0:
                    x = (sheet.cell(row,col).value)
                value = (sheet.cell(row,col).value)
                values.append(value)
            hadisContent.append(x)
            item = hadisClass(*values)
            items.append(item)
    return hadisContent, items
def prepro(datahadis):
    dhadis=[]
    for i in datahadis:
        cleanning = re.sub('[^a-zA-z\s]','', i)                   
        casefold = cleanning.lower();
        stopW = stopword.remove(casefold)   
        stemming = stemmer.stem(stopW)                                        
        tokens = word_tokenize(stemming)                                      
        dhadis.append(tokens)
    return dhadis


# In[ ]:




