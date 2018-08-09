largest_palindrome = 0
curr_pal = 0

for i in range(999):
    for j in range(999):
        curr_pal = i*j
        if (len(str(curr_pal)) == 6):
            if (str(curr_pal)[0] == str(curr_pal)[-1]) & (str(curr_pal)[1] == str(curr_pal)[-2]) & (str(curr_pal)[2] == str(curr_pal)[-3]) & (curr_pal > largest_palindrome):
                largest_palindrome = curr_pal

print('The largest palindrome made from the product of two 3-digit numbers is: ', largest_palindrome)

k = input('Press any key to exit')
