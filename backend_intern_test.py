# Python Test for Backend Development Intern
# Date: July 17, 2025
# Instructions:
# - Solve each problem below.
# - You are allowed to use Google search but not ChatGPT or other LLMs.
# - Write your code below each problem statement.
# - Make sure to test your code with the provided examples.
# Note: You may need to install the requests library using pip install requests for Problem 4.

# ---
# Problem 1: Data Processing with Lists, Lambdas, and Dictionaries
# You are given a list of dictionaries representing products, where each dictionary has the keys 'name', 'price', 'category', and 'stock'.
# Write a Python script that:
# - Filters the products to include only those with a price greater than 50 and stock greater than 0.
# - Creates a new list containing dictionaries with only the 'name' and 'category' keys.
# - Groups the products by 'category' into a dictionary where the keys are category names and the values are lists of product names.
# Use list comprehensions and lambda functions where appropriate.
# Example Input:
# products = [
#     {"name": "Laptop", "price": 1000, "category": "Electronics", "stock": 5},
#     {"name": "Mouse", "price": 25, "category": "Electronics", "stock": 10},
#     {"name": "Desk", "price": 75, "category": "Furniture", "stock": 3},
#     {"name": "Chair", "price": 60, "category": "Furniture", "stock": 0}
# ]
# Expected Output:
# {
#     "Electronics": ["Laptop"],
#     "Furniture": ["Desk"]
# }
# Your code here: 
#                     <- logic -> 
#printing only category and name of product then iter in our list of dictionary
#then simple check if price > 50 and stock > 0 return new list 
print("\n----------------------------Problem 1 --------------------------------\n")
def process_products(products):
    # Filter products with price > 50 and stock > 0
    filteredbypricestock = [product for product in products if product["price"] > 50 and product["stock"] > 0]
    grouped = {category: [p["name"] for p in filteredbypricestock if p["category"] == category]
               for category in set(p["category"] for p in filteredbypricestock)}
    return grouped
# Uncomment the following to test your function
products = [
    {"name": "Laptop", "price": 1000, "category": "Electronics", "stock": 5},
    {"name": "Mouse", "price": 60, "category": "Electronics", "stock": 10},
    {"name": "Desk", "price": 75, "category": "Furniture", "stock": 3},
    {"name": "Chair", "price": 60, "category": "Furniture", "stock": 0},
    {"name": "Table", "price": 60, "category": "Electronics", "stock": 1},
    {"name": "Bed", "price": 60, "category": "Furniture", "stock": 2},
    {"name": "Monitor", "price": 60, "category": "Electronics", "stock": 15}
]
print(process_products(products))

# ---
# Problem 2: Recursion for Tree Traversal
# You are given a nested dictionary representing a file system, where keys are folder names and values are either sub-dictionaries (for subfolders) or lists of files (with their sizes in the format 'filename:size').
# Write a recursive function to calculate the total size of all files in the file system.
# Example Input:
file_system = {
    "folder1": {
        "subfolder1": ["file1.txt:100", "file2.txt:200"],
        "subfolder2": ["file3.txt:150"]
    },
    "folder2": ["file4.txt:300"]
}
# Expected Output:
# 750  # Total size: 100 + 200 + 150 + 300
# Your code here:
#------------after first question uncomment-----------------#
print("\n---------------------------Problem 2 ---------------------------------")
def calculate_total_size(file_system):
    total = 0
    for x, y in file_system.items():
        if isinstance(y, dict):
            # y = y.split('.txt:')
            #total += y
            total += calculate_total_size(y)
        elif isinstance(y, list):
            for file in y:
                name, size = file.split('.txt:')
                total += int(size)
    return total

# Uncomment the following to test your function
# file_system = {
#     "folder1": {
#         "subfolder1": ["file1.txt:100", "file2.txt:200"],
#         "subfolder2": ["file3.txt:150"]
#     },
#     "folder2": ["file4.txt:300"]
#}
print(calculate_total_size(file_system))

# ---
# Problem 3: Inheritance and Exception Handling
# Design a base class Vehicle with two methods: start and drive.
# Create at least two subclasses, such as Car and Bicycle, each implementing these methods differently.
# Include exception handling to manage potential errors, such as attempting to start a vehicle with no fuel or driving a vehicle that hasn’t been started.
# Define a custom exception class VehicleError for these error conditions.
# Provide an example usage that demonstrates how exceptions are raised and handled in various scenarios.
# Your code here:
#------------ Second question -----------------#
print("\n---------------------------Problem 3 ---------------------------------")
class VehicleError(Exception):
    pass

class Vehicle:
    def start(self):
        raise NotImplementedError("Subclasses must implement this method")

    def drive(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def __init__(self):
        self.fuel = 0
        self.started = False

    def start(self, fuel):
        self.fuel = fuel
        if self.fuel <= 0:
            raise VehicleError("Cannot start car: No fuel.")
        self.started = True
        print(f"\nCar Starting... fuel remaining {self.fuel} liters")

    def drive(self):
        if not self.started:
            raise VehicleError("Cannot drive car: Car not started.")
        print("Car is driving...")

class Bicycle(Vehicle):
    def __init__(self):
        self.started = False

    def start(self):
        self.started = True
        print("Bicycle ready to ride!")

    def drive(self):
        if not self.started:
            raise VehicleError("Cannot ride bicycle: Bicycle not rideable.")
        print("Cyclingg...")

def demonstrate_vehicles():
    try:
        car = Car()
        car.start(10)
        car.drive()
        # drive car without start 
        car2 = Car()
        car2.drive()
    except VehicleError as error:
        print(f"Car error: {error}")
    try:
        bike = Bicycle()
        bike.start()
        bike.drive()
        # call without start function in bicycle
        bike2 = Bicycle()
        bike2.drive()
    except VehicleError as e:
        print(f"Bicycle error: {e}")
#-------------------------------------------------------#
# Uncomment the following to run the demonstration
demonstrate_vehicles()

# ---
# Problem 4: Concurrency with Threading or Multiprocessing
# Write a Python script that downloads the content of multiple URLs concurrently.
# You are given a list of URLs (use placeholder URLs like "http://example.com" for testing).
# Choose between using threading or multiprocessing to implement the concurrency, and include a short comment explaining your choice (considering whether the task is I/O-bound or CPU-bound and the role of the GIL).
# Measure and print the time taken compared to a sequential approach.
# Use the requests library for simplicity.
# Example Input:
urls = ["http://example.com", "http://example.org", "http://example.net",]
# # Expected Output:
# # Prints the length of content downloaded from each URL and the time taken for both concurrent and sequential approaches.
# # Your code here:
# #------------after third question uncomment-----------------#
print("\n---------------------------Problem 4 ---------------------------------")
# task is I/O bound specifically because it send request to server and wait to receive request from website/server. I/O tasks are involved and not computations from local machine.
import requests, threading, time
from concurrent.futures import ThreadPoolExecutor

thread_local = threading.local()

def download_concurrent(urls):
    start_time = time.time()
    download_all_sites(urls)
    duration = time.time() - start_time
    print(f"Downloaded concurrent {len(urls)} sites in {duration} seconds")

def download_all_sites(urls):
    with ThreadPoolExecutor(max_workers= 60) as executor:
        executor.map(download_site, urls)

def download_site(urls):
    session = get_session_for_thread()
    with session.get(urls) as response:
        print(f"Reading {len(response.content)} bytes from {urls}")

def get_session_for_thread():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

Start = 0
End = 0
def seqqqqqqqq():
    global Start
    global End
    def download_sequential(urls, delay=2):
        time.sleep(delay) 
        
    threads = []
    for link in urls:
        t = threading.Thread(target=download_sequential, args=(urls,), kwargs={"delay": 2})
        threads.append(t)
    for t in threads:
        Start = time.time()
        t.start()
        print(f"Sequential started for {link}")
    for t in threads:
        t.join()
        End = time.time() - Start
        print(f"Sequential ended for {link}")
    print(f"Downloaded sequential {len(urls)} sites in {End} seconds")


#-------------------------------------------------------------#
# Example usage:
#urls = ["http://example.com", "http://example.org", "http://example.net"]
print("Concurrent:")
download_concurrent(urls)

print("Sequential:")
seqqqqqqqq()


# ---
# Problem 5: Generators and Itertools
# Write a generator function that yields prime numbers up to a given limit.
# Then, use the itertools module to:
# - Extract the first 10 prime numbers using itertools.islice.
# - Filter out prime numbers that are not congruent to 1 modulo 6 (e.g., 7, 13, 19) using itertools.filterfalse.
# Example Input:
# limit = 50
# Expected Output:
# First 10 primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# Filtered primes (congruent to 1 mod 6): [7, 13, 19]
# Your code here:
#------------after fourth question uncomment-----------------#
print("\n---------------------------Problem 5 ----------------------------------\n")


import itertools

def prime_generator(limit):
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(num)):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num

def process_primes(limit):
    primes = prime_generator(limit)
    first_10 = list(itertools.islice(primes, 10))
    #primes_for_filter = prime_generator(limit)
    filtered = list(itertools.filterfalse(lambda x: x % 6 != 1, first_10))
    return first_10, filtered

# Example usage:
limit = 50
first_10, filtered = process_primes(limit)
print("First 10 primes:", first_10)
print("Filtered primes (mod 6 == 1):", filtered)

#--------------------------------------------------------------------#

# End of test. Please submit your completed code.
