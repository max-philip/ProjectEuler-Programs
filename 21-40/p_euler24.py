# Problem 24
# Lexicographic Permutations
# Millionth permutation of digits 0,1,2,3,4,5,6,7,8,9


import itertools

perms = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))


for count, perm in enumerate(perms):
    #print(count, perm)
    if (count == 999999):
        print(count, perm)
        out = ''
        for i in perm:
            out += str(i)
        break

print(out)
