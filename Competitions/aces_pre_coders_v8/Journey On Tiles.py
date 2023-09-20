row = int(input())

grid = []

for i in range(row):
    data = [int(x) for x in input().strip().split(" ")]
    grid.append(data)
    
def isValid(x, y):
    if x >= row:
        return False
    elif y >= row:
        return False
    return True

start_x = 0
start_y = 0
count = 0
while not (start_x == row -1 and start_y == row -1):
    print(start_x, start_y)
    if isValid(start_x+1, start_y) :
        if isValid(start_x, start_y+1):
            if grid[start_x+1][start_y] >= grid[start_x][start_y+1]:
                start_x = start_x + 1
                start_y = start_y
                count += grid[start_x][start_y]
            else:
                start_x = start_x 
                start_y = start_y+1
                count += grid[start_x][start_y+1]
        else:
            start_x = start_x + 1
            start_y = start_y
            count += grid[start_x][start_y]
    else:
        start_x = start_x 
        start_y = start_y + 1
        count += grid[start_x][start_y]
    
# and grid[start_x+1][start_y] >= grid[start_x][start_y+1] 
print(count)