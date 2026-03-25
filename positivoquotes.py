from repository import get_random_quote

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
}


def format_quote(quote_dict):
    """Format a quote dict into a readable string."""
    return f'"{quote_dict["quote"]}" — {quote_dict["author"]}'


def run():
    """Main loop: ask for mood, display encouragement + random quote."""
    while True:
        mood = input(
            "How are you feeling today (happy, sad, mad, angry, frustrated) or 'quit': "
        ).strip().lower()

        if mood == "quit":
            print("Goodbye! Stay positive!")
            break

        if mood not in MOOD_RESPONSES:
            print("Sorry, I don't recognize that mood. Please try again.")
            continue

        entry = MOOD_RESPONSES[mood]
        quote = get_random_quote()

        print(f"\n{entry['message']}")
        print(entry["encouragement"])
        print(format_quote(quote))
        print()


if __name__ == "__main__":
    run()
