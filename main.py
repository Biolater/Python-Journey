import math
import time
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

# for i in range(10):
#     print(i)

# for i in range(30, 50):
#     print(i)

# for i in range(50, 101, 2):
#     print(i)
    
# for i in range(10, 0, -1):
#     print(i)

# user_name = "mury.ash"

# for i in user_name:
#     print(i)

# for seconds in range(10, 0, -1):
#     time.sleep(1)
#     print(seconds)

# print("Happy New Year!")