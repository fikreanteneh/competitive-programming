# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    length = list(map(int, input().split(" ")))
    happy = input().split(" ")
    setA = set(input().split(" "))
    setB = set(input().split(" "))

def happieness(happy, setA, setB):
    answer = 0
    for i in happy:
        if i in setA: 
            answer += 1
        elif i in setB: 
            answer -= 1
    print(answer)
happieness(happy, setA, setB)
