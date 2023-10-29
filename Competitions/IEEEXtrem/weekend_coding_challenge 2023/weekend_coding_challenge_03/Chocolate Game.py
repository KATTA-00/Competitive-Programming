from collections import defaultdict

num = int(input())

def chocolate(arr):

    prefixes = (defaultdict(int), defaultdict(int))
    iter_arr = iter(arr)
    
    loses = 0
    prev = next(iter_arr)
    curr_xor = [prev, 0]
    it = 1
    
    prefixes[0][0] = 1
    prefixes[1][0] = 1
    prefixes[0][prev] = 1
    
    for i in iter_arr:
        curr_xor[it] ^= (i - prev)
        loses += prefixes[it][curr_xor[it]]
        prefixes[it][curr_xor[it]] += 1
        prefixes[it][curr_xor[it] ^ i] += 1
        it = not it
        prev = i
    
    
    return len(arr) * (len(arr) - 1) // 2 - loses


arr = [int(x) for x in input().strip().split(" ")]

print(chocolate(arr))

