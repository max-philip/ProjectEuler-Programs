

for a in range(1,333):
    bc_sum = 1000 - a

    for b in range(a, 1000):
        c = bc_sum - b
        if (a + b + c == 1000) & (a**2 + b**2 == c**2):
            print(a*b*c)
