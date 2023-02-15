class Solution:
    def isHappy(self, n: int) -> bool:
        check = {n}
        while n != 1:
            n = list(map(int, list(str(n))))
            n = [i ** 2 for i in n]
            n = sum(n)
            if n in check:
                return False
            check.add(n)
        return True
            