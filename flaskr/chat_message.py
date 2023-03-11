class ChatMessage:
    def __init__(self, r, c):
        self.role = r
        self.content = c

    def to_json(self):
        print(
            """{
              "role":{role}, 
              "content": {content}""".format(
                role=self.role, content=self.content
            )
        )
