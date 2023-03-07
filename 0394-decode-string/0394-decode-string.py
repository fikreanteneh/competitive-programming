class Solution:
    def decodeString(self, s: str) -> str:
            
        p = ["1","[",""]
        p.extend(list(s))
        p.append("]")
        return self.solution(p, 0, [])[0]
        
    def solution(self, s, right, temp):
        left = right
        
        while right < len(s):
            
            while s[right].isnumeric():
                right += 1
                
            temp.append(int("".join(s[left:right])))
            right += 1
            left = right

            while right < len(s) and s[right] != "]":
                middle = s[right]

                if s[right].isnumeric():
                    middle, right = self.solution(s, right, [])

                temp.append(middle)
                right += 1
                
            string = ("".join(temp[1:])) * (temp[0])
            return (string,right)