class Solution:
    def numberToWords(self, num: int) -> str:
        print(num)
        if num == 0:
            return "Zero"
        num = str(num)
        j, i = len(num),0 
        thou = ["","Thousand", "Million", "Billion", "Trillion"]
        ans = []
        while j / 3 > 1:
            x = self.calculate(num[j-3: j])
            if x != "":
                if i > 0: ans.append(thou[i])
                ans.append(x)
            j -= 3
            i += 1
        if i > 0:ans.append(thou[i])
        ans.append(self.calculate(num[0: j]))
        ans.reverse()
        return " ".join(ans)
    
    def calculate(self, num):
        num = int(num)
        num = str(num)
        if num == "0":
            return ""
        if len(num) == 3:
            return self.hunds(num)
        elif len(num) == 2:
            return self.teens(num)
        else:
            return self.one(num)
    def teens(self, num):
        teens = ["Ten", "Eleven", "Twelve", "Thirteen","Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        hund = ["Twenty", "Thirty","Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        ans = []
        if num[0] == "1":
            ans.append(teens[int(num) - 10])
        else:              
            ans.append(hund[int(num[0]) - 2])
            if num[1] != "0":
                ans.append(self.one(num[1]))
        x = " ".join(ans)
        return x
    def one(self, num):
        ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven","Eight","Nine"]
        return ones[int(num)]
    def hunds(self, nums):
        ans = [self.one(nums[0]), "Hundred"]
        if nums[1] != "0":
            ans.append(self.teens(nums[1:]))
        elif nums[2] != "0":
            ans.append(self.one(nums[2:]))
        return " ".join(ans)
