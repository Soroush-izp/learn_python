'''
)1تابعی بنویسید که که کار تابع داخلی  lenرا انجام دهد.
'''
# def lenP(v):
#    count = 0
#    for _ in v:
#       count += 1
#    return count


# print(lenP('wertyuiop'))
# -------------------------------

'''
تابعی بنویسید که که کار تابع داخلی  maxیا  minرا انجام
دهد
'''
#     Max
# def max1(*val):
#    max = val[0]
#    for i in val:
#       if i > max:
#          max = i
#    return max


# print(max1(2, 5, 10, 25, 54, 105, 168, 255, 324, 289))

#    #  Min
# def min1(*val):
#    min = val[0]
#    for i in val:
#       if i < min:
#          min = i
#    return min


# print(min1(2, 5, 10, 25, 54, 105, 168, 255, 324, 289))
# --------------------------------

'''
 )3تابعی بنویسید که که کار تابع داخلی  sumرا انجام دهد.

'''
# def sum1(val):
#    sum = 0
#    for i in val:
#       sum += i
#    return sum


# print(sum1([2, 4, 6, 6]))
# --------------------------------

'''
تابعی بنویسید که که یک عدد به عنوان ورودی گرفته تشخیص
دهد عدد مربع است یا خیر
'''
# n = int(input("n: "))
# for i in range(n):
#    f = i * i   # or i ** 2 | power 2
#    if f == n:
#       print(F"number is Square({i} * {i} = {n})")
#       break
#    # elif f > n:
#    #    print("number is not square")
#    #    break
# else:
#    print("number is not square")
# -------------------------------------

'''
تابعی بنویسید که قیمت کالا و درصد تخفیف را گرفته و قیمت
پس از تخفیف را محاسبه کند
'''
# def discount(price, discount):
#    discount_rate = (price * discount / 100 )
#    result = price - discount_rate
#    print("Discount Rate:", discount_rate)
#    print("New Price:", result)


# rate = int(input("rate: "))
# price = int(input("price: "))
# discount(price, rate)
# -------------------------------------------

'''
تابعی بنویسید که یک کاراکتر را خوانده و مشخص کند کاراکتر
یک رقم، حرف بزرگ، حرف کوچک و یا سایر نماد ها است
'''
def char_Acquaintance(char):
   chr = ord(char)
   if 48 <= chr <= 57:
      print("The char is number")
   elif 65 <= chr <= 90:
      print("The char is upper case str")
   elif 97 <= chr <= 122:
      print("The char is lower case str")
   elif 32 <= chr <= 47 or 58 <= chr <= 64 or 91 <= chr <= 96 or 123 <= chr <= 126:
      print("The char is from other symbols")
   else:
      print("Other!")


chr = input("Enter Char: ")
char_Acquaintance(chr)



