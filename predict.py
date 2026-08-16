from services.department_service import predict_department
from services.sentiment_service import predict_sentiment
from services.feedback_service import predict_feedback
from services.harmful_service import predict_harmful
from services.emergency_service import predict_emergency


def predict_all(complaint):

    results = {}

    try:
        results["department"] = predict_department(complaint)
    except Exception as e:
        results["department"] = f"Error: {e}"

    try:
        results["sentiment"] = predict_sentiment(complaint)
    except Exception as e:
        results["sentiment"] = f"Error: {e}"

    try:
        results["feedback_category"] = predict_feedback(complaint)
    except Exception as e:
        results["feedback_category"] = f"Error: {e}"

    try:
        results["harmful_content"] = predict_harmful(complaint)
    except Exception as e:
        results["harmful_content"] = f"Error: {e}"

    try:
        results["emergency"] = predict_emergency(complaint)
    except Exception as e:
        results["emergency"] = f"Error: {e}"

    return results