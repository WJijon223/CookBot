from api import recipe_api

def main_menu():
    print("Welcome to CookBot!")
    print("1. Add ingredients")
    print("2. View ingredients")
    print("3. Search for a recipe")
    print("4. Generate step-by-step instructions with AI")
    print("5. View saved recipes")
    print("6. Exit\n")

    user_choice = int(input("Please select an option (1-5): "))
    while user_choice < 1 or user_choice > 5:
        print("Invalid choice. Please select a number between 1 and 5.")
        user_choice = int(input("Please select an option (1-5): "))
    return user_choice

def ingredients_menu(ingredients_list):
    if len(ingredients_list) > 0:
        print("You already have ingredients saved. Would you like to clear them or add more?")
        clear_choice = input("Please enter your choice (1 or 2): ").strip().lower()

        while clear_choice not in ['1', '2']:
            print("Invalid choice. Please enter 1 to clear or 2 to add more ingredients.")
            clear_choice = input("Please enter your choice: ").strip().lower()
        
        if clear_choice == '1':
            ingredients_list.clear()
            print("All ingredients cleared.")

    num_ingredients = int(input("Enter number of ingredients: "))
    for _ in range(num_ingredients):
        ingredient = input("Enter ingredient: ")
        ingredients_list.append(ingredient)

    print("\nIngredients added successfully! Returning to main menu...\n")

def display_ingredients(ingredients_list):
    if not ingredients_list:
        print("No ingredients added yet.")
    else:
        print("Current ingredients:")
        for ingredient in ingredients_list:
            print(f"- {ingredient}")
    print("\nReturning to main menu...\n")

def search_recipe(ingredients_list, data):
    if data:
        print("You already have a recipe search in progess. Would you like to learn more about it or start a new search?")
        choice = input("Please enter your choice (1 to learn more, 2 to start a new search): ").strip().lower()

        while choice not in ['1', '2']:
            print("Invalid choice. Please enter 1 to learn more or 2 to start a new search.")
            choice = input("Please enter your choice: ").strip().lower()

        if choice == '2':
            data.clear()
            data = recipe_api.get_response_by_ingredients(ingredients_list)
    else:
        data = recipe_api.get_response_by_ingredients(ingredients_list)
    
    dish_names = recipe_api.get_dish_names(data)
    recipe_api.print_dish_names(dish_names)

    choosing = True
    while choosing:
        user_choice = input("Which dish would you like to learn more about? Please enter the name: ").strip()
        index = recipe_api.recipe_index_by_name(data, user_choice)

        while index == -1:
            print("Dish not found. Please try again.")
            user_choice = input("Which dish would you like to learn more about? Please enter the name: ").strip()
            index = recipe_api.recipe_index_by_name(data, user_choice)

        if data[index]["missedIngredients"]:
            print("You are missing the following ingredients for this recipe:")
            recipe_api.print_missing_ingredients(data, index)
        
        keep_choosing = input("Would you like to choose another dish? (yes/no): ").strip().lower()
        if keep_choosing != 'yes':
            choosing = False
            print("Returning to main menu...\n")
        elif keep_choosing == 'yes':
            print("Please choose another dish.\n")
        else:
            print("Invalid input. Returning to main menu...\n")
            choosing = False

def main():
    ingredients_list = []
    response_data = {}

    while True:
        choice = main_menu()
        if choice == 1:
            ingredients_menu(ingredients_list)
        elif choice == 2:
            display_ingredients(ingredients_list)
        elif choice == 3:
            search_recipe(ingredients_list, response_data)
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        else:
            print("Thank you for using CookBot! Goodbye!")
            break

if __name__ == "__main__":
    main()