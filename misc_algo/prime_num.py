
# find first n prime numbers
from math import sqrt
from math import ceil

def check_if_prime(number):
    """
    check whether a number is prime or not.
    :param number:
    :return:
    """
    prime = True
    sqrt_number = int(ceil(sqrt(number)))
    for i in range(2, sqrt_number + 1):
        if number % i == 0:
            prime = False
    return prime

def first_n_prime(n):
    """
    :param n: find first n prime number.
    :return:
    """
    prime_list = list()
    number = 2
    while len(prime_list) <= n:
        if check_if_prime(number):
            prime_list.append(number)
        number = number + 1
    return prime_list

print first_n_prime(15)