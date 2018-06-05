#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:49:38 2018

@author: abdul.ramadan
"""

#Import 3 datasets (keywords, tweets, btcoinValue)
def generateMainDataSet():
    
    import sys
    tweetsfilePath = './dataplace/tweets.csv'
    if __name__ == "__main__":
        tweetsfilePath = sys.argv[1]
    import pandas as pd
    keywords = pd.read_csv('./dataplace/dictionary.csv').values
    btcData = pd.read_csv('./dataplace/btcvalues.csv').values
    tweetsData = pd.read_csv(tweetsfilePath).values
    #dataset = pd.read_csv('dataplace/Data.csv')
    keywordsFreq = {}
    btcValues = {}
    
    #initialize Keywords freq array and put in file
    f = open('./dataplace/generatedData.csv','w')
    f.truncate()
    index = 0
    for word in keywords:
        keywordsFreq[word[0]] = 0;
        wordSep = word[0]+','
        f.write(wordSep)
        index +=1
    f.write('BTCValues\n')
    f.close()
    test = pd.read_csv('./dataplace/generatedData.csv')
    
    #make the btcoins values as dictionaries
    index = 0
    for btcvalue in btcData:
        index +=1
        btcValues[btcvalue[0]] = btcvalue[1]
    
    
    #pick keywords and flush them in file
    f = open('./dataplace/generatedData.csv','a')
    tmpKeywordsFreq = keywordsFreq.copy()
    currentData = tweetsData[0][0]
    #todo get dictionary key for current tweet
    for tweet in tweetsData:
        #flush into file
        if currentData != tweet[0]:
            currentData = tweet[0]
            for keyword, tmpKeywordFreq in tmpKeywordsFreq.items():
                wordSep = str(tmpKeywordFreq)+','
                f.write(wordSep)
            btcval = str(btcValues[currentData]) + '\n'
            f.write(btcval)
            tmpKeywordsFreq = keywordsFreq.copy()
        #count frequencies
        for word in tmpKeywordsFreq:
            tmpKeywordsFreq[word] += tweet[1].count(word)
    #flush last raw for today to file
    for keyword, tmpKeywordFreq in tmpKeywordsFreq.items():
        wordSep = str(tmpKeywordFreq)+','
        f.write(wordSep)
    btcval = '0\n' #no predicted value
    f.write(btcval)
    f.close()
    generatedData = pd.read_csv('./dataplace/generatedData.csv')
    return generatedData
    
    
    
    
    
    
    
    
    