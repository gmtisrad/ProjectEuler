from math import ceil

def prime_factorization(to_factor):
    largest_factor = 1
    for i in range(ceil(to_factor/2)):
        i += 1
        if 0 is to_factor % i and to_factor >= i * i:
            isPrime = True
            for j in range(ceil((i+1)/2)):
                if (0 == i % (j+1)) and (i is not (j+1)) and 1 is not (j+1):
                    isPrime = False
                    print("{} % {}".format(i, (j+1)))
            if isPrime:
                largest_factor = i
    print(largest_factor)
    return largest_factor


if __name__ == "__main__":
    number = int(input("Enter the number to find the largest prime factor for."))
    largest_factor = prime_factorization(number)

    print("The largest prime factor of {} is {}.".format(number, largest_factor))
