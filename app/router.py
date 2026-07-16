VISION_KEYWORDS = [
    "color",
    "colour",
    "shirt",
    "dress",
    "wearing",
    "pant",
    "pants",
    "shoe",
    "shoes",
    "cap",
    "hat",
    "face",
    "smile",
    "frown",
    "hand",
    "hair",
    "holding",
    "read",
    "text",
    "screen",
    "monitor",
    "describe",
    "look like",
    "appearance",
    "doing",
    "activity"
]


def requires_vision(question):
    question = question.lower()

    return any(word in question for word in VISION_KEYWORDS)
