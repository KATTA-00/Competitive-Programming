# function to find first index >= x
def lowerIndex(arr, n, x):
  l = 0
  h = n-1
  while (l <= h):
    mid = int((l + h)//2)
    if (arr[mid] >= x):
      h = mid - 1
    else:
      l = mid + 1
  return l
 
 
# function to find last index <= x
def upperIndex(arr, n, x):
  l = 0
  h = n-1
  while (l <= h):
    mid = int((l + h)//2)
    if (arr[mid] <= x):
      l = mid + 1
    else:
      h = mid - 1
  return h
 
 
# function to count elements within given range
def countInRange(arr, n, x, y):
  # initialize result
  count = 0
  count = upperIndex(arr, n, y) - lowerIndex(arr, n, x) + 1
  return count
 

num, q = [int(x) for x in input().strip().split(' ')]
arr = [int(x) for x in input().strip().split(' ')]
sorted_arr = sorted(arr)

for _ in range(q):
    t, a, b = [x for x in input().strip().split(' ')]

    if t == "!":
      arr[int(a) - 1] = int(b)
    else:
      sorted_arr = sorted(arr)
      print(countInRange(sorted_arr, num, int(a), int(b)))




