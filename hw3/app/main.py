from fastapi import FastAPI, HTTPException
from app.schemas import ClientFeatures
from app.model import load_model, predict

app = FastAPI(title="Churn Prediction API")

model = None


@app.on_event("startup")
def startup_event():
    global model
    model = load_model()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict_churn(features: ClientFeatures):

    try:
        result = predict(model, features)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
