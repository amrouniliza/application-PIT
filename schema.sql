CREATE TABLE product (
	lid serial PRIMARY KEY,
	code VARCHAR ( 100 ) NOT NULL,
	name VARCHAR ( 150 ) NOT NULL,
	price INT NOT NULL
);

Multiple insert
INSERT INTO
    product(code,name,price)
VALUES
    ('111', 'sucre', 10),
    ('222', 'tomate', 19),
    ('333', 'fromage', 21);
