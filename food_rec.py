# -*- coding: utf-8 -*-
"""Food_Rec.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UorCHW54DJnUjWCAc36rM8-MvbEDWqLE
"""

!pip install sentence-transformers

# Cell 2: Imports
import numpy as np
from typing import List, Dict
from dataclasses import dataclass
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import requests

# Cell 3: Define Recipe class
@dataclass
class Recipe:
    name: str
    ingredients: List[str]
    instructions: str
    cuisine: str
    difficulty: str

    def to_text(self) -> str:
        """Convert recipe to searchable text format"""
        return f"""
        Recipe: {self.name}
        Cuisine: {self.cuisine}
        Difficulty: {self.difficulty}
        Ingredients: {', '.join(self.ingredients)}
        Instructions: {self.instructions}
        """

# Cell 4: Define RecipeRecommender class
class RecipeRecommender:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.embedding_model = SentenceTransformer(model_name)
        self.recipes: List[Recipe] = []
        self.embeddings = None

    def add_recipes(self, recipes: List[Recipe]):
        """Add recipes and compute their embeddings"""
        self.recipes = recipes
        # Convert recipes to text format for embedding
        texts = [recipe.to_text() for recipe in recipes]
        self.embeddings = self.embedding_model.encode(texts)

    def find_similar_recipes(self, query: str, top_k: int = 3) -> List[Recipe]:
        """Find recipes most similar to the query"""
        query_embedding = self.embedding_model.encode([query])[0]
        similarities = cosine_similarity([query_embedding], self.embeddings)[0]
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        return [self.recipes[i] for i in top_indices]

# Cell 5: Define recipe fetching function
def fetch_recipes_from_api() -> List[Recipe]:
    """Fetch recipes from TheMealDB API"""
    recipes = []
    base_url = "https://www.themealdb.com/api/json/v1/1/search.php?s="

       # Fetch a few common dishes
    search_terms = ["chicken", "pasta", "fish", "rice", "soup"]

    for term in search_terms:
        response = requests.get(base_url + term)
        data = response.json()

        if not data['meals']:
            continue

        for meal in data['meals']:
            # Extract ingredients
            ingredients = []
            for i in range(1, 21):
                ingredient = meal.get(f'strIngredient{i}')
                if ingredient and ingredient.strip():
                    ingredients.append(ingredient)

            recipe = Recipe(
                name=meal['strMeal'],
                ingredients=ingredients,
                instructions=meal['strInstructions'],
                cuisine=meal.get('strArea', 'Unknown'),
                difficulty="Medium"  # API doesn't provide difficulty
            )
            recipes.append(recipe)

    return recipes

# Cell 6: Initialize and test the recommender
# Initialize recommender
recommender = RecipeRecommender()

# Fetch and add recipes
print("Fetching recipes...")
recipes = fetch_recipes_from_api()
recommender.add_recipes(recipes)
print(f"Loaded {len(recipes)} recipes")

# Cell 7: Function to search for recipes
def search_recipes(query: str, recommender: RecipeRecommender):
    print(f"\nSearching for: {query}")
    print("\nRecommended Recipes:")
    for recipe in recommender.find_similar_recipes(query):
        print(f"\n- {recipe.name} ({recipe.cuisine} cuisine)")
        print(f"  Ingredients: {', '.join(recipe.ingredients)}")
        print(f"  Instructions: {recipe.instructions[:200]}...")

# Cell 8: Example usage
# Test the recommender with a sample query
search_recipes("spicy chicken dinner", recommender)