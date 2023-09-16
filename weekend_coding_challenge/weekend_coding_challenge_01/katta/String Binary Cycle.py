s = input()

decimal = int(s, 2)  # Convert binary string to decimal
max_power = 1  # Initialize max_power to 1

# Check if decimal is divisible by 2 after cyclic shifts
for shift in range(0, len(s)):
    s = s[-1] + s[:-1]  # Perform a cyclic shift
    decimal = int(s, 2)  # Convert the shifted binary string to decimal

    if decimal % 2 == 0:
        max_power = max(max_power, shift+1)

if max_power == 1:
    print("0")  # X can be divisible with arbitrarily large power
else:
    print(max_power-1)
