from math import factorial

assume_max = 99999

print('Numbers which are equal to the sum of the factorial of their digits: \n')

total_sum = 0

for i in range(3, assume_max):

    fac_sum = 0
    for j in range(0, len(str(i))):
        fac_sum += factorial(int(str(i)[j]))

        if fac_sum > i:
            break

    if fac_sum == i:
        print(i)
        total_sum += i

print('Total sum: ' + str(total_sum))
        
k = input('\nAny key to exit')
