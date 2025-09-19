age = int(input("Enter your age: "))
movie_rating = input("Enter the movie rating (G, PG, PG-13, R): ").strip()

rating_requirements = {
    "G": 0,  
    "PG": 6,  
    "PG-13": 13,
    "R": 17
}

if movie_rating in rating_requirements:
    required_age = rating_requirements[movie_rating]
    if age >= required_age:
        print("You can watch the movie.")
    else:
        print(f"Not recommended for your age. You must be at least {required_age} years old for {movie_rating} rated movies.")
else:
    print("Invalid rating. Please enter G, PG, PG-13, or R.")
