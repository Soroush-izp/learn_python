# Normal

# s = []
# for i in range(10):
#     s.append(i ** 2)
# print(s)
# ---------

# # Comprehension
# l = [ i ** 2 for i in range(10)]    # in this code i use comprehension
# print(l)
# --- i can do this with map

# s = list(map(lambda i: i ** 2, range(10)))
# print(s)
# ------

# l = ["Soroush", "Ali", "Soheil", "saeed"]
# print([ch for name in l for ch in name])    # in comprehension last thing have to write first
# # -----
#
# matrix = [
#     [1, 2, 3, 16],
#     [4, 5, 6, 16],
#     [7, 8, 9, 16]
# ]
#
# t = [[row[i] for row in matrix]for i in range(4)]   # here i write nested comprehension (nested sumoriz)
# for j in t:
#     print(j)
# ----------

# I can use zip for this too
x1 = [2, 4, 6, 32]
x2 = [3, 6, 26, 33]

print(list(zip(x1, x2)))    # give from each list element in same col