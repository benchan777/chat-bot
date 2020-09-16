from random import choice

def get_bot_response(user_response):

    response_meal = ["Chinese food", "Mexican food", "Italian food"]
    response_drink = ["coffee", "soda", "boba tea", "smoothie"]
    response_dessert =  ["ice cream", "cake", "cookie"]

    if user_response == "food" or user_response == "meal":
        return choice(response_meal)
    elif user_response == "drink":
        return choice(response_drink)
    elif user_response == "dessert":
        return choice(response_dessert)
    else:
        return "I don't know what to do with that information."

def get_bot_response_meal(bot_response):

    response_chinese_food = ["orange chicken", "fried rice", "szechuan noodles"]
    response_mexican_food = ["tacos", "burrito", "enchilada"]
    response_italian_food = ["pizza", "pasta", "risotto"]

    if bot_response == "Chinese food":
        return choice(response_chinese_food)
    elif bot_response == "Mexican food":
        return choice(response_mexican_food)
    elif bot_response == "Italian food":
        return choice(response_italian_food)
    else:
        return

def get_bot_response_drink(bot_response):

    response_coffee = ["cappuccino", "latte", "flat white", "espresso"]
    response_soda =  ["sprite", "coke", "dr.pepper"]
    response_boba_tea = ["brown sugar milk tea", "oolong milk tea", "matcha milk tea"]
    response_smoothie = ["banana strawberry smoothie", "watermelon smoothie", "mango smoothie"]

    if bot_response == "coffee":
        return choice(response_coffee)
    elif bot_response == "soda":
        return choice(response_soda)
    elif bot_response == "boba tea":
        return choice(response_boba_tea)
    elif bot_response == "smoothie":
        return choice(response_smoothie)
    else:
        return

def get_bot_response_dessert(bot_response):

    response_ice_cream = ["coffee ice cream", "cookies and cream", "strawberry ice cream"]
    response_cake = ["carrot cake", "red velvet cake", "pound cake"]
    response_cookie = ["chocolate chip", "snickerdoodle", "sugar cookie"]

    if bot_response == "ice cream":
        return choice(response_ice_cream)
    elif bot_response == "cake":
        return choice(response_cake)
    elif bot_response == "cookie":
        return choice(response_cookie)
    else:
        return

print("Welcome to the meal helper bot! I'll help suggest some food, drinks, or desserts for you.")

while True:
    user_response = input("Do you feel like getting a meal, drink, or dessert? ")

    bot_response = get_bot_response(user_response)
    print(bot_response)

    more_suggestions = input(f"Would you like a suggestion on what kind of {bot_response} you would like? If you would like to exit now, please enter done. If you would like another type of meal selection, please enter no. ")

    if more_suggestions == "done":
        exit()

    if more_suggestions == "yes":
        break

while True:
    
    if user_response == "meal":
        response = get_bot_response_meal(bot_response)
        print(response)
    
    if user_response == "drink":
        response = get_bot_response_drink(bot_response)
        print(response)

    if user_response == "dessert":
        response = get_bot_response_dessert(bot_response)
        print(response)

    more_suggestions_2 = input(f"Would you like another {bot_response} suggestion? ")

    if more_suggestions_2 == "no":
        break