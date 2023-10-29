R1, C1, R2, C2 = map(int, input().split())

if R2==R1 and C2==C1:
    moves = 0
elif abs(R2 - R1) == abs(C2 - C1):
    
    moves = 1
elif (R1 + C1) % 2 == (R2 + C2) % 2:
    moves = 2
else:
    moves = -1

print(moves)