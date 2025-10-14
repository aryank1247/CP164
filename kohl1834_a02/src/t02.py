"""
-------------------------------------------------------
[Assignment 2 Task 2]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-19"
-------------------------------------------------------
"""
from Movie_utilities import get_by_rating, read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

rating = float(input("Enter a rating: "))

rmovies = get_by_rating(movies, rating)

print("Movies with a rating >= {}: ".format(rating))

for movie in rmovies:
    print("==============================================")
    print(movie)
