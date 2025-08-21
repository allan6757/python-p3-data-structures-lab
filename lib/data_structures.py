spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # return a list of just the names
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # return only foods with heat_level > 5
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    # print each food in the format: Name (Cuisine) | Heat Level: 🔥 * heat_level
    for food in spicy_foods:
        heat = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # return the first food that matches the cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    # reuse get_spiciest_foods and print them
    for food in get_spiciest_foods(spicy_foods):
        heat = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat}')

def get_average_heat_level(spicy_foods):
    # average = sum of heat levels / number of foods
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    # return a new list with the new food added
    return spicy_foods + [spicy_food]