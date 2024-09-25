# def func(a, *, b, c):   # in parameters when i use * parameters after that just can give name=value arguments
#    print('a: ', a)
#    print('b: ', b)
#    print('c: ', c)
# func(12, b=32, c=34)

# def func(a, b, /, c):   # in parameters when i use / parameters before that just can give ordered arguments
#    print('a: ', a)
#    print('b: ', b)
#    print('c: ', c)
# func(12, 33, c=34)

   # in parameters when i use * parameters after that just can give name=value arguments
   # in parameters when i use / parameters before that just can give ordered arguments
def func(a, b, /, c, d, *, e, f, g):   
   print('a: ', a)
   print('b: ', b)
   print('c: ', c)
   print('d: ', d)
   print('e: ', e)
   print('f: ', f)
   print('g: ', g)
func(12, 33, 34, 35, e=36, f=37, g=38)














