-- Exercise1 --------------------------------------------

SELECT rating, COUNT(*) AS number_of_films FROM film GROUP BY rating;

SELECT * FROM film WHERE rating IN ('G', 'PG-13');

SELECT title, length, rental_rate, rating FROM film
WHERE rating IN ('G', 'PG-13') AND length < 120 AND rental_rate < 3.00
ORDER BY title ASC;

UPDATE customer
SET first_name = 'Imad',
    last_name = 'Dabligi',
    email = 'imad@geeks.com'
WHERE first_name = 'Ivan' and last_name = 'Cromwell';


UPDATE address
SET address = '479 Sidi Maarouf',
    district = 'Casablanca',
    city_id = 300,
    postal_code = '20000',
    phone = '0612345678'
WHERE address_id = 1;


UPDATE address
SET address = 'Sidi Maarouf Techno Park',
    district = 'Casablanca',
    city_id = 300,
    postal_code = '20000',
    phone = '06000000'
WHERE address_id = 1;


-- Exercise2 --------------------------------------------

UPDATE students
SET birth_date = '1998-11-02'
WHERE first_name IN ('Lea', 'Marc') AND last_name = 'Benichou';


UPDATE students
SET last_name = 'Guez'
WHERE first_name = 'David' AND last_name = 'Grez';


DELETE FROM students
WHERE first_name = 'Lea' AND last_name = 'Benichou';


SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM students
WHERE birth_date > '2000-01-01';

SELECT first_name, last_name, COUNT(math_grade) AS total_grade
FROM students
GROUP BY first_name, last_name;

SELECT SUM(math_grade) AS total_grades
FROM students;
