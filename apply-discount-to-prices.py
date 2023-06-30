class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence, discount = sentence.split(" "), discount/100
        for i, word in enumerate (sentence):
            if word[0] =="$" and word[1:].isnumeric():
                nums = int(word[1:])
                nums = (nums - (nums * discount))
                nums = "$" + str(round(nums, 2))
                if nums[-3] != ".": nums += "0"
                sentence[i] = nums
        print(sentence)
        return " ".join(sentence)
