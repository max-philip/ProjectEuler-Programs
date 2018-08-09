file = open("p022_names.txt", "r")
for i in file:
    names = i.split(",")
    names.sort()

file.close()


def alpha_score(x):
    if x == 'A':
        return 1
    if x == 'B':
        return 2
    if x == 'C':
        return 3
    if x == 'D':
        return 4
    if x == 'E':
        return 5
    if x == 'F':
        return 6
    if x == 'G':
        return 7
    if x == 'H':
        return 8
    if x == 'I':
        return 9
    if x == 'J':
        return 10
    if x == 'K':
        return 11
    if x == 'L':
        return 12
    if x == 'M':
        return 13
    if x == 'N':
        return 14
    if x == 'O':
        return 15
    if x == 'P':
        return 16
    if x == 'Q':
        return 17
    if x == 'R':
        return 18
    if x == 'S':
        return 19
    if x == 'T':
        return 20
    if x == 'U':
        return 21
    if x == 'V':
        return 22
    if x == 'W':
        return 23
    if x == 'X':
        return 24
    if x == 'Y':
        return 25
    if x == 'Z':
        return 26
    return 0

loc = 0
total_namescore = 0
    
for name in names:
    loc += 1
    curr_alpha = 0

    for i in range(1, len(name)-1):
        curr_alpha += alpha_score(name[i])

    total_namescore += (loc*curr_alpha)

print("The total name score in the p022_names.txt file =", total_namescore)
        
