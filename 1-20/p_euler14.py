def even(num):
    num = num / 2
    return num

def odd(num):
    num = 3*num + 1
    return num



max_num = 1000000
chain_len = 0
chain_num = 0
max_chain = 0

for i in range(1, max_num):
    chain_len = 1

    curr_int = i
    while 1:
        if curr_int%2 == 0:
            curr_int = even(curr_int)
            chain_len += 1
        elif curr_int == 1:
            break
        else:
            curr_int = odd(curr_int)
            chain_len += 1
        

    if chain_len > max_chain:
        max_chain = chain_len
        chain_num = i

print(chain_num)
