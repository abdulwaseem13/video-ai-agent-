from router import route


class ContextBuilder:

    def __init__(self, assistant):
        self.assistant = assistant

    def build(self, question):

        intents = route(question)

        context = {

            "question": question,

            "intents": intents,

            "objects": self.assistant.objects,

            "vision": "",

            "ocr": "",

            "scene": self.assistant.scene_memory.get_description(),

            "conversation": self.assistant.memory.get_history(),

            "events": self.assistant.event_manager.get_events(),

            "persons": self.assistant.person_memory.get_people()

        }

        frame = None

        if self.assistant.camera:

            frame = self.assistant.camera.get_latest_frame()

        # ---------------- Vision ----------------

        # ---------------- Vision ----------------

        if "vision" in intents and frame is not None:

            if self.assistant.scene_cache.has_changed(frame):

                context["vision"] = self.assistant.vision.analyze(
                    frame,
                    question
                )

                self.assistant.scene_cache.update(
                    context["vision"]
                )
                print("📸 Calling Gemini Vision...")

            else:

                context["vision"] = self.assistant.scene_cache.get()
                print("📸 Calling Gemini Vision...")

        # ---------------- OCR ----------------

        if "ocr" in intents and frame is not None:

            try:

                from ocr.reader import OCRReader

                reader = OCRReader()

                context["ocr"] = reader.read(frame)

            except Exception:

                context["ocr"] = ""

        return context