'''
فرض کنید شما قرار است یک دیکشنری واقعی بنویسید. با
استفاده از نوع داده دیکشنری آن را پیاده سازی کنید. دقت کنید
که کلمه اصلی باید کلید دیکشنری باشد و معانی آن میتوانند
بیشتر از یک کلمه باشند. معانی را از کاربر بپرسید
'''

# list = []
# w1 = input("word 1: ")
# m1 = input("meaning word 1: ")
# list.append((w1, m1))
# w2 = input("word 2: ")
# m2 = input("meaning word 2: ")
# list.append((w2, m2))
# dict = dict(list)
# print(F"Dictionary: {dict}")
# k = input("word : ")
# print(dict[k])

#        master way

# dict = {}
# w = input("word: ")
# # m1 = input("meaning word 1: ")
# # m2 = input("meaning word 2: ")
# # m3 = input("meaning word 3: ")
# # m4 = input("meaning word 4: ")
# meanings = input("meaning: ").split(",") # split turn str into lists
# dict[w] = meanings
# print("Dictionary: ", dict)
# # ------2------
# '''
# حالا پس از انجام سوال قبلی، بخشی را به برنامه اضافه کنید تا
# یک کلمه را از کاربر گرفته و معانی آن را از دیکشنری خوانده و
# نمایش دهد
# '''
# word = input("Enter Your Word: ")
# # print("Meaning: ", dict[word]) # if meaning didn't exist it gave me an Error 
# print("Meaning: ", dict.get(word)) #  for solve pro use ( .get())

# ------3------
'''
دو لیست مختلف از شماره تلفن های افراد مختلف داریم.
ممکن است بعضی از شماره ها در لیست ها تکراری باشد (مثلا
 0939در هر دو لیست وجود داشته باشد). لیست جدیدی ایجاد
کنید که دو لیست قبلی را ترکیب میکند ولی تکراری ها در آن وجود
ندارند.(از نوع داده مجموعه کمک بگیرید)
'''
phones1 = ['0939', '0914', '0939']
phones2 = ['0939', '0923', '0933']
phones = set(phones1 + phones2)
print(phones)















