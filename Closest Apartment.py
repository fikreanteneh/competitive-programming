def find(blocks, reqs):
    answer = [float("-inf")] * len(blocks)
    for req in reqs:
        ans = [2*len(blocks) + 2] * len(blocks)
        mini = float("-inf")
        for i, block in enumerate(blocks):
            if block[req]: mini = i
            ans[i] = i - mini
        mini = float("inf")
        print(ans)
        for i in range(len(blocks)-1,-1,-1):
            block = blocks[i]
            if block[req]: mini = i
            ans[i] = min(ans[i], mini-i)
        print(ans)
        for i, closest in enumerate(ans): answer[i] = max(answer[i], ans[i])
    a = (float("inf"), -1)
    for i, ans in enumerate(answer):
        if ans < a[0] : a = (ans, i)
    return a[1]
print(find([
        {
            "gym": False,
            "school": True,
            "store": False
        },
        {
            "gym": True,
            "school": False,
            "store": False
        },
        {
            "gym": True,
            "school": True,
            "store": False
        },
        {
            "gym": False,
            "school": True,
            "store": False
        },
        {
            "gym": False,
            "school": True,
            "store": True
        }
    ], ["gym","school","store"]))
