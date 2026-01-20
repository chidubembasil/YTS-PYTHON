#print("Hello, World!")

#python Variables
num1 = 5

num2 = "5"

print(num1 + int(num2 ))  #correcting the error using casting

newNumber = 7 #camel case
new_number = 8 #snake case
NewNumber = 9 #pascal case


print(new_number)


#print(5 + 5)

#print(num + 6)


print(5 % 2) #modulus operator

#print is output while input are accepted
#single * is multiplication while multiple are exponentiation 

print(2 ** 3) #exponentiation operator

#Division and Floor division
#print(10 / 3) #division
print(17 // 3) #floor division


#python Data Types
#List: Ordered, indexed, changeable, allows duplicates
#Tuple: Ordered, indexed, unchangeable, allows duplicates 
#Set: unOrdered, not indexed, unchangeable, no duplicates
#Dictionary: Ordered, indexed, changeable, no duplicates

#python List
classes = ["Math", "Science", "History", "Art"]
print(type(classes))

#List is in ordered
print(classes[0]) #accessing list item
print(classes[3]) 
print(classes[2])

print(classes[3]) #index error becoz there is no line num 4 or (list index is out of range)


#list is indexed
print ((len (classes)-1)) #accessing highest index item
index = len(classes)-1   #it will bring the last item
print ((len (classes)-1)) #length of the list


#Class Work
#Use the membership operator to check if "Math" is in the classes  list 

print("Maths" in classes)   #The ans will be T or F


# list is changeable
classes[1] = "physics" #changing list item
print(classes)

#Allow duplicate
classes.append("Art") #adding list item to the end
print(classes)


#list constructor
schools = ["FUTA", "UNILAG", "FUTIMINA", "UNILORIN", "FUNAAB", "MAPOLY"]
print(type(schools))
print(schools[3]) 
print(schools[-1]) 

#range
print(schools[1:4]) #add 1 to the last word

print(schools[3:]) #lmain one  then last to the end  or start:stop:step


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0:10:3]) #slicing with step



#Assignment
#A simple Calculator that adds two numbers(from user input) and prints the results.






    #Functions
def my_function(x,y):
        return x + y
        print(my_function(2, 3)) #this line will not execute because it is after return statement


#Adding two numbers
# firstNum = int(input("Enter a number: "))
# secondNum = int(input("Enter a number: "))

# def my_cal(x,y):
#         z = x + y
#         print(z)
# my_cal(firstNum, secondNum)


#Multiplication
# def my_cal(a,b):
#         c = a * b
#         print(c)
# my_cal(firstNum, secondNum)


#Subtraction 
# def my_cal(a,b):
#         c = a - b
#         print(c)
# my_cal(firstNum, secondNum)


#Division
# def my_cal(a,b):
#         c = a / b
#         print(c)
# my_cal(firstNum, secondNum)



#Assignment
#Create a Calculator that can perform addition, subtraction, multiplication, and division based on user input.





#Class work

#Students =[
#  ("Alice","18",[78, 85, 90]),
#  ("Bob","20",[60, 65, 70]),
#  ("Charlie","19",[95, 92, 88]),
#  ("Daisly","17",[40, 55, 60])
#]
# 1. uses numbers and casting to convert all ages to integers and compute average scores.

# Students data

Students = [
    ("Alice", "18", [78, 85, 90]),
    ("Bob", "20", [60, 65, 70]),
    ("Charlie", "19", [95, 92, 88]),
    ("Daisly", "17", [40, 55, 60])
]

# Convert ages to integers and compute average scores
for student in Students:
    name, age, scores = student
    age = int(age)  # Convert age to integer
    average_score = sum(scores) / len(scores)  # Calculate average score
    print(f"{name} (Age: {age}) - Average Score: {average_score:.2f}")


#2. Iterate through the data of using for and while loops to print names and ages of all students.

# Using for loop
for student in Students:
    name, age, scores = student
    print(f"Name: {name}, Age: {age}")

# Using while loop
i = 0
while i < len(Students):
    name, age, scores = Students[i]
    print(f"Name: {name}, Age: {age}")
    i += 1

#3. Store processed results in a dictionary where names are keys and a tuple of (age, average score) are values.
results_dict = {}
for student in Students:
    name, age, scores = student
    age = int(age)
    average_score = sum(scores) / len(scores)
    results_dict[name] = (age, average_score)

print(results_dict)

#4. Uses if/else or a match statement to determine grades.

for student in Students:
    name, age, scores = student
    average_score = sum(scores) / len(scores)
    
    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    elif average_score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"{name} - Average Score: {average_score:.2f}, Grade: {grade}")


        #5. Encapsulates grading logic inside a function.
def get_grade(average_score):
        grade = "F"
        if average_score >= 90:
            grade = "A"
        elif average_score >= 80:
            grade = "B"
        elif average_score >= 70:
            grade = "C"
        elif average_score >= 60:
            grade = "D"
        else:
            grade = "F"
        return grade

   
for student in Students:
        name, age, scores = student
        age = int(age)
        average_score = sum(scores) / len(scores)
        grade = get_grade(average_score)
        print(f"Name: {name}, Age: {age}, Average Score: {average_score:.2f}, Grade: {grade}")


    #6. Uses range()to number student outputs.
for i in range(len(Students)):
        name, age, scores = Students[i]
        age = int(age)
        average_score = sum(scores) / len(scores)
        grade = get_grade(average_score)
        print(f"Student {i + 1}: Name: {name}, Age: {age}, Average Score: {average_score:.2f}, Grade: {grade}")

        #7. stores all average scores in an array.
average_scores = []
for student in Students:
        name, age, scores = student
        age = int(age)
        average_score = sum(scores) / len(scores)
        average_scores.append(average_score)

print("Average Scores:", average_scores)


#8. outputs each student's names, position, and grade.
for i, student in enumerate(Students):
        name, age, scores = student
        age = int(age)
        average_score = sum(scores) / len(scores)
        grade = get_grade(average_score)
        print(f"Student {i + 1}: Name: {name}, Age: {age}, Average Score: {average_score:.2f}, Grade: {grade}")


        #9. prints the highest and lowest average score.
highest_score = max(average_scores)
lowest_score = min(average_scores)
print(f"Highest Average Score: {highest_score:.2f}")
print(f"Lowest Average Score: {lowest_score:.2f}")


 