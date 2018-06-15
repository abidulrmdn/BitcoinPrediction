#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:49:38 2018

@author: abdul.ramadan
"""

#Import 3 datasets (keywords, tweets, btcoinValue)
#import pandas as pd
def plotData(X_train, X_test, y_train, y_test, pred_X):
    import matplotlib.pyplot as plt
    # Visualising the Training set results
    plt.scatter(X_train, y_train, color = 'red')
    plt.plot(X_train, pred_X, color = 'blue')
    plt.title('BTCVal vs KFreq (Training set)')
    plt.xlabel('Frequency of Kwords')
    plt.ylabel('BTCVal')
    plt.show()
    
    # Visualising the Test set results
    plt.scatter(X_test, y_test, color = 'red')
    plt.plot(X_train, pred_X, color = 'blue')
    plt.title('BTCVal vs KFreq (Test set)')
    plt.xlabel('Frequency of Kwords')
    plt.ylabel('BTCVal')
    plt.show()