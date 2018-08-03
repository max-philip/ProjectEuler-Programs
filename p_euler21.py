def sum_props(n):
    sum = 0
    for i in range(1, int(n/2)+1):
        if n%i == 0:
            sum += i

    return sum


amics = []
for i in range(1, 10000):
    b = sum_props(i)
    maybe_a = sum_props(b)
    if (maybe_a == i) and (i not in amics) and (i != b):
        print(i)
        amics.append(i)

print("TOTAL:", sum(amics))
