# for i in range(101):
#    if i % 3 == 0:
#       print(i)
# ---

# for i in range(3, 101, 3):
#    print(i)
# ---

# l = []
# for _ in range(5):
#    num = float(input("Enter a number: "))
#    l.append(num)
# print(sum(l)/len(l))
# ---

# مقسوم علیه
# def d(n):
#    l = []
#    for i in range(1, n+1):
#       if n % i == 0:
#          l.append(i)
#    return l
#
# print(sum(d(100)))
# ---

# تعداد مقسوم علیه n
# def d(n):
#    l = []
#    for i in range(1, n+1):
#       if n % i == 0:
#          l.append(i)
#    return l
#
# print(len(d(100)))
# ---

# کجموع اعداد تا 100
# def s(s, e, st=1):
#    l = []
#    for i in range(s, e+1, st):
#       l.append(i)
#    return l
#
# print(s(1, 100))
# ---

# # مجموع و تعداد مقسوم علیه های یک عدد
# def f(n):
#    l = []
#    for i in range(n+1):
#       l.append(i)
#    return l

# r = f(100)
# print(sum(r))
# print(len(r))
# # -------------

# '''
#    Create a Car class with two instance attributes:

# .color, which stores the name of the car’s color as a string
# .mileage, which stores the number of miles on the car as an integer
# '''

# class Car:
#    def __init__(self, color, mileage):
#       self.color = color
      # self.mileage = mileage
   
#    def __str__(self):
#       return f"The {self.color} car has {self.mileage} miles"


# print(Car("blue", 20000))
# print(Car("red", 30000))
# -------------

# '''
#    Create a GoldenRetriever class that inherits from the Dog class.
#    Give the sound argument of GoldenRetriever.speak() a default value of "Bark".
# '''
#
# # dog.py
#
# class Dog:
#    species = "Canis familiaris"
#
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age
#
#    def __str__(self):
#       return f"{self.name} is {self.age} years old"
#
#    def speak(self, sound):
#       return f"{self.name} says {sound}"
#
#
# class GoldenRetriever(Dog):
#    def speak(self, sound="Bark"):
#       return super().speak(sound)
#
#    # test my classes here
# GoldenRetriever = GoldenRetriever("Rex", 5)
# print(GoldenRetriever.speak())
# -------

import math

class React:
   def __init__(self, a, b):
      self.x = a
      self.y = b

   def Mohit(self):
      return (self.x + self.y) * 2
   def Masahat(self):
      return self.x * self.y
   def Zoom(self, z):
      self.x=self.x*z
      self.y=self.y*z


class Circle():
   def __init__(self, radius):
      self.radius = radius

   def circle_perimeter(self):
      return 2 * math.pi * self.radius

   def circle_area(self):
      return math.pi * self.radius ** 2

   def show(self):
      return f"(Circle: {str(self.radius)})"


class SuperInt():
   def __init__(self, n):
      self.n = n

   def Up(self):
      self.n += 1

   def Down(self):
      if self.n != 0:
         self.n -= 1

   def Right(self):
      self.n += 2

   def Left(self):
      if self.n >= 2:
         self.n -= -2

   def Show(self):
      return self.n


# a = React(10, 10)
# print(a.Mohit())
# print(a.Zoom(3))
# print(a.Mohit())

# r = Circle(5)
# print(r.circle_perimeter())1
# print(r.circle_area())
# print(r.show())

s = SuperInt(3)
s.Up()
s.Right()
print(s.Show())