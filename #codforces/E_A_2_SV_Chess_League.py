from collections import deque


def LI():
    return list(map(int, input().split(" ")))
def LS():
    return input().split(" ")
def LC():
    return input().split()
def I():
    return int(input())
def S():
    return input()


n,  maxi = LI()
n = 1 << n
rating = LI()

# def merge(que, diff):
#     players = deque([])
 
#     for i, val in enumerate(que):
#         players.append((val, val))
 
#     while len(players) > 1:
#         mini1, maxi1 = players.popleft()
#         mini2, maxi2 = players.popleft()
#         matches = { (maxi1, mini2): abs(maxi1 - mini2), (maxi1, maxi2): abs(maxi1 - maxi2), (mini1, mini2) : abs(mini1 - mini2), (mini1, maxi2): abs(mini1 - maxi2)} 
#         temp = []
#         for rate, difference in matches.items():
#             if difference > diff:
#                 temp.append(max(rate))
#             else:
#                 temp.append(rate[0])
#                 temp.append( rate[1])
#         players.append((min(temp), max(temp)))
#     left, right = players[0]
#     ans = []
#     for i, val  in enumerate(que):
#         if left <= val <= right:
#             ans.append( i+ 1)
#     return ans
# print(*merge(rating, maxi))


def calculate(first, second):
    ans = []
    l, r = len(first), len(second)
    i, j = 0, 0
    while i < l and j < r:
        if first[i] >= second[j]:
            if first[i] - second[j] <= maxi:
                ans.append(second[j])
            j += 1
        else:
            if second[j] - first[i] <= maxi:
                ans.append(first[i])
            i += 1
    ans.extend(first[i:])
    ans.extend(second[j:])
    # print(ans)
    return ans

def merge(left, right):
    if right - left < 1:
        return [rating[left]]
    mid = left + ((right - left) // 2)
    first = merge(left, mid)
    second = merge(mid + 1, right)
    # print(first, second)
    return calculate(first, second)

all = set(merge(0, n-1))
# print(all)
final = []
for i, val in enumerate(rating):
    if val in all:
        final.append(i + 1)
print(*final)
