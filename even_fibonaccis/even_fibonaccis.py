MAX_NUM = 4000000

def even_fibonaccis(accumulator, current, last):
    new_number = current + last

    if 0 is new_number % 2:
        accumulator += new_number
        print(new_number)

    if new_number <= MAX_NUM:
        return even_fibonaccis(accumulator, new_number, current)
    else:
        return accumulator

if __name__ == "__main__":
    max_fibs = even_fibonaccis(0, 0, 1)

    print ("Sum of all even fibonaccis is: {}.".format(max_fibs))