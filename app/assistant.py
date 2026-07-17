import cv2

from llm import ask_ai
from router import requires_vision

from memory import ConversationMemory
from scene_memory import SceneMemory
from scene_graph import SceneGraph
from event_manager import EventManager
from person_memory import PersonMemory

# New Modules
from context.builder import ContextBuilder
from context.prompt_builder import PromptBuilder
from ocr.reader import OCRReader

# Temporary (Gemini -> OpenRouter later)
from vision.provider import VisionProvider


class Assistant:

    def __init__(self):

        self.objects = []
        self.camera = None

        self.memory = ConversationMemory()
        self.scene_memory = SceneMemory()
        self.scene_graph = SceneGraph()
        self.event_manager = EventManager()
        self.person_memory = PersonMemory()
        self.vision = VisionProvider()

        # New
        self.context_builder = ContextBuilder()
        self.prompt_builder = PromptBuilder()
        self.ocr = OCRReader()

    def set_camera(self, camera):
        self.camera = camera

    def update_objects(self, objects):
        self.objects = objects
        self.scene_graph.update(objects)
        self.event_manager.update(objects)
        self.person_memory.update(objects)

    def ask(self, question):

        self.memory.add("user", question)

        if self.camera is None:
            answer = "Camera is not connected."

            self.memory.add("assistant", answer)
            return answer

        frame = self.camera.get_latest_frame()

        if frame is None:
            answer = "No frame available."

            self.memory.add("assistant", answer)
            return answer

        # -----------------------------
        # OCR
        # -----------------------------
        ocr_text = self.ocr.read(frame)

        # -----------------------------
        # Vision
        # -----------------------------
        scene_description = ""

        if requires_vision(question):

            try:
                scene_description = self.vision.analyze(
                    frame,
                    question
                )
            except Exception as e:
                print(e)

        # -----------------------------
        # Context
        # -----------------------------
        context = self.context_builder.build(
            question=question,
            objects=self.objects,
            ocr_text=ocr_text,
            scene_description=scene_description,
            history=self.memory.get_history()
        )

        prompt = self.prompt_builder.build(context)

        # -----------------------------
        # LLM
        # -----------------------------
        answer = ask_ai(
            self.objects,
            prompt,
            self.memory.get_history(),
            self.scene_memory.get_description()
        )

        self.scene_memory.update(
            scene_description,
            self.objects
        )

        self.memory.add("assistant", answer)

        return answer