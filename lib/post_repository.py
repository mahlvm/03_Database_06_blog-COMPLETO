from lib.post import Post
from lib.comments import Comments
from lib.tags import Tags

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
    
    def find_with_comments(self, post_id):
        rows = self._connection.execute("SELECT * FROM posts JOIN comments ON posts.id = comments.post_id WHERE posts.id = %s", [post_id])
        comments = []
        for row in rows:
            comment = Comments(row["id"], row["author_name"], row["post_id"])
            comments.append(comment)
        post = Post(rows[0]['post_id'], rows[0]['title'], rows[0]['content'], comments)
        return post
    
    def find_by_tags(self, tag_name):
        rows = self._connection.execute("SELECT * FROM tags JOIN posts_tags" \
                " ON posts_tags.tag_id = tags.id JOIN posts" \
                " ON posts_tags.post_id = posts.id" \
                " WHERE tags.name = %s", [tag_name])
        posts = []
        for row in rows:
            post = Post(row["id"], row["title"], row["content"])
            posts.append(post)
        tag = Tags(rows[0]['id'], rows[0]['name'], posts)
        return tag