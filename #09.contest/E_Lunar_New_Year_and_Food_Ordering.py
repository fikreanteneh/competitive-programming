n = list(map(int, input().split(" ")))
dish = list(map(int, input().split(" ")))
cost = list(map(int, input().split(" ")))
new = []
total = sum(dish)
for i, costt in enumerate(cost):
    new.append((costt, i))
new.sort()
new.reverse()
for i in range(n[1]):
    ans = 0
    customer = list(map(int, input().split(" ")))
    kind, quantity = customer[0], customer[1]
    new.append((cost[kind-1], kind-1))
    if total == 0:
        print(ans)
        continue
    j = 0

    while quantity > 0 and new:
        index = new[-1][1]
        costD = cost[index]
        typeD = dish[index]
        if typeD == 0:
            j += 1
            new.pop()
            continue
        elif quantity <= typeD:
            ans += (costD * quantity)
            total -= quantity
            dish[index] -= quantity
            quantity = 0
        else:
            quantity -= typeD
            total -= typeD
            ans += (costD * typeD)
            dish[index] = 0
        if typeD <= quantity or j == 0:
            new.pop()
        j += 1

    if quantity != 0:
        print(0)
    else:
        print(ans)
