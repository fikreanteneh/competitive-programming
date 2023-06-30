from collections import defaultdict
from collections import Counter

n = int(input())
def cost(n, c, planet):
    planets = dict(Counter(planet))
    cost = 0
    for i,j in planets.items():
        if j >= c:
            cost += c
        else:
            cost += j
    print(cost)
        
for k in range(n):
    nc = input().split(" ")
    planet = list(map(int, input().split(" ")))
    cost(int(nc[0]), int(nc[1]), planet)
