import functools
import datetime
def decorator():
    def wrapper(func):
        def inner():
            print("Starting decorator")
            result = func()
            print("Ending Decorator")
        return inner
    return wrapper

@decorator()
def say_hello():
    print("Hello, World!")

# # # #printing name with arguments with decorator ---------------------
# def Basic_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Welcome")
#         result = func(*args, **kwargs)
#         print("Goodbye")
#         return result
#     return wrapper

# @Basic_decorator
# def hello(name):
#     print(f"Hello, {name}!")
#     return 'end'

# print(hello("ok"))

# # #Printing Repeated names with decorator ----------------------
# # def repeat(num_times):
# #     def decorator_repeat(func):
# #         @functools.wraps(func)
# #         def wrapper(*args, **kwargs):
# #              def inner(*args, **kwargs):
# #                 print("Starting decorator")
# #                 for _ in range(num_times):
# #                     result = func(*args, **kwargs)
# #                 print("Ending Decorator")
# #                 return result
# #              return inner(*args, **kwargs)
# #         return wrapper
# #     return decorator_repeat

# # @repeat(num_times=3)
# # def printing_repeated_name(name):
# #     print(f"Printing name, {name}!")
    
# # print(printing_repeated_name("okname"))  


# ##calculating how many times function executed -----------------------

# class CountCalls():
#     def __init__(self, name):
#         self.name = name
#         self.calls = 0
#     def __call__(self, *args, **kwargs):
#         self.calls += 1
#         print(f"asdf Function {self.name} has been called {self.calls} times")
#         self.__call__ = 0
#         return self.name(*args, **kwargs)
    

# def check_execution_times(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         CountCalls.__call__+=1
#         print(f"Function {func.__name__} has been called {CountCalls.__call__} times")
#         return func(*args, **kwargs)
#     CountCalls.__call__ = 0 
#     return wrapper
    

# @check_execution_times
# def printingmessage(name):
#     print(f"Hello, {name}!" )

# print(printingmessage("okname"))
# print(printingmessage("okname2"))
# print(printingmessage("okname3"))
# print(printingmessage("okname4"))

# ##-----------------------------------------------##

def logs(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now(datetime.UTC)
        print(f"Executing Function \"{func.__name__}\" at {start_time} with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now(datetime.UTC)
        print(f" \"{func.__name__}\" returned: {result} at {end_time}, execution time: {end_time - start_time}")
        with open("logs.txt", "a") as log_file:
            log_file.write(f"Executing Function \"{func.__name__}\" at  {datetime.datetime.now(datetime.UTC)} with arguments: {args} and keyword arguments: {kwargs}\n \n \"{func.__name__}\" returned: {result} at {end_time}, execution time: {end_time - start_time}")
        return result
    return wrapper

@logs
def addition(a,b,c):
    return a + b + c

print("After addition: ",addition(7,9,3))  