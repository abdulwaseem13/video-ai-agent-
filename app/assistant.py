from app.llm import ask_from_prompt
from app.memory import ConversationMemory
from app.scene_memory import SceneMemory
from app.scene_graph import SceneGraph
from app.event_manager import EventManager
from app.person_memory import PersonMemory

from app.vision.provider import VisionProvider
from app.context.builder import ContextBuilder
from app.context.prompt_builder import PromptBuilder
from app.cache.scene_cache import SceneCache

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

        self.context_builder = ContextBuilder(self)
        self.prompt_builder = PromptBuilder()
        self.scene_cache = SceneCache()

    def set_camera(self, camera):
        self.camera = camera

    def update_objects(self, objects):

        self.objects = objects

        self.scene_graph.update(objects)
        self.event_manager.update(objects)
        self.person_memory.update(objects)

    def ask(self, question):

        # Store user message
        self.memory.add("user", question)

        # Build context
        context = self.context_builder.build(question)

        # Update scene memory if Vision was used
        if context["vision"]:
            self.scene_memory.update(
                context["vision"],
                self.objects
            )

        # Build prompt
        prompt = self.prompt_builder.build(context)

        # Ask Groq
        answer = ask_from_prompt(
            prompt,
            self.memory.get_history()
        )

        # Save AI response
        self.memory.add(
            "assistant",
            answer
        )

        return answer