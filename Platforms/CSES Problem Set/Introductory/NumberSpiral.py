def NumberSpiralPoint(row,col):
    if row==col:
        print(row*(col-1)+1)
        return

    if col>row:
        if col%2 == 0:
            print((col-1)**2 + row)
            return
        else:
            print(col**2-row+1)
            return
        
    else:
        if row%2 ==0:
            print(row**2-col+1)
            return
        else:
            print((row-1)**2 + col)
            return

n = int(input().strip())

for i in range(n):
    row, col = map(int,input().split())
    NumberSpiralPoint(row,col)

    



