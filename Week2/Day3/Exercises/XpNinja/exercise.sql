SELECT DISTINCT f.film_id, f.title, f.rating
FROM film f
JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
WHERE f.rating IN ('G', 'PG')
  AND (r.return_date IS NOT NULL OR r.rental_id IS NULL);

CREATE TABLE waiting_list (
    waiting_id SERIAL PRIMARY KEY,
    child_name VARCHAR(100) NOT NULL,
    film_id INTEGER NOT NULL,
    request_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (film_id) REFERENCES film(film_id)
);

SELECT f.title, COUNT(w.waiting_id) AS people_waiting
FROM waiting_list w
JOIN film f ON w.film_id = f.film_id
WHERE f.rating IN ('G', 'PG')
GROUP BY f.title;

INSERT INTO waiting_list (child_name, film_id)
VALUES 
('Youssef', 123),  
('Aya', 123),
('Sara', 150);

SELECT f.title, COUNT(w.waiting_id) AS people_waiting
FROM waiting_list w
JOIN film f ON w.film_id = f.film_id
WHERE f.rating IN ('G', 'PG')
GROUP BY f.title;
