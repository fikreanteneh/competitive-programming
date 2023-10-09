class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        prefix = 0
        left = 0
        for right in range(n):
            prefix += (gas[right] - cost[right])
            if (prefix < 0):
                left = right + 1
                prefix = 0
        return left if sum(gas)>= sum(cost) else -1
            
            
            
            