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

@app.route('/api',methods=['POST'])
def predict():
   if(request.data):
       jdata = request.get_json()
       if jdata['exp']:
           text = jdata['exp']
           text1 = float(text)
           prediction = model.predict([[text1]])
           print(prediction)
           p = int(prediction[0][1])
           return jsonify({'answer': p })    
    
    

if __name__ == '__main__':
    try:
        app.run(debug=False, port=3000)
        print("Server is opened")
    except:
        print("Server is exited unexpectedy. Please contat server admin.")

