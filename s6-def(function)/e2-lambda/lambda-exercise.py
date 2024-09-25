# '''
# برنامه ای بنویسید که با استفاده از لامبدا، اعداد زوج و فرد را در
# یک لیست از اعداد صحیح بشمارد
# '''
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# odd = len(list(filter(lambda x: x % 2 != 0, li)))
# positive = len(list(filter(lambda x: x % 2 == 0, li)))
# print(F"len list: {len(li)}, odd: {odd}, positive: {positive}")
# --------------------------------

# '''
# لیستی از تاپل ها به شکل [… ,′) ](Ali’, 93′) ,(Reza’, 65داریم.
# با استفاده از لامبدا برنامه ای بنویسید که این لیست را بر اساس
# اعداد موجود در تاپل مرتب کند
# '''
# li = [('ali', 12), ('reza', 10), ('soroush', 8), ('soheil', 33)]
# print(sorted(li, key=lambda x: x[1]))   # way1
# li.sort(key=lambda x: x[1])   # way2
# print(li)
# --------------------------------

# '''
# لیستی از دیکشنری ها به شکل [… , ’:{‘weight’: 50, ‘apple
# ’} ]‘redداریم. با استفاده از لامبدا برنامه ای بنویسید که این لیست
# را بر اساس رنگ موجود در دیکشنری مرتب کند
# '''
# li = [
#    {'weight': 50, 'apple': 'red'},
#    {'weight': 30, 'apple': 'yellow'},
#    {'weight': 580, 'apple': 'green'},
#    {'weight': 560, 'apple': 'gray'},
#    {'weight': 560, 'apple': 'purple'},
# ]

# print(sorted(li, key=lambda x: x['apple']))
# --------------------------------

# '''
# برنامه ای بنویسید تا لیستی از اعداد صحیح را با استفاده از
# لامبدا به زوج ها و فردها فیلتر کند.
# '''
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# odd = list(filter(lambda x: x % 2 != 0, li))
# positive = list(filter(lambda x: x % 2 == 0, li))
# print(F"len list: {li}, odd: {odd}, positive: {positive}")
# # --------------------------------

# '''
# ا استفاده از لامبدا یک برنامه ای بنویسید تا هر عدد را در
# لیستی از اعداد صحیح مربع و مکعب کند
# '''
# lst = [1, 5, 8, 10, 12, 32, 22, 23, 32, 38]
# print(lst)
# square = list(map(lambda x: x**2, lst))   # square power of 2
# print('square:',square)
# cube = list(map(lambda x: x**3, lst))   # cube power of 3
# print('cube:', cube)
# # --------------------------------

# '''
# با استفاده از لامبدا برنامه ای بنویسید تا بفهمید که آیا یک
# رشته داده شده با یک کاراکتر مشخص شروع می شود یا خیر
# '''

# char_test = lambda str, chr: print(F"{str} starts with {chr}") if str[0].lower() == chr.lower() else print(F"{str} didn't starts with {chr}")
# str = input("Enter string: ")
# chr = input("Enter char: ")
# char_test(str, chr)
# --------------------------------

'''
با استفاده از لامبدا برنامه ای بنویسید تا بررسی کند که آیا یک
رشته داده شده عددی است یا خیر. (توجه داشته باشید که
میخواهیم رشته های اعشاری همچون “ ”4.5هم تشخیص داده
شوند
'''

y = '3.5'
is_Number = lambda x: x.replace('.', '', 1).isdigit()
print(is_Number(y))

















