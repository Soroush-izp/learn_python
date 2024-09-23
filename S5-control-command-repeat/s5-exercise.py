'''
   برنامه اي بنويسيد كه دو عدد را از كاربر گرفته و اعداد مابين آن
ها را نمايش دهد
'''

# n, n2 = (input("enter two values to out number between them spared by (,):").split(','))
# n = int(n)
# n2 = int(n2)
# for i in range(n+1, n2):
#    print(i)
# --- master way

# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))
# min_ = min(x, y)
# max_ = max(x, y)
# while min_ <= max_:
#    print(min_)
#    min_ += 1
# ----------------------------------

'''
   برنامه اي بنويسيد كه دو عدد صحيح را گرفته و مقسوم عليه
هاي مشتركشان را نمايش دهد
'''

# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))
# xl = []
# yl = []
# for i in range(1, x+1):
#    if x % i == 0:
#       xl.append(i)
# for i in range(1, x+1):
#    if x % i == 0:
#       yl.append(i)
# # compar two list with change them to set()
# set_x = set(xl)
# set_y = set(yl)
# if set_x & set_y:
#    print(set_x & set_y)
# else:
#    print("they haven't any match!")
# --- master way

# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))
# min = min(x, y)
# for i in range(1, min+1):
#    if x % i == 0 and y % i == 0:
#       print(i, end=" ")
# ----------------------------------

'''
   برنامه اي بنويسيد كه دو عدد صحيح را گرفته و بزرگترين
مقسوم عليه مشتركشان را نمايش دهد
'''

# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))
# min = min(x, y)
# l = []
# for i in range(1, min+1):
#    if x % i == 0 and y % i == 0:
#       l.append(i)
# print(max(l))
# --- master way

# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))
# min = min(x, y)
# l = []
# for i in range(min, 1, -1):   # start from up( reverse) help us to have better performance 
#    if x % i == 0 and y % i == 0:
#       print(i)
#       break
# ----------------------------------

'''
   برنامه اي بنويسيد كه دو عدد صحيح را گرفته و كوچكترين 
مضرب مشتركشان را نمايش دهد
'''
# 8 -> 8 16 24 32 ...
# 6 -> 6 12 18 24 ...
# mazrab -> har bar adad + khodash mi shavad

# --- master way

# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))
# max_ = max(x, y)
# min_ = min(x, y)
# i = 0
# for i in range(1, min_+1):
#    if (max_ * i) % min_ == 0:
#       print(max_ * i)
#       break
# --- master way ( 2 )

# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))
# max_ = max(x, y)
# min_ = min(x, y)
# i = max_
# while i % min_ != 0:
#    i += max_
# print(i)
# ----------------------------------

'''
   برنامه اي بنويسيد كه عدد صحيحي را گرفته و تعداد رقمهايش را
نمايش دهد. (عدد را به رشته تبدیل نکنید
'''
# num = int(input("Enter num: "))
# t = 0
# while num > 0:
#    num //= 10  # vaghti taghsim sahih bar 10 mi konim yek ragham kam mi shavad
#    t += 1
# print(t)
# ----------------------------------

# برنامه ای که تعداد سطر را از کاربر گرفته و شکل زیر را رسم
# کند:
#     *
#    **
#   ***
#  ****
# *****

# n = int(input("Enter num: "))
# for i in range(1, n):
#    print((n - i) * ' ', i * '*', sep='')
# ------------------------------------------

'''
   ما یک لیست ده تایی از اسم های مختلف داریم. برنامه ای
بنویسید که کاربر یک اسم را در ذهن خود بگیرد و برنامه حدس
بزند آن اسم چیست. سپس از کاربر بپرسد که درست حدس زد
است یا خیر. اگر اشتباه بود اسم دیگری حدس بزند. برنامه نباید
اسمی را که قبلا کاربر گفته است اشتباه است، دوباره نشان دهد
'''
# from secrets import randbelow
# names = ['soroush', 'reza', 'roham', 'sam', 'soraya', 'soheil', 'fariba', 'samira', 'sahand', 'surena']

# while 1:
#    Forecast = names[randbelow(len(names))]
#    rse = input(F"You think about({Forecast}) Y/N:")
#    if rse.lower() != 'y':
#       print("Let me try again...")
#       names.remove(Forecast)
#       if names:
#          print("i guess every thing in list!")
#          break
#       # print(names)
#    else:
#       print("you Win")
#       break
# --- Master Way

# from random import choice
# names = ['soroush', 'reza', 'roham', 'sam', 'soraya', 'soheil', 'fariba', 'samira', 'sahand', 'surena']
# names_cp = names.copy()
# while 1:
#    # user_choice = input("your guess:")
#    if len(names_cp) == 0: 
#       print("i guess every thing in list!") 
#       break
#    cmp_choice = choice(names_cp)
#    ans = input(F"Is Your Guess {cmp_choice}?(Y/N):")
#    if "y" in ans.lower():
#       print("you Win")
#       break
#    names_cp.remove(cmp_choice)
















