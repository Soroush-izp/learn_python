# walrus ->  :=

# x = 3
# print(x=3)    # it gives me an error
# print(x==2)
# print(x:=2) # change x to 2
# print(x:=2 < 3) # with walrus assign 2 to x & check it is smaller then 3
# ------------

# it isn't efficient
# x = []
# s = input("enter q) for quit:")
# while s.lower() != "q":
#     x.append(s)
#     s = input("enter q) for quit:")
# print(f"Names: {x}")
# ---

# # this code more efficient then up code
# x = []
# while (s:=input("enter (q for quit: ").lower()) != 'q': # so with walrus i can give var value in condition & work with var
#     x.append(s)
# print(x)
# ------------------

# def func(x):
#     print(x ** 3)
# func(x:=9)
# print(x)    # i can access x changed out of func
# ----------------

# x = (z := 3)    # if := be in () can work fine
# print(f"x is {x}")
# print(f"z is {z}")

# most of the time i have to use walrus := in ()
# # ------------------
#
# def func(x=(c := 5)):
#     print(x ** 2)
#
#
# print(c)
# func()
# func(2)
# # ------------------
#
# def func(x: (c := 5) = 6):
#     print(x ** 2)
#
# print(c)
# func()
# func(2)
# # --------------
#
# f = lambda x: (c := x ** 2) # c in here is use less
#
# print(f)
# print(f(2))
# # print(c)    # this gives me error
# # --------------
#
# s = -3
# print(f"{s:=5}")    # this back to str method
# print(f"{(s:=5)}")    # i have to put this in () to work
# print(s)
# --------------

l = [1, 2, 3]

# this d isn't efficient
# d = {
#     "s": sum(l),
#     "l": len(l),
#     "a": sum(l) / len(l)
# }
# --

# here i use more efficient way
d = {
    "s": (s := sum(l)),
    "l": (l := len(l)),
    "a": s/l
}

print(d)

