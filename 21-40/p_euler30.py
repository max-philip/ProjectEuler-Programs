
def find_suffix(x):


    if len(str(x)) > 1:
        if str(x)[-2] == '1':
            return 'th'
    
    if (str(x)[-1] == '1'):
        return 'st'
    if str(x)[-1] == '2':
        return 'nd'
    if str(x)[-1] == '3':
        return 'rd'
    if (str(x)[-1] == '0') or (str(x)[-1] == '4') or (str(x)[-1] == '6') or (str(x)[-1] == '7') or (str(x)[-1] == '8') or (str(x)[-1] == '9') or (str(x)[-1] == '5'):
        return 'th'
    


power = int(input('Enter a number: '))

suffix = find_suffix(power)

print('\nNumbers that can be written as the sum of the ' + str(power) + suffix + ' powers of their digits:')

tot_sum = 0
for i in range(2, 999999):

    digit_5p = 0
    for j in range(0, len(str(i))):
        digit_5p += int(str(i)[j])**power
        if digit_5p > i:
            break

    if i == digit_5p:
        print(i)
        tot_sum += i

if tot_sum:
    print('\nThe sum of these numbers = ' + str(tot_sum))
else:
    print('\nNONE')

k = input('\nAny key to exit')
    
