import pandas as pd
import matplotlib.pyplot as plt

# Initialize mood history
mood_history = []

def add_mood(mood):
    """
    Add a mood entry to the history.
    """
    mood_history.append(mood)

def get_mood_history():
    """
    Return the mood history as a DataFrame.
    """
    return pd.DataFrame(mood_history, columns=["Mood"])

def plot_mood_history():
    """
    Plot the mood history.
    """
    df = get_mood_history()
    df["Mood"].value_counts().plot(kind="bar", color=["green", "blue", "red"])
    plt.title("Mood History")
    plt.xlabel("Mood")
    plt.ylabel("Count")
    return plt