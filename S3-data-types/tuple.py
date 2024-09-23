# t = (1, 2, 3, "soroush", [1, 2], (4, 5))

# in tuple i can't change elements
# t = 1, 2, 3, 4 # tuple can assign with out ()  of curse its better to use parenthesis
# print(type(t))
# print(t)
# -----------------------------------

# tuple features like list (slicing, *, +, etc) except changing features
# t = 1, 2, 3, 4 
# print(t * 2)
# print(t + t)
# print(t + (8, 9, 10))
# print(2 in t)
# print(t[1])
# print(t[:3])
# print(t[::2])
# -----------------------------------

# Tuples are unchangeable but i can change lists in tuples
# t = (1, 2, [1, 2, 3, 4, 5], 4 )
# print(t)
# t[2][0] = 9 #can change lists in tuples
# print(t)
# -----------------------------------

# l = []
# print(type(l))

# t = ()
# print(type(t))

# t = (1)  # whene i use one value in tuple its think it is expression( int)
# print(type(t))

# t = (1,)  # for solving this problem use one coma( , ) after value
# print(type(t))
# -------------------------------------

# t = tuple("soroush")
# print(t)
# print(type(t))

# t = tuple() # make empty tuple with tuple()
# print(t)
# print(type(t))
# -------------------------------------

# a way for changing tuple is convert tuple to list do change and return to tuple  again
# of curse better use list from beginning
# t = (1, 2, 3)
# print(t)
# l = list(t) # convert tuple to list
# l[0] = 8 # do change
# t = tuple(l)   # return to tuple  again
# print(t)
# -------------------------------------

# and now i have super assignment in tuple() and its support ( * ) like list (for give extra values)
# x, y, z = (1, 2, 3)
# print(x)
# print(y)
# print(z)

# *x, y, z = (1, 2, 3, 4, 5, 6, 7, 8)
# print(x)
# print(y)
# print(z)

# *x, y, z = ("soroush")
# print(x)
# print(y)
# print(z)
# -------------------------------------


# t1 = (1, 2, 3)
# t2 = t1  # like list tuple needs Deep copy 
# print(id(t1))
# print(id(t2))

# import copy
# t1 = (1, 2, 3, [4, 5])
# t2 = copy.deepcopy(t1) 
# # like list tuple needs Deep copy because list in tuple(changeable valuse) can be issue
# t2[3][0] = 9
# print("t1:", t1)
# print("t2:", t2)
# print(id(t1))
# print(id(t2))


























