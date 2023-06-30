class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def findGCD(y, x):
            while True:
                temp = y % x
                if not temp:
                    return x
                y, x = x, temp
        x = deck[0]
        deck = Counter(deck)
        gcd = deck[x]
        for i in deck.values():
            gcd = findGCD(max(gcd, i), min(gcd, i))
        
        if gcd > 1:
            return True
        return False