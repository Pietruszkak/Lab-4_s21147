import joblib
import pandas as pd
from typing import Union
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from sklearn.preprocessing import LabelEncoder, StandardScaler
from typing import List, Union

model = joblib.load('score_pred_model.joblib')
label_encoders = joblib.load('LabelEncoder.joblib')
scaler= joblib.load('StandardScaler.joblib')

class UserData(BaseModel):
    gender: str
    ethnicity: str
    fcollege: bool
    mcollege: bool
    home: bool
    urban: bool
    unemp: float
    wage: float
    distance: float
    tuition: float
    education: int
    income: str
    region: str

data={}

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Define a route to accept the JSON payload
@app.post("/submit-data")
async def submit_data(data: Union[UserData, List[UserData]] = Body(...)):

    if isinstance(data, UserData):
        data = [data]

    data_dicts = [dat.dict() for dat in data]
    df = pd.DataFrame(data_dicts, columns=['gender', 'ethnicity', 'fcollege', 'mcollege', 'home', 'urban', 'unemp', 'wage', 'distance', 'tuition', 'education', 'income', 'region'])
    categorical_columns = ['gender', 'ethnicity', 'income', 'region']
    boolean_columns = ['fcollege', 'mcollege', 'home', 'urban']
    numerical_columns = ['unemp', 'wage', 'distance', 'tuition', 'education']

    # Encoding categorical columns
    for column in categorical_columns:
        df[column] = label_encoders[column].transform(df[column])

    # Converting yes/no columns to binary 1/0
    for column in boolean_columns:
        df[column] = df[column].apply(lambda x: 1 if x == True else 0)

    # Scale numerical columns
    df[numerical_columns] = scaler.transform(df[numerical_columns])

    predictions=model.predict(df)
    print(predictions)
    
    return {"received_data": predictions.tolist()}