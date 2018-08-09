max_num = int(input('Enter a number: '))

curr_total = 1

for i in range(max_num, 0, -1):
    curr_total *= i

digits = str(curr_total)
digit_sum = 0

for j in range(0, len(digits)):
    digit_sum += int(digits[j])

print(str(max_num) + '! =', digits)
print('The sum of the digits of ' + digits + ' is ' + str(digit_sum))

k = input('Any key to exit')
