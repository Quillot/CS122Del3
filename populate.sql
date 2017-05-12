USE pixiedustdb;
INSERT INTO product(product_id, name, color, quantity_stocked, personalization_limit, price)
VALUES
(1, 'Swiffer', 'red', 99, 8, 20.50),
(2, 'Swiffer', 'orange', 50, 8, 20.50),
(3, 'Swiffer', 'yellow', 30, 8, 20.50),
(4, 'Swiffer', 'green', 10, 8, 20.50),
(5, 'Swiffer', 'blue', 25, 8, 20.50),
(6, 'Swiffer', 'purple', 55, 8, 20.50),
(7, 'Swiffer', 'black', 80, 8, 20.50),
(8, 'Swiffer', 'pink', 40, 8, 20.50),
(9, 'Niffler', 'red', 22, 5, 40.35),
(10, 'Niffler', 'orange', 58, 5, 40.35),
(11, 'Niffler', 'yellow', 99, 5, 40.35),
(12, 'Niffler', 'green', 7, 5, 40.35),
(13, 'Niffler', 'blue', 64, 5, 40.35),
(14, 'Niffler', 'purple', 87, 5, 40.35),
(15, 'Niffler', 'black', 40, 5, 40.35),
(16, 'Niffler', 'pink', 22, 5, 40.35),
(17, 'Loop-dee-Loop', 'red', 77, 8, 100.00),
(18, 'Loop-dee-Loop', 'orange', 69, 8, 100.00),
(19, 'Loop-dee-Loop', 'yellow', 42, 8, 100.00),
(20, 'Loop-dee-Loop', 'green', 8, 8, 100.00),
(21, 'Loop-dee-Loop', 'blue', 50, 8, 100.00),
(22, 'Loop-dee-Loop', 'purple', 93, 8, 100.00),
(23, 'Loop-dee-Loop', 'black', 10, 8, 100.00),
(24, 'Loop-dee-Loop', 'pink', 22, 8, 100.00),
(25, 'Plopper', 'red', 99, 6, 51.25),
(26, 'Plopper', 'orange', 20, 6, 51.25),
(27, 'Plopper', 'yellow', 70, 6, 51.25),
(28, 'Plopper', 'green', 53, 6, 51.25),
(29, 'Plopper', 'blue', 81, 6, 51.25),
(30, 'Plopper', 'purple', 4, 6, 51.25),
(31, 'Plopper', 'black', 39, 6, 51.25),
(32, 'Plopper', 'pink', 60, 6, 51.25);

INSERT INTO auth_user(id, password, last_login, is_superuser, username, first_name, 
						last_name, email, is_staff, is_active, date_joined)
VALUES
(2, '', NOW(), 0, 'jude', 'jude', 'bautista', 'jude@gmail.com', 0, 1, CURDATE()),
(3, '', NOW(), 0, 'nikki', 'nikki', 'uy', 'nikki@gmail.com', 0, 1, CURDATE()),
(4, '', NOW(), 0, 'jayce', 'jayce', 'ching', 'jayce@gmail.com', 0, 1, CURDATE()),
(5, '', NOW(), 0, 'kemp', 'kemp', 'po', 'kemp@gmail.com', 0, 1, CURDATE());

INSERT INTO agent(agent_id, total_transactions)
VALUES
(2, 2), 
(3, 1); 

INSERT INTO customer(customer_id, agent_id, street, city, country)
VALUES
(4, 2, "Soup Street", "Candy City", "Chocolate Country"),
(5, 3, "Sun Street", "Copernicus City", "Cassiopeia Country");

INSERT INTO recipient(recipient_id, first_name, last_name, street, city, country)
VALUES
(1, 'Kurt', 'De Leon', 'Wow Street', 'Much City', 'Very Country'),
(2, 'Gio', 'Lopez', 'Wow Street', 'Much City', 'Very Country');

INSERT INTO orderinfo(order_id, agent_id, customer_id, issue_date, issue_time, delivery_date, delivery_time, cart_ready)
VALUES
(1, 2, 4, CURDATE(), CURTIME(), CURDATE(), CURTIME(), 1), 
(2, 2, 4, CURDATE(), CURTIME(), CURDATE(), CURTIME(), 1), 
(3, 3, 5, CURDATE(), CURTIME(), CURDATE(), CURTIME(), 1), 
(4, 2, 4, Null, Null, Null, Null, 0),
(5, 2, 4, Null, Null, Null, Null, 1);

INSERT INTO content(content_id, order_id, product_id, personalization, quantity_ordered, discount)
VALUES
(1, 1, 1, 'Hello World', 20, 0.00),
(2, 2, 2, 'Hi there', 10, 0.00),
(3, 3, 3, 'Yo', 30, 0.00),
(4, 4, 2, 'Cart', 20, 0.00),
(5, 5, 3, 'Cart ready', 10, 0.00);

INSERT INTO invite(invite_id, invite_code, used)
VALUES
(1, 111, 0),
(2, 222, 0),
(3, 333, 0),
(4, 444, 0),
(5, 555, 0);


INSERT INTO feature(feature_id, product_id, feature_desc)
VALUES
(1, 1, 'Decent Swiffs'),
(2, 2, 'Slightly above average Swiffs'),
(3, 3, 'Good Swiffs'),
(4, 4, 'Very good Swiffs'),
(5, 5, 'Amazing Swiffs'),
(6, 6, 'Fantastic Swiffs'),
(7, 7, 'Best Swiffs'),
(8, 8, 'Ultimate Swiffs'),
(9, 9, 'Decent Niffs'),
(10, 10, 'Slightly above average Niffs'),
(11, 11, 'Good Niffs'),
(12, 12, 'Very good Niffs'),
(13, 13, 'Amazing Niffs'),
(14, 14, 'Fantastic Niffs'),
(15, 15, 'Best Niffs'), 
(16, 16, 'Ultimate Niffs'),
(17, 17, 'Decent Loops'),
(18, 18, 'Slightly above average Loops'),
(19, 19, 'Good Loops'),
(20, 20, 'Very good Loops'),
(21, 21, 'Amazing Loops'),
(22, 22, 'Fantastic Loops'),
(23, 23, 'Best Loops'),
(24, 24, 'Ultimate Loops'),
(25, 25, 'Decent Plops'),
(26, 26, 'Slightly above average Plops'),
(27, 27, 'Good Plops'),
(28, 28, 'Very good Plops'),
(29, 29, 'Amazing Plops'),
(30, 30, 'Fantastic Plops'),
(31, 31, 'Best Plops'),
(32, 32, 'Ultimate Plops');


INSERT INTO delivery(delivery_id, order_id, recipient_id, gift)
VALUES
(1, 1, 1, 0),
(2, 2, 1, 0),
(3, 3, 2, 0),
(5, 5, 1, 0);
	