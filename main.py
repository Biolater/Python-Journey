import math
import time
from typing import Union
import random

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

# random_int = random.randint(1,50)
# random_float = random.random()
# list_items = ["a","b","c","d","e"]
# random.shuffle(list_items)

# print(random_int)
# print(random_float)
# print(random.choice(list_items))
# print(list_items)


#------------ exception handling

# try:
#     numerator = int(input("Enter a number to divide:"))
#     denominator = int(input("Enter a number to divide by:"))
#     result = numerator / denominator    
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError:
#     print("You can only enter a numeric value")
# except Exception:
#     print("something went wrong")
# else: 
#     print(result)



