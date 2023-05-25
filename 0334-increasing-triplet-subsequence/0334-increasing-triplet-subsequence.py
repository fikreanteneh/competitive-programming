class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x, y = float("inf"), float("inf")
        
        for val in nums:
            if val <= x:
                x = val
            elif val <= y:
                y = val
            elif val > y:
                return True
        return False
                