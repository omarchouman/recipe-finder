"""
This module provides a Streamlit app for finding recipes based on provided ingredients.
"""

import json
import streamlit as st


st.title('Recipe Finder')
st.write('Enter ingredients to find recipes')

ingredients_input = st.text_input('Ingredients (comma-separated)', 'tomato, cheese, basil')

def load_recipes():
    """
    Load recipes from a JSON file.
    
    Returns:
        list: A list of recipes loaded from the JSON file.
    """
    with open('recipes.json', 'r', encoding='utf-8') as file:
        recipes = json.load(file)
    return recipes

def get_recipes(ingredients, recipe_list):
    """
    Find recipes that include all the specified ingredients.
    
    Args:
        ingredients (str): A comma-separated string of ingredients.
        recipe_list (list): A list of recipes.
    
    Returns:
        list: A list of recipes that contain all the specified ingredients.
    """
    ingredient_list = [ingredient.strip().lower() for ingredient in ingredients.split(',')]
    filtered_recipes = [
        recipe for recipe in recipe_list
        if all(ingredient in recipe['ingredients'] for ingredient in ingredient_list)
    ]
    return filtered_recipes

recipes_data = load_recipes()

if ingredients_input:
    matching_recipes = get_recipes(ingredients_input, recipes_data)
    if matching_recipes:
        for recipe in matching_recipes:
            st.write(f"**{recipe['name']}**")
            st.write(f"Ingredients: {recipe['ingredients']}")
    else:
        st.write('No recipes found.')
