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

def merge(que):
    ans = 0
    # print(que)
    while len(que) > 1:
        mini1, maxi1 = que.popleft()
        mini2, maxi2 = que.popleft()
        if  abs(maxi1 - mini2) > 1 and abs(maxi2 - mini1) > 1:
            return -1
        if mini2 < maxi1 :
            ans += 1
        que.append((min(mini1, mini2), max(maxi1, maxi2)))
        # print(que, ans)
    return ans 


test = I()
for t in range(test):
    n = I()
    nums = LI()
    for i, val in enumerate(nums):
        nums[i] = (val, val)
    nums = deque(nums)
    print(merge(nums))
    
    


