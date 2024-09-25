"""
رفتار  enumerateرا با استفاده از ژنراتور پیاده سازی کنید
"""
# enumerate remembering

# l = ['s', 'r', 'f']

# for i, j in enumerate(l):
#    print(i, j)


# # --- # create with norm( just for & return) way
# def customEnumerate(x):
#    list = []
#    for i in range(len(x)):
#       list.append((i, x[i]))
#    return list
   
   
# print(customEnumerate([1, 2, 3, 4, 5, 6]))
# ---

# def customEnumerate(x, start=0):
#    c = start
#    for i in range(len(x)):
#       yield (c, x[i])
#       c += 1
   
   
# # print(list(customEnumerate([1, 2, 3, 4, 5, 6])))
# print(list(customEnumerate("soroush", 3)))
# # ------------------------------

# """
# یک ژنراتور برای تولید دنباله فیبوناچی بنویسید
# """

# def fibonacci():
#    f1 = 0
#    yield f1
#    f2 = 1
#    yield f2
#    while 1:
#       f3 = f1 + f2
#       yield f3
#       f1 = f2
#       f2 = f3
      
      
# fib = fibonacci()
# for _ in range(10):
#    print(next(fib))
   
   
# # --------------------------

# """
# ژنراتوری بنویسید که یک لیست گرفته و جمع عناصر آن را
# برگراند. ( هربار یک عنصر جدید جمع شود )
# مثال : لیست [ ]1,2,3,4,5را داریم. ژنراتور باید اولین بار  ،1دومین
# بار  ،2 1سومین بار  3 2 1و… را برگرداند
# """

# def sumList(l):
#    sumL = 0
#    for i in l:
#       sumL += i
#       yield sumL
      
      
# l = sumList([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(l))
# # ----------------------------

# """
# ژنراتوری بنویسید که یک رشته گرفته و معکوس آن را برگرداند.
# ( هر بار یک کاراکتر )
# """

# def reversStr(s):
#    for i in range(len(s), 0, -1):
#       yield s[i-1]
      
      
# revers = reversStr("Soroush")
# # print(list(revers))
# for ch in revers:
#    print(ch)
# # # ----------------------------

# """
# یک ژنراتور بی نهایت از اعداد زوج یا فرد بنوییسید. زوج یا فرد
# بودن توسط کاربر تعیین میشود
# """

# def even_odd(s):
#    c = 0
#    while 1:
#       if s == 'even' and c%2 == 0:
#          yield c
#       elif s == 'odd' and c%2 != 0:
#          yield c
#       c+=1
         
         
# ev_od = even_odd('even')   # choose ( even / odd)
# for i in range(15):
#    print(next(ev_od))
# ------------------------------

"""
ژنراتوری ایجاد کنید که در هر مرحله، خروجی های زیر را تولید
کند:
بار اول : 1
بار دوم: 2 2
بار سوم: 3 3 3
و…
"""

def numRepeat(s):
   while 1:
      yield f' {s}' * s
      s += 1
      
      
nRep = numRepeat(3)
for i in range(10):
   print(next(nRep))