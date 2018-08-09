max_num = int(input('Enter a number > 7: '))
prime_sum = 2 + 3 + 5 + 7

for i in range(3, max_num):

    is_prime = 0

        
    if (i%2 != 0) & (i%3 != 0) & (i%5 != 0) & (i%7 != 0):
        for j in range(3, int(i**0.5)+1, 2):
            if i%j == 0:
                is_prime = 0
                break
            else:
                is_prime = 1

        if is_prime:
            prime_sum += i

print('The sum of primes below', max_num, 'is', prime_sum)

k = input('Press any key to exit')
