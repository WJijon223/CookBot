# CookBot

A terminal-based cooking assistant that helps you find recipes based on ingredients you have and provides AI-enhanced cooking instructions.

## Features

- Search for recipes based on 5-10 ingredients you have available
- Get detailed recipe information including ingredients and step-by-step instructions
- Receive AI-enhanced cooking instructions 
- Explore recipe variations and cooking tips
- Save and browse your recipe history

## Requirements

- Python 3.7+
- Spoonacular API key 
- Google Gemini API key 

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/CookBot.git
cd CookBot
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your Spoonacular API key:

```bash
# On macOS/Linux
export SPOONACULAR_API_KEY=your_api_key_here

You can get a free Spoonacular API key from: https://spoonacular.com/food-api

## Usage

Run the application with:

python CookBot/main.py
```

## Project Structure

```
CookBot/
├── main.py                 
├── requirements.txt        
├── README.md               
├── api/                   
│   ├── __init__.py         
│   ├── database.py         
│   ├── recipe_api.py       
│   └── gemini_api.py       
└── tests/                  
    ├── __init__.py         
    ├── test_database.py    
    └── test_gemini_api.py  
```

## Google Gemini Integration

CookBot uses Google's Gemini to generate cooking instructions.

1. Takes your ingredients and recipe title
2. Generates cooking instructions

## Testing

Run individual tests with:

```bash
python CookBot/tests/test_gemini_api.py
python CookBot/tests/test_database.py
```
