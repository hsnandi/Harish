#Hello world
print ("Hello World")

#How to import
import math
print (math.floor(3.65))
print (math.sin(90))
print (math.tan(0))
print (math.sin(0))

#variables
a = 1
b = 2
print (a+b)

#How to get type
Name = "Harish"
Number = 55
print (type(Name))
print (type(Number))

#Variables
list = ["Harish",2,3.5]
print (list)

list1 = ["Harry",2,3]
list1[0] = "Manish"
print (list1)

list2 = [5,6,7]
list2[1] = 8
print(list2)

#in 'LIST' elements can be changed, wheares in 'TUPLE' elements cannot be changed

tuple = (1,2,3)
print(tuple)

'''
List are in square bracket eg:[]
Tuples are in in round bracket eg:()
Dictionary are in {}
'''

list5 = [1,2,3,3,4]
s1 = set(list5)
print (s1)
#to remove the repeted element of LIST, "set" is used.

# if else statements
a=33
b=35
if b > a:
   print("b is greater than a")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

age = 19
if age >= 18:
   print ("you are an adult")
elif age > 3 and age < 18:
   print ("you are in school")
else:
   print ("you are child")
   
   
a = 2
b = 330
print("A") if a > b else print("B")

#functions
def average(num1, num2):
    avr = (num1 + num2) / 2
    return avr

print(average(3,6))

#while loop
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)  #number 3 would be missing now.

#for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

