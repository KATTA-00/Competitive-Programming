
n = int(input())

for j in range(n):
    index = int(input())
    sum = 0
    num = 1
    while True:
        sum = sum + 9*num*pow(10,num-1) # 9 1∑n x * 10**(x-1)
        if index<=sum:
            break
        num += 1

    #Digits away
    away = (sum - index)//num
    remainder = (sum - index)%num

    #Calculating number
    number = (pow(10,num)-1) - away
    numStr = str(number)
    print(numStr[- 1 - remainder])

    # 1 -9 >>>>>> 1 -----> 9
    # 10 - 99 >>>>> 2 ----------> 90x2=180
    # 100 - 999 >>>>> 3 ------------------> 900x3=2700


    # 2889 - 2870
