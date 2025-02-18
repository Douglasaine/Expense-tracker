movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
total_budget = sum(movie[1] for movie in movies)
average_budget = total_budget / len(movies)
print(f"The average budget is {average_budget}")
for movie in movies:
    if movie[1] > average_budget:
        over_average = movie[1] - average_budget
        print(f"{movie[0]} cost ${movie[1]} and ${over_average} over average")