# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

def blocking(t):
    for k in range(t):
        n = int(input())
        block = list(map(int, input().split(" ")))
        i, j = 0, n - 1
        stack = [float("inf")]
        flag = False
        while i < j:
            if block[i] >= block[j]:
                if block[i] > stack[-1]:
                    print("No")
                    flag = True
                    break
                stack.append(block[i])
                i += 1
            elif block[i] < block[j]:
                if block[j] > stack[-1]:
                    print("No")
                    flag = True
                    break
                stack.append(block[j])
                j -= 1
        if not flag: print("Yes")
blocking(t)
