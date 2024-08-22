import random
import os

# name = "Murad"
# age = 17
# hobby = "coding"

# movies = ["The Godfather", "The Dark Knight", "The Prestige"]
# movies.append("Inception")
# print(movies[1])

# try:
#     age = int(input("Enter your age: "))
#     if age < 18:
#         print("You are minor!")
#     elif age >= 18 and age < 65:
#         print("You are an adult!")
#     else:
#         print("You are an elder!")
# except ValueError:     
#     print("Invalid input!")
    

# def greet(name: str) -> None:
#     print(f"My name is {name}")
    
# greet("Murad")

# def add (a: int, b: int) -> int:
#     return a + b

# print(add(1, 2))

# def sumNumbers(list: list) -> int:
#     sum = 0
#     for number in list:
#         sum += number
#     return sum

# print(sumNumbers([1, 2, 3, 4, 5]))

# hello = lambda name: print(f"Hello {name}!")

# hello("Murad")


# person = {
#     "name": "Murad",
#     "age": 17,
#     "hobby": "coding",
#     "city": "Baku"
# }

# print(person.get("name"))
# person.update({"city": "Istanbul"})
# person.update({"favorite_color": "blue"})
# print(person)

# sentence = "Python is fun!"
# print(sentence.title())
# if "Python" in sentence:
#     print("Yes")
# else:
#     print("No")
# print(len(sentence))

# print(sentence[:4])
# print(sentence.split(" ")[len(sentence.split(" ")) - 1])
# modified_sentence = sentence.replace("fun", "awesome")

# print(modified_sentence)


# for i in range(1,6):
#     for j in range (1, 6):
#         product = i * j
#         print(f"{i} * {j} = {product}")
        
    
        
# random_n = random.randint(1,11)

# while True:
#     try:
#         number = int(input("Enter a number: "))
#         if number == random_n:
#             print("You guessed correctly!")
#             break
#         elif number < random_n:
#             print("Higher")
#             continue
#         else:
#             print("Lower")
#             continue
#     except ValueError:
#         print("Invalid input! Please enter a number.")
#         continue


# numbers = [n for n in range(1,11)]
# squares = [n*2 for n in numbers]
# evens = [n for n in numbers if n % 2 == 0]

# print(numbers)
# print(squares)
# print(evens)

# with open("new.txt", "r") as text_file:
#     print(text_file.read())

# def write_user_info_to_file():
#     try:
#         name = input("Please enter your name: ")
#         age = int(input("Please enter your name: "))
#         if len(name.strip()) == 0:
#             raise ValueError("Name cannot be empty.")
#         with open("user_info.txt", "w") as user_info_file:
#             user_info_file.write(f"Name: {name}\n")
#             user_info_file.write(f"Age: {age}\n")
#         print("User information has been saved to user_info.txt!")

#     except ValueError:
#         print("Invalid age entered. Please enter a number.")

# write_user_info_to_file()


# class Dog:
#     def __init__(self, name, breed) -> None:
#         self.name = name
#         self.breed = breed
        
#     def bark(self):
#         print(f"{self.name}: Woof! Woof!")
    
    

# pitbull = Dog("pitbull", "wild")

pitbull.bark()