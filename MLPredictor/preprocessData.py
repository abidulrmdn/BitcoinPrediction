#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:49:38 2018

@author: abdul.ramadan
"""

#Import 3 datasets (keywords, tweets, btcoinValue)
#import pandas as pd
def generateMainDataSet():
    import pandas as pd
    keywords = pd.read_csv('dataplace/dictionary.csv')
    btcvalues = pd.read_csv('dataplace/btcvalues.csv')
    tweets = pd.read_csv('dataplace/tweets.csv')
    dataset = pd.read_csv('dataplace/Data.csv')

    print("DataLoaded")
    return dataset



keywords = pd.read_csv('dataplace/dictionary.csv').values
btcvalues = pd.read_csv('dataplace/btcvalues.csv').values
tweets = pd.read_csv('dataplace/tweets.csv').values
dataset = pd.read_csv('dataplace/Data.csv')
keywordsFreq = {}
#truncate dataset file
f = open('dataplace/test.csv','w')
f.truncate() #Give your csv text here.
#open dataset for appending
#f = open('dataplace/test.csv','w')
index = 0
for word in keywords:
    keywordsFreq[word[0]] = 0;
    wordSep = word[0]+','
    f.write(wordSep)
    index +=1
    print(wordSep)
f.write('BTCValues\n')
## Python will convert \n to os.linesep
f.close()
test = pd.read_csv('dataplace/test.csv')




#keywordsFreq['asd'] = 10;
#if 'asdas' in keywordsFreq:
#    print('yes')