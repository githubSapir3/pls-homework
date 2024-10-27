import sys
import time

"""
Structure of software languages Exercise 2

Authors:
Eti kenig 213873904
Sapir Fick 32637815
"""

# -------------------question 1------------------
def create_tuple_recursive(n):
    if n == 1:
        return (1,)
    else:
        return create_tuple_recursive(n - 1) + (n,)


def create_tuple_tail_recursive(n):
    def tail_recursive(n, acc=()):
        if n == 0:
            return acc
        else:
            return tail_recursive(n - 1, acc + (n,))

    return tail_recursive(n)


recursive_result = create_tuple_recursive(100)
tail_recursive_result = create_tuple_tail_recursive(100)


# -----------------question 2-------------------
def sum_array(arr):
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])


def tail_sum_array(arr):
    def tail_sum(arr, sum):
        if not arr:
            return sum
        else:
            return tail_sum(arr[1:], sum + arr[0])

    return tail_sum(arr, 0)


print(sum_array(recursive_result))
print(tail_sum_array(recursive_result))

# -----------------question 3-------------------
def lcm_recursive(a, b, multiple=0):
    # מוצאים את המספר הגדול והקטן
    bigger = max(a, b)
    smaller = min(a, b)
    if multiple is 0:
        multiple = bigger
    if multiple % smaller == 0:
        return multiple
    return lcm_recursive(a, b, multiple + bigger)



print(lcm_recursive(12, 18)) 
print(lcm_recursive(10, 15))

# -----------------question 4-------------------
def to_digits(n):
    if n < 10:
        return [n]
    return to_digits(n // 10) + [n % 10]


def recursive_is_palindrome(digits):
    if len(digits) <= 1:
        return True
    return digits[0] == digits[-1] and recursive_is_palindrome(digits[1:-1])


def recursive_tail_is_palindrome(digits):
    def is_palindrome(digits, start=0, end=None):
        if end is None:
            end = len(digits) - 1
        if start >= end:
            return True
        return digits[start] == digits[end] and is_palindrome(digits, start + 1, end - 1)

    return is_palindrome(digits)


print(recursive_is_palindrome(to_digits(12321)))
print(recursive_tail_is_palindrome(to_digits(12321)))


# -----------------question 5-------------------
def sortedzip(*lists):
    # Base case: if there is only one element left, return it as a list
    if len(lists[0]) == 1:
        return [tuple(l[0] for l in lists)]
    
    # Find the minimum element (according to the first list) and its index
    min_index = min(range(len(lists[0])), key=lists[0].__getitem__)
    
    # Extract the minimum element tuple
    min_tuple = tuple(l[min_index] for l in lists)
    
    # Recursively call sortedzip on lists without the minimum element
    remaining_lists = [l[:min_index] + l[min_index+1:] for l in lists]
    
    return [min_tuple] + sortedzip(*remaining_lists)

# Test example
print(sortedzip([3, 1, 2], [5, 6, 4], ['a', 'b', 'c']))




"""---------------Lazy Evaluations and Generators-----------------"""


# -----------------question 1---------------

    # part A
def create_full_array():
    start_time = time.time()
    full_array = list(range(10001))
    end_time = time.time()
    execution_time = end_time - start_time
    memory_size = sys.getsizeof(full_array)

    # Part B
    start_time = time.time()
    first_5000_array = full_array[:5000]
    end_time = time.time()
    exec_time_first_5000 = end_time - start_time
    memory_size_first_5000 = sys.getsizeof(first_5000_array)

    return full_array, execution_time, memory_size, first_5000_array, exec_time_first_5000, memory_size_first_5000


def create_full_array_lazy():
    # Part A
    start_time = time.time()
    full_array = range(10001)
    end_time = time.time()
    execution_time = end_time - start_time
    memory_size = sys.getsizeof(full_array)

    # Part B
    start_time = time.time()
    first_5000_array_lazy = full_array[:5000]
    end_time = time.time()
    execution_time_5000 = end_time - start_time
    memory_size_5000 = sys.getsizeof(first_5000_array_lazy)
    return full_array, execution_time, memory_size, first_5000_array_lazy, execution_time_5000, memory_size_5000


full_array, exec_time_full, memory_size_full, first_5000_array, exec_time_first_5000, memory_size_first_5000 = create_full_array()
print("\nPart A normal")
print(f"Execution Time (full array): {exec_time_full:.6f} seconds")
print(f"Memory Size (full array): {memory_size_full} bytes")
print(f"Type of full array: {type(full_array)}")
print("\nPart B normal")
print(f"Execution Time (first 5000): {exec_time_first_5000:.6f} seconds")
print(f"Memory Size (first 5000): {memory_size_first_5000} bytes")
print(f"Type of first 5000 array: {type(first_5000_array)}")

full_array_lazy, exec_time_full_lazy, memory_size_full_lazy, first_5000_array_lazy, execution_time_5000, memory_size_5000 = create_full_array_lazy()
print("\nPart A Lazy")
print(f"Execution Time (lazy full array): {exec_time_full_lazy:.6f} seconds")
print(f"Memory Size (lazy full array): {memory_size_full_lazy} bytes")
print(f"Type of lazy full array: {type(full_array_lazy)}")
print("\nPart B Lazy")
print(f"Execution Time (lazy first 5000): {execution_time_5000:.6f} seconds")
print(f"Memory Size (lazy first 5000): {memory_size_5000} bytes")
print(f"Type of lazy first 5000 array: {type(first_5000_array_lazy)}")


# -----------------question 2---------------
def prime_numbers():
    num = 1
    while True:
        if not any(num % x == 0 for x in range(2, int(num ** 0.5) + 1)):
            yield num
        num += 1


# example of getting the first 10 prime numbers
primes = prime_numbers()
for x in range(10):
    print(next(primes))


# -----------------question 3-------------------
