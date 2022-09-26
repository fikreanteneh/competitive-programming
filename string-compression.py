class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        i = 1
        chars.insert(len(chars), None)
        while i < len(chars):
            if chars[i - 1] == chars[i]:
                count+=1
                del chars[i]
                continue
            elif count > 1:
                c = 1
                while count >= 10:
                    chars.insert(i,str(count%10))
                    count, c = count//10, c+1
                chars.insert(i,str(count))
                count = 1
                i+= c
            i+=1
        chars.pop()
        return len(chars)
