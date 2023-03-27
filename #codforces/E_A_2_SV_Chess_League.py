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


def merge(que, diff):
    players = deque([])

    for i, val in enumerate(que):
        players.append((val, val))

    while len(players) > 1:
        print(players)
        mini1, maxi1 = players.popleft()
        mini2, maxi2 = players.popleft()
        matches = { (maxi1, mini2): abs(maxi1 - mini2), (maxi1, maxi2): abs(maxi1 - maxi2), (mini1, mini2) : abs(mini1 - mini2), (mini1, maxi2): abs(mini1 - maxi2)} 
        temp = []
        for rate, difference in matches.items():
            if difference > diff:
                temp.append(max(rate))
            else:
                temp.append(rate[0])
                temp.append( rate[1])
        players.append((min(temp), max(temp)))
    left, right = players[0]
    ans = []
    for i, val  in enumerate(que):
        if left <= val <= right:
            ans.append( i+ 1)
    return ans


n,  maxi = LI()
rating = LI()
print(*merge(rating, maxi))
