from lib.post import Post

class PostRepository:

    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM posts")
        return [
            Post(row["id"], row["title"], row["content"])
            for row in rows
        ]
    
    def find(self, post_id):
        rows = self._connection.execute("SELECT * FROM posts WHERE id = %s", [post_id])
        row = rows[0]
        return Post(row["id"], row["title"], row["content"])
    
    def create(self, post_test):
        self._connection.execute(
            "INSERT INTO posts (title, content) VALUES (%s, %s)",
            [post_test.title, post_test.content]
        )
        return None
    
    def delete(self, post_id):
        self._connection.execute(
                "DELETE FROM posts WHERE id = %s", [post_id]
            )
        return
    