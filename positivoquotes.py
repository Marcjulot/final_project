from quotes import get_quote_for_mood

MOOD_RESPONSES = {
    "happy": {
        "message": "I am glad that you are happy! Lets keep the party going with a positive quote.",
        "encouragement": "Keep smiling!",
    },
    "sad": {
        "message": "I am sorry you are feeling that way. Hope this quote cheers you up!",
        "encouragement": "To be truly happy, you must practice smiling. Go ahead and smile.",
    },
    "mad": {
        "message": "I am sorry that you are feeling mad, I hope this quote can lighten your mood!",
        "encouragement": "Take a deep breath — this feeling will pass.",
    },
    "angry": {
        "message": "I am sorry you are feeling angry, maybe this quote will get you in a better mood.",
        "encouragement": "You got this, anger fades!",
    },
    "frustrated": {
        "message": "I am sorry you are feeling frustrated. Please read this quote to help.",
        "encouragement": "It only means that you are having a hard time right now. Tomorrow it will be better.",
    },
    "anxious": {
        "message": "I understand feeling anxious can be overwhelming. Here's something to help.",
        "encouragement": "Breathe in, breathe out. You are safe right now.",
    },
    "stressed": {
        "message": "Stress can feel heavy, but you are stronger than you think.",
        "encouragement": "Take a moment to pause — you deserve a break.",
    },
    "lonely": {
        "message": "Feeling lonely is tough, but you are never truly alone.",
        "encouragement": "Reach out to someone you trust — connection heals.",
    },
    "tired": {
        "message": "It's okay to feel tired. Rest is not a sign of weakness.",
        "encouragement": "Be gentle with yourself — recharge and come back stronger.",
    },
    "hopeful": {
        "message": "Hope is a beautiful thing! Let's fuel that feeling.",
        "encouragement": "Keep that spark alive — great things are ahead.",
    },
    "grateful": {
        "message": "Gratitude is a superpower! Here's a quote to match your vibe.",
        "encouragement": "A grateful heart attracts more blessings.",
    },
    "motivated": {
        "message": "Love that energy! Let's channel it with a powerful quote.",
        "encouragement": "You're unstoppable — keep pushing forward!",
    },
}

ALL_MOODS = sorted(MOOD_RESPONSES.keys())


def format_quote(quote_dict):
    """Format a quote dict into a readable string."""
    return f'"{quote_dict["quote"]}" — {quote_dict["author"]}'


def run():
    """Main loop: ask for mood, display encouragement + mood-matched quote."""
    moods_line1 = ", ".join(ALL_MOODS[:6])
    moods_line2 = ", ".join(ALL_MOODS[6:])

    while True:
        print(f"Moods: {moods_line1},")
        print(f"       {moods_line2}")
        mood = input("How are you feeling today? (or 'quit'): ").strip().lower()

        if mood == "quit":
            print("Goodbye! Stay positive!")
            break

        if mood not in MOOD_RESPONSES:
            print("Sorry, I don't recognize that mood. Please try again.\n")
            continue

        entry = MOOD_RESPONSES[mood]
        quote = get_quote_for_mood(mood)

        print(f"\n{entry['message']}")
        print(entry["encouragement"])
        print(format_quote(quote))
        print()


if __name__ == "__main__":
    run()
