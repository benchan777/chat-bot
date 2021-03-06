from random import choice

# This function will randomly choose an option inside the meal, drink, or dessert list depending on which option the user inputs.
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
        return "Please only enter food, meal, drink, or dessert."

# This function will randomly choose different types of Chinese, Mexican, or Italian food if the user says they want food.
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

# This function will randomly choose different types of coffee, soda, boba tea, or smoothies if the user says they want a drink. 
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

# This function will randomly choose different types of ice crea, cake, or cookies if the user says they want a dessert.
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

    # Asks the user to input if they want a meal, drink, or dessert.
    user_response = input("Do you feel like getting a meal, drink, or dessert? ")

    # Calls the get_bot_response function and then prints the result.
    bot_response = get_bot_response(user_response)
    print(bot_response)

    # Checks if the user entered one of the specified responses. If they did not, this if statement will loop back to the beginning of the while loop and prompt for another input.
    if user_response != "meal" and user_response != "drink" and user_response != "dessert" and user_response != "food":
       continue

    # Asks the user what they would like to do next. If the user enters no, it will go back to the beginning of the while loop and suggest another meal.
    print("If you would like to exit now, please enter done. If you would like another type of meal selection, please enter no.")
    more_suggestions = input(f"Would you like a suggestion on what kind of {bot_response} you would like? ")

    # If the user enters done, the program will terminate.
    if more_suggestions == "done":
        exit()

    # If the user enters yes, the current loop will be exited and the program will continue onto the next loop.
    if more_suggestions == "yes":
        break

while True:
    
    # Calls the function to suggest a random meal if the user inputs meal.
    if user_response == "meal":
        response = get_bot_response_meal(bot_response)
        print(response)
    
    # Calls the function to suggest a random drink if the user inputs drink.
    elif user_response == "drink":
        response = get_bot_response_drink(bot_response)
        print(response)

    # Calls the function to suggest a random dessert if the user inputs dessert.
    else:
        response = get_bot_response_dessert(bot_response)
        print(response)

    # Asks the user if they would like another suggestion. If yes is entered, the while statement will loop again.
    print("Enter no if you don't want any more suggestions.")
    more_suggestions_2 = input(f"Would you like another {bot_response} suggestion? ")

    # If the user enters no or done, the program will exit this while loop and the entire program will be finished running.
    if more_suggestions_2 == "no" or more_suggestions_2 == "done":
        break
