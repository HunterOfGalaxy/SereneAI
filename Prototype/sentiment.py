from transformers import pipeline

# Load sentiment analysis model (can be optimized with a different checkpoint)
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_mood(text):
    """Analyze user mood based on sentiment analysis."""
    try:
        result = sentiment_pipeline(text)[0]
        label = result['label'].lower()  # Convert to lowercase for consistency
        score = result['score']

        if "positive" in label and score > 0.6:
            return "😄 Happy"
        elif "negative" in label and score > 0.6:
            return "😔 Sad"
        elif "fear" in label or "anxious" in text.lower():
            return "😰 Anxious"
        else:
            return "😐 Neutral"

    except Exception as e:
        print("Sentiment Analysis Error:", e)
        return "😐 Neutral"

