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