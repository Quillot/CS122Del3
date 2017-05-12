USE pixiedust$pixiedustdb;

DROP TABLE invite;
DROP TABLE delivery;
DROP TABLE content;
DROP TABLE orderinfo;
DROP TABLE feature;
DROP TABLE product;
DROP TABLE recipient;
DROP TABLE customer;
DROP TABLE agent;

-- CREATE table auth_user (
-- 	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
-- 	password VARCHAR(255) NOT NULL,
-- 	last_login DATETIME,
-- 	is_superuser BOOLEAN NOT NULL,
-- 	username VARCHAR(30) NOT NULL,
-- 	first_name VARCHAR(30) NOT NULL,
-- 	last_name VARCHAR(30) NOT NULL,
-- 	email VARCHAR(254) NOT NULL,
-- 	is_staff BOOLEAN NOT NULL,
-- 	is_active BOOLEAN NOT NULL,
-- 	date_joined DATETIME NOT NULL
-- );

CREATE TABLE agent (
	agent_id INT NOT NULL PRIMARY KEY UNIQUE,
	total_transactions INT NOT NULL DEFAULT 0
);

CREATE TABLE invite (
	invite_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	invite_code INT NOT NULL DEFAULT 11111,
	used tinyint(1) NOT NULL DEFAULT 0
);

CREATE TABLE customer (
	customer_id INT NOT NULL PRIMARY KEY UNIQUE,
	agent_id INT NOT NULL DEFAULT 2,
	street VARCHAR(255) NOT NULL DEFAULT "Shiny Street",
	city VARCHAR(255) NOT NULL DEFAULT "Clean City",
	country VARCHAR(255) NOT NULL DEFAULT "Cool Country",
	FOREIGN KEY (agent_id) REFERENCES agent(agent_id)
);

CREATE TABLE recipient (
	recipient_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE, 
	first_name VARCHAR(255) NOT NULL DEFAULT "Ruscie",
	last_name VARCHAR(255) NOT NULL DEFAULT "Pient",
	street VARCHAR(255) NOT NULL DEFAULT "Shiny Street",
	city VARCHAR(255) NOT NULL DEFAULT "Clean City",
	country VARCHAR(255) NOT NULL DEFAULT "Cool Country"
);

CREATE TABLE product (
	product_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE, 
	name VARCHAR(255) NOT NULL DEFAULT "Swiffer",
	color VARCHAR(255) NOT NULL DEFAULT "red",
	quantity_stocked INT(2) NOT NULL DEFAULT 1,
	personalization_limit INT(1) NOT NULL DEFAULT 8,
	price FLOAT(2) NOT NULL DEFAULT 20.00
);

CREATE TABLE feature (
	feature_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	product_id INT NOT NULL DEFAULT 1,
	feature_desc VARCHAR(255) NOT NULL DEFAULT "",
	FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE orderinfo (
	order_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE, 
	agent_id INT NOT NULL DEFAULT 2,
	customer_id INT NOT NULL DEFAULT 4,
	issue_date DATE,
	issue_time TIME,
	delivery_date DATE ,
	delivery_time TIME,
	cart_ready BOOLEAN NOT NULL DEFAULT 0,
	FOREIGN KEY (agent_id) REFERENCES agent(agent_id),
	FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE content (
	content_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	order_id INT NOT NULL, 	
	product_id INT NOT NULL, 
	personalization VARCHAR(255) DEFAULT "",
	quantity_ordered INT DEFAULT 1,
	discount FLOAT(2) DEFAULT 0.00,
	FOREIGN KEY (order_id) REFERENCES orderinfo(order_id),
	FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE delivery (
	delivery_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	order_id INT NOT NULL UNIQUE,
	recipient_id INT DEFAULT NULL,
	gift BOOLEAN, 
	FOREIGN KEY (order_id) REFERENCES orderinfo(order_id),
	FOREIGN KEY (recipient_id) REFERENCES recipient(recipient_id)
);	
