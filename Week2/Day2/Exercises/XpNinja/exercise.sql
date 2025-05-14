SELECT * FROM actors;SELECT *
FROM customer
ORDER BY first_name ASC
OFFSET (
  SELECT COUNT(*) FROM customer
) - 2 LIMIT 2;

DELETE FROM payment
WHERE customer_id = (
  SELECT customer_id FROM customer WHERE first_name = 'Scott'
);

SELECT * FROM customer WHERE first_name = 'Scott';

SELECT 
    p.payment_id,
    c.first_name,
    c.last_name,
    p.amount,
    p.payment_date
FROM payment p
LEFT JOIN customer c ON p.customer_id = c.customer_id;

SELECT 
    p.payment_id,
    c.first_name,
    c.last_name,
    p.amount,
    p.payment_date
FROM payment p
INNER JOIN customer c ON p.customer_id = c.customer_id;
