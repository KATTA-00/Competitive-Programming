n, k = map(int, input().strip().split(' '))
x , y = map(int, input().strip().split(' '))
m = {}

for i in range(k):
    a, b = map(int, input().strip().split(' '))
    m[(a-1,b-1)] = 1

x_walk = [-1, 1, 0 , 0, -1, 1, 1, -1]
y_walk = [0, 0, 1, -1, -1, 1, -1, 1]

def isValid(x, y):
    try:
        if x < 0 or y < 0 or x >= n or y >= n or m[(x,y)] == 1:
            return False
        
        return True
    except:
        return True

count = 0
x = x -1
y = y -1
for i in range(len(x_walk)):

    new_x = x + x_walk[i]
    new_y = y + y_walk[i]
    
    while(isValid(new_x,new_y)):
        count += 1
        new_x = new_x + x_walk[i]
        new_y = new_y + y_walk[i]

print(count)

