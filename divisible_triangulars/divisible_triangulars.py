def find_triangle_number(num):
    accumulator = 0

    for i in range(1, num+1):
        accumulator += i

    return accumulator

def find_factors(num):
    factors = []

    for i in range(1, num+1):
        if i in factors:
            break
        if 0 == num % i:
            factors.append(i)
            factors.append(num/i)
    
    print(len(factors))
    return len(factors)

if __name__ == "__main__":
    num_factors = 0
    current_triangle = 0
    count = 1

    while num_factors < 500:
        current_triangle = find_triangle_number(count)
        num_factors = find_factors(current_triangle)
        count += 1

    print (current_triangle)
