def sumMultiples (max_num, first_mult, second_mult):
    accumulator = 0

    for i in range(max_num):
        if 0 is i % first_mult:
            accumulator += i
        elif 0 is i % second_mult:
            accumulator += i

    return accumulator

if __name__ == '__main__':
    max_num = int(input("Please enter the range you'd like to sum."))
    first_mult = int(input("Please enter the first multiple you'd like to get the sums of."))
    second_mult = int(input("Please enter the second multiple you'd like to get the sums of."))

    sum = sumMultiples(max_num, first_mult, second_mult)

    print("The sum of multiples of {} and {} in the range of 0 to {} is {}.".format(first_mult, second_mult, max_num, sum))
