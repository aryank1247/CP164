"""
-------------------------------------------------------
[Lab 1 Task 2]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-10"
-------------------------------------------------------
"""
from Movie import Movie

title = "Dellamorte Dellamore"
year = 1994
director = "Michele Soavi"
rating = 7.2
genres = [3, 4, 5, 8]

my_movie = Movie(title, year, director, rating, genres)

genres_list = my_movie.genres_list_string()

print(genres_list)
