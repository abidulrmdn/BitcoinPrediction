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
    data2 = pd.read_csv('Data.csv')
    print("Total score for asd")
    return data2