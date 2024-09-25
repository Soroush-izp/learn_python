# """
# یک تابع بازگشتی برای محاسبه مجموع عناصر در یک لیست
# بنویسید
# """

# def sum_list(l):
#    if l:
#       return l[-1] + sum_list(l[:-1])
#    return 0
# print(sum_list([1, 1, 1, 1]))
# # ---

# """
# یک تابع بازگشتی برای محاسبه توان یک عدد بنویسید
# """

# def pow(n, p):
#    if p:
#       return n * pow(n, p-1)
#    return 1


# print(pow(2, 3))
# # # ---

# """
# یک تابع بازگشتی برای معکوس کردن یک رشته بنویسید
# """

# def reverser(s):
#    if s:
#       return s[-1] + reverser(s[:-1])
#    return ''


# print(reverser('soroush'))
# # # ---

# """
# یک تابع بازگشتی برای شمارش تعداد تکرار یک عنصر در یک
# لیست بنویسید
# """
# def list_repeat(e, l):
#    if l:
#       if l[-1] == e:
#          return 1 + list_repeat(e, l[:-1])
#       else:
#          return list_repeat(e, l[:-1])
#    return 0


# print(list_repeat('s', 'soroush'))  # str are array of chr so it's work
# # # ---

# """
# یک تابع بازگشتی برای بررسی اینکه آیا یک رشته palindrome
# است یا خیر بنویسید ( از هر دو طرف به یک شکل خوانده میشود 
# """
# def is_palindrome(s):
#    if len(s) > 1 and s[0] == s[-1]:
#       return is_palindrome(s[1:-1]) if s[1:-1] else True
#    return False



# print(is_palindrome("s"))  
# # ---

"""
یک تابع بازگشتی برای محاسبه مجموع ارقام در یک عدد صحیح
مثبت بنویسید
"""
def sum_numeric(n):
   if abs(n) and n:
      return n%10 + sum_numeric(n//10)
   return 0


print(sum_numeric(1310))  