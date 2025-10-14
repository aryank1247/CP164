"""
-------------------------------------------------------
[Assignment 2 Task 5]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-19"
-------------------------------------------------------
"""
from Movie_utilities import genre_counts, read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

counts = genre_counts(movies)

print("Counts: {}".format(counts))
