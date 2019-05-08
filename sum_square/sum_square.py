def sum_square(range_to):
    sum_squared = 0
    sum_of_squares = 0

    for i in range(1, range_to+1):
        sum_squared += i
        sum_of_squares += (i * i)

    sum_squared = sum_squared * sum_squared

    difference = sum_squared - sum_of_squares

    print("{} - {} = {}".format(sum_squared, sum_of_squares, difference))

if __name__ == "__main__":
    sum_square(100)