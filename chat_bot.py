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

def get_bot_response_meal(response):

    response_chinese_food = ["orange chicken", "fried rice", "szechuan noodles"]
    response_mexican_food = ["tacos", "burrito", "enchilada"]
    response_italian_food = ["pizza", "pasta", "risotto"]

    response_coffee = ["cappuccino", "latte", "flat white", "espresso"]
    response_soda =  ["sprite", "coke", "dr.pepper"]
    response_boba_tea = ["brown sugar milk tea", "oolong milk tea", "matcha milk tea"]
    response_smoothie = ["banana strawberry smoothie", "watermelon smoothie", "mango smoothie"]

    if response == "Chinese food":
        return choice(response_chinese_food)
    elif response == "Mexican food":
        return choice(response_mexican_food)
    elif response == "Italian food":
        return choice(response_italian_food)
    elif response == "coffee":
        return choice(response_coffee)
    elif response == "soda":
        return choice(response_soda)
    elif response == "boba tea":
        return choice(response_boba_tea)
    elif response == "smoothie":
        return choice(response_smoothie)
    else:
        return


print("Welcome to the meal helper bot! I'll help suggest some food or drink for you.")

while True:
    user_response = input("Do you feel like getting a meal, drink, or dessert?")

    if user_response == "done":
        exit()
    
    response = get_bot_response(user_response)
    print(response)
    
    type_of_food = input(f"Would you like a suggestion on what kind of {response} you would like? If you would like to exit now, please enter done.")

    if type_of_food == "yes":
        response2 = get_bot_response_meal(response)
        print(response2)

