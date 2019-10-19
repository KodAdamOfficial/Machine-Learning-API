# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:36:36 2019

@author: bestm
"""

import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import pickle

class predictionDefault:
    def __init__(self,result):
        self.result = result;
    
    def serialie(self):
        return {'sonuç': self.result}

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def index():
    return '<h1>Sektör45 Bank Otomation</h1>'


@app.route('/credit',methods=['POST'])
def predict():
   if(request.data != None):
       jdata = request.get_json()
       exp = jdata['exp']
       cntrl = isinstance(exp, str)
       if cntrl == False:
           text = jdata['exp']
           text1 = float(text)
           prediction = model.predict([[text1]])
           print(prediction)
           salary = str(int(prediction[0][1]))
           return jsonify({"error":None,"data":{"Salary": salary}})    
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

