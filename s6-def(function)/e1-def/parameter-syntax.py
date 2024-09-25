# normal
# def max3(a, b, c):
#    print( max(a, b, c))

# with this way i can made a default value using( = )
# its considered when i didn't detect argument for it
# def max3(a=12, b=43, c=43):
#    print( max(a, b, c))

# ---

# max3(1, 2, 3)
# ---

# x, y, *z = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("x :", x)
# print("y :", y)
# print("z :", z)

# def max3(a, b, *c):  # when i use * befor y y gave every extra argument for him self( list)
#    print("a :", a)
#    print("b :", b)
#    print("c :", c)
# ---

# def max3(a, b=333, *c, d):  # d can gave value just with name=value argument way because it after ( *c)
#    print("a :", a)
#    print("b :", b)
#    print("c :", c)   # because c with * it can't argumented by name=value way
#    print("d :", d)

# max3(1, 2, 3, 5, 6, 7, 8 , 9, d=32)
# --- dictionary way

# def max3(**a):
#    print("a :", a)
#    print("a :", a['a'])
#    print("b :", a['b'])
#    print("c :", a['c'])
#    print("d :", a['d'])

# max3(a= 1, b= 2, c= 3, d= 4)
# --- dictionary way( combined by normal way)

# def max3(test, **a):
#    print("a :", a)
#    print("a :", a['a'])
#    print("b :", a['b'])
#    print("test :", test)

# max3(36, a= 1, b= 2)
# ---

# def max3(test, c=39, **a): # because i didn't assign the c in argument its use default value
#    print("test :", test)
#    print("c :", c)
#    print("a :", a)
#    print("a :", a['a'])
#    print("b :", a['b'])

# max3(36, a= 1, b= 2)
# ---

def max3(test, c=39, *f, **a): 
   print("test :", test)
   print("c :", c)
   print("*f :", f)
   print("a :", a)
   print("a :", a['a'])
   print("b :", a['b'])

max3(36, 37, 38, 39, 40, 41, 42, 43, 44, a= 1, b= 2)



















