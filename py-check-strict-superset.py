# Enter your code here. Read input from STDIN. Print output to STDOUT
superSet = list(map(int, input().split(" ")))
n = int(input())

def checker(n, superSet):
    superSet = set(superSet)
    length = len(superSet)
    for i in range(n):
        check = set(map(int, input().split(" ")))
        for j in check:
            if j not in superSet:
                print("False")
                return
        if len(check) >= length:
            print("False")
            return
    print("True")

checker(n, superSet)
