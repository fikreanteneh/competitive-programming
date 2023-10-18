class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        store =[defaultdict(int),defaultdict(int)]
        store[0][-1] = 0
        store[1][-2] = 0
        for i, val in enumerate(nums):
            store[i%2][val] += 1
        def calc(store):
            nums = [(-1, 0), (-2, 0)]
            for num, repeated in store.items():
                if repeated > nums[1][1]:
                    nums[0] = nums[1]
                    nums[1] = (num, repeated)
                elif repeated > nums[0][1]:
                    nums[0] = (num, repeated)
            return nums
        n = len(nums)
        x = calc(store[0])
        y = calc(store[1])
        if x[1][0] != y[1][0]:
            return n - x[1][1] - y[1][1]
        return min ( n - x[1][1] - y[0][1],  n - x[0][1] - y[1][1])
            