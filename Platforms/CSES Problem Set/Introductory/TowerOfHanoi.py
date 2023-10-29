def tower_of_hanoi(n, source, auxiliary, target, moves=[]):
    if n == 1:
        moves.append((source, target))
        return moves
    moves = tower_of_hanoi(n - 1, source, target, auxiliary, moves)
    moves.append((source, target))
    moves = tower_of_hanoi(n - 1, auxiliary, source, target, moves)
    return moves


n = int(input())
moves = tower_of_hanoi(n, 1, 2,3)

print(len(moves))
for move in moves:
    print(move[0], move[1])


