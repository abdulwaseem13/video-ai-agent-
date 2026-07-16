class EventManager:

    def __init__(self):
        self.previous = {}
        self.events = []

    def update(self, objects):

        current = {}

        for obj in objects:
            current[obj["id"]] = obj

        # New objects
        for obj_id in current:
            if obj_id not in self.previous:
                self.events.append(
                    f"{current[obj_id]['name']} #{obj_id} appeared."
                )

        # Disappeared objects
        for obj_id in self.previous:
            if obj_id not in current:
                self.events.append(
                    f"{self.previous[obj_id]['name']} #{obj_id} disappeared."
                )

        self.previous = current

    def get_events(self):
        events = self.events[:]
        self.events.clear()
        return events