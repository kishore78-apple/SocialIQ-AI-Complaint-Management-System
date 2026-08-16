from services.priority_service import predict_priority

tests = [
    "Street light is not working",
    "Garbage has not been collected",
    "Water leakage on the road",
    "There is a bomb threat in the station",
    "Need information about property tax"
]

for t in tests:
    print(f"Complaint: {t}")
    print("Priority:", predict_priority(t))
    print("-" * 50)