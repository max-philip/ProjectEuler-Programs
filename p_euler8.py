

num = int(input('Enter a 1000-digit number: '))

num_len = 1000
large_num = 0

for i in range(0, num_len-13):

    curr_num = int(str(num)[i])
    for ind in range(1, 13):
        curr_num *= int(str(num)[(i+ind)])

    if curr_num > large_num:
        large_num = curr_num

print('The greatest 13 adjacent product is: ', large_num)

k = input('\nPress any key to exit')
