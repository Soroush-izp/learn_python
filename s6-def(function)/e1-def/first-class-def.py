'''
اختصاص دادن مقدار یک تابع به یک متغیر.
فرستادن تابع به عنوان آرگومان تابعی دیگر.
برگردانندن یک تابع به عنوان مقدار نهایی یک تابع دیگر.
ذخیره کردن تابع در داده ساختار های مختلف.
بتواند متد ها و ویژگی های خاص خودش را نگه دارد.
'''

# can be created at run time ( in Run time It will be determined based on my code)
# x = True
# if x: # can be create or didn't create with if statement
#    def func(a):
#       print(a**2)


# # ---

# def A(a):
#    print(a)

#    def B(b):
#       print(b**2)
#    B(a)


# A(5)
# print(A.__name__)
# ----------------------

# # can be assigned to a variable 

# def x(a):
#    print(a**2)


# y = x
# y(3)
# # ----------------------

# # can be passed to another function as an argument

# def descending(list):
#    print(sorted(list))


# def ascending(list):
#    print(sorted(list, reverse=True))


# def mySort(f, myList):
#    f(myList)


# list = [12, 16, 32, 23, 1, 2, 3, 4, 7, 5, 8, 326, 789, 639]
# mySort(descending, list)
# mySort(ascending, list)
# ----------------------

# can be passed to another function as an argument

def mySort(s, myList):
   
   def descending(list):
      print(sorted(list))

   def ascending(list):
      print(sorted(list, reverse=True))

   if s.lower() == 'a': 
      return ascending
   elif s.lower() == 'd':
      return descending

list = [12, 16, 32, 23, 1, 2, 3, 4, 7, 5, 8, 326, 789, 639]
print(mySort('a', list))
print(mySort('d', list))
print(mySort('', list))

func = mySort('a', list)
func(list)

