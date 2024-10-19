# some type in py ver 3

# ver 3
# ordinary str s (ascii, uni-code)
# bytes - binary datas
# bytearray - binary changeable datas
# s = b"a"
# s0 = bytes("a", "utf-8")
# s1 = bytearray("a", "utf-8")
#
# print(type(s))
# print(type(s0))
# print(type(s1))
# ---

# # name = b"SoroushΪ"  # this give me error of just can contain ascii literal ( Ϊ)
# name = bytes("SoroushΪ", 'utf-8')  # when I use utf-8 encoding its well be ok
# print(name) # because these two( \xce\xaa) with together have meaning its showed in print separated
# print(name[0]) # here in this way i can move on str chr like lists and it's out ascii code of them for me
# print(chr(name[3])) # here in this way i can move on str chr like lists and it's out ascii code of them for me of cours i see the chr with chr() method
# print(name.decode('utf-8')) # when I do decode on it can sense right what it is
# print(type(name))
#
# print(chr(0xa6))
# # ---
#
# name = bytes(5) # create 5 bytes 0 for me
# print(name)
# print(type(name))
# ---
#
# name = bytes('SoroushÇ', 'utf-8')
# print(name)
# print(name.decode())
# print(type(name))

# .encode() # for encode ing can be in utf-8
# .decode() # for decode ing can be in utf-8
# # ---
#
# # now i want use bytearray() it's mutable -> changable
#
# name = bytearray('SoroushÇ', 'utf-8')
# name[0] = 126   # i can perform this change in bytes, it's doable in bytearray
# print(name.decode())
# print(type(name))
# ---
#

# name = bytes('SoroushÇ', 'ascii', 'namereplace') # for handle situation i use third args methods(strict -> give error, ignore, replace -> with ?, backslashreplace, namereplace
# print(name)
# print(type(name))
# ---

print((12).to_bytes(4, 'big'))