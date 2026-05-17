# 👑 Buzo Kingdom - Smart Kitchen Recipe Assistant

**Your Intelligent Kitchen Assistant Powered by Google Gemini AI**

A web-based smart kitchen application that helps you discover recipes based on your available ingredients, provides detailed nutritional information, and uses AI to generate custom recipes.

---

## ✨ Features

### 🍽️ Recipe Discovery
- **Smart Inventory Management**: Track your available ingredients from `inventory.txt`
- **Perfect Matches**: Find recipes you can make right now with your ingredients
- **Almost Possible**: Discover recipes missing only 1-2 ingredients
- **10+ Pre-configured Recipes**: Each with detailed instructions, nutrition, and cooking tips

### 🤖 AI-Powered Features
- **Gemini Integration**: Uses Google Gemini AI to generate custom recipes based on your ingredients
- **Smart Filtering**: Filter recipes by:
  - ⏱️ Cooking time
  - 🏷️ Meal type (Dairy/Meat/Pareve)
  - 🔒 Religious dietary requirements
- **Live Suggestions**: Real-time recipe matching as you type

### 📊 Detailed Information
- **Nutritional Data**: Calories, protein, carbs, and fat for every recipe
- **Cooking Instructions**: Step-by-step guide for each dish
- **Sauce Suggestions**: Recommended sauces for each meal
- **Pro Tips**: Chef tips for better results
- **Difficulty Levels**: Easy, Medium, Hard categorization

### 🎨 Modern UI
- Dark theme with purple accent colors
- Smooth animations and transitions
- Responsive design (mobile-friendly)
- 3D particle background effects
- Glassmorphism design elements

---

## 🏗️ Architecture

```
HomeArchitect/
├── app/
│   ├── app.py              # FastAPI backend
│   ├── Dockerfile          # Docker configuration
│   └── requirements.txt     # Python dependencies
├── dashboard/
│   ├── index.html          # Main application
│   ├── landing.html        # Landing page
├── nginx/
│   └── nginx.conf          # Reverse proxy config
├── docker-compose.yml      # Container orchestration
├── inventory.txt           # Your ingredients list
└── .env                    # Environment variables
```

### Backend Stack
- **FastAPI**: Modern Python web framework
- **Google Gemini AI**: Advanced recipe generation
- **Python 3.10+**: Language runtime

### Frontend Stack
- **HTML5 + CSS3**: Responsive layout
- **Vanilla JavaScript**: Dynamic interactions
- **Canvas API**: 3D particle effects

### Deployment
- **Docker**: Containerized application
- **Docker Compose**: Multi-service orchestration
- **Nginx**: Reverse proxy & static file serving

---

## 🚀 Getting Started

### Prerequisites
- Docker and Docker Compose installed
- Google Gemini API key (get it from [Google AI Studio](https://makersuite.google.com/app/apikey))
- Optional: Python 3.10+ for local development

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Amitaibou/HomeArchitect.git
cd HomeArchitect
```

2. **Set up environment variables**
```bash
# Edit .env file
echo "GEMINI_API_KEY=your_api_key_here" >> .env
echo "USER_NAME=Your Name" >> .env
```

3. **Update your inventory**
Edit `inventory.txt` with your available ingredients:
```
eggs
milk
cheese
chicken
rice
...
```

4. **Start the application**
```bash
docker-compose up --build
```

5. **Access the application**
- Open browser: `http://localhost`
- Nginx serves the frontend
- FastAPI backend runs on port 8000

---

## 📝 API Endpoints

### GET `/api`
Returns all recipes and inventory data.

**Response:**
```json
{
  "owner": "Your Name",
  "inventory": ["eggs", "milk", "cheese"],
  "available_recipes": ["..."],
  "almost_recipes": ["..."],
  "nutrition_note": "..."
}
```

### POST `/api/ai_recipe`
Generates a custom recipe using Gemini AI based on provided ingredients.

**Request:**
```json
{
  "ingredients": "chicken, rice, garlic, soy sauce"
}
```

**Response:**
```json
{
  "result": "Detailed recipe..."
}
```

---

## 📦 Recipes Included

1. **Cheese Omelet** (10 min, Easy)
2. **Teriyaki Chicken Rice Bowl** (35 min, Medium)
3. **Creamy Mushroom Pasta** (25 min, Medium)
4. **Tuna Corn Salad** (12 min, Easy)
5. **Grilled Cheese Toast** (8 min, Easy)
6. **Chicken Sandwich** (18 min, Medium)
7. **Potato Carrot Soup** (40 min, Medium)
8. **Honey Garlic Chicken** (30 min, Medium)
9. **Vegetable Fried Rice** (20 min, Easy)
10. **Quick Pancakes** (15 min, Easy)

Each recipe includes:
- Required ingredients
- Step-by-step instructions
- Nutritional information (calories, protein, carbs, fat)
- 3 sauce recommendations
- Professional cooking tip

---

## 🎯 Usage

### From the UI:

1. **View Your Inventory**: See all available ingredients
2. **Click Tags**: Select ingredients to filter recipes
3. **Find Recipes**: See matching recipes instantly
4. **Filter by Preferences**:
   - Select maximum cooking time
   - Choose meal type (Dairy/Meat/Pareve)
   - Specify meat consumption rules
5. **Click Recipe Card**: View full details, instructions, and nutrition
6. **Ask AI Chef**: Generate custom recipes for your ingredients

### Command Line (Optional):

```bash
# Test API endpoint
curl http://localhost:8000/api

# Generate recipe via AI
curl -X POST http://localhost:8000/api/ai_recipe \
  -H "Content-Type: application/json" \
  -d '{"ingredients": "chicken, rice"}'
```

---

## 🔧 Configuration

### Environment Variables (`.env`)

```bash
# Your name for the app
USER_NAME=Amitai and Asaf

# Google Gemini API Key (required for AI features)
GEMINI_API_KEY=your_google_gemini_api_key
```

### Inventory File (`inventory.txt`)

One ingredient per line:
```
eggs
milk
cheese
chicken
rice
tomato
lettuce
...
```

---

## 📱 Features Overview

### Smart Matching Algorithm
- Exact match: +10 points
- Partial match: +6 points  
- Prefix match: +2 points
- Ranked by score

### Dietary Restrictions
- **Religious Notes**: Warns if dairy consumed within 6 hours of meat
- **Category Filtering**: Separate meat, dairy, and pareve options

### Responsive Design
- ✅ Works on desktop, tablet, and mobile
- ✅ Touch-friendly interface
- ✅ Optimized image loading

---

## 🐳 Docker Commands

```bash
# Build and start
docker-compose up --build

# Stop containers
docker-compose down

# View logs
docker-compose logs -f app

# Rebuild after code changes
docker-compose up --build --no-cache
```

---

## 🛠️ Development

### Local Setup (without Docker)

```bash
# Install dependencies
pip install -r app/requirements.txt

# Set environment variables
export GEMINI_API_KEY="your_key"
export USER_NAME="Your Name"

# Run FastAPI server
uvicorn app.app:app --reload --port 8000

# Serve HTML (separate terminal)
python -m http.server 8080 --directory dashboard
```

Then access `http://localhost:8080`

### Project Structure

```
app/app.py
├── read_inventory()          # Read ingredients from file
├── get_available_recipes()   # Filter recipes by ingredients
├── home_api()               # GET /api endpoint
└── ai_recipe()             # POST /api/ai_recipe endpoint

dashboard/
├── index.html              # Main application UI
└── landing.html            # Landing/welcome page
```

---

## 🔐 API Key Setup

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the API key
5. Add to `.env` file: `GEMINI_API_KEY=your_key`
6. Restart the application

---

## 📊 Nutrition Information

All nutritional values are estimates based on standard portions and should not be considered medical advice. Values include:
- **Calories**: Total kilocalories per serving
- **Protein**: Grams of protein
- **Carbs**: Grams of carbohydrates
- **Fat**: Grams of fat

---

## 🎨 UI Components

- **Header**: Fixed navigation with clock and greeting
- **Sidebar**: Inventory, AI Recipe Finder, Preferences
- **Main Content**: Recipe grid with cards
- **Recipe Details**: Full recipe view with instructions
- **3D Background**: Animated particle effects

---

## 🚨 Troubleshooting

### Gemini API Not Working
- Verify API key in `.env`
- Check if key is valid and active
- Ensure quota not exceeded

### Recipes Not Showing
- Check that `inventory.txt` has ingredients
- Verify ingredient names match (case-insensitive)
- Refresh browser cache (Ctrl+F5)

### Docker Issues
```bash
# Clean up all containers
docker system prune -a

# Rebuild from scratch
docker-compose down -v
docker-compose up --build
```

---

## 📄 License

Open for personal use. Modify and distribute as needed!

---

## 👨‍💻 Author

**Amitai Bouzaglo **  
Created with ❤️ for a smarter kitchen.

---

## 🌟 Future Features

- [ ] User authentication & profiles
- [ ] Save favorite recipes
- [ ] Shopping list generator
- [ ] Ingredient search by category
- [ ] Recipe rating system
- [ ] Multi-language support
- [ ] Meal planning calendar
- [ ] Nutritional goals tracker
- [ ] Export recipes as PDF
- [ ] Voice commands support

---

## 📞 Support

For issues or questions:
1. Check this README
2. Review the code comments
3. Test with sample data
4. Verify API configuration

---

**Enjoy cooking with Buzo Kingdom! 👑🍽️**

