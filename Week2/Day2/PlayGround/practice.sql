SELECT COUNT(*) FROM actors;

SELECT * FROM actors;

SELECT * FROM actors WHERE first_name in ('Matt','Lea','Mohammed');

SELECT AVG(number_oscars) as avg_number_oscars FROM actors;

SELECT DISTINCT number_oscars as special_oscars FROM actors;


SELECT first_name, last_name, number_oscars FROM actors WHERE number_oscars >= 0;

SELECT first_name, last_name, sum(number_oscars) FROM actors GROUP BY first_name, last_name;

SELECT SUM(number_oscars) AS total_oscars FROM actors;

-- SELECT first_name, last_name, sum(number_oscars) FROM actors;
-- Error u need to use GROUP BY

SELECT * FROM actors WHERE first_name IN ('David', 'Mohammed', 'Matt');

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Rachid','Ouali','03/01/1970', 2);

INSERT INTO actors(first_name, last_name, age)
VALUES (, ,);





CREATE TABLE movies(
movie_id SERIAL,
movie_title VARCHAR(50) NOT NULL,
movie_story TEXT,
actor_playing_id INTEGER,
PRIMARY KEY (movie_id),
FOREIGN KEY (actor_playing_id) REFERENCES actors (actor_id)
);

INSERT INTO movies (movie_title, movie_story, actor_playing_id)
VALUES('REST', 'The life of a resting man',
(SELECT actor_id FROM actors where first_name = 'Rachid' and last_name = 'Ouali'));


SELECT * FROM movies;

SELECT actors.first_name, actors.last_name, movies.movie_title
FROM actors
INNER JOIN movies
on movies.actor_playing_id = actors.actor_id;


CREATE TABLE producers(
	producer_id SERIAL,
	producer_first_name VARCHAR(20),
	producer_last_name TEXT,
	producer_movie_id INTEGER,
	PRIMARY KEY (producer_id),
	FOREIGN KEY (producer_movie_id) REFERENCES movies (movie_id)
);


INSERT INTO producers(producer_first_name, producer_last_name, producer_movie_id)
VALUES ('HMAD', 'ALLALI', (SELECT movie_id FROM movies where movie_title = 'REST'));

INSERT INTO producers (producer_first_name, producer_last_name, producer_movie_id)
VALUES 
  ('HMAD', 'ALLALI', (SELECT movie_id FROM movies WHERE movie_title = 'REST')),
  ('HMAD', 'ALLALI', (SELECT movie_id FROM movies WHERE movie_title = 'DUNE')),
  ('NORA', 'SMITH',  (SELECT movie_id FROM movies WHERE movie_title = 'TENET')),
  ('ALI', 'RAHMAN',  (SELECT movie_id FROM movies WHERE movie_title = 'OPPENHEIMER'));



DELETE FROM producers where producer_first_name = 'HMAD';

SELECT * FROM producers;

SELECT producer_first_name, producer_last_name, movies.movie_title FROM Producers
RIGHT OUTER JOIN movies
ON movies.movie_id = producers.producer_movie_id;

