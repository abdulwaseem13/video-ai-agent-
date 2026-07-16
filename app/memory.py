class ConversationMemory:

    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append({
            "role": role,
            "content": message
        })

        # Keep only the last 20 messages
        self.history = self.history[-20:]

    def get_history(self):
        return self.history

    def clear(self):
        self.history = []