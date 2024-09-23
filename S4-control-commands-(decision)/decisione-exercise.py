'''
یک عدد از کاربر بگیرید و بررسی کنید که آیا هم بر  2و هم بر 5
بخش پذیر است یا نه؟
'''
# num = int(input("Enter Number: "))
# if num % 2 == 0 and num % 5 == 0:
#    print(F"{num} divisible in 2 | 5")
# else:
#    print(F"{num} not divisible in 2 | 5")

# way 2
# num = int(input("Enter Number: "))
# if num % 10 == 0: # num are divisible in 2 & 5 have 0 in rightest digit
#    print(F"{num} divisible in 2 & 5")
# else:
#    print(F"{num} not divisible in 2 | 5")
# ------------------------------

'''
اضلاع یک مثلث را از کاربر گرفته و مشخص کنید که آیا این
اضلاع تشکیل مثلث میدهند یا خیر؟ اگر جواب مثبت است، چه
نوع مثلثی؟ (مثلا متساوی الساقین، مختلف الاضلاع، قائم الزاویه
یا متساوی الاضلاع)
'''
# t1, t2, t3 = [int(x) for x in input("Enter the 3 sides of the triangle separate by(,): ").split(',')]
# if t1 < t2+t3 and t2 < t1+t3 and t3 < t1+t2:   # The sum of two side of triangle are more then another one 
#     print("It is a triangle")
#     if t1 == t2 or t2 == t3 or t3 == t1: # متساوی الساقین
#         print("Isosceles triangle") # just 2 sides are equal
#     if t1 != t2 and t2 != t3 and t1 != t3:  # مختلف الاضلاع
#         print("Different sided triangle") #  3 sides aren't equal
#     if (t1 ** 2 == t2 ** 2 + t3 ** 2) or (t2 ** 2 == t1 ** 2 + t3 ** 2) or\
#      (t3 ** 2 == t2 ** 2 + t1 ** 2): # قائم الزاویه
#         print("perpendicular triangle") #  The power of 2 of one side is equal to the sum
#         # of the powers of the other 2 sides
#     if t1 == t2 and t2 == t3:  # مثلث متساوی الاضلاع
#         print("Equilateral triangle") #  3 side are equal (60)
# else:
#     print("It isn't triangle")
# -----

#   master way
# x = int(input("X: "))
# y = int(input("Y: "))
# z = int(input("Z: "))

# if x < y+z and y < x+z and z < x+y: # The sum of two side of triangle are more then another one 
#     print("It is a triangle")
#     if t1 == t2 and t2 == t3:  # مثلث متساوی الاضلاع
#         print("Equilateral triangle") #  3 side are equal (60)
#     if t1 == t2 or t2 == t3 or t3 == t1: # متساوی الساقین
#         print("Isosceles triangle") # just 2 sides are equal
#     if t1 != t2 and t2 != t3 and t1 != t3:  # مختلف الاضلاع
#         print("Different sided triangle") #  3 sides aren't equal
#     if (t1 ** 2 == t2 ** 2 + t3 ** 2) or (t2 ** 2 == t1 ** 2 + t3 ** 2) or\
#      (t3 ** 2 == t2 ** 2 + t1 ** 2): # قائم الزاویه
#         print("perpendicular triangle") #  The power of 2 of one side is equal to the sum
#         # of the powers of the other 2 sides
# else:
#     print("It isn't triangle")
# ------------------------------

'''
یک کاراکتر از کاربر بگیرید و مشخص کنید کاراکتر وارد شده عدد
است، حروف انگلیسی است یا سایر نماد ها
'''
char = ord(input("just Enter char: "))
if 48 <= char <= 57:
    print("it's number")
elif 65 <= char <= 90 or 97 <= char <= 122:
    print("it's English char")
else:
    print("Other!")




