# Got full marks for this snippet:

from collections import deque

n = int(input())
rumor_heard = deque()
not_rumor_source = {}

rumor_spread_graph = {}

for i in range(n):
    person1, relation, person2 = map(str, input().split())
    
    if person1 not in not_rumor_source:
        not_rumor_source[person1] = True
    if person2 not in not_rumor_source:
        not_rumor_source[person2]  = True

    if person1 not in rumor_spread_graph:
        rumor_spread_graph[person1] = []
    if person2 not in rumor_spread_graph:
        rumor_spread_graph[person2] = []
   
    if relation == "??":
        rumor_spread_graph[person1].append(person2)
        rumor_spread_graph[person2].append(person1)
    else:
        not_rumor_source[person2] = False
        rumor_heard.append(person2)

rumor_sources = []
while rumor_heard:
    rumor_hearer = rumor_heard.popleft()
    for spreader in rumor_spread_graph[rumor_hearer]:
        rumor_spread_graph[spreader].remove(rumor_hearer)
        not_rumor_source[spreader] = False
        rumor_heard.append(spreader)

for person in not_rumor_source:
    if not_rumor_source[person]:
        rumor_sources.append(person)

rumor_sources.sort()
for source in rumor_sources:
    print(source)