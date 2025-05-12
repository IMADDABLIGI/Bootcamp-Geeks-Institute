CREATE DATABASE public;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,      
    name TEXT NOT NULL UNIQUE,   
    price REAL NOT NULL       
);

INSERT INTO items (name, price)
VALUES ('Small Desk', 100), ('Large desk', 300), ('Fan', 80);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,      
    first_name TEXT NOT NULL,
    last_name REAL NOT NULL
);

INSERT INTO customers (first_name, last_name)
VALUES ('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Greg', 'Jones'),
('Trevor', 'Green'),
('Melanie', 'Johnson')

SELECT * FROM items;

SELECT * FROM items WHERE price > 80;

SELECT * FROM items WHERE price <= 300;

SELECT * FROM customers WHERE last_name = 'Smith';

SELECT * FROM customers WHERE first_name != 'Scott';
