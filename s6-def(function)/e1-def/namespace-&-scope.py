# # print(dir(__builtins__))   # show i name defined in(1: built in) space accessible in every module
# # # built in name are for python
# import math
# pi = 20
# print(pi)
# print(math.pi)
# print(dir(math))  # with defining math in ( dir() )i can give names are in math

# # (2: Global) names are defined in every module
# x = 6
# def A():
#    pass
# globals()['y'] = 33
# print(y)
# print(globals())  # from previous it have some name + names i defined

# # (3: Enclose) it when happen i do nested def(function) definition 
# # Global
# def A():
#    # Enclose
#    x = 10
#    y = 12
#    print('A ->', x, y)
#    print(locals())
#    def A2():
#       # Local
#       x = 22
#       y = 33
#       print('A2 ->', x, y)
#       print(locals())
#    A2()

# def B():
#    x = 9
#    y = 16
#    print('B ->', x, y)
#    print(locals())


# A()
# B()

# # (4: Local) names are defined in (def, class, scope, ...) and can't access from out side
# def A():
#    x = 10
#    y = 12
#    print(x)
#    print(y)
#    print(locals())
   
# def B():
#    x = 9
#    y = 16
#    print(x)
#    print(y)
#    print(locals())


# A()
# B()
# -------------------------------------------------

# x = 10
# if x == 10: # value in if while for in global area
#    y = 12
# print(y)

# x = 6
# def A(): # value in def class have local area
#    x = 16

# A()
# print(x)
# ----------------------------------------------------

# x = 6
# def A(): # value in def class have local area
#    # enclose area
#    x = 3
#    def B():
#       x = 16
#    B()

# A()
# print(x)
# ----------------------------------------------------

# # how accessing global( variable) scope
# x = 5
# def A():
#    x = 2
#    print('A:', x)
#    def B():
#       global x # for accessing and changing global var i use global and name of var in spread line 
#       # to didn't consider it new var or gave me error or change enclose var
#       x += 1
#       print('b:', x)
#    B()
# A()
# print('global:', x)
# ----------------------------------------------------

# how accessing enclose( variable) scope\
# Global
x = 5
def A():
   # enclose
   x = 2
   print('A: 1', x)
   def B():
      # local
      nonlocal x # for accessing and changing Enclose var i use Enclose and name of var in spread line
      # Attention that both ( global, nonlocal) have to use in spread line before do change on that
      x += 1
      print('b:', x)
   print('A: 1', x)
   B()
   print('A: 2', x)
A()
print('global:', x)















