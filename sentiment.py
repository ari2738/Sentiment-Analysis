from textblob import TextBlob

def detect_emotion(text):
    text = text.lower()
    
    if any(word in text for word in ["happy", "love", "great", "amazing", "awesome"]):
        return "Happy 😊"
    elif any(word in text for word in ["sad", "depressed", "unhappy", "cry"]):
        return "Sad 😢"
    elif any(word in text for word in ["angry", "hate", "worst", "annoyed"]):
        return "Angry 😡"
    elif any(word in text for word in ["excited", "thrilled", "fantastic"]):
        return "Excited 🤩"
    else:
        return "Not Detected"

print("===== Advanced Sentiment Analyzer =====")
print("Type 'exit' to stop\n")

while True:
    user_input = input("Enter your sentence: ")
    
    if user_input.lower() == "exit":
        print("Program Ended.")
        break

    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

    # Sentiment classification
    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😡"
    else:
        sentiment = "Neutral 😐"

    confidence = round(abs(polarity) * 100, 2)

    emotion = detect_emotion(user_input)

    print("\n----- Result -----")
    print("Sentiment :", sentiment)
    print("Confidence:", confidence, "%")
    print("Emotion   :", emotion)
    print("------------------\n")
