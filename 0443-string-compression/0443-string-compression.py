class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars) + 1
        count = 1
        i = 1
        chars.append(";")
        # print(chars)
        last, index = chars[0], 0
        for i in range(1,n):
            if chars[i] == last:
                count += 1
                chars[i] = ""
            else:
                if count > 1:
                    count =  str(count)
                    k = 0
                    for j in range(index + 1, index + 1 + len(count)):
                        chars[j] = count[k]
                        k += 1
                last, index, count = chars[i], i, 1
        chars.pop()
        i = len(chars) - 1
        while i > 0:
            if chars[i] == "":
                chars.pop(i)
            i -= 1
            
        
        return len(chars)