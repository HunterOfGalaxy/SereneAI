from textblob import TextBlob

def analyze_mood(text):
    """
    Analyze the mood of the user based on their input.
    """
    try:
        # Get sentiment polarity
        sentiment = TextBlob(text).sentiment.polarity
        
        # Classify mood
        if sentiment > 0.2:
            return "😄 Happy"
        elif sentiment < -0.2:
            return "😔 Sad"
        else:
            return "😐 Neutral"
    except Exception as e:
        return f"Error analyzing mood: {str(e)}"