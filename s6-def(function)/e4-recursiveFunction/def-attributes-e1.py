# # every thing in python is object
# def func(x=0):
#    """
#    test .__doc__ attribute
#    """
#    pass


# # print(dir(func))  # give me all attributes of func
# print(func.__doc__)  # give doc of def
# print(func.__name__) # give name of def
# # ----------------------------

# def avg(li):
#    return sum(li)/len(li)


# print(avg([1, 2, 3, 4, 5]))
# ----------------------------

def avg(li):
   return sum(li)/len(li)


def avg2(li):
   return sum(li)/len(li)


# here i gave my def(functions) attribute | i can do this with ( setattr(object, key, value))
# i can get attr with this getattr(object, key, default(optional)) | hasattr(object, key)  check it exist
# of course we i have  delattr() to
avg.school_name = "taleb amoly"
setattr(avg2, 'school_name', 'ayatolla amoly')  # set dict(attribute) with setattr()
print(avg([1, 2, 3, 4, 5]))
print(avg.school_name, avg2.school_name)
print(avg.__dict__, avg2.__dict__)  # show all __dict__ dictionary
