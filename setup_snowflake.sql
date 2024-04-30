CREATE TABLE product (
    id INT AUTOINCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description VARCHAR(255),
    price DECIMAL(10, 2)
);


CREATE TABLE order (
    id INT AUTOINCREMENT PRIMARY KEY,
    product_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (product_id) REFERENCES product(id)
);

-- Inserting products
INSERT INTO product (name, description, price) VALUES
('Laptop', 'High-performance laptop', 1200.00),
('Smartphone', 'Latest model smartphone', 700.00),
('Headphones', 'Noise-cancelling headphones', 150.00);

-- Inserting orders
INSERT INTO order (product_id, quantity, order_date) VALUES
(1, 1, CURRENT_DATE()),
(2, 2, CURRENT_DATE()),
(3, 3, CURRENT_DATE());
