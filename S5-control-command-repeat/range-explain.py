
# print(range(10))
# print(type(range(10)))  
# print(list(range(10)))
# --------------------------

# x = list(range(10))
# print(x)
# --------------------------

# for i in range(5):
#    print(i)
# --------------------------

# for i in range(2, 8): # i can choose start and end for range
#    print(i)
# --------------------------

# for i in range(1, 10, 2): # i can choose step for range( ghadam)
#    print(i)
# ----------------------------

# for i in range(-20, -180, -20):
#    print(i)
# ----------------------------

# l = input("names: ").split('-')
# for i in range( len(l)):
#    print(i, l[i])
# ----------------------------

# factorial multiply from 1 to num  5 -> 1 * 2 * 3 * 4 * 5 = fact(5)
# l = int(input("num: "))
# fact = 1
# for i in range(1, l+1):
#    fact *= i
# print(fact)
# ----------------------------

# makos str
# l = input("num: ")
# for i in range(len(l) - 1, -1, -1):
#    print(l[i], end="")
# ----------------------------

# makos int( num)
# l = input("num: ")
# s = ""
# for i in range(len(l)-1, -1, -1):
#    s += l[i]
# print(int(s))
# ----------------------------

n = int(input("num: "))
for i in range(1, n+1):
   for j in range(1, i+1):
      print(j, end="")
   print()
for i in range(n - 1, 0, -1):
   for j in range(1, i+1):
      print(j, end="")
   print()




















