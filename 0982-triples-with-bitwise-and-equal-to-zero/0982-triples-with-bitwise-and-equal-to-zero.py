class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = defaultdict(int)
        for i in range(n):
            for j in range(n):
                count[nums[i]&nums[j]] += 1
        
#         def possibleGen(num):
#             posebible = set()
#             for i in range(16):
            
        answer = 0
        for num in nums:
            for item, repeat in count.items():
                if item & num == 0:
                    answer += repeat
        
        return answer
            