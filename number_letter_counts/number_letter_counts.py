from math import floor

def letter_count(range):
    thousands = int(range / 1000)
    hundreds = int((range % 1000)/100)
    tens = int((range % 100)/10)
    ones = int(range % 10)

    accumulator = 0

    ones_spelled = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    teens_spelled = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]

    tens_spelled = [
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    thousand = "thousand"

    hundred = "hundred"

    and_spelled = "and"

    if thousands > 0:
        accumulator += len(ones_spelled[thousands - 1])
        accumulator += len(thousand)
        print("{}{}".format(ones_spelled[thousands - 1], thousand))

    if hundreds > 0:
        accumulator += len(ones_spelled[hundreds - 1])
        accumulator += len(hundred)
        print("{}{}".format(ones_spelled[hundreds - 1], hundred))
        if tens > 0 or ones > 0:
            accumulator += len(and_spelled)
            print(and_spelled)

    if tens > 0:
        if tens != 1:
            accumulator += len(tens_spelled[tens-2])
            print("{}".format(tens_spelled[tens-2]))
        if tens == 1:
            accumulator += len(teens_spelled[ones])
            print("{}".format(teens_spelled[ones]))

    if ones > 0:
        if tens != 1:
            accumulator += len(ones_spelled[ones-1])
            print(ones_spelled[ones-1])


    print(accumulator)
    return(accumulator)
    # print("{} thousands {} hundreds {} tens {} ones".format(thousands, hundreds, tens, ones))

def letter_count_accumulator(to_count):
    accumulator = 0

    for i in range(1, to_count + 1):
        accumulator += letter_count(i)
        print(accumulator)

    return accumulator

if __name__ == "__main__":
    print(letter_count_accumulator(1000))
    #letter_count(101)