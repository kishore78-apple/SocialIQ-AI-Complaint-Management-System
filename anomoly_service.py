import pandas as pd
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

csv_path = os.path.join(
    PROJECT_ROOT,
    "09_anomaly_detection_results.csv"
)


def detect_anomaly():

    try:

        df = pd.read_csv(csv_path)

        if len(df) == 0:
            return "No anomaly detected"

        if "Anomaly" in df.columns:

            count = df["Anomaly"].sum()

            if count > 0:
                return f"{count} anomaly cases found"

        return "No anomaly detected"

    except:
        return "No anomaly detected"