from services.emergency_service import predict_emergency

complaint = "There is a fire in the government hospital. People are trapped."

print(predict_emergency(complaint))