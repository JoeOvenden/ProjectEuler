from math import trunc, sqrt
from itertools import cycle

def get_cycles(number):
    cycle_list = []
    number_str = str(number)
    for i in range(len(number_str)):
        element = int(number_str[i::] + number_str[0:i])
        cycle_list.append(element)
    return cycle_list


def get_unique_cycles(number):
    cycle_list = []
    number_str = str(number)
    for i in range(len(number_str)):
        element = int(number_str[i::] + number_str[0:i])
        if element not in cycle_list:
            cycle_list.append(element)
    return cycle_list


def is_palindrome(n):
    n_reversed = int(str(n)[::-1])
    if n == n_reversed:
        return True


def binary_search(ordered_list, x, pointer_left = None, pointer_right = None):
    # check to see if x is in the ordered_list
    if pointer_left is None:
        pointer_left = 0
        pointer_right = len(ordered_list) - 1
        
    # if list is empty, then x is not in the list
    if len(ordered_list) == 0:
        return False

    test_index = trunc((pointer_left + pointer_right)/2)

    # found the item, hooray!
    if ordered_list[test_index] == x:
        return True

    # this scenario means that we have exhausted the list and not found the item
    elif pointer_left == pointer_right:
        return False

    # search the left side
    elif ordered_list[test_index] > x:
        pointer_right = test_index - 1
        if pointer_right < pointer_left:
            return False
        else:
            return binary_search(ordered_list, x, pointer_left, pointer_right)

    # search the right side
    elif ordered_list[test_index] < x:
        pointer_left = test_index + 1
        return binary_search(ordered_list, x, pointer_left, pointer_right)


def get_N_pentagon_numbers(N):
    #returns N pentagon numbers
    pentagon_numbers = [1]
    for i in range(2, N + 1):
        pentagon_number = pentagon_numbers[i - 2] + (3 * i) - 2
        pentagon_numbers.append(pentagon_number)
    return pentagon_numbers


def get_N_triangle_numbers(N):
    #returns N triangle numbers
    triangle_numbers = []
    triangle_number = 0
    for i in range(1, N + 1):
        triangle_number += i
        triangle_numbers.append(triangle_number)
    return triangle_numbers


def get_triangle_numbers(x):
    #returns all triangle numbers <= x
    triangle_numbers = []
    triangle_number = 1
    n = 1
    while n <= x:
        triangle_numbers.append(triangle_number)
        n += 1
        triangle_number += n
    return triangle_numbers


def get_N_more_primes(primes, N):
    # prime list is assumed to contain all primes up until the last element
    # adds the next N primes to the prime list

    # incase the list of primes [2] gets passed
    # since number would get set to 2 but gets incremented by 2
    # so would miss all primes
    new_primes = []
    if len(primes) == 1:
        primes.append(3)

    number = primes[-1] + 2
    primes_added = 0
    while primes_added != N:
        if check_prime(primes, number) is True:
            primes.append(number)
            primes_added += 1
        number += 2


def check_prime(primes, number):
    # prime list is assumed to contain all primes up until the last element
    # highest prime must be at least trunc(sqrt(number))
    # returns True if number is prime
    isPrime = True
    divisor_limit = trunc(sqrt(number))
    for divisor in primes:
        if divisor > divisor_limit:
            break
        else:
            if number % divisor == 0:
                isPrime = False
                break
    if isPrime:
        return True
    else:
        return False


def get_primes_up_to(N):
    # returns all primes < n
    primes = [2]
    for number in range(3, N, 2):
        if check_prime(primes, number):
            primes.append(number)
    return primes


def get_N_primes(N):
    # returns the first N primes
    primes = [2]
    counter = 1
    number = 3
    while counter != N:
        if check_prime(primes, number):
            primes.append(number)
            counter += 1
        number += 2
    return primes

