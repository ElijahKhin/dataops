import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report

# Пример игрушечного датасета
data = pd.DataFrame({
    "days_since_last_order": [5, 12, 45, 90, 10, 120, 30, 3, 75, 20],
    "orders_30d": [4, 3, 1, 0, 5, 0, 2, 6, 1, 3],
    "avg_check": [2500, 1800, 900, 700, 3200, 500, 1500, 2800, 1100, 2000],
    "discount_usage_rate": [0.2, 0.5, 0.8, 0.9, 0.1, 1.0, 0.4, 0.15, 0.7, 0.3],
    "is_loyalty_member": [1, 1, 0, 0, 1, 0, 1, 1, 0, 1],
    "churn": [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]
})

X = data.drop(columns=["churn"])
y = data["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(random_state=42))
])

model.fit(X_train, y_train)

proba = model.predict_proba(X_test)[:, 1]
pred = model.predict(X_test)

print("ROC-AUC:", round(roc_auc_score(y_test, proba), 3))
print("\nClassification report:")
print(classification_report(y_test, pred))

# Пример скоринга новых клиентов
new_clients = pd.DataFrame({
    "days_since_last_order": [14, 80],
    "orders_30d": [3, 0],
    "avg_check": [2100, 650],
    "discount_usage_rate": [0.35, 0.95],
    "is_loyalty_member": [1, 0]
})

new_clients["churn_probability"] = model.predict_proba(new_clients)[:, 1]
print("\nNew clients scoring:")
print(new_clients)
