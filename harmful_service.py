import os
import joblib

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

MODELS_FOLDER = os.path.join(PROJECT_ROOT, "models")

harmful_model = joblib.load(
    os.path.join(MODELS_FOLDER, "harmful_content_prediction_model.pkl")
)


def predict_harmful(text):
    prediction = harmful_model.predict([text])[0]

    labels = {
        0: "Safe",
        1: "Harmful"
    }

    try:
        return labels[int(prediction)]
    except:
        return str(prediction)