class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        maxi, mini = float("-inf"), float("inf")
        sums = 0
        for i in salary: 
            sums += i
            maxi = max(maxi, i)
            mini = min(mini, i)
        sums -= (maxi + mini)
        return sums / (n - 2)
        