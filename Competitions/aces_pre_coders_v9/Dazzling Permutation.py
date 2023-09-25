num = int(input())

numbers = [int(x) for x in input().strip().split(" ")]

first = numbers.index(1)

n = 1
while True:
    if first+n >= num or numbers[first+n] != n + 1:
        break
    n+=1
    
c = numbers.copy()
numbers.sort()

print(numbers)
print(c)
l = []
count = 0
p = 0
while c != numbers:
    
    if numbers[count] == c[count]:
        l.append(p)
        p = 0
        count+=1
        continue
    
    if numbers[count] != c[count]:
        index = c.index(numbers[count])
        temp = c[count]
        c[count] = c[index]
        c[index] = temp
        p+=index - count
        
    count+=1
    
    print(l, p)
    
    
print(count)
print(l)
