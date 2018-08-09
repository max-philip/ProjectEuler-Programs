
num = int(input('Enter a number: '))
largest_prime = 0
for i in range(2,num//2):
    is_prime = 0
    
    for a in range(2,i):
        if (i%a == 0):
            is_prime = 0
            break
        else:
            is_prime = 1
    if (is_prime) & (num%i == 0):
        largest_prime = i;
        print(largest_prime)

print('\nThe largest prime factor is: ',largest_prime)

k = input("\nPress any key to exit")
