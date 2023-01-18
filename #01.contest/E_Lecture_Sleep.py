time = list(map(int, input().split(" ")))
lecture = list(map(int, input().split(" ")))
sleep = list(map(int, input().split(" ")))

def maximum(time, lecture, sleep):
    answer = 0
    for i, num in enumerate(lecture):
        if sleep[i] == 1:
            answer += num
            
    sums = 0
    for i in range(time[1]):
        if sleep[i] == 0:
            sums += lecture[i]
    maxi = sums if sleep[0] == 0 else 0
    
    for i in range(1, len(lecture) - time[1] + 1):
        if sleep[i - 1] == 0:
            sums -= lecture[i-1]
        if sleep[i + time[1]-1] == 0:
            sums += lecture[i + time[1]-1]
        maxi = max(maxi, sums)
    
    answer += maxi
    print(answer)
maximum(time, lecture, sleep)