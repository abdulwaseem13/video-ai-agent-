import os
from dotenv import load_dotenv
from groq import Groq
from app.status import Status

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama-3.3-70b-versatile"
)


def ask_ai(objects, prompt, history, scene_description):

    object_list = []

    for obj in objects:

        object_list.append(
            f"- {obj['name']} "
            f"(ID={obj.get('id', 'N/A')}, "
            f"Confidence={obj['confidence']:.2f}, "
            f"Position=({obj['center_x']}, {obj['center_y']}))"
        )

    object_text = "\n".join(object_list)

    system_prompt = f"""
You are an Advanced AI Desktop Assistant.

You can understand:

- Conversation History
- OCR Text
- Vision Description
- YOLO Detected Objects
- User Questions

Rules:

1. Use conversation history whenever useful.
2. Use OCR text if available.
3. Use vision description if available.
4. Use detected objects when relevant.
5. Never hallucinate.
6. If information is unavailable, clearly say so.
7. Give concise but helpful answers.

Current Scene Description:

{scene_description}

Detected Objects:

{object_text}
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    Status.update("Thinking...")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.3,
    )

    status.done()

    return response.choices[0].message.content

def ask_from_prompt(prompt, history):

    messages = [

        {
            "role": "system",
            "content":
            "You are an intelligent Desktop AI Assistant."
        }

    ]

    messages.extend(history)

    messages.append({

        "role": "user",

        "content": prompt

    })

    response = client.chat.completions.create(

        model=MODEL_NAME,

        messages=messages,

        temperature=0.3

    )

    return response.choices[0].message.content