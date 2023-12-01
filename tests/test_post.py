from lib.post import Post

def test_contructs_with_field():
    post = Post(1, 'How to use Git', 'Content1')
    assert post.id == 1
    assert post.title == 'How to use Git'
    assert post.content == 'Content1'

