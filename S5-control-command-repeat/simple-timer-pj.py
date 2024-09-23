import time # i using time module 
from os import system, name
while 1:
   choice = input("do you want to start: (Y/N)")
   if 'y' in choice.lower():
      hour, minute, second = input("Enter hour: minute: second -> ").split(':')
      hour = int(hour) # or straight * 3600
      minute = int(minute)
      second = int(second)
      total = hour * 60 * 60 + minute * 60 + second
      print("Timer Strats Now...")
      time.sleep(1)  # stop for 1 second
      while total>0:
         print(total)
         total -= 1
         time.sleep(1)  # stop for 1 second
         system( 'cls' if name == 'nt' else 'clear')  # clear screen for i in terminal( for timer number)
      print("Timer Ended...")
   elif 'n' in choice.lower():
      print("Exiting...")
      break
   else:
      print("Your Answer is Wrong!")