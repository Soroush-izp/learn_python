# Iterate -> تکرار کردن

# Iteration -> for / while

# Iterable -> قابل تکرار / قابل پیمایش


#  __iter__   -> means iterable

# print(dir([2,4,6,8])) # The dir() function returns all properties and methods of the specified object, without the values.
# print( '__iter__' in dir([1,2,3,4]))
# print( '__iter__' in dir(range(10)))
# ---------------------------------------------

# # Iterator -> تکرار کننده / تکرار گر  اخرین وضعیت خود را حفظ می کنند
# i = [2,4,3,6]
# print('__next__' in dir(i))
# i = iter(i) # change to iter( with every iterable can)
# print('__next__' in dir(i))
# # ---------------------------------------------

# # Iterator -> تکرار کننده / تکرار گر  اخرین وضعیت خود را حفظ می کنند
# i = [2,4,3,6]
# print(next(i)) # dives error because it's haven't next
# i = iter(i) # change to iter( with every iterable can)
# print(next(i))
# print(next(i))
# print(next(i))
# # up futures can write like below
# print(i.__next__())
# ---------------------------------------------

# # Iterator -> تکرار کننده / تکرار گر  اخرین وضعیت خود را حفظ می کنند
# i = [2,4,3,6]
# # print(next(i)) # dives error because it's haven't next
# i = iter(i) 
# while 1:
#    try:
#       print(next(i))
#    except StopIteration:
#       break
   
   
# ---------------------------------------------

# # Iterator -> تکرار کننده / تکرار گر  اخرین وضعیت خود را حفظ می کنند
# i = [2,4,3,6]
# # print(next(i)) # dives error because it's haven't next
# i = iter(i) 
# for l in i: # for automatically make it iterator
#    print(l)
   
# ---------------------------------------------

# from itertools import count   # this iterator didn't finish

# counter = count(10)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# ----------

# for i in counter:
   # print(i)



















