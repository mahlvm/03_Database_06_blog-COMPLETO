from lib.comments import Comments

def test_contructs_with_field():
    comment = Comments(4, 'Author4', 4)
    assert comment.id == 4
    assert  comment.author_name == 'Author4'
    assert comment.post_id == 4