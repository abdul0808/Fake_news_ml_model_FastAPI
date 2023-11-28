# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:36:48 2022

@author: abdul
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    news_heading: str
    

# loading the saved model
fakenews_model = pickle.load(open('FakeNews_model.sav','rb'))


@app.post('/FakeNews_prediction')
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    news = input_dictionary['news_heading']
    


    input_list = [news]
    
    prediction = fakenews_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The news is Real'
    
    else:
        return 'The news is Fake'


