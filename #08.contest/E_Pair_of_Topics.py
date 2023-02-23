n = int(input())
num1 = list(map(int, input().split(" ")))
num2 = list(map(int, input().split(" ")))

new = []
for i in range(n):
    new.append(num1[i] - num2[i])

new.sort()
ans = 0
# print(new)
i, j = 0, n - 1
while i >= j:
    while j < i and new[j] + new[i] <= 0:
        j += 1

    ans += max(i - j, 0)
    i -= 1

print(ans)


# x = [None] * 3
# x[0] = 0
# for j, i in enumerate(new):
#     if i[0] == 0 and x[1] is None:
#         x[1] = j
#     if i[0] > 0 and x[2] is None:
#         x[2] = j
#         break
# # ans += ( (x[2] - x[1]) * (n - x[2]) )
# # for i in range(x[2]-1, -1, -1):
# #     ans += i
# i, j = 0, x[2]
# # print(new)
# # print(x)
# while i < x[1] and j < n:
#     if abs(new[i][0]) < abs(new[j][0]):
#         ans += (n - j)
#         i += 1
#         j -= 1
#     j += 1
# print(ans)
