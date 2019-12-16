# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:36:36 2019

@author: bestm
"""

import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import pickle
from sklearn.tree import DecisionTreeClassifier

class predictionDefault:
    def __init__(self,result):
        self.result = result;
    
    def serialie(self):
        return {'sonuç': self.result}

app = Flask(__name__)
model = pickle.load(open('modelCredit2.pkl','rb'))

@app.route('/')
def index():
    return '<h1>Sektör45 Bank Otomation</h1>'


@app.route('/credit',methods=['POST'])
def predict():
   if(request.data != None):
       jdata = request.get_json()
       credit = jdata['credit']
       age = jdata['age']
       homeState = jdata['home']
       creditC = jdata['creditCount']
       phoneState = jdata['phoneState']
       ctrl1 = isinstance(credit,str)
       ctrl2 = isinstance(age,str)
       ctrl3 = isinstance(homeState,str)
       ctrl4 = isinstance(creditC,str)
       ctrl5 = isinstance(phoneState,str)
       if( ctrl1 == False & ctrl2 == False & ctrl3 == False & ctrl4 == False & ctrl5 == False): 
           
           prediction = model.predict([[int(credit),int(age),int(homeState),int(creditC),int(phoneState)]])
           
           salary = prediction[0]
           state = "Kredi Verme"
           if(round(salary)==1):
               state = "Kredi Ver"
          
           
           return jsonify({"error":None,"data":{"CrediState": state}})    
       else:
           return jsonify({'error': 'Invalid value. Please just post number value',"data":None})
    
   else:
       return jsonify({'error': 'No value. Please just post number value',"data":None})

if __name__ == '__main__':
    try:
        app.run(debug=False, port=8080)
        print("Server is opened")
    except:
        print("Server is exited unexpectedy. Please contat server admin.")

