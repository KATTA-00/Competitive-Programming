num = int(input())

vowel = ["a", "e", "i", "o", "u"]

for _ in range(num):
    
    s = list(input())
    ss = [x for x in s if x in vowel]
    
    new_s = set(ss)
    
    if len(new_s) == 1:
        print("Easy")
        continue
        
    new_s = sorted(ss)
    
    if new_s == ss:
        print("Easy")
        continue
    ss.reverse()
    if new_s == ss:
        print("Medium")
        continue
    print("Hard")
    
    