# encoding & decoding didn't need key
# Ascii & Unicode

c = 45
a = "A"
print(bin(c))
print(ord(a))   # bin() back char to ascii code
print(bin(ord(a)))  # bin() back to binary code
print(chr(65))  # chr() back ascii code to char
# \u with this i can use unicode in my str ""
# \  i can use for showing octal in str ""
# \x use for showing in hex format in str ""
