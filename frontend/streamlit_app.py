import streamlit as st
import requests
import os

# Backend API URL
API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000/predict"
)

st.set_page_config(
    page_title="SocialIQ",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ SocialIQ AI Complaint Management System")
st.write(
    "AI-powered complaint analysis and government intelligence platform."
)

st.divider()

st.subheader("Submit a Complaint")

citizen_name = st.text_input(
    "Citizen Name",
    placeholder="Enter your name"
)

complaint = st.text_area(
    "Enter your complaint",
    placeholder="Example: There is no drinking water supply in our area.",
    height=150
)

if st.button("🔍 Analyze Complaint", use_container_width=True):

    if not citizen_name.strip():
        st.warning("Please enter your name.")

    elif not complaint.strip():
        st.warning("Please enter a complaint.")

    else:
        try:

            with st.spinner("SocialIQ AI is analyzing your complaint..."):

                response = requests.post(
                    API_URL,
                    json={
                        "citizen_name": citizen_name,
                        "complaint": complaint
                    },
                    timeout=60
                )

            if response.status_code == 200:

                data = response.json()

                st.success("Complaint analyzed successfully!")

                st.subheader("🤖 AI Analysis Results")

                prediction = data.get("prediction", {})

                col1, col2 = st.columns(2)

                with col1:

                    st.info(
                        f"🏢 Department: "
                        f"{prediction.get('department', 'Unavailable')}"
                    )

                    st.info(
                        f"😊 Sentiment: "
                        f"{prediction.get('sentiment', 'Unavailable')}"
                    )

                    st.info(
                        f"📂 Feedback Category: "
                        f"{prediction.get('feedback_category', 'Unavailable')}"
                    )

                    st.info(
                        f"🚨 Emergency: "
                        f"{prediction.get('emergency', 'Unavailable')}"
                    )

                with col2:

                    st.info(
                        f"⚠️ Harmful Content: "
                        f"{prediction.get('harmful_content', 'Unavailable')}"
                    )

                    st.info(
                        f"🔥 Priority: "
                        f"{prediction.get('priority', 'Unavailable')}"
                    )

                    st.info(
                        f"📈 Trend: "
                        f"{prediction.get('trend', 'Unavailable')}"
                    )

                    st.info(
                        f"🔍 Anomaly: "
                        f"{prediction.get('anomaly', 'Unavailable')}"
                    )

                st.divider()

                st.subheader("🏛️ Government Action")

                st.success(
                    prediction.get(
                        "government_action",
                        "No recommendation available"
                    )
                )

            else:

                st.error(
                    f"Backend error: {response.status_code}"
                )

                st.code(response.text)

        except requests.exceptions.ConnectionError:

            st.error(
                "Unable to connect to the SocialIQ backend."
            )

        except Exception as e:

            st.error(f"Error: {str(e)}")