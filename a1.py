"""
CSSE1001 Assignment 1
Semester 1, 2023
"""

# Fill these in with your details
__author__ = "Justin Teng"
__email__ = "justint3ng@gmail.com"
__date__ = "24/03/2023"

import constants
from constants import *

# Write your functions here
def num_hours() -> float:
    hours = 27.0
    return hours

def get_recipe_name(recipe):
    recipe_name = recipe[0]
    return recipe_name

def parse_ingredient(raw_ingredient_detail):
    details_amount, measure, ingredient = raw_ingredient_detail
    new_raw_ingredient_details = (float(details_amount), measure, ingredient)
    return new_raw_ingredient_details

def create_recipe():
    recipe_name = input("Please enter the recipe name: ")
    ingredients = []
    while True:
        ingredient = input("Please enter an ingredient (leave blank to end): ")
        if ingredient == "":
            break
        ingredients.append(ingredient)
    recipe = (recipe_name + ", " + ingredients)
    return recipe

def recipe_ingredients(recipe: tuple[str, str]) -> tuple[tuple[float, str, str]]:
    name, ingredients_string = recipe
    ingredients = []
    for ingredient_string in ingredients_string.split(','):
        amount_string, measure, name = ingredient_string.strip().split()
        amount = float(amount_string)
        ingredients.append((amount,measure,name))
    return tuple(ingredients)

def add_recipe(new_recipe, recipes):
    recipes.append(new_recipe)
    return recipes

def find_recipe(recipe_name: str, recipes_list: list[tuple[str, str]]) -> tuple[str, str]:
    for recipe in recipes_list:
        if recipe[0] == recipe_name:
            return recipe
        else:
            return None

def remove_recipe(recipe_name, recipes) -> None:
    for recipe in recipes:
        if recipe_name in recipe:
            recipes.remove(recipe)
            print("Recipe removed")
            return recipes

    else:
        print("There is no such recipe")

def get_ingredient_amount(ingredient: str, recipes_list: tuple[str, str]) -> tuple[float, str]:
    recipe_name = input("What is the recipe: ")
    if recipe_name in recipes_list:
        if ingredient in recipes_list[recipe_name]['ingredients']:
            amount = recipes_list[recipe_name]['ingredients'][ingredient]
            unit = recipes_list[recipe_name]['units'][ingredient]
            return amount, unit
        else:
            print("Ingredients not in the recipe")

    else:
        print("Recipe not found in the list")

def add_to_shopping_list(ingredients_details: tuple[float, str, str], shopping_list: list[tuple[float, str, str] | None]) -> None:
    amount, unit, ingredient = ingredients_details
    for i, item in enumerate(shopping_list):
        if item is not None and item[2] == ingredient:
            current_amount = item[0]
            new_amount = current_amount + amount
            shopping_list[i] = (new_amount, unit, ingredient)
            break

        else:
            shopping_list.append((amount, unit, ingredient))

def remove_from_shopping_list(ingredient_name: str, amount: float, shopping_list: list) -> None:
    for i, item in enumerate(shopping_list):
        if item is not None and item[2] == ingredient_name:
            current_amount = item[0]
            new_amount = current_amount - amount
            if new_amount <= 0:
                shopping_list[i] = None

            else:
                shopping_list[i] = (new_amount, item[1], ingredient_name)
            break

        else:
            print(f"{ingredient_name} not found in the shopping list")

def generate_shopping_list(recipes: list[tuple[str, str]]) -> list[tuple[float, str, str]]:
    shopping_list = []
    for recipe in recipes:
        for ingredient in recipe[1].split(','):
            ingredient_parts = ingredient.strip().split(' ')
            amount = float(ingredient_parts[0])
            measure = ingredient_parts[1]
            ingredient_name = ' '.join(ingredient_parts[2:])
            for i, item in enumerate(shopping_list):
                if item is not None and item[2] == ingredient_name and item[1] == measure:
                    current_amount = item[0]
                    new_amount = current_amount + amount
                    shopping_list[i] = (new_amount, measure, ingredient_name)
                    break
            else:
                shopping_list.append((amount, measure, ingredient_name))
    return shopping_list

def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
    shopping_list.sort(key=lambda x: x[2])
    max_amount_len = max(len(str(row[0])) for row in shopping_list)
    max_measure_len = max(len(row[1]) for row in shopping_list)
    max_name_len = max(len(row[2]) for row in shopping_list)

    for row in shopping_list:
        print(f"| {row[0]:>{max_amount_len}} | {row[1]:>{max_measure_len}} | {row[2]:<{max_name_len}} |")

def sanitise_command(command: str) -> str:
    command = command.lower().strip()

    command = ''.join(c for c in command if not c.isdigit())

    return command

def main():
# Write the rest of your code here

if __name__ == "__main__":
    main()
    while True:
        command = input("Please enter a command: ").lower()

        if command == "h":
            print(constants.HELP_TEXT)
        elif command == "mkrec":
            new_recipe = create_recipe()
        elif command.startswith("add"):
            recipe_collection = add_recipe(new_recipe, recipe_collection)
        elif command.startswith("rm"):
            recipe_name = input("Which recipe would you like to remove: ")
            recipe = remove_recipe(recipe_name, recipe_collection)
        elif command.startswith("rm -i"):
            remove_from_shopping_list()
        elif command.startswith("ls"):
            add_to_shopping_list()
        elif command.startswith("ls -a"):
            generate_shopping_list()
        elif command.startswith("ls -s"):
            display_ingredients()
        elif command == "g":
            generate_shopping_list()
        elif command == "q":
            print("Thank you for using the program")
            break







