# from time import sleep
# import functools

# def dec(func):
#     @functools.wraps(func)  # prevent rewrite func.__name__ show original func
#     def wrapper_decorator(*args, **kwargs):
#         print('*'*40)
#         value = func(*args, **kwargs)
#         print('-'*40)
#         return value

#     return wrapper_decorator


# @dec
# def rev(n):
#     if n <= 0:
#         return
#     sleep(0.5)
#     print(n)
#     rev(n - 1)


# rev(10)
# -----------------------   # how use recursive func with generator

from time import sleep

import sys    # work with system
print(sys.getrecursionlimit())  # get limit of saving data in stack
# print(sys.setrecursionlimit(15))  # set limit of saving data in stack
# these method good for manage resources & prevent end less loop

def g_rev(n):
    if n <= 0:
        return
    sleep(0.5)
    yield n
    # g_rev(n - 1)    # (this is another generator) now (it have to be used like below)
    for i in g_rev(n - 1):
        yield i


g = g_rev(10)
# print(g)    # <generator object g_rev at 0x000001A80B2D36B0>
print(list(g))