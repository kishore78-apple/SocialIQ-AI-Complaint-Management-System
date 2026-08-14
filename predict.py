import sys
import os


# =====================================================
# PROJECT ROOT
# =====================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


# =====================================================
# AI SERVICES
# =====================================================

from services.department_service import predict_department
from services.feedback_service import predict_feedback
from services.sentiment_service import predict_sentiment
from services.harmful_service import predict_harmful
from services.emergency_service import predict_emergency
from services.priority_service import predict_priority
from services.trend_service import predict_trend
from services.anomoly_service import detect_anomaly
from services.government_action_service import predict_government_action


# =====================================================
# GOVERNMENT ACTION MAPPING
# =====================================================

def get_department_action(department, complaint):
    """
    Generate a department-consistent government action.

    The Government Action model is still executed, but the
    final action is aligned with the predicted department
    so that unrelated departments are not returned.
    """

    department_text = str(department).strip().lower()
    complaint_text = str(complaint).strip().lower()

    # -------------------------------------------------
    # ELECTRICITY
    # -------------------------------------------------

    electricity_keywords = [
        "electricity",
        "electrical",
        "power",
        "transformer",
        "electric wire",
        "electrical wire",
        "power line",
        "electric pole",
        "electric shock",
        "current",
        "voltage",
        "power outage",
        "electricity outage",
    ]

    if (
        "electricity" in department_text
        or "electrical" in department_text
        or "power" in department_text
        or any(keyword in complaint_text for keyword in electricity_keywords)
    ):
        if any(
            keyword in complaint_text
            for keyword in [
                "fallen wire",
                "electric wire",
                "electrical wire",
                "sparks",
                "spark",
                "electric shock",
                "live wire",
                "dangerous wire",
                "transformer explosion",
            ]
        ):
            return "Electricity Department - Emergency Electrical Services"

        return "Electricity Department - Electrical Services"


    # -------------------------------------------------
    # WATER SUPPLY
    # -------------------------------------------------

    water_keywords = [
        "water supply",
        "drinking water",
        "water shortage",
        "no water",
        "water pipeline",
        "water pipe",
        "water leakage",
        "water leak",
    ]

    if (
        "water" in department_text
        or "water supply" in department_text
        or any(keyword in complaint_text for keyword in water_keywords)
    ):
        return "Water Supply Department - Water Services"


    # -------------------------------------------------
    # DRAINAGE
    # -------------------------------------------------

    drainage_keywords = [
        "drainage",
        "drain",
        "sewer",
        "sewage",
        "blocked drain",
        "drain blockage",
        "sewer blockage",
        "storm water drain",
    ]

    if (
        "drain" in department_text
        or "sewer" in department_text
        or "sanitation" in department_text
        or any(keyword in complaint_text for keyword in drainage_keywords)
    ):
        return "Drainage Department - Drainage and Sewerage Services"


    # -------------------------------------------------
    # ROADS / PUBLIC WORKS
    # -------------------------------------------------

    road_keywords = [
        "road",
        "pothole",
        "potholes",
        "street",
        "highway",
        "footpath",
        "pavement",
        "road damage",
        "road repair",
    ]

    if (
        "road" in department_text
        or "public works" in department_text
        or "pothole" in department_text
        or any(keyword in complaint_text for keyword in road_keywords)
    ):
        return "Public Works Department - Road Maintenance"


    # -------------------------------------------------
    # HEALTH / HOSPITAL
    # -------------------------------------------------

    health_keywords = [
        "hospital",
        "doctor",
        "medical",
        "health",
        "patient",
        "medicine",
        "treatment",
        "clinic",
        "ambulance",
    ]

    if (
        "health" in department_text
        or "hospital" in department_text
        or "medical" in department_text
        or any(keyword in complaint_text for keyword in health_keywords)
    ):
        return "Health Department - Healthcare Services"


    # -------------------------------------------------
    # SANITATION / GARBAGE
    # -------------------------------------------------

    sanitation_keywords = [
        "garbage",
        "waste",
        "trash",
        "rubbish",
        "dirty",
        "sanitation",
        "waste collection",
        "garbage collection",
    ]

    if (
        "sanitation" in department_text
        or "municipal" in department_text
        or "waste" in department_text
        or "garbage" in department_text
        or any(keyword in complaint_text for keyword in sanitation_keywords)
    ):
        return "Sanitation Department - Waste Management"


    # -------------------------------------------------
    # TRANSPORT
    # -------------------------------------------------

    transport_keywords = [
        "bus",
        "transport",
        "public transport",
        "vehicle",
        "traffic",
        "bus service",
        "bus stop",
    ]

    if (
        "transport" in department_text
        or "traffic" in department_text
        or any(keyword in complaint_text for keyword in transport_keywords)
    ):
        return "Transport Department - Public Transport Services"


    # -------------------------------------------------
    # GOVERNMENT OFFICE / ADMINISTRATION
    # -------------------------------------------------

    government_keywords = [
        "government office",
        "government employee",
        "certificate",
        "application",
        "official",
        "document",
        "office",
        "application status",
    ]

    if (
        "government" in department_text
        or "administration" in department_text
        or "revenue" in department_text
        or any(keyword in complaint_text for keyword in government_keywords)
    ):
        return "Government Administration Department - Application and Grievance Services"


    # -------------------------------------------------
    # DEFAULT
    # -------------------------------------------------

    return "Concerned Government Department - Appropriate Action"


# =====================================================
# MAIN PREDICTION FUNCTION
# =====================================================

def predict_all(complaint: str):

    results = {}

    # =================================================
    # DEPARTMENT
    # =================================================

    try:
        results["department"] = predict_department(complaint)

    except Exception as e:
        print("Department Error:", e)
        results["department"] = "Unknown"


    # =================================================
    # SENTIMENT
    # =================================================

    try:
        results["sentiment"] = predict_sentiment(complaint)

    except Exception as e:
        print("Sentiment Error:", e)
        results["sentiment"] = "Unknown"


    # =================================================
    # FEEDBACK CATEGORY
    # =================================================

    try:
        results["feedback_category"] = predict_feedback(complaint)

    except Exception as e:
        print("Feedback Error:", e)
        results["feedback_category"] = "Unknown"


    # =================================================
    # HARMFUL CONTENT
    # =================================================

    try:
        results["harmful"] = predict_harmful(complaint)

    except Exception as e:
        print("Harmful Error:", e)
        results["harmful"] = "Unknown"


    # =================================================
    # EMERGENCY
    # =================================================

    try:
        results["emergency"] = predict_emergency(complaint)

    except Exception as e:
        print("Emergency Error:", e)
        results["emergency"] = "Unknown"


    # =================================================
    # PRIORITY
    # =================================================

    try:
        results["priority"] = predict_priority(complaint)

    except Exception as e:
        print("Priority Error:", e)
        results["priority"] = "Unknown"


    # =================================================
    # TREND FORECASTING
    # =================================================

    try:
        results["trend"] = predict_trend()

    except Exception as e:
        print("Trend Error:", e)
        results["trend"] = "Unavailable"


    # =================================================
    # ANOMALY DETECTION
    # =================================================

    try:
        results["anomaly"] = detect_anomaly()

    except Exception as e:
        print("Anomaly Error:", e)
        results["anomaly"] = "Unavailable"


    # =================================================
    # GOVERNMENT ACTION MODEL
    # =================================================

    try:

        # First execute the existing Government Action model.
        model_action = predict_government_action(complaint)

        print("Original Government Action Model:", model_action)

    except Exception as e:

        print("Government Action Model Error:", e)

        model_action = "Unknown"


    # =================================================
    # DEPARTMENT-CONSISTENT GOVERNMENT ACTION
    # =================================================

    try:

        department = results.get("department", "Unknown")

        corrected_action = get_department_action(
            department,
            complaint
        )

        results["government_action"] = corrected_action

        print("Department:", department)
        print("Original Government Action:", model_action)
        print("Corrected Government Action:", corrected_action)

    except Exception as e:

        print("Government Action Mapping Error:", e)

        # If mapping fails, retain the original model result.
        results["government_action"] = model_action


    # =================================================
    # RETURN ALL RESULTS
    # =================================================

    return results