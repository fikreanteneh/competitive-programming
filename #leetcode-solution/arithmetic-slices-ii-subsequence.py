class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # answer = 0
        # store = [defaultdict(lambda: [1]) for _ in range(len(nums))]
        # for i, nums1 in enumerate(nums):
        #     for j in range(i - 1, -1, -1):
        #         nums2 = nums[j]
        #         diff = nums1 - nums2
        #         for index in store[j][diff]:
        #             store[i][diff].append(index + 1)
        #             if index >= 2:
        #                 answer += 1
        # return answer
        answer = 0
        store = [defaultdict(int) for _ in range(len(nums))]
        for i, nums1 in enumerate(nums):
            for j in range(i - 1, -1, -1):
                nums2 = nums[j]
                diff = nums1 - nums2
                answer += store[j][diff]
                store[i][diff] += (1 + store[j][diff])
        return answer
