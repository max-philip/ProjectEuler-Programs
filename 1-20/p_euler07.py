from math import sqrt

num = 3
i=0

prime_no = 10001

while True:
    is_prime = 0

    for j in range(2, 1+int(sqrt(num+1))):
        if (num%j == 0):
            is_prime = 0
            break
        else:
            is_prime = 1
    
    if is_prime:
        i += 1

    if (i == prime_no-1):
        print(num)
        break

    num += 2
