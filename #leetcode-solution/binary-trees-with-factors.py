class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        store = {val: 1 for val in arr}
        arr.sort()
        n = len(arr)
        for i in range(n):
            curr = arr[i]
            for j in range(i):
                target = curr / arr[j]
                count1 = store.get(arr[j], 0)
                count2 = store.get(target, 0)
                store[curr] += (count1*count2)
        return sum(store.values()) % (10**9 + 7)