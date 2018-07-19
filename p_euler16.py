exp = int(input('Enter an integer: '))

digit_sum = 0

num = 2 ** exp

for i in range(0, len(str(num))):
    digit_sum += int(str(num)[i])

print('The value of 2^', exp, 'is: ', num)
print('The sum of its digits is: ', digit_sum)

k = input('Any key to exit')
