from sqlalchemy.orm import Session
import models


def create_complaint(db: Session, citizen_name: str, complaint: str):

    new_complaint = models.Complaint(
        customer_name=citizen_name,
        email="",
        phone="",
        complaint=complaint
    )

    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)

    return new_complaint


def save_prediction(db: Session, complaint_id: int, results: dict):

    prediction = models.Prediction(
        complaint_id=complaint_id,
        department=results.get("department"),
        priority=None,
        sentiment=results.get("sentiment"),
        emergency=results.get("emergency"),
        harmful=results.get("harmful"),
        feedback_category=results.get("feedback_category"),
        government_action=None
    )

    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    return prediction