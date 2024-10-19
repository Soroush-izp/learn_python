print(dir(str))

# casefold -> change to short letters
s = "SOROUSHIZADPANAH"
# print(s.casefold()) # .casefold() like .lower() but powerfuller then it

# print(repr(s.center(30, 'f'))) # put my str in center of length i specify, i choose full with what in arg 2
# .expandtabs() -> replace tab with space
# ---

d = {'f': "Soroush", 'l': "Izadpanah"}
# print("My Name is {f} - {l}".format_map(d)) # with .format_map() i can use dec key value in f string
# .index() find char index in str  it like (.find() but find when didn't find turn -1 to me this give error)

# .isalpha() -> if all in str are letter it give me True
# .isascii() -> all are ascii

# all of them are the same but they have difference in them focuses (a good answer exist in stackoverflow)
# their ordered based on their focus from top to bottom
# .isnumeric() -> all are 0 to 9
# .isdecimal() -> all are 0 to 9
# .isdigit() -> all are 0 to 9
# ---

# .isidentifier() -> if name i give to it is ok for naming var, user, etc it turn True for me
# .isprintable() -> check its ok for print
# .isspace() -> all of my str is space ' '
# .istitle() -> capitalize first letter of each word
# .isupper() -> all of letters are capital or not
# .ljust() -> go everything to left in length i specify, these like .center()
# .rjust() -> go everything to right in length i specify, these like .center()
# ---

# table = str.maketrans("S", "f", "O")    # O choos to be delete
# print(s)
# print(table)
# print(s.translate(table))   # do somthing like translate base on my table -> i can make it with dic or with .maketrans() method
# ---

# .partition()  -> turn tuple with befor himself after thing i specify, i can make it from rigth with r first of it
# --

# removeprefix(), removesuffix()  -> remove one what i specify from start & end of str
# lstrip(), rstrip()  -> remove all what i specify from start & end of str, order of what have to be delete isn't important
# .split() -> create list seprate by what i specify, i can choos num of what have to be seprat
# .splitlines() -> create list and seprate by new line '\n'

# .swapcase() -> revers letters capital, small situation

# zfill() -> fill our value base what i specify, it's help full for clock, etc pj