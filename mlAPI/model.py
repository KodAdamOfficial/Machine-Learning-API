# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json

#Import dataset

dataset = pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,].values

#Split the dataset Training and Testing

from sklearn.model_selection import train_test_split
x_train, x_test , y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state=0)

#▲Fitting SLR to the Training set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)


#Test this model with x_test set
y_pred = regressor.predict(x_test)

#Saving model

pickle.dump(regressor, open('model.pkl','wb'))

#Loading model to compare the results

model = pickle.load(open('model.pkl','rb'))
pro = model.predict([[4.2]])

print(pro)
