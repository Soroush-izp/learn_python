# lambda = one line def without name can have name with assigning to the var
# can be used without parapets() it didn't need return because it return everything after ( : )
# i can't use while ( and other multi-line thing in lambda)
# def func(x):
#    return x**2

# below lambda func like up func just with lambda way
# a = lambda x: x**2
# print(a(2))
# print(a(5))
# ---

# a = lambda x, y: x**2 + y**2  # lambda automatically returns every thing after ( : )
# print(a(2, 2))
# -----------------------------

# some of important built in def in python

# # The map() function executes( run) a specified function for each item in an iterable.
# # The item is sent to the function as a parameter.
# # map(function, iterable)  map good for do change in every item of iterable in a function
# def func(x):
#    return x ** 2

# li = [1,2,3,4,5,6,7,8,9]
# # print(list(map(func, li)))
# # using lambda for map function can be good => accessible short ,...
# print(list(map(lambda x: x**2, li)))
# ---

# # The filter() function returns an iterator where the items are filtered through a function
# # to test if the item is accepted or not.
# # filter(function, iterable) filter good for check every item of iterable support i condition
# # and filter list based on my condition in func returned true or false
# def func(x):
#    return x > 5

# li = [1,2,3,4,5,6,7,8,9]
# # print(list(filter(func, li)))
# # using lambda for filter function can be good => accessible short ,...
# print(list(filter(lambda x: x > 5, li)))
# # didn't forgot for grtting list of oterable in built in def i have to use ( list() ) func
# ---

# # reduce()  -> its form functools( have to be import from functools)
# # performs cumulative operations on iterables
# from functools import reduce

# def func(x, y):
#    return x + y

# li = [1,2,3,4,5,6,7,8,9]

# # print(reduce(func, li))
# print(reduce(lambda x, y: x + y, li))
# ---

# sorted()  
# The sorted() function returns a sorted list of the specified iterable object.
from functools import reduce

def func(x):
   return x%2

li = [1,2,3,4,5,6,7,8,9]

# print(reduce(func, li))
print(sorted(li, key=func))   # give sorted func in in front of key
