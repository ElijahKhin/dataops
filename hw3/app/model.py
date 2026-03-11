import random
from app.schemas import ClientFeatures


def load_model():
    print("Loading churn model...")
    return {"version": "1.0-churn-model"}


def predict(model: dict, features: ClientFeatures):

    if features.income > 50000 and features.credit_limit > 10000:
        score = random.uniform(0.7, 0.99)
        prediction = "low_risk"
    else:
        score = random.uniform(0.3, 0.69)
        prediction = "high_risk"

    return {
        "prediction": prediction,
        "score": round(score, 4)
    }
