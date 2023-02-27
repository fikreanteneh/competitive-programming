t = int(input())
for test in range(t):
    n, iteration = list(map(int, input().split(" ")))
    soldiers = list(map(int, input()))

    for j in range(iteration):
        before = soldiers[:]
        for i in range(n):
            if i == 0 and soldiers[i]==0:
                if  soldiers[i + 1] == 1:
                    before[i] = 1
                continue
            if i == len(soldiers) - 1:
                if soldiers[i - 1] == 1:
                    before[i] = 1
                continue
            if soldiers[i] == 0 and ((soldiers[i-1] == 1 and soldiers[i+1] != 1) or (soldiers[i+1] == 1 and soldiers[i-1] != 1)):
                before[i] = 1
        if before == soldiers:
            break
        else:
            soldiers = before
    
    print(''.join(map(str, soldiers)))



    # last = soldiers.copy()
    # for i in range(iteration):
    #     stack = [False]
    #     last = soldiers.copy()
    #     print(last)
    #     for j in soldiers:
    #         if j == "1":
    #             if stack[-1] == 0 and stack[-2] != "1":
    #                 stack.pop()
    #                 stack.append("1")
    #                 stack.append("1")
    #             else:
    #                 stack.append("1")
    #         elif j == "0":
    #             if stack[-1] == "1":
    #                 stack.append("1")
    #             else:
    #                  stack.append("0")
    #     soldiers = stack[1:]
    #     print(soldiers)
    #     if soldiers == soldiers:
    #         break







    # soldiers = list(input())
    # print(soldiers)
    # indexes = [-2]
    # for j, k in enumerate(soldiers):
    #     if k == "1":
    #         indexes.append(j)
    # indexes.append(n)
    # print("----",indexes)
    # ans = []
    # for i in range(1, n+1):
    #     print(indexes[i] - 1, indexes[i-1]+1)
    #     count = 0
    #     for j in range(indexes[i]-1,indexes[i-1] + 1, -1):
    #         print(j)  
    #         ans.append(j)
    #         count += 1

    #     print("rr")
    # print(ans)
    