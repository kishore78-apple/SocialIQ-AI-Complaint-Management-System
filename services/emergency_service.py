import os
import joblib

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

MODELS_FOLDER = os.path.join(PROJECT_ROOT, "models")

model = joblib.load(
    os.path.join(MODELS_FOLDER, "EmergencyDetectionModel.pkl")
)


def predict_emergency(text):
    prediction = model.predict([text])[0]

    labels = {
        0: "Non Emergency",
        1: "Emergency"
    }

    try:
        return labels[int(prediction)]
    except:
        return str(prediction)