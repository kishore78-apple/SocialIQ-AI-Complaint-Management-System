import os
import joblib

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

MODELS_FOLDER = os.path.join(PROJECT_ROOT, "models")

vectorizer = joblib.load(
    os.path.join(MODELS_FOLDER, "feedback_tfidf_vectorizer.pkl")
)

model = joblib.load(
    os.path.join(MODELS_FOLDER, "feedback_category_prediction_model.pkl")
)

encoder = joblib.load(
    os.path.join(MODELS_FOLDER, "feedback_label_encoder.pkl")
)


def predict_feedback(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)
    return str(encoder.inverse_transform(prediction)[0])