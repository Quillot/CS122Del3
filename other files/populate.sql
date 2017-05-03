USE del3db;
INSERT INTO product(product_id, name, color, quantity_stocked, personalization_limit, price)
VALUES
(1, 'Swiffer', 'pink', 99, 8, 20.50),
(2, 'Swiffer', 'red', 50, 8, 20.50),
(3, 'Swiffer', 'blue', 30, 8, 20.50),
(4, 'Swiffer', 'black', 10, 8, 20.50);

INSERT INTO auth_user(id, password, last_login, is_superuser, username, first_name, 
						last_name, email, is_staff, is_active, date_joined)
VALUES
#id 1 belongs to superuser
(2, '', NOW(), 0, 'jude', 'jude', 'bautista', 'jude@gmail.com', 0, 1, CURDATE()),
(3, '', NOW(), 0, 'nikki', 'nikki', 'uy', 'jude@gmail.com', 0, 1, CURDATE()),
(4, '', NOW(), 0, 'jayce', 'jayce', 'ching', 'jayce@gmail.com', 0, 1, CURDATE()),
(5, '', NOW(), 0, 'kemp', 'kemp', 'po', 'nikki@gmail.com', 0, 1, CURDATE());

INSERT INTO agent(agent_id, total_transactions)
VALUES
(2, 2), # makes jude an agent
(3, 1); # makes nikki an agent

INSERT INTO customer(customer_id, agent_id, street, city, country)
VALUES
(4, 2, "Soup Street", "Candy City", "Chocolate Country"),
(5, 3, "Sun Street", "Copernicus City", "Cassiopeia Country");

INSERT INTO recipient(recipient_id, first_name, last_name, street, city, country)
VALUES
(1, 'Kurt', 'De Leon', 'Wow Street', 'Much City', 'Very Country'),
(2, 'Gio', 'Lopez', 'Wow Street', 'Much City', 'Very Country');

INSERT INTO orderinfo(order_id, agent_id, customer_id, issue_date, issue_time, delivery_date, delivery_time)
VALUES
(1, 2, 4, CURDATE(), CURTIME(), CURDATE(), CURTIME()), # Jude (2) in charge of order 1 sent to Kurt (1) by Jayce(4)
(2, 2, 4, CURDATE(), CURTIME(), CURDATE(), CURTIME()), # Jude (2) in charge of order 2 sent to Kurt (1) by Jayce(4)
(3, 3, 5, CURDATE(), CURTIME(), CURDATE(), CURTIME()); # Nikki (3) in charge of order 3 sent to Gio (2) by Kemp (5)

INSERT INTO content(order_id, product_id, personalization, quantity_ordered, discount)
VALUES
(1, 1, 'Hello World', 20, 0.00),
(2, 2, 'Hi there', 10, 0.00),
(3, 3, 'Yo', 30, 0.00),
(3, 2, 'Yello', 20, 0.00);

INSERT INTO invite(invite_id, invite_code, used)
VALUES
(1, 12345, 0),
(2, 11111, 0),
(3, 12341, 0);

INSERT INTO feature(product_id, feature_desc)
VALUES
(1, 'Good Swiffs'),
(2, 'Good Swiffs'),
(3, 'Good Swiffs'),
(4, 'Best Swiffs');
