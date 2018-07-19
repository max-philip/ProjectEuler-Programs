champ = "0."

for i in range(1, 1000001):
    champ += str(i)

exp = 1

for i in range(1,len(champ)):
    if i == 2:
        exp *= int(champ[i])

    if i == 11:
        exp *= int(champ[i])

    if i == 101:
        exp *= int(champ[i])

    if i == 1001:
        exp *= int(champ[i])

    if i == 10001:
        exp *= int(champ[i])

    if i == 100001:
        exp *= int(champ[i])

    if i == 1000001:
        exp *= int(champ[i])

print("Expression =", exp)

k = input('Any key to exit')
