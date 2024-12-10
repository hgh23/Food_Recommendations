# Food Recipe Recommender

A sophisticated recipe recommendation system that uses natural language processing and text embeddings to find recipes matching your preferences. The system leverages the power of sentence transformers for semantic search and integrates with TheMealDB API for a diverse recipe database.

## 🌟 Features

- **Natural Language Search**: Find recipes using everyday language (e.g., "spicy vegetarian dinner" or "quick healthy breakfast")
- **Semantic Understanding**: Uses advanced NLP to understand the meaning behind your queries
- **Smart Recommendations**: Suggests recipes based on ingredients, cooking style, cuisine type, and more
- **Real-Time Recipe Data**: Integration with TheMealDB API for up-to-date recipe information
- **Detailed Recipe Information**: Get complete ingredients lists, cooking instructions, and cuisine types

## 📋 Requirements

- Python 3.7+
- sentence-transformers
- numpy
- scikit-learn
- requests
- dataclasses

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/hgh23/Food_Recommendations.git
cd food-recommender
```

2. Install required packages:
```bash
pip install sentence-transformers numpy scikit-learn requests
```

## 💻 Usage

### Google Colab
1. Open the provided notebook in Google Colab
2. Run all cells in sequence
3. Use the search function to find recipes:
```python
search_recipes("spicy chicken dinner", recommender)
```

### Local Python Environment
```python
from food import RecipeRecommender, fetch_recipes_from_api

# Initialize the recommender
recommender = RecipeRecommender()

# Load recipes
recipes = fetch_recipes_from_api()
recommender.add_recipes(recipes)

# Find recipes
results = recommender.find_similar_recipes("healthy vegetarian pasta")
```

## 🏗️ Project Structure

```
food-recommender/
│
├── food.py              # Main implementation file
├── requirements.txt     # Package dependencies
└── README.md           # Project documentation
```

## 🔧 Core Components

### Recipe Class
- Stores recipe information including name, ingredients, instructions, cuisine, and difficulty
- Provides text conversion for embedding generation

### RecipeRecommender Class
- Manages recipe database and embeddings
- Performs semantic search using sentence transformers
- Returns similar recipes based on natural language queries

## 🌟 Example Queries

```python
# Find healthy breakfast options
search_recipes("healthy breakfast with fruits", recommender)

# Look for dinner ideas
search_recipes("easy italian dinner recipes", recommender)

# Find specific cuisine
search_recipes("authentic mexican dishes", recommender)
```

## 🔍 How It Works

1. **Text Embedding**: Converts recipes and queries into high-dimensional vectors using sentence transformers
2. **Semantic Matching**: Uses cosine similarity to find recipes that best match the query's meaning
3. **Ranking**: Returns the top-k most similar recipes

## 🔄 API Integration

The system integrates with TheMealDB API to fetch recipe data:
- Automatically retrieves recipes for common categories
- Extracts detailed information including ingredients and instructions
- Handles API response parsing and data structuring

## 🛠️ Customization

### Modify Search Parameters
```python
# Change number of results
results = recommender.find_similar_recipes(query, top_k=5)

# Use different embedding model
recommender = RecipeRecommender(model_name="different-model-name")
```

## 📝 Future Improvements

- Add support for dietary restrictions and allergies
- Implement recipe rating and user feedback
- Add more recipe sources and APIs
- Include preparation time and difficulty filtering
- Add support for image-based recipe search

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- TheMealDB for providing the recipe API
- Sentence Transformers library for text embeddings
- scikit-learn for similarity calculations