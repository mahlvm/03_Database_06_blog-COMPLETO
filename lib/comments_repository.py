from lib.comments import Comments

class CommentsRepository:

    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM comments")
        return [
            Comments (row["id"], row["author_name"], row["post_id"])
            for row in rows
        ]
    
    def find(self, comment_id):
        rows = self._connection.execute("SELECT * FROM comments WHERE id = %s", [comment_id])
        row = rows[0]
        return Comments(row["id"], row["author_name"], row["post_id"])
    
    def create(self, comment_test):
        self._connection.execute(
            "INSERT INTO comments (author_name, post_id) VALUES (%s, %s)",
            [comment_test.author_name, comment_test.post_id]
        )
        return None
    
    def delete(self, comment_id):
        self._connection.execute(
                "DELETE FROM comments WHERE id = %s", [comment_id]
            )
        return