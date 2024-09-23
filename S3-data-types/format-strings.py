#     Classic Method

# [(key)] [Flag] [w] [.p] type

# type
# x = 3
# y = 2.32
# print("x : %i\ny : %f\nz : %i"%(x, y, 3 * 3))
# print("%c" % (98))   #char
# print("%c" % (51))   #char
# print("test : %s" % ("sam"))   #char

# %d = int, %o = Octal, %x = Hexadecimal, %e = namad elmi, r = ?
# print("test : %o" %(359))
# print("test : %x" %(359))
# --------------------------

# y = 2.3292657267

# [.p]
# print("test : %.2f" % (y))
# print("test : %.8f" % (y))
# --------------------------

# y = 2.3292657267
# [w] -> length 
# print("%4.2f" % (y))
# print("%9.2f" % (y))
# print("%29.2f" % (y))
# ----------------------

# y = 2.3292657267
# [Flag] -> + - 0
# print("%+6.2f" % (y))
# print("%-26.2f" % (y), "*", sep="")  # using ( - ) flag -> change the direction of [w] overflow
# print("%026.2f" % (y))  
# -------------------------

# [(key)]
# d = { 'a': 2, 'b': 3, 'c': 4, 'd': 5}
# print("%(a)i - %(c)i" %(d))   # we didn't need order to use this method
# -------------------------

# y = 2.3292657267
# p = int(input("P :"))
# # print("%.*f" %(p, y))
# print("%*.*f" %(8, p, y))



#     .Format Method (easy)

# x = 5
# y = 7.554475
# print("X is {}\nY is {}\nZ is {}".format(5, y, 5 + 7))

# x = 5
# y = 7.554475
# print("X is {2}\nY is {0}\nZ is {1}".format(5, y, 5 + 7))
# print("X is {1}\nY is {1}\nZ is {1}".format(5, y, 5 + 7))
# print("X is {}\nY is {}\nZ is {}".format(5, y, 5 + 7))
# --------------------------------------

# x = 5
# y = 7.554475
# d = {'x': 4, 'y': 3, 'z': 38.33}
# print("X is {x}\nY is {z}\nZ is {y}".format(**d))  # use dictionary with key and  input ** befor it
# print("X is {x}\nY is {y}\nZ is {z}".format( x=d['x'], y=d['y'], z=d['z'])) # this is another way
# --------------------------------------

# print("X is {}\nY is {}\nZ is {}".format( *'sor')) # this way work on tavali
# print("X is {}\nY is {}\nZ is {}".format( *[1, 2, 3])) # this way work on tavali
# --------------------------------------

# { [filed_name] [ '!' conversion] [ ':' format_space] }

# print("X is {0!s}".format( 'Soroush'))
# print("X is {0!r}".format( 'Soroush'))
# print("X is {0!a}".format( '+µ')) # for ascii code
# print("X is {:.2}".format( 3.123))
# --------------------------------------

# [[fill]align] [sign] [#] [0] [width][grouping_option][.precision][type]

# [type]
# print("X is {0:%}".format( 1.5644)) # % darsad mi dahad
# print("X is {0:%}".format( 1/3)) # % darsad mi dahad
# print("X is {0:s}".format( 'sdada'))

# [.precision]
# print("X is {0:.4}".format( 12.223312))
# print("X is {0:.6}".format( 12.223312))

# [grouping_option]  for seprate larg num values
# print("X is {0:,.2f}".format( 12223312))
# print("X is {0:_.2f}".format( 12223312))

# [width]
# print("X is {0:8_.2f}".format( 12223333))
# print("X is {0:15,.2f}".format( 12223333))
#     d = int
# [0]
# print("X is {0:015,.2f}".format( 122233))

# [#] -> mabna
# print("b is {0:#b}".format( 122233))
# print("X is {0:#x}".format( 122233))
# print("o is {0:#o}".format( 122233))

# [sign]
# print("o is {0:+}".format( 52))
# print("o is {0:+}".format( -52))
# print("o is {0:-}".format( -52))
# print("o is {0:-}".format( 52))
# print("o is {0: }".format( -52))
# print("o is {0: }".format( 52))

# [[fill]align]  => jahat
# print("o is {0:<15}".format( 12), '*', sep="")
# print("o is {0:>15}".format( 12), '*', sep="")
# print("o is {0:^15}".format( 12), '*', sep="")  # center align
# print("o is {0:=^15}".format( 12), '*', sep="")  # fill with
# print("o is {0:-<15}".format( 12), '*', sep="")
# print("o is {0:+>15}".format( 12), '*', sep="")

# print("o is {0:{align}{sign}{width}}".format( 12, align='<', sign='+', width=18), '*', sep="")   # giving info from user in input fild
# --------------------------------------

      # f-string new way for formating strings   this format way have last version feture 
# x = 'soroush'
y = 3.333
# # print(F"x = {x!r}\ny = {y:.2f}\nz = {3**3}")

# x = 3.5646
# print(F"x = {x:010.2f}\ny = {y:.2f}\nz = {3**3}")

# x = 5
# y = 4.5648
# # print(F"X is {x}")
# # print(F"X is {{x}}") # {{{{{{x}}}}}}
# print("{{}} is {{{{}}}}".format(x, y)) 
# --------------------------------------

# name = "Soroush"
# age = 20

# msg = (  # Trick for making string beautiful
#    F"name: {name}\n"
#    F"age: {age}"
# )
# print(msg)
# --------------------------------------

import datetime

# print(datetime.datetime.now())
# print(datetime.datetime.today())

# today = datetime.datetime.today()

# print(F"year: {today:%Y}")
# print(F"year: {today:%Y/%m***%B, %H:%M}")

x = 5
print(f"{x:<15}*") 