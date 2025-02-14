import requests
import random

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
HEADERS = {"Authorization": "Bearer hf_"} # Replace hf_ with your Hugging Face API key

MOOD_ACTIONS = {
    "😔 Sad": "Offer comforting words and suggest an activity like journaling or a calming exercise.",
    "😄 Happy": "Encourage them to reflect on positive moments or share their joy.",
    "😐 Neutral": "Provide general mental wellness tips, such as mindfulness or gratitude exercises."
}

def get_chatbot_response(user_input, mood, chat_history):
    """Generate responses based on user input, mood, and conversation history."""
    try:
        # Build context from the last 3 exchanges
        history_text = "\n".join(
            [f"User: {chat['You']}\nSerene: {chat['Serene']}" for chat in chat_history[-3:]]
        )
        
        prompt = (
            f"You are Serene, a mental wellness assistant. The user feels {mood.lower()}.\n"
            f"User: {user_input}\n"
            f"Serene: (Provide a unique, non-repetitive, empathetic response)"
        )
            
        response = requests.post(API_URL, json={"inputs": prompt}, headers=HEADERS).json()

        if isinstance(response, dict) and 'error' in response:
            print(f"API Error: {response['error']}")
            return varied_fallback_response(mood)

        # Ensure response parsing is correct
        try:
            reply = response[0]['generated_text'].strip() if isinstance(response, list) else response.get('generated_text', '').strip()
        except Exception as e:
            print("Response Parsing Error:", e)
            return varied_fallback_response(mood)

        if not reply or len(reply) < 5:
            return varied_fallback_response(mood)

        return reply

    
    except Exception as e:
        print("Error:", e)
        return varied_fallback_response(mood)

def varied_fallback_response(mood):
    """Provide varied fallback responses based on mood."""
    fallback_responses = {
        "😔 Sad": [
            "I'm here for you. Have you tried writing down your thoughts?",
            "It's okay to feel this way. Would you like to listen to some calming music?",
            "You're not alone. Maybe a short walk could help clear your mind?"
        ],
        "😄 Happy": [
            "That's great! What's making you feel this way?",
            "I'm glad you're feeling positive. Would you like to share more?",
            "Keep enjoying the good vibes! Any recent win you'd like to celebrate?"
        ],
        "😐 Neutral": [
            "Let's try a quick mindfulness exercise. Close your eyes and take 3 deep breaths.",
            "Maybe think about one thing you're grateful for today.",
            "How about a small break to relax your mind for a moment?"
        ]
    }
    return random.choice(fallback_responses.get(mood, fallback_responses["😐 Neutral"]))
