from math import pow

def power_digit_sum(num):
    return str(int(pow(2, num)))


if __name__ == "__main__":
    num_string = power_digit_sum(1000)
    accumulator = 0

    for i in range(len(num_string)):
        accumulator  = accumulator + int(num_string[i])

    print(accumulator)