# first assignment 

first_number =int(input("Enter Your First Number: "))
second_number =int(input("Enter Your Second Number:"))
operator = int(input("Input Your Operator(+ , _- ,* , /):"))
if operator == '+':
    print(first_number + second_number)
elif operator == '-':
    print(first_number - second_number)
elif operator == '*':
    print(first_number * second_number)
elif operator == '/':
    print(first_number / second_number)
    
    
    
    # second assignment
    food = ["rice", "beans", "plantain", "noodles", "spaghetti"]
user_input = input("Enter an item to check if it's in the food list: ")
if user_input in food:
    print(f"{user_input} is in the food list.")
else:
    print(f"{user_input} is not in the food list.")
    