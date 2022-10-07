def gg(nums, k):
    sum = 0
    res = []
    cache = {0:[-1]}
    for j, i in enumerate(nums):
        sum += i
        if sum - k in cache:
            for l in cache[sum-k]:
                res.append(nums[l+1: j+1])0
        print(sum, i)
        if sum in cache:
            cache[sum].append(j)
        else: cache[sum] = [j]
    print(cache)
    return res
