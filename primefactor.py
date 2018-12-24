import sys


def get_factors(n):
    factors = []
    total_sum = 0  # Do the sum to increase performance
    num = n

    c_factor = 2
    while num % c_factor == 0:
        num //= c_factor
        factors.append(c_factor)
        total_sum += c_factor

    c_factor = 3
    while c_factor <= (num // c_factor):
        while num % c_factor == 0:
            num //= c_factor
            factors.append(c_factor)
            total_sum += c_factor

        c_factor += 2

    if num > 1:
        factors.append(num)
        total_sum += num
    return factors, total_sum


def run_reduction(x):
    count = 1
    (factors, sum_factors) = get_factors(x)
    while not factors[0] == x:
        x = sum_factors
        count += 1
        (factors, sum_factors) = get_factors(x)
    return x, count


if __name__ == '__main__':
    results = []
    for line in sys.stdin:
        number = int(line.strip())
        if not number == 4:
            result = run_reduction(number)
            results.append(f"{result[0]} {result[1]}")
    print("\n".join(results))
