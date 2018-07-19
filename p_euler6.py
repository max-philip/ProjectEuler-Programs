sum_of_sq = 0
sq_of_sum = 0
sum1 = 0

for i in range(1,101):
    sum_of_sq += i*i

for j in range(1,101):
    sum1 += j

sq_of_sum = sum1*sum1
print(sq_of_sum - sum_of_sq)

k = input('Press any key to exit')
