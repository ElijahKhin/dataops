import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path("models/churn_model.joblib")


def load_model():
    return joblib.load(MODEL_PATH)


def predict(data: pd.DataFrame):

    model = load_model()

    probs = model.predict_proba(data)[:, 1]

    return probs


if __name__ == "__main__":

    example = pd.DataFrame({
        "days_since_last_order": [10, 80],
        "orders_30d": [3, 0],
        "avg_check": [2000, 700],
        "discount_usage_rate": [0.3, 0.9],
        "is_loyalty_member": [1, 0]
    })

    predictions = predict(example)

    print(predictions)
