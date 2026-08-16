from services.sentiment_service import predict_sentiment

complaint = "Garbage has not been collected for five days."

print(predict_sentiment(complaint))