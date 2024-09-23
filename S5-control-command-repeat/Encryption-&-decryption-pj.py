while 1: # 1 = True
   print("Choose Your Option:\n\t1)Encrypt\n\t2)Decrypt\n\t3)Exit")
   choice = input("Your Choice: ")
   if choice == '1':
      plain_text = input("text: ")
      encrypted_text = ""
      for c in plain_text:
         x = (ord(c) * 2) + 5   # with this formula on char characters encrypt data
         encrypted_text += chr(x)
      print('Encrypted Text:', encrypted_text)
      print('\n'+'-'*30)
      
   elif choice == '2':
      encrypted_text = input("Encrypted Text: ")
      plain_text = ""
      for c in encrypted_text:
         x = (ord(c) - 5) // 2   # with this formula on char characters decrypt data
         plain_text += chr(x)
      print('Plain Text:', plain_text)
      print('\n'+'-'*30)
      
   elif choice == '3':
      print("Goodbye!")
      break
   
   else:
      print("Your Choice is Wrong!")




































