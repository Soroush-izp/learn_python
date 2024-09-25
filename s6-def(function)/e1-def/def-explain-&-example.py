# def cube (x):
#    return x ** 3

# def pass_test (x):
#    pass

# y = cube
# print(y(3))
# ----------------------

# def that give back digit repeat in number

# def repeat(num, d):  # simple way
#    c = 0
#    for i in str(num):
#       if i in str(d):
#          c += 1
#    print(c)

# repeat(13332, 3)
# --- mathematic way

# def repeat(num, d):  # mathematic way
#    c = 0
#    while num > 0:
#       if num % 10 == d:
#          c += 1
#       num //= 10
#    print(c)

# repeat(13332, 3)
# --- simplest way

# def repeat(num, d):  #  simplest way
#    c = str(num).count(str(d))
#    print(c)

# repeat(13332, 3)
# ----------------------

# # sum of factorials up to the selected number (all numbers)
# # 1! + 2! + 3! + 4! + ... + n!   -> n factorial
# # جمع فاکتوریل اعداد از یک تا جایی که مشخص کردیم

# def fact(n):   # for good coding in python i have to have two line empty after def( function)
#    f = 1
#    for j in range(1, n+1):
#       f *= j
#    return f


# def sum_fact(n):   # for good coding in python i have to have two line empty after def( function)
#    sum = 0
#    for i in range(1, n+1):
#       sum += fact(i)
#    return sum


# n = int(input("Enter n!: "))
# print(F"Sum Factorial until {n}:", sum_fact(n))
# ----------------------

# # def name can't be python built in def
# def max3(a, b, c):   # finds maximum num for i
#    n1 = input("Enter N1: ")
#    n2 = input("Enter N2: ")
#    n3 = input("Enter N3: ")
#    return max(a, b, c)


# print(max3())





















