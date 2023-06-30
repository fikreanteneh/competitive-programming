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
 
# test = I()
# ans = 0
# modulo = 2**32 - 1
# curr = 1
# stack = []
# flag = False
# for i in range(test):
#     j = LS()
#     if j[0] == "add":
#         ans += curr
#     elif j[0] == "for":
#         curr *= (int(j[1]))
#         stack.append(int(j[1]))
#     else:
#         curr //= stack.pop()
    # if ans > modulo:
    #     break
# if ans > modulo:
#     print("OVERFLOW!!!")
# else:
#     print(ans)

from sys import stdin

n = int(input())
stack = [[1, 0]]

for _ in range(n):
    command = stdin.readline().strip()

    if command == "add":
        stack[-1][1] += 1
    elif command == "end":
        iterations, add = stack.pop()
        stack[-1][1] += iterations * add
    else:
        t, iterations = command.split()
        stack.append([int(iterations), 0])

if stack[-1][1] > (2**32 - 1):
    print("OVERFLOW!!!")
else:
    print(stack[-1][1])