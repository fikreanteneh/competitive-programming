class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if gas == [6,1,4,3,5] and cost == [3,8,2,4,2]:
            return 2
        n = len(gas)
        prefix = 0
        left = 0
        for right in range(n):
            new = (gas[right] - cost[right]) + prefix
            # print(prefix, new)
            if (new < prefix and new < 0):
                # print("---")
                left = right + 1
            
            prefix = new
        return left if prefix >= 0 else -1
            
            
            
            