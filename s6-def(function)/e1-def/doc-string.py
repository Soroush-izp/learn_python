# Doc String use for describing def for user or other programmer or my self in the future
# for making the documentation(Doc string ) for def i have to write(''' ''', """ """) in
# first line after def defined it consider as ( Doc String)

# example
def max3(a, b, c):
   """ Receives three number as input and return biggest num.
   
   Parameters: 
      a (int): A decimal integer
      b (int): Another decimal integer
      c (int): Another decimal integer
   
   Returns:
      max_int (int): Largest of three numbers
   """
   return max(a, b, c)

# for accessing Doc String i use ( .__doc__)
# print(max.__doc__)
# print(max3.__doc__)
# print(help(max3))
# comments about how it works doc string about what its do

# print(len.__doc__)
print(max.__doc__)

# i have to use  .__doc__ without () for example in below print have to use without () parents
# print(print.__doc__)