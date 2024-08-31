class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)

        @cache
        def dp(index, differ):
            
            if index == n:
                if differ == 0:
                    return 0
                return -inf

            option1 = rods[index] + dp(index + 1, differ + rods[index] )
            option2 = dp(index + 1,  differ - rods[index] )
            option3 = dp(index + 1, differ)
            return max(option1, option2, option3)       

        return dp(0, 0)