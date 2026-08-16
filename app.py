import streamlit as st
import joblib

model = joblib.load("government_sentiment_prediction_model.pkl")

st.set_page_config(
    page_title="Government Sentiment Prediction",
    page_icon="📊"
)

st.title("Government Sentiment Prediction")

text = st.text_area(
    "Enter government feedback",
    placeholder="Example: The government scheme is very useful."
)

if st.button("Predict Sentiment"):
    if text.strip():
        prediction = model.predict([text])[0]
        st.success(f"Predicted Sentiment: {prediction}")
    else:
        st.warning("Please enter some text.")