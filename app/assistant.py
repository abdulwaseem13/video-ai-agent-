from llm import ask_ai
from vision_ai import analyze_image
from router import requires_vision
from memory import ConversationMemory
from scene_memory import SceneMemory
from scene_graph import SceneGraph
from event_manager import EventManager
from person_memory import PersonMemory 

class Assistant:

    def __init__(self):
        self.objects = []
        self.camera = None

        self.memory = ConversationMemory()
        self.scene_memory = SceneMemory()
        self.scene_graph = SceneGraph()
        self.event_manager = EventManager()
        self.person_memory = PersonMemory()
        

    def set_camera(self, camera):
        self.camera = camera

    def update_objects(self, objects):
        self.objects = objects
        self.scene_graph.update(objects)
        self.event_manager.update(objects)
        self.person_memory.update(objects)

    def ask(self, question):

    # Save the user's question
        self.memory.add("user", question)

        # Vision questions
        if requires_vision(question):

            if self.camera is None:
                answer = "Camera is not connected."
            else:
                frame = self.camera.get_latest_frame()

                if frame is None:
                    answer = "No camera frame available."
                else:
                    answer = analyze_image(frame, question)

                    self.scene_memory.update(
                        answer,
                        self.objects
                    )

        else:

            # YOLO questions
            if not self.objects:
                answer = "I don't see any objects."
            else:
                answer = ask_ai(
                    self.objects,
                    question,
                    self.memory.get_history(),
                    self.scene_memory.get_description()
                )

        # Save the AI's answer
        self.memory.add("assistant", answer)

        return answer