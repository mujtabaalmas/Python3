# #write a recursive function to print countdown of a given number 
from time import sleep

def countdown(n):
    print(n)
    sleep(1)            #adding sleep from import time to look real countdown
    if n > 0:
        countdown(n-1)

# # x = int(input("SET A TIMER !!!"))
# # if x<0:
# #     print(f"Cannot set that timer value {x}")
# # else:
# #     countdown(x)
# # print("CountDown Finished !!!")
countdown(3)
print("CountDown Finished !!!")

##-----------------------------------
# setup_string = """
# print("Iterative:")
# def factorial(n):
#     return_value = 1
#     for i in range(2, n + 1):
#         return_value *= i
#     return return_value
# """

# from timeit import timeit
# timeit("factorial(4)", setup=setup_string, number=10000000)
# print(timeit())

##-------------------------------
# setup_string = "from math import factorial"

# from timeit import timeit
# timeit("factorial(4)", setup=setup_string, number=10000000)

# print(timeit())

#---------------------------------

#Printing fibbonacci numbers on nth index #0,1,1,2,3,5,8
def fib(n):
    if n==0 or n==1:
        return n
    return  fib(n-1) + fib(n-2)

print("Fibbonacci Number:",fib(6))