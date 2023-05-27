class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        available = defaultdict(int)
        for i, val in enumerate(bills):
            available[val] += 1
            if val == 10:
                if available[5] < 1:
                    return False
                available[5] -= 1
            elif val == 20:
                if available[10] and available[5]:
                    available[5] -= 1
                    available[10] -= 1
                    continue
                elif available[5] >= 3:
                    available[5] -= 3
                    continue
                return False

        return True
            
            
        