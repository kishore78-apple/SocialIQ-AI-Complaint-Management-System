from services.harmful_service import predict_harmful

complaint = "I will attack the government office tomorrow."

print(predict_harmful(complaint))