from random import randint
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@time_it
def bubble_sort(array):
    arr = array[:]  
    n = len(arr)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
        if already_sorted:
            break
    return arr

@time_it
def insertion_sort(array):
    arr = array[:]
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

def merge(left, right):
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_left == len(left):
            result += right[index_right:]
            break
        if index_right == len(right):
            result += left[index_left:]
            break
    return result

@time_it
def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(
        merge_sort(array[:midpoint]),
        merge_sort(array[midpoint:])
    )

@time_it
def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[randint(0, len(array) - 1)]
    low = [x for x in array if x < pivot]
    same = [x for x in array if x == pivot]
    high = [x for x in array if x > pivot]
    return quicksort(low) + same + quicksort(high)



arr = [64, 34, 25, 12, 22]

print("Bubble Sort:", bubble_sort(arr))
print("Insertion Sort:", insertion_sort(arr))
print("Merge Sort:", merge_sort(arr[:]))  
print("Quick Sort:", quicksort(arr[:]))   
