# x = 'a'
# c = [x for x in (1, 2, 3)]
# print(x)
# print(c)
# # -------------
#
# # this is generator expretion(comprehension)
# c = (x for x in (1, 2, 3))  # when i put comprehention in () it didn't make tuple it make generator expretion(comprehension)
# print(c)
# # print(list(c))
# print(next(c))
# print(next(c))
# print(next(c))

# notice that : understanding comprehension can be hard in some cases
# # -----
#
# x = "asdiudhqwoiddqwbdqwiugdygvchjc"
# s = {i for i in x}  # this remove repeated strs( i put it in the set{})
# print(s)
# -----

#
# s = {i for i in range(1, 10+1) if i % 2 == 0}  # positive number calc
# print(s)
# # ------------
#
# # i can use it for dict
# d = {"soroush": 23, "ali": 39, "mohammad": 70}
# s = {key: value for key, value in d.items()}
# print(s)
# # ------------
# #
# # # i can use it for dict
# d1 = ["a", "b", "c"]
# d2 = ["dasd", "hdad", "sajjnd"]
# s = {key: value for key, value in zip(d1, d2)}  # i concat two list with zip(key, value) method
# print(s)
# # -------------
#
# x = [1, 2, 3, 4, 5]
# y = []
#
# for num in x:
#     y.append(num if num % 2 != 0 else 0)
# print(y)
#
# # i can do up job simply with this
# l = [n if n % 2 != 0 else 0 for n in x]
# # -------------
# #
# x = [1, 2, 3, 4, 5]
# def func(n):
#     if n % 2 == 0:
#         return n
#     else:
#         return 0
#
# # i can do up job simply with this
# l = [func(n) for n in x]    # i can use def too
# print(l)
# # ------------
#
# from random import randrange
#
# def func():
#     return randrange(50, 150)
#
#
# x = [n for _ in range(10) if (n:=func()) > 100]
# print(x)
# ---------------

t = ["soroush", "soheil", "sorena"]
d = {name:[input(f"Enter {name} Score {i}: ") for i in range(1, 3)] for name in t}
print(d)




