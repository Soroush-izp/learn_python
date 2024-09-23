# x, y, z = 5, 8, 9 
# x, y, z = input("x, y, z: ").split(',') #with this method i can get multiple input with one input()
# # split(',') -> this method spread str i can choose spreader
# print("x: ", x)
# print("y: ", y)
# print("z: ", z)
# type of output is str
# -------------------------------

# number of inputs shouldn't be less or more 
# for solve this problem define it the list
# x = input("x: ").split(',') #with this method i can get multiple input with one input()
# print("x: ", x)
# -------------------------------

# type of output is str
x = [int(x) for x in input("x: ").split(',')] # make all type int
print("x: ", x)










