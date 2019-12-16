# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('dataset.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,5].values


from sklearn.model_selection import train_test_split
x_train, x_test , y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state=0)



from sklearn.tree import DecisionTreeClassifier



clf = DecisionTreeClassifier().fit(x_train, y_train)

print('Accuracy of Decision Tree classifier on training set: {:.2f}'
     .format(clf.score(x_train, y_train)))
print('Accuracy of Decision Tree classifier on test set: {:.2f}'
     .format(clf.score(x_test, y_test)))

pickle.dump(clf, open('modelCredit2.pkl','wb'))

state = clf.predict([[5000,30,1,2,1]])
print(state[0])
if(round(state[0])==1):
    print("Kredi Ver")
else:
    print("Kredi Yok Sana")    
