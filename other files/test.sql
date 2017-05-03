DROP DATABASE testdb;
CREATE DATABASE testdb;
USE testdb;
DROP TABLE orders;
DROP TABLE product;
DROP TABLE feature;
DROP TABLE customer;
DROP TABLE agent;
DROP TABLE recipient;
DROP TABLE delivery;
DROP TABLE content;

CREATE TABLE customer (
	customerno INT NOT NULL PRIMARY KEY,
	lastname VARCHAR(255),
	firstname VARCHAR(255)
);

CREATE TABLE agent (
	agentno INT NOT NULL PRIMARY KEY,
	lastname VARCHAR(255),
	firstname VARCHAR(255),
	customerno INT,
	FOREIGN KEY (customerno) REFERENCES customer(customerno)
);

CREATE TABLE recipient (
	recipientno INT NOT NULL PRIMARY KEY,
	lastname VARCHAR(255),
	firstname VARCHAR(255),
	address VARCHAR(255),
	city VARCHAR(255),
	country VARCHAR(255),
	sentby INT, #need a reference to whoever sent it
	FOREIGN KEY (sentby) REFERENCES customer(customerno)
);

CREATE TABLE orders (
	orderno INT NOT NULL PRIMARY KEY,
	issuedate DATE,
	deliverydate DATE,
	agentno INT,
	recipientno INT,
	FOREIGN KEY(agentno) REFERENCES agent(agentno),
	FOREIGN KEY(recipientno) REFERENCES recipient(recipientno)
);

CREATE TABLE product (
	productno INT NOT NULL PRIMARY KEY,
	productname VARCHAR(255),
	color VARCHAR(30),
	stock INT, #how to limit to more than 1
	personalizationlimit VARCHAR(255),
	price FLOAT(2) #check this
);

CREATE TABLE feature (
	productno INT NOT NULL,  #might be better way to implement this
	PRIMARY KEY(productno),
	FOREIGN KEY(productno) REFERENCES product(productno)
);



CREATE TABLE delivery (
	recipientno INT NOT NULL,
	orderno INT NOT NULL,
	gift BOOLEAN,
	PRIMARY KEY(recipientno, orderno),
	FOREIGN KEY(recipientno) REFERENCES recipient(recipientno),
	FOREIGN KEY(orderno) REFERENCES orders(orderno)
);

CREATE TABLE content (
	orderno INT NOT NULL,
	productno INT NOT NULL,
	personalization varchar(255),
	quantityordered INT, #limit this
	discount float(2), #??
	PRIMARY KEY(orderno, productno),
	FOREIGN KEY(orderno) REFERENCES orders(orderno),
	FOREIGN KEY(productno) REFERENCES product(productno)
);