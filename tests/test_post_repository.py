from lib.post_repository import PostRepository
from lib.post import Post
from lib.comments import Comments
from lib.tags import Tags

def test_all(db_connection):
    db_connection.seed("seeds/blog_novo.sql")
    repository = PostRepository(db_connection)
    result = repository.all()
    assert result == [
        Post (1, 'How to use Git', 'Conten1'),
        Post (2, 'Fun classes', 'Conten2'),
        Post (3, 'Using a REPL', 'Conten3'),
        Post (4, 'My weekend in Edinburgh', 'Conten4'),
        Post (5, 'The best chocolate cake EVER', 'Conten5'),
        Post (6, 'A foodie week in Spain', 'Conten6'),
        Post (7, 'SQL basics', 'Conten7')
    ]

def test_find(db_connection):
    db_connection.seed("seeds/blog_novo.sql")
    repository = PostRepository(db_connection)
    result = repository.find(3)
    assert result == Post (3, 'Using a REPL', 'Conten3')

def test_create(db_connection):
    db_connection.seed("seeds/blog_novo.sql")
    repository = PostRepository(db_connection)
    post = Post(None, 'PostTest', 'ContentTest')
    assert repository.create(post) == None
    result = repository.all()
    assert result == [
        Post (1, 'How to use Git', 'Conten1'),
        Post (2, 'Fun classes', 'Conten2'),
        Post (3, 'Using a REPL', 'Conten3'),
        Post (4, 'My weekend in Edinburgh', 'Conten4'),
        Post (5, 'The best chocolate cake EVER', 'Conten5'),
        Post (6, 'A foodie week in Spain', 'Conten6'),
        Post (7, 'SQL basics', 'Conten7'),
        Post (8, 'PostTest', 'ContentTest')
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/blog_novo.sql")
    repository = PostRepository(db_connection)
    assert repository.delete(3) == None
    result = repository.all()
    assert result == [
        Post (1, 'How to use Git', 'Conten1'),
        Post (2, 'Fun classes', 'Conten2'),
        Post (4, 'My weekend in Edinburgh', 'Conten4'),
        Post (5, 'The best chocolate cake EVER', 'Conten5'),
        Post (6, 'A foodie week in Spain', 'Conten6'),
        Post (7, 'SQL basics', 'Conten7')
    ]


def  test_find_comments_per_post(db_connection):
    db_connection.seed("seeds/blog_novo.sql")
    repository = PostRepository(db_connection)
    result = repository.find_with_comments(1)
    assert result == Post(1, 'How to use Git', 'Conten1', [
        Comments (1,'Author1', 1),
        Comments (8,'Author8', 1)
    ])

def  test_find_post_per_tag(db_connection):
    db_connection.seed("seeds/blog_novo.sql")
    repository = PostRepository(db_connection)
    result = repository.find_by_tags('coding')
    assert result == Tags(1, 'coding', [
        Post (1, 'How to use Git', 'Conten1'),
        Post (2, 'Fun classes', 'Conten2'),
        Post (3, 'Using a REPL', 'Conten3'),
        Post (7, 'SQL basics', 'Conten7'),
    ])