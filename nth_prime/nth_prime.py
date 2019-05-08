from math import ceil

def find_nth_prime(n):
    # starting with one prime and changing the starting index to 3 to we can iterate over only odds
    prime_count = 1

    current_prime = 2

    num = 3

    while prime_count < int(n):
        if is_prime(num):
            print("{} is prime. Incrementing count.".format(num))
            prime_count += 1
            print("New prime count is {}.".format(prime_count))
            current_prime = num
        num += 2
    return current_prime


def is_prime(num):
    isPrime = True

    print("Determining primality of {}.".format(num))

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
    num_prime = input("Which number prime would you like to find?")
    print(find_nth_prime(num_prime))
