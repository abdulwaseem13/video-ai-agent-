import math


class SceneGraph:

    def __init__(self):
        self.graph = {}

    def update(self, objects):
        self.graph = {}

        for obj in objects:
            obj_id = obj["id"]

            self.graph[obj_id] = {
                "id": obj_id,
                "name": obj["name"],
                "center": (
                    obj["center_x"],
                    obj["center_y"]
                ),
                "near": []
            }

        ids = list(self.graph.keys())

        # Find nearby objects
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):

                a = self.graph[ids[i]]
                b = self.graph[ids[j]]

                d = math.dist(a["center"], b["center"])

                if d < 200:
                    a["near"].append(b["id"])
                    b["near"].append(a["id"])

    def get(self):
        return self.graph