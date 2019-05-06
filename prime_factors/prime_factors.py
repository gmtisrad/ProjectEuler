from math import ceil

def prime_factorization(to_factor):
    for i in reversed(range(ceil(to_factor/2))):
        if 0 is to_factor % (i+1):
            print("{} is a factor.".format(i+1))
            is_prime = True
            for j in range(ceil(i+1)):
                if 0 is i % (j+1) and 1 is not j+1:
                    is_prime = False
            if is_prime:
                return i+1

if __name__ == "__main__":
    number = int(input("Enter the number to find the largest prime factor for."))
    largest_factor = prime_factorization(number)

    print("The largest prime factor of {} is {}.".format(number, largest_factor))
