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
            return self.threeDigit(num)
        elif len(num) == 2:
            return self.twoDigit(num)
        else:
            return self.oneDigit(num)

    def twoDigit(self, num):
        twoDigit = ["Ten", "Eleven", "Twelve", "Thirteen","Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        hund = ["Twenty", "Thirty","Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        ans = []
        if num[0] == "1":
            ans.append(twoDigit[int(num) - 10])
        else:              
            ans.append(hund[int(num[0]) - 2])
            if num[1] != "0":
                ans.append(self.oneDigit(num[1]))
        x = " ".join(ans)
        return x

    def oneDigit(self, num):
        onesDigit = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven","Eight","Nine"]
        return onesDigit[int(num)]

    def threeDigit(self, num):
        ans = [self.oneDigit(num[0]), "Hundred"]
        if num[1] != "0":
            ans.append(self.twoDigit(num[1:]))
        elif num[2] != "0":
            ans.append(self.oneDigit(num[2:]))
        return " ".join(ans)
