import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Customer_Churn")

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score

# Load dataset
df = pd.read_csv(
    "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# Remove ID column
df.drop("customerID", axis=1, inplace=True)

# Fix TotalCharges
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Target
df["Churn"] = df["Churn"].map({
    "No":0,
    "Yes":1
})

X = df.drop("Churn", axis=1)
y = df["Churn"]

categorical_cols = X.select_dtypes(
    include=["object"]
).columns.tolist()

numeric_cols = X.select_dtypes(
    exclude=["object"]
).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            Pipeline([
                ("imputer",
                 SimpleImputer(strategy="most_frequent")),
                ("encoder",
                 OneHotEncoder(handle_unknown="ignore"))
            ]),
            categorical_cols
        ),
        (
            "num",
            Pipeline([
                ("imputer",
                 SimpleImputer(strategy="median"))
            ]),
            numeric_cols
        )
    ]
)

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

X_train_processed = preprocessor.fit_transform(
    X_train
)

X_test_processed = preprocessor.transform(
    X_test
)

with mlflow.start_run():

    model = RandomForestClassifier(
    n_estimators=500,
    max_depth=15,
    min_samples_split=5,
    class_weight="balanced",
    random_state=42
)

    model.fit(
        X_train_processed,
        y_train
    )

    preds = model.predict(
        X_test_processed
    )

    acc = accuracy_score(
        y_test,
        preds
    )

    f1 = f1_score(
        y_test,
        preds
    )

    mlflow.log_metric(
        "accuracy",
        acc
    )

    mlflow.log_metric(
        "f1",
        f1
    )

    mlflow.sklearn.log_model(
        model,
        "model"
    )

    print("Accuracy:",acc)
    print("F1:",f1)

joblib.dump(
    model,
    "models/model.pkl"
)

joblib.dump(
    preprocessor,
    "models/preprocessor.pkl"
)

joblib.dump(
    X.columns.tolist(),
    "models/features.pkl"
)

print("Training Completed")