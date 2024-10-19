# from copy import deepcopy

# print(dir(list))
# li = [1, 2, 3]
# print(li)
# li.append(4)
# li[len(li):] = [5]
# print(li)
# li.clear()  # clear list elements
# del li[0] # can delete in this way to
# print(li)
# li.append(9)
# print(li)

# # this give shallow copy( it didn't work in nested lists) i have to use deepcopy() for solving the problem
# li2 = li.copy()
# li[0] = [0]
# print(li2, li)
# ---

li = [1, 2, 3, 3, 3]
# print(li.count(3))   # .count() count number of repeating
li.extend([3, 6, 9])   # .extend() concat to list
print(li)
print(li.index(3, 3))   # .index() find first index of srg, in the args 2 specify start searching from where
li.insert(1, "i") # i give .insert(index, value) put what i want in index i specifying
print(li)

# .pop() -> cut last index element for me from list, i can cut with specify index .pop(0)
li.remove(3)   # give him item and removed (of course remove first repeat of)
print(li)

li.reverse()   # make list reverse for me
# reversed() return reverse list (don't make list reverse)
print(li)

li.remove('i') # i remove "i" for perform below action
# .sort() sort list for me i can use this before .reverse() for having reverse sorted list
li.sort(reverse=True, key=lambda x: x%2)  # i can perform these action 

# print(li[::-1]) # reverse can happen with this way to