class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # a - 0, e- 1, i - 2, o - 3 u - 4
        rules = [ [1], [0, 2], [0,1,3,4], [2, 4], [0] ]
        store = [1,1,1,1,1]
        MOD = 10**9 + 7
        for _ in range(1, n):
            nextt = [0,0,0,0,0]
            for curr in range(5):
                for i, rule in enumerate(rules):
                    if curr in rule:
                        nextt[curr] += store[i]
                        nextt[curr] %= MOD
            store = nextt
        return sum(store)%MOD