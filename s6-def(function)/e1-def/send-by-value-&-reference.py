# def func(a):
#    a += 1
#    print(a)

# x = 1
# func(x)   # here pass by value happen( a copy send)
# print(x) # x didn't change because mutable & immutable data types
#  in python everything object and sending arguments are in reference way
# in c/c++ i have to use ( &) before var to send call by reference  

# # mutable -> تغییر پذیر
# # mutable -> objects when we change them they changing without id changing( they changeable data)
# x = [2, 3]
# print(id(x))
# x += [5, 9]
# print(id(x))

# # immutable -> تغییر ناپذیر
# bolean number string tuple, ... they behavior like send pass by value
# (Even though everything is sent by reference)

# # immutable -> objects when we change them they changing with id changing( make new value
# # with every changes)(they onchangable data)
# x = 2
# print(id(x))
# x += 3
# print(id(x))


'''
# mutable values
   list
   Dictionaries 
   Sets
   Byte arrays
'''
'''
# immutable
   Numbers
   Strings
   Tuples
   Bytes
   Booleans
   Frozen sets
'''
# attention when i using = i make a new var and didn't consider before
# when i want send by value i have to send a copy off that value ( [:], copy.deepcopy() )
# for nested list its important

def func(a):
   a += 1
   print(a)
   return a

x = 1
x = func(x) # with this way i can have changes out of def
print(x)






