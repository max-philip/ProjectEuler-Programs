

largest_sum = 0
large_a = 0
large_b = 0

for a in range(1, 100):
    for b in range(1, 100):

        num = a**b

        digit_sum = 0

        for i in range(0, len(str(num))):
            digit_sum += int(str(num)[i])

        if digit_sum > largest_sum:
            largest_sum = digit_sum
            large_a = a
            large_b = b


print(largest_sum, large_a, large_b)

k = input('Any key to exit')
