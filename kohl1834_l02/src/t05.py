"""
-------------------------------------------------------
[Lab 1 Task 1]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-18"
-------------------------------------------------------
"""
from Stack_array import Stack
from utilities import stack_test
from Movie_utilities import read_movie

s = Stack()

fh = open("movies.txt", "r", encoding="utf-8")

for line in fh:
    movie = read_movie(line)
    s.push(movie)

stack_test(s)
