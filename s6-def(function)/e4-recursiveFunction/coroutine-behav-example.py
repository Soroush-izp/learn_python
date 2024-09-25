# def blocker_gen(words): # block bad content
#    print("Ready!")
#    w = None
#    while 1:
#       word = yield w
#       if word not in words:
#          w = word 
#       else:
#          w = "*" * len(w)
      
      
# g = blocker_gen(["fuck", "cow", "horse", "khamenei"])
# next(g)
# print(g.send("Soroush"))
# print(g.send("cow"))
# # --------------------------

def spliter_gen(delimiter=" "): # block bad content
   print("Start!")
   s = None
   while 1:
      line = yield s
      s = line.split(delimiter)
      

g = spliter_gen("-")
next(g)
print(g.send("soroush-soheil-koroosh-kiarash-darush"))
