import joblib
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

MODELS = os.path.join(PROJECT_ROOT, "models")

model = joblib.load(
    os.path.join(
        MODELS,
        "government_department_prediction_model.pkl"
    )
)


def predict_government_action(text):

    prediction = model.predict([text])[0]

    return str(prediction)