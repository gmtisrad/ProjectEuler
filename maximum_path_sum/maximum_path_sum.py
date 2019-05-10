def get_triangle():
    my_triangle = []
    input_file = open("/home/gtimm/Documents/Projects/ProjectEuler/maximum_path_sum/data.txt")

    for line in input_file:
        my_triangle.append(str.split(line))

    return my_triangle

# Greedy depth first not brute force
def probe(triangle, x = 0, y = 0, current_sum = 0):
    idx = x
    idy = y
    current_sum = current_sum

    if x == 0 and y == 0:
        current_sum = int(triangle[x][y])

    if (len(triangle) - idx >= 2):
        largest = 0
        best_idy = 0

        for idyp in range(len(triangle[idx + 1])):
            num = int(triangle[idx + 1][int(idyp)])
            accumulator = 0
            if not(idyp == idy or idyp == idy + 1):
                print("{} didn't line up with {} below.".format(num, num2))
                break
            else:
                for idypt in range(len(triangle[idx + 2])):
                    accumulator = num
                    num2 = int(triangle[idx + 2][idypt])
                    if idypt == idyp or idypt == idyp + 1:
                        accumulator += num2
                        if largest < accumulator:
                            largest = accumulator
                            best_idy = idypt
                    else:
                        print("{} didn't line up with {} below.".format(num, num2))
                        break;
        print("{} + {} = {}".format(current_sum, largest, current_sum + largest))
        current_sum += largest


    if len(triangle) - idx + 1 == 1:
        largest = 0
        if triangle[idx + 1][idy] > triangle[idx + 1][idy + 1]:
            current_sum += triangle[idx + 1][idy]
        else:
            current_sum += triangle[idx + 1][idy]
        idx += 1
    if len(triangle) == idx + 1:
        return current_sum
    else:
        probe(triangle, idx + 2, idy, current_sum)

# Brute force attempt
def brute_force(triangle, accumulator, idx, idy, data = []):
    new_idy = idy

    if idx == -1:
        brute_force(triangle, accumulator + int(triangle[idx + 1][idy]), idx + 1, idy, data)
    else:
        if idx < len(triangle) - 1:
            brute_force(triangle, accumulator + int(triangle[idx + 1][idy]), idx + 1, idy, data)
            brute_force(triangle, accumulator + int(triangle[idx + 1][idy + 1]), idx + 1, idy + 1, data)
        else:
            data.append(accumulator)






if __name__ == "__main__":
    triangle = get_triangle()
    store = []

    brute_force(triangle, 0, -1, 0, store)

    largest = 0

    for i in store:
        if i > largest:
            largest = i
            print(largest)
    print(largest)