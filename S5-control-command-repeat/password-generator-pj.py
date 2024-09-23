import random
import string  # access to string without trouble
# print(string.ascii_lowercase) # ascii_lowercase for accessing lower case letters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
# letters = string.ascii_letters   # ascii_letters for accessing all letters upper or lower case
symbols = "<>?/!@#$%^&*\|~_+-"
numbers = "0123456789"
all = lower + upper + symbols + numbers

while 1:
   print("Choose Your Option:\n\t1)Create a Password\n\t2)Exit")
   choice = input("Your Choice: ")
   if choice == '1':
      length = int(input("Enter Password Length: "))
      password = ''.join(random.sample(all, length))  # random sample gave i list because of that i use join to change that to str
      print(password)
      print("-"*30)
   elif choice == '2':
      print("GoodBye!")
      break
   else:
      print("Your Choice is Wrong!")










