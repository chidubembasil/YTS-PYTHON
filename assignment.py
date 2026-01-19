# # first assignment 

# first_number =int(input("Enter Your First Number: "))
# second_number =int(input("Enter Your Second Number:"))
# operator = int(input("Input Your Operator(+ , _- ,* , /):"))
# if operator == '+':
#     print(first_number + second_number)
# elif operator == '-':
#     print(first_number - second_number)
# elif operator == '*':
#     print(first_number * second_number)
# elif operator == '/':
#     print(first_number / second_number)
    
    
    
#     # second assignment
#     food = ["rice", "beans", "plantain", "noodles", "spaghetti"]
# user_input = input("Enter an item to check if it's in the food list: ")
# if user_input in food:
#     print(f"{user_input} is in the food list.")
# else:
#     print(f"{user_input} is not in the food list.")
    
    
    
    # third assignment
    
i = 2

while i <= 1000:
    prime = True
    j = 2

    while j <= i - 1:
        
        if i % j == 0:
            prime = False
            break
        j += 1

    if prime:
        print(i)

    i += 1
    
    # fourth assignment
MovieProducer = input("Enter the name of the producer:")
MovieTitle = input("Enter the title of the movie:")

MovieDetails = {
  "James Cameron, Jon Landau": "Titanic",
"James Cameron, Jon Landau": "Avatar",
"Christopher Nolan, Emma Thomas, Charles Roven": "The Dark Knight",
"Christopher Nolan, Emma Thomas": "Inception",
"Jerry Bruckheimer": "Pirates of the Caribbean series",
"David Heyman": "Harry Potter film series",
"Christopher Nolan, Emma Thomas, Charles Roven": "The Dark Knight",
"Christopher Nolan, Emma Thomas": "Inception",
"Jerry Bruckheimer": "Pirates of the Caribbean series",
"David Heyman": "Harry Potter film series",
"Peter Jackson, Barrie M. Osborne, Fran Walsh": "The Lord of the Rings trilogy",
"Peter Jackson, Jan Blenkin, Carolynne Cunningham, Fran Walsh": "King Kong (2005)",
"Gary Kurtz, George Lucas": "Star Wars (original film)",
"Frank Marshall, George Lucas, Howard Kazanjian": "Raiders of the Lost Ark",
"Mo Abudu, Iretiola Doyle (executive producers via EbonyLife)": "The Wedding Party",
"Kemi Adetiba, Kene Okwuosa (among others)": "King of Boys",
"Charles Okpaleke": "Living in Bondage: Breaking Free",
"Jade Osiberu": "Sugar Rush",
"Mo Abudu": "Òlòtūré"

}


MovieDetails[MovieProducer] = MovieTitle

if "David Heyman" in MovieDetails :
   print(MovieDetails["David Heyman"])
   
   for i in MovieDetails:
       print(i , MovieDetails[i])
       
else:
           print("Producer not found in the movie details.")

# if MovieProducer in MovieDetails:
#     print(f"The producer '{MovieProducer}' is associated with the movie '{MovieDetails[MovieProducer]}'.")
    
#     for producer, title in MovieDetails.items():
#         print(f"Producer: {producer}, Movie Title: {title}")
        
#     else:
#         print(f"No movie found for producer '{MovieProducer}'.")



