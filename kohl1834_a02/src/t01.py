"""
-------------------------------------------------------
[Assignment 2 Task 1]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-19"
-------------------------------------------------------
"""

from Movie_utilities import read_movies, get_by_year

with open("movies.txt", "r") as file:
    movies = read_movies(file)

year = int(input("Enter Year: "))
movies_by_year = get_by_year(movies, year)

print(f"Movies from {year}:")
for movie in movies_by_year:
    print(movie)
