from lib.comments_repository import CommentsRepository
from lib.comments import Comments

def test_all(db_connection):
    db_connection.seed("seeds/blog_novo.sql")
    repository = CommentsRepository(db_connection)
    result = repository.all()
    assert result == [
        Comments (1,'Author1', 1),
        Comments (2,'Author2', 2),
        Comments (3,'Author3', 3),
        Comments (4,'Author4', 4),
        Comments (5,'Author5', 5),
        Comments (6,'Author6', 6),
        Comments (7,'Author7', 7),
        Comments (8,'Author8', 1),
        Comments (9,'Author9', 2),
        Comments (10,'Author10', 3),
        Comments (11,'Author11', 4),
        Comments (12,'Author12', 5),
        Comments (13,'Author13', 6),
        Comments (14,'Author14', 7)
    ]

def test_find(db_connection):
    db_connection.seed("seeds/blog_novo.sql")
    repository = CommentsRepository(db_connection)
    result = repository.find(3)
    assert result == Comments (3,'Author3', 3)

def test_create(db_connection):
    db_connection.seed("seeds/blog_novo.sql")
    repository = CommentsRepository(db_connection)
    comment = Comments(None, 'Author_test', 1)
    assert repository.create(comment) == None
    result = repository.all()
    assert result == [
        Comments (1,'Author1', 1),
        Comments (2,'Author2', 2),
        Comments (3,'Author3', 3),
        Comments (4,'Author4', 4),
        Comments (5,'Author5', 5),
        Comments (6,'Author6', 6),
        Comments (7,'Author7', 7),
        Comments (8,'Author8', 1),
        Comments (9,'Author9', 2),
        Comments (10,'Author10', 3),
        Comments (11,'Author11', 4),
        Comments (12,'Author12', 5),
        Comments (13,'Author13', 6),
        Comments (14,'Author14', 7),
        Comments (15,'Author_test', 1)
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/blog_novo.sql")
    repository = CommentsRepository(db_connection)
    assert repository.delete(3) == None
    result = repository.all()
    assert result == [
        Comments (1,'Author1', 1),
        Comments (2,'Author2', 2),
        Comments (4,'Author4', 4),
        Comments (5,'Author5', 5),
        Comments (6,'Author6', 6),
        Comments (7,'Author7', 7),
        Comments (8,'Author8', 1),
        Comments (9,'Author9', 2),
        Comments (10,'Author10', 3),
        Comments (11,'Author11', 4),
        Comments (12,'Author12', 5),
        Comments (13,'Author13', 6),
        Comments (14,'Author14', 7)
    ]