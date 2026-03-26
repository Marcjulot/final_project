import Foundation

struct Quote {
    let text: String
    let author: String
}

enum Mood: String, CaseIterable, Identifiable {
    case angry
    case anxious
    case frustrated
    case grateful
    case happy
    case hopeful
    case lonely
    case mad
    case motivated
    case sad
    case stressed
    case tired

    var id: String { rawValue }

    var displayName: String { rawValue.capitalized }

    var emoji: String {
        switch self {
        case .happy: return "😊"
        case .sad: return "😢"
        case .mad: return "😤"
        case .angry: return "😡"
        case .frustrated: return "😩"
        case .anxious: return "😰"
        case .stressed: return "😫"
        case .lonely: return "🥺"
        case .tired: return "😴"
        case .hopeful: return "🌟"
        case .grateful: return "🙏"
        case .motivated: return "💪"
        }
    }

    var message: String {
        switch self {
        case .happy:
            return "I am glad that you are happy! Lets keep the party going with a positive quote."
        case .sad:
            return "I am sorry you are feeling that way. Hope this quote cheers you up!"
        case .mad:
            return "I am sorry that you are feeling mad, I hope this quote can lighten your mood!"
        case .angry:
            return "I am sorry you are feeling angry, maybe this quote will get you in a better mood."
        case .frustrated:
            return "I am sorry you are feeling frustrated. Please read this quote to help."
        case .anxious:
            return "I understand feeling anxious can be overwhelming. Here's something to help."
        case .stressed:
            return "Stress can feel heavy, but you are stronger than you think."
        case .lonely:
            return "Feeling lonely is tough, but you are never truly alone."
        case .tired:
            return "It's okay to feel tired. Rest is not a sign of weakness."
        case .hopeful:
            return "Hope is a beautiful thing! Let's fuel that feeling."
        case .grateful:
            return "Gratitude is a superpower! Here's a quote to match your vibe."
        case .motivated:
            return "Love that energy! Let's channel it with a powerful quote."
        }
    }

    var encouragement: String {
        switch self {
        case .happy:
            return "Keep smiling!"
        case .sad:
            return "To be truly happy, you must practice smiling. Go ahead and smile."
        case .mad:
            return "Take a deep breath — this feeling will pass."
        case .angry:
            return "You got this, anger fades!"
        case .frustrated:
            return "It only means that you are having a hard time right now. Tomorrow it will be better."
        case .anxious:
            return "Breathe in, breathe out. You are safe right now."
        case .stressed:
            return "Take a moment to pause — you deserve a break."
        case .lonely:
            return "Reach out to someone you trust — connection heals."
        case .tired:
            return "Be gentle with yourself — recharge and come back stronger."
        case .hopeful:
            return "Keep that spark alive — great things are ahead."
        case .grateful:
            return "A grateful heart attracts more blessings."
        case .motivated:
            return "You're unstoppable — keep pushing forward!"
        }
    }

    var quotes: [Quote] {
        switch self {
        case .happy:
            return [
                Quote(text: "Happiness is not something ready made. It comes from your own actions.", author: "Dalai Lama"),
                Quote(text: "The most wasted of days is one without laughter.", author: "E.E. Cummings"),
                Quote(text: "Happiness depends upon ourselves.", author: "Aristotle"),
                Quote(text: "The purpose of our lives is to be happy.", author: "Dalai Lama"),
                Quote(text: "Joy is not in things; it is in us.", author: "Richard Wagner"),
                Quote(text: "Be happy for this moment. This moment is your life.", author: "Omar Khayyam"),
                Quote(text: "The happiness of your life depends upon the quality of your thoughts.", author: "Marcus Aurelius"),
            ]
        case .sad:
            return [
                Quote(text: "Even the darkest night will end and the sun will rise.", author: "Victor Hugo"),
                Quote(text: "The wound is the place where the Light enters you.", author: "Rumi"),
                Quote(text: "Tears are words that need to be written.", author: "Paulo Coelho"),
                Quote(text: "Every moment is a fresh beginning.", author: "T.S. Eliot"),
                Quote(text: "You are allowed to feel messed up and inside out. It doesn't mean you're defective — it just means you're human.", author: "David Mitchell"),
                Quote(text: "The only way out is through.", author: "Robert Frost"),
                Quote(text: "Stars can't shine without darkness.", author: "D.H. Sidebottom"),
            ]
        case .mad:
            return [
                Quote(text: "For every minute you remain angry, you give up sixty seconds of peace of mind.", author: "Ralph Waldo Emerson"),
                Quote(text: "Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned.", author: "Buddha"),
                Quote(text: "Speak when you are angry and you will make the best speech you will ever regret.", author: "Ambrose Bierce"),
                Quote(text: "The best fighter is never angry.", author: "Lao Tzu"),
                Quote(text: "Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured.", author: "Mark Twain"),
                Quote(text: "When anger rises, think of the consequences.", author: "Confucius"),
            ]
        case .angry:
            return [
                Quote(text: "You will not be punished for your anger, you will be punished by your anger.", author: "Buddha"),
                Quote(text: "Anger, if not restrained, is frequently more hurtful to us than the injury that provokes it.", author: "Seneca"),
                Quote(text: "The greatest remedy for anger is delay.", author: "Thomas Paine"),
                Quote(text: "How much more grievous are the consequences of anger than the causes of it.", author: "Marcus Aurelius"),
                Quote(text: "Anybody can become angry — that is easy, but to be angry with the right person and to the right degree and at the right time and for the right purpose, and in the right way — that is not within everybody's power and is not easy.", author: "Aristotle"),
                Quote(text: "Do not let your anger lead to hatred, as you will hurt yourself more than you would the other.", author: "Stephen Richards"),
            ]
        case .frustrated:
            return [
                Quote(text: "Our greatest glory is not in never falling, but in rising every time we fall.", author: "Confucius"),
                Quote(text: "Patience is not the ability to wait, but the ability to keep a good attitude while waiting.", author: "Joyce Meyer"),
                Quote(text: "The gem cannot be polished without friction, nor man perfected without trials.", author: "Chinese Proverb"),
                Quote(text: "Frustration, although quite painful at times, is a very positive and essential part of success.", author: "Bo Bennett"),
                Quote(text: "It does not matter how slowly you go as long as you do not stop.", author: "Confucius"),
                Quote(text: "A river cuts through rock, not because of its power, but because of its persistence.", author: "Jim Watkins"),
                Quote(text: "The only impossible journey is the one you never begin.", author: "Tony Robbins"),
            ]
        case .anxious:
            return [
                Quote(text: "Nothing diminishes anxiety faster than action.", author: "Walter Anderson"),
                Quote(text: "You don't have to control your thoughts. You just have to stop letting them control you.", author: "Dan Millman"),
                Quote(text: "Anxiety does not empty tomorrow of its sorrows, but only empties today of its strength.", author: "Charles Spurgeon"),
                Quote(text: "The way to develop self-confidence is to do the thing you fear and get a record of successful experiences behind you.", author: "William Jennings Bryan"),
                Quote(text: "Life is ten percent what you experience and ninety percent how you respond to it.", author: "Dorothy M. Neddermeyer"),
                Quote(text: "Present fears are less than horrible imaginings.", author: "William Shakespeare"),
                Quote(text: "You wouldn't worry so much about what others think of you if you realized how seldom they do.", author: "Eleanor Roosevelt"),
            ]
        case .stressed:
            return [
                Quote(text: "The greatest weapon against stress is our ability to choose one thought over another.", author: "William James"),
                Quote(text: "It's not the load that breaks you down, it's the way you carry it.", author: "Lou Holtz"),
                Quote(text: "Almost everything will work again if you unplug it for a few minutes, including you.", author: "Anne Lamott"),
                Quote(text: "The time to relax is when you don't have time for it.", author: "Sydney J. Harris"),
                Quote(text: "In times of stress, the best thing we can do is take a deep breath.", author: "Thich Nhat Hanh"),
                Quote(text: "Tension is who you think you should be. Relaxation is who you are.", author: "Chinese Proverb"),
                Quote(text: "Stress is caused by being here but wanting to be there.", author: "Eckhart Tolle"),
            ]
        case .lonely:
            return [
                Quote(text: "The soul that sees beauty may sometimes walk alone.", author: "Johann Wolfgang von Goethe"),
                Quote(text: "Loneliness adds beauty to life. It puts a special burn on sunsets and makes night air smell better.", author: "Henry Rollins"),
                Quote(text: "The eternal quest of the human being is to shatter his loneliness.", author: "Norman Cousins"),
                Quote(text: "You cannot be lonely if you like the person you're alone with.", author: "Wayne Dyer"),
                Quote(text: "Music was my refuge. I could crawl into the space between the notes and curl my back to loneliness.", author: "Maya Angelou"),
                Quote(text: "Being alone has a power that very few people can handle.", author: "Steven Aitchison"),
                Quote(text: "Loneliness is not lack of company, loneliness is lack of purpose.", author: "Guillermo Maldonado"),
            ]
        case .tired:
            return [
                Quote(text: "Rest when you're weary. Refresh and renew yourself, your body, your mind, your spirit. Then get back to work.", author: "Ralph Marston"),
                Quote(text: "Almost everything will work again if you unplug it for a few minutes, including you.", author: "Anne Lamott"),
                Quote(text: "Take rest; a field that has rested gives a bountiful crop.", author: "Ovid"),
                Quote(text: "It's not the mountain we conquer but ourselves.", author: "Edmund Hillary"),
                Quote(text: "Sometimes the most productive thing you can do is relax.", author: "Mark Black"),
                Quote(text: "Perseverance is not a long race; it is many short races one after the other.", author: "Walter Elliot"),
                Quote(text: "You are never too old to set another goal or to dream a new dream.", author: "C.S. Lewis"),
            ]
        case .hopeful:
            return [
                Quote(text: "Hope is being able to see that there is light despite all of the darkness.", author: "Desmond Tutu"),
                Quote(text: "Once you choose hope, anything's possible.", author: "Christopher Reeve"),
                Quote(text: "Learn from yesterday, live for today, hope for tomorrow.", author: "Albert Einstein"),
                Quote(text: "Hope is a waking dream.", author: "Aristotle"),
                Quote(text: "Where there is no vision, there is no hope.", author: "George Washington Carver"),
                Quote(text: "Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence.", author: "Helen Keller"),
                Quote(text: "Hope is the thing with feathers that perches in the soul.", author: "Emily Dickinson"),
            ]
        case .grateful:
            return [
                Quote(text: "Gratitude turns what we have into enough.", author: "Aesop"),
                Quote(text: "Enjoy the little things, for one day you may look back and realize they were the big things.", author: "Robert Brault"),
                Quote(text: "Gratitude is not only the greatest of virtues, but the parent of all the others.", author: "Cicero"),
                Quote(text: "When I started counting my blessings, my whole life turned around.", author: "Willie Nelson"),
                Quote(text: "Gratitude makes sense of our past, brings peace for today, and creates a vision for tomorrow.", author: "Melody Beattie"),
                Quote(text: "The more grateful I am, the more beauty I see.", author: "Mary Davis"),
                Quote(text: "Gratitude is the healthiest of all human emotions.", author: "Zig Ziglar"),
            ]
        case .motivated:
            return [
                Quote(text: "The secret of getting ahead is getting started.", author: "Mark Twain"),
                Quote(text: "It always seems impossible until it's done.", author: "Nelson Mandela"),
                Quote(text: "Don't watch the clock; do what it does. Keep going.", author: "Sam Levenson"),
                Quote(text: "The future belongs to those who believe in the beauty of their dreams.", author: "Eleanor Roosevelt"),
                Quote(text: "Success is not final, failure is not fatal: it is the courage to continue that counts.", author: "Winston Churchill"),
                Quote(text: "Believe you can and you're halfway there.", author: "Theodore Roosevelt"),
                Quote(text: "Act as if what you do makes a difference. It does.", author: "William James"),
            ]
        }
    }

    func randomQuote() -> Quote {
        quotes.randomElement()!
    }
}
