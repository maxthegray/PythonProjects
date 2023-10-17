import math

def is_perfect_square(a):
        if a < 0:
                    return False
        sqrt_a = int(math.sqrt(a))
        return sqrt_a * sqrt_a == a

def is_prime(num):
        if num < 2:
                    return False
        for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                          return False
        return True

num = int(input("Enter a number: "))

if is_perfect_square(num):
        print(num, "is a perfect square.", math.sqrt(num))
else:
        print(num, "is not a perfect square.", math.sqrt(num))

if is_prime(num):
        print(num, "is a prime number.")
else:
            print(num, "is not a prime number.")
