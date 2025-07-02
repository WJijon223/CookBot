from api import recipe_api

def main_menu():
    print("\nWelcome to CookBot!")
    print("1. Add ingredients")
    print("2. View ingredients")
    print("3. Search for a recipe")
    print("4. Generate step-by-step instructions with AI")
    print("5. View saved recipes")
    print("6. Exit\n")

    user_choice = input("Please select an option (1-6): ")
    while (not user_choice.isdigit()) or (int(user_choice) < 1 or int(user_choice)) > 6:
        print("Invalid choice. Please select a number between 1 and 6.")
        user_choice = input("Please select an option (1-6): ")
    return int(user_choice)

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

    num_ingredients = input("Enter number of ingredients: ").strip()
    while not num_ingredients.isdigit() or int(num_ingredients) <= 0:
        print("Invalid input. Please enter a positive integer.")
        num_ingredients = input("Enter number of ingredients: ").strip()

    for _ in range(int(num_ingredients)):
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
    if not ingredients_list:
        print("No ingredients added yet. Please add ingredients first.")
        return
    
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
    if not dish_names:
        print("No recipes found for the given ingredients. Please try adding different ingredients.")
        return
    recipe_api.print_dish_names(dish_names)

    choosing = True
    while choosing:
        index = input("Which dish would you like to learn more about? Please enter the number (0 to Return to Main Menu): ").strip()
        while (not index.isdigit()) and (int(index) < 0 or int(index) > len(index)):
            print(f"Invalid choice. Please enter a number between 1 and {len(dish_names)}.")
            index = input("Which dish would you like to learn more about? Please enter the number (0 to Return to Main Menu): ").strip()
        if index == '0':
            print("Returning to main menu...\n")
            return
        index = int(index) - 1

        if data[index]["missedIngredients"]:
            print(f"You are missing the following ingredients for {data[index]['title']}:")
            recipe_api.print_missing_ingredients(data, index)
        
        keep_choosing = input("Would you like to learn about another dish?? (yes/no): ").strip().lower()
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