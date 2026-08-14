import joblib
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

model = joblib.load(
    os.path.join(
        PROJECT_ROOT,
        "05_priority_prediction_model.pkl"
    )
)


def predict_priority(text):

    prediction = model.predict([text])[0]

    return str(prediction)