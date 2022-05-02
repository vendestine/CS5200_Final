from model import Mysql
from tabulate import tabulate

# user table
class User():
    def __init__(self):
        self.mysql = Mysql()

    def user_register(self, *args):
        sql = "INSERT INTO user(phone_number, user_password, user_type)" \
              "VALUES ('{}', '{}', '{}')".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("register success!")
            return True
        else:
            print("register fail!")
            return False

    def user_login(self, *args):
        sql = "SELECT * FROM user WHERE phone_number = '{}' AND user_password = '{}'".format(*args)
        result = self.mysql.get_all(sql)
        if not result:
            print("login in fail!")
            return False
        else:
            print("log in success!")
            return result

    def user_change_phone(self, *args):
        sql = "UPDATE user SET phone_number = '{}' WHERE phone_number = '{}' AND user_password = '{}'".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("change phone number success!")
            return True
        else:
            print("change phone number fail!")
            return False

    # def user_delete(self, *args):
    #     sql = "DELETE FROM user WHERE phone_number = '{}' AND user_password = '{}'".format(*args)
    #     result = self.mysql.update(sql)
    #     if not result:
    #         print("delete user success")
    #     else:
    #         print("delete user fail")



# customer table
class Customer():
    def __init__(self):
        self.mysql = Mysql()

    def customer_read(self, arg):
        sql = "SELECT * FROM customer WHERE phone_number = '{}'".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("read customer fail")
        else:
            print("read customer success")
            print(tabulate(result, headers='keys', tablefmt="simple"))

    def customer_edit(self, *args):
        sql = "UPDATE customer SET user_password = '{}', first_name = '{}', last_name = '{}'," \
              "mail = '{}' WHERE phone_number = '{}'".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("edit customer information success!")
            return True
        else:
            print("edit customer information fail!")
            return False

    def customer_delete(self, arg1, arg2):
        sql = "DELETE FROM customer WHERE phone_number = '{}' AND user_password = '{}'".format(arg1, arg2)
        result = self.mysql.update(sql)
        if not result:
            print("delete customer success")
            return True
        else:
            print("delete customer fail")
            return False


# restaurant table
class Restaurant():
    def __init__(self):
        self.mysql = Mysql()

    def restaurant_read(self, arg):
        sql = "SELECT * FROM restaurant WHERE phone_number = '{}'".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("read restaurant fail")
        else:
            print("read restaurant success")
            print(tabulate(result, headers='keys', tablefmt="simple"))

    def restaurant_edit(self, *args):
        sql = "UPDATE restaurant SET user_password = '{}', shop_name = '{}', label = '{}'" \
              "WHERE phone_number = '{}'".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("edit restaurant information success!")
            return True
        else:
            print("edit restaurant information fail!")
            return False

    def restaurant_delete(self, arg1, arg2):
        sql = "DELETE FROM restaurant WHERE phone_number = '{}' AND user_password = '{}'".format(arg1, arg2)
        result = self.mysql.update(sql)
        if not result:
            print("delete restaurant success")
            return True
        else:
            print("delete restaurant fail")
            return False


    def restaurant_read_by_user(self):
        sql = "SELECT shop_name, label FROM restaurant"
        result = self.mysql.get_all(sql)
        if not result:
            print("read restaurant fail")
        else:
            print("read restaurant success")
            print(tabulate(result, headers='keys', tablefmt="simple"))

    def name_exist(self, arg):
        sql = "SELECT * FROM restaurant WHERE shop_name = '{}'".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("not exist this id")
        else:
            return result



# address table
class Address():
    def __init__(self):
        self.mysql = Mysql()

    def address_add(self, *args):
        sql = "INSERT INTO address(address_id, customer_id, address_line, city, state, zip_code)" \
              "VALUES ({}, '{}', '{}', '{}', '{}', '{}')".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("address add success!")
            return True
        else:
            print("address add fail!")
            return False

    def address_read(self, arg):
        sql = "SELECT * FROM address WHERE customer_id = '{}'".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("read address fail")
        else:
            print("read address success")
            print(tabulate(result, headers='keys', tablefmt="simple"))

    def address_edit(self, *args):
        sql = "UPDATE address SET address_line = '{}', city = '{}', state = '{}', zip_code = '{}'" \
              "WHERE customer_id = '{}' AND address_id = {}".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("edit address information success!")
            return True
        else:
            print("edit address information fail!")
            return False

    def address_delete(self, arg1, arg2):
        sql = "DELETE FROM address WHERE customer_id = '{}' AND address_id = {} ".format(arg1, arg2)
        result = self.mysql.update(sql)
        if not result:
            print("delete address success")
            return True
        else:
            print("delete address fail")
            return False

    def id_exist(self, arg):
        sql = "SELECT * FROM address WHERE address_id = {}".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("not exist this id")
        else:
            return result

    def line_exist(self, arg):
        sql = "SELECT * FROM address WHERE address_line = '{}'".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("not exist this address line")
        else:
            return result



# payment table
class Payment():
    def __init__(self):
        self.mysql = Mysql();

    def card_add(self, *args):
        sql = "INSERT INTO payment_card(payment_id, customer_id, card_number, cvc, zip_code)" \
              "VALUES ({}, '{}', '{}', {}, '{}')".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("card add success!")
            return True
        else:
            print("card add fail!")
            return False

    def card_read(self, arg):
        sql = "SELECT * FROM payment_card WHERE customer_id = '{}'".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("read card fail")
        else:
            print("read card success")
            print(tabulate(result, headers='keys', tablefmt="simple"))

    def card_edit(self, *args):
        sql = "UPDATE payment_card SET card_number = '{}', cvc = {}, zip_code = '{}' " \
              "WHERE customer_id = '{}' AND payment_id = {} ".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("edit card information success!")
            return True
        else:
            print("edit card information fail!")
            return False

    def card_delete(self, arg1, arg2):
        sql = "DELETE FROM payment_card WHERE customer_id = '{}' AND payment_id = {}".format(arg1, arg2)
        result = self.mysql.update(sql)
        if not result:
            print("delete card success")
            return True
        else:
            print("delete card fail")
            return False

    def id_exist(self, arg):
        sql = "SELECT * FROM payment_card WHERE payment_id = {}".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("not exist this id")
        else:
            return result

    def card_exist(self, arg):
        sql = "SELECT * FROM payment_card WHERE card_number = '{}'".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("not exist this id")
        else:
            return result



# dish table
class Dish():
    def __init__(self):
        self.mysql = Mysql()

    def dish_add_by_restaurant(self, *args):
        sql = "INSERT INTO dish(dish_id, dish_name, dish_description, dish_price, shop_id)" \
              "VALUES ('{}', '{}', '{}', {}, '{}')".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("dish add success!")
            return True
        else:
            print("dish add fail!")
            return False

    def dish_read_by_restaurant(self, arg):
        sql = "SELECT dish_id, dish_name, dish_description, dish_price FROM dish WHERE shop_id = '{}'".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("read dish fail")
        else:
            print("read dish success")
            print(tabulate(result, headers='keys', tablefmt="simple"))



    def dish_read_by_customer(self, arg):
        sql = "CALL dish_read_by_customer('{}')".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("read dish fail")

        else:
            print("read dish success")
            print(tabulate(result, headers='keys', tablefmt="simple"))
            return result


    def dish_in(self, arg):
        sql = "CALL dish_read_by_customer('{}')".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("read dish fail")

        else:
            print("read dish success")
            print(tabulate(result, headers='keys', tablefmt="simple"))
            return result


    def dish_edit_by_restaurant(self, *args):
        sql = "UPDATE dish SET dish_name = '{}', dish_description = '{}', dish_price = {} "\
              "WHERE shop_id = '{}' AND dish_id = '{}'".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("edit dish information success!")
            return True
        else:
            print("edit dish information fail!")
            return False

    def dish_delete_by_restaurant(self, arg1, arg2):
        sql = "DELETE FROM dish WHERE shop_id = '{}' AND dish_id = '{}'".format(arg1, arg2)
        result = self.mysql.update(sql)
        if not result:
            print("delete dish success")
            return True
        else:
            print("delete dish fail")
            return False

    def id_exist(self, arg):
        sql = "SELECT * FROM dish WHERE dish_id = '{}'".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("not exist this id")
        else:
            return result


# order table
class Order():
    def __init__(self):
        self.mysql = Mysql()

    def order_add_by_customer(self, *args):
        sql = "CALL order_add_by_customer('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("order add success!")
            return True
        else:
            print("order add fail!")
            return False

    def order_fix(self):
        sql = "CALL order_fix()"
        result = self.mysql.update(sql)
        if not result:
            print("order fix success!")
        else:
            print("order fix fail!")

    def order_read_by_customer(self, arg):
        sql = "CALL order_read_by_customer('{}')".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("read order fail")
        else:
            print("read order success")
            print(tabulate(result, headers='keys', tablefmt="simple"))


    def order_read_by_restaurant(self, arg):
        sql = "CALL order_read_by_restaurant('{}')".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("read order fail")
        else:
            print("read order success")
            print(tabulate(result, headers='keys', tablefmt="simple"))

    def order_delete_by_customer(self, arg1, arg2):
        sql = "DELETE FROM `order` WHERE customer_id = '{}' AND order_id = {}".format(arg1, arg2)
        result = self.mysql.update(sql)
        if not result:
            print("delete order success")
            return True
        else:
            print("delete order fail")
            return False


    def order_delete_by_restaurant(self, arg1, arg2):
        sql = "DELETE FROM `order` WHERE shop_id = '{}' AND order_id = {} ".format(arg1, arg2)
        result = self.mysql.update(sql)
        if not result:
            print("delete order success")
            return True
        else:
            print("delete order fail")
            return False

    def id_exist(self, arg):
        sql = "SELECT * FROM `order` WHERE order_id = {}".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("not exist this id")
        else:
            return result


# comment table
class Comment():
    def __init__(self):
        self.mysql = Mysql()

    def comment_add_by_customer(self, *args):
        sql = "CALL comment_add_by_customer('{}', {}, '{}', '{}')".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("comment add success!")
            return True
        else:
            print("comment add fail!")
            return False

    def comment_read_by_customer(self, arg):
        sql = "CALL comment_read_by_customer('{}')".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("read comment fail")
        else:
            print("read comment success")
            print(tabulate(result, headers='keys', tablefmt="simple"))


    def comment_read_by_restaurant(self, arg):
        sql = "CALL comment_read_by_restaurant('{}')".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("read comment fail")
        else:
            print("read comment success")
            print(tabulate(result, headers='keys', tablefmt="simple"))

    def comment_edit_by_customer(self, *args):
        sql = "CALL comment_edit_by_customer('{}', {}, '{}', '{}', {})".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("edit comment information success!")
            return True
        else:
            print("edit comment information fail!")
            return False

    def comment_delete_by_customer(self, *args):
        sql = "CALL comment_delete_by_customer('{}', '{}', {})".format(*args)
        result = self.mysql.update(sql)
        if not result:
            print("delete comment success")
            return True
        else:
            print("delete comment fail")
            return False

    def id_exist(self, arg):
        sql = "SELECT * FROM `comment` WHERE comment_id = {}".format(arg)
        result = self.mysql.get_all(sql)
        if not result:
            print("not exist this id")
        else:
            return result


# test
if __name__ == '__main__':
    # user function
    s1 = User()
    # s2 = User()
    # s1.user_register('7818739553', '123123', 'customer')
    # result = s1.user_login('7818739553', '123123')
    # print(result)
    # print({1: 2, 2: 3, 3: 4})
    # print(result[0]['user_type'])
    # s.user_delete('7818739553', '123qwe')
    # s.user_changeid('7818739550', '7818739553', '123123')
    # s1.user_register('7818739550', '123qwe', 'restaurant')
    # s.user_register('7818739551', '123qwe', 'driver')

    # customer function
    c = Customer()
    # c.customer_edit('123qwe', 'wenzhe', 'li', '104qweqwe@qq.com', '7818739553')
    # c.customer_read('7818739553')
    # c.customer_delete('7818739553')

    p = Payment()
    # p.card_add('7818739553', '1111111111111111', 123, '02148')
    # p.card_read('7818739553')
    # p.card_edit('2222222222222222', 122, 12345, '7818739553')
    # p.card_delete('7818739553', '1111111111111111')

    a = Address()
    # a.address_add('7818739553', '100 exchange street', 'malden', 'MA', '02148')
    # a.address_read('7818739553')
    # a.address_edit('101 exchange street', 'boston', 'MA', '02148', '7818739553')
    # a.address_delete('7818739553', '100 exchange street')

    r= Restaurant()
    # r.restaurant_edit('123123', 'mcdonload', 'fast food', '7818739550')
    # r.restaurant_read('7818739550')
    # r.restaurant_delete('7818739550')

    co = Comment()
    # co.comment_add_by_customer('very good', 5, '7818739553', 'mcdonload')
    # co.comment_read_by_customer('mcdonload')
    # co.comment_read_by_restaurant('7818739550')
    # co.comment_edit_by_customer('not well', '3', '7818739553', 'mcdonload', 2)
    # co.comment_delete_by_customer('mcdonload', '7818739553', '2')

    # dish = Dish()
    # dish.dish_add_by_restaurant('A01', 'big mac', 'hamburger', 20, '7818739550')
    # dish.dish_add_by_restaurant('A02', 'fries', 'gao', 10, '7818739550')
    # list = dish.dish_in('laoge')
    # print(list)
    # res = [item[key] for item in list for key in item]
    # print(res)
    # ans = 'dou,loi'.split(',')
    # print(ans)
    # print(set(ans) < set(res))
    # dish.dish_read_by_restaurant('7818739550')
    # dish.dish_edit_by_restaurant('big mac', 'hanmburer', 30, '7818739550')
    # dish.dish_delete('7818739550')

    # o = Order()
    # o.order_add_by_customer('pick up', 'big mac,fries', 'active', '7818739553', 'mcdonload', '100 exchange street', '1111111111111111')
    # o.order_fix()
    # o.order_read_by_customer('1aoge')
    # o.order_read_by_restaurant('7818739550')
    # o.order_delete_by_customer('7818739553', 1)