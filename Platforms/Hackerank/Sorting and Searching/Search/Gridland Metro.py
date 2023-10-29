def gridlandMetro(n, m, k, track):
    rowDict = {}

    for r, c1, c2 in track:
        rowRanges = rowDict.get(r,[])
        for rRange in rowRanges:
            if c1 <= rRange[1] and c2 >= rRange[0]:
                rRange[0] = min(rRange[0], c1)
                rRange[1] = max(rRange[1], c2)
                break

        else:
            rowRanges.append([c1,c2])

        rowDict[r] = rowRanges

    totalCount = n * m
    for r, rowRanges in rowDict.items():
        for c1, c2 in rowRanges:
            totalCount += c1-c2-1

    return totalCount



n, m, k = map(int, input().rstrip().split())
track = []
for _ in range(k):
    track.append(list(map(int, input().rstrip().split())))

result = gridlandMetro(n, m, k, track)
print(result)