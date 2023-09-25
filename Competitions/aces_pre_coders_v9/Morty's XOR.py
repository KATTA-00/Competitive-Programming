test = int(input())

for i in range(test):
    
    num = int(input())
    
    number = [int(x) for x in input().strip().split(" ")]
    
    xor  = [0]
    
    for i in range(len(number)):
        xor.append(xor[-1] ^ number[i])
        
    sum = 0
    for i in range(1, num+1):
        for j in range(i+1, num+1):
            sum = sum ^ xor[i-1] ^ xor[j]
            
    for i in number:
        sum = sum ^ i

    print(sum)