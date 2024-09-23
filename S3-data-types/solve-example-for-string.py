# Counting char in string(s)
# s = "ali is good boy"
# c = input("Enter a char: ")
# print(s.count(c))
# ------------------------

# finding the last word in the string
# s = input("Enter string: ")
# s = s.rstrip()
# i = s.rfind(' ')
# print(s[i + 1:])
# ------------------------

# s in b 
# s = input("Enter string: ")
# b = input("Enter string: ")
# print(s in b)
# ------------------------

# remove any whitespace from string
# s = input("Enter string: ")
# print(s.replace(' ', '').replace('\t', ''))
# ------------------------

# remove 0 from number
phone = input("Enter phone number: ")
print(int(phone.lstrip('0')))
