class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        sums = skill[0] + skill[-1]
        n = len(skill) - 1
        for i in range((n+1)//2):
            sk = skill[i] + skill[n-i]
            if sk != sums:
                return -1
            chemistry += (skill[i] * skill[n-i])
        return chemistry