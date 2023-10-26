from collections import deque


def cost(r,b):
  dx = b[0]-r[0]
  dy = b[1]-r[1]
  return dx*dx+dy*dy

def check(limit):
  rtob = {r: [b for b in range(m) if c[r][b] <= limit] for r in range(n)}
  btor = {b: [r for r in range(m) if c[r][b] <= limit] for b in range(m)}
  assd_r = {}
  assd_b = {}
  assd = 0
  arb = False
  assdnow = True
  while assdnow:
    
    assdnow = False
    for r in range(n):
      if r not in assd_r:
        paths = deque() 
        visited_r = set()
        visited_r.add(r)
        for b in reversed(rtob[r]):
          paths.append([(r,b)])
        while paths:
          path = paths.pop()
          rc, b = path[-1] 
          
          if b not in assd_b:
            
            
            for rc, b in path:
              assd_r[rc] = b
              assd_b[b] = rc
            assd += 1
            if assd >= k:
              
              return True
            assdnow = True
            break
          else:
            
            rc = assd_b[b]
            if rc not in visited_r:
              visited_r.add(rc)
              for bc in reversed(rtob[rc]):
                if b != bc:
                  np = path[:]
                  np.append((rc,bc))
                  paths.append(np)
  
  return False

n,m,k = map(int,input().split())
arr1 = [tuple(map(int,input().split())) for _ in range(n)]
arr2 = [tuple(map(int,input().split())) for _ in range(m)]
c = [[cost(r,b) for b in arr2] for r in arr1] 
segs = sorted([c[r][b] for r in range(n) for b in range(m)])

lo = 0
hi = len(segs) - 1
while lo < hi:

  mid = (hi + lo) // 2
  if check(segs[mid]):
    hi = mid
  else:
    lo = mid + 1

print(segs[lo])


