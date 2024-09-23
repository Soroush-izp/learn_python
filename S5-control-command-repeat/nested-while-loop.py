# # Loop 1
# i = 1
# while i <= 10:
#    # Loop 2
#    j = 1
#    while j <= 10:
#       print("\tj:", j)
#       j += 1
#    print("i:", i)
#    i += 1
# print(F"&&&{i}")
# -------------------------

# l = ['reza', 'soroush', 'neda', 'sam']
# i = 0
# lenL = len(l)
# while i < lenL:
#    j = 0
#    while j < len(l[i]):
#       if j % 2 == 0:
#          print(l[i][j].upper(), end='')
#       else:
#          print(l[i][j], end='')
#       j += 1
#    print()
#    i += 1
# -------------------------

# l = input("name: ").split("-")
# i = 0
# lenL = len(l)
# while i < lenL:
#    j = 0
#    while j < len(l[i]):
#       if j % 2 == 0:
#          print(l[i][j].upper(), end='')
#       else:
#          print(l[i][j], end='')
#       j += 1
#    print()
#    i += 1
# -------------------------

# * table
i = 1
while i <= 10:
   j = 1
   while j <= 10:
      print(F"{i} * {j} = {i * j}", end=" , ")
      j += 1
   print()
   i += 1