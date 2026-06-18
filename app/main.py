from fastapi import FastAPI
import pandas as pd
import joblib

from app.schema import Customer

app = FastAPI(
    title="Customer Churn Prediction API"
)

model = joblib.load("models/model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

@app.get("/")
def home():
    return {
        "message": "Customer Churn API Running"
    }

@app.post("/predict")
def predict(customer: Customer):

    df = pd.DataFrame([customer.model_dump()])

    processed = preprocessor.transform(df)

    prediction = model.predict(processed)[0]

    probability = model.predict_proba(processed)[0][1]

    return {
        "prediction": int(prediction),
        "churn_probability": round(float(probability), 4)
    }