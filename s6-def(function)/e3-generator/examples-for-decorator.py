from functools import wraps
from time import perf_counter

# passwords = {"soroush": '2130842615', "koroosh": '2143178212', "darush": '3212678778'}
# blacklist = {'soroush'}

# # apply this with decorator
# def ban(func): # if user in block list print blocked & prevent process
#    @wraps(func)
#    def inner(*args, **kwargs):
#       if args[0] in blacklist:
#          print('This user is blocked!')
#       else:
#          func(*args, **kwargs)
#    return inner

# @ban
# def print_password(username):
#    print(username, ":", passwords[username])
   
# @ban
# def change_password(username, new_password):
#    passwords[username] = new_password
#    print(username, ":", passwords[username])
   
# # print_password("darush")
# change_password("soroush", '122332')
# ---------------------------

def latency(func):
   @wraps(func)   # prevent rewrite func.__name__ show original func
   def wrapper_decorator(*args, **kwargs):
      start_time = perf_counter()
      value = func(*args, **kwargs)
      end_time = perf_counter()
      run_time = end_time - start_time
      print('the run time of ', func.__name__, 'is: ', run_time)
      return value
   
   return wrapper_decorator

@latency
def A(y):
   s = 0
   for i in range(y):
      s += i**2
      
@latency
def B(x):
   fact = 1
   for i in range(1, x+1):
      fact *= i
      

A(10)
B(5)