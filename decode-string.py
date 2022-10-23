class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        for j in range(len(s)):
            letter = s[j]
            if letter == "[":
                stack.append(s[i:j])
                i = j + 1
            elif letter == "]":
                stack.append(s[i:j])
                i = j + 1
                string = ""
                while not stack[-1].isnumeric():
                    string = stack.pop() + string
                string = string * int(stack.pop())
                stack.append(string)
            if letter.isnumeric() and 97 <= ord(s[j-1]) <= 122:
                stack.append(s[i:j])
                i = j
        stack.append(s[i:j +1])
        return "".join(stack)
        
        
        
        "a2"
        """
        [3,a,cc]
        [accaccacc]
        
        
        answer = ""
        i = 0
        
        [[[acccc]]]
        1,0,0
        num = int(s[i:j]) >>  i >>j
        string = s[i:j+1]
        answer += string* num  >> 
        """
        """answer = ""
        i = 0
        300
        num = 1
        string = ""
        for j in range(len(s)):
            if s[j] == "[":
                if i == j: num = 1
                else: num = s[i:j]
                i = j + 1
            elif s[j] == "]":
                string = s[i:j]
                i = j + 1
                answer += (string * num)
        return answer"""
        #parent = {"[", "]"} 
        
        """
        stack = [3,"a","cc"]
         "c" * 2cc
         ["aaa", 2,"bc"]
         aaa  bcbc
         "100"
         
        """
         
        
        
        
        
    
