# List of available foods
food_list = ["rice", "beans", "yam", "bread", "spaghetti", "egg", "garri", "vegetables"]

# Ask the user to enter a food
user_food = input("Enter a food name: ").lower()

# Check if the food is in the list
if user_food in food_list: 
    print("✅ Food is available!")
else:
    print("❌ Food is not available.")
