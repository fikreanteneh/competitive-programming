# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())

values = [0] * n
for i in range(n): values[i] = input()
words = Counter(values)
print(len(words))
new = []
for i in words.items(): new.append(str((i[1])))
print(" ".join(new))
