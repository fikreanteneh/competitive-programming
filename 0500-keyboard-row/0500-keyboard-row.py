class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        n1 = set(list("qwertyuiop"))
        n2 = set(list("asdfghjkl"))
        n3 = set(list("zxcvbnm"))
        def check(x, n):
            for i in x:
                if i.lower() not in n:
                    return False
            return True
        ans = []
        for i in words:
            x = set(list(i))
            if check(x,n1) or check(x,n2)  or check(x,n3) :
                ans.append(i)
        return ans
        