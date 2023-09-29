# def countDivisors(N):
#     divisors = [0]*(N+1)

#     for i in range(1,N+1):
#         for j in range(i,N+1,i):
#             divisors[j]+=1

#     return divisors
# t = int(input())
# inputList = []
# for i in range(t):
#     inputList.append(int(input()))

# divisors = countDivisors(max(inputList))

# for i in range(t):
#     print(divisors[inputList[i]])


def countDiv(n):
    count = 2

    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            count += 2

    if n**(1/2)%1 == 0:
        count -= 1

    return count

n = int(input())

for i in range(n):
    x = int(input())
    print(countDiv(x))