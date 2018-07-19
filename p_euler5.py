is_divisible = 0
j = 100

while 1:
    for i in range(1,20):
        if (j%i != 0):
            is_divisible = 0
            break
        else:
            is_divisible = 1
    if is_divisible:
        print(j)
        break
    j+=20

k = input('Press any key to exit')

    
