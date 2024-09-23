#     break

# word = 0
# while word <= 10:
#    print(F"{word}")
#    word += 1
# print("-" * 30)
# -----------------------

# i = 1
# while i < 100:
#    print(i)
#    if i == 8:
#       break
#    i += 1
# -----------------------

# n = float(input("n: "))
# m = n
# while 1:
#    s = input("Do You Continue? (y/n): ")
#    if s.lower() == 'n':
#       break
#    n = float(input("n: "))
#    if n < m:
#       m = n
# print(n, "is smallest number!")
# -----------------------

# m = float('inf')
# while 1:
#    n = float(input("n: "))
#    if n < m:
#       m = n
#    s = input("Do You Continue? (y/n): ")
#    if s.lower() == 'n':
#       break
# print(n, "is smallest number!")
# -----------------------

#     continue
# i = 0
# while i < 10:
#    i += 1
#    if i % 3 == 0:
#       continue
#    print(i)
# -----------------------

#     else  fro ( while )
# i = 0
# while i < 10:
#    i += 1
#    if i % 3 == 0:
#       continue
#    print(i)
# else: # if while loop have normal end while else run
#    print("everything alright!")
# -----------------------

# calculate ( aval numbers) prime num : be gheyr az khodesh , 1 maghsome digari nadarand
n = int(input("n: "))
i = 2
if n > 1:
   # pass # pass for didn't write anything
   while i < (n//2) + 1:  # it can be true with ( n//2) + 1
      if n % i == 0:
         print(n, "is not a prime number!")
         break
      i += 1
   else: # attention that else just run when while loop didn't get an error ( while has normal cycle)
      print(n, "is a prime number!")
else:
   print(n, "is not a prime number!")




























