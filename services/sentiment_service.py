import os
import joblib

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

MODELS_FOLDER = os.path.join(PROJECT_ROOT, "models")

sentiment_model = joblib.load(
    os.path.join(MODELS_FOLDER, "government_sentiment_prediction_model.pkl")
)


def predict_sentiment(text):
    prediction = sentiment_model.predict([text])[0]
    return str(prediction)