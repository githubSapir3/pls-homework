
import time
from functools import reduce
from datetime import datetime, timedelta
from math import factorial

"""
Structure of software languages Exercise 2

Authors:
Eti kenig 213873904
Sapir Fick 32637815
"""


"""question 1"""
func = lambda x: (x / 2) + 2

# 1.1
lst = list(map(func, range(0, 10001)))

# 1.2
start_time = time.time()
sum_lst = reduce(lambda x, y: x + y, lst)
end_time = time.time()

# 1.3
reduce_time = end_time - start_time
start_time = time.time()
sum_loop = 0
for num in lst:
    sum_loop += num
end_time = time.time()
loop_time = end_time - start_time
print(f"Time taken with reduce: {reduce_time} seconds")
print(f"Time taken with loop: {loop_time} seconds")

# 1.4
full_lambda = reduce(lambda x, y: x + y, list(map(func, range(0, 10001))))

"""question 2"""
numbers = list(range(1, 10001))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# 2.1
even_func = lambda sum, next: sum * next
odd_func = lambda x, next: (x / 2) + 2 + next

# 2.2
even_result = reduce(even_func, even_numbers)
odd_result = reduce(odd_func, odd_numbers)


"""question 3"""
def get_dates(start_date, num_dates, skip_days):
    date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    date_generator = (date_obj + timedelta(days=i * skip_days) for i in range(num_dates))
    return list(map(lambda d: d.strftime("%Y-%m-%d"), date_generator))


result_dates = get_dates("2024-01-01", 5, 7)

"""question 4"""
def power_function(base):
    return lambda x: base ** x


def power_map(x, n):
    return map(lambda i: x ** i, range(n + 1))


def taylor_exp(x, terms):
    return sum((x ** n) / factorial(n) for n in range(terms))


print(power_function(5))
print(list(power_map(2, 4)))
print(f"taylor_exp {taylor_exp(1, 10)}")


"""question 5"""
def task_manager():
    tasks = {}

    def add_task(task_name, status='incomplete'):
        if task_name not in tasks:
            tasks[task_name] = status

    def get_tasks():
        return tasks

    def complete_task(task_name):
        if task_name in tasks:
            tasks[task_name] = 'complete'

    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }


