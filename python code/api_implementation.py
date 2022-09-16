# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 12:09:59 2022

@author: Walid
"""

import json
import requests


url = 'http://localhost:8000/diabetes_prediction'

# Diabete example of values
input_data_for_model = {
    
    'Pregnancies': 6,
    'Glucose' : 148,
    'BloodPressure' : 72,
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 50

    }

# Non-diabete example of values
input_data_for_model = {
    
    'Pregnancies': 1,
    'Glucose' : 85,
    'BloodPressure' : 66,
    'SkinThickness' : 29,
    'Insulin' : 0,
    'BMI' : 26.6,
    'DiabetesPedigreeFunction' : 0.351,
    'Age' : 31

    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data= input_json)

print(response.text)