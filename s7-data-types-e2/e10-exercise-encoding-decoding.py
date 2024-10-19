"""
    )1رشته “ ”!Hello, Worldرا  Encodeکنید(با استفاده از انکدینگ
 )UTF-8و آن را چاپ کنید
"""
#
# chr = "!Hello, World"
# encoded_chr = chr.encode('UTF-8')
# print(encoded_chr)
# ---
#
"""
    بایت های زیر را با استفاده از انکدینگ  UTF-8دیکد )(decode
کنید و رشته  decodeشده را چاپ کنید:
b’My name is M\xc3\xb6bius’
"""
#
# chr = b'My name is M\xc3\xb6bius'
# docoded_chr = chr.decode('UTF-8')
# print(docoded_chr)
# ---

"""
    لیستی از کاراکترها را داریم، هر کاراکتر را به مقدار ASCII
مربوطه تبدیل کنید و نتایج را در یک لیست جدید ذخیره کنید.
"""

# l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# new_list = [ ord(i) for i in l] # i'm using comprehension method here
# print(new_list)
# ---

"""
    یک جمله از کاربر بگیرید و سپس مجموع مقادیر  ASCIIتمام
کاراکترهای جمله را محاسبه و چاپ کنید
"""

# sentence = input("Enter a sentence: ")
# sentence_char_code = [ord(chr) for chr in sentence] # comprehension method
# print(sentence_char_code)
# print(sum(sentence_char_code))
# ---

"""
    لیست زیر شامل  unicode code pointها است. با استفاده
از انکدینگ  UTF-16آن ها را به بایت  encodeکنید و نتیجه را
چاپ کنید.
————————————————————]1024 ,5678 ,234 ,987[
————————————
"""

# code_points = [1024, 5678, 234, 987]
# encoded_bytes = b''.join(chr(cp).encode('utf-16') for cp in code_points)
# print(encoded_bytes)
# ---

"""
    بایت های زیر را با استفاده از انکدینگ  UTF-16دیکد کنید و
رشته  decodedشده را چاپ کنید

b’\xff\xfeM\x00y\x00 \x00N\x00a\x00m\x00e\x00′
"""

# byte_data = b'\xff\xfeM\x00y\x00 \x00N\x00a\x00m\x00e\x00'
# decoded_string = byte_data.decode('utf-16')
# print(decoded_string)
# ---

"""
    تابعی بنویسید که رشته ای را به عنوان ورودی میگیرد و نمایش
هگزادسیمال بایت های انکد شده  UTF-8را برمی گرداند
"""

def str_encode_to_hex(s):
    byte_data = s.encode('utf-8')   # encode to utf-8
    return byte_data.hex()  # hex show

print(str_encode_to_hex('hello'))