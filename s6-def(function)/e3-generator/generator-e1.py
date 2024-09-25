# def func(x):
#    return x**2
# # ---

# def func(x):
#    yield x**2  # for generator i use yield -> yield wait for next to run again
#    print('x')
   
# x = func(5)
# print(x)
# print(next(x))
# print(next(x))
# # ---

# def func(x):
#    print('space0')
#    yield x**2  # for generator i use yield -> yield wait for next to run again( out next item)
#    print('space1')
#    yield 5  # for generator i use yield -> yield wait for next to run again
#    print('space2')
#    yield 'ok'  # for generator i use yield -> yield wait for next to run again
   
# x = func(5)
# print(x)
# print(next(x))
# print(next(x))
# # ---

# # generator didn't make(generate) anything until i want from him
# def generator():
#    for i in range(1000):
#       yield i**2


# g = generator()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# # ---

# # generator didn't make(generate) anything until i want from him
# def generator():
#    for i in range(5):
#       yield i**2  # here when it higher than range number generate  StopIteration error


# g = generator()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# # print(next(g))  # because its 6th it gave me error (StopIteration) -> range(5)
# # in for its managed automatically with for statement
# ---

# generator didn't make(generate) anything until i want from him
def generator():
   for i in range(5):
      yield i**2  # here when it higher than range number generate  StopIteration error


g = generator()
i = iter([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(next(i))  # with for StopIteration error managed automatically
for g in i:
   print(g)
