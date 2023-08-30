class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letter = {
            "2":"abc",
            "3": "def",
            "4": "ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        n = len(digits)
        answer = []
        def sol(index, curr):
            if index == n:
                answer.append(curr)
                return
            
            
            for lett in letter[digits[index]]:
                sol(index + 1, curr + lett)
        
        sol(0, "")
                
        return answer