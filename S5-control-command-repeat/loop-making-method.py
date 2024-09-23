# l = ['a', 'b', 'c', 'd', 'e', 'f']
# for i in range(len(l)):
#    print(i, ':', l[i])
# -------------------

# l = ['a', 'b', 'c', 'd', 'e', 'f']
# # i have another def do this for me
# print(enumerate(l))
# print(list(enumerate(l)))  # enumerate : put index value beside each other in tuple in list
# -------------------

# l = ['a', 'b', 'c', 'd', 'e', 'f']
# # it can be used instead of range in for loop
# for i, v in enumerate(l):
#    print(i, ":", v)  # enumerate put list element index value beside each other
# -------------------

# l = ['a', 'b', 'c', 'd', 'e', 'f']
# # it can be used instead of range in for loop
# for i, v in enumerate(l, 5):  # i can choose where index should have start in second input of enumerate
#    print(i, ":", v)
# -------------------

# # zip in for loop to zip ordered values in for loop
# l = ['soroush', 'milad', 'sam']
# a = [20, 21, 21]
# # it can be used instead of range in for loop
# for i, v in zip(l, a):  
#    print(i, ", age:", v)
# -------------------

# reversed to out values in for loop reversed
# l = ['soroush', 'milad', 'sam']
# a = [20, 21, 21]
# # it can be used instead of range in for loop
# for i in reversed(l):  
#    print(i)
# -------------------

# # sorted to out sorted values
# l = ['soroush', 'milad', 'sam']
# a = [20, 28, 21]
# # it can be used instead of range in for loop
# # for i in sorted(l):  
# #    print(i)
# for i in sorted(a):  
#    print(i)
# ----------------------

# # use revers sorted
# a = [20, 28, 21]
# # for i in reversed(sorted(a)):  
# #    print(i)
# #              or do this to revers sorted
# for i in sorted(a, reverse=True):  
#    print(i)
