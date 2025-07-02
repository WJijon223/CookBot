import requests
import json
import os

# Function to get ingredients from the user (calls the API)
def get_response_by_ingredients(items):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ",".join(items),
        "number": 5,
        "apiKey": os.environ.get("SPOONACULAR_API_KEY"),
        "ignorePantry" : True
    }

    if not params["apiKey"]:
        print("API key is not set. Please set the SPOONACULAR_API_KEY environment variable and restart program.")
        return

    response = requests.get(url, params=params)
    return response.json()

# Function to get recipe index from response by name
def recipe_index_by_name(response, name):
    for i, recipe in enumerate(response):
        if recipe['title'].lower() == name.lower():
            return i
    return -1

# Function to print missing ingredients for a recipe by index
def print_missing_ingredients(response, index):
    for ingredient in response[index]['missedIngredients']:
        print(f"- {ingredient['name']} ({ingredient['amount']} {ingredient['unit']})")
    print("\n")

# Returns a list of recipe names from the response
def get_dish_names(response):
    return [recipe['title'] for recipe in response]

# Function to print dish names
def print_dish_names(dish_list):
    print("Here are some dish ideas based on your ingredients:")
    for i, dish in enumerate(dish_list):
        print(f"{i + 1}. {dish}")
    print("\n")