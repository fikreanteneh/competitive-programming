class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
        curr = 0
        # curr is the size string as we go
        for i, val in enumerate(s):
            # if is a char we increase by one else multiply by the num
            # This would give us the string size at that index when decoded
            #  l e e t 2 c o  d  e  3    >>  
            #  1 2 3 4 8 9 10 11 12 36
            if val.isnumeric() : 
                curr *= int(val)
            else:
                curr += 1
            # If k curr passe k that means we can find the kth index upto that point 
            # and the rest is useless
            if curr >= k: 
                break
        # Now we go in the reverse direction to find the kth
        for j in range(i, -1, -1):
            # curr == k it mean we can just return the index sinc K %= curr == 0
            # since the string is repeated we need to k can be relative to curr/s[i]
            # leetleetcodeleetleetcodeleetleetcode 15th
            # in the 1st iteration
            #   k = 15 curr = 36
            #   k = k % curr = 10   curr //3 = 12
            #   this like removing the 2 reapeated leetleetcode
            #   and assuming only one leetleetcode but k should be relative to that 
            #   finding 15th k in ength 36 is same as finding 3rd in leetleetcode 
            #   so when we pass by char we decrease size by one else do integer division
            # in the 2nd 
            #   k = 15 % 12 = 3  curr = 11
            # continus until it reach 2 so by that time k = 3 curr = 8
            #  now it the same us the above we are trying to find 3rd from leetleet
            k %= curr
            if k == 0 and not s[j].isnumeric():
                return s[j]
            
            # curr == 36 which is way bigger than 10 so we have to go back k = 36 curr//s[i] = 12
            if s[j].isnumeric():
                curr //= int(s[j])
            else:
                curr -= 1

        
            
                    
        
                
            
            
            