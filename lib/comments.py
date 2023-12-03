class Comments:
    def __init__(self, id, author_name, post_id):
        self.id = id
        self.author_name = author_name
        self.post_id = post_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Comments({self.id}, {self.author_name}, {self.post_id})"