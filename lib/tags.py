class Tags:
    def __init__(self, id, name, posts = None ):
        self.id = id
        self.name = name
        self.posts = posts or []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Tags({self.id}, {self.name})"