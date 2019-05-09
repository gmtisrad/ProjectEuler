grid_string = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
grid = []
to_mult = 4

# Grid set up and helpers #

def create_grid(width):
    count = 0
    for idx in range(width):
        row = []
        for idy in range(width):
            row.append(get_number(count))
            count += 3
        grid.append(row)

def get_number(x):
    number = (grid_string[x] + grid_string[x+1])
    number = int(number)

    return number

def print_grid():
    for i in range(20):
        print(grid[i])

def traverse_grid(width):
    largest = 0
    
    for i in range(width):
        for j in range(width):
            # Getting the product of 4 up from the current location
            if i >= to_mult:
                number = up_product(i, j)
                if largest < number:
                    largest = number
            # Getting the product of 4 up_right from the current location
            if i >= to_mult and j <= width - to_mult:
                number = up_right_product(i, j)
                if largest < number:
                    largest = number
            # Getting the product of 4 right from the current location
            if j <= width - to_mult:
                number = right_product(i, j)
                if largest < number:
                    largest = number
            # Getting the product of 4 down_right from the current location
            if j <= width - to_mult and i <= width - to_mult:
                number = down_right_product(i, j)
                if largest < number:
                    largest = number
            # Getting the product of 4 down from current location
            if i <= width - to_mult:
                number = down_product(i, j)
                if largest < number:
                    largest = number
            # Getting the product of 4 down_left from the current location
            if i <= width - to_mult and j >= to_mult:
                number = down_left_product(i, j)
                if largest < number:
                    largest = number
            # Getting the product of 4 left from the current location
            if j >= to_mult:
                number = left_product(i, j)
                if largest < number:
                    largest = number
            # Getting the product of 4 up_left from the current location
            if j >= to_mult and i >= to_mult:
                number = up_left_product(i, j)
                if largest < number:
                    largest = number
    print(largest)
    return largest
            

# End grid set up and helpers #

# Products in all directions #

def up_product(x,y):
    accumulator = 1

    for idx in range(to_mult):
        accumulator *= grid[x-idx][y]
    return accumulator

def up_right_product(x,y):
    accumulator = 1

    for idx in range(to_mult):
        accumulator *= grid[x-idx][y+idx]
    return accumulator

def right_product(x,y):
    accumulator = 1

    for idx in range(to_mult):
        accumulator *= grid[x][y+idx]
    return accumulator

def down_right_product(x,y):
    accumulator = 1

    for idx in range(to_mult):
        accumulator *= grid[x+idx][y+idx]
    return accumulator

def down_product(x,y):
    accumulator = 1

    for idx in range(to_mult):
        accumulator *= grid[x+idx][y]
    return accumulator

def down_left_product(x,y):
    accumulator = 1

    for idx in range(to_mult):
        accumulator *= grid[x+idx][y-idx]
    return accumulator

def left_product(x,y):
    accumulator = 1

    for idx in range(to_mult):
        accumulator *= grid[x][y-idx]
    return accumulator

def up_left_product(x,y):
    accumulator = 1

    for idx in range(to_mult):
        accumulator *= grid[x-idx][y-idx]
    return accumulator

# End products in all directions #

if __name__ == "__main__":
    create_grid(20)

    print_grid()

    traverse_grid(20)