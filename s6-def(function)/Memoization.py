# 0   1  1  2  3  5  8  13   21  ...
# 0   1  2  3  4  5  6  7    8   ...

# here i use decorator for save result in dict & prevent repeating calculation
import functools

def memoize(func):
    memory = {} # save all answers(value) with input(key) in this dict for prevent recalculating
    @functools.wraps(func)  # prevent rewrite func
    def wrapper_decorator(n):
        if n not in memory:
            memory[n] = func(n)
        return memory[n]
    return wrapper_decorator


@memoize    # this decorator prevent recalculate in recursive function
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(40))
