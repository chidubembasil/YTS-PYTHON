<<<<<<< HEAD
# # # is_true = True

# # # if is_true:
# # #     print("the value is true")
# # # elif not is_true:
# # #     print("the value is false")
# # # else:
# # #     print("the value is true or false ")
    
# # # match is_true:
# # #     case True:
# # #         print("the value is true")
# # #     case False:
# # #         print("the value is false")
# # #     case _:
# # #         print("the value is not true or false ")
        
# #         # While loop
# # # i = 1
# # # while i <= 1000:
# # #     print(i)
# # #     i += 1
# #     # "and , or , not" for logical operations in python
    
# #     # print out even numbers
# # # i = 2
# # # while i <= 1000:
# # #     print(i)
# # #     i += 2

# #     # inverse
# # # i = 1000
# # # while i >=1:
# # #         print(i)
# # #         i -= 2
        
# # # for i in range (5 , 20 , 2):
# # #      print(i)

# # for i in range (2 , 1000 , 2) :
# #     print(i)

# person = {
#     "name": "John",
#     "age": 30,
#     "isMonster": False,
#     "city": "New York"
# }  

# print(person) 
# print(person["age"])
# print(person["name"])

# person.pop("age") 
# person["age"] =25
# print(person)
 
# person.update({"age": 35})
# print(person)




# bookAuthor = input("Enter the name of the author:")
# bookName = input("Enter the name of the book:")
# books = {
#     "james Green": "The Silent Patient",  
#     "james Green" : "48 laws of powers" ,
#     "Mark Manson": "The Clover Run" ,
#     "james Clear": "Atomic Habits" ,  
#     "robert smith": "Where the Crawdads Sing",
#     "linda brown": "The Midnight Library",
#     "michael johnson": "The Vanishing Half"
    
# }

# books[bookAuthor] = bookName

# if "james Green" in books:
#     # print(f"Book by james Green: {books['james Green']}")
#     print(books["james Green"])

#     for i in books:
#         # print(f"Author: {i}, Book: {books[i]}")
#         print(i)

# else :
#     print('The Book is not in the dictionary')
     
     
     
    #  functions
    
# def my_function():
#         print("Hi there!")
#         print(342)
        
# my_function()   


# def my_function(x ,y):       
#     # ANYTHING INSIDE THE BRACKET ABOVE IS CALLED PARAMETERS
#         z = x + y
#         print(z)
        
# my_function(2 ,3) 
# # ANYTHING INSIDE THE BRACKET ABOVE IS CALLED ARGUMENTS


# def my_function(x , y):
      
#       return x + y

# print(my_function(2 ,3) )


# def my_details(name , age , gender):
#   print(f"my name is {name}, im  {age}, and im a {gender}")

# my_details("basil", 17, "male")


# first_num = int(input("Enter your first number: "))
# sign = input("Enter an arithmetic operator : ")
# second_num = int(input("Enter your second number: "))   


# def my_Cal(first_num , sign , second_num):
#     if sign == "+":
#         return first_num + second_num
#     elif sign == "-":
#         return first_num - second_num
#     elif sign == "*":
#         return first_num * second_num
#     elif sign == "/":
#         return first_num / second_num
#     else:
#         return "Invalid operator"
# print(my_Cal(first_num , sign , second_num))



firstNum = int(input("Enter your first number: "))
# sign = input("Enter an arithmetic operator : ")
secondNum = int(input("Enter your second number: "))   


def my_Cal(x , y):
    z = x + y         
    print(z)
my_Cal(firstNum , secondNum)


def my_Cal(x , y):
     z = x * y
     print(z)
my_Cal(firstNum , secondNum)



def my_Cal(x , y):
     z = x - y
     print(z)
my_Cal(firstNum , secondNum)



def my_Cal(x , y):
     z = x / y
     print(z)
my_Cal(firstNum , secondNum)