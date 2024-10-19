'''
    یک رشته بگیرید و طول آن را در صورتی که بیشتر از  10باشد
چاپ کنید. ( از عملگر والروس در شرط استفاده کنید )
'''

# s = input("Enter a string: ")
# if (n := len(s)) > 10:
#     print(f"num: {n}, string: {s}")
# else:
#     print(f"string: {s}\n is too short")
# # -----------
#
# '''
#     در صورتی که یک لیست بیشتر از  5عنصر داشته باشد، جمع دو
# عنصر اول آن را چاپ کنید. ( از عملگر والروس در شرط استفاده
# کنید )
# '''
# l = [1, 2, 3, 4, 5, 6]
# l2 = [1, 2, 3, 4]
#
# if (n := len(ln := l)) > 5:
#     print(f"num: {n}, list: {ln}")
# else:
#     print(f"list: {ln}\n is too short!")
# -----------
#
# '''
#     برنامه ای بنویسید که جمع اعدادی که کاربر وارد میکند را
# محسابه کند. برنامه تا زمانی که کاربر یک رشته خالی نزده است
# ادامه پیدا کند. ( از عملگر والروس در شرط استفاده کنید )
# '''

# sum = 0
# while num := input("Enter a number: "):
#     sum += int(num)
#
# print(f"The sum is {sum}")
# -----------------

'''
    بررسی کنید که آیا یک عدد خاص (مثلا  )5در یک لیست وجود
دارد یا خیر. در صورت وجود ایندکس آن را چاپ کنید. ( از عملگر
والروس در شرط استفاده کنید )
'''

# l = [2, 8, 16, 26, 34, 9, 3]
# if (n := int(input("Enter a number: "))) in (li := l):
#     print(f"{n} is exist in {l}\n list")
# else:
#     print(f"{n} is not exist in {l}")
# -- another way

# l = [2, 8, 16, 26, 34, 9, 3]
# target = 3
# for i, num in enumerate(l):
#     if (found := num) == target:
#         print(f"{found} exist in {i}")
#     else:
#         print(f"{found} not exist in {i}")
# ---------------------

'''
    برنامه ای را بنویسید که اعداد تصادفی بین یک تا  100را تولید
می کند. اگر عدد تولید شده بزرگ تر از  80باشد برنامه متوقف
میشود. تعداد اعداد تولید شده باید چاپ شود. ( از عملگر والروس
در حلقه استفاده کنید )
'''
from random import randint

# l = []
# while (n := randint(1, 100)):
#     if n > 80:
#         print(f"number more then 80 generated: {n}")
#         break
#     print(f"number less than 80 generated: {n}")
#     l.append(n)
#
# # print(l)
# print(len(l))
# ----------------------

'''
    یک جمله از کاربر بگیرید و با استفاده از عملگر والروس، تعداد
کلمات آن را چاپ کنید
'''
if (length := len((input("Enter your sentence: ").split()))):
    print(length)
else:
    print("Enter validate number!")









