"""
-------------------------------------------------------
[Lab 1 Task 7]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-11"
-------------------------------------------------------
"""
from Movie_utilities import read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

file_handle.close()

for movie in movies:
    print("{}\n====================".format(movie))
