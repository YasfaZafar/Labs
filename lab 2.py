# While Loop

count = 0
while count < 3:
    count += 1
    print("Hello Geek")


# Single statement while block:

count = 0
while count == 2:
    print("Hello Geek")


# for in Loop:

l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)


print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)


# Continue Statement:

for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        continue
    print("Current Letter :", letter)

#Break Statement 

for letter in "geekforgeeks":
    if letter == "k":
        break
    print("Current Letter :",letter)

#Python Function

def my_func():
    print ("hello from function")
my_func()

#Function with Parameters

def my_func(fname):
    print(fname + "Zafar")
my_func("Yasfa")
my_func("Shahan")
my_func("Afra")

#Default Parameter Value

def my_func(country="Norway"):
    print("im from" +country)
my_func("sweden")
my_func("brazil")
my_func("")

#Passing a List as a Parameter

def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Return Values

def my_func(x):
    return 5*x
print(my_func(3))
print(my_func(4))
print(my_func(5))

#Keyword Argument 

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

# Create Class and Object

class Dog:
    def bark(self):
        print("Woof!")


my_dog = Dog()

my_dog.bark()

# The _init_() Function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# Object Methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


p1 = Person("John", 36)
p1.display()  # Output: Name: John, Age: 36

