from services.feedback_service import predict_feedback

complaint = "Garbage has not been collected for five days."

print(predict_feedback(complaint))