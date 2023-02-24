class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sums = ans = 0
        prefix = defaultdict(int)
        prefix[0] += 1
        for num in nums:
            sums += num
            target = sums - k
            ans += prefix[target]
            prefix[sums] += 1
        return ans
                
        