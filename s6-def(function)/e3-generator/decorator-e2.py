# def star(func):
#    def inner(*args, **kwargs):
#       print('*' * 30)
#       func(*args, **kwargs)
#       print('*' * 30)


#    return inner

# @star
# def msg(m):
#    print(m)

# msg('msg test')
# # ----------------------

# def star(func):
#    def inner(*args, **kwargs):
#       print('*' * 30)
#       m = func(*args, **kwargs)
#       print('*' * 30)
#       return m

#    return inner

# @star
# def msg(m):
#    return m

# print(msg('msg test'))
# # ----------------------

# def dash(func):
#    def inner(*args, **kwargs):
#       print('-' * 30)
#       func(*args, **kwargs)
#       print('-' * 30)
#    return inner

# def plus(func):
#    def inner(*args, **kwargs):
#       print('+' * 30)
#       func(*args, **kwargs)
#       print('+' * 30)
#    return inner

# def star(func):
#    def inner(*args, **kwargs):
#       print('*' * 30)
#       func(*args, **kwargs)
#       print('*' * 30)
#    return inner

# @dash
# @plus
# @star
# def msg(m):
#    print(m)

# msg('msg test')
# # ----------------------

# def dash(func):
#    def inner(*args, **kwargs):
#       print('-' * 30)
#       func(*args, **kwargs)
#       print('-' * 30)
#    return inner

# def plus(func):
#    def inner(*args, **kwargs):
#       print('+' * 30)
#       func(*args, **kwargs)
#       print('+' * 30)
#    return inner

# def star(func):
#    def inner(*args, **kwargs):
#       print('*' * 30)
#       func(*args, **kwargs)
#       print('*' * 30)
#    return inner

# # @dash
# # @plus
# # @star
# def msg(m):
#    print(m)

# msg('msg test')

# # up decorator simply like this
# printer = dash(plus(star(msg)))
# printer('test')
# ------------------------

# def star(x):
#    def inner1(func):
#       def inner2(*args, **kwarg):
#          print('*' * x)
#          func(*args, **kwarg)
#          print('*' * x)

#       return inner2

#    return inner1

# @star(20)   # i can give decorators args : i have add another def for giving func
# def msg(name):
#    print("I am " + name)

# msg("test")
# # # ----------------------

# # import functools
# from functools import wraps   # this is shorter
# def star(func):
#    # @functools.wraps(func)  # info in func -> msg copy & didn't rewrite
#    @wraps(func)  # info in func -> msg copy & didn't rewrite
#    def inner(*args, **kwargs):
#       print('*' * 30)
#       func(*args, **kwargs)
#       print('*' * 30)
#    return inner

# @star
# def msg(m):
#    """ prints a message """
#    print(m)

# # msg('msg test')

# print(msg.__doc__)   # doc string
# print(msg.__name__)  # name(func)
# ---------------------------------------

# a good formula for making decorator and use functools
import functools


def latency(func):
    @wraps(func)  # prevent rewrite func.__name__ show original func
    def wrapper_decorator(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print("the run time of ", func.__name__, "is: ", run_time)
        return value

    return wrapper_decorator


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        # do something after
        return value

    return wrapper_decorator
