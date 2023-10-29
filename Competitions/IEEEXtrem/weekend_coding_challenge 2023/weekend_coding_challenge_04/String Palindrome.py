# Manacher's Algorithm

def lengths(S):
    N = len(S)
    S = S + S  
    
    def manacher(s):
        s = '#' + '#'.join(s) + '#'
        N = len(s)
        P = [0] * N
        C, R = 0, 0
        
        for i in range(N):
            if i < R:
                mirror = 2 * C - i
                P[i] = min(R - i, P[mirror])
            
           
            a, b = i + (1 + P[i]), i - (1 + P[i])
            while a < N and b >= 0 and s[a] == s[b]:
                P[i] += 1
                a += 1
                b -= 1
            
            
            if i + P[i] > R:
                C, R = i, i + P[i]
        
        return P
    
    max_lengths = []
    for k in range(N):
        rotated_S = S[k:k+N] 
        P = manacher(rotated_S)
        max_len = max(P)
        max_lengths.append(max_len)
    
    return max_lengths


N = int(input())
S = input()

max_lengths = lengths(S)
for length in max_lengths:
    print(length)
