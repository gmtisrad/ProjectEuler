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

def prime_summation(limit):
    accumulator = 2

    idx = 3

    while idx < limit:
        if is_prime(idx):
            accumulator += idx
        idx += 2

    print(accumulator)


if __name__ == "__main__":
    prime_summation(2000000)