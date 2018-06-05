#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 10:26:45 2018

@author: abdul.ramadan
"""

# Importing the libraries
#import numpy as np
import preprocessData as ppd

# Importing the dataset
dataset = ppd.generateMainDataSet()
X = dataset.iloc[:, :1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

#import visualizeData as vd
#vd.plotData(X_train, X_test, y_train, y_test, regressor.predict(X_train));
print(int(y_pred[-1] > dataset.iloc[-2,-1]))