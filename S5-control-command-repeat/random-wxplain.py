# ----------------------

# import random  # for use random package

# random.randint()
# random.choice()
# ----
# or 
# from random import randint
# ----------------------

# from random import random  # between 0 and 1 (1 didn't exist)
# print(random())
# ----------------------

# from random import random, seed
# seed(3)  # seed feature generate predictable random sequence num based on num we input on it
# # if seed is empty it gave us num based on system time( time of day)
# print(random())
# print(random())
# print(random())
# print(random())
# # it help to now( predict) what random sequence of num generated
# ----------------------

# from random import random, seed
# seed()  # if seed is empty or undefined it gave us num based on system time( time of day)

# print(random())
# print(random())
# print(random())
# print(random())
# it help to now( predict) what random sequence of num generated
# ----------------------

# from random import random, seed

# # random shape :=> random()
# # formula for gave random sequence:=>  min + (rand * (max - min))
# min = 5
# max = 15
# # 15 - 5 between these num( its never be max number) solution for this
# # problem is gave it type int and ( max + 1)
# for _ in range(10):  # when i didn't use index in for i can set ( _ ) instead of var
#    print(min + ( random() * (max - min))) # with this formula I can gave random sequence
# ------------------------------------

# # or simples way for making sequence of number with out needing formula is ( uniform)
# from random import random, uniform
# for _ in range(10):
#    print(uniform(5, 15))
# # ------------------------------------

# # or simples way for making sequence of number with out needing formula is ( uniform)
# from random import random, uniform
# for _ in range(10):
#    print(uniform(5, 15 + 1))   # didn't forgot max always have be( plus 1) - (5 - 15)
# # ------------------------------------

# # i can use randint for making random int
# from random import randint
# for _ in range(10):
#    print(randint(5, 15))   # in randint i didn't need (max + 1) ( max plus 1) its normally work
# # ------------------------------------

# # i can  use randrange for making sequence of radom number with step
# from random import randrange
# for _ in range(10):
#    print(randrange(4, 100, 2))   # this example make sequence of random positive number 
#    # between (4 and 100) because it started with 4 and ends with 100 with step of 2
# # ------------------------------------

# how i choose random value from list
# one way is
# from random import randint
# l = [33, 65, 78, 93, 99, 102, 321, 378]
# for _ in range(10):
#    print(l[randint(0, len(l) - 1)])   # its have to be minus 1 because list start with 0
# between (4 and 100) because it started with 4 and ends with 100 with step of 2

# # ------------------------------------

# # how i choose random value from list
# # simples way is using choice
# from random import choice
# l = [33, 65, 78, 93, 99, 102, 321, 378]
# for _ in range(10):
#    print(choice(l))  # choice is best way for choosing random value from list
# # ------------------------------------

# # how i make Random list from( with) another list( sample )
# from random import sample
# l = [33, 65, 78, 93, 99, 102, 321, 378, 98, 999]

# # for _ in range(10):
# #    print(sample(l, 3))  # sample(list, numberOfRandomChosenElement)
# for _ in range(10):
#    print(sample(l, 9))  # sample(list, numberOfRandomChosenElement)
# ------------------------------------

# # list ra shansi bor mi zanad 
# from random import shuffle
# l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print(l)  
# shuffle(l)  # attention that it make changes on main list   
# print(l)  
#     .copy
# ----------------------

'''
   attention that i can use numpy
   for making random number 
   num py are advanced and use for  ( AI )
'''
# ------------------------------

# # shir khat game with random
# from random import choice

# coin = ['shir', 'khat']
# sh = kh = 0
# for _ in range(1000):
#    if choice(coin) == 'shir':
#       sh += 1
#    else:
#       kh += 1
# print(F"Shir: {sh}\nKhat: {kh}")
# ------------------------------

from random import randint
# meghdar tas 

tas = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for _ in range(1000):
   tas[randint(1, 6)] += 1
print(tas)





