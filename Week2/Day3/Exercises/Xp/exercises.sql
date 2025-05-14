-- Exercise1 -------------------------------------------------------------------------------
SELECT * FROM language;

SELECT f.title, f.description, l.name FROM film f
INNER JOIN language l
ON f.language_id = l.language_id;


SELECT f.title, f.description, l.name  FROM language l
LEFT JOIN film f 
ON f.language_id = l.language_id;

CREATE TABLE new_film(
	new_film_id SERIAL PRIMARY KEY,
	name VARCHAR(60)
);

INSERT INTO new_film(name)
VALUES ('Wja3 Trab'),('Borto9ala lmora'),('Khouloud');

CREATE TABLE customer_review(
	review_id SERIAL PRIMARY KEY NOT NULL,
	film_id INTEGER,
	language_id INTEGER,
	title VARCHAR(30),
	score INTEGER,
	review_text TEXT,
	last_update DATE,
	FOREIGN KEY (film_id) REFERENCES new_film (new_film_id) ON DELETE CASCADE,
	FOREIGN KEY (language_id) REFERENCES language (language_id)
);

INSERT INTO 
customer_review(film_id, language_id, title, score, review_text, last_update)
VALUES	(1, 1, 'Review Title', 9, 'Film kan naadi', '2025-05-14'),
		(2, 1, 'NOICE', 8, 'Tfarjo fih 3la 7ssabi', '2025-05-14');

DELETE FROM new_film WHERE new_film.name = 'Wja3 Trab';

-- Exercise2 -------------------------------------------------------------------------------

UPDATE film
SET language_id = 2
WHERE title = 'Chamber Italian';

-- The foreign keys defined for the customer table are (store_id - address_id).
-- The affection of insert will be strict means if u didn't give a real id value it will return an error.

DROP TABLE customer_review;
-- It's an easy step, because this table is only a child for other parents

SELECT COUNT(*) FROM rental
WHERE return_date IS NULL;


SELECT f.title, f.replacement_cost
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;



SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe'
AND f.description ILIKE '%sumo%';


SELECT title
FROM film
WHERE length < 60 AND rating = 'R';


SELECT f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN payment p ON r.rental_id = p.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND p.amount > 4.00
  AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

SELECT f.title, f.description, f.replacement_cost
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC;

