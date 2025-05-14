SELECT r.rental_id, c.first_name, c.last_name, r.rental_date, r.return_date
FROM rental r
INNER JOIN customer c ON r.customer_id = c.customer_id
WHERE r.return_date IS NULL;

SELECT c.first_name, c.last_name, COUNT(r.rental_id) AS rentals_out
FROM rental r
INNER JOIN customer c ON r.customer_id = c.customer_id
WHERE r.return_date IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY rentals_out DESC;


SELECT DISTINCT f.title
FROM film f
INNER JOIN film_actor fa ON f.film_id = fa.film_id
INNER JOIN actor a ON fa.actor_id = a.actor_id
INNER JOIN film_category fc ON f.film_id = fc.film_id
INNER JOIN category c ON fc.category_id = c.category_id
WHERE a.first_name = 'Joe' AND a.last_name = 'Swank'
  AND c.name = 'Action';

