from io import StringIO
from fastapi import FastAPI, File, Form, UploadFile
import pickle
from pydantic import BaseModel
import requests
import pandas as pd


app = FastAPI()

class breastCancer(BaseModel):
    mean_radius: float
    mean_texture: float
    mean_perimeter: float
    mean_area: float
    mean_smoothness: float
    mean_compactness: float
    mean_concavity: float
    mean_concave_points: float
    mean_symmetry: float
    mean_fractal_dimension: float
    radius_error: float
    texture_error: float
    perimeter_error: float
    area_error: float
    smoothness_error: float
    compactness_error: float
    concavity_error: float
    concave_points_error: float
    symmetry_error: float
    fractal_dimension_error: float
    worst_radius: float
    worst_texture: float
    worst_perimeter: float
    worst_area: float
    worst_smoothness: float
    worst_compactness: float
    worst_concavity: float
    worst_concave_points: float
    worst_symmetry: float
    worst_fractal_dimenstion: float


@app.get("/")
async def root():
    return {"Message":"Hello world"}

@app.post("/predict")
async def predict_cancer(cancer:breastCancer):
    data = cancer.dict()
    data_in = [data['mean_radius'],data['mean_texture'],data['mean_perimeter'],data['mean_area'],data['mean_smoothness'],data['mean_compactness'],data['mean_concavity'],data['mean_concave_points'],data['mean_symmetry']
               ,data['mean_fractal_dimension'],data['radius_error'],data['texture_error'],data['perimeter_error'],data['area_error'],data['smoothness_error'],data['compactness_error'],data['concavity_error'],data['concave_points_error'],data['symmetry_error'],data['fractal_dimension_error'],data['worst_radius'],data['worst_texture'],data['worst_perimeter'],data['worst_area']
               ,data['worst_smoothness'],data['worst_compactness'],data['worst_concavity'],data['worst_concave_points'],data['worst_symmetry'],data['worst_fractal_dimenstion']]

    endpoint = "http://127.0.0.1:1234/invocations"
    interference_request = {
        "dataframe_records":[data_in]
    }
    print(data_in)
    response = requests.post(endpoint, json=interference_request)
    return {
            "prediction":response.text
        }

@app.post("/files/")
async def batch_prediction(file: bytes = File(...)):
    s = str(file,'utf-8')
    data=StringIO(s)
    df = pd.read_csv(data)
    lst = df.values.tolist()
    endpoint = "http://127.0.0.1:1234/invocations"
    interference_request = {
        "dataframe_records":lst
    }
    response = requests.post(endpoint, json=interference_request)
    return {
            "prediction":response.text
        }