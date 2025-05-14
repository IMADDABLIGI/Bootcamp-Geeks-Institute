CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    FOREIGN KEY (order_id) REFERENCES product_orders(order_id) ON DELETE CASCADE
);

INSERT INTO product_orders (customer_name)
VALUES ('Imad'), ('Sara');

INSERT INTO items (order_id, product_name, quantity, price)
VALUES
(1, 'Mouse', 2, 15.99),
(1, 'Keyboard', 1, 45.00),
(2, 'Monitor', 1, 200.00),
(2, 'USB Cable', 3, 5.00);

CREATE OR REPLACE FUNCTION get_total_order_price(order_input INT)
RETURNS NUMERIC AS $$
DECLARE
    total NUMERIC(10,2);
BEGIN
    SELECT SUM(quantity * price)
    INTO total
    FROM items
    WHERE order_id = order_input;

    RETURN COALESCE(total, 0);
END;
$$ LANGUAGE plpgsql;

SELECT get_total_order_price(1) AS total_price;
