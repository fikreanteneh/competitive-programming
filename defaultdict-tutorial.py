# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n = list(map(int, input().split(" ")))
setA = defaultdict(list)

for i in range(n[0]):
    word = input()
    setA[word].append(str(i + 1))
for i in range(n[1]):
    word = input()
    if not setA[word]:
        print("-1")
    else:
        print(" ".join(setA[word]))

