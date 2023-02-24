class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        i = 0
        stack = [""]
        # print(stack, path)
        for i in path:
            # print("iii", i)
            if i == "" or i == ".":
                continue
            elif i == "..":
                if stack[-1]:
                    stack.pop()
            # elif i == ".":
            #     # while stack[-1] != "":
            #     #     stack.pop()
            #     continue
            else:
                stack.append(i)
            # print("---",stack)
        if not stack[-1]:
            stack.append("")
        return "/".join(stack)
        
            
            