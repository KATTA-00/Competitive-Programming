a, b = map(int, input().strip().split(" "))
countArr = [0] * (b - a + 1)
eightnumb = [89, 145, 42, 20, 4, 16, 37, 58]

for i in range(a, b ):
    if a == 1:
        countArr[0] = 1

    if countArr[i - a] != 1:
        numseq = []
        s = 0
        n = i

        while s != 1 and s!=4:
            s = 0
            numseq.append(n)

            while n != 0:
                s = s + (n % 10) ** 2
                n = n//10

            n = s

        if s == 1:
            for num in numseq:
                if num >= a and num <= b:
                    countArr[num - a] = 1



print(sum(countArr))
