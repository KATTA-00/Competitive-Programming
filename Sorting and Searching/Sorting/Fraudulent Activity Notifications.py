import bisect

def getMedian2(v):
    n = len(v)
    m = n // 2
    m -= 1
    if n % 2 == 1:
        return v[m + 1] * 2
    else:
        return v[m] + v[m + 1]

def activityNotifications(expenditure, d):
    n = len(expenditure)
    
    if d == n:
        return 0
    
    pass_window = expenditure[:d]
    pass_window.sort()
    
    ret = 0
    
    for i in range(d, n):
        if expenditure[i] >= getMedian2(pass_window):
            ret += 1
        
        # Update pass_window with binary search
        left_index = bisect.bisect_left(pass_window, expenditure[i])
        pass_window.insert(left_index, expenditure[i])
        
        remove_index = bisect.bisect_left(pass_window, expenditure[i - d])
        pass_window.pop(remove_index)
    
    return ret
   
n,d = map(int,input().split())
expenditure = list(map(int, input().rstrip().split()))

result = activityNotifications(expenditure, d)
print(result)