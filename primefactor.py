import sys
import time

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
    while not factors[0] == x and not sum_factors == x:
        x = sum_factors
        count = count + 1
        (factors, sum_factors) = get_factors(x)
    return x, count


if __name__ == '__main__':
    results = []
    for line in sys.stdin:
        start = time.time()
        number = int(line.strip())
        if not number == 4:
            result = run_reduction(number)
            end = time.time()
            results.append("{value:05f} {number} {r0} {r1}".format(value=(end-start), number=number, r0=result[0], r1=result[1]))
    print("\n".join(results))

