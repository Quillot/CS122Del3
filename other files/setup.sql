DROP DATABASE del3db;
CREATE DATABASE del3db;
USE del3db;

DROP TABLE invite;
DROP TABLE delivery;
DROP TABLE content;
DROP TABLE orderinfo;
DROP TABLE feature;
DROP TABLE product;
DROP TABLE recipient;
DROP TABLE customer;
DROP TABLE agent;

CREATE TABLE agent (
	agent_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	total_transactions INT
);

CREATE TABLE invite (
	invite_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	invite_code INT,
	used tinyint(1)
);

CREATE TABLE customer (
	customer_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	agent_id INT,
	street VARCHAR(255),
	city VARCHAR(255),
	country VARCHAR(255),
	FOREIGN KEY (agent_id) REFERENCES agent(agent_id)
);

CREATE TABLE recipient (
	recipient_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE, 
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	street VARCHAR(255),
	city VARCHAR(255),
	country VARCHAR(255)
);

CREATE TABLE product (
	product_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE, 
	name VARCHAR(255),
	color VARCHAR(255),
	quantity_stocked INT(2),
	personalization_limit INT(1),
	price FLOAT(2)
);

CREATE TABLE feature (
	product_id INT NOT NULL PRIMARY KEY,
	feature_desc VARCHAR(255),
	FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE orderinfo (
	order_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE, 
	agent_id INT NOT NULL,
	customer_id INT NOT NULL,
	recipient_id INT,
	issue_date DATE,
	issue_time TIME,
	delivery_date DATE,
	delivery_time TIME,	
	FOREIGN KEY (agent_id) REFERENCES agent(agent_id),
	FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
	FOREIGN KEY (recipient_id) REFERENCES recipient(recipient_id)
);

CREATE TABLE content (
	-- content_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	order_id INT NOT NULL, 	
	product_id INT NOT NULL, 
	PRIMARY KEY (order_id, product_id),
	personalization VARCHAR(255),
	quantity_ordered INT,
	discount FLOAT(2),
	FOREIGN KEY (order_id) REFERENCES orderinfo(order_id),
	FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE delivery (
	-- delivery_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	order_id INT NOT NULL,
	recipient_id INT NOT NULL,
	PRIMARY KEY (order_id, recipient_id),
	-- gift BOOLEAN, 
	FOREIGN KEY (order_id) REFERENCES orderinfo(order_id),
	FOREIGN KEY (recipient_id) REFERENCES recipient(recipient_id) -- from name to id
);
