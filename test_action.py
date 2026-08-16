from services.government_action_service import predict_government_action

text = "Garbage has not been collected for two weeks."

result = predict_government_action(text)

print("Government Action:", result)