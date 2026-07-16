class SceneMemory:

    def __init__(self):
        self.description = ""
        self.last_objects = []

    def update(self, description, objects):
        self.description = description
        self.last_objects = objects

    def get_description(self):
        return self.description

    def get_objects(self):
        return self.last_objects

    def clear(self):
        self.description = ""
        self.last_objects = []