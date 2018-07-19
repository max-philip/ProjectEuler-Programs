
max_num = int(input('Enter a number: '))

psum = 0

for i in range(1, max_num+1):
    psum += i**i

print('The self power series of ' + str(max_num) + ' =')
print(psum)
    
k = input('\nAny key to exit')
