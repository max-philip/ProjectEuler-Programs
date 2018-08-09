
def binary_palindrome(x):
    bnum = int(bin(x)[2:])

    is_palindrome = 1
    for i in range(1, len(str(bnum))//2 + 1):
        if str(bnum)[i-1] != str(bnum)[-i]:
            is_palindrome = 0
            break
    if is_palindrome:
        return bnum
    else:
        return 0



num_max = 1000000

print('\nNumbers under ' + str(num_max) + ' that are palindromes in decimal and binary: \n')

dec_sum = 0

for i in range(1, num_max):

    is_palindrome = 1
    for j in range(1, len(str(i))//2 + 1):
        if str(i)[j-1] != str(i)[-j]:
            is_palindrome = 0
            break

    if is_palindrome:

        binary_p = binary_palindrome(i)

        if binary_p:
            print('{:7d} = {}'.format(i, binary_p))
            dec_sum += i

print('\nThe decimal sum of all these palindromes is ' + str(dec_sum))

k = input('\nAny key to exit')
        
        
