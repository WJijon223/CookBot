import unittest
from unittest.mock import patch
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api import recipe_api


class TestRecipeAPI(unittest.TestCase):
    @patch('api.recipe_api.requests.get')
    def test_get_response_by_ingredients(self, mock_get):
        # Setting up mock return value
        mock_response = mock_get.return_value
        mock_response.json.return_value = [
            {"id": 1, "title" : "Test Recipe 1"},
            {"id": 2, "title" : "Test Recipe 2"},
        ]

        # Calling the function with a sample ingredient list
        ingredients = ["tomato", "cheese"]
        result = recipe_api.get_response_by_ingredients(ingredients)

        # Assertions
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['title'], "Test Recipe 1")

    def test_recipe_index_by_name(self):
        response_data = [
            {"id": 1, "title": "Test Recipe 1"},
            {"id": 2, "title": "Test Recipe 2"},
        ]
        self.assertEqual(recipe_api.recipe_index_by_name(response_data, "Test Recipe 1"), 0)
        self.assertEqual(recipe_api.recipe_index_by_name(response_data, "Test Recipe 2"), 1)
        self.assertEqual(recipe_api.recipe_index_by_name(response_data, "Nonexistent Recipe"), -1)

    @patch('builtins.print')
    def test_print_missing_ingredients(self, mock_print):
        mock_response = [
            {"missedIngredients": [
                {"name": "tomato", "amount": 2, "unit": "cups"},
                {"name": "cheese", "amount": 1, "unit": "cup"}
            ]}
        ]

        recipe_api.print_missing_ingredients(mock_response, 0)

        mock_print.assert_any_call("- tomato (2 cups)")
        mock_print.assert_any_call("- cheese (1 cup)")


    def test_get_dish_names(self):
        response_1 = [
            {"id": 1, "title": "Test Recipe 1"},
            {"id": 2, "title": "Test Recipe 2"},
        ]
        response_2 = []

        self.assertEqual(recipe_api.get_dish_names(response_1), ["Test Recipe 1", "Test Recipe 2"])
        self.assertEqual(recipe_api.get_dish_names(response_2), [])

    @patch('builtins.print')
    def test_print_dish_names(self, mock_print):
        dish_list = ["Dish 1", "Dish 2", "Dish 3"]
        recipe_api.print_dish_names(dish_list)

        # Check if print was called with the correct output
        mock_print.assert_any_call("Here are some dish ideas based on your ingredients:")
        mock_print.assert_any_call("1. Dish 1")
        mock_print.assert_any_call("2. Dish 2")
        mock_print.assert_any_call("3. Dish 3")
        mock_print.assert_any_call("\n")

if __name__ == '__main__':
    unittest.main()