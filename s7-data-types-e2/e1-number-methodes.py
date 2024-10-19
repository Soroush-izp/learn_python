# divmod(x, y)   # out (x//y, x % y)
# print(divmod(10, 3))   # out (x//y, x % y), (3, 1)

# print(pow(10, 3))   # out pow -> 10 * 10 * 10 = 1000
# print(pow(2, 4, 3))   # out pow -> 2 * 2 * 2 * 2 = 16 % 3 # most used in security

# print(round(12,12314354))  # circle number for me
# print(round(12,12314354, 3))  # circle number for me(in 2th specify circle number until where)

# print(abs(-12.342))  # make numbers positive
# ----

# if i want to see methods & attributes my data type have i can use dir()
# a = 32
# print(dir(a))
# ---

# int methods

# # bit_length  => number of bytes i need for write number in binary
# x = 10
# print(x)
# print(bin(x))
# print(x.bit_length())

# x = .75
# print(x.as_integer_ratio())   # this method give me an ratio( nesbat)
# print((2.5).as_integer_ratio())   # this method give me an ratio( nesbat)

# x = 10   # 1010
# print(x.bit_count()) # number of (num 1) bites when turn number to binary
# print(bin(x))
# # ---

# x = 3 - 4j  # this is complex number
# print(x.imag)  # it show mohomi
# print(x.real)  # it show real
# print(x.conjugate())  # it show mozdavaj (it's make: positive -> negative / negative -> positive)
# ---

# from fractions import Fraction

# x = Fraction(3, 4)   # kasr misazad
# print(x)
# print(x.numerator)   # numerator get out sorat kasr
# print(x.denominator) # denominator get out makhraj kasr

# x = 16
# print(x.denominator)fr
# ---

# x = 16
# # to_bytes : array of bytes 
# print(x.to_bytes())
# print(x.to_bytes(3, byteorder='big', signed=False))  # (num of bytes, order of bytes big, little, motammam 2  True/False)
# # --

# x = 256
# # to_bytes : array of bytes 
# print(x.to_bytes(3, byteorder='little', signed=False))  # (num of bytes, order of bytes big, little, motammam 2  True/False)
# --


# from_bytes : array of bytes to original num ( revers of to_bytes)
# print(int.from_bytes(b'\x00\x01\x00', byteorder='little'))  
# ---------       float methods

f = 16.5
print(f.hex())
print(f.fromhex('0x1.0800000000000p+4'))
print(f.is_integer())   # it's an integer or not True/False

