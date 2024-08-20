from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

class UserMeasurements(BaseModel):
    chest: float
    shoulder: float
    front_length: float
    sleeve_length: float

@app.get('/')
async def root():
    return {"message": "API up and running"}

@app.post('/predict')
async def predict_size(user: UserMeasurements):
    chest_weighted = user.chest * 1.5
    shoulder_weighted = user.shoulder * 2.0

    user_input = pd.DataFrame([{
        'Chest_weighted': chest_weighted,
        'Shoulder_weighted': shoulder_weighted,
        'Front_Length': user.front_length,
        'Sleeve_length': user.sleeve_length
    }])

    predicted_size_num = model.predict(user_input)[0]

    size_map = {0: 'XS', 1: 'S', 2: 'M', 3: 'L', 4: 'XL', 5: 'XXL'}
    predicted_size = size_map[predicted_size_num]

    return {"predicted_size": predicted_size}
