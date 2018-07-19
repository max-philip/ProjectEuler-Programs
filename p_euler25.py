a = 1
b = 1
c = 0

index = 2

max_digits = int(input('Enter a number: '))

while 1:
    c = a + b
    index += 1
    if len(str(c)) >= max_digits:
        print('The first term in the Fibonacci sequence to contain ' + str(max_digits) + ' digits is ' + str(c))
        print('It has an index of ' + str(index))
        break
  
    a = b + c
    index += 1
    if len(str(a)) >= max_digits:
        print('The first term in the Fibonacci sequence to contain ' + str(max_digits) + ' digits is ' + str(a))
        print('It has an index of ' + str(index))
        break
    
    b = a + c
    index += 1
    if len(str(b)) >= max_digits:
        print('The first term in the Fibonacci sequence to contain ' + str(max_digits) + ' digits is ' + str(b))
        print('It has an index of ' + str(index))
        break


k = input('Any key to exit')
