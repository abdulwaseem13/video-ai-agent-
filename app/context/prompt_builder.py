class PromptBuilder:

    def build(self, context):

        prompt = f"""
You are an intelligent AI assistant.

Current Scene
-------------
{context['scene_description']}

Detected Objects
----------------
{context['objects']}

Visible Text
------------
{context['ocr_text']}

Conversation History
--------------------
{context['history']}

User Question
-------------
{context['question']}

Answer naturally.
"""

        return prompt