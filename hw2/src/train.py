import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import joblib
from pathlib import Path


DATA_PATH = Path("data/churn.csv")
MODEL_PATH = Path("models/churn_model.joblib")


def load_data():
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["churn"])
    y = df["churn"]
    return X, y


def build_pipeline():

    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("model", LogisticRegression())
    ])

    return pipeline


def train():

    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    pipeline = build_pipeline()

    pipeline.fit(X_train, y_train)

    preds = pipeline.predict_proba(X_test)[:, 1]

    auc = roc_auc_score(y_test, preds)

    print(f"ROC-AUC: {auc:.3f}")

    MODEL_PATH.parent.mkdir(exist_ok=True)

    joblib.dump(pipeline, MODEL_PATH)

    print("Model saved:", MODEL_PATH)


if __name__ == "__main__":
    train()
