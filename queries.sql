SELECT * FROM product WHERE product.price < 60;

# Get quantity of product and quantity ordered of product
SELECT o.order_id as 'Order ID', p.product_id AS 'Product ID', p.name Name, p.color Color, CONCAT(a.first_name, ' ', a.last_name) AS 'Ordered By',  p.quantity_stocked AS 'Quantity Stocked', c.quantity_ordered AS 'Quantity Ordered'
FROM product p, content c, auth_user a, orderinfo o
WHERE p.product_id=c.product_id AND a.id=o.customer_id AND c.order_id=o.order_id AND o.cart_ready IS TRUE AND o.issue_time IS NULL;

# Get orders and agents and customers
SELECT o.order_id AS 'Order ID', CONCAT(aa.first_name, ' ', aa.last_name) AS 'Agent', CONCAT(a.first_name, ' ', a.last_name) AS 'Customer'
FROM orderinfo o, auth_user a, auth_user aa, agent ag
WHERE o.issue_time IS NOT NULL AND o.cart_ready=True AND o.customer_id=a.id AND o.agent_id=ag.agent_id AND aa.id=ag.agent_id
ORDER BY o.agent_id, o.order_id ASC;

#Customers who sent gifts
SELECT DISTINCT CONCAT(a.first_name, ' ', a.last_name) AS 'Customers who have sent gifts' 
FROM delivery d, orderinfo o, auth_user a  
WHERE d.gift=True AND d.order_id=o.order_id AND o.customer_id=a.id;

#Customers who didn't send gifts
SELECT DISTINCT CONCAT(a.first_name, ' ', a.last_name) AS 'Customers who have not sent gifts'
FROM delivery d, orderinfo o, auth_user a  
WHERE a.first_name NOT IN (SELECT a.first_name FROM delivery d, auth_user a, orderinfo o WHERE d.gift=True AND a.id=o.customer_id AND d.order_id=o.order_id) AND d.order_id=o.order_id AND o.customer_id=a.id;

