# decorator
# توابع تو در تو
# ارسال تابع به عنوان ارگومان
# decorator get another def and return it with more feature with another def

# def dec(func):
#    def inner():
#       print('*'*30)
#       func()
#       print('*'*30)
#    return inner


# def func():
#    print('reza')


# def func2():
#    print('ali')


# d = dec(func)
# d2 = dec(func2)
# # print(d)
# d()
# d2()
# # ----------------------------

# def dec(func):
#    def inner():
#       print('*'*30)
#       func()
#       print('*'*30)
#    return inner


# @dec  # this is way for using def easy
# def func():
#    print('reza')


# @dec  # for use this i have to write @nameOfDecoratorFunc
# def func2():
#    print('ali')


# func()
# func2()
# ----------------------------

# another example for add feature to def with decorator
def dec(func):
   def inner(a, b):
      if b == 0:
         print("Warning!!!")
      else:
         func(a, b)
   return inner


@dec  # easy way for using decorator
def func(a, b):
   print(a*b)


# # using decorator with hard way
# func1 = dec(func)
# func1(5, 10)

func(10, 0)













