# mark = int(input("mark: "))
# # print(bool(mark))
# if mark > 10:
#     print("mark score over 10")
#     print("#"*9)
# # else:
# #     print("denied( Rejected)")
# #     print("*"*3)
# print('End')
# -------------------------------

# mark = int(input("mark: "))
# if mark <= 20 and mark >= 15:
#     print("A")
# elif mark < 15 and mark >= 10:
#     print("B")
# elif mark < 10 and mark >= 5:
#     print("C")
# elif mark < 5 and mark >= 0:
#     print("D")
# else:
#     print("Out Of Range")
# print("End")
# -------------------------------

# summarize of up code
# mark = int(input("mark: "))
# if 20 >= mark >= 15:
#     print("A")
# elif 15 > mark >= 10:
#     print("B")
# elif 10 > mark >= 5:
#     print("C")
# elif 5 > mark >= 0:
#     print("D")
# else:
#     print("Out Of Range")
# print("End")
# -------------------------------

# mark = int(input("Num: "))
# # Nested is example
# if mark > 10:
#     print("Ok")
#     if 15 <= mark <=20:
#         print("A")
#     elif 14 > mark > 10:
#         print("B")
# else:
#     print("Rejected")
# -------------------------------

# # Ternary if ( one line if)
# y = 10
# x = 10 + 2 if y < 20 else 5
# print(F"X: {x}")
# -------------------------------

# Ternary if ( one line if)
# y = 10
# x = 33 if y < 20 else 5
# print(F"X: {x}")
# -------------------------------

# Detect Num Are Positive or Negative 
# num = int(input("Num: "))
# if num % 2 == 0:
#     print(F"{num} is Positive")
# elif num % 2 != 0:
#     print(F"{num} is Negative")

# this ( Positive or Negative App ) are more efficient
# num = int(input("Num: "))
# if num % 2 == 0:
#     print(F"{num} is Positive")
# else:   # well if didn't positive its negative so i use else
#     print(F"{num} is Negative")
# -------------------------------

# Find Min Num
min = int(input("Num X: "))
y = int(input("Num Y: "))
z = int(input("Num Z: "))

if y < min:
    min = y
if z < y or z < min:
    min = z
print(F"Min Num: {min}")








