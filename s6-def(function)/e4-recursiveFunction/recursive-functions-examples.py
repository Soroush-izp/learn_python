# import time
# def timer(x):
#    print(x)
#    if x == 0:
#       return # break if condition is True
#    time.sleep(1)
#    timer(x-1)
   
   
# timer(10)
# # ---

# """
# برنامه ای که حاصل ضرب ارقام بزرگتر از 5 یک رقم را حساب کند 
# """

# def mul5(x):
#    if x == 0:
#       return 1
#    elif x % 10 < 5:
#       return mul5(x//10)
#    else:
#       return x % 10 * mul5(x // 10)
   
   
# print(mul5(123456))
# # ---

# """
# برنامه ای که مضارب 3 را تا ان عددی که تعیین کردیم بگیرد
# """

# def m3(x):
#    if x < 3:
#       return
#    elif x % 3 == 0:
#       print(x)
#       return m3(x-1)
      
#    return m3(x-1)
   
   
# m3(10)
# ---

def fib(n):
   if n == 0 or n == 1:
      return n
   return fib(n-1) + fib(n-2)

print(fib(7))