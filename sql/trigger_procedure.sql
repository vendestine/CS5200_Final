USE food_app;

DELIMITER $$
CREATE TRIGGER insert_after_insert_user 
AFTER INSERT ON user
FOR EACH ROW
BEGIN
IF (NEW.user_type = 'customer') THEN
	INSERT INTO customer(phone_number, user_password) VALUES(NEW.phone_number, NEW.user_password);
ELSEIF (NEW.user_type = 'restaurant') THEN 
	INSERT INTO restaurant(phone_number, user_password) VALUES(NEW.phone_number, NEW.user_password);
END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_user_after_update_customer 
AFTER UPDATE ON customer
FOR EACH ROW
BEGIN
UPDATE user SET user_password = NEW.user_password WHERE phone_number = NEW.phone_number;
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER delete_user_after_delete_customer 
AFTER DELETE ON customer
FOR EACH ROW
BEGIN
DELETE FROM user WHERE phone_number = OLD.phone_number;
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_user_after_update_restaurant 
AFTER UPDATE ON restaurant
FOR EACH ROW
BEGIN
UPDATE user SET user_password = NEW.user_password WHERE phone_number = NEW.phone_number;
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER delete_user_after_delete_restaurant 
AFTER DELETE ON restaurant
FOR EACH ROW
BEGIN
DELETE FROM user WHERE phone_number = OLD.phone_number;
END $$
DELIMITER ;



-- comment customer: crud    restaurant: r     
DROP PROCEDURE IF EXISTS comment_add_by_customer;
DELIMITER $$
CREATE PROCEDURE comment_add_by_customer(content TEXT, rating INT, customer_id CHAR(11), shop_name VARCHAR(30) )
BEGIN
	DECLARE shop_id CHAR(11);
    SELECT r.phone_number INTO shop_id 
    FROM restaurant r 
    WHERE r.shop_name = shop_name; 
    INSERT INTO comment(content, rating, customer_id, shop_id) VALUES (content, rating, customer_id, shop_id);
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS comment_read_by_customer;
DELIMITER $$
CREATE PROCEDURE comment_read_by_customer(shop_name VARCHAR(30))
BEGIN    
	SELECT comment_id, shop_name, content, rating, first_name
    FROM comment co, restaurant r, customer c 
    WHERE co.customer_id = c.phone_number 
	AND co.shop_id = r.phone_number
    AND r.shop_name = shop_name;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS comment_read_by_restaurant;
DELIMITER $$
CREATE PROCEDURE comment_read_by_restaurant(shop_id CHAR(11))
BEGIN
	SELECT comment_id, shop_name, content, rating, first_name
    FROM comment co, restaurant r, customer c 
    WHERE co.customer_id = c.phone_number 
	AND co.shop_id = r.phone_number
    AND co.shop_id = shop_id;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS comment_edit_by_customer;
DELIMITER $$
CREATE PROCEDURE comment_edit_by_customer(content TEXT, rating INT, customer_id CHAR(11), shop_name VARCHAR(30), id INT)
BEGIN    

	DECLARE shop_id CHAR(11);
    SELECT r.phone_number INTO shop_id 
    FROM restaurant r 
    WHERE r.shop_name = shop_name; 
    
    UPDATE comment SET content = content, rating = rating
    WHERE customer_id = customer_id AND shop_id = shop_id AND comment_id = id;
END$$
DELIMITER ;



DROP PROCEDURE IF EXISTS comment_delete_by_customer;
DELIMITER $$
CREATE PROCEDURE comment_delete_by_customer(shop_name VARCHAR(30), customer_id CHAR(11), id INT)
BEGIN    

	DECLARE shop_id CHAR(11);
    SELECT r.phone_number INTO shop_id 
    FROM restaurant r 
    WHERE r.shop_name = shop_name; 
    
    DELETE FROM comment WHERE shop_id = shop_id 
    AND customer_id = customer_id AND comment_id = id;
END$$
DELIMITER ;


--  dish customer:r     restaurant: crud
DROP PROCEDURE IF EXISTS dish_read_by_customer;
DELIMITER $$
CREATE PROCEDURE dish_read_by_customer(shop_name VARCHAR(30))
BEGIN
SELECT dish_id, dish_name, dish_description, dish_price
FROM dish d, restaurant r
WHERE d.shop_id = r.phone_number AND r.shop_name = shop_name;
END$$
DELIMITER ;


-- order   customer:crd + fix      restaurant: rd 
DROP PROCEDURE IF EXISTS order_add_by_customer;
DELIMITER $$
CREATE PROCEDURE order_add_by_customer(order_type VARCHAR(30), order_description TEXT, order_status VARCHAR(30), 
customer_id CHAR(11), shop_name VARCHAR(30), address_line VARCHAR(50), payment_card VARCHAR(16))
BEGIN
	DECLARE shop_id CHAR(11);
    SELECT r.phone_number INTO shop_id 
    FROM restaurant r 
    WHERE r.shop_name = shop_name;
    
    INSERT INTO `order`(order_type, order_description, order_time, order_status, customer_id, shop_id, address_line, payment_card)
    VALUES (order_type, order_description, now(), order_status, customer_id, shop_id, address_line, payment_card);
    
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS order_fix;
DELIMITER $$
CREATE PROCEDURE order_fix(id INT)
BEGIN

truncate table order_dish;
INSERT INTO order_dish SELECT * FROM
(SELECT order_id, dish_id
FROM
(SELECT o.order_id, substring_index(substring_index(o.order_description, ',', b.help_topic_id + 1), ',', - 1) AS dish_name
FROM `order` o
INNER JOIN mysql.help_topic b
ON b.help_topic_id < (length(o.order_description) - length(REPLACE(o.order_description, ',', '')) + 1)) ans,
dish d
WHERE ans.dish_name = d.dish_name) details;

UPDATE `order` SET order_total =  
(SELECT SUM(dish_price) AS total_price
FROM order_dish od, dish d
WHERE od.dish_id = d.dish_id AND od.order_id = id) WHERE order_id = id; 
    
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS order_read_by_customer;
DELIMITER $$
CREATE PROCEDURE order_read_by_customer(phone_number CHAR(11))
BEGIN
SELECT order_id, order_type, order_description, order_total, order_time, order_status, shop_name, address_line, payment_card
FROM `order` o, restaurant r
WHERE o.shop_id = r.phone_number AND o.customer_id = phone_number;
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS order_read_by_restaurant;
DELIMITER $$
CREATE PROCEDURE order_read_by_restaurant(phone_number CHAR(11))
BEGIN
SELECT order_id, order_type, order_description, order_total, order_time, order_status, shop_name, address_line, payment_card
FROM `order` o, restaurant r
WHERE o.shop_id = r.phone_number AND o.shop_id = phone_number;
END$$
DELIMITER ;


SHOW triggers;