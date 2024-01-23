N = int(input("What`s N?"))


def is_prime(n):
    if n <= 1:
        return False  # 1 and negative numbers are not prime

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # N is evenly divisible by i, so N is not prime

    return True  # If no i divides N, then N is prime


result = is_prime(N)
print(result)
