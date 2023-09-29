def countValues(n):
     
    # unset_bits keeps track of count of un-set
    # bits in binary representation of n
    unset_bits = 0
     
    while(n):
        if n & 1 == 0:
            unset_bits += 1
        n = n >> 1
         
    # Return 2 ^ unset_bits    
    return 1 << unset_bits

print(countValues(int(input())))