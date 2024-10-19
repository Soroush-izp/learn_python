"""
    یک شی بایت ایجاد کنید و نمایش هگزادسیمال آن را چاپ
کنید
"""

# # ایجاد یک شی بایت
# # byte_obj = bytes([0x45, 0x67, 0x89, 0xAB])
# byte_obj = bytes("soroush", 'utf-8')
#
# # تبدیل بایت‌ها به نمای هگزادسیمال
# hex_representation = byte_obj.hex()
#
# # چاپ نمای هگزادسیمال
# print("Hexadecimal representation:", hex_representation)
# ---

"""
    یک رشته هگزا دسیمال را به  bytearrayتبدیل کنید
"""

# hex_string = '736f726f757368'
# byte_array = bytearray.fromhex(hex_string)  # here i change hex to bytearray
# print(byte_array)
# ---

"""
    یک  bytearrayایجاد کنید و عناصر آن را ویرایش کنید
"""

# byte_array = bytearray("Soroush", "utf-8")
# byte_array[2] = 32
# print(byte_array)
# ---

"""
    دو شی  byteرا به هم متصل کنید
"""

# byte_array1 = bytes("Soroush", "utf-8")
# byte_array2 = bytes("Soroush", "utf-8")
#
# full_byte_array = byte_array1 + byte_array2
# print(full_byte_array)
# ---

"""
    بررسی کنید که آیا مقدار  byteخاصی (مثلا  )20در bytearray
وجود دارد یا خیر
"""

# byte_array = bytearray("Soroush ", "utf-8")
# print(32 in byte_array)
# print(b'f' in byte_array)
# print(b'S' in byte_array)
# ---

"""
    یک  bytearrayرا به لیستی از اعداد صحیح تبدیل کنید
"""

# byte_array = bytearray("Soroush ", "utf-8")
# int_list = [n for n in byte_array]  # i use comprehension method here
# print(int_list)
# ---

"""
    ایندکس یک مقدار  byteخاص را در  bytearrayپیدا کنید
"""

if_exist = []
byte_array = bytearray("Soroush ", "utf-8")
if_exist.append(byte_array.index(b'S'))
if_exist.append(byte_array.index(b'o'))
if_exist.append(byte_array.index(32))
print(if_exist)
