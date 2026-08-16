import streamlit as st
import os
import requests
import pandas as pd
from datetime import datetime, timedelta

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="SocialIQ AI Complaint Management System",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

API_URL = os.getenv(
    "API_URL",
    "https://socialiq-ai-complaint-management-system-1.onrender.com/predict",
)

# =====================================================
# SESSION STATE
# =====================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "last_prediction" not in st.session_state:
    st.session_state.last_prediction = None

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>
    .main {
        background: #f5f7fb;
    }

    .title {
        font-size: 42px;
        font-weight: 700;
        color: #0B5394;
    }

    .subtitle {
        font-size: 18px;
        color: #666666;
    }

    .footer {
        text-align: center;
        color: gray;
        font-size: 14px;
        padding: 20px;
    }

    /* Force a visible vertical scrollbar in the left sidebar */
    section[data-testid="stSidebar"] > div:first-child {
        height: 100vh;
        overflow-y: scroll !important;
        scrollbar-width: auto;
    }

    section[data-testid="stSidebar"] > div:first-child::-webkit-scrollbar {
        width: 10px;
    }

    section[data-testid="stSidebar"] > div:first-child::-webkit-scrollbar-thumb {
        background: #777777;
        border-radius: 8px;
    }

    section[data-testid="stSidebar"] > div:first-child::-webkit-scrollbar-track {
        background: #20212b;
    }

    .nav-box {
        padding: 10px;
        border-radius: 8px;
        background: #20212b;
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def safe_text(value):
    """Convert prediction values to readable text."""
    if value is None:
        return "Not available"
    return str(value)


def build_history_dataframe():
    """Return history as a DataFrame."""
    if not st.session_state.history:
        return pd.DataFrame()

    return pd.DataFrame(st.session_state.history)


def trend_direction(value):
    """Convert trend prediction text into increase/decrease/stable."""
    text = safe_text(value).lower()

    if any(word in text for word in ["increase", "increasing", "rise", "higher", "up"]):
        return "Increase"
    if any(word in text for word in ["decrease", "decreasing", "fall", "lower", "down"]):
        return "Decrease"
    if any(word in text for word in ["stable", "same", "constant", "no change"]):
        return "Stable"

    return "Unknown"


# =====================================================
# SIDEBAR NAVIGATION
# =====================================================

with st.sidebar:
    st.markdown("## 🏛️ SocialIQ")
    st.caption("AI Complaint Management System")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📝 Complaints",
            "📈 Trend Forecasting",
            "⚠️ Anomaly Detection",
            "🤖 AI Predictions",
            "ℹ️ System Information",
        ],
        index=0,
    )

    st.divider()

    st.markdown("### 📌 Quick Status")
    st.write("🟢 FastAPI Backend")
    st.write("🤖 9 AI Prediction Outputs")
    st.write("🗄️ PostgreSQL")
    st.write(f"📊 Complaints: {len(st.session_state.history)}")

    st.divider()

    st.markdown("### 🔧 Prediction Outputs")
    st.write("1. Department")
    st.write("2. Sentiment")
    st.write("3. Feedback Category")
    st.write("4. Harmful Content")
    st.write("5. Emergency")
    st.write("6. Priority")
    st.write("7. Trend Forecasting")
    st.write("8. Anomaly Detection")
    st.write("9. Government Action")

    st.divider()

    st.caption("© 2026 SocialIQ AI Project")

# =====================================================
# HEADER
# =====================================================

st.markdown(
    '<div class="title">🏛️ SocialIQ AI Complaint Management System</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">Artificial Intelligence Powered Citizen Complaint Classification Dashboard</div>',
    unsafe_allow_html=True,
)

st.divider()

# =====================================================
# DASHBOARD PAGE
# =====================================================

if page == "🏠 Dashboard":

    st.subheader("📊 Dashboard Overview")

    df = build_history_dataframe()

    total = len(df)

    emergency_count = (
        int((df["Emergency"].astype(str).str.lower() == "emergency").sum())
        if not df.empty and "Emergency" in df.columns
        else 0
    )

    harmful_count = (
        int((df["Harmful"].astype(str).str.lower() == "harmful").sum())
        if not df.empty and "Harmful" in df.columns
        else 0
    )

    negative_count = (
        int((df["Sentiment"].astype(str).str.lower() == "negative").sum())
        if not df.empty and "Sentiment" in df.columns
        else 0
    )

    high_priority_count = (
        int(df["Priority"].astype(str).str.lower().isin(["high", "urgent", "critical"]).sum())
        if not df.empty and "Priority" in df.columns
        else 0
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.metric("Total Complaints", total)

    with c2:
        st.metric("🚨 Emergency", emergency_count)

    with c3:
        st.metric("😟 Negative", negative_count)

    with c4:
        st.metric("⭐ High Priority", high_priority_count)

    with c5:
        st.metric("🛡️ Harmful", harmful_count)

    st.divider()

    if df.empty:
        st.info("No complaints submitted yet. Go to 📝 Complaints and analyze a complaint.")
    else:
        st.subheader("📋 Recent Complaints")
        st.dataframe(
            df.tail(10),
            use_container_width=True,
            hide_index=True,
        )

        st.divider()

        st.subheader("🏢 Complaints by Department")

        if "Department" in df.columns:
            department_counts = (
                df["Department"]
                .fillna("Unknown")
                .astype(str)
                .value_counts()
            )
            st.bar_chart(department_counts)

# =====================================================
# COMPLAINT PAGE
# =====================================================

elif page == "📝 Complaints":

    st.subheader("📝 Register New Complaint")

    citizen_name = st.text_input("Citizen Name")

    complaint = st.text_area(
        "Complaint",
        height=180,
        placeholder="Enter the citizen complaint here...",
    )

    predict = st.button(
        "🚀 Analyze Complaint",
        use_container_width=True,
    )

    if predict:

        if not citizen_name.strip():
            st.error("Please enter Citizen Name.")

        elif not complaint.strip():
            st.error("Please enter Complaint.")

        else:

            payload = {
                "citizen_name": citizen_name,
                "complaint": complaint,
            }

            try:

                with st.spinner("Running all AI models..."):

                    response = requests.post(
                        API_URL,
                        json=payload,
                        timeout=60,
                    )

                if response.status_code == 200:

                    data = response.json()

                    complaint_id = data.get("complaint_id", "N/A")
                    prediction = data.get("prediction", {})

                    if not isinstance(prediction, dict):
                        prediction = {}

                    st.session_state.last_prediction = prediction

                    st.session_state.history.append(
                        {
                            "Complaint ID": complaint_id,
                            "Citizen": citizen_name,
                            "Complaint": complaint,
                            "Department": prediction.get("department"),
                            "Priority": prediction.get("priority"),
                            "Sentiment": prediction.get("sentiment"),
                            "Feedback": prediction.get("feedback_category"),
                            "Emergency": prediction.get("emergency"),
                            "Harmful": prediction.get("harmful"),
                            "Trend": prediction.get("trend"),
                            "Anomaly": prediction.get("anomaly"),
                            "Government Action": prediction.get("government_action"),
                            "Time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                        }
                    )

                    st.success("✅ Complaint submitted successfully.")

                    st.subheader("🤖 AI Prediction Results")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.success(
                            f"🏢 Department: {safe_text(prediction.get('department'))}"
                        )
                        st.info(
                            f"⭐ Priority: {safe_text(prediction.get('priority'))}"
                        )
                        st.warning(
                            f"😊 Sentiment: {safe_text(prediction.get('sentiment'))}"
                        )
                        st.info(
                            f"💬 Feedback Category: {safe_text(prediction.get('feedback_category'))}"
                        )
                        st.success(
                            f"🛡️ Harmful Content: {safe_text(prediction.get('harmful'))}"
                        )

                    with col2:
                        st.error(
                            f"🚨 Emergency: {safe_text(prediction.get('emergency'))}"
                        )
                        st.info(
                            f"📈 Trend Forecast: {safe_text(prediction.get('trend'))}"
                        )
                        st.warning(
                            f"⚠️ Anomaly Detection: {safe_text(prediction.get('anomaly'))}"
                        )
                        st.success(
                            f"🏛️ Government Action: {safe_text(prediction.get('government_action'))}"
                        )
                        st.info(f"🆔 Complaint ID: {complaint_id}")

                else:
                    st.error(f"❌ Backend Error: HTTP {response.status_code}")
                    st.code(response.text)

            except requests.exceptions.ConnectionError:
                st.error(
                    "❌ Cannot connect to the SocialIQ FastAPI backend."
                )
                st.info(f"Backend URL: {API_URL}")

            except requests.exceptions.Timeout:
                st.error("❌ Backend request timed out.")

            except Exception as exc:
                st.error("❌ Unexpected error")
                st.exception(exc)

    st.divider()

    st.subheader("📊 Complaint History")

    df = build_history_dataframe()

    if df.empty:
        st.info("No complaints submitted yet.")
    else:
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇️ Download CSV Report",
            data=csv,
            file_name="SocialIQ_Complaints_Report.csv",
            mime="text/csv",
            use_container_width=True,
        )

        if st.button("🗑️ Clear Dashboard History", use_container_width=True):
            st.session_state.history = []
            st.session_state.last_prediction = None
            st.success("Dashboard history cleared successfully.")
            st.rerun()

# =====================================================
# TREND FORECASTING PAGE
# =====================================================

elif page == "📈 Trend Forecasting":

    st.subheader("📈 Trend Forecasting Dashboard")

    df = build_history_dataframe()

    if df.empty:
        st.info("Submit complaints first to generate the trend dashboard.")
    else:

        if "Trend" in df.columns:

            trend_counts = (
                df["Trend"]
                .fillna("Unknown")
                .astype(str)
                .apply(trend_direction)
                .value_counts()
            )

            st.markdown("### 🔮 Forecast Summary")

            latest_trend = str(df.iloc[-1]["Trend"])
            direction = trend_direction(latest_trend)

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("Latest Trend", direction)

            with c2:
                st.metric("Trend Records", len(df))

            with c3:
                if direction == "Increase":
                    status = "📈 Increasing"
                elif direction == "Decrease":
                    status = "📉 Decreasing"
                elif direction == "Stable":
                    status = "➡️ Stable"
                else:
                    status = "ℹ️ Unknown"
                st.metric("Forecast Status", status)

            st.info(f"Latest model forecast: **{latest_trend}**")

            st.divider()

            st.markdown("### 📊 Trend Forecast Graph")

            # Count complaints in submission order.
            # This provides a real graph even when the trend model returns
            # a text prediction instead of a numeric forecast.
            chart_df = pd.DataFrame(
                {
                    "Complaint Number": range(1, len(df) + 1),
                    "Complaint Volume": range(1, len(df) + 1),
                }
            ).set_index("Complaint Number")

            st.line_chart(chart_df, use_container_width=True)

            st.caption(
                "The line shows cumulative complaint volume from the complaints "
                "recorded in the current Streamlit session. The model's textual "
                "forecast is shown above."
            )

            st.divider()

            st.markdown("### 📌 Trend Prediction Distribution")

            if not trend_counts.empty:
                st.bar_chart(trend_counts)

            st.divider()

            st.markdown("### 🧾 Trend Prediction History")

            trend_table = df[
                [
                    col
                    for col in ["Complaint ID", "Time", "Trend"]
                    if col in df.columns
                ]
            ].copy()

            st.dataframe(
                trend_table,
                use_container_width=True,
                hide_index=True,
            )

        else:
            st.warning("Trend prediction data is not available.")

# =====================================================
# ANOMALY DETECTION PAGE
# =====================================================

elif page == "⚠️ Anomaly Detection":

    st.subheader("⚠️ Anomaly Detection Dashboard")

    df = build_history_dataframe()

    if df.empty:
        st.info("Submit complaints first to generate the anomaly dashboard.")
    elif "Anomaly" not in df.columns:
        st.warning("Anomaly prediction data is not available.")
    else:

        anomaly_series = df["Anomaly"].fillna("Unknown").astype(str)

        def is_anomaly(value):
            text = value.strip().lower()

            # Handle explicit normal / non-anomaly results first.
            if any(
                phrase in text
                for phrase in [
                    "no anomaly",
                    "no anomalies",
                    "not anomaly",
                    "normal",
                    "no outlier",
                    "not abnormal",
                ]
            ):
                return False

            return (
                "anomaly" in text
                or "abnormal" in text
                or "outlier" in text
                or text in {"1", "true", "yes"}
            )

        anomaly_flags = anomaly_series.apply(is_anomaly)

        anomaly_count = int(anomaly_flags.sum())
        normal_count = int(len(df) - anomaly_count)

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Total Checked", len(df))

        with c2:
            st.metric("⚠️ Anomalies", anomaly_count)

        with c3:
            st.metric("✅ Normal", normal_count)

        st.divider()

        st.markdown("### 📊 Anomaly Status Graph")

        anomaly_chart = pd.Series(
            {
                "Normal": normal_count,
                "Anomaly": anomaly_count,
            },
            name="Complaints",
        )

        st.bar_chart(anomaly_chart, use_container_width=True)

        st.divider()

        st.markdown("### 🔍 Anomaly Results")

        anomaly_table = df[
            [
                col
                for col in [
                    "Complaint ID",
                    "Complaint",
                    "Department",
                    "Priority",
                    "Anomaly",
                    "Time",
                ]
                if col in df.columns
            ]
        ].copy()

        st.dataframe(
            anomaly_table,
            use_container_width=True,
            hide_index=True,
        )

        st.caption(
            "The anomaly dashboard uses the value returned by the project's "
            "anomaly service. It does not replace the trained anomaly model."
        )

# =====================================================
# AI PREDICTIONS PAGE
# =====================================================

elif page == "🤖 AI Predictions":

    st.subheader("🤖 AI Prediction Dashboard")

    df = build_history_dataframe()

    if df.empty:
        st.info("No AI prediction results are available yet.")
    else:

        prediction_columns = [
            "Complaint ID",
            "Department",
            "Priority",
            "Sentiment",
            "Feedback",
            "Emergency",
            "Harmful",
            "Trend",
            "Anomaly",
            "Government Action",
        ]

        available_columns = [
            col for col in prediction_columns if col in df.columns
        ]

        st.dataframe(
            df[available_columns],
            use_container_width=True,
            hide_index=True,
        )

        st.divider()

        st.markdown("### 🏢 Department Distribution")

        if "Department" in df.columns:
            st.bar_chart(
                df["Department"]
                .fillna("Unknown")
                .astype(str)
                .value_counts()
            )

        st.markdown("### ⭐ Priority Distribution")

        if "Priority" in df.columns:
            st.bar_chart(
                df["Priority"]
                .fillna("Unknown")
                .astype(str)
                .value_counts()
            )

# =====================================================
# SYSTEM INFORMATION PAGE
# =====================================================

elif page == "ℹ️ System Information":

    st.subheader("ℹ️ System Information")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            """
            ### 🤖 AI Prediction Outputs

            ✅ Department Classification

            ✅ Sentiment Analysis

            ✅ Feedback Category Classification

            ✅ Harmful Content Detection

            ✅ Emergency Detection

            ✅ Priority Prediction

            ✅ Trend Forecasting

            ✅ Anomaly Detection

            ✅ Government Action Recommendation
            """
        )

    with col2:
        st.info(
            """
            ### 💻 Technology Stack

            • Python

            • Streamlit

            • FastAPI

            • PostgreSQL

            • SQLAlchemy

            • Scikit-learn

            • Pandas

            • NumPy

            • Joblib

            • Machine Learning
            """
        )

    st.divider()

    st.subheader("📌 Project Summary")

    st.success(
        """
        The SocialIQ AI Complaint Management System automatically analyses
        citizen complaints using Artificial Intelligence.

        The complaint passes through the currently deployed AI prediction pipeline covering
        classification, sentiment, priority, safety, forecasting,
        anomaly detection, and government action recommendation.

        The Streamlit dashboard communicates with the FastAPI backend,
        displays prediction results, maintains complaint history,
        provides trend and anomaly dashboards, and supports CSV export.
        """
    )

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        <h3>🏛️ SocialIQ AI Complaint Management System</h3>
        <p>Artificial Intelligence Powered Citizen Complaint Management Platform</p>
        <p>Built using FastAPI • Streamlit • PostgreSQL • Machine Learning</p>
        <p>© 2026 SocialIQ AI Project</p>
    </div>
    """,
    unsafe_allow_html=True,
)