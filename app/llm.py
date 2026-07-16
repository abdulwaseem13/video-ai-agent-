import os
from dotenv import load_dotenv
from groq import Groq

# Load .env variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")


def ask_ai(objects, question, history, scene_description):

    scene = ""

    for obj in objects:
        scene += (
            f"- {obj['name']} "
            f"(ID={obj.get('id', 'N/A')}, "
            f"confidence={obj['confidence']}, "
            f"position=({obj['center_x']}, {obj['center_y']}))\n"
        )

    messages = [
        {
            "role": "system",
            "content": """
You are an intelligent AI Vision Assistant.

You have four sources of information:

1. Conversation history.
2. Current scene description.
3. Current detected objects.
4. The user's latest question.

Always use the conversation history to answer follow-up questions.

Never say "I haven't described anything yet" if the answer exists in the conversation history.

If something cannot be determined from the image, say so honestly.

Do not invent information.
"""
        }
    ]

    # Add previous conversation
    messages.extend(history)

    # Add the current user question
    messages.append({
        "role": "user",
        "content": f"""
Current Scene Description:

{scene_description}

Detected Objects:

{scene}

Question:

{question}
"""
    })

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.3
    )

    return response.choices[0].message.content