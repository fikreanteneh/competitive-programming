if __name__ == '__main__':
    n = int(input())
def pythonPrint(n):
    ans = [None] * n
    for i in range(1,n+1):
        ans[i-1] = str(i)
    print("".join(ans))
pythonPrint(n)
