import math
import time
from typing import Union
import random
import os
import shutil
#------------ data types and variables

# user_name = "John"
# user_age = 25
# user_is_admin = True

# print(f"Hello {user_name}, your age is {user_age}. Your admin status is {user_is_admin}.")

# city = "Baku is capital of Azerbaijan"
# age = "25"
# space = "    hi"
# splitted_city = city.split(" ")

#------------ string methods

# print(city.capitalize())
# print(city.casefold())
# print(city.center(60, "*"))
# print(city.count("i"))
# print(city.replace("i", "O"))
# print(city.encode())
# print(city.endswith("n"))
# print(city[0:4].endswith("u"))
# print(city.find("o"))
# print(city.index("u"))
# print(space.strip())
# print(" ".join(splitted_city))

#------------ type casting

# x = 1
# y = 2.0
# z = "3"

# x = float(x)
# y = int(y)
# z = int(z)

# print(x)
# print(y)
# print(z)


#------------ input method

# user_name = str(input("Enter your name: "))
# age = int(input("Enter your age: "))

# print(f"Hello {user_name}, your age is {age}.")

#------------ math functions

# pi = 3.14
# root = 9
# numbers = [1,2,3,4,5]

# print(round(pi))
# print(math.ceil(pi))
# print(math.sqrt(root))
# print(math.floor(pi))
# print(abs(-pi))
# print(math.pow(pi,3))
# print(max(numbers))
# print(sum(numbers))
# print(min(numbers))

#------------ string slicing

# string = "Hello World"

# only_hello = string[:5]
# only_world = string[6:]
# reversed_str = string[::-1]
# only_hello_slice = slice(0,5)
# print(only_hello)
# print(only_world)
# print(reversed_str)
# print(string[only_hello_slice])


#------------ if else elif statements


# user_name = "mury.ash"
# password = "1234"
# age = int(input("Enter your age: "))
# user_name_input = str(input("Enter your username: "))
# password_input = str(input("Enter your password: "))

# if age == 100:
#     print("You are a centruy old!")
# elif age >= 18:
#     print("You are an adult!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a minor!")

# if user_name_input == user_name and password_input == password:
#     print("Welcome!")
# else:
#     print("Wrong username or password!")

# if age == 30 or age == 40:
#     print("You are either 30 or 40 years old!")

# if age != 30 and age != 40:
#     print("You are not either 30 or 40 years old!")
# else:

#     print("You are either 30 or 40 years old!")

#------------ while loops

# while 1==1:
#     print("Hello")

# count = 0

# while True:
#     count += 1
#     if count == 10:
#         print(count)
#         break
#     elif count == 5 or count == 7:
#         continue
#     else:
#         print(count)
#         pass

# name = str(input("Enter your name: "))

# while len(name.strip()) == 0:
#     name = str(input("Enter your name: "))

# print(name)

# no_integer = str(input("Enter non integer character: "))

# while no_integer.isnumeric():
#     no_integer = str(input("Enter non integer character: "))

# print(no_integer)

#------------ for loops

# user_name = "mury.ash"

# for i in range(10):
#     print(i)

# for i in range(1,101):
#     print(i)

# for i in user_name:
#     print(i)

# for i in range(len(user_name)):
#     print(user_name[i])

# for i in range(2,11,2):
#     print(i)

# string = ""

# for i in range(1,11):
#     print(i)
#     time.sleep(1)

# print("Done!")

#------------ nested loops

# rows = int(input("Enter number of rows: "))
# columns = int(input("Enter number of columns: "))
# symbol = input("Enter symbol: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()


#------------ break, continue, pass

# for i in range(1, 11):
#     if i == 5 or i == 7:
#         continue
#     print(i)

# for i in range(1, 11):
#     if i == 5 or i == 7:
#         pass
#     else :
#         print(i)

# for i in range(1, 11):
#     if i == 5 or i == 7:
#         break
#     print(i)


#------------ lists

# names = ["Murad", "Gunay", "Nadir", "Huseyn", "Simran"]

# name1, name2, *rest = names

# print(rest)

# numbers = [i for i in range(100)]

# names[0] = "Amin"
# names[:2] = ["Ali", "Veli"]
# names.append("Amin")
# names.insert(0, "Amin")
# names.remove("Murad")
# names.pop(1)
# del names[0:2]
# names.clear()
# for name in names:
#     print(name)

#------------ 2D lists

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]

# foods = [drinks, dinner, dessert]

# for food in foods:
#     food_arr = []
#     for food_item in food:
#         food_arr.append(food_item)
#     print(food_arr)

# for i, food in enumerate(foods):
#     print(f"index: {i}, value: {food}")

#------------ tuples

# car = ("bmw", 2019, "red", 2000)

# print(car)
# print(car[::-1])
# print(car[0:3])
# car[0] = "audi"

# (brand, year, color, price) = car

# print(brand, year, color, price)

#------------ sets

# sports = {"Football","MMA","Swimming","Golf","Chess","Boxing","Chess"}

# extra_sports = {"Basketball","Rugby","Cricket"}

# sports.add("Bowling")
# sports.update(extra_sports)
# sports.union(extra_sports)
# joined_sets = sports | extra_sports

# print(sports)
# print(joined_sets)
# print(sports.intersection(extra_sports))
# for x in sports:
#     print(x, end=" ")


#------------ dictionaries

# user_details = {
#     "username": "mury.ash",
#     "age": 25,
#     "country": "Azerbaijan",
#     "hobbies": ["coding","reading","movie watching"]
# }

# extra_user_details = {
#     "school": "244 number middle school",
#     "has_brothers": False,
#     "has_sisters": False,
#     "has_girlfriend": True
# }

# user_details.update(extra_user_details)
# user_details.pop("age")
# user_details.clear()
# user_details.popitem()

# print(user_details)
# print(user_details["age"])
# print(user_details["SSS"])
# print(user_details.get("age"))
# print(user_details.get("s"))
# print(user_details.keys())
# print(user_details.values())
# for key, value in user_details.items():
#     print(f"key: {key}, value: {value}")

#------------ indexing

# name = "murad yusubov"

# if(name.index("m") == 0):
#     print(True)
# else:
#     print(False)

# first_name = name[:5]
# last_name = name[6:]

# print(f"Hi {first_name.capitalize()} {last_name.capitalize()}")

#------------ functions

# def add(a: int, b: int) -> int:
#     return a + b

# def subtract(a: int, b: int) -> int:
#     return a - b

# def multiply(a: int, b: int) -> int:
#     return a * b

# def divide(a: int, b: int) -> int:
#     return a / b


# print(add(10, 20))
# print(subtract(10, 20))
# print(multiply(10, 20))
# print(divide(10, 20))

#------------ kwargs

# def sum_numbers(**kwargs):
#     total = 0
#     for number in kwargs.values():
#         total += number
#     return total

# print(sum_numbers(n1=1, n2=2, n3=3))


#------------ variable scopes

# name = "S" # global variable

# def display_name(name: str) -> str:
#     given_name = name # local variable
#     print(f"Hello, {given_name}")


# print(name)
# display_name("murad")

#------------ args

# def sum_numbers(*args):
#     print(sum(args))
    

# sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#------------ string format

# def hello_animal(animal: str, item: str) -> str:
#     str = f"Hello {animal}! You have {item}"
#     print(str)
    

# hello_animal("cat", "cat food")

#------------ random numbers

# random_number = random.randint(1,100)
# random_float = random.random()
# colors = ["green", "blue", "red"]
# random_color = random.choice(colors)
# random.shuffle(colors)
# colors_2 = random.sample(colors, 2)


#------------ exception handling

# try:
#     numerator = int(input("Enter a value to divide:"))
#     divider = int(input("Enter a value to divide by:"))
#     result = numerator / divider
#     print(result)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("You didn't enter a number!")
# except Exception:
#     print("Something went wrong...")

#------------ file detection

# path = "C:\\Users\\yusif\\OneDrive\\Masaüstü\\pycharm"

# if os.path.exists(path) and os.path.isfile(path):
#     print("That is a file and it exists")
# else:
#     print("That is not a file or it doesn't exist")

# if os.path.exists(path) and os.path.isdir(path):
#     print("That is a directory and it exists")
# else:
#     print("That is not a directory or it doesn't exist")
    
#------------ file reading

# with open("a.txt","r") as text_file:
#     file = text_file.read()
#     print(file)

#------------ file writing

# with open("a.txt","w") as text_file:
#     text_file.write("New text")

# with open("a.txt","a") as text_file:
#     text_file.write("\nESMA + MURAD = FOREVER")
    

#------------ copy a file

# shutil.copyfile("a.txt", "new.txt")
# shutil.copy("a.txt", "new.txt")

#------------ move a file

# source = "C:\\Users\\yusif\\OneDrive\\Masaüstü\\Health_Small.png"
# destination = "C:\\Users\\yusif\\OneDrive\\Masaüstü\\pycharm\\Health-Bar\\assets\\Health-Small.png"

# try:
#     if(os.path.exists(destination)):
#         print("There is already a file there")
#     else:
#         shutil.move(source, destination)
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("You don't have permission to move that")
# except Exception:
#     print("Something went wrong...")


#------------ delete a file 

# try:
#     os.remove("a.txt")
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("You don't have permission to delete that")
# except Exception:
#     print("Something went wrong...")
# else:
#     print("File was deleted successfully!")



#------------ classes

# class Car:
#     def __init__(self, name, color, year):
#         self.name = name
#         self.color = color
#         self.year = year
    
#     def drive(self):
#         print(f"{self.name} is driving")
        
#     def stop(self):
#         print(f"{self.name} is stopping")

# car = Car("bmw", "red", 2019)

# print(car.name)
# print(car.color)
# print(car.year)
# car.drive()
# car.stop()

# class Shop:
#     def __init__(self, name, items):
#         self.name = name
#         self.items = items

#     def get_items_count(self):
#         return len(self.items)
    
#     def get_items(self):
#         return self.items
    
#     def add_item(self, item):
#         self.items.append(item)
        
#     def remove_item(self, item):
#         self.items.remove(item)
        

# shop = Shop("My Shop", ["apple", "banana", "orange"])


# shop.add_item("bread")

# print(shop.get_items())


#------------ class inheritance

# class Human:
#     alive = True
    
#     def walk(self):
#         print("walking")
        
#     def sleep(self):
#         print("sleeping")
        

# class Murad(Human):
#     pass


# class Esma(Human):
#     pass

    

# murad = Murad()
# esma = Esma()

# print(murad.alive)
# print(esma.alive)


#------------ multilevel inheritance

# class Organism:
#     alive = True
    

# class Animal(Organism):
#     def eat(self):
#         print("eating")
        
# class Dog(Animal):
#     def bark(self):
#         print("barking")


# animal = Animal()
# dog = Dog()

# print(animal.alive)
# print(dog.alive)


#------------ multiple inheritance

# class Prey:
#     def flee(self):
#         print("fleeing")
        

# class Predator:
#     def hunt(self):
#         print("hunting")
        

# class Fish(Prey, Predator):
#     pass

# fish = Fish()

# fish.flee()
# fish.hunt()


#------------ method overriding

# class Person:
#     def __init__(self, name) -> None:
#         self.name = name
        
#     def talk(self):
#         print(f"Hi, I am {self.name}")
        

# class Student(Person):
#     def __init__(self, name, student_id) -> None:
#         super().__init__(name)
#         self.student_id = student_id
        
#     def talk(self):
#         print(f"Hi, I am {self.name} and my student id is {self.student_id}")
        


# murad = Student("Murad", 123)
# person = Person("Yusif")

# murad.talk()
# person.talk()


#------------ method chaining

# class Calculator:
#     def __init__(self, n1, n2) -> None:
#         self.n1 = n1
#         self.n2 = n2
        
#     def add(self):
#         print(self.n1 + self.n2)
#         return self
    
#     def subtract(self):
#         print(self.n1 - self.n2)
#         return self
    
#     def multiply(self):
#         print(self.n1 * self.n2)
#         return self
    
#     def divide(self):
#         print(self.n1 / self.n2)
#         return self
        

# calculator = Calculator(10, 5)
    
# calculator.add().subtract().multiply().divide()


#------------ super function

# class Animal:
#     def __init__(self, food) -> None:
#         self.food = food
        
#     def eat(self):
#         print(f"This animal eats {self.food}")
        


# class Rabbit(Animal):
#     def __init__(self, food) -> None:
#         super().__init__(food)
        
        
# rabbit = Rabbit("Carrot")
# rabbit.eat()

# class Person:
#     def __init__(self, name, age, gender) -> None:
#         self.name = name
#         self.age = age
#         self.gender = gender
    
#     def introduce(self):
#         print(f"Hi, my name is {self.name}")
#         print(f"I am {self.age} years old")
#         print(f"I am a {self.gender}")
        

# class Murad(Person):
#     def __init__(self, name, age, gender) -> None:
#         super().__init__(name, age, gender)
        


# murad = Murad("Murad", 20, "male")
# murad.introduce()
        


#------------ abstract classes

# from abc import ABC, abstractmethod

# class Person(ABC):
#     @abstractmethod
#     def introduce(self):
#         pass
#     @abstractmethod
#     def eat(self):
#         pass
#     @abstractmethod
#     def sleep(self):
#         pass
#     @abstractmethod
#     def drink(self):
#         pass
    

# class Murad(Person):
#     def __init__(self, name) -> None:
#         self.name = name
        
#     def introduce(self):
#         print(f"Hi, my name is {self.name}")
        
#     def eat(self):
#         print("eating")
        
#     def sleep(self):
#         print("sleeping")
        
#     def drink(self):
#         print("drinking")
        

# murad = Murad("Murad")
# murad.introduce()
# murad.eat()
# murad.sleep()
# murad.drink()


#------------ objects as arguments

# class Person:
#     name = None
    

# def change_name(person, name):
#     person.name = name
    

# murad = Person()
# change_name(murad, "Murad")
# print(murad.name)


#------------ duck typing


# class Person:
#     def __init__(self, gender):
#         self.gender = gender
        
#     def walk(self):
#         print("walking")
        

# class Student:
#     def study(self, obj):
#         print(f"{obj.gender} is studying")
        

# person = Person("Male")
# student = Student()

# student.study(person) 



#------------ walrus operator

# print(happy := True)

# foods = []

# while food := input("Enter food: ") != "quit":
#     foods.append(food)

# print(foods)

# numbers = [1,2,3,4,5,6,7,8,9,10]

# while True:
#     if (num := int(input("Enter number: "))) in numbers:
#         print(num)
#         break
#     else:
#         print("Enter a valid number")
#         continue
        


# sample_data = [
#     {"userId": 1,  "name": "rahul", "completed": False},
#     {"userId": 1, "name": "rohit", "completed": False},
#     {"userId": 1,  "name": "ram", "completed": False},
#     {"userId": 1,  "name": "ravan", "completed": True}
# ]
 
# for entry in sample_data:
#     if name := entry.get("name"):
#         print(name)


    

#------------ functions as variables

# def introduce(name):
#     print(f"Hi, my name is {name}")
    

# name = introduce

# name("murad")


#------------ higher order functions

# def loud(text: str) -> str:
#     return text.upper()

# def quiet(text: str) -> str:
#     return text.lower()

# def talk (func, text):
#     print(func(text))
    
# talk(loud, "murad")
# talk(quiet, "yusubov")

# def add (n1,n2):
#     return n1+n2

# def calculate(n1, n2):
#     print(add(n1, n2))
    
# calculate(1,2)


#------------ lambda functions

# introduce = lambda name, age: f"Hi, my nae is {name}. Im {age} years old"


#------------ sort

# numbers = [8,4,6,2,1,7,5,3]

# users = [{"name": "Murad", "age": 17}, {"name": "Akif", "age": 16}, {"name": "Namid", "age": 34}]

# users.sort(key=lambda user: user['age'])

# users.sort(key=lambda user: user['name'])

# numbers.sort()

# numbers.sort(reverse=True)


#------------ map

# numbers = [1,2,3,4,5,6,7,8]

# doubled = list(map(lambda n: n*2, numbers))

# cars = [("bmw", 2019), ("audi", 2018), ("mercedes", 2020)]

# doubled_year = list(map(lambda car: (car[0], car[1] * 2), cars))

#------------ filter

# numbers = list(range(1,101))
# only_even = lambda n: n % 2 == 0
# evens = list(filter(only_even, numbers))


#------------ reduce
# numbers = list(range(1,101))
# sum = functools.reduce(lambda n1, n2: n1 + n2, numbers)
# max = functools.reduce(lambda n1, n2: max(n1, n2), numbers)

#------------ list comprehensions

# squares = [number*2 for number in range(1,21)]
# filtered = [number for number in range(1,51) if number % 2 == 0]
# nested_list = [[1, 2], [3, 4, 5], [6, 7]]
# flattened_list = [item for sublist in nested_list for item in sublist]
# words = ["apple", "banana", "cherry"]
# first_letters = [word[0] for word in words]

#------------ dictionary comprehensions


# squares = { number: number * 2 for number in range(1,11) }
# strings = ["Hello", "World", "Apple", "Murad", "Comprehensions", "Multiply"]
# length_of_strings = { string: len(string) for string in strings }
# even_odd = { number: "Even" if number % 2 == 0 else "Odd" for number in range(1,21) }
# sentence = "I love you so much, very very much"
# splitted = sentence.split()
# frequency = { word: splitted.count(word) for word in splitted }


#------------ zip function

# usernames = ["Biolater", "mury.ash", "feeezss"]
# passwords = ["linor124", "p2@ssword", "ayyyettim12"]
# zipped = zip(usernames, passwords)


#------------ time module

# import time

# print(time.time())
# print(time.gmtime(0))
# print(time.ctime(time.time()))
# for i in range(1,11):
#     print(i)
#     time.sleep(1)
# print(time.localtime(time.time()))
# print(time.strftime("%H:%M:%S", time.localtime()))
