# Calorie Counter
database = 'calories.txt' # Foods with Calories
def foods():
    while True:
        foods_input = input("What foods have you eaten? Enter food items separated by commas: ")
        food_list = [item.strip() for item in foods.split(',') if item.strip()]

        if food_list:
            break
        else:
            print("Invalid, Did you put it correctly? It needs atleast one food item")
    print("Food items entered:", food_list)
# TODO: implement calorie database and count the food items in the list
def caloriecounter(food_list, foods_input, database):