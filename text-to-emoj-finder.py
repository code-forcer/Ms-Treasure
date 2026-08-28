#Emoji to text convert or text to emoji converter
#Collections
emoji_box = {
    "angry":"😠",    "happy":"😊",
    "sad":"😔",    "love":"❤️",
    "smile":"😊",    "cry":"😭",
    "laugh":"😂",    "think":"🤔",
    "wink":"😉",    "kiss":"😘",
    "heart":"❤️",    "star":"⭐",
    "sparkles":"✨",    "clap":"👏",
    "thumbs up":"👍",    "thumbs down":"👎",
    "wave":"👋",    "hello":"👋",
    "bye":"👋",    "yes":"✅",
    "no":"❌",    "maybe":"🤔",
    "okay":"👌",    "fire":"🔥",
    "water":"💧",    "earth":"🌍",
    "air":"💨",    "sun":"☀️",
    "moon":"🌙",    "star":"⭐",
    "cloud":"☁️",    "rain":"🌧️",
    "storm":"🌩️",    "snow":"❄️",
    "wind":"🌬️",    "fire":"🔥",
    "water":"💧",    "earth":"🌍",
    "air":"💨",    "sun":"☀️",
    "moon":"🌙",    "star":"⭐",
    "cloud":"☁️",    "rain":"🌧️",
    "storm":"🌩️",    "snow":"❄️",
    "wind":"🌬️",    "fire":"🔥",
    "water":"💧",    "earth":"🌍",
    "air":"💨",    "sun":"☀️",
    "moon":"🌙",    "star":"⭐",
    "cloud":"☁️",    "rain":"🌧️",
    "storm":"🌩️",    "snow":"❄️",
    "wind":"🌬️",}
#create a function call intent
def emoji(text):
    return emoji_box[text.lower()]
print(emoji(input("Enter the emoji: ")))
