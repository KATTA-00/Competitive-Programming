t = int(input())

for _ in range(t):
    s = input()
    
    l = []
    letters = ["a", "b", "c", "d", "e", "f", "g"]
    
    for i in letters:
        l.append(s.count(i))
        
    m = max(l)
    
    print(letters[l.index(m)].upper())
    