"""
-------------------------------------------------------
[Assignment 2 Task 4]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-19"
-------------------------------------------------------
"""
from Movie_utilities import read_movies, get_by_genres

with open("movies.txt", "r") as file:
    movies = read_movies(file)

genres = [3, 4]  # Example: romance and comedy
movies_by_genres = get_by_genres(movies, genres)

print(f"Movies matching all genres {genres}:")
for movie in movies_by_genres:
    print(movie)
