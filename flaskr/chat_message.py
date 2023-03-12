class ChatMessage:
    def __init__(self, r, c):
        self.role = r
        self.content = c

    def to_message(self):
        if self.role and self.content:
            return (
                """ "role": "{role}", "content": "{content}" """.format(
                    role=self.role, content=self.content
                ))
        else:
            raise ValueError("role and content cannot be empty or None")


class UserMessage(ChatMessage):
    def __init__(self, c):
        self.role = "user"
        self.content = c


class SystemMessage(ChatMessage):
    def __init__(self, c):
        self.role = "system"
        self.content = c


class BehaviourMessage(ChatMessage):
    def __init__(self, c):
        self.role = "assistant"
        self.content = c
