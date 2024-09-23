# l = [1, 2, 3, 4, 5, 6]
# s = "soroush izadpanah"
# t = ("a", "b", "c")
# d = {"a": 1, "b": 2, "c": 3}

# for i in l: # it loop over ( l ) list
#    print(i)

# for i in s: # it loop over ( s ) str
#    print(i)

# for i in t: # it loop over ( t ) tuple
#    print(i)

# for i in d: # it loop over ( d ) dictionary keys
#    print(i)
# so for loop over iterable ( sequences )
# ------------------------

# list = [67, 92, 102, 110, 87, 72, 96]

# for c in list:
#    print('-'*9) 
#    print(chr(c))  # chr( ) gave i meaning of ascii code 

# else, break, continue => all feature in ( while ) present in for 
# ------------------------

# with for, out element in both lists
# list1 =[1, 4, 8, 9, 5, 54, 12, 32]
# list2 =[43, 24, 18, 722, 5, 54, 12, 32]

# way1
# for l1 in list1:
#    for l2 in list2:
#       if l1 == l2:
#          print(l1)

# way2
# for l1 in list1:
#    if l1 in list2:
#       print(l1)
# ------------------------

# a, b, c = [1, 2, 3]
# a, *b, c = [1, 2, 4, 6, 9, 3] # if i use * before one of var its can give more extra values
# print(a, b, c)

# i can have up situation in for
# for a in [[2,3,4], [6,7,8], [9,10,12]]:
#    print(a)
# ---------

# a, b, c = [1, 2, 3] # down a b c var in for loop work like this
# for a, b, c in [[2,3,4], [6,7,8], [9,10,12]]:
#    print('a: ', a, 'b: ', b, 'c:', c)

   # just like up var assigning
# for a, b, *c in [[2, 3, 4, 0, 0], [6, 7, 8, 0, 0], [9, 10, 12, 0, 0]]:
#    print('a: ', a, 'b: ', b, 'c:', c)
# --------------------------------------------

d = {"a": 1, "b": 2, "c": 3}
# for i in d: # it loop over ( d ) dictionary keys
#    print(F'{i}: {d[i]}')

# for i in d.keys(): # it loop over ( d ) dictionary keys
#    print(F'{i}: {d[i]}')

# for i in d.values(): # it loop over ( d ) dictionary values
#    print(i)

# for i in d.items(): # it loop over ( d ) dictionary and turn back items( tuple of key values)
#    print(i)

for key, value in d.items(): # it loop over ( d ) dictionary and turn back 
   print(key, ':', value)  #items with var key & value separately


























