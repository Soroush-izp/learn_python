# print(dir(tuple))

# t = (1, 2, 2, 2, 3, 4, 5)
# print(t.count(2))
# print(t.index(2))
# --------------------- Set

# print(dir(set))
t = {1, 2, 2, 2, 3, 4, 5}  # elements in set have to be not change able
print(t)
# t.clear() # make set clear
# t.add(9)
# print(t)
# like another data types set have to be .copy() for copying otherwise cause problem of call by reference
# - 

t = {1, 2, 3, 4}
s = {3, 4, 18, 24}

# print(t.difference(s))  # .difference()  out differences 
# print(t.difference_update(s))  # .difference_update()  implement differences on set 
# print(t)

print(t.isdisjoint(s))  # .isdisjoint()  if they haven't same element it turn back True

# pop()  still work in set bout i can't specify index i haven't index in set
# remember set hasn't order