def find_palindrome_product():
    largest_palindrome = 0
    i = j = 999

    while (i > 0):
        j = i
        while(j > 0):
            if is_palindrome(i * j) and (i * j) > largest_palindrome:
                largest_palindrome = i * j
                print(largest_palindrome)
            j -=1
        i -= 1

    return(largest_palindrome)


def is_palindrome(number):
    is_palindrome = True
    num_string = str(number)
    right_sentinel = len(num_string)-1

    for i in range(right_sentinel):
        temp_num = right_sentinel - i
        if (i != temp_num and (num_string[i] != num_string[temp_num])):
            is_palindrome = False
        else:
            pass 

    return is_palindrome

if __name__ == "__main__":
    find_palindrome_product()