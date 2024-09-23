# s = {1, 5, 6, 9}  # sets can change ( .add() )
# print(s) 
# s.add(5)
# print(s) # sets are didn't except repeated values
# -------------------------------

# # add tuples togther
# t = (1, 5, 6, 9)
# print(id(t))
# f = t + ( 8,)
# print(id(f))   # these aren't same they are deferent values
# print(f)  # this is new value
# -------------------------------

# s = {1, 2, 3}
# print(s)
# print(id(s))
# s.add(5) # here i really add 5 to set value
# print(s)
# print(id(s))

# so at the end sets can change tuple can't change ( i have to make a nem value with + tuples together)
# sets didn't ordered so i can't access to sets elements with index
# s = {1, 2, 3}
# print(s[1]) # it gave Error
# -------------------------------

# empty { } didn't make set for empty set i have to use {""} or use ( set() )
# s = set("soroush")   # it's not ordered && don't except repeated values
# print(s)

# s = set([1, 1, 2, 2, 3, 5])   # sets can't be dictionary key
# print(s)
# in sets i can't set values that can change like Lists | of curse i can use tuples in set becaus they can;t change
# with ( .add() ) can add a value to set | with ( .update() ) i can add multiple values to sets

# s = set([1, 1, 2, ])
# s.update([5, 8, 10, 12], ["soroush", "sam", "surena"])
# print(s)
# -------------------------------

# for remove values from sets i use ( .remove() ) && ( .discard() ) 
# when value we want delete didn't exist remove gave Error discard do nothing
# s = {1, 3, "soroush", 3.456}
# # s. remove("soroush")
# # s. remove("sor")   # it gives error because this value didn't exist 

# # s. discard("soroush")
# s. discard("sor")   # it do nothing because this value didn't exist 
# print(s)
# -------------------------------

# notice that ( len() ) sets gives value when repeated values deleted 
# ( in ) work on sets
# s = {1, 1, 1, 1}
# print( len(s)) # length os  s  is 1( repeated values not count in sets(deleted) )

# s = {1, 1, 1, 1}
# print( 1 in s) 
# print( 3 in s) 
# -------------------------------

# thinking about ejtema , eshterak  in sets
# P = {3, 9, 15, 12, 6, 18}
# Q = {12, 6, 18, 10 ,4, 16, 2, 8, 14}

# print(P - Q)   # every thing P have And Q didn't have ( .difference() )
# print(P.difference(Q))   # every thing P have And Q didn't have ( .difference() )

# print(Q.difference(P))   # every thing Q have And P didn't have
# print(Q - P)   # every thing Q have And P didn't have ( .difference() )

# print(Q | P)   # ( ejtema ) All element (in both P and Q)
# print(Q.union(P))   # ( ejtema ) All element (in both P and Q)

# print(Q & P)   # ( eshterak ) every thing exist in both P and Q (both P and Q have)
# print(Q.intersection(P))   # ( eshterak ) every thing exist in both P and Q (both P and Q have)

# print(Q ^ P)   # ( تفاضل متقارن ) َAll thing exist in both of P and Q except Element both of them have
# print(Q.symmetric_difference(P))   # ( تفاضل متقارن ) َAll thing exist in both of P and Q except Element both of them have

# print(P < Q)   # ( زیر مجموعه ) all in p is in the q
# print(Q.symmetric_difference(P))   # ( زیر مجموعه ) all in p is in the q
# -------------------------------

   # A = {40, 50, 20, 10, 30, 60}
   # B = {10, 30, 60}

   # print(B < A)   # ( زیر مجموعه ) all in B is in the A ( B in the A)
   # print(B.issubset(A))   #  ( زیر مجموعه ) all in B is in the A ( B in the A)

   # print(B > A)   # ( زیر مجموعه ) all in A is in the B ( A in the B)
   # print(A.issuperset(B))   #  ( B )والد ( A ) 
















