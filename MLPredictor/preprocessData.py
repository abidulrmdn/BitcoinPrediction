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
#truncate dataset file
f = open('dataplace/test.csv','w')
f.truncate() #Give your csv text here.
f.close()

#open dataset for appending
f = open('dataplace/test.csv','a')
f.write('hi, there\n') #Give your csv text here.
f.write('no, way\n') #Give your csv text here.
## Python will convert \n to os.linesep
f.close()
test = pd.read_csv('dataplace/test.csv')
for word in keywords:
    print(word)