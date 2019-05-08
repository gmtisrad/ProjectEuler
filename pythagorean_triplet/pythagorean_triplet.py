from math import floor

def pythagorean_triplet(sum):
    a = 1
    b = 2
    c = 3

    found = False

    while a < (floor(sum / 3) - 1) and not found:

        b = a + 1

        while b < floor(sum / 2) and not found:

            c = (sum - (a + b))

            if is_triplet(a, b, c):

                found = True

                print("FOUND IT")

                return (a * b * c)

            print("a{}, b{}, c{}".format(a, b, c))

            b += 1

        print("a{}, b{}, c{}".format(a, b, c))

        a += 1


def is_triplet(a, b, c):
    csq = (c * c)

    asq = (a * a)

    bsq = (b * b)

    #print("{} + {} = {}".format(asq, bsq, csq))

    return ((asq + bsq) == csq)


if __name__ == "__main__":
    print(pythagorean_triplet(1000))
