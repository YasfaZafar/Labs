#program 1:
start=1500
end=2700
txt=input("type any number: ")
print(txt)
result=[]
for num in range(start,end+1):
    if(num%7==0) and (num%5==0):
        result.append(num)
print("Numbers that are divisible by 7 and multiple of 5 between 1500 and 2700:")
print(result)


#program 2:
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Conversion Program")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

        

#Guess a number between 1 to 9
import random
def guess_num():
    num=random.randint(1,9)
    guess=None
    while guess!=num:
        guess=int(input("Type a number between 1 and 9: "))
        if guess==num:
            print("Well played!")
        else:
            print("Try again")
guess_num()


#Construct a pattern using nested for loop
def print_pattern():
    for i in range(1,6):
        print("*" * i)
    for i in range(4,0,-1):
        print("*" * i)
print_pattern()


#Reverse a word provided by the user
word= input("Enter a word: ")
def reverse_word():
    return word[::-1]
print(reverse_word())

#Count the number of even and odd numbers from a series of numbers
def even_odd_num(numbers):
    even_count=0
    odd_count=0
    for i in numbers:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1
    return even_count,odd_count
numbers=[1,2,3,4,5,6,7,8,9]
even_count, odd_count = even_odd_num(numbers)

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")


#Print each item and its corresponding type from a list
def print_list_types(datalist):
    for item in datalist:
        print(item, type(item))

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {'class': 'V', 'section': 'A'}]
print_list_types(datalist)


#Print numbers from 0 to 6 except 3 and 6
for i in range(0,7):
    if i==3or i==6:
        continue
    print (i)


#Print "FizzBuzz" for multiples of 3 and 5
def fizzbuzz():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()

#Get the Fibonacci series between 0 to 50
def fibonacci_series():
    a, b = 0, 1
    while a <= 50:
        print(a, end=' ')
        a, b = b, a + b

fibonacci_series()

#Generate a two-dimensional array based on given rows and columns
def generate_array(m, n):
    array = [[i * j for j in range(n)] for i in range(m)]
    return array

rows, cols = 3, 4
print("Generated array:", generate_array(rows, cols))

#Accept a sequence of lines and print them in lower case
def print_lines():
    lines = []
    while True:
        line = input("Enter a line (blank line to terminate): ")
        if line == "":
            break
        lines.append(line.lower())
    for line in lines:
        print(line)

print_lines()

# 13. Print binary numbers divisible by 5
def binary_divisible_by_5(binary_numbers):
    divisible_by_5 = [num for num in binary_numbers if int(num, 2) % 5 == 0]
    return ','.join(divisible_by_5)

binary_numbers = input("Enter binary numbers separated by commas: ").split(',')
print("Binary numbers divisible by 5:", binary_divisible_by_5(binary_numbers))

#Count the number of digits and letters in a string
def count_digits_letters(s):
    digits = sum(c.isdigit() for c in s)
    letters = sum(c.isalpha() for c in s)
    return letters, digits

s = "Python 3.2"
letters, digits = count_digits_letters(s)
print("Letters:", letters)
print("Digits:", digits)

#Check the validity of a password
import re

def check_password(password):
    if (6 <= len(password) <= 16 and
        re.search(r'[a-z]', password) and
        re.search(r'[A-Z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[$#@]', password)):
        return True
    return False

password = input("Enter a password: ")
if check_password(password):
    print("Password is valid")
else:
    print("Password is invalid")
