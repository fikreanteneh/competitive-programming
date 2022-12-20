class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orders = {}
        for i, letter in enumerate(order):orders[letter] = i
        for i in range(1, len(words)):
            flag = False
            index, left, right = 0, words[i-1], words[i]
            l, r = len(left), len(right)
            x = min(l, r)
            while index < x and orders[right[index]] == orders[left[index]]:
                index +=1
            if index == l : continue
            elif index == r: return False
            elif orders[right[index]] < orders[left[index]]: return False
        return True