class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        if len(arr) >= 2:
            ans += 1
            if arr[1] < arr[0]: flag = "dec"
            elif arr[1] == arr[0]: 
                flag = "any"
                ans -= 1
            else: flag = "inc"
        tot = ans
        for i in range(2, len(arr)):
            #print(flag, arr[i-1], arr[i])
            if (flag == "inc" and arr[i-1] < arr[i]) or (flag == "dec" and arr[i-1] > arr[i]) : 
                #print(11111)
                tot = 1
            elif arr[i-1] == arr[i]:
                tot = 0
                flag = "any"
            elif (flag == "inc" or flag == "any") and arr[i-1] > arr[i]: 
                #print(222)
                flag = "dec"
            else:
                #print(333)
                flag = "inc"
            tot += 1
            ans = max(tot, ans)
            #print(ans)
        return ans
