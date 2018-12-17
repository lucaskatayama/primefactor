import sys

cache = {}


def get_factors(n):

    if n in cache:
        return cache[n]
    factors = []
    total_sum = 0
    c_factor = 2
    num = n

    while c_factor <= (num // c_factor):
        while num % c_factor == 0:
            num = num // c_factor
            factors.append(c_factor)
            total_sum = total_sum + c_factor
        c_factor = c_factor + 1

    if num > 1:
        factors.append(num)
        total_sum += num

    cache[n] = (factors, total_sum)
    return factors, total_sum


def run_reduction(x):
    count = 1
    (factors, sum_factors) = get_factors(x)
    while not factors[0] == x and not x == sum_factors:
        x = sum_factors
        count = count + 1
        (factors, sum_factors) = get_factors(x)
    return x, count


if __name__ == '__main__':
    results = []
    for line in sys.stdin:
        number = int(line.strip())
        result = run_reduction(number)
        results.append("{} {}".format(result[0], result[1]))
    print("\n".join(results))

