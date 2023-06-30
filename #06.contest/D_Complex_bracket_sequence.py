bracket = input()
l, r = 0, len(bracket)-1
ans = []
while l < r:
    while l < r and bracket[l] == ")":
        l += 1
    while l < r and bracket[r] == "(":
        r -= 1
    if l < r:
        ans.append(l + 1)
        ans.append(r + 1)
    l += 1
    r -= 1


ans.sort()

if (len(ans) > 0):
    print(1)
    print(len(ans))
    print(*ans)
else:
    print(0)
