n = int(input())


def function(n):
    for i in range(n):
        string = str(input())
        correct = {"0"}
        length = len(string)
        if length == 1:
            print(string)
            continue
        l, r = 0, 0
        while r < length:
            l = r + 1
            while l < length and string[l] == string[r]:
                l += 1
            if (l - r) % 2 == 1:
                correct.add(string[r])
            r = l
        correct = list(correct)
        correct.sort()
        print("".join(correct[1:]))


function(n)
