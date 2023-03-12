class ChatMessage:
    def __init__(self, r, c):
        self.role = r
        self.content = c

    def to_message(self):
        if self.role is None or self.content is None:
            raise ValueError("role and content cannot be None")
        else:
            return (
                """ "role": "{role}", "content": "{content}" """.format(
                    role=self.role, content=self.content
                ))
