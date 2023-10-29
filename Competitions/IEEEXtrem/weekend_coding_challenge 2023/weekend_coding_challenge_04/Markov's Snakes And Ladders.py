import random

t = int(input())

for _ in range(t):
    prob = list(map(float, input().strip().split(",")))
    
    l, n =  list(map(float, input().strip().split(",")))
    
    laders = [ list(map(int, x.strip().split(","))) for x in input().strip().split(" ")]
    la = {x[0]:x[1] for x in laders}
        
    snakes = [ list(map(int, x.strip().split(","))) for x in input().strip().split(" ")]
    sn = {x[0]:x[1] for x in snakes}
    
    tot = 0
    totC = 0
    for q in range(5000):
        s = 1
        c = 0
        
        for p in range(1000):
            m = random.uniform(0,1)
            move = 0
            if m < prob[0]:
                move = 1
            elif m < prob[0]+prob[1]:
                move = 2
            elif m < prob[0]+prob[1]+prob[2]:
                move = 3
            elif m < prob[0]+prob[1]+prob[2]+prob[3]:
                move = 4
            elif m < prob[0]+prob[1]+prob[2]+prob[3]+prob[4]:
                move = 5
            else:
                move = 6
                
            if s+move <= 100:
                s += move
                if s in la:
                    s = la[s]
                elif s in sn:
                    s = sn[s]
            c += 1
            if s == 100:
                totC += 1
                tot += c
                break
            
    print(round(tot/totC))
                