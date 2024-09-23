# danshjoo = ["soroush", "izadpanah", 20, 23.33, True, 3 + 9j, [1, 2, 3]]
# danshjoo = [1, 5, 9, 'reza']
# print(danshjoo, "\n", type(danshjoo))

# str = list("soroush")
# print(str, "\n", type(str))

# str = "soroush Izadpanah"
# print(str.split())   # separate by space by default or what we determine

# l = [3, 6, 9, 'Soroush']
# print(l[1])
# print(l[1:3])  # slicing support in lists
# print(l[::2])  # slicing(++) support in lists

# print(l * 2) 
# print(l + ['sdf', 'ref']) 
# l = l + ['sdf', 'ref']
# print(l)

# mutable      -> can change
# immutable -> can't change

# lists are mutable
# ---------------------

# l = [3, 6, 9, 'Soroush']
# z = [3, 6, 9, 'Soroush']

# print(l == z)

# l = [3, 6, 9, 'Soroush']
# z = [3, 9, 6, 'Soroush']
# a = 'Soroush Izadpanah'

# print(l == z)
# in
# print(3 in l)  # can check a member in the list
# print(4 in l)  
# print('Soroush' in l)  
# print('Sor' in l)  
# print('Sor' in a)  # agar kami shabahat peyda konad True mi dahad
# print('Iza' in a)
# ---------------------------------------------------------------- 2

# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# l2 = l1
# in this situation both l1 and l2 point to the same address in storage
# in change one of them, both of them change
# with id() we can see this, both storage address the same
# print(id(l1))
# print(id(l2))
# l2[0] = 9
# print(id(l1))
# print(id(l2))
# print(l1)
# ----------------------------

# for solving this problem i have to send copy of l1 to l2 (with slice or with .copy() method) Like below
# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# l2 = l1[:] # now they didn't efect on togther
# l2 = l1.copy() # now they didn't efect on togther
# print(id(l1))
# print(id(l2))
# ----------------------------

# x = [2, 6, 9, ['soroush', 'izadpanah']]
# print(x[3][0])
# print(x[3][0][0])
# print(x[3][0][-1])
# -------------------------------------

# l1 = [1, 2, ["a", "b", "c"]]
# l2 = l1.copy() 
# print(id(l1))
# print(id(l2))

# l2[2][0] = 3
# print(F"L1: {l1}\nL2: {l2}")  # when we change list in the list Shallow copy can't solve problem
# both lists change we need Deep copy to prevent these problems 
# print(id(l1))
# print(id(l2))

# Shallow copy ->  کپی سطحی: اشیاء داخلی ارجاء داده می شوند
# Shallow copy => .copy() or [:]

# Deep copy -> کپی عمیق: اشباء داخلی را هم کپی می کند
# because of this(after Shallow copy) when we change list in list both list are change
# for solving this problem i need to use deep copy
# ----------------------------------------------

#     Deep Copy -> deepcopy()
# for using deep copy we have to first import copy 
# import copy
# second we use deepcopy() method
# l1 = [1, 2, ["a", "b", "c"]]
# l2 = copy.deepcopy(l1)
# ----------------------------------------------------------------------- 3

# l = [1, 2, 3, 4]
# print(l)
# l.append(8)
# print(l)

# l = [1, 2, 3, 4]
# print(l)
# l.append([8, 10, 12, 14, 18]) # i can add anything to end of list
# print(l)

# l = [1, 2, 3, 4, 5, 6]
# print(l[2:5])
# l[2:5] = ["a", "b", "c"] # i chang every were i list with this way 
# l[2:5] = ["a", "b", "c", "d", "e", "f", "g", "h", "i"] # if i give it more or less value nothing change just do it 
# l[2:5] = ["a", "b"] # if i give it more or less value nothing change just do it 
# print(l)
# at the end i can use slicing for do what ever i want with lists 
# ----------------------------

# l = [1, 2, 3, 4, 5, 6]
# del l[4] # using (del) for delete from list
# del l[2:4] # using (del) for delete from list and with slice it can be handier 
# print(l)
# ----------------------------

# l = [1, 2, 3, 4, 5, 6]

# print(l[:len(l)])
# print(l[len(l)-1])
# ----------------------------

# a , b, c = [1, 2, 3] # don't forgot order is important in this assignment
# print(a , b, c)
# ----------------------------

# order is important in this assignment ( * )
# a , b, *c = [1, 2, 3, 4, 5, 6, 7] # using ( * ) before var for make variable list of extra values
# print(a , b, c)
# ----------------------------

# order is important in this assignment ( * )
# *a , b, c = [1, 2, 3, 4, 5, 6, 7] # using ( * ) before var for make variable list of extra values
# print("a: {}\nb: {}\nc: {}".format(a , b, c))
# ( * ) before ( a ) give extra values at start off list for ( a ) 
# ----------------------------

# order is important in this assignment ( * )
# a , *b, c = [1, 2, 3, 4, 5, 6, 7] # using ( * ) before var for make variable list of extra values
# print("a: {}\nb: {}\nc: {}".format(a , b, c))
# ( * ) before ( b ) give extra values at center off list for ( b ) 