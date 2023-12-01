-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;
DROP TABLE IF EXISTS posts CASCADE;



CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
-- CREATE TABLE comments (
--     id SERIAL PRIMARY KEY,
--     author_name VARCHAR,
--     post_id INT
--     CONSTRAINT fk_post FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE
    
-- );

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    author_name VARCHAR(255),
    post_id INTEGER
    -- CONSTRAINT fk_post FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE
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
('Author5', 6),
('Author5', 7),
('Author6', 1),
('Author7', 2),
('Author8', 3),
('Author9', 4),
('Author10', 5),
('Author11', 6),
('Author12', 7);