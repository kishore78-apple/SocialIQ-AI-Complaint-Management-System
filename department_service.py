import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODELS = os.path.join(BASE_DIR, "models")

vectorizer = joblib.load(
    os.path.join(MODELS, "04_tfidf_vectorizer.pkl")
)

model = joblib.load(
    os.path.join(MODELS, "04_department_model.pkl")
)

encoder = joblib.load(
    os.path.join(MODELS, "04_label_encoder.pkl")
)


def predict_department(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)
    return str(encoder.inverse_transform(prediction)[0])