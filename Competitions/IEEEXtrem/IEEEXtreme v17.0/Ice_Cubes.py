T = int(input())
for t in range(T):
    N, M, K, B = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]  # Corrected this line
    
    