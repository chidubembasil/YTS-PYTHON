<<<<<<< HEAD
# # print("Hello, World!")
# # print("Hello, World!")

# # x =47
# # print(x)
# # y = 45
# # print(y)
# # z = x + y
# # print(z)


# # b = str(67)  
# # print(b)
# # y = int(3)   
# # z = float(3)  
# # print(b, y, z)


# # num1 = 10
# # print(type(num1))

# # num2 = "20.5"
# # print(type(num2))
# # # casting
# # print(5 + int("5"))

# age =int(input("Enter your age: "))
# print("Your age is:", age)
# print("age > 18:", age > 18)

# name =str(input("Enter your name: "))
# print("Your name is:", name)

# height =float(input("Enter your height in meters: "))
# print("Your height is:", height, "meters")



# print("Welcome to the Python programming world!") 




# # newNumber = 7   # camel casing
# # new_number = 8  # snake casing
# # NewNumber = 9   # pascal casing


# # new_number = 14
# # print(new_number)

# # print(5%2)

# # print(2**3)





# # script for a simple calculator(+ , - , <, * , /) that adds two numbers from user inputs and prints the result .


# # classwork
# # use the membership operator to check if "Math" is present in the list of classes below and print the result.
# classes = ["Math", "Science", "History", "Art", "P.E"]
# # print ("Math" in classes)
# # print ("Physics" in classes)
# classes[1] ="physics"
# print(classes)

# classes.append("Art")
# print(classes)


# # list constructor
# schools = list(("FUTA", "UNILAG", "FUTMINNA", "UNILORIN", "FUNNAB"))
# print(type(schools))
# print(schools[3])
# print(schools[-3])
# print(schools[-1])
# print(schools[-2])
# print(schools[1:4])  
# print(schools[3:5]) 
# print(schools[3:])
# print(schools[1:])
# print(schools[:3])
# # for the range to work the last index must be plus 1






# nums =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[0:10:2])  #slicing with step
# print(nums[0:10:1])  #slicing with step
# print(nums[0:10:3])  #slicing with step
# print(nums[1:10:2])  #slicing with step


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


# print("operator == +:", operator )
# print("operator == -:", operator )
# print("operator == *:", operator )   
# print("operator == /:", operator )

# name =str(input("Enter your name: "))
# print("Your name is:", name)

# height =float(input("Enter your height in meters: "))
# print("Your height is:", height, "meters")
=======
movieProducer = input("enter the name of the producer:")
movieTitle = input("enter the title of the movie:")

movies = {
    "boys before flowers": "treasure in the palace",
    "power ranger": "spider man",
    "pj mask": "the man call God",

}
movies[movieProducer] = movieTitle

if "boys before flowers" in movies:
    print(movies["boys before flowers"])

    for i in movies:
        print(i)



else:
       print("The movieis not in the dictionary")  
>>>>>>> a5f94f95a6edfef52463cad5a66e87d8742450b8
