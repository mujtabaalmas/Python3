# #basic iterator from a list-------
# ok = [10, 20, 30]
# myiter  = iter(ok)
# print(next(myiter))  
# print(next(myiter))  
# print(next(myiter))  

# #creating a class for iterators 
# class CountUpTo():
#     def __iter__(self):
#         self.count = 1
#         return self
#     def __next__(self):
#         if self.count <= 5:
#             current = self.count
#             self.count +=1
#             return current
#         else:
#             raise StopIteration

# x =CountUpTo()
# y = iter(x)
# for z in y:
#     print(z, end=' ')
# # print(next(y)) 
# # print(next(y))
# # print(next(y))
# # print(next(y))

##diplaying characters from string using iterators
# mystr = "hello world"
# striter = iter(mystr)
# for i in striter:
#     print(i, end=' ')


# # Write a function that checks whether a given object is iterable or not.
# iterllist = "ok", 9,9,999, [12, 34, 56], (1, 2, 3), {1, 2, 3}, {'a': 1, 'b': 2}

# def is_iterable(a):
#     try:
#         iter(a)
#         return True
#     except TypeError:
#         return False
    
# if is_iterable(iterllist):
#     xyz = iter(iterllist)
#     for i in xyz:
#         print(i, end=' ')
# else:
#     print("The object is not iterable, cannot iterate over it.")
#     raise StopIteration

##Catching StopIteration Exception
# ele2 = 2,3
# iele2 = iter(ele2)
# try:
#     print(next(iele2))  
#     print(next(iele2))  
#     print(next(iele2))
# except StopIteration:
#     print("No more elements to iterate :)")


# Creating a custom iterator that generates Fibonacci numbers

class FibonacciIterator:
    def __init__(self, stop):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self): # magic methods 
        
        if self._index < self._stop:
            self._index += 1
            fib_number = self._current
            self._current, self._next = (
                self._next,
                self._current + self._next,
            )
            return fib_number
        else:
            raise StopIteration


for fibNum in FibonacciIterator(10):
    print(fibNum, end=' '*2)


