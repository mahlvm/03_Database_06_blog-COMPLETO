-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts CASCADE;
DROP TABLE IF EXISTS tags CASCADE;
DROP TABLE IF EXISTS posts_tags CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE SEQUENCE IF NOT EXISTS comments_id_seq;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255)
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    author_name VARCHAR(255),
    post_id INTEGER
    -- CONSTRAINT fk_post FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name text
);

CREATE TABLE posts_tags (
    post_id int,
    tag_id int,
    constraint fk_post foreign key(post_id) references posts(id) on delete cascade,
    constraint fk_tag foreign key(tag_id) references tags(id) on delete cascade,
    PRIMARY KEY (post_id, tag_id)
);


INSERT INTO posts (title, content) VALUES
('How to use Git', 'Conten1'),
('Fun classes', 'Conten2'),
('Using a REPL', 'Conten3'),
('My weekend in Edinburgh', 'Conten4'),
('The best chocolate cake EVER', 'Conten5'),
('A foodie week in Spain', 'Conten6'),
('SQL basics', 'Conten7');

INSERT INTO comments (author_name, post_id) VALUES
('Author1', 1),
('Author2', 2),
('Author3', 3),
('Author4', 4),
('Author5', 5),
('Author6', 6),
('Author7', 7),
('Author8', 1),
('Author9', 2),
('Author10', 3),
('Author11', 4),
('Author12', 5),
('Author13', 6),
('Author14', 7);

INSERT INTO tags (name) VALUES
('coding'),
('travel'),
('cooking'),
('education');

INSERT INTO posts_tags (post_id, tag_id) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 3),
(6, 2),
(7, 1),
(6, 3),
(2, 4),
(3, 4);

