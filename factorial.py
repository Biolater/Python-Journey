import functools
number = int(input("Enter a number: "))

all_numbers = list(range(1, number + 1))


print(functools.reduce(lambda x, y: x * y, all_numbers))