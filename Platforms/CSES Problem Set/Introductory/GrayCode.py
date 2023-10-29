# Read the number of bits for the Gray code from the user
n = int(input())

# Iterate through all integers from 0 to 2^n - 1
for i in range(1 << n):
    # Calculate the Gray code value for the current integer 'i'
     # Gray codes are generated using bitwise XOR (^) between current integer 'i' and its right shift by 1 (i >> 1)
    val = (i ^ (i >> 1))
    
    # Convert the Gray code value to a binary string and remove the '0b' prefix
    s = bin(val)[2::]
    
    # Print the Gray code with leading zeros to make it 'n' bits long
    print(s.zfill(n), end="\n")
