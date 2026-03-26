"""Curated mood-specific quotes for the Positivo app."""

import random

MOOD_QUOTES = {
    "happy": [
        {"quote": "Happiness is not something ready made. It comes from your own actions.", "author": "Dalai Lama"},
        {"quote": "The most wasted of days is one without laughter.", "author": "E.E. Cummings"},
        {"quote": "Happiness depends upon ourselves.", "author": "Aristotle"},
        {"quote": "The purpose of our lives is to be happy.", "author": "Dalai Lama"},
        {"quote": "Joy is not in things; it is in us.", "author": "Richard Wagner"},
        {"quote": "Be happy for this moment. This moment is your life.", "author": "Omar Khayyam"},
        {"quote": "The happiness of your life depends upon the quality of your thoughts.", "author": "Marcus Aurelius"},
    ],
    "sad": [
        {"quote": "Even the darkest night will end and the sun will rise.", "author": "Victor Hugo"},
        {"quote": "The wound is the place where the Light enters you.", "author": "Rumi"},
        {"quote": "Tears are words that need to be written.", "author": "Paulo Coelho"},
        {"quote": "Every moment is a fresh beginning.", "author": "T.S. Eliot"},
        {"quote": "You are allowed to feel messed up and inside out. It doesn't mean you're defective — it just means you're human.", "author": "David Mitchell"},
        {"quote": "The only way out is through.", "author": "Robert Frost"},
        {"quote": "Stars can't shine without darkness.", "author": "D.H. Sidebottom"},
    ],
    "mad": [
        {"quote": "For every minute you remain angry, you give up sixty seconds of peace of mind.", "author": "Ralph Waldo Emerson"},
        {"quote": "Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned.", "author": "Buddha"},
        {"quote": "Speak when you are angry and you will make the best speech you will ever regret.", "author": "Ambrose Bierce"},
        {"quote": "The best fighter is never angry.", "author": "Lao Tzu"},
        {"quote": "Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured.", "author": "Mark Twain"},
        {"quote": "When anger rises, think of the consequences.", "author": "Confucius"},
    ],
    "angry": [
        {"quote": "You will not be punished for your anger, you will be punished by your anger.", "author": "Buddha"},
        {"quote": "Anger, if not restrained, is frequently more hurtful to us than the injury that provokes it.", "author": "Seneca"},
        {"quote": "The greatest remedy for anger is delay.", "author": "Thomas Paine"},
        {"quote": "How much more grievous are the consequences of anger than the causes of it.", "author": "Marcus Aurelius"},
        {"quote": "Anybody can become angry — that is easy, but to be angry with the right person and to the right degree and at the right time and for the right purpose, and in the right way — that is not within everybody's power and is not easy.", "author": "Aristotle"},
        {"quote": "Do not let your anger lead to hatred, as you will hurt yourself more than you would the other.", "author": "Stephen Richards"},
    ],
    "frustrated": [
        {"quote": "Our greatest glory is not in never falling, but in rising every time we fall.", "author": "Confucius"},
        {"quote": "Patience is not the ability to wait, but the ability to keep a good attitude while waiting.", "author": "Joyce Meyer"},
        {"quote": "The gem cannot be polished without friction, nor man perfected without trials.", "author": "Chinese Proverb"},
        {"quote": "Frustration, although quite painful at times, is a very positive and essential part of success.", "author": "Bo Bennett"},
        {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
        {"quote": "A river cuts through rock, not because of its power, but because of its persistence.", "author": "Jim Watkins"},
        {"quote": "The only impossible journey is the one you never begin.", "author": "Tony Robbins"},
    ],
    "anxious": [
        {"quote": "Nothing diminishes anxiety faster than action.", "author": "Walter Anderson"},
        {"quote": "You don't have to control your thoughts. You just have to stop letting them control you.", "author": "Dan Millman"},
        {"quote": "Anxiety does not empty tomorrow of its sorrows, but only empties today of its strength.", "author": "Charles Spurgeon"},
        {"quote": "The way to develop self-confidence is to do the thing you fear and get a record of successful experiences behind you.", "author": "William Jennings Bryan"},
        {"quote": "Life is ten percent what you experience and ninety percent how you respond to it.", "author": "Dorothy M. Neddermeyer"},
        {"quote": "Present fears are less than horrible imaginings.", "author": "William Shakespeare"},
        {"quote": "You wouldn't worry so much about what others think of you if you realized how seldom they do.", "author": "Eleanor Roosevelt"},
    ],
    "stressed": [
        {"quote": "The greatest weapon against stress is our ability to choose one thought over another.", "author": "William James"},
        {"quote": "It's not the load that breaks you down, it's the way you carry it.", "author": "Lou Holtz"},
        {"quote": "Almost everything will work again if you unplug it for a few minutes, including you.", "author": "Anne Lamott"},
        {"quote": "The time to relax is when you don't have time for it.", "author": "Sydney J. Harris"},
        {"quote": "In times of stress, the best thing we can do is take a deep breath.", "author": "Thich Nhat Hanh"},
        {"quote": "Tension is who you think you should be. Relaxation is who you are.", "author": "Chinese Proverb"},
        {"quote": "Stress is caused by being here but wanting to be there.", "author": "Eckhart Tolle"},
    ],
    "lonely": [
        {"quote": "The soul that sees beauty may sometimes walk alone.", "author": "Johann Wolfgang von Goethe"},
        {"quote": "Loneliness adds beauty to life. It puts a special burn on sunsets and makes night air smell better.", "author": "Henry Rollins"},
        {"quote": "The eternal quest of the human being is to shatter his loneliness.", "author": "Norman Cousins"},
        {"quote": "You cannot be lonely if you like the person you're alone with.", "author": "Wayne Dyer"},
        {"quote": "Music was my refuge. I could crawl into the space between the notes and curl my back to loneliness.", "author": "Maya Angelou"},
        {"quote": "Being alone has a power that very few people can handle.", "author": "Steven Aitchison"},
        {"quote": "Loneliness is not lack of company, loneliness is lack of purpose.", "author": "Guillermo Maldonado"},
    ],
    "tired": [
        {"quote": "Rest when you're weary. Refresh and renew yourself, your body, your mind, your spirit. Then get back to work.", "author": "Ralph Marston"},
        {"quote": "Almost everything will work again if you unplug it for a few minutes, including you.", "author": "Anne Lamott"},
        {"quote": "Take rest; a field that has rested gives a bountiful crop.", "author": "Ovid"},
        {"quote": "It's not the mountain we conquer but ourselves.", "author": "Edmund Hillary"},
        {"quote": "Sometimes the most productive thing you can do is relax.", "author": "Mark Black"},
        {"quote": "Perseverance is not a long race; it is many short races one after the other.", "author": "Walter Elliot"},
        {"quote": "You are never too old to set another goal or to dream a new dream.", "author": "C.S. Lewis"},
    ],
    "hopeful": [
        {"quote": "Hope is being able to see that there is light despite all of the darkness.", "author": "Desmond Tutu"},
        {"quote": "Once you choose hope, anything's possible.", "author": "Christopher Reeve"},
        {"quote": "Learn from yesterday, live for today, hope for tomorrow.", "author": "Albert Einstein"},
        {"quote": "Hope is a waking dream.", "author": "Aristotle"},
        {"quote": "Where there is no vision, there is no hope.", "author": "George Washington Carver"},
        {"quote": "Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence.", "author": "Helen Keller"},
        {"quote": "Hope is the thing with feathers that perches in the soul.", "author": "Emily Dickinson"},
    ],
    "grateful": [
        {"quote": "Gratitude turns what we have into enough.", "author": "Aesop"},
        {"quote": "Enjoy the little things, for one day you may look back and realize they were the big things.", "author": "Robert Brault"},
        {"quote": "Gratitude is not only the greatest of virtues, but the parent of all the others.", "author": "Cicero"},
        {"quote": "When I started counting my blessings, my whole life turned around.", "author": "Willie Nelson"},
        {"quote": "Gratitude makes sense of our past, brings peace for today, and creates a vision for tomorrow.", "author": "Melody Beattie"},
        {"quote": "The more grateful I am, the more beauty I see.", "author": "Mary Davis"},
        {"quote": "Gratitude is the healthiest of all human emotions.", "author": "Zig Ziglar"},
    ],
    "motivated": [
        {"quote": "The secret of getting ahead is getting started.", "author": "Mark Twain"},
        {"quote": "It always seems impossible until it's done.", "author": "Nelson Mandela"},
        {"quote": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
        {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
        {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
        {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
        {"quote": "Act as if what you do makes a difference. It does.", "author": "William James"},
    ],
}


def get_quote_for_mood(mood):
    """Return a random quote dict for the given mood, or None if mood not found."""
    quotes = MOOD_QUOTES.get(mood)
    if not quotes:
        return None
    return random.choice(quotes)
