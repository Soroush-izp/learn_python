def max3(a, b, c):
   print( max(a, b, c))


# # syntax 1
# # put value ordered
# # normal way
# max3(1, 2, 3)
# ----------------------------------

# # syntax 2
# # put name=value
# max3(a=1, b=2, c=3)

# # syntax combined 1 + 2
# # put normal + name=value
# max3(1, c=3, b=2) # attention that fist normal way second name= value way
# # and i can't choose that value i gave him value in ordered way
# ----------------------------------

# # syntax 3
# # *iterable (str, tuple, list, set, ...)
# max3(*[1, 5, 9])  # its gave to argument ordered
# max3(*(1, 5, 9))  # its gave to argument ordered
# max3(*{1, 5, 9})  # its gave to argument ordered
# ---

# x, y, z = [5, 9, 6]
# print(x, y, z)
# --------------

# x = [5, 8, 12]
# max3(*x)
# ----------------------------------

# # syntax 4
# # dictionary syntax ->  i use ( **dict ) two * before dictionary to consider dict key as name of
# # arguments definition and put their value on it
# d = {"a": 23, "b": 32, "c": 33}
# max3(**d)












