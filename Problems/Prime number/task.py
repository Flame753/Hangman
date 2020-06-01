number = int(input())


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if is_prime(number):
    print("This number is prime")
else:
    print("This number is not prime")