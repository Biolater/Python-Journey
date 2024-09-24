import functools

greeting = lambda name="there": f"Hello, {name}!"




# print(greeting("Murad"))
# print(greeting())

# numbers = {1,2,3,4,5}
# numbers_2 = {5,6,7,8,9}

# print(numbers.union(numbers_2))
# print(numbers.intersection(numbers_2))
# print(numbers.difference(numbers_2))




# def calculateFactorial() -> int:
#     try:
#         number = int(input("Enter a number: "))
#         if number == 0:
#             return 0
#         if number == 1:
#             return 1
        
#         if number < 0:
#             raise ValueError("Number cannot be negative!")
        
#         return functools.reduce(lambda n1, n2: n1 * n2, [number for number in range(1, number+1)])
#     except Exception:
#         print("error occured")


        
# print(calculateFactorial())        