# def list_range(start, end, step=1): # do range work: now i want do this with generator
#    new_range = []
#    while start < end:
#       new_range.append(start)
#       start += step
#    return new_range



# r = range(10, 20, 2)
# # print(r)
# # print(list(r))
# lr = list_range(10, 20, 2)
# print(lr)
# --------------------

# def gen_range(start, end, step=1):  # making range with generator
#    while start < end:
#       yield start
#       start += step
      
      
# gr = gen_range(10, 20, 2) 
# print(gr)
# print(list(gr))
# # # -----------------------

# #  here test making range with normal way & handy way  |result: its better & faster with generator
# from time import perf_counter

# def list_range(start, end, step=1): # do range work: now i want do this with generator
#    new_range = []
#    while start < end:   # its slower because its first make list all of num second work on it
#       new_range.append(start)
#       start += step
#    return new_range


# start = perf_counter()
# lr = list_range(1, 10000)
# s = 0
# for i in lr:
#    if i == 3:
#       break
#    s += i**2
# end = perf_counter()
# print('ln: ', end-start )
# # -

# # so after all  generator is faster and better  because: it makes next element when needed
# def gen_range(start, end, step=1):  # making range with generator
#    while start < end:
#       yield start # generator( yield) -> makes next element when needed
#       start += step

# start2 = perf_counter()
# gr = gen_range(1, 10000) 
# s = 0
# for j in gr:
#    if j == 3:  # when if condition true & loop break happen generator didn't make nexts numbers
#       break
#    s += j**2
# end2 = perf_counter()
# print('gn: ', end2-start2 )
# --------------------

# def my_generator(r=10):
#    for i in range(r):
#       yield i**2
      
      
# g = my_generator()
# print(list(g)) # when i use list its end and can't go to next item
# # ---

# y = my_generator()
# print(sum(y)) # here i can use all feature like sum, avg, min, max, ...
# # ---

# x = my_generator()
# print(max(x)) # here i can use all feature like sum, avg, min, max, ...
# ---     # important

# x = my_generator()
# x.close()   # this close the generator now this generator is useless
# print(list(x)) # its didn't work because i use (.close) feature 
# # ---     # important

# x = my_generator()
# for i in x:
#    if i == 16:
#       x.throw(ValueError("Error !"))  # throw use for Exception in generator( yield)
#    print(i)
# # ---     # important

# def square_gn(r=10):
#    for i in range(r):
#       yield i**2

# def even_gn(r=10):
#    for i in range(r):
#       if i%2 == 0:   # in this situation yield didn't get this number and its good for performance 
#          yield i**2

# sg = square_gn()
# eg = even_gn()

# print(list(sg))
# print(list(eg))
# # ---     # important

# def square_gn(nums):
#    for i in nums:
#       yield i**2

# def even_gn(nums):
#    for i in nums:
#       if i%2 == 0:   # in this situation yield didn't get this number and its good for performance 
#          yield i**2

# sg = square_gn([1, 2, 3])
# eg = even_gn([1, 2, 3, 5, 7, 8, 10, 12])

# print(list(sg))
# print(list(eg))
# ---     # important

def square_gn(nums):
   for i in nums:
      yield i**2

def even_gn(nums):
   for i in nums:
      if i%2 == 0:   # in this situation yield didn't get this number and its good for performance 
         yield i**2

print(sum(square_gn(even_gn([1, 2, 3, 4, 7, 9, 1, 5, 2, 9, 6])))) # here i use combination off these generators end with sum 
# 2, 4, 2, 6
# 4, 8, 4, 36
# sum of all at the end