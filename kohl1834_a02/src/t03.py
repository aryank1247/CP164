"""
-------------------------------------------------------
[Assignment 2 Task 3]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-19"
-------------------------------------------------------
"""
from Movie_utilities import get_by_genre, read_movies

file_handle = open("movies.txt", 'r')

movies = read_movies(file_handle)

genre = int(input("Enter a genre code: "))

gmovies = get_by_genre(movies, genre)

for movie in gmovies:
    print("========================================")
    print(movie)
