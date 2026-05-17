import os
from fastapi import FastAPI, Request
from dotenv import load_dotenv
import google.generativeai as genai



load_dotenv()

app = FastAPI()

OWNER_NAME = os.getenv("USER_NAME", "Home Owner")
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

for model in genai.list_models():
    print(model.name, model.supported_generation_methods)


def read_inventory():
    try:
        with open("inventory.txt", "r") as file:
            items = file.read().splitlines()
        return items
    except FileNotFoundError:
        return ["No inventory file found"]


def get_available_recipes(inventory):
    inventory_set = set(item.lower().strip() for item in inventory)

    recipes = [
        {
            "name": "Cheese Omelet",
            "category": "dairy",
            "required_items": {"eggs", "cheese", "milk"},
            "time_minutes": 10,
            "difficulty": "Easy",
            "nutrition": {
                "calories": 330,
                "protein": 24,
                "carbs": 5,
                "fat": 23
            },
            "image": "https://images.unsplash.com/photo-1525351484163-7529414344d8",
            "steps": [
                "Beat eggs with a little milk.",
                "Heat a pan with butter.",
                "Pour the eggs into the pan.",
                "Add cheese and cook until soft."
            ],
            "sauces": ["Hot sauce", "Garlic mayo", "Ketchup"],
            "tip": "Cook on low heat so the omelet stays soft."
        },
        {
            "name": "Teriyaki Chicken Rice Bowl",
            "category": "meat",
            "required_items": {"chicken", "rice", "teriyaki"},
            "time_minutes": 35,
            "difficulty": "Medium",
            "nutrition": {
                "calories": 620,
                "protein": 42,
                "carbs": 72,
                "fat": 14
            },
            "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b",
            "steps": [
                "Cook the rice.",
                "Cut the chicken into small pieces.",
                "Cook the chicken in a hot pan.",
                "Add teriyaki sauce and serve over rice."
            ],
            "sauces": ["Teriyaki", "Soy sauce", "Sweet chili"],
            "tip": "Let the sauce reduce for 2 minutes for stronger flavor."
        },
        {
            "name": "Creamy Mushroom Pasta",
            "category": "dairy",
            "required_items": {"pasta", "mushrooms", "milk", "cheese"},
            "time_minutes": 25,
            "difficulty": "Medium",
            "nutrition": {
                "calories": 560,
                "protein": 22,
                "carbs": 78,
                "fat": 18
            },
            "image": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9",
            "steps": [
                "Boil the pasta.",
                "Cook mushrooms with butter and garlic.",
                "Add milk and cheese.",
                "Mix with pasta until creamy."
            ],
            "sauces": ["Garlic cream", "Parmesan", "Chili oil"],
            "tip": "Use pasta water to make the sauce smoother."
        },
        {
            "name": "Tuna Corn Salad",
            "category": "pareve",
            "required_items": {"tuna", "corn", "lettuce", "cucumber", "tomato"},
            "time_minutes": 12,
            "difficulty": "Easy",
            "nutrition": {
                "calories": 360,
                "protein": 30,
                "carbs": 28,
                "fat": 12
            },
            "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd",
            "steps": [
                "Chop lettuce, cucumber and tomato.",
                "Add tuna and corn.",
                "Mix with olive oil and lemon.",
                "Serve cold."
            ],
            "sauces": ["Lemon dressing", "Yogurt sauce", "Garlic sauce"],
            "tip": "Add the dressing only right before eating."
        },
        {
            "name": "Grilled Cheese Toast",
            "category": "dairy",
            "required_items": {"bread", "cheese", "butter"},
            "time_minutes": 8,
            "difficulty": "Easy",
            "nutrition": {
                "calories": 430,
                "protein": 18,
                "carbs": 38,
                "fat": 24
            },
            "image": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af",
            "steps": [
                "Butter the bread slices.",
                "Place cheese between the slices.",
                "Toast in a pan.",
                "Cook until golden and melted."
            ],
            "sauces": ["Ketchup", "Garlic mayo", "Tomato dip"],
            "tip": "Use medium-low heat so the cheese melts before the bread burns."
        },
        {
            "name": "Chicken Sandwich",
            "category": "meat",
            "required_items": {"chicken", "bread", "lettuce", "tomato"},
            "time_minutes": 18,
            "difficulty": "Medium",
            "nutrition": {
                "calories": 520,
                "protein": 38,
                "carbs": 45,
                "fat": 18
            },
            "image": "https://images.unsplash.com/photo-1528736235302-52922df5c122",
            "steps": [
                "Cook or warm the chicken.",
                "Toast the bread.",
                "Add lettuce and tomato.",
                "Add chicken and sauce."
            ],
            "sauces": ["Garlic mayo", "Barbecue", "Honey mustard"],
            "tip": "Slice the chicken thin so the sandwich is easier to eat."
        },
        {
            "name": "Potato Carrot Soup",
            "category": "pareve",
            "required_items": {"potato", "carrot", "onion", "garlic"},
            "time_minutes": 40,
            "difficulty": "Medium",
            "nutrition": {
                "calories": 280,
                "protein": 7,
                "carbs": 52,
                "fat": 6
            },
            "image": "https://images.unsplash.com/photo-1547592180-85f173990554",
            "steps": [
                "Chop potato, carrot, onion and garlic.",
                "Cook onion and garlic in a pot.",
                "Add potato and carrot with water.",
                "Cook until soft and blend."
            ],
            "sauces": ["Olive oil", "Lemon", "Black pepper"],
            "tip": "Blend only half the soup if you want texture."
        },
        {
            "name": "Honey Garlic Chicken",
            "category": "meat",
            "required_items": {"chicken", "honey", "garlic", "soy sauce"},
            "time_minutes": 30,
            "difficulty": "Medium",
            "nutrition": {
                "calories": 480,
                "protein": 40,
                "carbs": 32,
                "fat": 18
            },
            "image": "https://images.unsplash.com/photo-1598515214211-89d3c73ae83b",
            "steps": [
                "Mix honey, garlic and soy sauce.",
                "Cook chicken in a pan.",
                "Pour the sauce over the chicken.",
                "Cook until sticky and glazed."
            ],
            "sauces": ["Honey garlic", "Soy sauce", "Teriyaki"],
            "tip": "Do not use very high heat because honey burns fast."
        },
        {
            "name": "Vegetable Fried Rice",
            "category": "pareve",
            "required_items": {"rice", "eggs", "carrot", "corn", "soy sauce"},
            "time_minutes": 20,
            "difficulty": "Easy",
            "nutrition": {
                "calories": 510,
                "protein": 18,
                "carbs": 78,
                "fat": 15
            },
            "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b",
            "steps": [
                "Use cooked rice.",
                "Scramble eggs in a pan.",
                "Add carrot and corn.",
                "Add rice and soy sauce."
            ],
            "sauces": ["Soy sauce", "Sweet chili", "Teriyaki"],
            "tip": "Cold rice works better than fresh rice."
        },
        {
            "name": "Quick Pancakes",
            "category": "dairy",
            "required_items": {"flour", "milk", "eggs"},
            "time_minutes": 15,
            "difficulty": "Easy",
            "nutrition": {
                "calories": 450,
                "protein": 16,
                "carbs": 68,
                "fat": 14
            },
            "image": "https://images.unsplash.com/photo-1528207776546-365bb710ee93",
            "steps": [
                "Mix flour, milk and eggs.",
                "Heat a pan with butter.",
                "Pour small circles of batter.",
                "Flip when bubbles appear."
            ],
            "sauces": ["Honey", "Yogurt", "Chocolate spread"],
            "tip": "Do not overmix the batter."
        }
    ]

    available_recipes = []
    almost_recipes = []

    for recipe in recipes:
        missing_items = recipe["required_items"] - inventory_set

        recipe_copy = recipe.copy()
        recipe_copy["required_items"] = list(recipe["required_items"])
        recipe_copy["missing_items"] = list(missing_items)

        if len(missing_items) == 0:
            available_recipes.append(recipe_copy)
        elif len(missing_items) <= 2:
            almost_recipes.append(recipe_copy)

    return available_recipes, almost_recipes


@app.get("/api")
def home_api():
    inventory = read_inventory()
    available_recipes, almost_recipes = get_available_recipes(inventory)

    return {
        "owner": OWNER_NAME,
        "inventory": inventory,
        "available_recipes": available_recipes,
        "almost_recipes": almost_recipes,
        "message": "Choose what you feel like eating today!",
        "nutrition_note": "Nutrition values are rough estimates and not medical advice."
    }

@app.post("/api/ai_recipe")
async def ai_recipe(request: Request):
    if not os.getenv("GEMINI_API_KEY"):
        return {"error": "No Gemini API key configured on server."}

    data = await request.json()
    ingredients = data.get("ingredients", "")

    prompt = (
        f"Suggest a detailed recipe using ONLY these ingredients: {ingredients}. "
        "Include: recipe name, required ingredients with weights, calories, protein, carbs, fat, "
        "prep time, difficulty, and step-by-step instructions. Respond in clear English."
    )

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)

        return {"result": response.text}

    except Exception as e:
        return {"error": str(e)}