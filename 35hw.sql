DROP TABLE IF EXISTS ord_pro;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS customer_profiles;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    email VARCHAR(40) UNIQUE NOT NULL
);

CREATE TABLE customer_profiles (
    id SERIAL PRIMARY KEY,
    phone_number VARCHAR(15) NOT NULL,
    address VARCHAR(100) NOT NULL,
    customer_id INT NOT NULL REFERENCES customers(id) ON DELETE CASCADE UNIQUE
);

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    contact_email VARCHAR(40) UNIQUE NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    supplier_id INT NOT NULL REFERENCES suppliers(id) ON DELETE CASCADE
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    customer_id INT NOT NULL REFERENCES customers(id) ON DELETE CASCADE
);

CREATE TABLE ord_pro (
    id SERIAL PRIMARY KEY,
    order_id INT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    quantity INT NOT NULL CHECK (quantity > 0),
    UNIQUE(order_id, product_id)
);

INSERT INTO customers (name, email) VALUES
    ('Alice Johnson', 'alice.johnson@example.com'),
    ('Bob Smith', 'bob.smith@example.com');

INSERT INTO customer_profiles (phone_number, address, customer_id) VALUES
    ('123-456-7890', '123 Main St, Anytown, USA', 1),
    ('987-654-3210', '456 Elm St, Othertown, USA', 2);

INSERT INTO suppliers (name, contact_email) VALUES
    ('Tech Supplies Inc.', 'contact@techsupplies.com'),
    ('Home Goods Co.', 'contact@homegoods.com');

INSERT INTO products (name, price, supplier_id) VALUES
    ('Laptop', 999.99, 1),
    ('Smartphone', 599.99, 1),
    ('Desk Chair', 199.99, 2),
    ('Coffee Table', 149.99, 2);

INSERT INTO orders (customer_id) VALUES
    (1),
    (2);
INSERT INTO ord_pro (order_id, product_id, quantity) VALUES
    (1, 1, 1),
    (1, 3, 2),
    (2, 2, 1),
    (2, 4, 1);

SELECT
customers.name AS "Customer Name",
products.name AS "Product Name",
SUM(ord_pro.quantity) AS "Total Quantity Ordered",
SUM(products.price * ord_pro.quantity) AS "Total Price Ordered"
FROM customers
JOIN orders ON customers.id = orders.customer_id
JOIN ord_pro ON orders.id = ord_pro.order_id
JOIN products ON ord_pro.product_id = products.id
GROUP BY customers.name, products.name;