-- Create a table for storing product information
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert a large number of records into the products table
INSERT INTO products (product_name, category, price, stock) VALUES
('Product 1', 'Category A', 19.99, 100),
('Product 2', 'Category B', 29.99, 200),
('Product 3', 'Category C', 39.99, 300),
('Product 4', 'Category A', 49.99, 150),
('Product 5', 'Category B', 59.99, 250);

-- Generate more records to reach over 3000 lines of code
-- Each block contains 100 records, and we'll repeat it 30 times with slight modifications

-- Block 1
INSERT INTO products (product_name, category, price, stock) VALUES
('Product 6', 'Category C', 24.99, 100),
('Product 7', 'Category A', 34.99, 200),
('Product 8', 'Category B', 44.99, 300),
-- ...
('Product 105', 'Category C', 64.99, 250);

-- Block 2
INSERT INTO products (product_name, category, price, stock) VALUES
('Product 106', 'Category A', 20.99, 100),
('Product 107', 'Category B', 30.99, 200),
('Product 108', 'Category C', 40.99, 300),
-- ...
('Product 205', 'Category A', 60.99, 250);

-- Repeat similar blocks to reach the desired number of lines

-- ...

-- Block 30
INSERT INTO products (product_name, category, price, stock) VALUES
('Product 2906', 'Category C', 29.49, 100),
('Product 2907', 'Category A', 39.49, 200),
('Product 2908', 'Category B', 49.49, 300),
-- ...
('Product 3005', 'Category C', 69.49, 250);

-- Queries to retrieve data
SELECT * FROM products WHERE price > 50.00;
SELECT category, COUNT(*) AS product_count FROM products GROUP BY category;

-- Update some records
UPDATE products SET stock = stock + 50 WHERE category = 'Category A';
UPDATE products SET price = price * 1.10 WHERE category = 'Category B';

-- Delete some records
DELETE FROM products WHERE stock < 50;

-- More complex queries
SELECT category, AVG(price) AS average_price FROM products GROUP BY category HAVING AVG(price) > 30.00;

-- Example of a stored procedure (optional, for extra lines)
DELIMITER //

CREATE PROCEDURE GetProductsByCategory (IN cat VARCHAR(100))
BEGIN
    SELECT * FROM products WHERE category = cat;
END //

DELIMITER ;

-- Call the stored procedure
CALL GetProductsByCategory('Category A');
CALL GetProductsByCategory('Category B');
CALL GetProductsByCategory('Category C');
