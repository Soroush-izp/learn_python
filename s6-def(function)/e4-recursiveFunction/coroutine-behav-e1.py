"""
کروتین‌ها (Coroutines) در پایتون نوعی تابع هستند
که می‌توانند در وسط اجرای خود متوقف شوند و بعداً از همان نقطه ادامه یابند.
این ویژگی به ما این امکان را می‌دهد که برنامه‌هایی با عملکرد غیرهمزمان 
(asynchronous) بنویسیم. کروتین‌ها معمولاً با استفاده از کلمات کلیدی async و await تعریف و استفاده می‌شوند.
"""

# def my_gen():
#    print("Ready!")
#    while 1:
#       yield 1  # i have generator here
#       print("ok!")
      
      
# g = my_gen()
# print(next(g))
# # ------------------

# def my_gen():
#    print("Ready!")
#    while 1:
#       x = yield  # i have generator here
#       print("ok!", x)   # x var given from yield is None
      
      
# g = my_gen()
# next(g)
# next(g)
# # ------------------

# def my_gen():
#    print("Ready!")
#    while 1:
#       x = yield 3 # with define send i can specif what return( save in x) from yield
#       print("ok!", x)   
      
      
# g = my_gen()
# print(g)
# print(next(g)) # here i give val in front yield
# # for using send, i have to use next for program reach to yield after that i can use send
# g.send("Soroush") # i send data have to be return from yield to x var
# g.send("sahand") # out this for next time
# # ------------------

# def my_gen():
#    print("Ready!")
#    for i in range(10):
#       x = yield i # here first something yield after that it run again for return val in x & print that
#       print("ok!", x)   
      
      
# g = my_gen()
# print(next(g)) # here i give val in front yield
# print(g.send("Soroush")) # i send data have to be return from yield to x var
# print(g.send("sahand")) # out this for next time
# # ------------------

# def my_gen():
#    print("Ready!")
#    for i in range(10):
#       x = yield i # here first something yield after that it run again for return val in x & print that
#       print("ok!", x)   
      
      
# g = my_gen()
# print(next(g)) # here i give val in front yield
# print(g.send("Soroush")) # i send data have to be return from yield to x var
# print(g.__next__())
# print(g.send("sahand")) # out this for next time
# ------------------

from functools import wraps

def coroutine(func):
   @wraps(func)   # prevent rewrite func.__name__ show original func
   def start(*args, **kwargs):
      gn = func()
      next(gn)
      return gn
   
   return start

@coroutine  # now with coroutine decorator i can use .send() without next( i add next feature to it)
def my_gen():
   print("Ready!")
   for i in range(3):
      x = yield i # here first something yield after that it run again for return val in x & print that
      print("ok!", x)   
      
      
g = my_gen()

print(g.send("Soroush"))
print(g.send("sahand"))