# Problem 25
# Circular Primes

# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
# 71, 73, 79, and 97.

# How many circular primes are there below one million?

from itertools import permutations


def make_rotations(num):
    return [''.join(p) for p in permutations(num)]


def is_prime(x):
   for i in range(2, (int(x/2)+1)):
       if (x % i) == 0:
           return False
   return True


k = int(input("Enter max num: "))
count = 0
for num in range(2, k):
    rotates = make_rotations(str(num))

    all_primes = True

    for perm in rotates:
        if not is_prime(int(perm)):
            all_primes = False
            break

    if all_primes:
        count += 1

print(count)
