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


    
# and grid[start_x+1][start_y] >= grid[start_x][start_y+1] 
print(count)