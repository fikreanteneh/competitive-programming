from collections import defaultdict

n = int(input())
def replace(numbers, string):
    store = defaultdict(list)
    for i, num in enumerate(numbers):
        store[num].append(i)
    for i, lists in store.items():
        check = string[lists[0]]
        for j in lists:
            if string[j]!= check:
                print("NO")
                return
    print("YES")
for k in range(n):
    m = int(input())
    numbers = input().split(" ")
    string = input()
    replace(numbers, string)
