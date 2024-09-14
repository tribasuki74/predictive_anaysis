# filename: deploy.py
# statement to run fastapi dev deploy.py

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import pickle

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, classification_report

class Data(BaseModel):
    gender: int = 0 # Female
    age: int = 50 # Adulthood
    hypertension: int = 0 # non-hypertension
    heart_disease: int = 1 # has heart disease
    smoking_history: int = 3 # not current
    bmi: float = 25.19 # over weight
    HbA1c_level: float = 6.6 # possible diabetic
    blood_glucose_level: int = 140 # quite high

app = FastAPI()

@app.post("/predict")
async def create_item(data: Data):
    label = ['Non-diabetic', 'Diabetic']
    # Extract features from the data sent via POST
    features = [data.gender, data.age, data.hypertension, data.heart_disease, 
                data.smoking_history, data.bmi, data.HbA1c_level, data.blood_glucose_level]

    # Load from pk1 file
    model = pickle.load(open('random-forest-model.pk1' , 'rb'))

    # Make prediction
    prediction = model.predict([features])
    print(prediction)
    
    # Send back the prediction as a json
    result = {'result': int(prediction[0]), 'message': label[prediction[0]], 'status': True}
    print(result)
    return result
    
   