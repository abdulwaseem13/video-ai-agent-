class PersonMemory:

    def __init__(self):
        self.people = {}

    def update(self, objects):

        for obj in objects:

            if obj["name"] != "person":
                continue

            pid = obj["id"]

            if pid not in self.people:

                self.people[pid] = {
                    "id": pid,
                    "first_seen": True,
                    "description": "",
                    "last_position": (
                        obj["center_x"],
                        obj["center_y"]
                    )
                }

            self.people[pid]["last_position"] = (
                obj["center_x"],
                obj["center_y"]
            )

    def get_people(self):
        return self.people