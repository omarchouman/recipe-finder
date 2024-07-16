import streamlit as st
import json

st.title('Recipe Finder')
st.write('Enter ingredients to find recipes')

ingredients = st.text_input('Ingredients (comma-separated)', 'tomato, cheese, basil')


def load_recipes():
    with open('recipes.json', 'r') as file:
        recipes = json.load(file)
    return recipes


def get_recipes(ingredients, recipes):
    ingredient_list = [ingredient.strip().lower() for ingredient in ingredients.split(',')]
    filtered_recipes = [recipe for recipe in recipes if all(ingredient in recipe['ingredients'] for ingredient in ingredient_list)]
    return filtered_recipes


recipes = load_recipes()

if ingredients:
    matching_recipes = get_recipes(ingredients, recipes)
    if matching_recipes:
        for recipe in matching_recipes:
            st.write(f"**{recipe['name']}**")
            st.write(f"Ingredients: {recipe['ingredients']}")
    else:
        st.write('No recipes found.')
