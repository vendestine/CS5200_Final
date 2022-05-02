INSERT INTO 
`user` (phone_number, user_password, user_type)         
VALUES 
('7818739550', '123456', 'customer'),
('7818739551', '123456', 'customer'),
('7818739552', '123456', 'customer'),
('7818739560', '123456', 'restaurant'),
('7818739561', '123456', 'restaurant'),
('7818739562', '123456', 'restaurant');

INSERT INTO
customer (phone_number, user_password, first_name, last_name, mail)
VALUES
('7818739550', '123456', 'wenzhe', 'li', '123@gmail.com'),
('7818739551', '123456', 'siyuan', 'li', '124@gmail.com'),
('7818739552', '123456', 'dama', 'li', '125@gmail.com');

INSERT INTO
restaurant (phone_number, user_password, shop_name, label)
VALUES
('7818739560', '123456', 'mcdonald', 'fast food'),
('7818739561', '123456', 'popeyes', 'fast food'),
('7818739562', '123456', 'starbucks', 'coffee');

INSERT INTO
payment_card (payment_id, customer_id, card_number, cvc, zip_code)
VALUES
(1, '7818739550', '1234567890123450', 123, '02148'),
(2, '7818739550', '1234567890123451', 456, '02148'),
(3, '7818739550', '1234567890123452', 789, '02148');

INSERT INTO
address (address_id, customer_id, address_line, city, state, zip_code)
VALUES
(1, '7818739550', '100 exchange street', 'malden', 'MA', '02148'),
(2, '7818739550', '110 exchange street', 'malden', 'MA', '02148'),
(3, '7818739550', '120 exchange street', 'malden', 'MA', '02148');

INSERT INTO
dish (dish_id, dish_name, dish_description, dish_price, shop_id)
VALUES
('a01', 'sushi', 'japan', '15', '7818739560'),
('a02', 'wudong', 'japan', '20', '7818739560'),
('a03', 'noodle', 'japan', '10', '7818739560');

INSERT INTO 
`order` (order_id, order_type, order_description, order_total, order_time, order_status, customer_id, shop_id, address_line, payment_card)
VALUES
(1, 'pick up', 'sushi,wudong', 35, '2022-4-22 14:09:30', 'active', '7818739550', '7818739560', '100 exchange street', '1234567890123450'),
(2, 'pick up', 'sushi', 15, '2022-4-23 14:09:30', 'active', '7818739550', '7818739560', '110 exchange street', '1234567890123451'),
(3, 'pick up', 'wudong', 20, '2022-4-24 14:09:30', 'active', '7818739550', '7818739560', '120 exchange street', '1234567890123452');

INSERT INTO 
order_dish (order_id, dish_id)
VALUES
(1, 'a01'),
(1, 'a02'),
(2, 'a01'),
(3, 'a02');

INSERT INTO
`comment`(comment_id, content, rating, customer_id, shop_id)
VALUES
(1, 'good', 5, '7818739550', '7818739560'),
(2, 'just so so', 3, '7818739550', '7818739560'),
(3, 'bad', 2, '7818739550', '7818739560');



