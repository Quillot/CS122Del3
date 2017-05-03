USE del3db;
DROP TABLE orderinfo;
DROP TABLE content;
DROP TABLE delivery;
DROP TABLE agent;
DROP TABLE customer;
DROP TABLE recipient;
DROP TABLE product;
DROP TABLE feature;

CREATE TABLE agent (
	agent_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	total_transactions INT
);

CREATE TABLE invite (
	invite_code INT NOT NULL,
	used BOOLEAN NOT NULL
);

CREATE TABLE customer (
	customer_id INT NOT NULL PRIMARY KEY UNIQUE,
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

CREATE TABLE orderinfo (
	order_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE, 
	agent_id INT,
	recipient_id INT,
	issue_date DATE,
	issue_time TIME,
	delivery_date DATE,
	delivery_time TIME,
	FOREIGN KEY (agent_id) REFERENCES agent(agent_id),
	FOREIGN KEY (recipient_id) REFERENCES recipient(recipient_id)
);

CREATE TABLE content (
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
	order_id INT NOT NULL,
	recipient_id INT,
	PRIMARY KEY (order_id, recipient_id),
	gift BOOLEAN, -- changed
	FOREIGN KEY (order_id) REFERENCES orderinfo(order_id),
	FOREIGN KEY (recipient_id) REFERENCES recipient(recipient_id) -- from name to id
);
