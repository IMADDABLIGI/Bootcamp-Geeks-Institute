-- Exercise 1 --------------------------------------------------------------------

SELECT * FROM items ORDER BY price ASC;

SELECT * FROM items WHERE price >= 80 ORDER BY price DESC;

SELECT first_name, last_name FROM customers ORDER BY first_name ASC LIMIT 3;

SELECT last_name FROM customers ORDER BY last_name DESC;

-- Exercise 2 --------------------------------------------------------------------


SELECT * FROM customer;

SELECT (first_name, last_name) AS full_name FROM customer;

SELECT DISTINCT create_date FROM customer;

SELECT * FROM customer ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

SELECT address, phone
FROM address
WHERE district = 'Texas';

SELECT * FROM film WHERE film_id = 15 OR film_id = 150;

SELECT film_id, title, description, length, rental_rate FROM film
WHERE title = 'Brooklyn Desert';

SELECT film_id, title, description, length, rental_rate FROM film
WHERE title LIKE 'Br%';

SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10;

SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10 OFFSET 10;

SELECT c.first_name, c.last_name, p.amount, p.payment_date FROM customer c
INNER JOIN payment p
ON c.customer_id = p.customer_id
ORDER BY c.customer_id;

SELECT * FROM film
WHERE film_id NOT IN ( SELECT DISTINCT film_id FROM inventory);

SELECT ct.city, cn.country FROM city ct
INNER JOIN country cn
ON ct.country_id = cn.country_id;
