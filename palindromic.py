import csv


def output_to_file(data, file):
    writer = csv.writer(file)
    writer.writerows(data)


def is_palindromic(i):

    if len(i) == 0:
        return False
    rev = list(reversed(i))
    return rev == i


def base10_to_baseN(n, b):
    assert b > 1

    if n == 0:
        return [0]

    result = list()
    while n > 0:
        result.insert(0, n % b)
        n //= b
    return result


def find_min_base_palindromic(n):
    base = 2
    rep = base10_to_baseN(n, base)
    while not is_palindromic(rep):
        base += 1
        rep = base10_to_baseN(n, base)
    return base


if __name__ == '__main__':
    output = list()
    for x in range(1, 1001):
        output.append((x, find_min_base_palindromic(x)))
    file = open("/Users/matthewwalsh/Desktop/palindromic.csv", "w")
    output_to_file(output, file)
