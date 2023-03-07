    def calc(n):
        if len(n) == 1:
            return int(n)
        n = sum(list(map(int, list(n))))
        return calc(str(n))
        
    return calc(n * k)
