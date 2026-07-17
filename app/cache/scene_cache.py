import hashlib
import cv2


class SceneCache:

    def __init__(self):

        self.frame_hash = None
        self.description = ""

    def _get_hash(self, frame):

        small = cv2.resize(frame, (64, 64))

        gray = cv2.cvtColor(
            small,
            cv2.COLOR_BGR2GRAY
        )

        return hashlib.md5(
            gray.tobytes()
        ).hexdigest()

    def has_changed(self, frame):

        new_hash = self._get_hash(frame)

        if self.frame_hash != new_hash:

            self.frame_hash = new_hash

            return True

        return False

    def update(self, description):

        self.description = description

    def get(self):

        return self.description

    def clear(self):

        self.frame_hash = None
        self.description = ""