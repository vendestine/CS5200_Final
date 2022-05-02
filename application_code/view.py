from controller import User, Customer, Restaurant, Payment, Address, Comment, Order, Dish
import pymysql
from setting import DB_CONFIG

# page1: start the application
def page1_start():
    print("Connecting the local Database......")
    try:
        connection = pymysql.connect(**DB_CONFIG)
    except Exception as e:
        print("Error: {}".format(e))
        print("Check setting file again, connect fail!")
    else:
        print("Connection Success!")


# page2: user login in or register and then jump tp customer view or restaurant view
def page2_user():
    print("welcome to the food order system!")
    while True:
        print('''
        option 1: Already hava a account?, log in now.
        option 2: New here? please register first.
        ''')
        answer = input("please choose option number! \n")
        if not answer.isdigit():
            print('illegal input, please use number!')
            continue

        answer = int(answer)
        user1 = User()

        if answer == 1:
            print("user phone number and password to log in")
            phone_number = input("phone number: ")
            password = input("password: ")
            list = [phone_number, password]

            result = user1.user_login(*list)
            if not result:
                continue
            if result[0]['user_type'] == 'customer':
                print('Enter the customer page')
                page3_customer(phone_number, password)
            elif result[0]['user_type'] == 'restaurant':
                print('Enter the restaurant page')
                page4_restaurant(phone_number, password)

        elif answer == 2:
            while True:
                print('Now register!')
                phone_number = input("Enter phone number to register： ")
                if len(phone_number) != 11 or (not phone_number.isdigit()):
                    print("phone number illegal input! (set 11 digit phone number)")
                    continue

                password = input("set password： ")
                if len(password) > 30 or len(password) <= 0:
                    print("password illegal input! (length should be 0 - 30)")
                    continue

                type = input("choose user type in (customer, restaurant)： ")
                if type not in ['customer', 'restaurant']:
                    print('user type illegal input! (only two types available)')
                    continue

                list = [phone_number, password, type]
                result = user1.user_register(*list)
                if result:
                    break
                else:
                    continue
        else:
            print("Input number out of option number, please use correct number to input")

# page3: customer start page
def page3_customer(phone_number, password):
    while True:
        print('This is the customer page')
        print('''
        BASIC:
        option1: View your basic information
        option2: Edit your basic information
        option3: Cancellation account
        option4: Change phone number
        
        ADVANCED:
        option5: Go to the address page for further information
        option6: Go to the payment page for further information
        
        Order:
        option7: Choose Restaurant and go to menu page
        option8: Go to make an order
        option9: Go to the comment page 
        ''')

        answer = input("please choose option number! \n")
        if not answer.isdigit():
            print('illegal input, please use number!')
            continue

        answer = int(answer)
        customer1 = Customer()
        user2 = User()

        if answer == 1:
            print('Display the customer basic information below')
            customer1.customer_read(phone_number)

        elif answer == 2:
            while True:
                print('Now Edit the basic customer information!')

                new_password = input("set new password： ")
                if len(new_password) > 30 or len(new_password) <= 0:
                    print("password illegal input! (length should be 0 - 30)")
                    continue

                first_name = input("Edit the first name： ")
                if len(first_name) > 30 or len(first_name) < 0 or (not first_name.isalpha()):
                    print("set first name illegal! (length should be 0 - 30 and alphabet)")
                    continue

                last_name = input("Edit the last name： ")
                if len(last_name) > 30 or len(last_name) < 0 or (not last_name.isalpha()):
                    print("set last name illegal! (length should be 0 - 30 and alphabet)")
                    continue

                mail = input("Enter the mail： ")
                if len(mail) > 50 or len(mail) < 0:
                    print("set mail illegal! (length should be 0 - 50)")
                    continue

                list = [new_password, first_name, last_name, mail, phone_number]
                result = customer1.customer_edit(*list)
                if result:
                    break
                else:
                    continue

        elif answer == 3:
            while True:
                print('Ready to cancel this account')
                confirm = input("Enter the password again to cancel this account: ")
                if confirm == password:
                    print('Confirm password Success!')
                    result = customer1.customer_delete(phone_number, confirm)
                    if result:
                        break
                    else:
                        continue
                else:
                    print('wrong password!, go back to main page')
                    break

        elif answer == 4:
            while True:
                print("Ready to change phone number")
                new_phone_number = input("Enter new phone number： ")
                if len(new_phone_number) != 11 or (not new_phone_number.isdigit()):
                    print("phone number input illegal! (set 11 digit phone number)")
                    continue

                confirm = input("Enter the password again to change phone number: ")
                if confirm == password:
                    print('Confirm password Success!')
                    list = [new_phone_number, phone_number, confirm]
                    result = user2.user_change_phone(*list)
                    if result:
                        break
                    else:
                        continue
                else:
                    print('wrong password! go back to main page')
                    break

        elif answer == 5:
            page5_address(phone_number, password)
        elif answer == 6:
            page6_payment(phone_number, password)
        elif answer == 7:
            page7_dish_customer_view(phone_number, password)
        elif answer == 8:
            page8_order_customer_view(phone_number, password)
        elif answer == 9:
            page9_comment_customer_view(phone_number, password)
        else:
            print("Input wrong format, please use correct number to input")

# page4: restaurant start page
def page4_restaurant(phone_number, password):
    while True:
        print('This is the restaurant page')
        print('''
        BASIC:
        option1: View your restaurant basic information
        option2: Edit your restaurant basic information
        option3: Cancellation restaurant account
        option4: Change phone number
    
        Order:
        option5: Go to menu page
        option6: Go to order page
        option7: Go to the comment page 
        ''')

        answer = input("please choose option number! \n")
        if not answer.isdigit():
            print('illegal input, please use number!')
            continue

        answer = int(answer)

        restaurant1 = Restaurant()
        user3 = User()

        if answer == 1:
            print('Display the restaurant basic information below')
            restaurant1.restaurant_read(phone_number)

        elif answer == 2:
            while True:
                print('Now Edit the basic restaurant information!')

                new_password = input("set new password： ")
                if len(new_password) > 30 or len(new_password) <= 0:
                    print("password input illegal! (length should be 0 - 30)")
                    continue

                shop_name = input("Enter the shop name： ")
                if len(shop_name) > 30 or len(shop_name) < 0:
                    print("set name illegal! (length should be 0 - 30 length )")
                    continue

                label = input("Enter the label： ")
                if len(label) > 30 or len(label) < 0:
                    print("set label illegal! (length should be 0 - 30)")
                    continue

                list = [new_password, shop_name, label, phone_number]
                result = restaurant1.restaurant_edit(*list)
                if result:
                    break
                else:
                    continue

        elif answer == 3:
            while True:
                print('Ready to cancel this account')
                confirm = input("Enter the password again to cancel this account: ")
                if confirm == password:
                    print('Confirm password Success!')
                    result = restaurant1.restaurant_delete(phone_number, confirm)
                    if result:
                        break
                    else:
                        continue
                else:
                    print('wrong password! go back to main page')
                    break

        elif answer == 4:
            while True:
                print("Ready to change phone number")
                new_phone_number = input("Enter new phone number： ")
                if len(new_phone_number) != 11 or (not new_phone_number.isdigit()):
                    print("phone number illegal! (set 11 digit phone number)")
                    continue

                confirm = input("Enter the password again to change phone number: ")
                if confirm == password:
                    print('Confirm password Success!')
                    list = [new_phone_number, phone_number, confirm]
                    result = user3.user_change_phone(*list)
                    if result:
                        break
                    else:
                        continue
                else:
                    print('wrong password! go back to main page')
                    break

        elif answer == 5:
            page7_dish_shop_view(phone_number, password)
        elif answer == 6:
            page8_order_shop_view(phone_number, password)
        elif answer == 7:
            page9_comment_shop_view(phone_number, password)
        else:
            print("Input wrong format, please use correct number to input")

# page5: customer address information page
def page5_address(phone_number, password):
    while True:
        print('This is the customer address page')
        print('''
        option1: create new address
        option2: Read saved address
        option3: Edit the address
        option4: Delete the address
        option5: Go back to customer page
        ''')

        answer = input("please choose option number! \n")
        if not answer.isdigit():
            print('illegal input, please use number!')
            continue

        answer = int(answer)

        address1 = Address()

        if answer == 1:
            while True:
                print('Now complete the address form to create new address')
                address_id = input("Enter a number for address id：")
                if not address_id.isdigit():
                    print("input illegal! (must input number)")
                    continue

                address_line = input("Enter the specific address： ")
                if len(address_line) > 50 or len(address_line) <= 0:
                    print("address line length illegal! (should be  less than 50)")
                    continue

                city = input('Enter city: ')
                if len(city) > 30 or len(city) <= 0:
                    print("city length illegal! (should be less than 30)")
                    continue

                state = input('Enter state:  (2 char eg: MA)  ')
                if len(state) != 2 or (not state.isalpha()):
                    print("state form wrong! (right eg: MA)")
                    continue

                zip_code = input('Enter zip code: ')
                if len(zip_code) != 5 or (not zip_code.isdigit()):
                    print("zip code form wrong! (eg: 02148)")
                    continue

                list = [address_id, phone_number, address_line, city, state, zip_code]
                result = address1.address_add(*list)
                if result:
                    break
                else:
                    continue

        elif answer == 2:
            print('View  all the saved address below')
            address1.address_read(phone_number)

        elif answer == 3:
            while True:
                print('Now complete the address form to edit address')
                address_id = input("Enter edit address id：")
                res = address1.id_exist(address_id)
                if not res:
                    continue

                address_line = input("Enter new specific address： ")
                if len(address_line) > 50 or len(address_line) <= 0:
                    print("address line length illegal! (should be  less than 50)")
                    continue

                city = input('Enter new city: ')
                if len(city) > 30 or len(city) <= 0:
                    print("city length illegal! (should be  less than 30)")
                    continue

                state = input('Enter new state: ')
                if len(state) != 2 or (not state.isalpha()):
                    print("state form wrong! (eg: MA)")
                    continue

                zip_code = input('Enter new zip code: ')
                if len(zip_code) != 5 or (not zip_code.isdigit()):
                    print("zip code form wrong! (eg: 02148)")
                    continue

                list = [address_line, city, state, zip_code, phone_number, address_id]
                result = address1.address_edit(*list)
                if result:
                    break
                else:
                    continue

        elif answer == 4:
            while True:
                print('Now Prepare to delete an address')
                address_id = input("Enter want delete address id： ")
                res = address1.id_exist(address_id)
                if not res:
                    continue

                result = address1.address_delete(phone_number, address_id)
                if result:
                    break
                else:
                    continue
        elif answer == 5:
            page3_customer(phone_number, password)
        else:
            print("Input wrong format, please use correct number to input")

# page6: customer payment information page
def page6_payment(phone_number, password):
    while True:
        print('This is the customer card page')
        print('''
        option1: Add a new card for payment 
        option2: Read saved cards information
        option3: Edit one card information
        option4: Delete one card
        option5: Go back to customer page
        ''')

        answer = input("please choose option number! \n")
        if not answer.isdigit():
            print('illegal input, please use number!')
            continue

        answer = int(answer)

        card1 = Payment()

        if answer == 1:
            while True:
                print('Now complete the card form to add a new card')
                payment_id = input("Enter a number for this payment id：")
                if not payment_id.isdigit():
                    print("input illegal! (must input number)")
                    continue

                card_number = input("Enter the new card number： ")
                if len(card_number) != 16 or (not card_number.isdigit()):
                    print("card number illegal input! (should be 16 digit)")
                    continue

                cvc = input('Enter the cvc code for this card: ')
                if len(cvc) != 3 or (not cvc.isdigit()):
                    print("city input illegal! (should be 3 digit)")
                    continue

                zip_code = input('Enter zip code: ')
                if len(zip_code) != 5 or (not zip_code.isdigit()):
                    print("zip code form illegal! (eg: 02148)")
                    continue

                list = list = [payment_id, phone_number, card_number, cvc, zip_code]
                result = card1.card_add(*list)
                if result:
                    break
                else:
                    continue

        elif answer == 2:
            print('View  all the saved card information below')
            card1.card_read(phone_number)

        elif answer == 3:
            while True:
                print('Now complete the card form to edit card information')
                payment_id = input("Enter a number for this payment id：")
                res = card1.id_exist(payment_id)
                if not res:
                    continue

                card_number = input("Enter the new card number： ")
                if len(card_number) != 16 or (not card_number.isdigit()):
                    print("card number illegal input! (should be 16 digit)")
                    continue

                cvc = input('Enter the cvc code for this card: ')
                if len(cvc) != 3 or (not cvc.isdigit()):
                    print("city input wrong! (should be 3 digit)")
                    continue

                zip_code = input('Enter zip code: ')
                if len(zip_code) != 5 or (not zip_code.isdigit()):
                    print("zip code form wrong! (eg: 02148)")
                    continue

                list = [card_number, cvc, zip_code, phone_number, payment_id]
                result = card1.card_edit(*list)
                if result:
                    break
                else:
                    continue

        elif answer == 4:
            while True:
                print('Now Prepare to delete a card')
                payment_id = input("Enter want delete payment card id：")
                res = card1.id_exist(payment_id)
                if not res:
                    continue

                result = card1.card_delete(phone_number, payment_id)
                if result:
                    break
                else:
                    continue

        elif answer == 5:
            page3_customer(phone_number, password)
        else:
            print("Input wrong format, please use correct number to input")


# page7 restaurant dish menu page(shop view)
def page7_dish_shop_view(phone_number, password):
    while True:
        print('This is the restaurant menu page')
        print('''
        option1: create new dish
        option2: Read the menu
        option3: Edit one dish
        option4: Delete one dish
        option5: Go back to restaurant basic page
        ''')

        answer = input("please choose option number! \n")
        if not answer.isdigit():
            print('illegal input, please use number!')
            continue

        answer = int(answer)

        dish1 = Dish()

        if answer == 1:
            while True:
                print('Now ready to add a new dish in the menu')
                dish_id = input("set the dish id：")
                if len(dish_id) != 3 or (not dish_id.isalnum()):
                    print("input illegal! (eg: a01)")
                    continue

                dish_name = input("Enter the new dish name： ")
                if len(dish_name) > 30 or len(dish_name) <= 0:
                    print("dish name illegal input! (should be less than 30)")
                    continue

                dish_description = input('Enter the brief description for this dish: ')

                dish_price = input('set the price for this dish: ')
                if len(dish_price) > 3 or (not dish_price.isdigit()):
                    print("price set wrong! (should 0 - 999)")
                    continue

                list = [dish_id, dish_name, dish_description, dish_price, phone_number]
                result = dish1.dish_add_by_restaurant(*list)
                if result:
                    break
                else:
                    continue

        elif answer == 2:
            print('View the menu')
            dish1.dish_read_by_restaurant(phone_number)

        elif answer == 3:
            while True:
                print('Now ready to edit a new dish in the menu')

                dish_id = input("choose the dish id：")
                res = dish1.id_exist(dish_id)
                if not res:
                    continue

                dish_name = input("Enter the edit dish name： ")
                if len(dish_name) > 30 or len(dish_name) <= 0:
                    print("dish name wrong input! (should be less than 30)")
                    continue

                dish_description = input('Edit the brief description for this dish: ')

                dish_price = input('set the edited price for this dish')
                if len(dish_price) > 3 or (not dish_price.isdigit()):
                    print("price set wrong! (should 0 - 999)")
                    continue

                list = [dish_name, dish_description, dish_price, phone_number, dish_id]
                result = dish1.dish_edit_by_restaurant(*list)
                if result:
                    break
                else:
                    continue

        elif answer == 4:
            while True:
                print('Now Prepare to delete a dish in the menu')
                dish_id = input("Enter want delete dish id：")
                res = dish1.id_exist(dish_id)
                if not res:
                    continue

                result = dish1.dish_delete_by_restaurant(phone_number, dish_id)
                if result:
                    break
                else:
                    continue

        elif answer == 5:
            page4_restaurant(phone_number, password)
        else:
            print("Input wrong format, please use correct number to input")

# page7 restaurant dish menu page (customer view)
def page7_dish_customer_view(phone_number, password):
    while True:
        print('This is the restaurant menu page')
        print('''
        You can only view the menu
        option1: Read all the restaurants
        option2: Read one restaurant menu
        option3: Go back to customer page
        ''')

        answer = input("please choose option number! \n")
        if not answer.isdigit():
            print('illegal input, please use number!')
            continue

        answer = int(answer)

        restaurant2 = Restaurant()
        dish2 = Dish()

        if answer == 1:
            restaurant2.restaurant_read_by_user()

        elif answer == 2:
            print('View the restaurant menu')
            while True:
                shop_name = input("Enter the shop name： ")
                res = restaurant2.name_exist(shop_name)
                if not res:
                    continue

                result = dish2.dish_read_by_customer(shop_name)
                break

        elif answer == 3:
            page3_customer(phone_number, password)
        else:
            print("Input wrong format, please use correct number to input")


# page8 order page (customer view)
def page8_order_customer_view(phone_number, password):
    while True:
        print('This is the order page')
        print('''
        option1: Make an order
        option2: Read all the orders
        option3: delete one order
        option4: Go back to customer page
        ''')

        answer = input("please choose option number! \n")
        if not answer.isdigit():
            print('illegal input, please use number!')
            continue

        answer = int(answer)

        restaurant3 = Restaurant()
        address3 = Address()
        card3 = Payment()
        order1 = Order()
        dish6 = Dish()

        if answer == 1:
            while True:
                print('Ready to make an order')
                shop_name = input("Enter the shop name： ")
                res = restaurant3.name_exist(shop_name)
                if not res:
                    continue

                address_line = input("Enter address line：")
                res = address3.line_exist(address_line)
                if not res:
                    continue

                payment_card = input("Enter the payment card number：")
                res = card3.card_exist(payment_card)
                if not res:
                    continue

                order_type = input('Enter type (pick up, deliver):  ')
                if order_type not in ['pick up', 'delivery']:
                    print("illegal input! (only two types)")
                    continue

                order_description = input('Enter the order dish: (eg: a,b,c):  ')
                temp = order_description.split(',')
                dishes = dish6.dish_in(shop_name)
                res = [item[key] for item in dishes for key in item]
                if not (set(temp) <set(res)):
                    print('not exit some dish in the order')
                    continue


                order_status = input('Enter status type (active, cancel):  ')
                if order_status not in ['active', 'cancel']:
                    print('illegal input! (only two types')
                    continue

                list = [order_type, order_description, order_status, phone_number, shop_name, address_line, payment_card]
                result = order1.order_add_by_customer(*list)
                if result:
                    order1.order_fix()
                    break
                else:
                    continue

        elif answer == 2:
            print('view all the orders')
            order1.order_read_by_customer(phone_number)

        elif answer == 3:
            while True:
                order_id = input("Enter the order_id you want to delete： ")
                res = order1.id_exist(order_id)
                if not res:
                    continue

                result = order1.order_delete_by_customer(phone_number, order_id)
                if result:
                    break
                else:
                    continue

        elif answer == 4:
            page3_customer(phone_number, password)

        else:
            print("Input wrong format, please use correct number to input")

# page8 order page (restaurant view)
def page8_order_shop_view(phone_number, password):
    while True:
        print('This is the order page')
        print('''
        you can only read or delete the order
        option1: Read all the orders
        option2: delete one order
        option3: Go back to restaurant page
        ''')

        answer = input("please choose option number! \n")
        if not answer.isdigit():
            print('illegal input, please use number!')
            continue

        answer = int(answer)

        restaurant4 = Restaurant()
        address4 = Address()
        card4 = Payment()
        order2 = Order()


        if answer == 1:
            print('view all the orders')
            order2.order_read_by_restaurant(phone_number)

        elif answer == 2:
            while True:
                order_id = input("Enter the order_id you want to delete： ")
                res = order2.id_exist(order_id)
                if not res:
                    continue

                result = order2.order_delete_by_restaurant(phone_number, order_id)
                if result:
                    break
                else:
                    continue

        elif answer == 3:
            page4_restaurant(phone_number, password)
        else:
            print("Input wrong format, please use correct number to input")

#page9 comment page (customer view)
def page9_comment_customer_view(phone_number, password):
    while True:
        print('This is the restaurant comment page')
        print('''
        option1: find the restaurant to comment
        option2: Make an comment for a restaurant
        option3: Read all the comment this restaurant
        option4: update a comment
        option5: delete a comment
        option6: Go back to customer page
        ''')

        answer = input("please choose option number! \n")
        if not answer.isdigit():
            print('illegal input, please use number!')
            continue

        answer = int(answer)

        restaurant4 = Restaurant()
        comment1 = Comment()

        if answer == 1:
            restaurant4.restaurant_read_by_user()

        elif answer == 2:
            while True:
                print('Ready to make a comment')
                shop_name = input("Enter the shop name： ")
                res = restaurant4.name_exist(shop_name)
                if not res:
                    continue

                content = input("Enter the comment content： ")

                rating = input('rating this restaurant: ')
                if not rating.isdigit():
                    print("wrong input! (rating must be digit)")
                    continue

                list = [content, rating, phone_number, shop_name]
                result = comment1.comment_add_by_customer(*list)
                if result:
                    break
                else:
                    continue

        elif answer == 3:
            while True:
                print('view all the comments for one restaurant')
                shop_name = input("Enter the shop name： ")
                res = restaurant4.name_exist(shop_name)
                if not res:
                    continue

                comment1.comment_read_by_customer(shop_name)
                break

        elif answer == 4:
            while True:
                comment_id = input("Enter the comment id you want to update: ")
                res = comment1.id_exist(comment_id)
                if not res:
                    continue

                shop_name = input("Enter the shop name： ")
                res = restaurant4.name_exist(shop_name)
                if not res:
                    continue

                content = input("Enter the comment content： ")

                rating = input('rating this restaurant: ')
                if not rating.isdigit():
                    print("wrong input! (rating must be digit): ")
                    continue

                list = [content, rating, phone_number, shop_name, comment_id]
                result = comment1.comment_edit_by_customer(*list)
                if result:
                    break
                else:
                    continue

        elif answer == 5:
            while True:
                print('Ready to delete comment')
                comment_id = input("Enter the comment id you want to update: ")
                res = comment1.id_exist(comment_id)
                if not res:
                    continue

                shop_name = input("Enter the shop name： ")
                res = restaurant4.name_exist(shop_name)
                if not res:
                    continue

                list = [shop_name, phone_number, comment_id]
                result = comment1.comment_delete_by_customer(*list)
                if result:
                    break
                else:
                    continue

        elif answer == 6:
            page3_customer(phone_number, password)

        else:
            print("Input wrong format, please use correct number to input")

# page9 comment page (restaurant view)
def page9_comment_shop_view(phone_number, password):
    while True:
        print('This is the restaurant comment page')
        print('''
        option1: Read the comment in your restaurant
        option2: Go back to restaurant page
        ''')

        answer = input("please choose option number! \n")
        if not answer.isdigit():
            print('illegal input, please use number!')
            continue

        answer = int(answer)
        comment2 = Comment()

        if answer == 1:
            print('view the comment')
            comment2.comment_read_by_restaurant(phone_number)

        elif answer == 2:
            page4_restaurant(phone_number, password)
        else:
            print("Input wrong format, please use correct number to input")

if __name__ == '__main__':
    page1_start()
    page2_user()