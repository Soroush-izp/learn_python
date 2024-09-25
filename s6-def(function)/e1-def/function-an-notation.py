# Note the function
# with this way i can choose type for parameters and if arguments have wrong type it give me an error message
# it give me error when ( mypy ) installed
# it names anNotation
# def max3(a:int, b:int, c:int):
#    return max(a,b,c) 

# print(max3(1, 2, '3'))

# with arrow after () of def i can choose type for output
def max3(a:int, b:int, c:int = 9) -> int:
   return max(a,b,c) 

# print(max3(1, 2, '3'))
print(max3.__annotations__)   # with this way i can see all type of def (.__annotations__)

















