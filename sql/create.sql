CREATE DATABASE IF NOT EXISTS food_app;
USE food_app;

CREATE TABLE `user` (
	phone_number CHAR(11) PRIMARY KEY,
    user_password VARCHAR(30) NOT NULL,
    user_type VARCHAR(30) NOT NULL
);

CREATE TABLE customer (
	phone_number CHAR(11) PRIMARY KEY,
    user_password VARCHAR(30) NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    mail VARCHAR(50),
    FOREIGN KEY (phone_number) REFERENCES `user`(phone_number)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE restaurant (
	phone_number CHAR(11) PRIMARY KEY,
    user_password VARCHAR(30) NOT NULL,
    shop_name VARCHAR(30),
    label VARCHAR(30),
    FOREIGN KEY (phone_number) REFERENCES `user`(phone_number)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE payment_card (
	payment_id INT PRIMARY KEY,
    customer_id CHAR(11) NOT NULL,
    card_number CHAR(16) NOT NULL,
    cvc INT NOT NULL,
    zip_code CHAR(5) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(phone_number)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE address (
    address_id INT PRIMARY KEY,
    customer_id CHAR(11) NOT NULL,
    address_line VARCHAR(50) NOT NULL,
    city VARCHAR(30) NOT NULL,
    state CHAR(2) NOT NULL,
    zip_code CHAR(5) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(phone_number)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `comment` (
	comment_id INT PRIMARY KEY AUTO_INCREMENT,
    content TEXT,
    rating INT NOT NULL,
    customer_id CHAR(11),
    shop_id CHAR(11) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(phone_number)
		ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (shop_id) REFERENCES restaurant(phone_number)
		ON UPDATE CASCADE ON DELETE CASCADE	
);

CREATE TABLE `order` (
	order_id INT PRIMARY KEY AUTO_INCREMENT,
    order_type VARCHAR(30) NOT NULL,
    order_description TEXT NOT NULL,
    order_total INT,
    order_time DATETIME NOT NULL,
    order_status VARCHAR(30) NOT NULL,
    customer_id CHAR(11) NOT NULL,
    shop_id CHAR(11) NOT NULL,
    address_line VARCHAR(50) NULL,
    payment_card CHAR(16) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(phone_number)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (shop_id) REFERENCES restaurant(phone_number)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE dish (
	dish_id CHAR(3) PRIMARY KEY,
    dish_name VARCHAR(30) NOT NULL,
    dish_description TEXT NOT NULL,
    dish_price INT NOT NULL,
    shop_id CHAR(11) NOT NULL,
    FOREIGN KEY (shop_id) REFERENCES restaurant(phone_number)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE order_dish  (
	order_id INT,
    dish_id CHAR(3),
    PRIMARY KEY (order_id, dish_id),
    FOREIGN KEY (order_id) REFERENCES `order`(order_id)
		ON UPDATE CASCADE ON DELETE CASCADE,	
	FOREIGN KEY (dish_id) REFERENCES dish(dish_id)
		ON UPDATE CASCADE ON DELETE CASCADE
);
