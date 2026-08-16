from predict import predict_all

complaint = "Garbage has not been collected for five days."

results = predict_all(complaint)

print("\n===== AI Predictions =====")

for key, value in results.items():
    print(f"{key} : {value}")