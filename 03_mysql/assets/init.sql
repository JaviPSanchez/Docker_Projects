CREATE TABLE IF NOT EXISTS products (
    product_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(50),
    retail_price DOUBLE
);

INSERT INTO products (product_name, retail_price) values ('LEATHER BELT', 18.54);
INSERT INTO products (product_name, retail_price) values ('PC FIX', 250.00);
INSERT INTO products (product_name, retail_price) values ('CAR WASHER', 25.36);
INSERT INTO products (product_name, retail_price) values ('PANTS', 45.50);
