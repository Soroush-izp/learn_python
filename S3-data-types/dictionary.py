# d = {}
# print(d)
# print(type(d))
# ---------------------

# in dictionary order(index) isn't important 
# d = {1: 5, "b": 10}  # key most be immutable value -> tuple, str, num, etc.
# print(d["b"])

# d = {1: 5, "b": 10, "b": 8}  # key most unic -> you didn't get error but value change
# print(d["b"])

# d = {1: 5, "b": 8}   # dictionary is mutable
# d["b"] = 20 # change
# d["d"] = 32 # add
# print(d)
# print(d.get("t")) # if key isn't exist turn none not Error( .get() )
# ----------------------------------

# 3 important method on python
# d.keys()  -> get all keys
# d.values()   -> get all values
# d.items()   -> get both key values

# d = {"b": 12, "a": 13, "c": "30"}
# print(d.keys())   # type of these method result isn't list its dict_keys
# print(type(d.keys()))   # type of these method result isn't list its dict_keys

# print(d.values()) # type of these method result isn't list its dict_values
# print(type(d.values())) # type of these method result isn't list its dict_values

# print(d.items())  # type of these method result isn't list its dict_items
# print(type(d.items()))  # type of these method result isn't list its dict_items

# they have to convert to lists
# ----------------------------------------

# d = {"b": 12, "a": 13, "c": "30"}
# del d["b"]  # delete one key value from dictionary
# del d  # for delete dictionary
# print(d)
# ----------------------------------------

# d = {"b": 12, "a": 13, "c": "30"}
# d["c"] = "reza"
# how change key in dictionary
# x = d["c"]
# del d["c"]
# d["x"] = x

# print(d)
# ----------------------------------------

# l = [8, 2, 0, 5, 6, 7]
# # print(sorted(l))
# l = sorted(l, reverse=True)
# print(l)
# ----------------------------------------

# d = {"b": 12, "a": 13, "c": 30}
# print(sorted(d))
# print(sorted(d.keys()))
# print(sorted(d.values()))
# print(sorted(d.values(), reverse=True))
# ----------------------------------------

# for convert to dictionary   dict()

# d = dict([("a", 32), ("b", 21), ("c", 25)])  # this list with key value in tuple can convert to dictionary
# d = dict(a=10, b=43, z=87) # or like this in just tuple and have to be string
# ----------------------------------------

# compression
# d = {x: x**2 for x in range(10)}
# print(d)
# ----------------------------------------

# value of dic can dic (key can't be dic)
# d = {
#    '169': {"name": "soroush", "age": 20},
#    '172': {"name": "reza", "age": 25},
# }
# print(d["172"])
# print("169" in d)
# print("169" not in d)
# print(d["169"] == {"name": "soroush", "age": 20})
# ----------------------------------------

# d = {"a": 5, "b": 6}
# print(d == {"a": 5, "b": 6})
# ----------------------------------------

# The code snippet is demonstrating how to create a dictionary by zipping two separate lists of keys
# and values together using the `zip()` function.
# i can use ( zip() ) to make a dictionary with two seprate list of key & values
a = ['a', 'b', 'c']
v = [1, 2, 3]
i = zip(a, v)  # to zip two list together
print(dict(i)) # its in zip format i have to convert it to other format( dict )



