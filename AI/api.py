from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import json

app=FastAPI()

class model_input(BaseModel):
    BHK : int()
    Size : int()
    Floor : int()
    AreaType:int()
    City:int()
    FurnishingStatus:int()
    TenantPreferred:int()
    
    
    
house = joblib.load('model_HouseRent')

@app.post('/rent')
def house_rent(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    bhk1 = input_dictionary['BHK']
    size1 = input_dictionary['Size']
    floor1 = input_dictionary['Floor']
    area1=input_dictionary['Area Type']
    city1=input_dictionary['City']
    status1=input_dictionary['Furnishing Status']
    tenant1=input_dictionary['Tenant Preferred']
    
    input_list = [bhk1,size1,floor1,area1,city1,status1,tenant1]
    prediction = model_HouseRent.predict([input_list])
    
    if prediction[0] == 10000:
        return 'the rent is 10000'
    else:
        return 'No'
        