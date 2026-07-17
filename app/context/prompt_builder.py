class PromptBuilder:

    def build(self, context):

        objects = ""

        for obj in context["objects"]:

            objects += (
                f"- {obj['name']} "
                f"(ID={obj.get('id','?')}, "
                f"Confidence={obj['confidence']}, "
                f"Position=({obj['center_x']},{obj['center_y']}))\n"
            )

        events = "\n".join(context["events"])

        people = ""

        for pid, person in context["persons"].items():

            people += (
                f"Person {pid} "
                f"Last Position: {person['last_position']}\n"
            )

        prompt = f"""
You are an intelligent Desktop AI Assistant.

Answer naturally.

Never invent information.

If something is unknown, clearly say you cannot determine it.

------------------------------------------------

Current Scene

{context["scene"]}

------------------------------------------------

Vision Analysis

{context["vision"]}

------------------------------------------------

OCR

{context["ocr"]}

------------------------------------------------

Detected Objects

{objects}

------------------------------------------------

Recent Events

{events}

------------------------------------------------

Known Persons

{people}

------------------------------------------------

User Question

{context["question"]}
"""

        return prompt