

        

students = [
    ("Alice", "18", [78, 85, 90]),
    ("Bob", "20", [60, 65, 70]),
    ("Charlie", "19", [95, 92, 88]),
    ("Daisy", "17", [40, 55, 60])
]


def determine_grade(avg):
    match avg:
        case a if a >= 70:
            return "A"
        case a if 60 <= a < 70:
            return "B"
        case a if 50 <= a < 60:
            return "C"
        case a if 45 <= a < 50:
            return "D"
        case _:
            return "F"



results = {}
averages = []


for student in students:
    name = student[0]
    age = int(student[1])           
    scores = student[2]
    
    avg = sum(scores) / len(scores) 
    grade = determine_grade(avg)

    results[name] = {
        "age": age,
        "scores": scores,
        "average": avg,
        "grade": grade
    }

    averages.append(avg)



i = 0
print("\nSTUDENT REPORT")


while i < len(students):
    name = students[i][0]
    avg = results[name]["average"]
    grade = results[name]["grade"]

    print(f"{i+1}. {name} - Average: {avg:.2f}, Grade: {grade}")
    i += 1



highest = max(averages)
lowest = min(averages)

print("\nSUMMARY")

print(f"Highest Average Score: {highest:.2f}")
print(f"Lowest Average Score: {lowest:.2f}")