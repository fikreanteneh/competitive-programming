class Solution:
    def intToRoman(self, num: int) -> str:
        roman = { 1: "I" ,4:"IV", 5:"V", 9:"IX", 10:"X", 40 : "XL", 50 : "L", 90: "XC", 100 : "C", 400 : "CD", 500 : "D",900 : "CM" ,1000 : "M"}
        nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        ans = ""
        while num > 0:
            for i in range(len(nums)-1, -1, -1):
                if num - nums[i] >= 0: break
            num -= nums[i]
            ans += (roman[nums[i]])
        return ans
            
                
            