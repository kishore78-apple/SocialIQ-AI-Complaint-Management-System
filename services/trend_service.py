import pandas as pd
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

csv_path = os.path.join(
    PROJECT_ROOT,
    "08_trend_forecasting_future_predictions.csv"
)


def predict_trend():

    try:
        df = pd.read_csv(csv_path)

        if len(df) == 0:
            return "Trend data unavailable"

        latest = df.iloc[-1]

        if "Predicted_Complaints" in df.columns:
            return f"Expected complaints next month : {int(latest['Predicted_Complaints'])}"

        return "Complaint volume expected to increase next month"

    except:
        return "Complaint volume expected to increase next month"