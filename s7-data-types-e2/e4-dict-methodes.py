print(dir(dict))
d = {"s": 3, "a": 9}
print('*' * 90)

# with .clear() i can clean
# in dictionary i have call by reference problem solution is  deepcopy() from copy
# print(d)
# # print(d.fromkeys("a"))  # .fromkeys() it's return a dict with key i specify have to be called with another dict & didn't any work with that dict
# print(d.fromkeys(("a", "s", "o", "m"), 3))  # .fromkeys() i can put keys in tuple & give alls same value

# print(d.get('a'))
# print(d.get('c', )) # .get() turn key value for me and turn None if key isn't exist
# print(d.get('c', 0)) # .get() here i specify if key didn't exist it turns what

# print(d.items())  # out -> dict_items([('s', 3), ('a', 9)])
# print(d.keys())   # out -> dict_keys(['s', 'a'])
# print(d.values()) # out -> dict_values([3, 9])

# .pop() in dict work if i specify the key   i can specify what out if key didn't exist in 2th arg
# .popitem() it choose what should cut himself ( it's ordinary that delete last one)

# print(d)
# print(d.setdefault("a", 0))   # .setdefault() if it's didn't exist from past it make new element for dict(key, value)
# print(d.setdefault("b", 2))
# print(d)

# .update()  concat dict together/ add key value element to dict
# print(d)
# print(d.update({"o": 23, "g": 32, "u": 38}))
# print(d)
# # -

# print(d)
# print(d.update([["o", 23], ["g", 32], ["u", 38]]))
# print(d)
# -

# print(d)
# print(d.update(F=32, R=43, T=54  ))
# print(d)
# ---

d = {"s": 3, "a": 9}
s = {"d": 38, "g": 90}

a = d | s   # concat two dict can happen in this way
print(a)