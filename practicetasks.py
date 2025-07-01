# even odd check  -----------------------
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Even")
# else:  
#     print("Odd")

# Find the greatest number ----------
# num1 = int(input("enter number 1: "))
# num2 = int(input("enter number 2: "))
# num3 = int(input("enter number 3: "))

# if num3 < num1 >num2:
#     print("Number", num1, "is greater")
# elif num3 < num2 >num1:
#     print("Number", num2, "is greater")
# elif num1 < num3 >num2:
#     print("Number", num3, "is greater")
# elif num1 == num2 == num3:
#     print("All numbers are equal")
# elif num1 == num2 > num3:
#     print("Number", num1, "and", num2, "are both equal and greater than", num3)
# elif num1 == num3 > num2:
#     print("Number", num1, "and", num3, "are both equal and greater than", num2)
# elif num2 == num3 > num1:
#     print("Number", num2, "and", num3, "are both equal and greater than", num1)
# else:
#     print("Invalid input")


# Sum of first N natural numbers -----------
# def countsum(n):
#     sum = n * (n + 1) // 2
#     return sum
 
# number = int(input("Enter Number N: "))
# print("Sum of first", number, "natural numbers is:", int(countsum(number)))

# Meow N times -------------------
# def main():
#     number  = get_number()
#     meow(number)

# def get_number():
#     while True:
#             n = int(input("what's n? "))
#             if n > 0:
#                 break
#     return n
# def meow(n):
#     for i in range(n):
#         print("Meow", end=" ")
        
# main()

# students = {
#     "umar": "20",
#     "Ali": "21",
#     "Ahmed": "22",
# }

# for student in students:
#     print(student, students[student], sep=", ")

# Get a number from the user and print it
# -----------------------------------
# def main():
#      x = get_number("what's x? ")
#      print(f"x is: {x}")

# def get_number(prompt):
#      while True:
#           try:
#             return int(input(prompt)) 
#           except ValueError:
#             pass
          
# main()

# lfunc = lambda x : "even" if x % 2 == 0 else "odd"
# y= int(input("Enter a number: "))

# print(lfunc(y),"number: check by lambda function")

# Decorators in Python
# --------------------------------------------------
# from time import sleep, time

# def ticktok(func):
#     def Wrapper(*args, **kwargs):
#         t1 = time()
#         result = func(*args, **kwargs)
#         t2 = time() - t1
#         print(f"Time taken to execute {func.__name__} is {t2} seconds")
#         #return result
#     return Wrapper

# @ticktok
# def siarra_ok(a):
#     check_even_odd = lambda x : "even" if x % 2 == 0 else "odd"
#     print(f"{a} is {check_even_odd(a)}")
#     sleep(1)  

# print(siarra_ok(int(input("Enter a number to find even or odd: "))))

