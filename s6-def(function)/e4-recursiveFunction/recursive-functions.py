# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!

# # fact just with for loop
# def fact(x):
#    f = 1
#    for i in range(1, x+1):
#       f *= i
      
      
#    return f


# print(fact(5))
# ------

# fact with recursive function
def rec_fact(x):
   if x == 0:  # it's required i have to add stop condition for fact
      return 1
   else:
      return x * rec_fact(x-1)
   

print(rec_fact(3))