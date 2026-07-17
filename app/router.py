

INTENTS = {

    "vision": [

        # General
        "see", "look", "watch", "view", "observe",
        "inspect", "analyze", "analyse",
        "describe", "explain", "summarize", "summarise",
        "identify", "recognize", "recognise",

        # Scene
        "scene", "environment", "surroundings",
        "room", "workspace", "desk",
        "screen", "display", "monitor",
        "window", "camera", "webcam",
        "image", "picture", "photo", "frame",

        # Questions
        "what do you see",
        "what can you see",
        "what is visible",
        "what's on my screen",
        "what is on my screen",
        "what's happening",
        "what is happening",

        # Position
        "left", "right", "top", "bottom",
        "middle", "center", "centre",
        "above", "below",
        "behind", "beside",
        "next to", "near", "far",

        # Appearance
        "color", "colour",
        "shape", "size",
        "appearance",
        "background",
        "foreground",
        "wearing",
        "holding"
    ],

    "ocr": [

        # Reading
        "read",
        "extract",
        "ocr",
        "text recognition",

        # Text
        "text",
        "written",
        "writing",
        "word",
        "words",
        "sentence",
        "paragraph",
        "character",
        "letter",
        "number",
        "digit",

        # Documents
        "document",
        "pdf",
        "page",
        "article",
        "email",
        "mail",
        "message",
        "chat",

        # Programming
        "code",
        "script",
        "terminal",
        "console",
        "command",
        "logs",
        "log",

        # Errors
        "error",
        "warning",
        "exception",
        "traceback",
        "stack trace",
        "compile",
        "compiler",
        "syntax",

        # UI
        "button text",
        "label",
        "menu",
        "heading",
        "caption",
        "title",

        # Questions
        "what does this say",
        "what is written",
        "read the screen",
        "read this",
        "copy text",
        "extract text",
        "transcribe",
        "translate"
    ],

    "object": [

        # General
        "object",
        "objects",
        "item",
        "items",
        "thing",
        "things",

        # Humans
        "person",
        "people",
        "man",
        "woman",
        "boy",
        "girl",
        "human",
        "face",

        # Electronics
        "laptop",
        "computer",
        "pc",
        "monitor",
        "keyboard",
        "mouse",
        "phone",
        "mobile",
        "tablet",
        "tv",
        "television",

        # Office
        "chair",
        "table",
        "book",
        "notebook",
        "pen",
        "paper",
        "bag",
        "backpack",
        "cup",
        "glass",
        "bottle",

        # Furniture
        "door",
        "window",

        # Questions
        "is there",
        "do you see",
        "how many",
        "count",
        "locate",
        "where is",
        "find",
        "detect",
        "show me"
    ],

    "memory": [

        "remember",
        "recall",
        "earlier",
        "before",
        "previous",
        "history",
        "conversation",
        "last time",
        "what did you say",
        "what did i ask",
        "what were we discussing"
    ],

    "rag": [

        "search document",
        "search file",
        "knowledge base",
        "documentation",
        "manual",
        "guide",
        "report",
        "policy",
        "pdf",
        "excel",
        "spreadsheet",
        "word",
        "docx",
        "ppt",
        "presentation",
        "wiki",
        "summarize document"
    ],

    "database": [

        "database",
        "db",
        "sql",

        "employee",
        "attendance",
        "leave",
        "calendar",
        "meeting",
        "task",
        "project",
        "customer",
        "client",
        "record",

        "search employee",
        "find employee",
        "employee id",
        "attendance report"
    ],

    "function": [

        "open",
        "close",
        "create",
        "delete",
        "update",
        "edit",
        "add",
        "remove",
        "insert",
        "download",
        "upload",
        "generate",
        "send",
        "export",
        "import"
    ],

    "chat": [

        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
        "thanks",
        "thank you",
        "how are you",
        "who are you",
        "help"
    ]
}


def route(question: str) -> list[str]:
    """
    Returns a list of matching intents.

    Example:
    --------
    route("Read the error on my screen")
    -> ["vision", "ocr"]

    route("How many people are there?")
    -> ["object"]

    route("Search employee 101")
    -> ["database"]
    """

    question = question.lower().strip()

    matched = []

    for intent, keywords in INTENTS.items():

        for keyword in keywords:

            if keyword in question:

                matched.append(intent)
                break

    # Default
    if not matched:
        matched.append("chat")

    return matched


def has_intent(question: str, intent: str) -> bool:
    """
    Convenience helper.

    Example:
        if has_intent(question, "vision"):
            ...
    """

    return intent in route(question)


def print_intents(question: str):
    """
    Debug helper.
    """

    intents = route(question)

    print("=" * 50)
    print("Question :", question)
    print("Intents  :", intents)
    print("=" * 50)