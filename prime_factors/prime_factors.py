from math import ceil
import time

def prime_factorization(to_factor):
    largest = 2

    count = 2
    start = time.time()
    while to_factor > count * count:
        if 0 == to_factor % count:
            if is_prime(count):
                print("{} is prime and {}".format(count, (largest < count)))
                if largest < count:
                    largest = count
        if count == 2:
            count += 1
        else:
            count += 2
    end = time.time()

    print ("Calculation took: {}s".format(end - start))
    return largest


def is_prime(num):
    isPrime = True

    idx = 2

    while num >= idx * idx:
        if 0 is num % idx:
            isPrime = False
        if idx is 2:
            idx += 1
        else:
            idx += 2
    return isPrime

if __name__ == "__main__":
    number = int(input("Enter the number to find the largest prime factor for."))
    largest_factor = prime_factorization(number)

    print("The largest prime factor of {} is {}.".format(number, largest_factor))
