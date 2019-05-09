def run_collatz(start_num):
    current = start_num
    collatz_list = [start_num]

    while current != 1:
        # Even case
        if 0 == current % 2:
            current = current / 2
        # Odd case
        else:
            current = (3 * current) + 1
        collatz_list.append(current)

    return len(collatz_list)

if __name__ == "__main__":
    max_collatz = 1000000
    largest_start = 0
    largest_length = 0

    for i in range(1, max_collatz + 1):
        length = run_collatz(i)
        if length > largest_length:
            largest_length = length
            largest_start = i
            print("New largest start: {} \nNew largest length: {}".format(largest_start, largest_length))

    print("Largest start: {} \nLargest length: {}".format(largest_start, largest_length))