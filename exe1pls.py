"""
Structure of software languages Exercise 1

Authors:
Eti kenig 213873904
Sapir Fick 32637815
"""

# 1a
def get_penta_num(n):
    return (n * (3 * n - 1)) // 2


# 1b
def penta_num_range(na, nb):
    return list(map(get_penta_num, range(na, nb)))


# 2
def sum_digit(num):
    return sum(list(map(int, str(num))))


# 3
def gimatric(word):
    gematria_dict = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5,
        'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
        'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60,
        'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100, 'ר': 200,
        'ש': 300, 'ת': 400
    }
    return sum(gematria_dict.get(letter, 0) for letter in word)


# 4
def is_prime(n):
    if n <= 1:
        return "not prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "not prime"
    return "prime"


def twin_primes(p1):
    if is_prime(p1-2):
        return p1-2
    if is_prime(p1+2):
        return p1+2
    return -1


def prime_dict(limit):
    return {p: (p + 2 if is_prime(p + 2) else (p - 2 if is_prime(p - 2) else None)) for p in range(2, limit + 1) if is_prime(p)}


def square(x):
    return x * x


def double(x):
    return x * 2


def inverse(x):
    return "Undefined" if x == 0 else 1 / x


def apply_functions(n, functions):
    return dict(map(lambda func: (func.__name__, list(map(func, n))), functions))
    
def c(funcs, nums):
    return tuple(zip(funcs, map(lambda f: tuple(map(f, nums)), funcs)))
    
def c3(funcs, nums):
    return tuple(zip(map(lambda f: f.__name__, funcs), map(lambda f: tuple(map(f, nums)), funcs)))
    

if __name__ == '__main__':
    # 1
    n = int(input("Enter value for the pentagonal number: "))
    print(f"Penta number for n={n}: {get_penta_num(n)}")

    na, nb = map(int, input("Enter the range for pentagonal numbers (n1 n2): ").split())
    print(f"Penta numbers range from {na} to {nb}: {penta_num_range(na, nb)}")
    # 2
    n = int(input("Enter a number to  sum of its digits: "))
    print(f"Sum of digits of {n}: {sum_digit(n)}")
    # 3
    word = input("Enter a Hebrew word to calculate its gematria value: ")
    print(f"Gematria value of '{word}': {gimatric(word)}")
    # 4
    num = int(input("Enter a number : "))
    print(f"the number {num} is {is_prime(num)}. the twin : {twin_primes(num)}")

    limit = int(input("Enter a limit "))
    print(f"the dictionary is {prime_dict(limit)}. ")

    # 6
    numbers = [1, 2, 3, 4, 0]
    functions = [square, double, inverse]
    result = apply_functions(numbers, functions)
    print(result)
